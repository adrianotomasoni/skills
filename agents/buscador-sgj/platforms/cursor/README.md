# Cursor — Adaptador

A regra fica em `.cursor/rules/buscador-sgj.mdc` (Project Rule, formato MDC).

- Para forcar a regra em todo o projeto, troque `alwaysApply: false` por `true`.
- Para acionar so em arquivos especificos, preencha `globs:` (ex.: `**/oportunidades/**`,
  `supabase/functions/**`).
- A regra referencia `prompts/system_prompt.md`, `schemas/parecer.schema.json`,
  `docs/quadro_normativo.md` e `examples/casos_referencia.md` — mantenha esses caminhos.

Legado: se usar a versao antiga, copie o conteudo de `prompts/system_prompt.md` para um
`.cursorrules` na raiz.
