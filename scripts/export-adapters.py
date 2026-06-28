#!/usr/bin/env python3
"""
export-adapters.py
Generates per-platform adapters from the canonical skills into dist/<platform>/.

Adaptation rules (see skills/meta/multiplatform-authoring/references/):
- claude, claude-code, gemini, copilot, codex: keep frontmatter (copy as-is).
- openai, manus: STRIP frontmatter -> description becomes a preamble.
- cursor: convert to .mdc rule (description + globs/alwaysApply, then body).

dist/ is gitignored; never edit dist/ by hand.
"""

import sys
import shutil
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import (  # noqa: E402
    GREEN, YELLOW, BLUE, NC,
    parse_frontmatter, find_skill_dirs,
)

KEEP_FM = ['claude', 'claude-code', 'gemini', 'copilot', 'codex']
STRIP_FM = ['openai', 'manus']
ALWAYS_APPLY = {'multiplatform-authoring', 'using-superpowers'}


def strip_adapter(name, desc, body):
    title = name.replace('-', ' ').title()
    return f"# {title}\n\nUse esta skill quando: {desc}\n\n{body.lstrip()}"


def cursor_adapter(name, desc, body):
    apply = 'true' if name in ALWAYS_APPLY else 'false'
    return (f"---\ndescription: {desc}\nglobs:\nalwaysApply: {apply}\n---\n\n{body.lstrip()}")


def main():
    ap = argparse.ArgumentParser(description='Export per-platform adapters')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--platform', default=None, help='only this platform')
    args = ap.parse_args()

    repo_root = Path(__file__).parent.parent
    skills_root = repo_root / 'skills'
    dist = repo_root / 'dist'
    targets = ([args.platform] if args.platform else KEEP_FM + STRIP_FM + ['cursor'])

    skills = find_skill_dirs(skills_root)
    print(f"\n{BLUE}📤 Exporting {len(skills)} skills → {len(targets)} platform(s){NC}\n")

    for plat in targets:
        out_dir = dist / plat
        count = 0
        for sp in skills:
            text = (sp / 'SKILL.md').read_text(encoding='utf-8')
            fields, _, body = parse_frontmatter(text)
            fields = fields or {}
            name = fields.get('name', sp.name)
            desc = fields.get('description', '')

            if plat in KEEP_FM:
                # copy whole skill dir (frontmatter preserved)
                dest = out_dir / sp.parent.name / name
                content = None
            elif plat in STRIP_FM:
                dest = out_dir / f"{name}.md"
                content = strip_adapter(name, desc, body)
            elif plat == 'cursor':
                dest = out_dir / f"{name}.mdc"
                content = cursor_adapter(name, desc, body)
            else:
                continue

            if args.dry_run:
                kind = 'copy-dir' if content is None else 'write'
                print(f"  {YELLOW}[{plat}]{NC} {kind} → {dest.relative_to(repo_root)}")
            else:
                if content is None:
                    if dest.exists():
                        shutil.rmtree(dest)
                    shutil.copytree(sp, dest)
                else:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_text(content, encoding='utf-8')
            count += 1
        print(f"{GREEN}✓{NC} {plat}: {count} skills")

    if args.dry_run:
        print(f"\n{YELLOW}(dry-run, nothing written){NC}")
    else:
        print(f"\n{GREEN}✅ Adapters in dist/{NC}")
    print()


if __name__ == '__main__':
    main()
