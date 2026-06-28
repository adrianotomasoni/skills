---
name: code-review-checklist
description: "Revisa código com checklist estruturado (legibilidade, segurança, testabilidade, manutenibilidade), com feedback acionável e construtivo. Use SEMPRE que houver: revisar um PR ou trecho de código, pedir 'faz um code review', 'revisa esse código', 'esse código está bom?', avaliar qualidade antes de merge, ou padronizar o processo de review do time. Aplica-se ao stack TradeRisk (Python, Edge Functions Deno, React/TypeScript). Não usar para escrever código novo do zero nem para design de API (use api-design-restful)."
---

# Code Review Checklist

## Overview

Você é um engenheiro sênior revisando código da TradeRisk. Aplique este checklist sistematicamente em todos os Pull Requests, priorizando segurança, performance e manutenibilidade, com feedback acionável e construtivo. Aplica-se ao stack TradeRisk (Python, Edge Functions Deno, React/TypeScript).

## Quando usar

- Revisar um PR ou trecho de código
- Pedidos como "faz um code review", "revisa esse código", "esse código está bom?"
- Avaliar qualidade antes de merge
- Padronizar o processo de review do time
- **Quando NÃO usar:** escrever código novo do zero; design de API → use `api-design-restful`

## Core Pattern

### Antes de Abrir o PR
- [ ] Branch criada a partir de `main`
- [ ] PR title segue Conventional Commits
- [ ] Testes unitários passando
- [ ] Sem console.log ou debug code

### Segurança
- [ ] Sem secrets no código (use env vars)
- [ ] Inputs sanitizados antes de queries
- [ ] Autenticação/autorização verificada
- [ ] SQL injection impossível (parameterized queries)

### Qualidade de Código
- [ ] Funções < 50 linhas
- [ ] Nomes descritivos e sem abreviações desnecessárias
- [ ] Sem código duplicado (DRY)
- [ ] Tratamento de erros explícito

### Performance
- [ ] Sem N+1 queries em loops
- [ ] Índices adequados em queries Supabase
- [ ] Imagens otimizadas (next/image)
- [ ] Lazy loading em componentes pesados

## Quick Reference

Checklists específicos em `checklists/`:

- `react.md` – Componentes React e hooks
- `typescript.md` – TypeScript e tipagem
- `supabase.md` – Queries e RLS policies

## Common Mistakes

- Aprovar PR sem rodar/checar os testes → exigir testes passando.
- Deixar secrets ou console.log no código → bloquear no review.
- Ignorar N+1 queries e índices ausentes → impacto direto de performance.
- Feedback vago ("melhore isso") → dar feedback acionável e construtivo.
