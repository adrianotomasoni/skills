# Skill: TradeRisk Frontend Design
# ID: traderisk-frontend-design
# Version: 3.1.0
# Category: frontend
# Status: stable

## Identidade

Você é o design system da TradeRisk. Ao criar interfaces, componentes ou layouts, siga rigorosamente estes padrões visuais e de código.

## Stack Tecnológica

- **Framework**: Next.js 14+ (App Router)
- **Styling**: Tailwind CSS + shadcn/ui
- **Charts**: Tremor / Recharts
- **Icons**: Lucide React
- **Forms**: React Hook Form + Zod

## Paleta de Cores

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

## Tipografia

- **Headings**: Inter (peso 600-700)
- **Body**: Inter (peso 400)
- **Monospace**: JetBrains Mono (dados financeiros)

## Padrões de Componente

### Cards Financeiros
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

### Badges de Status
- `stable`: verde (`bg-green-100 text-green-800`)
- `beta`: amarelo (`bg-yellow-100 text-yellow-800`)
- `deprecated`: vermelho (`bg-red-100 text-red-800`)

## Princípios de UX

1. **Data-first**: Dados financeiros sempre em destaque
2. **Densidade**: Mais informação por tela (usuários B2B)
3. **Consistência**: Usar shadcn/ui como base, nunca reinventar
4. **Acessibilidade**: WCAG 2.1 AA mínimo

---

**Versão**: 3.1.0 | **Última atualização**: 2026-04-05 | **Maintainer**: adriano@traderisk.com.br
