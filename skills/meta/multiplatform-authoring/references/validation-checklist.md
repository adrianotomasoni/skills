# Checklist de Validação Completa

## Estrutura
- [ ] `skills/<categoria>/<id>/SKILL.md` existe.
- [ ] `skills/<categoria>/<id>/skill.json` existe.
- [ ] `skills/<categoria>/<id>/README.md` existe.
- [ ] `<categoria>` ∈ {core, frontend, content, engineering, tools, process, meta}.

## Frontmatter (SKILL.md)
- [ ] Começa com bloco `---` … `---`.
- [ ] Contém **apenas** `name` e `description`.
- [ ] `name` casa com `^[a-z0-9-]+$` e é igual ao nome da pasta.
- [ ] Bloco de frontmatter ≤ 1024 caracteres.
- [ ] `description` em terceira pessoa, com gatilhos, sem resumir workflow.

## Corpo (SKILL.md)
- [ ] Tem `# Título`, `## Overview`, `## Quando usar`.
- [ ] Seções de conteúdo (`## Core Pattern` / `## Quick Reference` / `## Common Mistakes`).
- [ ] Persona/identidade está no `## Overview`, não no `description`.

## skill.json
- [ ] JSON válido.
- [ ] Campos: `id`, `name`, `version`, `category`, `status`, `type`, `tags`, `maintainer`, `dependencies`, `platforms`.
- [ ] `id` == nome da pasta == `name` do frontmatter.
- [ ] `status` ∈ {stable, beta, experimental, deprecated}.
- [ ] `type` ∈ {technique, pattern, reference}.
- [ ] `platforms` cobre as 8 plataformas.

## Agentes (AGENT.md / agent.json)
- [ ] `AGENT.md` com frontmatter `name`/`description`/`tools`/`model`.
- [ ] `agent.json` com `linkedSkills` e bloco `platforms`.
- [ ] Skills vinculadas existem no repo.

## Sem duplicados (inviolável)
- [ ] Não existe outra skill/agente com o mesmo `id` (nome de pasta).
- [ ] Não existe outra com o mesmo `name` no frontmatter.
- [ ] Nenhum agente tem `id` igual ao de uma skill.
- [ ] Não há skill/agente com **função equivalente** já no repo (`grep -ril "<tema>" skills/ agents/`); se houver, estenda a existente ou diferencie a `description`.

## Automático
- [ ] `python3 scripts/validate-skills.py --strict` → sem erros.
- [ ] `python3 scripts/validate-agents.py` → sem erros.
- [ ] `python3 scripts/generate-registry.py` → `registry.json` atualizado (descrições não vazias).
- [ ] `python3 scripts/export-adapters.py --dry-run` → sem erros.
- [ ] CI `.github/workflows/validate.yml` verde.
