---
name: traderisk-frontend-design
description: "Define o design system e a UI do produto TradeRisk — cores, tipografia e padrões de componentes. Use SEMPRE que houver: criar/ajustar telas ou componentes do produto TradeRisk, aplicar o design system, padronizar visual de dashboards financeiros internos. Não usar para apresentações/decks (use apresentacao-alto-impacto)."
---

# TradeRisk Frontend Design

## Overview

Você é o design system da TradeRisk. Ao criar interfaces, componentes ou layouts, siga rigorosamente estes padrões visuais e de código para garantir consistência em todo o produto.

## Quando usar

- Criar ou ajustar telas e componentes do produto TradeRisk
- Aplicar o design system (cores, tipografia, componentes) em uma interface do produto
- Padronizar o visual de dashboards e telas financeiras internas
- **Quando NÃO usar:** apresentações, decks ou pitches comerciais → use `apresentacao-alto-impacto`

## Core Pattern

### Stack Tecnológica

- **Framework**: Next.js 14+ (App Router)
- **Styling**: Tailwind CSS + shadcn/ui
- **Charts**: Tremor / Recharts
- **Icons**: Lucide React
- **Forms**: React Hook Form + Zod

### Paleta de Cores

```typescript
// Design tokens TradeRisk
export const colors = {
  primary: '#1E40AF',      // Azul TradeRisk
  primaryDark: '#1E3A8A',
  secondary: '#0EA5E9',    // Azul claro
  success: '#16A34A',
  warning: '#D97706',
  danger: '#DC2626',
  neutral: {
    50: '#F8FAFC',
    100: '#F1F5F9',
    900: '#0F172A',
  }
};
```

### Tipografia

- **Headings**: Inter (peso 600-700)
- **Body**: Inter (peso 400)
- **Monospace**: JetBrains Mono (dados financeiros)

### Padrões de Componente

#### Cards Financeiros
```tsx
<Card className="border-l-4 border-primary">
  <CardHeader>
    <CardTitle className="text-sm font-medium text-gray-500">
      {label}
    </CardTitle>
  </CardHeader>
  <CardContent>
    <div className="text-2xl font-bold font-mono">{value}</div>
  </CardContent>
</Card>
```

#### Badges de Status
- `stable`: verde (`bg-green-100 text-green-800`)
- `beta`: amarelo (`bg-yellow-100 text-yellow-800`)
- `deprecated`: vermelho (`bg-red-100 text-red-800`)

## Quick Reference

| Elemento | Padrão |
|----------|--------|
| Cor primária | `#1E40AF` (azul TradeRisk) |
| Fonte headings/body | Inter |
| Fonte dados financeiros | JetBrains Mono |
| Base de componentes | shadcn/ui |
| Charts | Tremor / Recharts |
| Ícones | Lucide React |
| Acessibilidade mínima | WCAG 2.1 AA |

## Método passo a passo

1. **Partir do shadcn/ui.** Nunca reimplemente do zero o que o shadcn/ui já entrega (Button, Card, Table, Dialog, Form, Badge). Use o componente base e estilize por cima com Tailwind. Isso garante acessibilidade e consistência de fábrica.
2. **Aplicar tokens de cor / tipografia.** Use os tokens de `design-system/colors.ts` e `design-system/typography.ts` — nunca hex soltos no JSX. Cores semânticas (`primary`, `success`, `danger`, `muted`) mapeiam para as CSS variables do shadcn (`--primary` etc.).
3. **Seguir padrões de layout / tabela / form.** Sidebar fixa + header com breadcrumb, conteúdo em grid responsivo. Tabelas com coluna numérica mono alinhada à direita; forms com label acima, validação Zod inline e submit no canto inferior direito. Detalhes em `design-system/patterns.md`.
4. **Estados e feedback.** Toda tela com dados tem loading (skeleton), empty e error states. Toast (sonner) para confirmações, Dialog modal para ações destrutivas. Nunca spinner isolado.
5. **Acessibilidade WCAG AA.** Contraste ≥ 4.5:1, foco visível (`focus-visible`), navegação completa por teclado, labels associados a inputs e ARIA nos componentes interativos.
6. **Densidade data-first.** Usuários B2B esperam muita informação por tela. Priorize densidade controlada: espaçamento compacto, tipografia clara, números em destaque com fonte mono. Dados nunca escondidos em texto pequeno.

## Exemplos de componente

Os exemplos completos em código (tsx) estão em `design-system/patterns.md`. Resumo dos padrões:

### StatCard financeiro

```tsx
<Card className="border-l-4 border-l-primary">
  <CardHeader className="pb-2">
    <CardTitle className="text-sm font-medium text-muted-foreground">Exposição total</CardTitle>
  </CardHeader>
  <CardContent>
    <div className="font-mono text-2xl font-bold tabular-nums">R$ 2.430.500</div>
    <p className="mt-1 text-xs text-success">+4,2% vs. mês anterior</p>
  </CardContent>
</Card>
```

### Coluna numérica em DataTable (mono, à direita)

```tsx
{
  accessorKey: "valor",
  header: () => <div className="text-right">Valor</div>,
  cell: ({ row }) => (
    <div className="text-right font-mono tabular-nums">
      {formatBRL(row.getValue("valor"))}
    </div>
  ),
}
```

### Badge de status

```tsx
const statusStyles = {
  stable: "bg-green-100 text-green-800",
  beta: "bg-yellow-100 text-yellow-800",
  deprecated: "bg-red-100 text-red-800",
} as const;

<Badge className={statusStyles[status]}>{label}</Badge>
```

### Form field com RHF + Zod

```tsx
<FormField
  control={form.control}
  name="valor"
  render={({ field }) => (
    <FormItem>
      <FormLabel>Valor da operação</FormLabel>
      <FormControl>
        <Input type="number" className="font-mono text-right" {...field} />
      </FormControl>
      <FormMessage />
    </FormItem>
  )}
/>
```

## Common Mistakes

- Reinventar componentes em vez de usar shadcn/ui como base → sempre partir do shadcn/ui.
- Esconder dados financeiros em texto pequeno → dados sempre em destaque (data-first).
- Layout com baixa densidade → usuários B2B esperam mais informação por tela.
- Ignorar contraste e navegação por teclado → manter WCAG 2.1 AA no mínimo.
- Usar hex soltos no JSX em vez dos tokens → centralize em `design-system/colors.ts`.
- Números financeiros em fonte proporcional → use `font-mono tabular-nums` para alinhamento de colunas.
- Esquecer empty/error states em telas de dados → projetar os quatro estados sempre.
- Spinner isolado para carregamento → preferir skeleton no formato da tabela/card.

## Referências / Embasamento

- [Tokens de cor](design-system/colors.ts)
- [Tokens de tipografia](design-system/typography.ts)
- [Padrões de componentes e layout](design-system/patterns.md)
