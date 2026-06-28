---
name: multiplatform-authoring
description: "Regra-mãe de autoria deste repositório: define o formato canônico portável de TODA skill e agente para funcionar em Claude, Claude Code, OpenAI/ChatGPT, Gemini, Cursor, Copilot, Codex e Manus. Use SEMPRE que houver: criar uma skill ou agente novo, editar/revisar um existente, padronizar descrição, decidir onde um arquivo vai em cada plataforma, ou validar o repositório. É obrigatória antes de adicionar qualquer skill/agente. Não usar para o conteúdo de domínio de uma skill específica (isso vive na própria skill)."
---

# Multiplatform Authoring — A Regra-Mãe

## Overview

Este é o **repositório-mãe** de skills e agentes. **Princípio central:** toda
skill e todo agente nascem **multiplataforma**. Você escreve UMA fonte canônica;
um adaptador a exporta para cada plataforma. Nada entra no repo sem seguir este
contrato. Esta skill governa e administra essa regra.

> Autoria de skills É TDD aplicado a documentação — para a técnica de *escrever*
> uma boa skill, use a skill `writing-skills` (em `skills/process/`). Esta skill
> adiciona a camada **multiplataforma + governança** por cima dela.

## Quando usar

- Criar uma skill ou agente novo (use ANTES de começar).
- Editar, revisar ou padronizar uma skill/agente existente.
- Decidir onde cada arquivo vai em cada plataforma / como exportar.
- Validar o repositório ou auditar conformidade.
- **Quando NÃO usar:** para o conteúdo de domínio de uma skill (taxonomias,
  fórmulas) — isso vive dentro da própria skill.

## Core Pattern — O Contrato Canônico

Cada **skill** = uma pasta `skills/<categoria>/<id>/` com:

1. **`SKILL.md`** — começa com frontmatter YAML contendo **apenas** dois campos:
   - `name`: kebab-case `^[a-z0-9-]+$`, **igual ao nome da pasta**.
   - `description`: terceira pessoa, no padrão de gatilhos (ver abaixo).
   - O bloco de frontmatter inteiro deve ter **≤ 1024 caracteres**.
   - Corpo: `# Título` / `## Overview` / `## Quando usar` / `## Core Pattern` /
     `## Quick Reference` / `## Common Mistakes`.
2. **`skill.json`** (sidecar) — metadados que **NÃO** entram no prompt:
   `version`, `category`, `status`, `type`, `tags`, `maintainer`,
   `dependencies`, `platforms`. (Schema em `templates/skill.json`.)
3. `README.md` + apoio opcional (`templates/`, `examples/`, `tests/`).

Cada **agente** = `agents/<id>/` com `AGENT.md` (frontmatter
`name`/`description`/`tools`/`model` — superset do subagent do Claude Code) +
`agent.json` sidecar. Ver `references/agent-format.md`.

**Por que frontmatter mínimo + sidecar:** o frontmatter é injetado no prompt em
todas as plataformas que leem o padrão agentskills.io; mantê-lo enxuto evita
estourar o limite de 1024 chars e impede que bookkeeping vaze para o contexto.

## Padrão de description (gatilhos, não workflow)

```
[O que faz, 1 frase]. Use SEMPRE que houver: [gatilhos concretos —
pedidos/verbos típicos]. Não usar para [fronteira] (use <outra-skill>).
```

- Terceira pessoa. Comece pelos **gatilhos**, não pela persona.
- **NUNCA resuma o workflow** no `description` — isso faz o agente seguir o
  resumo em vez de ler a skill. Detalhes em `references/naming-rules.md`.

## Quick Reference — Mapa por Plataforma

| Plataforma | Onde fica | Formato | Adaptação |
|---|---|---|---|
| Claude.ai | upload em Knowledge / Project | mantém frontmatter | nenhuma |
| Claude Code | `~/.claude/skills/<id>/` | frontmatter (NÃO lê o alias) | nenhuma |
| Codex | `~/.codex/skills/` ou `~/.agents/skills/` | frontmatter | nenhuma |
| Gemini CLI | `~/.gemini/skills/` ou `~/.agents/skills/` | frontmatter | mapa via GEMINI.md |
| Copilot CLI | `~/.copilot/skills/` ou `~/.agents/skills/` | frontmatter | nenhuma |
| Cursor | `.cursor/rules/<id>.mdc` | frontmatter `.mdc` | converter p/ `.mdc` |
| OpenAI GPT/Assistant | Instructions / upload | **sem** frontmatter | strip → preâmbulo |
| Manus | config local do agente | **sem** frontmatter | strip |

Detalhe por plataforma em `references/` (um arquivo por plataforma) e a matriz
completa em `references/platform-matrix.md`. A exportação é automatizada por
`scripts/export-adapters.py` (gera `dist/<plataforma>/`).

## Checklist de Validação (antes de commitar)

- [ ] Pasta `skills/<categoria>/<id>/` com `SKILL.md` + `skill.json` + `README.md`.
- [ ] `name` == nome da pasta, `^[a-z0-9-]+$`.
- [ ] Frontmatter só com `name`+`description`, bloco ≤ 1024 chars.
- [ ] `description` no padrão de gatilhos, sem resumir workflow.
- [ ] `skill.json` com `category` válida (core/frontend/content/engineering/tools/process/meta) e `platforms` preenchido.
- [ ] `python3 scripts/validate-skills.py --strict` passa.
- [ ] `python3 scripts/generate-registry.py` atualizado e commitado.
- [ ] Lista completa em `references/validation-checklist.md`.

## Administração & Enforcement

- **Fonte da verdade:** este repo no GitHub. Todas as plataformas derivam dele.
- **🚫 Sem duplicados (inviolável):** nunca inclua skill/agente com id ou nome já
  existente, nem com função equivalente a uma já presente. Antes de criar, busque
  (`grep -ril "<tema>" skills/ agents/`) e cheque o `registry.json`. Se já existe,
  estenda a existente; se o escopo difere, diferencie na `description` (fronteira
  "Não usar para X"). `validate-skills.py`/`validate-agents.py` recusam (exit 1)
  ids/nomes repetidos e colisão de id entre agente e skill.
- **Enforcement automático:** `validate-skills.py` + `.github/workflows/validate.yml`
  recusam skills/agentes fora do contrato (frontmatter, naming, 1024 chars, categoria, duplicados).
- **Distribuição:** `export-adapters.py` gera as versões por plataforma em `dist/`;
  `sync-*.sh` publica nos destinos locais.
- **Evolução desta regra:** mudou o contrato? Atualize esta SKILL.md, os
  `references/`, os `templates/` e os scripts de validação **no mesmo PR**.

## Common Mistakes

- ❌ Metadados como comentários `# ID:` no topo → ✅ frontmatter YAML + `skill.json`.
- ❌ `description` em primeira pessoa ou resumindo o passo a passo → ✅ gatilhos em terceira pessoa.
- ❌ `name` com maiúsculas/espaços ou ≠ pasta → ✅ kebab-case igual à pasta.
- ❌ Escrever só para Claude → ✅ validar o mapa de plataformas e rodar `export-adapters.py`.
- ❌ Enfiar `version`/`tags` no frontmatter → ✅ vão no `skill.json`.
