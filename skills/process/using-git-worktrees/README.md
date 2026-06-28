# using-git-worktrees

> Categoria: `process` · Formato canônico multiplataforma.

## O que é
Garante um workspace isolado para a feature antes de começar, usando ferramentas nativas da plataforma ou, como fallback, `git worktree`. Evita misturar trabalho novo com mudanças não commitadas no diretório atual.

## Quando dispara
- Início de trabalho que precisa de isolamento do workspace atual.
- Antes de executar um plano de implementação (executing-plans / subagent-driven-development).
- "Comece essa feature numa branch separada".

## Como usar
- **Claude Code / Cursor:** invoque a skill no início; ela detecta se já há worktree/branch e cria um se necessário.
- **Codex / Copilot CLI / Gemini CLI:** detecta o ambiente git com comandos read-only (worktree vs detached HEAD) antes de criar; em sandboxes que bloqueiam push, orienta os controles nativos do app.
- **claude.ai / OpenAI / Manus:** sem git local — gere os comandos de worktree para o usuário rodar.

## Exemplo
"Vamos implementar o cache" → a skill cria `git worktree add ../proj-cache feature/cache`, isolando a feature do diretório principal.

## Material de apoio
- Detecção de ambiente git por plataforma: `../using-superpowers/references/codex-tools.md`.
- Conteúdo completo em [`SKILL.md`](SKILL.md); metadados em [`skill.json`](skill.json).
