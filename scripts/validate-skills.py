#!/usr/bin/env python3
"""
validate-skills.py
Validates every skill against the canonical multiplatform contract:
- SKILL.md with YAML frontmatter containing ONLY name + description
- frontmatter block <= 1024 chars; name matches ^[a-z0-9-]+$ and == dir name
- sibling skill.json with valid category/status/type and platforms block
See skills/meta/multiplatform-authoring for the rule this enforces.
"""

import sys
import json
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import (  # noqa: E402
    GREEN, YELLOW, RED, BLUE, NC,
    VALID_CATEGORIES, VALID_STATUSES, VALID_TYPES, PLATFORMS,
    NAME_RE, FRONTMATTER_MAX,
    parse_frontmatter, frontmatter_block, find_skill_dirs, duplicates,
)

REQUIRED_FILES = ['SKILL.md', 'README.md', 'skill.json']


def validate_skill(skill_path: Path) -> list[str]:
    errors = []
    dir_name = skill_path.name
    category = skill_path.parent.name

    for req in REQUIRED_FILES:
        if not (skill_path / req).exists():
            errors.append(f"Missing required file: {req}")

    skill_md = skill_path / 'SKILL.md'
    if skill_md.exists():
        text = skill_md.read_text(encoding='utf-8')
        fields, _, _ = parse_frontmatter(text)
        block = frontmatter_block(text)
        if fields is None:
            errors.append("SKILL.md has no YAML frontmatter (--- ... ---)")
        else:
            if 'name' not in fields:
                errors.append("frontmatter missing 'name'")
            else:
                name = fields['name']
                if not NAME_RE.match(name):
                    errors.append(f"name '{name}' must match ^[a-z0-9-]+$")
                if name != dir_name:
                    errors.append(f"name '{name}' must equal dir name '{dir_name}'")
            if 'description' not in fields or not fields['description']:
                errors.append("frontmatter missing 'description'")
            extra = set(fields) - {'name', 'description'}
            if extra:
                errors.append(f"frontmatter has extra fields {sorted(extra)} (move to skill.json)")
            if len(block) > FRONTMATTER_MAX:
                errors.append(f"frontmatter block {len(block)} chars > {FRONTMATTER_MAX}")

    sj = skill_path / 'skill.json'
    if sj.exists():
        try:
            meta = json.loads(sj.read_text(encoding='utf-8'))
        except json.JSONDecodeError as e:
            errors.append(f"skill.json invalid JSON: {e}")
            meta = None
        if meta is not None:
            if meta.get('id') != dir_name:
                errors.append(f"skill.json id '{meta.get('id')}' != dir '{dir_name}'")
            if meta.get('category') not in VALID_CATEGORIES:
                errors.append(f"skill.json category '{meta.get('category')}' invalid")
            elif meta.get('category') != category:
                errors.append(f"skill.json category '{meta.get('category')}' != folder '{category}'")
            if meta.get('status') not in VALID_STATUSES:
                errors.append(f"skill.json status '{meta.get('status')}' invalid")
            if meta.get('type') not in VALID_TYPES:
                errors.append(f"skill.json type '{meta.get('type')}' invalid")
            plats = meta.get('platforms', {})
            missing = [p for p in PLATFORMS if p not in plats]
            if missing:
                errors.append(f"skill.json platforms missing: {missing}")
    return errors


def main():
    ap = argparse.ArgumentParser(description='Validate skills (canonical multiplatform format)')
    ap.add_argument('--skill', default=None, help='e.g. core/judicial-monitoring')
    ap.add_argument('--strict', action='store_true')
    args = ap.parse_args()

    repo_root = Path(__file__).parent.parent
    skills_root = repo_root / 'skills'
    if not skills_root.exists():
        print(f"{RED}❌ skills/ not found{NC}")
        sys.exit(1)

    if args.skill:
        paths = [skills_root / args.skill]
        if not paths[0].exists():
            print(f"{RED}❌ Skill not found: {args.skill}{NC}")
            sys.exit(1)
    else:
        paths = find_skill_dirs(skills_root)

    print(f"\n{BLUE}🔍 Validating {len(paths)} skill(s)...{NC}\n")
    total = 0
    for p in paths:
        rel = p.relative_to(skills_root)
        errs = validate_skill(p)
        if errs:
            print(f"{RED}❌ {rel}{NC}")
            for e in errs:
                print(f"   • {e}")
            total += len(errs)
        else:
            print(f"{GREEN}✓  {rel}{NC}")

    # ── Duplicate guard (regra inviolável: sem duplicados) ──
    if not args.skill:
        all_dirs = find_skill_dirs(skills_root)
        dup_ids = duplicates([d.name for d in all_dirs])
        if dup_ids:
            print(f"\n{RED}❌ Skill IDs duplicados (proibido):{NC}")
            for sid, c in sorted(dup_ids.items()):
                locs = [str(d.relative_to(skills_root)) for d in all_dirs if d.name == sid]
                print(f"   • '{sid}' aparece {c}x: {locs}")
            total += len(dup_ids)
        names = []
        for d in all_dirs:
            f, _, _ = parse_frontmatter((d / 'SKILL.md').read_text(encoding='utf-8'))
            if f and f.get('name'):
                names.append(f['name'])
        dup_names = duplicates(names)
        if dup_names:
            print(f"\n{RED}❌ Nomes de skill duplicados no frontmatter:{NC}")
            for n, c in sorted(dup_names.items()):
                print(f"   • '{n}' aparece {c}x")
            total += len(dup_names)

    print()
    if total == 0:
        print(f"{GREEN}✅ All skills valid!{NC}\n")
        sys.exit(0)
    print(f"{RED}❌ {total} error(s).{NC}\n")
    sys.exit(1)


if __name__ == '__main__':
    main()
