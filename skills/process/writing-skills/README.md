# writing-skills

> Categoria: `process` · Formato canônico multiplataforma.

## O que é
Como criar, editar e validar skills antes de publicar. Trata a autoria de skills como TDD aplicado a documentação de processo: rode cenários sem a skill (RED), escreva a skill (GREEN), feche brechas de racionalização (REFACTOR).

## Quando dispara
- "Crie uma skill para X", "edite a skill Y", "essa skill está sendo ignorada".
- Antes de publicar qualquer skill que imponha disciplina (que o agente teria incentivo para burlar).
- Ao revisar frontmatter (name/description ≤1024 chars) e estrutura de arquivos de apoio.

## Como usar
- **Claude Code / Codex / Cursor:** invoque a skill; ela orienta estrutura, escrita do `SKILL.md`, e teste com subagents sob pressão.
- **Gemini CLI / Copilot CLI:** ativada nativamente ao trabalhar em skills.
- **claude.ai / OpenAI / Manus:** cole `SKILL.md` e siga o ciclo RED-GREEN-REFACTOR para a skill nova.

## Exemplo
Escrever uma skill de TDD → roda cenários de pressão (prazo, custo afundado) sem a skill, captura as racionalizações verbatim, e escreve contadores explícitos até o agente cumprir a regra sob pressão máxima.

## Material de apoio
- [`testing-skills-with-subagents.md`](testing-skills-with-subagents.md) — metodologia completa de teste (cenários de pressão, tabelas de racionalização, meta-teste).
- [`anthropic-best-practices.md`](anthropic-best-practices.md) — boas práticas de autoria de skills.
- [`persuasion-principles.md`](persuasion-principles.md) — princípios usados para construir pressão nos cenários de teste.
- `examples/CLAUDE_MD_TESTING.md`, `graphviz-conventions.dot`, `render-graphs.js` — exemplo de campanha de teste e convenções/render de diagramas.
- Mapas de tool por runtime: `../using-superpowers/references/`.
- Conteúdo completo em [`SKILL.md`](SKILL.md); metadados em [`skill.json`](skill.json).
