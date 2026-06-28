# Code Review Checklist

## O que é

Skill para revisar código com um checklist estruturado (segurança, qualidade,
performance, testabilidade e manutenibilidade) e dar feedback acionável e
priorizado. Alinhada ao stack TradeRisk (Python, Edge Functions Deno,
React/TypeScript), com checklists específicos por stack.

## Gatilhos (quando dispara)

- Revisar um PR ou trecho de código.
- Pedidos como "faz um code review", "revisa esse código", "esse código está bom?".
- Avaliar qualidade antes de merge.
- Padronizar o processo de review do time.

Não dispara para escrever código novo do zero nem para design de API (use
`api-design-restful`).

## Como usar por plataforma

- **Claude Code / Cursor:** rode sobre o diff do PR; a skill aplica o método e os
  checklists e devolve feedback classificado (bloqueante/sugestão/nit).
- **Outros assistentes:** cole o diff e referencie `SKILL.md` + o checklist do stack.

## Exemplo de uso

> "Revisa esse PR que adiciona um formulário em React com Supabase."

A skill checa contexto e testes, passa pelo checklist de segurança e qualidade,
aplica `react.md` e `supabase.md` e prioriza os pontos de bloqueio no topo.

## Material de apoio

- [`SKILL.md`](SKILL.md) — método passo a passo e como dar feedback.
- [`checklists/react.md`](checklists/react.md) — React (estado, acessibilidade, performance, forms, testes).
- [`checklists/typescript.md`](checklists/typescript.md) — TypeScript (tipagem, segurança de tipos, config).
- [`checklists/supabase.md`](checklists/supabase.md) — Supabase (RLS, Edge Functions, performance, migrations).

## Tags

`code-review` `react` `typescript` `supabase` `engineering`
