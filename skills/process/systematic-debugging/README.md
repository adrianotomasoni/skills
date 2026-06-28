# systematic-debugging

> Categoria: `process` · Formato canônico multiplataforma.

## O que é
Método disciplinado para qualquer bug, falha de teste ou comportamento inesperado: investigar a causa-raiz **antes** de propor correções, em vez de aplicar palpites que só mascaram o sintoma.

## Quando dispara
- Um teste quebrou, há um stack trace, ou o comportamento diverge do esperado.
- "Por que isso está falhando?", "corrige esse bug".
- ANTES de escrever qualquer fix — palpite sem causa-raiz é o anti-padrão central.

## Como usar
- **Claude Code / Codex / Cursor:** invoque a skill ao topar com o bug; ela conduz rastreamento de causa-raiz, hipótese, e fix com teste de regressão.
- **Gemini CLI / Copilot CLI:** ativada nativamente ao detectar falha.
- **claude.ai / OpenAI / Manus:** cole `SKILL.md` e siga o roteiro de investigação antes de tocar no código.

## Exemplo
Teste intermitente → em vez de aumentar um timeout, a skill leva ao rastreamento da causa (espera baseada em condição), escreve o teste que reproduz, e só então corrige.

## Material de apoio
- [`root-cause-tracing.md`](root-cause-tracing.md) — rastrear o sintoma até a origem.
- [`defense-in-depth.md`](defense-in-depth.md) — camadas de proteção contra a classe do bug.
- [`condition-based-waiting.md`](condition-based-waiting.md) e [`condition-based-waiting-example.ts`](condition-based-waiting-example.ts) — eliminar flakiness por espera condicional.
- [`find-polluter.sh`](find-polluter.sh) — achar o teste que polui o estado compartilhado.
- Conteúdo completo em [`SKILL.md`](SKILL.md); metadados em [`skill.json`](skill.json).
