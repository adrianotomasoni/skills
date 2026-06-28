# 🧠 Skills & Agents — Repositório-Mãe Multiplataforma

Repositório **central** de todas as skills e agentes de IA. Uma fonte canônica,
usável em **Claude, Claude Code, OpenAI (ChatGPT / Custom GPTs / Assistants),
Google Gemini / Gemini CLI, Cursor, GitHub Copilot, Codex e Manus**.

> **Princípio:** toda skill e todo agente nascem multiplataforma. Você escreve
> uma vez no formato canônico; um adaptador exporta para cada plataforma. A regra
> que governa isso é a skill [`multiplatform-authoring`](skills/meta/multiplatform-authoring/SKILL.md).

## 📊 Inventário

**33 skills · 2 agentes · 7 categorias** (índice completo em [`registry.json`](registry.json)).

| Categoria | Conteúdo |
|---|---|
| `meta` | **`multiplatform-authoring`** — a regra-mãe de autoria/governança |
| `core` | Negócio: `credit-risk-analysis`, `judicial-monitoring`, `licitaradar`, `seo-audit-traderisk`, `localiza-credor-rj`, `auditoria-de-seo-on-page` |
| `content` | `skill-traderisk-content-writer`, `internal-comms` |
| `frontend` | `traderisk-frontend-design`, `apresentacao-alto-impacto`, `frontend-design` |
| `engineering` | `api-design-restful`, `code-review-checklist`, `doc-coauthoring` |
| `tools` | `file-reading`, `pdf-operations`, `mcp-builder` |
| `process` | Engenharia de processo (estilo *superpowers*): `brainstorming`, `test-driven-development`, `systematic-debugging`, `writing-skills`, `writing-plans`, `executing-plans`, `subagent-driven-development`, `dispatching-parallel-agents`, `using-git-worktrees`, `using-superpowers`, `requesting-code-review`, `receiving-code-review`, `verification-before-completion`, `finishing-a-development-branch`, `frontend-design-process` |

Catálogo descritivo completo (o que faz, gatilhos, como usar em cada plataforma):
👉 **[docs/USAGE.md](docs/USAGE.md)**

## 📁 Estrutura

```
skills/
├── meta/          # governança (multiplatform-authoring)
├── core/          # skills de negócio
├── content/  frontend/  engineering/  tools/
└── process/       # skills de processo (superpowers)
agents/
├── _template/
├── credit-risk-analyst/    # → skill credit-risk-analysis
└── judicial-watcher/       # → skill judicial-monitoring
templates/         # SKILL-TEMPLATE.md, skill.json, AGENT-TEMPLATE.md, agent.json
scripts/           # validate-skills, validate-agents, generate-registry, export-adapters, sync-*
dist/              # adapters por plataforma (gerados, gitignored)
docs/              # USAGE, MULTIPLATFORM, INTEGRATION, CONTRIBUTING, ARCHITECTURE
registry.json      # índice master (schema 2.0.0)
```

## 🧩 Formato canônico (resumo)

Cada skill = pasta com:
- **`SKILL.md`** — frontmatter YAML com **só** `name` + `description` (≤ 1024 chars) + corpo.
- **`skill.json`** — metadados (`version`, `category`, `status`, `type`, `tags`, `platforms`…).
- **`README.md`**.

Detalhes e o porquê: [docs/MULTIPLATFORM.md](docs/MULTIPLATFORM.md) e a skill
[`multiplatform-authoring`](skills/meta/multiplatform-authoring/SKILL.md).

## 🚀 Uso rápido

```bash
# Validar tudo
python3 scripts/validate-skills.py --strict
python3 scripts/validate-agents.py

# Regenerar o índice
python3 scripts/generate-registry.py --summary

# Exportar adapters por plataforma (dist/)
python3 scripts/export-adapters.py

# Instalar no Claude Code local
./scripts/sync-to-claude.sh
```

Por plataforma (Claude.ai, OpenAI, Gemini, Cursor, Copilot, Codex, Manus):
ver [docs/USAGE.md](docs/USAGE.md) e [docs/INTEGRATION.md](docs/INTEGRATION.md).

## ➕ Incluir novas skills e novos agentes

> Antes de criar/editar **qualquer** skill ou agente, consulte a regra-mãe
> [`multiplatform-authoring`](skills/meta/multiplatform-authoring/SKILL.md).

### 🚫 Regra inviolável: SEM duplicados

**Nunca** inclua uma skill ou agente duplicado. Antes de criar, verifique:

```bash
# 1. O id/nome já existe? (skills e agentes têm namespaces próprios, mas ids não se repetem)
python3 scripts/generate-registry.py >/dev/null && \
python3 -c "import json;d=json.load(open('registry.json'));\
print('skills:', sorted(s['id'] for s in d['skills']));\
print('agents:', sorted(a['id'] for a in d['agents']))"

# 2. Já existe algo com função equivalente? (busque por palavras-chave)
grep -ril "<tema/gatilho>" skills/ agents/
```

O bloqueio é **automático**: `validate-skills.py` e `validate-agents.py` recusam
(exit 1) ids de skill repetidos, nomes de frontmatter repetidos, ids de agente
repetidos e colisão de id entre agente e skill. O CI roda isso em todo PR.
Se a função já existe, **estenda/ajuste a skill existente** em vez de criar outra;
se o escopo é de fato diferente, **diferencie na `description`** declarando a
fronteira ("Não usar para X (use `outra-skill`)").

### Nova SKILL

```bash
mkdir -p skills/<categoria>/<id>            # categoria: core|content|frontend|engineering|tools|process|meta
cp templates/SKILL-TEMPLATE.md skills/<categoria>/<id>/SKILL.md
cp templates/skill.json        skills/<categoria>/<id>/skill.json
# edite: name (==<id>), description (padrão de gatilhos + fronteira), corpo e metadados; crie README.md
python3 scripts/validate-skills.py --strict
python3 scripts/generate-registry.py
```

### Novo AGENTE

```bash
mkdir -p agents/<id>
cp templates/AGENT-TEMPLATE.md agents/<id>/AGENT.md
cp templates/agent.json        agents/<id>/agent.json
# edite frontmatter (name==<id>, description com fronteira, tools, model), agent.json (linkedSkills, platforms), README.md
# (opcional) bundle de apoio: reference/ (núcleo canônico), examples/, docs/, schemas/, platforms/, run_agent.py
python3 scripts/validate-agents.py
python3 scripts/generate-registry.py
```

Detalhes: [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) ·
formato de agente: [agent-format](skills/meta/multiplatform-authoring/references/agent-format.md).

## 🛫 Invocar um agente/skill em cada novo projeto

Para usar um agente (ex.: `buscador-sgj`) ou skill dentro de outro projeto:

```bash
# Instala no projeto-alvo (.claude/skills, .claude/agents, .cursor/rules)
./scripts/install-into-project.sh --agent buscador-sgj --target ../meu-projeto
./scripts/install-into-project.sh --skill credit-risk-analysis --target ../meu-projeto
./scripts/install-into-project.sh --all --target ../meu-projeto     # tudo

# Ou rode o agente via API (provider-agnóstico), a partir do núcleo canônico
pip install -r agents/buscador-sgj/requirements.txt
python agents/buscador-sgj/run_agent.py --provider anthropic \
  --input agents/buscador-sgj/examples/processo_exemplo.json
```

Por plataforma (Claude.ai, OpenAI, Gemini, Cursor, Lovable, Manus), cada agente
traz um guia em `agents/<id>/platforms/`. Mapa geral: [docs/MULTIPLATFORM.md](docs/MULTIPLATFORM.md).

## 🔐 Segurança

- Nunca commite credenciais/tokens. Use `.gitignore` e `.env.example`.
- Valide antes do push; o CI bloqueia formato inválido.

## 📄 Licença

MIT — ver [LICENSE](LICENSE).

---

**Maintainer:** Adriano Tomasoni · adriano@traderisk.com.br
