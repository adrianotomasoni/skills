# 🔄 GUIA DE SINCRONIZAÇÃO - adrianotomasoni/skills

## Seu Repositório
```
GitHub: https://github.com/adrianotomasoni/skills.git
URL SSH: git@github.com:adrianotomasoni/skills.git
```

---

## PARTE 1: SETUP INICIAL

### 1.1 Clone o Repositório (Se não tiver)

```bash
# Via HTTPS
git clone https://github.com/adrianotomasoni/skills.git
cd skills

# Ou via SSH (recomendado)
git clone git@github.com:adrianotomasoni/skills.git
cd skills

# Verifique a estrutura
ls -la
```

### 1.2 Verificar Estrutura Atual

```bash
# Ver o que já existe
tree -L 2

# Ou
find . -type f -name "*.md" | head -20
```

### 1.3 Adicione Remotes (se necessário)

```bash
# Verificar remotes existentes
git remote -v

# Adicionar upstream (se trabalhar com fork)
git remote add upstream git@github.com:adrianotomasoni/skills.git
```

---

## PARTE 2: ESTRUTURA RECOMENDADA

### 2.1 Organize o Repositório

```bash
# Crie a estrutura base
mkdir -p skills/{traderisk,general,experimental}
mkdir -p docs/{usage,best-practices,examples}
mkdir -p tests
mkdir -p scripts

# Crie arquivos essenciais
touch skills/_index.yaml
touch .cursorrules
touch manus.config.json
touch README.md
touch CHANGELOG.md
```

### 2.2 Estrutura Completa

```
skills/
├── README.md                          # Documentação principal
├── CHANGELOG.md                       # Histórico de mudanças
├── LICENSE                           # MIT/Apache
├── .gitignore                        # Git config
├── .cursorrules                      # Para Cursor
├── .github/
│   ├── workflows/
│   │   ├── validate-skills.yml       # CI/CD
│   │   └── sync.yml                  # Auto-sync
│   └── CODEOWNERS
├── manus.config.json                 # Para Manus
├── skills/
│   ├── _index.yaml                   # Índice master
│   ├── traderisk/
│   │   ├── frontend-design/
│   │   │   ├── SKILL.md
│   │   │   ├── prompts.yaml
│   │   │   └── examples/
│   │   ├── credit-risk-analysis/
│   │   ├── seo-auditoria/
│   │   └── content-writer/
│   ├── general/
│   │   ├── code-review/
│   │   ├── api-design/
│   │   └── doc-coauthoring/
│   └── experimental/
│       ├── judicial-classifier-v4/
│       └── licitaradar-setup/
├── docs/
│   ├── USAGE.md                      # Como usar
│   ├── TRIGGERING.md                 # Triggers
│   ├── BEST-PRACTICES.md             # Padrões
│   └── EXAMPLES/
│       ├── traderisk-portal-ui.md
│       └── ...
├── tests/
│   ├── test-triggers.js
│   └── validate-yaml.js
└── scripts/
    ├── sync-to-claude.sh
    ├── sync-to-cursor.sh
    ├── sync-to-manus.sh
    └── validate-skills.sh
```

---

## PARTE 3: SINCRONIZAÇÃO COM CLAUDE (claude.ai)

### 3.1 Entender o Mapeamento

**Claude acessa skills em:**
```
/mnt/skills/user/
```

**Seu repositório está em:**
```
/home/user/skills/ (ou ~/skills)
```

### 3.2 Script de Sincronização para Claude

```bash
#!/bin/bash
# scripts/sync-to-claude.sh

set -e

GITHUB_SKILLS="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/skills"
CLAUDE_SKILLS="/mnt/skills/user"

echo "🔄 Sincronizando para Claude..."

# Criar diretórios se não existirem
mkdir -p "$CLAUDE_SKILLS"

# Sincronizar cada skill
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
    src="$skill_dir/SKILL.md"
    dst="$CLAUDE_SKILLS/${category}-${skill_name}/SKILL.md"
    
    if [ -f "$src" ]; then
      mkdir -p "$(dirname "$dst")"
      cp "$src" "$dst"
      
      # Copiar arquivos adicionais
      if [ -d "$skill_dir/examples" ]; then
        cp -r "$skill_dir/examples" "$(dirname "$dst")/"
      fi
      if [ -f "$skill_dir/checklist.md" ]; then
        cp "$skill_dir/checklist.md" "$(dirname "$dst")/"
      fi
      if [ -f "$skill_dir/prompts.yaml" ]; then
        cp "$skill_dir/prompts.yaml" "$(dirname "$dst")/"
      fi
      
      echo "✓ ${category}/${skill_name}"
    fi
  done
done

echo "✅ Sincronização com Claude concluída"
```

### 3.3 Como Usar

```bash
# Dar permissão
chmod +x scripts/sync-to-claude.sh

# Executar
./scripts/sync-to-claude.sh

# Resultado
ls /mnt/skills/user/
# Output: traderisk-credit-risk-analysis/
#         traderisk-frontend-design/
#         etc...
```

### 3.4 Automação (Opcional)

Adicione ao seu bashrc/zshrc:

```bash
# ~/.bashrc ou ~/.zshrc
alias sync-claude='~/skills/scripts/sync-to-claude.sh'
alias sync-all='~/skills/scripts/sync-all.sh'

# Função para sincronizar ao entrar no diretório
cd_skills() {
  cd ~/skills
  ./scripts/sync-to-claude.sh
}
```

---

## PARTE 4: SINCRONIZAÇÃO COM CURSOR

### 4.1 Copiar .cursorrules

```bash
# Copie para cada projeto Cursor
cp skills/.cursorrules /path/to/your/cursor/workspace/.cursorrules

# Ou symlink (mais elegante)
ln -s ~/skills/.cursorrules ~/projects/projeto1/.cursorrules
ln -s ~/skills/.cursorrules ~/projects/projeto2/.cursorrules
```

### 4.2 Script Automático para Cursor

```bash
#!/bin/bash
# scripts/sync-to-cursor.sh

set -e

GITHUB_SKILLS="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CURSOR_PROJECTS=(
  "$HOME/projects/traderisk-portal"
  "$HOME/projects/portal-licitacao"
  "$HOME/projects/licitaradar"
  "$HOME/projects/riskinsect-pro"
)

echo "🔄 Sincronizando para Cursor..."

for project in "${CURSOR_PROJECTS[@]}"; do
  if [ -d "$project" ]; then
    cp "$GITHUB_SKILLS/.cursorrules" "$project/.cursorrules"
    echo "✓ $project"
  fi
done

echo "✅ Sincronização com Cursor concluída"
```

### 4.3 .cursorrules Setup

**Arquivo:** `skills/.cursorrules`

```
# .cursorrules - Cursor AI Configuration
# Sync com: https://github.com/adrianotomasoni/skills

# Carrega skills do repositório local
SKILLS_REPO = ~/skills
SKILLS_INDEX = ~/skills/skills/_index.yaml

# Skills disponíveis
[Skills]
traderisk-frontend-design = ~/skills/skills/traderisk/frontend-design/SKILL.md
credit-risk-analysis = ~/skills/skills/traderisk/credit-risk-analysis/SKILL.md
seo-auditoria-traderisk = ~/skills/skills/traderisk/seo-auditoria/SKILL.md
content-writer = ~/skills/skills/traderisk/content-writer/SKILL.md
code-review = ~/skills/skills/general/code-review/SKILL.md

# Trigger automático por keyword
[Triggers]
"cria um componente" → traderisk-frontend-design
"análise de crédito" → credit-risk-analysis
"SEO" → seo-auditoria-traderisk
"revisa esse código" → code-review

# Configurações globais
[GlobalRules]
stack = React + TypeScript + Tailwind
backend = Supabase + Edge Functions
deployment = Vercel + Lovable
brand = TradeRisk (veja docs/BEST-PRACTICES.md)

# Referência
See: ~/skills/docs/BEST-PRACTICES.md
```

### 4.4 Atualizar .cursorrules Periodicamente

```bash
# Sempre que mudar skills
git -C ~/skills add skills/
git -C ~/skills commit -m "Update skills"
git -C ~/skills push

# Depois sincronize Cursor
./scripts/sync-to-cursor.sh
```

---

## PARTE 5: SINCRONIZAÇÃO COM MANUS

### 5.1 Configuração do Manus

**Arquivo:** `skills/manus.config.json`

```json
{
  "version": "1.0",
  "skillsPath": "./skills",
  "skillsIndex": "./skills/_index.yaml",
  "autoLoad": true,
  
  "cache": {
    "enabled": true,
    "ttl": 3600,
    "location": "./.manus-cache"
  },
  
  "triggers": {
    "mode": "keyword-matching",
    "fuzzyMatch": true,
    "minConfidence": 0.75
  },
  
  "integrations": {
    "claude": {
      "enabled": true,
      "syncPath": "/mnt/skills/user"
    },
    "cursor": {
      "enabled": true,
      "projects": [
        "$HOME/projects/traderisk-portal",
        "$HOME/projects/portal-licitacao"
      ]
    }
  },
  
  "export": {
    "enabled": true,
    "formats": ["markdown", "json", "yaml"],
    "destination": "./exports"
  }
}
```

### 5.2 TypeScript Loader para Manus

**Arquivo:** `scripts/SkillLoader.ts`

```typescript
import fs from 'fs';
import path from 'path';
import YAML from 'yaml';

interface Skill {
  id: string;
  name: string;
  category: string;
  path: string;
  triggers: string[];
  content: string;
}

interface SkillIndex {
  version: string;
  categories: Array<{
    id: string;
    name: string;
    skills: Array<{
      id: string;
      name: string;
      path: string;
      triggers: string[];
    }>;
  }>;
}

export class SkillLoader {
  private skillsIndex: SkillIndex;
  private skillsPath: string;

  constructor(skillsPath: string = './skills') {
    this.skillsPath = skillsPath;
    this.loadIndex();
  }

  private loadIndex(): void {
    const indexPath = path.join(this.skillsPath, '_index.yaml');
    const raw = fs.readFileSync(indexPath, 'utf-8');
    this.skillsIndex = YAML.parse(raw);
  }

  async loadSkill(skillId: string): Promise<Skill> {
    const skillMeta = this.findSkillById(skillId);
    if (!skillMeta) {
      throw new Error(`Skill not found: ${skillId}`);
    }

    const skillPath = path.join(this.skillsPath, skillMeta.path, 'SKILL.md');
    const content = fs.readFileSync(skillPath, 'utf-8');

    return {
      id: skillMeta.id,
      name: skillMeta.name,
      category: this.findCategoryBySkillId(skillId),
      path: skillMeta.path,
      triggers: skillMeta.triggers,
      content,
    };
  }

  async detectSkill(userQuery: string): Promise<Skill | null> {
    const allSkills = this.getAllSkills();

    for (const skill of allSkills) {
      for (const trigger of skill.triggers) {
        if (userQuery.toLowerCase().includes(trigger.toLowerCase())) {
          return this.loadSkill(skill.id);
        }
      }
    }
    return null;
  }

  private findSkillById(id: string): any {
    for (const category of this.skillsIndex.categories) {
      const found = category.skills.find((s) => s.id === id);
      if (found) return { ...found, category: category.id };
    }
    return null;
  }

  private findCategoryBySkillId(id: string): string {
    for (const category of this.skillsIndex.categories) {
      if (category.skills.some((s) => s.id === id)) {
        return category.id;
      }
    }
    return 'unknown';
  }

  private getAllSkills(): any[] {
    return this.skillsIndex.categories.flatMap((c) => c.skills);
  }

  // Sincronizar com repositório
  async syncFromGitHub(): Promise<void> {
    // Implementar: pull latest do GitHub
    // Recarregar index
    this.loadIndex();
  }
}
```

### 5.3 Integração com Seu Manus

```typescript
// No seu código Manus
import { SkillLoader } from './scripts/SkillLoader';

const skillLoader = new SkillLoader('./skills');

// Detectar skill automaticamente
const userQuery = "cria um componente de análise de crédito";
const skill = await skillLoader.detectSkill(userQuery);

if (skill) {
  console.log(`Carregada skill: ${skill.name}`);
  // Use skill.content no seu pipeline
}
```

---

## PARTE 6: GIT WORKFLOW (IMPORTANTE!)

### 6.1 Commits e Pushes

```bash
# Sempre que adicionar/modificar skills
cd ~/skills

# 1. Verifique o status
git status

# 2. Adicione as mudanças
git add skills/
git add docs/
git add scripts/

# 3. Commit com mensagem clara
git commit -m "Add/Update: [skill-name] - [what changed]"

# Exemplos:
git commit -m "Add: credit-risk-analysis skill with IFRS support"
git commit -m "Update: frontend-design with new components"
git commit -m "Fix: trigger keywords in seo-auditoria"

# 4. Push para GitHub
git push origin main
```

### 6.2 Branches para Novas Skills

```bash
# Para desenvolvimento de novas skills
git checkout -b feature/judicial-classifier-v4

# Trabalhe na skill
mkdir -p skills/experimental/judicial-classifier-v4

# Commit
git commit -m "WIP: judicial classifier v4"

# Quando pronta
git commit -m "Feat: judicial classifier v4 complete"

# Push
git push origin feature/judicial-classifier-v4

# Crie Pull Request no GitHub (opcional)
# Depois merge para main
```

### 6.3 Tags para Releases

```bash
# Quando uma versão está estável
git tag -a v1.0.0 -m "Release: Skills v1.0 with credit analysis"
git push origin v1.0.0

# Ou semântico
git tag -a v1.1.0-skills -m "Add: new skills batch"
```

---

## PARTE 7: SCRIPT MASTER DE SINCRONIZAÇÃO

Combine tudo em um script:

```bash
#!/bin/bash
# scripts/sync-all.sh

set -e

GITHUB_REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CLAUDE_SKILLS="/mnt/skills/user"
CURSOR_PROJECTS=(
  "$HOME/projects/traderisk-portal"
  "$HOME/projects/portal-licitacao"
)

echo "🚀 Iniciando sincronização completa..."
echo ""

# 1. Validar repositório GitHub
echo "1️⃣ Validando repositório..."
if [ ! -d "$GITHUB_REPO/.git" ]; then
  echo "❌ Não é um repositório Git"
  exit 1
fi
echo "✓ Repositório válido"

# 2. Verificar mudanças não commitadas
echo ""
echo "2️⃣ Verificando mudanças..."
if ! git -C "$GITHUB_REPO" diff-index --quiet HEAD --; then
  echo "⚠️  Mudanças não commitadas detectadas:"
  git -C "$GITHUB_REPO" status --short
  read -p "Deseja commitá-las antes de sincronizar? (s/n) " -n 1 -r
  echo
  if [[ $REPLY =~ ^[Ss]$ ]]; then
    git -C "$GITHUB_REPO" add -A
    git -C "$GITHUB_REPO" commit -m "Auto-commit before sync: $(date)"
  fi
fi

# 3. Sincronizar com Claude
echo ""
echo "3️⃣ Sincronizando com Claude..."
"$GITHUB_REPO/scripts/sync-to-claude.sh"

# 4. Sincronizar com Cursor
echo ""
echo "4️⃣ Sincronizando com Cursor..."
"$GITHUB_REPO/scripts/sync-to-cursor.sh"

# 5. Sincronizar com Manus (se configurado)
if [ -f "$GITHUB_REPO/manus.config.json" ]; then
  echo ""
  echo "5️⃣ Sincronizando com Manus..."
  # npx ts-node scripts/SkillLoader.ts sync
  echo "✓ Manus (manual check: npm run sync-manus)"
fi

# 6. Push para GitHub (opcional)
echo ""
read -p "Deseja fazer push para GitHub? (s/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Ss]$ ]]; then
  echo "6️⃣ Fazendo push..."
  git -C "$GITHUB_REPO" push origin main
  echo "✓ Push realizado"
fi

echo ""
echo "✅ Sincronização completa!"
echo ""
echo "Resumo:"
echo "  Claude: /mnt/skills/user/"
echo "  Cursor: Multiple projects"
echo "  Manus: Local cache"
echo ""
echo "Próximos passos:"
echo "  1. Verifique Claude (claude.ai): /mnt/skills/user/"
echo "  2. Teste Cursor: abra um projeto e verifique .cursorrules"
echo "  3. Teste Manus: rode skillLoader"
```

### Usar o Script

```bash
chmod +x scripts/sync-all.sh
./scripts/sync-all.sh
```

---

## PARTE 8: CHECKLIST DE SINCRONIZAÇÃO

```
✅ SETUP INICIAL
  ☐ Clone o repositório
  ☐ Crie estrutura de diretórios
  ☐ Configure git remotes
  ☐ Crie .gitignore

✅ CLAUDE (claude.ai)
  ☐ Execute sync-to-claude.sh
  ☐ Verifique /mnt/skills/user/
  ☐ Teste em claude.ai
  ☐ Configure memory/preferences (opcional)

✅ CURSOR (VS Code)
  ☐ Copie .cursorrules para workspaces
  ☐ Execute sync-to-cursor.sh
  ☐ Teste triggers em Cursor
  ☐ Verifique detecção automática

✅ MANUS (Custom)
  ☐ Configure manus.config.json
  ☐ Implemente SkillLoader.ts
  ☐ Teste loadSkill()
  ☐ Configure detecção automática

✅ GIT WORKFLOW
  ☐ Commit mudanças
  ☐ Push para GitHub
  ☐ Verifique remotes
  ☐ Configure branches (opcional)

✅ AUTOMAÇÃO
  ☐ Configure aliases bash/zsh
  ☐ Configure cron jobs (opcional)
  ☐ Configure GitHub Actions (opcional)
  ☐ Teste sync-all.sh
```

---

## PARTE 9: TROUBLESHOOTING

### Problema: Sincronização não funciona com Claude

```bash
# Verificar se diretório existe
ls -la /mnt/skills/user/

# Se não existir, criar
mkdir -p /mnt/skills/user/

# Executar sync manualmente
./scripts/sync-to-claude.sh -v (verbose)

# Verificar permissões
ls -la /mnt/skills/user/traderisk-*/
```

### Problema: .cursorrules não é reconhecido

```bash
# Verificar se arquivo existe
ls -la .cursorrules
cat .cursorrules

# Verificar sintaxe
# Cursor recarrega ao salvar arquivo

# Se problema persistir:
# 1. Feche e abra Cursor novamente
# 2. Limpe cache: ~/.cursor/
# 3. Recrie .cursorrules
```

### Problema: Git conflicts

```bash
# Quando pullar remotamente
git pull origin main

# Se houver conflicts
git status

# Resolver manualmente
# Depois:
git add .
git commit -m "Resolve conflicts"
git push origin main
```

### Problema: Permissões de script

```bash
# Se scripts não executam
chmod +x scripts/*.sh

# Verificar
ls -la scripts/

# Executar com bash
bash scripts/sync-all.sh
```

---

## PARTE 10: AUTOMAÇÃO AVANÇADA (Opcional)

### 10.1 GitHub Actions - Auto-Sync

**Arquivo:** `.github/workflows/sync.yml`

```yaml
name: Auto-Sync Skills

on:
  push:
    branches: [main]
    paths:
      - 'skills/**'
      - '.cursorrules'
      - 'manus.config.json'

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Validate Skills
        run: bash scripts/validate-skills.sh
      
      - name: Create Tag
        if: success()
        run: |
          git tag -a v$(date +%Y%m%d-%H%M%S) \
            -m "Auto-sync: $(date)"
          git push origin --tags
      
      - name: Notify
        if: success()
        run: echo "✅ Skills sincronizadas!"
```

### 10.2 Cron Job Local - Sync Periódico

```bash
# Adicione ao crontab
crontab -e

# Sincronize a cada hora
0 * * * * cd ~/skills && ./scripts/sync-all.sh >> ~/skills/logs/sync.log 2>&1

# Ou a cada 30 minutos
*/30 * * * * cd ~/skills && ./scripts/sync-to-claude.sh
```

---

## PARTE 11: FLUXO TÍPICO DO DIA

```bash
# 1. Ao iniciar trabalho
cd ~/skills
git pull origin main

# 2. Criar nova skill ou editar existente
mkdir -p skills/traderisk/minha-nova-skill
vim skills/traderisk/minha-nova-skill/SKILL.md

# 3. Testar em Claude (manual)
# - Rode sync-to-claude.sh
# - Teste em claude.ai

# 4. Testar em Cursor (manual)
# - Rode sync-to-cursor.sh
# - Abra Cursor e teste triggers

# 5. Commit e Push
git add skills/
git commit -m "Add: minha-nova-skill"
git push origin main

# 6. Sincronização automática (todos os ambientes)
./scripts/sync-all.sh
```

---

## PARTE 12: REFERÊNCIA RÁPIDA

```bash
# Sincronizar tudo de uma vez
./scripts/sync-all.sh

# Sincronizar só Claude
./scripts/sync-to-claude.sh

# Sincronizar só Cursor
./scripts/sync-to-cursor.sh

# Validar estrutura
./scripts/validate-skills.sh

# Ver status Git
git status

# Ver remotes
git remote -v

# Pull latest
git pull origin main

# Push mudanças
git push origin main

# Ver todas as skills
cat skills/_index.yaml
```

---

## RESUMO FINAL

| Ambiente | Sincronização | Arquivo | Status |
|----------|---|---|---|
| **Claude** | `sync-to-claude.sh` | `/mnt/skills/user/` | Manual ⚠️ |
| **Cursor** | `sync-to-cursor.sh` | `.cursorrules` | Manual ⚠️ |
| **Manus** | TypeScript Loader | `manus.config.json` | Automático ✅ |
| **GitHub** | Git push | Repository | Manual ⚠️ |
| **Tudo** | `sync-all.sh` | Script master | 1 comando ✅ |

---

**Última atualização:** 2026-04-12
**Versão:** 2.0 (Repositório específico: adrianotomasoni/skills)

EOF
cat /home/claude/sincronizacao-skills-repo.md
