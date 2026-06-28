#!/usr/bin/env python3
"""
validate-agents.py
Validates agents/<id>/ against the portable agent contract:
- AGENT.md frontmatter with name (==dir, ^[a-z0-9-]+$), description, tools, model
- agent.json with id, platforms, and linkedSkills that exist in skills/
"""

import sys
import json
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import (  # noqa: E402
    GREEN, RED, BLUE, NC,
    NAME_RE, FRONTMATTER_MAX,
    parse_frontmatter, frontmatter_block, find_agent_dirs, find_skill_dirs,
)


def validate_agent(agent_path: Path, known_skills: set) -> list[str]:
    errors = []
    dir_name = agent_path.name
    for req in ['AGENT.md', 'agent.json']:
        if not (agent_path / req).exists():
            errors.append(f"Missing {req}")

    am = agent_path / 'AGENT.md'
    if am.exists():
        text = am.read_text(encoding='utf-8')
        fields, _, _ = parse_frontmatter(text)
        block = frontmatter_block(text)
        if fields is None:
            errors.append("AGENT.md has no frontmatter")
        else:
            name = fields.get('name', '')
            if not NAME_RE.match(name):
                errors.append(f"name '{name}' must match ^[a-z0-9-]+$")
            if name != dir_name:
                errors.append(f"name '{name}' != dir '{dir_name}'")
            for f in ['description', 'tools', 'model']:
                if not fields.get(f):
                    errors.append(f"frontmatter missing '{f}'")
            if len(block) > FRONTMATTER_MAX:
                errors.append(f"frontmatter {len(block)} > {FRONTMATTER_MAX}")

    aj = agent_path / 'agent.json'
    if aj.exists():
        try:
            meta = json.loads(aj.read_text(encoding='utf-8'))
        except json.JSONDecodeError as e:
            errors.append(f"agent.json invalid JSON: {e}")
            meta = None
        if meta is not None:
            if meta.get('id') != dir_name:
                errors.append(f"agent.json id != dir '{dir_name}'")
            if not meta.get('platforms'):
                errors.append("agent.json missing 'platforms'")
            for sk in meta.get('linkedSkills', []):
                if sk not in known_skills:
                    errors.append(f"linkedSkill '{sk}' not found in skills/")
    return errors


def main():
    ap = argparse.ArgumentParser(description='Validate agents')
    ap.add_argument('--strict', action='store_true')
    args = ap.parse_args()

    repo_root = Path(__file__).parent.parent
    agents_root = repo_root / 'agents'
    skills_root = repo_root / 'skills'
    known = {p.name for p in find_skill_dirs(skills_root)}

    paths = find_agent_dirs(agents_root)
    print(f"\n{BLUE}🔍 Validating {len(paths)} agent(s)...{NC}\n")
    total = 0
    for p in paths:
        errs = validate_agent(p, known)
        if errs:
            print(f"{RED}❌ {p.name}{NC}")
            for e in errs:
                print(f"   • {e}")
            total += len(errs)
        else:
            print(f"{GREEN}✓  {p.name}{NC}")
    print()
    if total == 0:
        print(f"{GREEN}✅ All agents valid!{NC}\n")
        sys.exit(0)
    print(f"{RED}❌ {total} error(s).{NC}\n")
    sys.exit(1)


if __name__ == '__main__':
    main()
