#!/bin/bash
# scripts/sync-to-claude.sh
# Instala as skills (e agentes) deste repo no Claude Code.
#   skills -> ~/.claude/skills/<id>/      (namespace plano por id)
#   agents -> ~/.claude/agents/<id>.md
# Claude Code NÃO lê o alias ~/.agents/skills/ — por isso o destino é ~/.claude.

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_SRC="$REPO_ROOT/skills"
AGENTS_SRC="$REPO_ROOT/agents"
CLAUDE_SKILLS="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
CLAUDE_AGENTS="${CLAUDE_AGENTS_DIR:-$HOME/.claude/agents}"

GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; BLUE='\033[0;34m'; NC='\033[0m'

echo -e "${BLUE}📦 Sincronizando skills/agentes para Claude Code...${NC}\n"

if [ ! -d "$SKILLS_SRC" ]; then
  echo -e "${RED}❌ skills/ não encontrado: $SKILLS_SRC${NC}"; exit 1
fi

mkdir -p "$CLAUDE_SKILLS" "$CLAUDE_AGENTS"

skill_count=0
for category_dir in "$SKILLS_SRC"/*/; do
  [ -d "$category_dir" ] || continue
  for skill_dir in "$category_dir"*/; do
    [ -f "$skill_dir/SKILL.md" ] || continue
    skill_id=$(basename "$skill_dir")
    dst="$CLAUDE_SKILLS/$skill_id"
    rm -rf "$dst"
    cp -r "$skill_dir" "$dst"
    echo -e "${GREEN}  ✓${NC} skill: $skill_id"
    ((skill_count++))
  done
done

agent_count=0
if [ -d "$AGENTS_SRC" ]; then
  for agent_dir in "$AGENTS_SRC"/*/; do
    [ -f "$agent_dir/AGENT.md" ] || continue
    agent_id=$(basename "$agent_dir")
    [ "$agent_id" = "_template" ] && continue
    cp "$agent_dir/AGENT.md" "$CLAUDE_AGENTS/$agent_id.md"
    echo -e "${GREEN}  ✓${NC} agent: $agent_id"
    ((agent_count++))
  done
fi

echo ""
echo -e "${GREEN}✅ $skill_count skills em $CLAUDE_SKILLS${NC}"
echo -e "${GREEN}✅ $agent_count agentes em $CLAUDE_AGENTS${NC}\n"
