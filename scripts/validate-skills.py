#!/usr/bin/env python3
"""
validate-skills.py
Validates all skills in the repository against required structure.
"""

import os
import sys
import json
import argparse
from pathlib import Path

REQUIRED_FILES = ['SKILL.md', 'README.md']
REQUIRED_SKILL_FIELDS = ['# ID:', '# Version:', '# Category:', '# Status:']
VALID_CATEGORIES = ['core', 'frontend', 'content', 'engineering', 'tools']
VALID_STATUSES = ['stable', 'beta', 'experimental', 'deprecated']

# ANSI colors
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
BLUE = '\033[0;34m'
NC = '\033[0m'


def validate_skill(skill_path: Path) -> list[str]:
    """Validate a single skill directory. Returns list of errors."""
    errors = []

    # Check required files
    for req_file in REQUIRED_FILES:
        if not (skill_path / req_file).exists():
            errors.append(f"Missing required file: {req_file}")

    # Validate SKILL.md content
    skill_md = skill_path / 'SKILL.md'
    if skill_md.exists():
        content = skill_md.read_text(encoding='utf-8')

        for field in REQUIRED_SKILL_FIELDS:
            if field not in content:
                errors.append(f"SKILL.md missing field: {field}")

        # Validate category
        for line in content.splitlines():
            if line.startswith('# Category:'):
                category = line.split(':', 1)[1].strip()
                if category not in VALID_CATEGORIES:
                    errors.append(
                        f"Invalid category '{category}'. "
                        f"Valid: {', '.join(VALID_CATEGORIES)}"
                    )

            if line.startswith('# Status:'):
                status = line.split(':', 1)[1].strip()
                if status not in VALID_STATUSES:
                    errors.append(
                        f"Invalid status '{status}'. "
                        f"Valid: {', '.join(VALID_STATUSES)}"
                    )

    return errors


def find_skills(skills_root: Path) -> list[Path]:
    """Find all skill directories (those containing SKILL.md or README.md)."""
    skills = []
    for category_dir in skills_root.iterdir():
        if not category_dir.is_dir() or category_dir.name.startswith('.'):
            continue
        for skill_dir in category_dir.iterdir():
            if not skill_dir.is_dir() or skill_dir.name.startswith('.'):
                continue
            skills.append(skill_dir)
    return sorted(skills)


def main():
    parser = argparse.ArgumentParser(description='Validate skills in the repository')
    parser.add_argument(
        '--skill',
        help='Validate a specific skill (e.g., core/judicial-monitoring)',
        default=None,
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Exit with error code if any warnings found',
    )
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent
    skills_root = repo_root / 'skills'

    if not skills_root.exists():
        print(f"{RED}❌ Skills directory not found: {skills_root}{NC}")
        sys.exit(1)

    if args.skill:
        skill_paths = [skills_root / args.skill]
        missing = [p for p in skill_paths if not p.exists()]
        if missing:
            print(f"{RED}❌ Skill not found: {args.skill}{NC}")
            sys.exit(1)
    else:
        skill_paths = find_skills(skills_root)

    print(f"\n{BLUE}🔍 Validating {len(skill_paths)} skill(s)...{NC}\n")

    total_errors = 0
    for skill_path in skill_paths:
        relative = skill_path.relative_to(skills_root)
        errors = validate_skill(skill_path)

        if errors:
            print(f"{RED}❌ {relative}{NC}")
            for err in errors:
                print(f"   • {err}")
            total_errors += len(errors)
        else:
            print(f"{GREEN}✓  {relative}{NC}")

    print()
    if total_errors == 0:
        print(f"{GREEN}✅ All skills valid! No errors found.{NC}\n")
        sys.exit(0)
    else:
        print(f"{RED}❌ Found {total_errors} error(s). Please fix before committing.{NC}\n")
        sys.exit(1)


if __name__ == '__main__':
    main()
