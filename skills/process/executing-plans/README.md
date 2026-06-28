# executing-plans

> Categoria: `process` · Formato canônico multiplataforma.

## O que é
Executa um plano de implementação já escrito, numa sessão separada, tarefa por tarefa, com checkpoints de revisão. É a alternativa a subagent-driven-development quando você não tem (ou não quer) subagents no fluxo.

## Quando dispara
- Existe um arquivo de plano (ex.: `docs/superpowers/plans/...`) pronto para ser executado.
- "Implemente este plano", "execute as tarefas do plano".
- NÃO dispara para tarefas sem plano escrito — nesse caso use brainstorming + writing-plans antes.

## Como usar
- **Claude Code / Codex / Cursor:** invoque a skill; ela lê o plano inteiro, cria um todo por tarefa e executa em sequência com revisão por tarefa.
- **Gemini CLI / Copilot CLI:** ativada nativamente; o fluxo de revisão usa subagents quando disponíveis.
- **claude.ai / OpenAI / Manus:** cole `SKILL.md` e siga o passo a passo; sem subagents, releia o diff com olhos críticos a cada tarefa.

## Exemplo
Plano de 3 tarefas → lê tudo, levanta a única inconsistência ao parceiro, executa cada tarefa com TDD + verificação + revisão, e fecha com finishing-a-development-branch.

## Material de apoio
- Template de revisão: `../requesting-code-review/code-reviewer.md`.
- Suporte a subagents por plataforma: `../using-superpowers/references/`.
- Conteúdo completo em [`SKILL.md`](SKILL.md); metadados em [`skill.json`](skill.json).
