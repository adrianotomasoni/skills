# Frontend Design Patterns

Princípios gerais de design de interface (layout, hierarquia, responsividade, performance
percebida e acessibilidade) para web/app **fora** do produto TradeRisk. Para o produto, use
`traderisk-frontend-design`.

## Quando usa (gatilhos)

- "Melhore a aparência / UX desta tela"
- "Defina breakpoints / responsividade / comportamento mobile"
- "Revise a acessibilidade desta UI"
- "Como deixar este carregamento mais rápido (percebido)?"

## Como usar por plataforma

- **Claude Code / Cowork:** a skill é carregada automaticamente ao trabalhar em UI genérica; siga o método passo a passo do `SKILL.md`.
- **Revisão de UI existente:** rode o checklist de `reference/ui-accessibility-checklist.md` sobre a tela.

## Exemplo

> "Esta tela de listagem só tem o estado com dados. Adicione loading, empty e error."
> → a skill orienta skeleton no formato do conteúdo, empty state com próxima ação e
> error state com `role="alert"` + retry (exemplos no `SKILL.md`).

## Material de apoio

- [`SKILL.md`](SKILL.md) — método, exemplos e common mistakes.
- [`reference/ui-accessibility-checklist.md`](reference/ui-accessibility-checklist.md) — checklist acionável de UI e acessibilidade (WCAG 2.1 AA).

## Tags

`design` `frontend` `patterns` `ux` `acessibilidade` `responsividade`
