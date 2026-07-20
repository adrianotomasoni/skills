# Mapeamento de Nomenclatura — Skills Globais → Repositório

> Antes de criar uma skill nova (`docs/CONTRIBUTING.md`), confira esta tabela. Skills globais do
> Claude (`~/.claude/skills/`) e as skills deste repositório às vezes têm nomes diferentes para o
> mesmo conteúdo, porque o nome no repo segue a convenção `^[a-z0-9-]+$` curta (regra
> `skills/meta/multiplatform-authoring`) enquanto o nome global às vezes é mais descritivo. Se o seu
> conteúdo já está listado abaixo, **edite a skill existente** em vez de criar uma pasta nova.

Origem: levantamento feito em `docs/AUDITORIA-SKILLS.md` (§5.3) durante a auditoria de 2026-07-20.

| Nome como skill global (Claude) | Skill correspondente no repositório |
|---|---|
| `code-review-estruturado-checklist` | `engineering/code-review-checklist` |
| `design-de-api-restful-boas-praticas` | `engineering/api-design-restful` |
| `seo-auditoria-traderisk` / `seo-traderisk` | `core/seo-audit-traderisk` |
| `skill-traderisk-content-writer-seguro-de-credito-risco` | `content/skill-traderisk-content-writer` |
| `arquiteto-ciberseguranca` | `engineering/arquiteto-ciberseguranca` |

As demais skills globais autorais do usuário (`apresentacao-alto-impacto`,
`auditoria-de-seo-on-page`, `credit-risk-analysis`, `localiza-credor-rj`,
`traderisk-frontend-design`, `doc-coauthoring`, `mcp-builder`) já usam o mesmo nome nos dois
lugares — não precisam de entrada nesta tabela.

## Como manter esta tabela atualizada

Ao migrar uma skill global para o repo com um nome diferente do original, adicione uma linha aqui
no mesmo PR (veja o checklist em `CONTRIBUTING.md`).
