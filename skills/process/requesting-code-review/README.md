# requesting-code-review

> Categoria: `process` · Formato canônico multiplataforma.

## O que é
Como **pedir** code review: despachar um reviewer subagent com contexto preciso (o diff e os requisitos, nunca o histórico da sua sessão) para pegar problemas antes que se propaguem.

## Quando dispara
- Após cada tarefa em subagent-driven-development.
- Ao concluir uma feature relevante ou antes de fazer merge em main.
- Opcional mas valioso: quando travado, antes de refatorar, depois de corrigir um bug complexo.

## Como usar
- **Claude Code:** pegue `BASE_SHA`/`HEAD_SHA`, preencha o template `code-reviewer.md` e despache via `Agent`.
- **Codex / Copilot CLI / Gemini CLI:** mesmo template, despachado por `spawn_agent` / `task` / `invoke_agent`.
- **claude.ai / OpenAI / Manus:** sem subagents, cole o template e o diff numa nova conversa "limpa" para obter a revisão.

## Exemplo
Concluiu a Task 2 → `BASE_SHA`/`HEAD_SHA`, despacha reviewer com descrição + requisitos; ele devolve Strengths / Issues (Critical/Important/Minor) / verdict. Corrige Critical e Important antes de seguir.

## Material de apoio
- [`code-reviewer.md`](code-reviewer.md) — template do prompt de reviewer (placeholders, formato de saída, exemplo).
- Lado complementar (receber review): `../receiving-code-review/`.
- Conteúdo completo em [`SKILL.md`](SKILL.md); metadados em [`skill.json`](skill.json).
