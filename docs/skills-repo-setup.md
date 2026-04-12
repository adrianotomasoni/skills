# Skills Repository - Organização Centralizada

## Estrutura Proposta

```
adriano-skills/
├── README.md                          # Índice master de todas as skills
├── .github/
│   ├── workflows/
│   │   └── validate-skills.yml       # CI/CD para validar YAML
│   └── CODEOWNERS
├── .cursorrules                       # Rules para Cursor
├── .manus.config.json                 # Config para Manus (opcional)
├── skills/
│   ├── _index.yaml                   # Índice machine-readable
│   ├── traderisk/
│   │   ├── frontend-design/
│   │   │   ├── SKILL.md              # Conteúdo principal
│   │   │   ├── prompts.yaml          # Variações de prompt
│   │   │   ├── examples/             # Casos de uso
│   │   │   └── checklist.md          # QA/validação
│   │   ├── credit-risk-analysis/
│   │   ├── content-writer/
│   │   ├── seo-auditoria/
│   │   └── ...
│   ├── general/
│   │   ├── doc-coauthoring/
│   │   ├── code-review/
│   │   └── ...
│   └── experimental/                 # Draft/WIP skills
├── docs/
│   ├── USAGE.md                      # Como usar em cada ambiente
│   ├── TRIGGERING.md                 # Como otimizar triggers
│   ├── BEST-PRACTICES.md
│   └── EXAMPLES/
│       ├── traderisk-portal-ui.md
│       ├── licitaradar-setup.md
│       └── credit-analysis-workflow.md
├── tests/
│   ├── test-triggers.js              # Testar acionamento
│   └── validate-yaml.js
└── scripts/
    ├── export-for-claude.sh          # Export skills para Claude
    ├── export-for-cursor.sh          # Export skills para Cursor
    └── sync-to-manus.sh              # Sync com Manus
```

## Arquivo Principal: `skills/_index.yaml`

```yaml
version: "1.0"
lastUpdated: 2026-04-12
categories:
  - name: "TradeRisk"
    description: "Skills específicas para a operação TradeRisk"
    skills:
      - id: "traderisk-frontend-design"
        name: "TradeRisk Frontend Design"
        path: "traderisk/frontend-design"
        priority: "critical"
        triggers:
          - "cria um componente"
          - "monta esse layout"
          - "faz um design pra"
          - "React component"
          - "revisa o UI"
        tags: ["ui", "react", "design", "traderisk"]
        minTokens: 2000
        
      - id: "credit-risk-analysis"
        name: "Análise de Risco de Crédito"
        path: "traderisk/credit-risk-analysis"
        priority: "high"
        triggers:
          - "análise de crédito"
          - "limite de crédito"
          - "balanço do cliente"
          - "Serasa"
          - "parecer de crédito"
        tags: ["credit", "risk", "financial", "b2b"]
        
      - id: "seo-auditoria-traderisk"
        name: "Auditoria SEO TradeRisk"
        path: "traderisk/seo-auditoria"
        priority: "medium"
        triggers:
          - "analisar SEO"
          - "ranking caiu"
          - "como estamos no Google"
        tags: ["seo", "marketing", "analytics"]

  - name: "General"
    description: "Skills gerais, reutilizáveis"
    skills:
      - id: "code-review-checklist"
        name: "Code Review Estruturado"
        path: "general/code-review"
        priority: "medium"
        triggers:
          - "revisa esse código"
          - "code review"
          - "está bom?"

  - name: "Experimental"
    description: "WIP / protótipos"
    skills:
      - id: "judicial-classifier-v4"
        name: "Classificador Judicial V4"
        path: "experimental/judicial-classifier"
        status: "draft"
```

## Como Usar em Cada Ambiente

### 1. **Claude (claude.ai)**

Adicione ao seu `.txt` de memory/preferences:

```
**Skills Repository**
- GitHub: github.com/adrianotomasoni/adriano-skills
- Sync automático: as skills estão sempre atualizadas
- Localização local: /mnt/skills/user/*
- Acionamento: baseado em keywords do SKILL.md

Todas as skills estão documentadas em SKILL.md com:
- Descrição de 1-2 linhas
- Quando usar (triggers)
- Tags para categorização
```

**Acesso em Claude:**
```
Adriano, use a skill [nome] pra isso
```
Claude detecta automaticamente pelo path e trigger keywords.

### 2. **Cursor**

Crie `.cursorrules` na raiz do seu workspace:

```
# Cursor AI Rules - Adriano's Skills

You have access to the following skills library: github.com/adrianotomasoni/adriano-skills

When the user asks for:
- "cria um componente" ou "faz um design" → use skill: traderisk-frontend-design
- "análise de crédito" ou "balanço" → use skill: credit-risk-analysis
- "revisa esse código" → use skill: code-review-checklist
- "SEO", "ranking", "Google" → use skill: seo-auditoria-traderisk

Load the relevant SKILL.md from /skills/{category}/{skill-name}/SKILL.md
Apply the prompts and context from that skill to your responses.

Always reference: docs/BEST-PRACTICES.md for guidelines
```

**No Cursor, adicione ao `cursorignore`:**
```
node_modules/
.git/
tests/
scripts/
```

### 3. **Manus (Seu Framework Custom)**

Configure no `manus.config.json`:

```json
{
  "skillsPath": "./skills",
  "skillsIndex": "skills/_index.yaml",
  "autoLoad": true,
  "cache": {
    "enabled": true,
    "ttl": 3600
  },
  "triggers": {
    "mode": "keyword-matching",
    "fuzzyMatch": true,
    "minConfidence": 0.75
  },
  "export": {
    "formats": ["markdown", "json", "yaml"],
    "destination": "./exports"
  }
}
```

Depois implemente um loader em TypeScript:

```typescript
// manus/SkillLoader.ts
import YAML from 'yaml';
import fs from 'fs';
import path from 'path';

interface Skill {
  id: string;
  name: string;
  path: string;
  triggers: string[];
  content: string;
}

export class SkillLoader {
  private skillsIndex: any;
  private skillsPath: string;

  constructor(skillsPath: string = './skills') {
    this.skillsPath = skillsPath;
    this.loadIndex();
  }

  private loadIndex() {
    const indexPath = path.join(this.skillsPath, '_index.yaml');
    const raw = fs.readFileSync(indexPath, 'utf-8');
    this.skillsIndex = YAML.parse(raw);
  }

  async loadSkill(skillId: string): Promise<Skill> {
    // Busca no índice
    const skillMeta = this.findSkillById(skillId);
    if (!skillMeta) throw new Error(`Skill not found: ${skillId}`);

    // Carrega o SKILL.md
    const skillPath = path.join(
      this.skillsPath,
      skillMeta.path,
      'SKILL.md'
    );
    const content = fs.readFileSync(skillPath, 'utf-8');

    return {
      id: skillMeta.id,
      name: skillMeta.name,
      path: skillMeta.path,
      triggers: skillMeta.triggers,
      content
    };
  }

  async detectSkill(userQuery: string): Promise<Skill | null> {
    // Busca skill por trigger matching
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
      const found = category.skills.find((s: any) => s.id === id);
      if (found) return found;
    }
    return null;
  }

  private getAllSkills(): any[] {
    return this.skillsIndex.categories.flatMap((c: any) => c.skills);
  }
}
```

## Setup Rápido (Copiar e Colar)

### Clone e Configure:

```bash
# 1. Crie o repositório
mkdir adriano-skills
cd adriano-skills
git init
git remote add origin https://github.com/adrianotomasoni/adriano-skills.git

# 2. Copie a estrutura
mkdir -p skills/{traderisk,general,experimental}/{frontend-design,credit-risk-analysis,seo-auditoria}
mkdir -p docs tests scripts .github/workflows

# 3. Sincronize skills existentes
cp /mnt/skills/user/traderisk-frontend-design/SKILL.md skills/traderisk/frontend-design/
cp /mnt/skills/user/credit-risk-analysis/SKILL.md skills/traderisk/credit-risk-analysis/
cp /mnt/skills/user/seo-auditoria-traderisk/SKILL.md skills/traderisk/seo-auditoria/

# 4. Crie _index.yaml, .cursorrules, etc.
# (use os templates abaixo)

# 5. Push
git add .
git commit -m "Initial skills repository setup"
git push -u origin main
```

## Sincronização com Claude

Para manter as skills sincronizadas entre GitHub e Claude (`/mnt/skills/user`):

```bash
#!/bin/bash
# scripts/sync-to-claude.sh

GITHUB_SKILLS="$PWD/skills"
CLAUDE_SKILLS="/mnt/skills/user"

for category in traderisk general experimental; do
  for skill in $GITHUB_SKILLS/$category/*/; do
    skill_name=$(basename "$skill")
    src="$skill/SKILL.md"
    dst="$CLAUDE_SKILLS/$category-$skill_name/SKILL.md"
    
    if [ -f "$src" ]; then
      mkdir -p "$(dirname "$dst")"
      cp "$src" "$dst"
      echo "✓ Synced: $skill_name"
    fi
  done
done
```

## Versionamento e Releases

Use GitHub Releases para marcar versões estáveis:

```yaml
# .github/workflows/release.yml
name: Create Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Create Release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: ${{ github.ref }}
          release_name: Skills Release ${{ github.ref }}
          body_path: CHANGELOG.md
```

## Próximos Passos

- [ ] Criar repositório no GitHub
- [ ] Migrar skills existentes para estrutura
- [ ] Criar `.cursorrules` para seu workspace
- [ ] Implementar SkillLoader no Manus
- [ ] Configurar CI/CD de validação
- [ ] Documentar cada skill com exemplos
- [ ] Setup automático de sincronização

## Recursos

- `/docs/USAGE.md` – Como usar em cada ambiente
- `/docs/TRIGGERING.md` – Otimizar acionamento automático
- `/docs/BEST-PRACTICES.md` – Padrões de skill
