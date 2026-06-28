# verification-before-completion

> Categoria: `process` · Formato canônico multiplataforma.

## O que é
Antes de afirmar que algo está "pronto", "corrigido" ou "passando", você roda o comando de verificação e confirma a saída. Evidência antes de afirmação, sempre. Proíbe alegações de sucesso sem prova.

## Quando dispara
- Prestes a dizer "feito", "funciona", "testes passam", "bug corrigido".
- Antes de commitar ou abrir PR.
- Sempre que a tentação for declarar sucesso de memória ou por suposição.

## Como usar
- **Claude Code / Codex / Cursor:** invoque a skill no momento de concluir; ela exige rodar a verificação real (testes, build, lint) e ler a saída antes de afirmar.
- **Gemini CLI / Copilot CLI:** ativada nativamente antes de marcar tarefa concluída.
- **claude.ai / OpenAI / Manus:** cole `SKILL.md`; se não puder executar, declare explicitamente que a verificação não foi rodada.

## Exemplo
"O bug está corrigido." → a skill bloqueia até você rodar `npm test`, ver a saída verde e pristine, e só então afirmar — citando o comando e o resultado.

## Material de apoio
- Conteúdo completo em [`SKILL.md`](SKILL.md); metadados em [`skill.json`](skill.json).
