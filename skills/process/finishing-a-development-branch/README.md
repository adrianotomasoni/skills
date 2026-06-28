# finishing-a-development-branch

> Categoria: `process` · Formato canônico multiplataforma.

## O que é
Conduz o encerramento de um branch de desenvolvimento: verifica que os testes passam e apresenta opções estruturadas (merge, abrir PR, ou limpeza/descarte) em vez de decidir por conta própria.

## Quando dispara
- Implementação concluída e todos os testes passando.
- "Terminei, e agora?", "podemos fazer merge?", "abre o PR".
- Ao final de executing-plans / subagent-driven-development.

## Como usar
- **Claude Code / Codex / Cursor:** invoque a skill ao concluir; ela roda a suíte, confirma o estado do branch e oferece as opções.
- **Gemini CLI / Copilot CLI:** ativada nativamente; detecta worktree/branch antes de propor ações de push/PR.
- **claude.ai / OpenAI / Manus:** cole `SKILL.md`; gere os comandos de merge/PR para o usuário executar onde tiver acesso ao git.

## Exemplo
Feature pronta → a skill roda os testes, confirma verde, e pergunta: (a) merge em main, (b) abrir PR, (c) manter branch. Você escolhe e ela executa.

## Material de apoio
- Detecção de ambiente git (worktree/detached HEAD) por plataforma: `../using-superpowers/references/codex-tools.md`.
- Conteúdo completo em [`SKILL.md`](SKILL.md); metadados em [`skill.json`](skill.json).
