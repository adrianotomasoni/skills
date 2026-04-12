#!/bin/bash
# scripts/sync-to-cursor.sh
# Sincroniza .cursorrules com todos os projetos Cursor

set -e

GITHUB_REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CURSORRULES_SRC="$GITHUB_REPO/.cursorrules"

# Cores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}📝 Sincronizando .cursorrules para Cursor...${NC}"
echo ""

# Verificar se .cursorrules existe
if [ ! -f "$CURSORRULES_SRC" ]; then
  echo -e "${RED}❌ .cursorrules não encontrado em: $CURSORRULES_SRC${NC}"
  exit 1
fi

# Lista de projetos Cursor (customize conforme necessário)
CURSOR_PROJECTS=(
  "$HOME/projects/traderisk-portal"
  "$HOME/projects/portal-licitacao"
  "$HOME/projects/licitaradar"
  "$HOME/projects/riskinsect-pro"
  "$HOME/projects/one-tower-leiloeiro"
)

copy_count=0

for project in "${CURSOR_PROJECTS[@]}"; do
  if [ -d "$project" ]; then
    cp "$CURSORRULES_SRC" "$project/.cursorrules"
    echo -e "${GREEN}  ✓${NC} $(basename "$project")"
    ((copy_count++))
  else
    echo -e "${YELLOW}  ⊘${NC} Projeto não encontrado: $project"
  fi
done

echo ""
echo -e "${GREEN}✅ Sincronizado: $copy_count projetos${NC}"
echo ""

# Instruções adicionais
echo -e "${YELLOW}💡 Próximos passos:${NC}"
echo "  1. Abra Cursor em cada projeto"
echo "  2. Feche e reabra para carregar novo .cursorrules"
echo "  3. Teste os triggers em cada projeto"
echo ""
