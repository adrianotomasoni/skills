# subagent-driven-development

> Categoria: `process` · Formato canônico multiplataforma.

## O que é
Executa um plano na **sessão atual** despachando um implementer subagent novo por tarefa, uma revisão por tarefa (spec + qualidade), e uma revisão ampla do branch no fim. Contexto isolado por tarefa, sem poluição, com iteração rápida.

## Quando dispara
- Há um plano com tarefas em sua maioria independentes.
- Você quer ficar na mesma sessão (sem handoff para outra sessão).
- Sua plataforma tem subagents. Sem subagents, use executing-plans.

## Como usar
- **Claude Code:** controlador usa `Agent` por tarefa + scripts em `scripts/` para briefs e pacotes de diff.
- **Codex (`multi_agent`) / Copilot CLI / Gemini CLI:** despacha implementer/reviewer com `spawn_agent` / `task` / `invoke_agent`, preenchendo os templates.
- **claude.ai / OpenAI / Manus:** sem subagents nativos — prefira executing-plans.

## Exemplo
Plano de N tarefas → por tarefa: gera brief, despacha implementer (TDD, commit, self-review), gera pacote de diff, despacha task-reviewer (spec ✅/❌ + qualidade), corrige Critical/Important, marca no ledger. No fim, revisão ampla do branch.

## Material de apoio
- [`implementer-prompt.md`](implementer-prompt.md) — template do implementer.
- [`task-reviewer-prompt.md`](task-reviewer-prompt.md) — template do reviewer por tarefa (spec + qualidade).
- `scripts/` — `task-brief`, `review-package`, `sdd-workspace` (handoffs por arquivo + ledger de progresso).
- Revisão final do branch: `../requesting-code-review/code-reviewer.md`.
- Conteúdo completo em [`SKILL.md`](SKILL.md); metadados em [`skill.json`](skill.json).
