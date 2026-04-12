#!/bin/bash
# scripts/sync-to-claude.sh
# Sincroniza skills do repositório para Claude (/mnt/skills/user)

set -e

GITHUB_SKILLS="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/skills"
CLAUDE_SKILLS="/mnt/skills/user"

# Cores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}📦 Sincronizando skills para Claude...${NC}"
echo ""

# Verificar se diretório GitHub existe
if [ ! -d "$GITHUB_SKILLS" ]; then
  echo -e "${RED}❌ Diretório de skills não encontrado: $GITHUB_SKILLS${NC}"
  exit 1
fi

# Criar diretório Claude se não existir
mkdir -p "$CLAUDE_SKILLS"

# Sincronizar cada skill
skill_count=0
for category_dir in "$GITHUB_SKILLS"/{traderisk,general,experimental}; do
  if [ ! -d "$category_dir" ]; then
    continue
  fi
  
  category=$(basename "$category_dir")
  
  for skill_dir in "$category_dir"/*/; do
    if [ ! -d "$skill_dir" ]; then
      continue
    fi
    
    skill_name=$(basename "$skill_dir")
    skill_id="${category}-${skill_name}"
    src="$skill_dir/SKILL.md"
    dst="$CLAUDE_SKILLS/${skill_id}"
    
    if [ -f "$src" ]; then
      mkdir -p "$dst"
      
      # Copiar arquivo principal
      cp "$src" "$dst/SKILL.md"
      
      # Copiar exemplos
      if [ -d "$skill_dir/examples" ]; then
        cp -r "$skill_dir/examples" "$dst/" 2>/dev/null || true
      fi
      
      # Copiar checklist
      if [ -f "$skill_dir/checklist.md" ]; then
        cp "$skill_dir/checklist.md" "$dst/"
      fi
      
      # Copiar prompts
      if [ -f "$skill_dir/prompts.yaml" ]; then
        cp "$skill_dir/prompts.yaml" "$dst/"
      fi
      
      echo -e "${GREEN}  ✓${NC} $skill_id"
      ((skill_count++))
    fi
  done
done

echo ""
echo -e "${GREEN}✅ Sincronizado: $skill_count skills${NC}"
echo -e "${YELLOW}Local: $CLAUDE_SKILLS${NC}"
echo ""
