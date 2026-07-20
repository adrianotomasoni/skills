# Policies Supabase prontas

## 0. Diagnóstico — rode isto primeiro

```sql
-- tabelas sem RLS no schema public = achado CRÍTICO
select c.relname as tabela, c.relrowsecurity as rls_ativa
from pg_class c join pg_namespace n on n.oid = c.relnamespace
where n.nspname = 'public' and c.relkind = 'r'
order by c.relrowsecurity, c.relname;

-- tabelas com RLS ligada mas SEM policy = ninguém acessa (ou você achou que estava seguro)
select c.relname
from pg_class c join pg_namespace n on n.oid = c.relnamespace
where n.nspname='public' and c.relkind='r' and c.relrowsecurity
and not exists (select 1 from pg_policies p where p.tablename = c.relname);

-- leia o predicado de cada policy. "tem policy" não é o mesmo que "está protegido"
select tablename, policyname, cmd, qual, with_check from pg_policies where schemaname='public';
```

## 1. Dono do próprio registro

```sql
alter table public.documentos enable row level security;

create policy "leitura do proprio" on public.documentos
  for select using ((select auth.uid()) = user_id);

create policy "insere como si mesmo" on public.documentos
  for insert with check ((select auth.uid()) = user_id);

create policy "atualiza o proprio" on public.documentos
  for update using ((select auth.uid()) = user_id)
              with check ((select auth.uid()) = user_id);   -- os DOIS. sem o with check, o usuário reatribui a linha

create policy "deleta o proprio" on public.documentos
  for delete using ((select auth.uid()) = user_id);

create index on public.documentos (user_id);  -- policy sem índice = full scan por request
```

`(select auth.uid())` em vez de `auth.uid()` puro faz o Postgres avaliar uma vez por query,
não uma vez por linha. Em tabelas grandes a diferença é de ordem de magnitude.

## 2. Multi-tenant (organização / empresa)

Nunca faça o join da tabela de membros direto na policy — recursão e lentidão.
Use uma função `security definer` estável:

```sql
create or replace function public.orgs_do_usuario()
returns setof uuid language sql stable security definer set search_path = '' as $$
  select org_id from public.membros where user_id = (select auth.uid());
$$;

create policy "acesso por organizacao" on public.faturas
  for select using (org_id in (select public.orgs_do_usuario()));
```

`set search_path = ''` é obrigatório: sem isso, a função `security definer` é sequestrável
por schema shadowing. O advisor do Supabase sinaliza isso como `function_search_path_mutable`.

## 3. Proteção por COLUNA (o buraco que RLS não fecha)

RLS decide se você pode escrever na linha. Ela **não compara valor novo contra valor antigo**.
Uma policy de update legítima permite o usuário mudar `role`, `is_admin`, `saldo`, `preco`.

```sql
create or replace function public.trava_colunas_criticas()
returns trigger language plpgsql as $$
begin
  if new.role is distinct from old.role
     or new.is_admin is distinct from old.is_admin
     or new.org_id is distinct from old.org_id then
    raise exception 'campo protegido: alteração negada';
  end if;
  return new;
end $$;

create trigger trg_trava_colunas before update on public.perfis
  for each row execute function public.trava_colunas_criticas();
```

## 4. Papéis — do jeito certo

```sql
-- ERRADO: o usuário edita raw_user_meta_data à vontade via updateUser()
using ( (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin' )

-- CERTO: tabela própria, escrita apenas server-side
create table public.papeis (
  user_id uuid primary key references auth.users on delete cascade,
  papel text not null check (papel in ('admin','editor','leitor'))
);
alter table public.papeis enable row level security;
create policy "so leitura do proprio papel" on public.papeis
  for select using ((select auth.uid()) = user_id);
-- nenhuma policy de insert/update/delete: só service_role escreve
```

## 5. Storage

```sql
create policy "upload na propria pasta" on storage.objects
  for insert to authenticated
  with check (bucket_id = 'anexos' and (storage.foldername(name))[1] = (select auth.uid())::text);
```

Bucket público + insert liberado = você virou CDN gratuita para malware de terceiros.

## 6. Teste de invasão (rode antes de publicar)

```bash
# com a ANON key — deve retornar [] ou erro, nunca dados
curl -s "$SUPABASE_URL/rest/v1/perfis?select=*" \
  -H "apikey: $ANON_KEY" -H "Authorization: Bearer $ANON_KEY" | head -c 400
```

Se isso devolve linhas de outras pessoas, o projeto está exposto agora. Não é teórico.
