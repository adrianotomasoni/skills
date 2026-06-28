# multiplatform-authoring — A Regra-Mãe

A skill de **governança** deste repositório. Define o formato canônico portável
de toda skill e agente para funcionar em **Claude, Claude Code, OpenAI, Gemini,
Cursor, Copilot, Codex e Manus**, e como esse padrão é validado e distribuído.

## Quando aplicar
Antes de **criar ou editar** qualquer skill/agente, e ao validar/auditar o repo.

## O que ela contém
- `SKILL.md` — o contrato canônico, padrão de descrição, mapa por plataforma,
  checklist e o modelo de enforcement.
- `references/` — detalhe operacional:
  - `platform-matrix.md` — matriz completa (onde fica / frontmatter / ativação).
  - `claude.md`, `claude-code.md`, `openai.md`, `gemini.md`, `cursor.md`,
    `copilot.md`, `codex.md`, `manus.md` — instalação e uso por plataforma.
  - `naming-rules.md` — nomenclatura e padrão de `description`.
  - `validation-checklist.md` — checklist completo.
  - `agent-format.md` — formato portável de agente.

## Relação com `writing-skills`
`writing-skills` (em `skills/process/`) ensina a *técnica* de escrever uma boa
skill (TDD de documentação). `multiplatform-authoring` adiciona a camada
**multiplataforma + governança** por cima.

## Tags
`governanca` `multiplataforma` `autoria` `padrao` `regra` `skills` `agentes`
