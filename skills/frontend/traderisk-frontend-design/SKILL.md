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

## Common Mistakes

- Reinventar componentes em vez de usar shadcn/ui como base → sempre partir do shadcn/ui.
- Esconder dados financeiros em texto pequeno → dados sempre em destaque (data-first).
- Layout com baixa densidade → usuários B2B esperam mais informação por tela.
- Ignorar contraste e navegação por teclado → manter WCAG 2.1 AA no mínimo.
