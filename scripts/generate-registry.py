#!/usr/bin/env python3
"""
generate-registry.py
Generates registry.json (schema 2.0.0) from canonical skills + agents.
Reads name/description from SKILL.md frontmatter and metadata from skill.json.
"""

import sys
import json
import argparse
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import (  # noqa: E402
    GREEN, YELLOW, BLUE, NC,
    parse_frontmatter, find_skill_dirs, find_agent_dirs,
)

REPO_URL = 'https://github.com/adrianotomasoni/skills'
MAINTAINER = 'adriano@traderisk.com.br'


def skill_entry(skill_path: Path, skills_root: Path):
    text = (skill_path / 'SKILL.md').read_text(encoding='utf-8')
    fields, _, _ = parse_frontmatter(text)
    fields = fields or {}
    meta = {}
    sj = skill_path / 'skill.json'
    if sj.exists():
        try:
            meta = json.loads(sj.read_text(encoding='utf-8'))
        except json.JSONDecodeError:
            meta = {}
    skill_id = fields.get('name') or meta.get('id') or skill_path.name
    return {
        'id': skill_id,
        'category': skill_path.parent.name,
        'name': meta.get('name', skill_id),
        'version': meta.get('version', '1.0.0'),
        'status': meta.get('status', 'stable'),
        'type': meta.get('type', 'technique'),
        'description': fields.get('description', ''),
        'path': str(skill_path.relative_to(skills_root.parent)),
        'file': 'SKILL.md',
        'tags': meta.get('tags', []),
        'dependencies': meta.get('dependencies', []),
        'platforms': meta.get('platforms', {}),
        'maintainer': meta.get('maintainer', MAINTAINER),
    }


def agent_entry(agent_path: Path, repo_root: Path):
    text = (agent_path / 'AGENT.md').read_text(encoding='utf-8')
    fields, _, _ = parse_frontmatter(text)
    fields = fields or {}
    meta = {}
    aj = agent_path / 'agent.json'
    if aj.exists():
        try:
            meta = json.loads(aj.read_text(encoding='utf-8'))
        except json.JSONDecodeError:
            meta = {}
    agent_id = fields.get('name') or meta.get('id') or agent_path.name
    return {
        'id': agent_id,
        'name': meta.get('name', agent_id),
        'version': meta.get('version', '1.0.0'),
        'status': meta.get('status', 'stable'),
        'description': fields.get('description', ''),
        'path': str(agent_path.relative_to(repo_root)),
        'file': 'AGENT.md',
        'tools': fields.get('tools', ''),
        'model': fields.get('model', 'inherit'),
        'linkedSkills': meta.get('linkedSkills', []),
        'platforms': meta.get('platforms', {}),
        'maintainer': meta.get('maintainer', MAINTAINER),
    }


def main():
    ap = argparse.ArgumentParser(description='Generate registry.json (2.0.0)')
    ap.add_argument('--summary', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    repo_root = Path(__file__).parent.parent
    skills_root = repo_root / 'skills'
    agents_root = repo_root / 'agents'
    registry_path = repo_root / 'registry.json'

    print(f"\n{BLUE}📦 Generating registry.json (2.0.0)...{NC}\n")

    skills = []
    for p in find_skill_dirs(skills_root):
        e = skill_entry(p, skills_root)
        skills.append(e)
        warn = '' if e['description'] else f" {YELLOW}(empty description!){NC}"
        print(f"{GREEN}✓{NC}  skill: {e['id']} ({e['category']}) v{e['version']}{warn}")

    agents = []
    for p in find_agent_dirs(agents_root):
        e = agent_entry(p, repo_root)
        agents.append(e)
        print(f"{GREEN}✓{NC}  agent: {e['id']} v{e['version']}")

    registry = {
        'version': '2.0.0',
        'lastUpdated': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'repository': REPO_URL,
        'maintainer': MAINTAINER,
        'counts': {'skills': len(skills), 'agents': len(agents)},
        'skills': sorted(skills, key=lambda x: (x['category'], x['id'])),
        'agents': sorted(agents, key=lambda x: x['id']),
    }
    output = json.dumps(registry, ensure_ascii=False, indent=2)

    if args.dry_run:
        print(f"\n{YELLOW}--- DRY RUN ---{NC}\n")
        print(output)
    else:
        registry_path.write_text(output + '\n', encoding='utf-8')
        print(f"\n{GREEN}✅ registry.json: {len(skills)} skills, {len(agents)} agents{NC}")

    if args.summary:
        cats = {}
        for s in skills:
            cats[s['category']] = cats.get(s['category'], 0) + 1
        print(f"\n{BLUE}📊 By category:{NC}")
        for c, n in sorted(cats.items()):
            print(f"    {c}: {n}")
        empty = [s['id'] for s in skills if not s['description']]
        if empty:
            print(f"\n{YELLOW}⚠ skills with empty description: {empty}{NC}")
        print()


if __name__ == '__main__':
    main()
