#!/usr/bin/env python3
"""
generate-registry.py
Generates registry.json from skill metadata found in SKILL.md files.
"""

import json
import os
import re
import sys
import argparse
from datetime import datetime, timezone
from pathlib import Path

# ANSI colors
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
NC = '\033[0m'


def parse_skill_metadata(skill_path: Path) -> dict | None:
    """Extract metadata from a SKILL.md file."""
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return None

    content = skill_md.read_text(encoding='utf-8')
    metadata = {}

    # Parse header fields (# Key: Value)
    for line in content.splitlines():
        line = line.strip()
        if not line.startswith('#'):
            break
        if ':' in line:
            key = line.lstrip('#').split(':')[0].strip().lower()
            value = line.split(':', 1)[1].strip()
            metadata[key] = value

    if not metadata.get('id'):
        return None

    # Parse tags from README.md if available
    tags = []
    readme = skill_path / 'README.md'
    if readme.exists():
        readme_content = readme.read_text(encoding='utf-8')
        tag_match = re.search(r'## Tags\s*\n\s*`([^`]+)`', readme_content)
        if tag_match:
            tags = [t.strip() for t in tag_match.group(1).split('`') if t.strip()]
        # Also look for inline tags like `tag1` `tag2`
        tag_line = re.search(r'## Tags\s*\n(.+)', readme_content)
        if tag_line:
            inline_tags = re.findall(r'`([^`]+)`', tag_line.group(1))
            tags = list(set(tags + inline_tags))

    # Get last modified from git or file mtime
    last_modified = datetime.now().strftime('%Y-%m-%d')

    # Build skill entry
    category = metadata.get('category', 'unknown')
    skill_id = metadata.get('id', skill_path.name)
    relative_path = f"skills/{category}/{skill_path.name}"

    return {
        'id': skill_id,
        'category': category,
        'name': _extract_name(content) or skill_id,
        'version': metadata.get('version', '1.0.0'),
        'description': _extract_description(content),
        'path': relative_path,
        'file': 'SKILL.md',
        'status': metadata.get('status', 'stable'),
        'tags': sorted(tags),
        'maintainer': _extract_maintainer(content),
        'lastModified': last_modified,
    }


def _extract_name(content: str) -> str:
    """Extract skill name from SKILL.md content."""
    for line in content.splitlines():
        if line.startswith('# Skill:'):
            return line.split(':', 1)[1].strip()
    return ''


def _extract_description(content: str) -> str:
    """Extract description from Objetivo section."""
    lines = content.splitlines()
    in_objetivo = False
    for line in lines:
        if line.startswith('## Objetivo'):
            in_objetivo = True
            continue
        if in_objetivo:
            line = line.strip()
            if line and not line.startswith('#'):
                # Remove markdown formatting
                line = re.sub(r'\*+', '', line)
                return line[:120]
            elif line.startswith('#'):
                break
    return ''


def _extract_maintainer(content: str) -> str:
    """Extract maintainer email from SKILL.md footer."""
    match = re.search(r'Maintainer\*\*:\s*([^\s|]+)', content)
    if match:
        return match.group(1).strip()
    return 'adriano@traderisk.com.br'


def find_skills(skills_root: Path) -> list[Path]:
    """Find all skill directories."""
    skills = []
    for category_dir in sorted(skills_root.iterdir()):
        if not category_dir.is_dir() or category_dir.name.startswith('.'):
            continue
        for skill_dir in sorted(category_dir.iterdir()):
            if not skill_dir.is_dir() or skill_dir.name.startswith('.'):
                continue
            skills.append(skill_dir)
    return skills


def main():
    parser = argparse.ArgumentParser(description='Generate registry.json from skill metadata')
    parser.add_argument('--summary', action='store_true', help='Print summary after generating')
    parser.add_argument('--dry-run', action='store_true', help='Print output without writing')
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent
    skills_root = repo_root / 'skills'
    registry_path = repo_root / 'registry.json'

    if not skills_root.exists():
        print(f"❌ Skills directory not found: {skills_root}")
        sys.exit(1)

    print(f"\n{BLUE}📦 Generating registry.json...{NC}\n")

    skill_entries = []
    skill_paths = find_skills(skills_root)

    for skill_path in skill_paths:
        entry = parse_skill_metadata(skill_path)
        if entry:
            skill_entries.append(entry)
            print(f"{GREEN}✓{NC}  {entry['id']} ({entry['category']}) v{entry['version']}")
        else:
            print(f"{YELLOW}⊘{NC}  {skill_path.name} – no SKILL.md metadata, skipped")

    registry = {
        'version': '1.0.0',
        'lastUpdated': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'repository': 'https://github.com/adrianotomasoni/skills',
        'maintainer': 'adriano@traderisk.com.br',
        'skills': skill_entries,
    }

    output = json.dumps(registry, ensure_ascii=False, indent=2)

    if args.dry_run:
        print(f"\n{YELLOW}--- DRY RUN OUTPUT ---{NC}\n")
        print(output)
    else:
        registry_path.write_text(output + '\n', encoding='utf-8')
        print(f"\n{GREEN}✅ registry.json updated with {len(skill_entries)} skill(s){NC}")

    if args.summary:
        print(f"\n{BLUE}📊 Summary:{NC}")
        categories: dict[str, int] = {}
        statuses: dict[str, int] = {}
        for entry in skill_entries:
            categories[entry['category']] = categories.get(entry['category'], 0) + 1
            statuses[entry['status']] = statuses.get(entry['status'], 0) + 1

        print("\n  By category:")
        for cat, count in sorted(categories.items()):
            print(f"    {cat}: {count}")

        print("\n  By status:")
        for status, count in sorted(statuses.items()):
            print(f"    {status}: {count}")
        print()


if __name__ == '__main__':
    main()
