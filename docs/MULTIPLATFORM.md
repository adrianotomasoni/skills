# 🌐 MULTIPLATFORM — A Regra e o Fluxo de Distribuição

Este repositório é a **fonte única** das suas skills e agentes. Você escreve
**uma vez** no formato canônico; um adaptador exporta para cada plataforma.

A regra que governa tudo isso é a skill [`multiplatform-authoring`](../skills/meta/multiplatform-authoring/SKILL.md)
(categoria `meta`). Esta página é o resumo operacional.

## 1. Formato canônico

Cada skill = `skills/<categoria>/<id>/` com:

| Arquivo | Papel |
|---|---|
| `SKILL.md` | Frontmatter YAML (**só** `name` + `description`, ≤ 1024 chars) + corpo. É o que vai pro prompt. |
| `skill.json` | Metadados que **não** vão pro prompt: `version`, `category`, `status`, `type`, `tags`, `dependencies`, `platforms`. |
| `README.md` | Apresentação humana. |

Agentes = `agents/<id>/` com `AGENT.md` (frontmatter `name`/`description`/`tools`/`model`) + `agent.json`.

**Por quê frontmatter mínimo + sidecar?** O frontmatter é injetado no contexto em
toda plataforma que segue o padrão agentskills.io. Mantê-lo enxuto respeita o
limite de 1024 chars e evita poluir o prompt com bookkeeping.

## 2. Padrão de `description`

```
[O que faz]. Use SEMPRE que houver: [gatilhos concretos]. Não usar para [fronteira] (use <outra-skill>).
```
Terceira pessoa, comece pelos gatilhos, **nunca resuma o workflow** (senão o agente
segue o resumo em vez de ler a skill). Ver
[naming-rules](../skills/meta/multiplatform-authoring/references/naming-rules.md).

## 3. Mapa por plataforma

| Plataforma | Onde fica | Frontmatter | Adaptação |
|---|---|---|---|
| Claude.ai | upload Knowledge | mantém | nenhuma |
| Claude Code | `~/.claude/skills/<id>/` | mantém | nenhuma (não lê o alias) |
| Codex | `~/.codex/skills/` ou `~/.agents/skills/` | mantém | nenhuma |
| Gemini CLI | `~/.gemini/skills/` ou `~/.agents/skills/` | mantém | mapa via GEMINI.md |
| Copilot CLI | `~/.copilot/skills/` ou `~/.agents/skills/` | mantém | nenhuma |
| Cursor | `.cursor/rules/<id>.mdc` | `.mdc` | converte p/ `.mdc` |
| OpenAI | Instructions / Knowledge | **remove** | strip → preâmbulo |
| Manus | config local | **remove** | strip |

Detalhe por plataforma: um arquivo por plataforma em
[`references/`](../skills/meta/multiplatform-authoring/references/).

### Alias cross-runtime `~/.agents/skills/`
Codex, Copilot CLI e Gemini CLI compartilham `~/.agents/skills/`. Claude Code **não**
— para ele, sempre `~/.claude/skills/`.

## 4. Distribuição automatizada

```bash
# Gera dist/<plataforma>/ a partir das skills canônicas
python3 scripts/export-adapters.py            # todas as plataformas
python3 scripts/export-adapters.py --platform openai   # só uma
python3 scripts/export-adapters.py --dry-run  # só mostra o que faria

# Instala no Claude Code local
./scripts/sync-to-claude.sh

# Distribui .cursorrules / .mdc para projetos Cursor
./scripts/sync-to-cursor.sh
```
`dist/` é gerado e **gitignored** — nunca edite à mão.

## 5. Governança / Enforcement

- `scripts/validate-skills.py --strict` e `scripts/validate-agents.py` recusam
  qualquer skill/agente fora do contrato.
- `.github/workflows/validate.yml` roda a validação + checa o `registry.json` em cada PR.
- Mudou o contrato? Atualize **no mesmo PR**: a skill `multiplatform-authoring`,
  os `references/`, os `templates/` e os scripts de validação.

## 6. Criar uma skill nova (checklist rápido)

```bash
mkdir -p skills/<categoria>/<id>
cp templates/SKILL-TEMPLATE.md skills/<categoria>/<id>/SKILL.md
cp templates/skill.json        skills/<categoria>/<id>/skill.json
# edite name (==<id>), description (padrão de gatilhos), corpo e metadados
python3 scripts/validate-skills.py --skill <categoria>/<id>
python3 scripts/generate-registry.py
```
Checklist completo: [validation-checklist](../skills/meta/multiplatform-authoring/references/validation-checklist.md).
