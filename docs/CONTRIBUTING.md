# Como Contribuir com Novas Skills

> **Leia primeiro:** a regra-mãe [`multiplatform-authoring`](../skills/meta/multiplatform-authoring/SKILL.md)
> e [MULTIPLATFORM.md](MULTIPLATFORM.md). Toda skill/agente segue o **formato canônico**
> (frontmatter YAML + `skill.json`).

## Pré-requisitos

- Git configurado com suas credenciais
- Acesso ao repositório `adrianotomasoni/skills`
- Python 3.8+ (para scripts de validação)

## Adicionando uma Nova Skill

### 0. Confira se já não existe (migração de skill global)

Se você está migrando uma skill do seu Claude global (`~/.claude/skills/`), confira
[`docs/MAPEAMENTO-NOMENCLATURA.md`](MAPEAMENTO-NOMENCLATURA.md) — o nome global e o nome no repo
podem divergir. Se já existir uma skill correspondente, **edite-a** (seção "Editando uma Skill
Existente" abaixo) em vez de criar uma pasta nova. Ao migrar com um nome diferente do original,
adicione uma linha nessa tabela no mesmo PR.

### 1. Crie a Branch

```bash
git checkout main
git pull origin main
git checkout -b feature/skill-nome-da-skill
```

### 2. Crie a Estrutura de Diretório

```bash
# Categorias: core / frontend / content / engineering / tools / process / meta
CATEGORIA=core
SKILL_ID=minha-nova-skill

mkdir -p skills/$CATEGORIA/$SKILL_ID
cp templates/SKILL-TEMPLATE.md skills/$CATEGORIA/$SKILL_ID/SKILL.md
cp templates/skill.json        skills/$CATEGORIA/$SKILL_ID/skill.json
```

### 3. Edite o SKILL.md (formato canônico)

Frontmatter YAML com **apenas** `name` + `description` (bloco ≤ 1024 chars):

```markdown
---
name: minha-nova-skill   # == nome da pasta, ^[a-z0-9-]+$
description: "[O que faz]. Use SEMPRE que houver: [gatilhos concretos]. Não usar para [fronteira] (use <outra-skill>)."
---

# Nome Legível

## Overview
## Quando usar
## Core Pattern
## Quick Reference
## Common Mistakes
```

Regras de `name`/`description` (terceira pessoa, gatilhos, **sem resumir workflow**):
[naming-rules](../skills/meta/multiplatform-authoring/references/naming-rules.md).

### 4. Edite o skill.json + README.md

Preencha `version`, `category`, `status`, `type`, `tags`, `platforms` no `skill.json`.
Crie um `README.md` curto (o que é + como usar + tags).

### 5. Valide a Skill

```bash
python3 scripts/validate-skills.py --skill $CATEGORIA/$SKILL_ID
```

### 6. Atualize o Registry

```bash
python3 scripts/generate-registry.py
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

- [ ] `SKILL.md` com frontmatter (`name`==pasta, `description` no padrão de gatilhos, bloco ≤ 1024 chars)
- [ ] `skill.json` com `category`/`status`/`type` válidos e `platforms` preenchido
- [ ] `README.md` presente
- [ ] Versão atualizada no `skill.json`
- [ ] `python3 scripts/validate-skills.py --strict` passou sem erros
- [ ] `python3 scripts/generate-registry.py` rodado e `registry.json` commitado
- [ ] (agentes) `python3 scripts/validate-agents.py` passou
- [ ] Commit com mensagem clara (Conventional Commits)

Checklist completo: [validation-checklist](../skills/meta/multiplatform-authoring/references/validation-checklist.md).

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
