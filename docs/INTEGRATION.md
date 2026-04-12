# INTEGRATION.md - Como Integrar Skills em Diferentes Plataformas

## 1️⃣ Claude.ai (Web)

### Método A: Upload Direto
1. Acesse **claude.ai** → **Settings** (canto inferior esquerdo)
2. Vá até **Knowledge** ou **Custom Instructions**
3. Clique **Upload Files**
4. Selecione os arquivos `.md` de skills que quer disponibilizar
5. Pronto! Claude terá acesso automático

### Método B: Paste em Custom Instructions
1. Settings → **Custom Instructions**
2. Cole o conteúdo inteiro da skill em "What would you like Claude to know about you?"
3. Exemplo:
```
# SKILL: Análise de Risco de Crédito

Você é um especialista em análise de risco de crédito comercial...
[colar conteúdo completo do SKILL.md]
```

### Método C: Usar como Knowledge Base (Claude Team/Enterprise)
1. Workspace Settings → Knowledge
2. Upload arquivo ou conecte repositório GitHub
3. Claude pode referenciar automaticamente

---

## 2️⃣ Cursor / VS Code

### Instalação Rápida

#### Opção A: Clone o Repositório
```bash
# Clone para um local acessível
git clone https://github.com/adrianotomasoni/skills.git ~/.cursor/skills

# Ou para VS Code
git clone https://github.com/adrianotomasoni/skills.git ~/.vscode/skills
```

#### Opção B: Configurar `.cursor/rules.md`

Crie um arquivo `.cursor/rules.md` no seu projeto:

```markdown
# Regras do Projeto

## Skills Disponíveis

Você tem acesso aos seguintes skills:

### Core Business
- **judicial-monitoring**: Detecção de eventos em processos judiciais
  Arquivo: ~/.cursor/skills/skills/core/judicial-monitoring/SKILL.md
  
- **credit-risk-analysis**: Análise de risco de crédito comercial
  Arquivo: ~/.cursor/skills/skills/core/credit-risk-analysis/SKILL.md

### Frontend
- **traderisk-frontend-design**: Design de interfaces para TradeRisk
  Arquivo: ~/.cursor/skills/skills/frontend/traderisk-frontend-design/SKILL.md

Quando solicitado um trabalho nessas áreas, consulte os skills relevantes.
```

#### Opção C: Usar Rules com @-mentions

No chat do Cursor, você pode fazer:

```
@skill judicial-monitoring como posso melhorar a detecção de eventos?
```

Para isso funcionar, adicione ao `.cursor/rules.md`:
```markdown
## Convenção de Skills

Use @-mentions para referenciar skills:
- @skill-name-aqui

Os arquivos estão em: ~/.cursor/skills/skills/
```

#### Opção D: Integração com Custom Instructions

1. Abra Cursor Settings
2. Vá até **General** → **Rules** ou **Instructions**
3. Paste:
```
## Skills Repository

Você tem acesso a um repositório de skills em ~/.cursor/skills/

Para usar:
- Leia ~/cursor/skills/skills/[categoria]/[skill-id]/SKILL.md
- Siga as instruções do skill
- Referencie no contexto quando relevante
```

---

## 3️⃣ Manus (Local)

### Configuração Padrão

1. **Clone o repo:**
```bash
git clone https://github.com/adrianotomasoni/skills.git ~/projects/skills
```

2. **Crie `manus.config.json` na raiz do seu projeto:**
```json
{
  "skillsPath": "~/projects/skills/skills",
  "skillsRegistry": "~/projects/skills/registry.json",
  "autoLoadSkills": true,
  "categories": [
    "core",
    "frontend",
    "content",
    "engineering"
  ]
}
```

3. **Use em Manus:**
```
@load-skill judicial-monitoring
@load-skill credit-risk-analysis

Tenho um caso de garantia judicial. Como proceder?
```

4. **Ou referencie diretamente:**
```
~/projects/skills/skills/core/judicial-monitoring/

Qual é o contexto para classificação nível C?
```

---

## 4️⃣ GitHub (Source of Truth)

### Workflow Padrão

1. **Crie uma branch para mudar uma skill:**
```bash
git checkout -b feature/improve-credit-risk-skill
```

2. **Edite a skill:**
```bash
# Exemplo: editar skill de credit risk
nano skills/core/credit-risk-analysis/SKILL.md
```

3. **Valide a alteração:**
```bash
python scripts/validate-skills.py --skill credit-risk-analysis
```

4. **Commit & Push:**
```bash
git add skills/core/credit-risk-analysis/SKILL.md
git commit -m "feat: Add new financial metrics to credit risk skill"
git push origin feature/improve-credit-risk-skill
```

5. **Abra Pull Request no GitHub:**
- Vá para https://github.com/adrianotomasoni/skills/pulls
- Clique "New Pull Request"
- Selecione sua branch
- Descreva as mudanças
- Espere CI passar
- Merge!

---

## 5️⃣ Claude Code (Terminal)

Se você está usando Claude Code no seu ambiente local:

```bash
# 1. Clone o repositório
git clone https://github.com/adrianotomasoni/skills.git

# 2. Navegue para uma skill
cd skills/skills/core/judicial-monitoring

# 3. Peça ajuda ao Claude Code
# No seu editor, cole o prompt:
cat SKILL.md | claude --system "Revise and improve this skill description"
```

---

## 6️⃣ Integração com APIs e Webhooks

### Auto-sync com GitHub Actions

Crie `.github/workflows/sync-skills.yml`:

```yaml
name: Sync Skills to Services

on:
  push:
    branches: [main]
    paths:
      - 'skills/**'

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Generate Registry
        run: python scripts/generate-registry.py
      
      - name: Validate Skills
        run: python scripts/validate-skills.py
      
      - name: Commit if changed
        run: |
          git config user.name "Skills Bot"
          git config user.email "bot@traderisk.com"
          git add registry.json
          git commit -m "Auto: Update registry.json" || true
          git push
```

### Webhook para Notificar Quando Skills Mudam

Crie um script em `.github/workflows/notify.yml`:

```yaml
name: Notify Skill Changes

on:
  push:
    branches: [main]
    paths:
      - 'skills/**'

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Send Notification
        run: |
          echo "Skills foram atualizadas!"
          echo "Sync em: $(date)"
```

---

## 7️⃣ Workflow Recomendado (Dia-a-dia)

### Para Editar uma Skill Existente:

```bash
# 1. Sincronize
git pull origin main

# 2. Crie branch
git checkout -b feature/melhorar-xyz

# 3. Edite em Cursor/VS Code
# Abra o arquivo da skill:
skills/core/credit-risk-analysis/SKILL.md

# 4. Teste localmente
# Em Claude/Cursor, cole o arquivo atualizado

# 5. Commit
git add skills/core/credit-risk-analysis/SKILL.md
git commit -m "Improve: Add new scoring criteria"

# 6. Push & PR
git push origin feature/melhorar-xyz
# Abra PR no GitHub
```

### Para Criar uma Nova Skill:

```bash
# 1. Crie diretório
mkdir -p skills/category/nova-skill

# 2. Crie estrutura
touch skills/category/nova-skill/{SKILL.md,README.md}
mkdir -p skills/category/nova-skill/{examples,tests}

# 3. Edite SKILL.md em Cursor

# 4. Atualize registry.json
python scripts/generate-registry.py

# 5. Commit tudo
git add skills/category/nova-skill/
git add registry.json
git commit -m "feat: Add nova-skill"
git push
```

---

## 8️⃣ Sincronização Entre Plataformas

### Checklist para Manter Tudo Sincronizado

- [ ] GitHub é a **source of truth** (sempre)
- [ ] Editar skills sempre em uma branch
- [ ] Validar antes de merge
- [ ] Após merge, sincronizar com:
  - [ ] Claude.ai (re-upload manual ou knowledge base)
  - [ ] Cursor (git pull ~/.cursor/skills)
  - [ ] Manus (sincronização automática via config)

### Script de Sincronização (Automático)

```bash
#!/bin/bash
# sync-all-skills.sh

echo "🔄 Sincronizando skills entre plataformas..."

# 1. Pull do GitHub
cd ~/projects/skills
git pull origin main

# 2. Sincronizar Cursor
cp -r skills ~/.cursor/skills/

# 3. Atualizar registry
python scripts/generate-registry.py

# 4. Validar tudo
python scripts/validate-skills.py

echo "✅ Sincronização completa!"
```

Use assim:
```bash
chmod +x scripts/sync-all-skills.sh
./scripts/sync-all-skills.sh
```

---

## 📊 Comparação de Plataformas

| Plataforma | Melhor para | Frequência de Atualização | Sincronização |
|------------|------------|--------------------------|---------------|
| GitHub | Source of truth, controle de versão | Por commit | Manual/Automática via webhook |
| Claude.ai | Conversas rápidas, sem setup | Upload manual | Via knowledge base ou paste |
| Cursor | Desenvolvimento de código | Automática (git pull) | Automática |
| Manus | Automação local, CI/CD | Automática via config | Automática |
| VS Code | Desenvolvimento local | Automática (git) | Automática |

---

## 🆘 Troubleshooting

### "Não consigo acessar a skill em Cursor"
```bash
# 1. Verifique se está no path correto
ls ~/.cursor/skills/skills/core/

# 2. Force refresh
cd ~/.cursor/skills && git pull origin main

# 3. Reinicie Cursor
```

### "Git merge conflict nas skills"
```bash
# 1. Abra o arquivo em conflito
git diff skills/core/credit-risk-analysis/SKILL.md

# 2. Resolva manualmente em Cursor
# 3. Commit
git add skills/core/credit-risk-analysis/SKILL.md
git commit -m "resolve: merge conflict"
```

### "Registry.json está desatualizado"
```bash
# Regenere automaticamente
python scripts/generate-registry.py
git add registry.json
git commit -m "auto: update registry"
```

---

**Última atualização**: 2026-04-12  
**Status**: ✅ Pronto para produção
