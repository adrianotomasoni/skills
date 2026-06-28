# test-driven-development

> Categoria: `process` · Formato canônico multiplataforma.

## O que é
TDD estrito: escreva o teste primeiro, veja-o falhar, escreva o código mínimo para passar. A Lei de Ferro: nenhum código de produção sem um teste falhando antes. É uma skill **rígida** — siga à risca.

## Quando dispara
- Qualquer nova feature, correção de bug, refatoração ou mudança de comportamento.
- ANTES de escrever código de implementação.
- Pensou "pulo o TDD só desta vez"? Isso é racionalização — a skill existe justamente para barrar isso.

## Como usar
- **Claude Code / Codex / Cursor:** invoque a skill antes de implementar; siga RED → verify RED → GREEN → verify GREEN → REFACTOR.
- **Gemini CLI / Copilot CLI:** ativada nativamente ao iniciar implementação.
- **claude.ai / OpenAI / Manus:** cole `SKILL.md` e siga o ciclo; não escreva implementação antes de ver o teste falhar.

## Exemplo
"Adicione retry com 3 tentativas" → escreve o teste que conta tentativas, roda e vê falhar pelo motivo certo, implementa o mínimo, vê passar, refatora mantendo verde.

## Material de apoio
- [`testing-anti-patterns.md`](testing-anti-patterns.md) — armadilhas ao adicionar mocks ou utilitários de teste (testar o mock em vez do código, método só-de-teste em produção, mock incompleto).
- Conteúdo completo em [`SKILL.md`](SKILL.md); metadados em [`skill.json`](skill.json).
