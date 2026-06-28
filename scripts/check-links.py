#!/usr/bin/env python3
"""
check-links.py
Falha (exit 1) se qualquer SKILL.md / AGENT.md / README.md / arquivo de apoio referenciar
um arquivo relativo que NÃO existe — garante o "embasamento" prometido (sem links mortos).

Verifica:
- Links markdown: [texto](caminho-relativo)
- Menções a arquivos de referência em prosa: `references/x.md`, `algo-tools.md`, `*.md`/`*.ts`/`*.json`
  citados em crase (`...`).
Ignora: http(s)://, mailto:, âncoras (#...), caminhos absolutos.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import GREEN, YELLOW, RED, BLUE, NC  # noqa: E402

REPO = Path(__file__).parent.parent
SCAN_DIRS = ['skills', 'agents', 'templates', 'docs']
SCAN_EXT = {'.md'}

MD_LINK = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
# crase contendo um caminho de arquivo com extensão conhecida
BACKTICK_PATH = re.compile(r'`([^`\n]+?\.(?:md|ts|js|json|py|sh|mdc|txt))`')

EXT_OK = ('.md', '.ts', '.js', '.json', '.py', '.sh', '.mdc', '.txt')


def is_external(target: str) -> bool:
    t = target.strip()
    return (
        t.startswith('http://') or t.startswith('https://') or t.startswith('mailto:')
        or t.startswith('#') or t.startswith('/') or t.startswith('~')
        or t.startswith('<') or '$' in t or '*' in t
    )


def candidates(text: str):
    for m in MD_LINK.finditer(text):
        yield m.group(1).split('#')[0].strip(), 'link'
    for m in BACKTICK_PATH.finditer(text):
        yield m.group(1).split('#')[0].strip(), 'ref'


def main():
    strict_refs = '--refs' in sys.argv  # também valida menções em crase (mais rígido)
    broken = []
    checked = 0
    for d in SCAN_DIRS:
        root = REPO / d
        if not root.exists():
            continue
        for f in root.rglob('*'):
            if f.suffix not in SCAN_EXT or not f.is_file():
                continue
            text = f.read_text(encoding='utf-8', errors='ignore')
            for target, kind in candidates(text):
                if kind == 'ref' and not strict_refs:
                    continue
                if is_external(target) or not target:
                    continue
                if not target.endswith(EXT_OK):
                    continue
                resolved = (f.parent / target).resolve()
                checked += 1
                if not resolved.exists():
                    broken.append((str(f.relative_to(REPO)), target, kind))

    print(f"\n{BLUE}🔗 Verificando links relativos ({checked} alvos){NC}\n")
    if not broken:
        print(f"{GREEN}✅ Nenhum link quebrado.{NC}\n")
        sys.exit(0)
    print(f"{RED}❌ {len(broken)} link(s) quebrado(s):{NC}")
    for src, tgt, kind in broken:
        print(f"   • [{kind}] {src} → {tgt}")
    print(f"\n{YELLOW}Dica: crie o arquivo de apoio ou corrija o caminho. "
          f"Use --refs para também validar menções em crase.{NC}\n")
    sys.exit(1)


if __name__ == '__main__':
    main()
