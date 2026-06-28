# TradeRisk Frontend Design

Design system e padrões de UI do **produto TradeRisk**: cores, tipografia e padrões de
componentes para dashboards financeiros internos. Para apresentações/decks use
`apresentacao-alto-impacto`; para UI genérica fora do produto use `frontend-design`.

Stack: Next.js 14+ (App Router) · Tailwind CSS · shadcn/ui · Tremor/Recharts · Lucide ·
React Hook Form + Zod.

## Versão

**3.1.0**

## Quando usa (gatilhos)

- "Crie / ajuste esta tela ou componente do produto TradeRisk"
- "Aplique o design system nesta interface"
- "Padronize o visual deste dashboard financeiro"

## Como usar por plataforma

- **Claude Code / Cowork:** siga o método do `SKILL.md` (partir do shadcn/ui → tokens → padrões → estados → acessibilidade → densidade).
- **Implementação:** importe tokens de `design-system/colors.ts` e `typography.ts`; copie os componentes de `design-system/patterns.md`.

## Exemplo

> "Crie um card de KPI com a exposição total e variação."
> → `StatCard` com borda primária, valor em `font-mono tabular-nums` e delta com cor
> semântica de sucesso/erro (código em `design-system/patterns.md`).

## Estrutura

```
traderisk-frontend-design/
├── SKILL.md
├── README.md
└── design-system/
    ├── colors.ts       # tokens de cor + semânticos + mapeamento shadcn/Tailwind
    ├── typography.ts   # famílias, escala, lineHeight, letterSpacing, uso semântico
    └── patterns.md     # layout, tabelas, forms e componentes em código (tsx)
```

## Material de apoio

- [`design-system/colors.ts`](design-system/colors.ts)
- [`design-system/typography.ts`](design-system/typography.ts)
- [`design-system/patterns.md`](design-system/patterns.md)

> Valores proprietários exatos da marca aparecem como `TODO:` nos arquivos do design system.

## Tags

`design` `frontend` `react` `nextjs` `tailwind` `shadcn`
