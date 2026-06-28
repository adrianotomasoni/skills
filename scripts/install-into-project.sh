#!/bin/bash
# scripts/install-into-project.sh
# Instala uma skill ou um agente deste repo-mãe dentro de um projeto-alvo,
# para que você possa invocá-lo em qualquer novo projeto.
#
# Uso:
#   ./scripts/install-into-project.sh --agent buscador-sgj --target ../meu-projeto
#   ./scripts/install-into-project.sh --skill credit-risk-analysis --target ../meu-projeto
#   ./scripts/install-into-project.sh --all --target ../meu-projeto
#
# O que faz no projeto-alvo:
#   - skills  -> <target>/.claude/skills/<id>/      (Claude Code / Codex / Gemini / Copilot)
#   - agentes -> <target>/.claude/agents/<id>.md    (Claude Code subagent) + bundle em
#                <target>/.claude/agents/<id>/ (reference/, examples/, etc., se existirem)
#   - Cursor  -> <target>/.cursor/rules/<id>.mdc    (via export-adapters)
set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; BLUE='\033[0;34m'; NC='\033[0m'

KIND=""; ID=""; TARGET=""; ALL=0
while [ $# -gt 0 ]; do
  case "$1" in
    --skill) KIND="skill"; ID="$2"; shift 2;;
    --agent) KIND="agent"; ID="$2"; shift 2;;
    --all) ALL=1; shift;;
    --target) TARGET="$2"; shift 2;;
    *) echo -e "${RED}Arg desconhecido: $1${NC}"; exit 1;;
  esac
done

if [ -z "$TARGET" ]; then echo -e "${RED}❌ --target é obrigatório${NC}"; exit 1; fi
mkdir -p "$TARGET/.claude/skills" "$TARGET/.claude/agents" "$TARGET/.cursor/rules"

install_skill() {
  local sid="$1"
  local src
  src=$(find "$REPO_ROOT/skills" -maxdepth 2 -type d -name "$sid" | head -1)
  if [ -z "$src" ]; then echo -e "${RED}  ✗ skill '$sid' não encontrada${NC}"; return 1; fi
  rm -rf "$TARGET/.claude/skills/$sid"; cp -r "$src" "$TARGET/.claude/skills/$sid"
  echo -e "${GREEN}  ✓${NC} skill $sid → .claude/skills/$sid"
}

install_agent() {
  local aid="$1"
  local src="$REPO_ROOT/agents/$aid"
  if [ ! -f "$src/AGENT.md" ]; then echo -e "${RED}  ✗ agente '$aid' não encontrado${NC}"; return 1; fi
  cp "$src/AGENT.md" "$TARGET/.claude/agents/$aid.md"
  # bundle de apoio (reference/, examples/, docs/, schemas/) se existir
  rm -rf "$TARGET/.claude/agents/$aid"
  if compgen -G "$src/*/" > /dev/null; then
    mkdir -p "$TARGET/.claude/agents/$aid"
    for d in "$src"/*/; do
      bn=$(basename "$d"); [ "$bn" = "platforms" ] && continue
      cp -r "$d" "$TARGET/.claude/agents/$aid/$bn"
    done
  fi
  echo -e "${GREEN}  ✓${NC} agente $aid → .claude/agents/$aid.md"
}

echo -e "${BLUE}📦 Instalando em: $TARGET${NC}\n"
if [ "$ALL" = "1" ]; then
  for d in "$REPO_ROOT"/skills/*/*/; do [ -f "$d/SKILL.md" ] && install_skill "$(basename "$d")"; done
  for d in "$REPO_ROOT"/agents/*/; do
    bn=$(basename "$d"); [ "$bn" = "_template" ] && continue
    [ -f "$d/AGENT.md" ] && install_agent "$bn"
  done
elif [ "$KIND" = "skill" ]; then install_skill "$ID"
elif [ "$KIND" = "agent" ]; then install_agent "$ID"
else echo -e "${RED}❌ informe --skill <id>, --agent <id> ou --all${NC}"; exit 1; fi

# Cursor adapters (.mdc) — só para skills (agentes não têm adapter .mdc gerado)
if command -v python3 >/dev/null 2>&1; then
  python3 "$REPO_ROOT/scripts/export-adapters.py" --platform cursor >/dev/null 2>&1 || true
  copied_cursor=0
  if [ -d "$REPO_ROOT/dist/cursor" ]; then
    if [ "$ALL" = "1" ]; then
      cp "$REPO_ROOT"/dist/cursor/*.mdc "$TARGET/.cursor/rules/" 2>/dev/null && copied_cursor=1 || true
    elif [ "$KIND" = "skill" ] && [ -f "$REPO_ROOT/dist/cursor/$ID.mdc" ]; then
      cp "$REPO_ROOT/dist/cursor/$ID.mdc" "$TARGET/.cursor/rules/" && copied_cursor=1
    fi
  fi
  [ "$copied_cursor" = "1" ] && echo -e "${GREEN}  ✓${NC} regras Cursor → .cursor/rules/"
fi

echo -e "\n${GREEN}✅ Concluído.${NC}"
echo -e "${YELLOW}Claude Code:${NC} reabra o projeto; skills via ferramenta Skill, agentes via Agent."
