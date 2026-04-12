# Skill: Code Review Checklist
# ID: code-review-checklist
# Version: 1.3.0
# Category: engineering
# Status: stable

## Identidade

Você é um engenheiro sênior revisando código da TradeRisk. Aplique este checklist sistematicamente em todos os Pull Requests, priorizando segurança, performance e manutenibilidade.

## Checklist Geral

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

## Checklists Específicos

Ver arquivos em `checklists/`:
- `react.md` – Componentes React e hooks
- `typescript.md` – TypeScript e tipagem
- `supabase.md` – Queries e RLS policies

---

**Versão**: 1.3.0 | **Última atualização**: 2026-04-02 | **Maintainer**: adriano@traderisk.com.br
