# Checklist Supabase – Code Review

## Queries
- [ ] RLS policies habilitadas na tabela
- [ ] Filtros adequados (evitar full table scan)
- [ ] Índices criados para colunas filtradas frequentemente
- [ ] Paginação implementada (`.range()` ou `.limit()`)

## Segurança
- [ ] Service role key nunca exposta no frontend
- [ ] Políticas de RLS testadas para cada role
- [ ] Realtime subscriptions com filtros adequados

## Migrations
- [ ] Migration reversível (rollback possível)
- [ ] Sem breaking changes em tabelas com dados
- [ ] Índices criados `CONCURRENTLY` em produção
