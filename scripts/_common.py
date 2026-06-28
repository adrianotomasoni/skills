#!/usr/bin/env python3
"""
_common.py
Shared helpers for skill/agent tooling. No third-party dependencies
(simple YAML frontmatter parsing for the minimal `name`/`description` schema).
"""

import json
import re
from pathlib import Path

VALID_CATEGORIES = ['core', 'frontend', 'content', 'engineering', 'tools', 'process', 'meta']
VALID_STATUSES = ['stable', 'beta', 'experimental', 'deprecated']
VALID_TYPES = ['technique', 'pattern', 'reference']
PLATFORMS = ['claude', 'claude-code', 'openai', 'gemini', 'cursor', 'copilot', 'codex', 'manus']
NAME_RE = re.compile(r'^[a-z0-9-]+$')
FRONTMATTER_MAX = 1024

# ANSI colors
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
BLUE = '\033[0;34m'
NC = '\033[0m'


def parse_frontmatter(text: str):
    """Parse a leading YAML frontmatter block.

    Returns (fields: dict, raw_block: str, body: str) or (None, '', text).
    Supports the minimal schema: flat `key: value` lines, optionally quoted.
    """
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', text, re.S)
    if not m:
        return None, '', text
    raw_inner, body = m.group(1), m.group(2)
    raw_block = text[:m.start(2)] if m.start(2) else m.group(0)
    fields = {}
    key = None
    for line in raw_inner.splitlines():
        if re.match(r'^[A-Za-z_][\w-]*:', line):
            key, _, val = line.partition(':')
            key = key.strip()
            val = val.strip()
            if len(val) >= 2 and val[0] in '"\'' and val[-1] == val[0]:
                val = val[1:-1]
            fields[key] = val
        elif key and line.strip():
            # continuation of a folded value
            fields[key] = (fields[key] + ' ' + line.strip()).strip()
    return fields, raw_block, body


def frontmatter_block(text: str) -> str:
    """Return the raw frontmatter block (including --- fences) or ''."""
    m = re.match(r'^---\n.*?\n---', text, re.S)
    return m.group(0) if m else ''


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception as e:  # noqa: BLE001
        return None, str(e)


def find_skill_dirs(skills_root: Path):
    """All <category>/<id> directories that contain a SKILL.md."""
    skills = []
    for category_dir in sorted(skills_root.iterdir()):
        if not category_dir.is_dir() or category_dir.name.startswith('.'):
            continue
        for skill_dir in sorted(category_dir.iterdir()):
            if not skill_dir.is_dir() or skill_dir.name.startswith('.'):
                continue
            if (skill_dir / 'SKILL.md').exists():
                skills.append(skill_dir)
    return skills


def find_agent_dirs(agents_root: Path):
    if not agents_root.exists():
        return []
    out = []
    for d in sorted(agents_root.iterdir()):
        if not d.is_dir() or d.name.startswith('.') or d.name == '_template':
            continue
        if (d / 'AGENT.md').exists():
            out.append(d)
    return out
