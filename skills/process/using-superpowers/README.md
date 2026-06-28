# using-superpowers

> Categoria: `process` · Formato canônico multiplataforma.

## O que é
Skill de bootstrap: estabelece como encontrar e usar skills. A regra central — invocar qualquer skill potencialmente relevante **antes** de qualquer resposta ou ação, inclusive antes de perguntas de esclarecimento. Instruções do usuário (CLAUDE.md/AGENTS.md/GEMINI.md) sempre têm prioridade sobre as skills.

## Quando dispara
- No início de qualquer conversa/tarefa.
- Sempre que houver ao menos 1% de chance de uma skill se aplicar.
- É o ponto de entrada do sistema de skills — as demais skills de process partem daqui.

## Como usar
- **Claude Code:** invoque skills com a tool `Skill`. **Codex:** skills carregam nativamente. **Copilot CLI:** tool `skill`. **Gemini CLI:** `activate_skill`.
- **Antigravity (`agy`):** sem tool de skill — leia o `SKILL.md` com `view_file` (`IsSkillFile: true`).
- **claude.ai / OpenAI / Manus:** cole `SKILL.md` no início; trate a regra "skill antes de responder" manualmente.

## Exemplo
Usuário pede "corrige esse bug" → antes de qualquer coisa, invoca systematic-debugging (process primeiro), anuncia "Using systematic-debugging to...", e só então age.

## Material de apoio
- `references/claude-code-tools.md`, `references/codex-tools.md`, `references/copilot-tools.md`, `references/gemini-tools.md`, `references/pi-tools.md`, `references/antigravity-tools.md` — mapeamento de ações ("dispatch a subagent", "create a todo") para as tools de cada runtime e convenções de arquivo de instruções.
- Conteúdo completo em [`SKILL.md`](SKILL.md); metadados em [`skill.json`](skill.json).
