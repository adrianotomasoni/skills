# receiving-code-review

> Categoria: `process` · Formato canônico multiplataforma.

## O que é
Como **receber** feedback de code review com rigor técnico: verificar cada sugestão antes de aplicar, em vez de concordar por reflexo ou implementar às cegas. Concordância performática ("boa ideia!") sem verificação é um anti-padrão.

## Quando dispara
- Você recebeu comentários de review (humano ou de um reviewer subagent).
- Antes de aplicar as sugestões — especialmente quando o feedback parece dúbio ou tecnicamente questionável.
- "O reviewer disse X, o que faço?".

## Como usar
- **Claude Code / Codex / Cursor:** invoque a skill ao receber o feedback; ela orienta verificar cada item contra o código/testes antes de mexer.
- **Gemini CLI / Copilot CLI:** ativada nativamente.
- **claude.ai / OpenAI / Manus:** cole `SKILL.md` e use o critério de verificação antes de aceitar/rejeitar cada ponto.

## Exemplo
Reviewer: "isso tem race condition". → em vez de "concordo, corrigindo", a skill exige reproduzir/raciocinar sobre a condição; se procede, corrige; se não, responde com a evidência técnica.

## Material de apoio
- Lado complementar (pedir review): `../requesting-code-review/`.
- Conteúdo completo em [`SKILL.md`](SKILL.md); metadados em [`skill.json`](skill.json).
