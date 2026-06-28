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

## RLS detalhado
- [ ] RLS habilitado (`ENABLE ROW LEVEL SECURITY`) em toda tabela exposta
- [ ] Policy específica por operação: `SELECT`, `INSERT`, `UPDATE`, `DELETE` (não uma genérica `FOR ALL`)
- [ ] `INSERT` usa `WITH CHECK`; `UPDATE` usa `USING` e `WITH CHECK`; `SELECT`/`DELETE` usam `USING`
- [ ] Ownership via `auth.uid()` comparado à coluna de dono (ex.: `user_id = auth.uid()`)
- [ ] Sem policy permissiva demais (`USING (true)`) em tabela com dados sensíveis
- [ ] Roles distintos (anon vs authenticated) cobertos e testados
- [ ] Funções `SECURITY DEFINER` usadas com cuidado e `search_path` fixado

## Edge Functions (Deno)
- [ ] Input validado (Zod ou validação manual) antes de usar o body
- [ ] CORS configurado (headers e tratamento do preflight `OPTIONS`)
- [ ] Secrets via `Deno.env.get`, nunca hardcoded; service role só no servidor
- [ ] Timeouts e tratamento de erro em chamadas externas (sem await pendurado)
- [ ] Respostas com status HTTP e corpo de erro padronizados
- [ ] Sem vazar detalhes internos/stack trace na resposta
- [ ] Cliente Supabase criado com o token do usuário quando a operação deve respeitar RLS

## Performance
- [ ] `select` de colunas específicas em vez de `select('*')`
- [ ] Joins via foreign tables do PostgREST (`select('*, related(*)')`) em vez de múltiplas idas
- [ ] Índices para colunas usadas em filtros, ordenação e joins
- [ ] `count` exato (`{ count: 'exact' }`) só quando necessário (é caro)
- [ ] Paginação com `.range()`/`.limit()`; sem buscar a tabela inteira
- [ ] Sem N+1 (loop disparando uma query por item)

## Realtime
- [ ] Subscriptions com filtro de servidor (não filtrar no cliente após receber tudo)
- [ ] RLS também protege os eventos de Realtime (publicação respeita policies)
- [ ] Cleanup/unsubscribe ao desmontar para evitar leaks de conexão
- [ ] Apenas as tabelas necessárias na publicação Realtime

## Storage
- [ ] Buckets públicos vs privados escolhidos conscientemente
- [ ] Policies de bucket por operação (upload/download/delete) com `auth.uid()`
- [ ] URLs assinadas (signed URLs) com expiração para conteúdo privado
- [ ] Validação de tipo/tamanho de arquivo no upload
- [ ] Caminho do objeto namespaced por usuário/tenant quando aplicável

## Migrations (adicional)
- [ ] Migration idempotente quando possível (`IF NOT EXISTS` / `IF EXISTS`)
- [ ] Ordem das migrations consistente (timestamps crescentes, sem conflito)
- [ ] Mudanças destrutivas em tabelas com dados feitas em etapas (expand/contract)
