---
name: frontend-design
description: "Aplica princípios de design de interface (layout, hierarquia, responsividade, performance, acessibilidade) para web/app em geral. Use SEMPRE que houver: melhorar a aparência ou UX de uma interface genérica, definir breakpoints/responsividade, revisar acessibilidade de uma UI fora do produto. Não usar para o produto TradeRisk (use traderisk-frontend-design)."
---

# Frontend Design Patterns

## Overview

Você é um especialista em design de interfaces web modernas, com foco em produtos B2B, dashboards financeiros e aplicações de dados complexos. Esta skill reúne princípios gerais de design aplicáveis a qualquer interface web/app.

## Quando usar

- Melhorar a aparência ou a UX de uma interface genérica
- Definir responsividade, breakpoints e comportamento mobile
- Revisar performance percebida e acessibilidade de uma UI
- **Quando NÃO usar:** trabalho no produto TradeRisk com seu design system → use `traderisk-frontend-design`

## Core Pattern

### Responsividade
- Mobile-first com breakpoints: sm(640) md(768) lg(1024) xl(1280)
- Componentes collapsíveis em mobile
- Touch targets mínimo 44x44px

### Performance
- Lazy loading para imagens e componentes pesados
- Skeleton loading em vez de spinners
- Optimistic UI para ações do usuário

### Acessibilidade
- ARIA labels em todos os elementos interativos
- Contraste mínimo 4.5:1 (WCAG AA)
- Suporte a navegação por teclado

## Quick Reference

| Área | Diretriz |
|------|----------|
| Breakpoints | sm 640 / md 768 / lg 1024 / xl 1280 |
| Mobile | Mobile-first, componentes collapsíveis |
| Touch target | Mínimo 44x44px |
| Loading | Skeleton em vez de spinner |
| Feedback | Optimistic UI |
| Contraste | Mínimo 4.5:1 (WCAG AA) |
| Teclado | Navegação completa suportada |

## Common Mistakes

- Projetar desktop-first e adaptar depois → começar mobile-first.
- Usar spinners para carregamento longo → preferir skeleton loading.
- Touch targets menores que 44x44px → dificultam uso em mobile.
- Esquecer ARIA labels e contraste → quebra acessibilidade WCAG AA.
