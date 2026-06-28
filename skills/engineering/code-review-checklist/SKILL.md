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

## Método passo a passo

1. **Entender contexto/objetivo do PR.** Leia a descrição, o ticket relacionado e o escopo. O que o PR pretende resolver? Está dentro do escopo (sem mudanças não relacionadas)? Se o objetivo não estiver claro, peça contexto antes de revisar linha a linha.
2. **Rodar/checar testes.** Confirme que CI está verde, que há testes cobrindo o comportamento novo e que os testes realmente exercitam o caso (não só "não quebram"). Rode localmente quando o risco justificar.
3. **Checklist de segurança.** Secrets fora do código, inputs validados/sanitizados, autenticação **e** autorização, queries parametrizadas, dados sensíveis não logados. Segurança vem antes de estilo.
4. **Qualidade.** Legibilidade, nomes, funções coesas e curtas, ausência de duplicação, tratamento explícito de erros, ausência de código morto/debug.
5. **Performance.** N+1 queries, índices, payloads, re-renders, alocações em loops quentes, paginação. Foque no que tem impacto real no caminho crítico.
6. **Checklist específico por stack.** Aplique o checklist do(s) stack(s) tocado(s): [`checklists/react.md`](checklists/react.md), [`checklists/typescript.md`](checklists/typescript.md), [`checklists/supabase.md`](checklists/supabase.md).
7. **Feedback acionável priorizado.** Separe bloqueante de sugestão/nit, seja específico e dê exemplo. Resuma os pontos mais importantes no topo do review.

## Como dar feedback

Classifique cada comentário para que o autor saiba o peso:

- **Bloqueante:** precisa ser resolvido antes do merge (bug, falha de segurança, quebra de contrato). Deixe explícito por quê.
- **Sugestão:** melhoria recomendada mas não obrigatória; explique o trade-off.
- **Nit:** detalhe menor de estilo/preferência; prefixe com `nit:` para sinalizar baixa prioridade.

Princípios:

- **Seja específico.** Aponte a linha e o problema concreto, não "isso está ruim".
- **Aponte um exemplo.** Mostre o trecho corrigido ou referencie um padrão existente no repo.
- **Comente o código, não a pessoa.** "Esta função faz duas coisas" e não "você complicou".
- **Reconheça o que está bom.** Feedback positivo também orienta o time.
- **Faça perguntas quando não tiver certeza.** "Esse caminho cobre o caso de `null`?" abre conversa em vez de assumir erro.

## Common Mistakes

- Aprovar PR sem rodar/checar os testes → exigir testes passando.
- Deixar secrets ou console.log no código → bloquear no review.
- Ignorar N+1 queries e índices ausentes → impacto direto de performance.
- Feedback vago ("melhore isso") → dar feedback acionável e construtivo.
- Não distinguir bloqueante de nit → autor não sabe o que precisa mudar antes do merge.
- Revisar estilo antes de correção/segurança → priorize o que tem risco real primeiro.
- Aprovar mudanças fora do escopo do PR → pedir para separar em outro PR.
- Revisar PRs gigantes de uma vez → pedir para quebrar; reviews grandes escondem bugs.

## Referências / Embasamento

- [`checklists/react.md`](checklists/react.md) — componentes, hooks, estado, acessibilidade, performance, formulários e testes em React.
- [`checklists/typescript.md`](checklists/typescript.md) — tipagem, segurança de tipos, configuração e tratamento de erros em TypeScript.
- [`checklists/supabase.md`](checklists/supabase.md) — RLS, Edge Functions Deno, performance, migrations, Realtime e Storage.
