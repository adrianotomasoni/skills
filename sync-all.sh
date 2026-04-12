#!/bin/bash
# scripts/sync-all.sh
# Sincroniza skills com Claude, Cursor e GitHub em uma única execução

set -e

GITHUB_REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT_DIR="$GITHUB_REPO/scripts"

# Cores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

# Timestamps
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo -e "${MAGENTA}"
echo "╔════════════════════════════════════════════╗"
echo "║  🚀 SINCRONIZAÇÃO COMPLETA DE SKILLS      ║"
echo "║  GitHub: adrianotomasoni/skills            ║"
echo "╚════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""
echo -e "${CYAN}Timestamp: $DATE${NC}"
echo ""

# PARTE 1: Validação
echo -e "${BLUE}[1/5] Validando repositório...${NC}"
echo ""

if [ ! -d "$GITHUB_REPO/.git" ]; then
  echo -e "${RED}❌ Não é um repositório Git válido${NC}"
  exit 1
fi

if [ ! -d "$GITHUB_REPO/skills" ]; then
  echo -e "${RED}❌ Diretório 'skills' não encontrado${NC}"
  exit 1
fi

echo -e "${GREEN}✓ Repositório válido${NC}"
echo ""

# PARTE 2: Verificar mudanças
echo -e "${BLUE}[2/5] Verificando mudanças não commitadas...${NC}"
echo ""

if ! git -C "$GITHUB_REPO" diff-index --quiet HEAD -- 2>/dev/null; then
  echo -e "${YELLOW}⚠️  Mudanças detectadas:${NC}"
  git -C "$GITHUB_REPO" status --short | head -10
  echo ""
  
  read -p "Deseja commitá-las antes de sincronizar? (s/n) " -n 1 -r
  echo
  echo ""
  
  if [[ $REPLY =~ ^[Ss]$ ]]; then
    git -C "$GITHUB_REPO" add -A
    COMMIT_MSG="Auto-commit before sync: $DATE"
    git -C "$GITHUB_REPO" commit -m "$COMMIT_MSG"
    echo -e "${GREEN}✓ Mudanças commitadas${NC}"
  fi
else
  echo -e "${GREEN}✓ Sem mudanças pendentes${NC}"
fi
echo ""

# PARTE 3: Sincronizar Claude
echo -e "${BLUE}[3/5] Sincronizando com Claude...${NC}"
echo ""

if [ -f "$SCRIPT_DIR/sync-to-claude.sh" ]; then
  bash "$SCRIPT_DIR/sync-to-claude.sh"
else
  echo -e "${RED}❌ Script sync-to-claude.sh não encontrado${NC}"
fi

echo ""

# PARTE 4: Sincronizar Cursor
echo -e "${BLUE}[4/5] Sincronizando com Cursor...${NC}"
echo ""

if [ -f "$SCRIPT_DIR/sync-to-cursor.sh" ]; then
  bash "$SCRIPT_DIR/sync-to-cursor.sh"
else
  echo -e "${RED}❌ Script sync-to-cursor.sh não encontrado${NC}"
fi

echo ""

# PARTE 5: Push para GitHub
echo -e "${BLUE}[5/5] Opções de GitHub...${NC}"
echo ""

echo "Opções:"
echo "  1) Push para 'main' (padrão)"
echo "  2) Criar tag de release"
echo "  3) Pular"
echo ""

read -p "Escolha uma opção (1-3): " -n 1 choice
echo
echo ""

case $choice in
  1)
    echo -e "${YELLOW}Fazendo push para main...${NC}"
    git -C "$GITHUB_REPO" push origin main
    echo -e "${GREEN}✓ Push realizado${NC}"
    ;;
  2)
    echo -e "${YELLOW}Criando tag de release...${NC}"
    TAG_NAME="v$(date +%Y%m%d-%H%M%S)"
    git -C "$GITHUB_REPO" tag -a "$TAG_NAME" -m "Skills sync: $DATE"
    git -C "$GITHUB_REPO" push origin "$TAG_NAME"
    echo -e "${GREEN}✓ Tag criada: $TAG_NAME${NC}"
    ;;
  3)
    echo -e "${YELLOW}⊘ Push pulado${NC}"
    ;;
  *)
    echo -e "${RED}Opção inválida${NC}"
    ;;
esac

echo ""

# Resumo Final
echo -e "${MAGENTA}"
echo "╔════════════════════════════════════════════╗"
echo "║  ✅ SINCRONIZAÇÃO CONCLUÍDA               ║"
echo "╚════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

echo -e "${CYAN}Resumo da Sincronização:${NC}"
echo "  📦 Claude:  /mnt/skills/user/"
echo "  🖥️  Cursor:  $(find ~ -name '.cursorrules' 2>/dev/null | wc -l) projetos"
echo "  🔗 GitHub:  $(git -C "$GITHUB_REPO" rev-parse --short HEAD 2>/dev/null || echo 'unknown')"
echo ""

echo -e "${CYAN}Próximas Ações:${NC}"
echo "  1️⃣  Teste em Claude.ai (regenere contexto)"
echo "  2️⃣  Feche e reabra Cursor"
echo "  3️⃣  Rode skillLoader no Manus"
echo ""

echo -e "${GREEN}Tudo sincronizado! 🎉${NC}"
echo ""
