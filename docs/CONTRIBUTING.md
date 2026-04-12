# Como Contribuir com Novas Skills

## Pré-requisitos

- Git configurado com suas credenciais
- Acesso ao repositório `adrianotomasoni/skills`
- Python 3.8+ (para scripts de validação)

## Adicionando uma Nova Skill

### 1. Crie a Branch

```bash
git checkout main
git pull origin main
git checkout -b feature/skill-nome-da-skill
```

### 2. Crie a Estrutura de Diretório

```bash
# Escolha a categoria: core / frontend / content / engineering / tools
CATEGORIA=core
SKILL_ID=minha-nova-skill

mkdir -p skills/$CATEGORIA/$SKILL_ID/{examples,tests}
```

### 3. Crie o SKILL.md

Copie o template `docs/SKILL-TEMPLATE.md` (se existir) ou use esta estrutura:

```markdown
# Skill: [Nome da Skill]
# ID: [skill-id]
# Version: 1.0.0
# Category: [core|frontend|content|engineering|tools]
# Status: [stable|beta|experimental]

## Identidade
[Quem você é e qual sua função]

## Objetivo
[O que esta skill faz]

## [Seções específicas da skill]

---
**Versão**: 1.0.0 | **Última atualização**: YYYY-MM-DD | **Maintainer**: seu@email.com
```

### 4. Crie o README.md

```markdown
# [Nome da Skill]

[Descrição em uma linha]

## Versão
**1.0.0**

## Como Usar
[Exemplos de uso]

## Tags
`tag1` `tag2`
```

### 5. Valide a Skill

```bash
python scripts/validate-skills.py --skill $CATEGORIA/$SKILL_ID
```

### 6. Atualize o Registry

```bash
python scripts/generate-registry.py
```

### 7. Commit e Pull Request

```bash
git add skills/$CATEGORIA/$SKILL_ID/ registry.json
git commit -m "feat: Add $SKILL_ID skill"
git push origin feature/skill-nome-da-skill
```

Abra o Pull Request no GitHub com:
- **Título**: `feat: Add [nome da skill]`
- **Descrição**: O que a skill faz, por que foi criada, como usar

---

## Editando uma Skill Existente

```bash
git checkout -b fix/skill-nome-da-skill

# Edite o arquivo
vim skills/core/judicial-monitoring/SKILL.md

# Atualize a versão no arquivo
# PATCH: 1.0.0 → 1.0.1 (correção)
# MINOR: 1.0.0 → 1.1.0 (nova funcionalidade)
# MAJOR: 1.0.0 → 2.0.0 (mudança incompatível)

# Valide
python scripts/validate-skills.py --skill core/judicial-monitoring

# Atualize registry
python scripts/generate-registry.py

git commit -am "fix: Correct classification in judicial-monitoring"
git push origin fix/skill-nome-da-skill
```

---

## Checklist antes do PR

- [ ] `SKILL.md` criado com todos os campos obrigatórios
- [ ] `README.md` com exemplo de uso
- [ ] Versão atualizada no `SKILL.md`
- [ ] `registry.json` atualizado
- [ ] `python scripts/validate-skills.py` passou sem erros
- [ ] Commit com mensagem clara (Conventional Commits)

---

## Convenções de Commit

Seguimos [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: Add credit-risk-analysis skill
fix: Correct judicial-monitoring classification
improve: Better examples in seo-audit-traderisk
docs: Update CONTRIBUTING.md
chore: Update registry.json
```

---

## Revisão e Merge

- PRs são revisados pelo maintainer (@adrianotomasoni)
- CI automático valida as skills
- Merge via squash para manter histórico limpo
