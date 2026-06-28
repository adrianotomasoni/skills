# brainstorming

> Categoria: `process` · Formato canônico multiplataforma.

## O que é
Skill de descoberta que roda **antes** de qualquer trabalho criativo. Explora intenção do usuário, requisitos e design antes de escrever código — e produz um documento de spec que outras skills (writing-plans, executing-plans) consomem.

## Quando dispara
- "Vamos construir X", "adicione a funcionalidade Y", "crie um componente Z".
- Qualquer pedido que mude comportamento sem requisitos fechados.
- Antes de entrar em plan mode. Na ordem de prioridade das skills, brainstorming vem primeiro.

## Como usar
- **Claude Code / Codex / Cursor:** invoque a skill (`Skill`/nativa) ao receber o pedido; ela conduz as perguntas e gera a spec em `docs/superpowers/specs/`.
- **Gemini CLI / Copilot CLI:** ativada via `activate_skill` / tool `skill`; siga o roteiro de perguntas.
- **claude.ai / OpenAI / Manus:** cole o corpo de `SKILL.md` no início da conversa e siga o fluxo de exploração antes de propor solução.

## Exemplo
Usuário: "Quero um botão de exportar relatório." → a skill pergunta formato, escopo, casos de borda e fluxo do usuário antes de qualquer linha de código, fechando uma spec revisável.

## Material de apoio
- [`visual-companion.md`](visual-companion.md) — companion visual para sessões de brainstorming.
- [`spec-document-reviewer-prompt.md`](spec-document-reviewer-prompt.md) — prompt para revisar o documento de spec gerado.
- `scripts/` — servidor e templates HTML do companion visual.
- Conteúdo completo em [`SKILL.md`](SKILL.md); metadados em [`skill.json`](skill.json).
