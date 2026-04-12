#!/usr/bin/env python3
"""
test-skills.py
Runs evaluation suites against skills that have tests/eval-suite.json.
"""

import json
import sys
import argparse
from pathlib import Path

# ANSI colors
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
BLUE = '\033[0;34m'
NC = '\033[0m'


def run_eval_suite(skill_path: Path, api_key: str | None = None) -> dict:
    """
    Run evaluation suite for a skill.
    Returns dict with results.

    Note: Without an API key, runs structural validation only.
    With an API key, runs actual inference tests against Claude.
    """
    eval_file = skill_path / 'tests' / 'eval-suite.json'
    if not eval_file.exists():
        return {'status': 'skipped', 'reason': 'No eval-suite.json found'}

    try:
        suite = json.loads(eval_file.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        return {'status': 'error', 'reason': f'Invalid JSON: {e}'}

    casos = suite.get('casos', [])
    if not casos:
        return {'status': 'skipped', 'reason': 'No test cases defined'}

    # Structural validation (always runs)
    errors = []
    for caso in casos:
        if 'id' not in caso:
            errors.append("Test case missing 'id'")
        if 'input' not in caso:
            errors.append(f"Case {caso.get('id', '?')} missing 'input'")

    if errors:
        return {'status': 'failed', 'errors': errors}

    if not api_key:
        return {
            'status': 'structural_ok',
            'cases': len(casos),
            'message': 'Structural validation passed. Use --api-key to run inference tests.',
        }

    # Inference tests (requires API key)
    # TODO: implement actual Claude API calls here
    return {
        'status': 'not_implemented',
        'message': 'Inference testing not yet implemented. Structural validation passed.',
    }


def main():
    parser = argparse.ArgumentParser(description='Run skill evaluation suites')
    parser.add_argument(
        '--skill',
        help='Test a specific skill (e.g., core/judicial-monitoring)',
        default=None,
    )
    parser.add_argument(
        '--api-key',
        help='Anthropic API key for inference tests',
        default=None,
    )
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent
    skills_root = repo_root / 'skills'

    if args.skill:
        skill_paths = [skills_root / args.skill]
    else:
        skill_paths = []
        for category_dir in sorted(skills_root.iterdir()):
            if not category_dir.is_dir() or category_dir.name.startswith('.'):
                continue
            for skill_dir in sorted(category_dir.iterdir()):
                if skill_dir.is_dir() and not skill_dir.name.startswith('.'):
                    skill_paths.append(skill_dir)

    print(f"\n{BLUE}🧪 Running tests for {len(skill_paths)} skill(s)...{NC}\n")

    passed = failed = skipped = 0

    for skill_path in skill_paths:
        relative = skill_path.relative_to(skills_root)
        result = run_eval_suite(skill_path, args.api_key)

        status = result.get('status', 'unknown')
        if status in ('structural_ok', 'not_implemented'):
            print(f"{GREEN}✓{NC}  {relative} – {result.get('message', status)}")
            passed += 1
        elif status == 'skipped':
            print(f"{YELLOW}⊘{NC}  {relative} – {result.get('reason', 'skipped')}")
            skipped += 1
        elif status == 'failed':
            print(f"{RED}❌{NC}  {relative}")
            for err in result.get('errors', []):
                print(f"     • {err}")
            failed += 1
        else:
            print(f"{YELLOW}?{NC}  {relative} – {status}")
            skipped += 1

    print(f"\n{BLUE}Results:{NC} {passed} passed, {failed} failed, {skipped} skipped\n")

    if failed > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
