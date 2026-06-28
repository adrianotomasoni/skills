# Convenções de Endpoints — API RESTful TradeRisk

Convenções acionáveis para manter as APIs consistentes. Use em conjunto com
[`openapi-minimal.yaml`](openapi-minimal.yaml) e [`error-response.json`](error-response.json).

## Nomenclatura de recursos

- Recursos sempre no **plural** e em **kebab-case**: `/credit-analyses`, `/payment-methods`.
- Use **substantivos**, nunca verbos: `POST /credit-analyses` (não `/createCreditAnalysis`).
- IDs em **UUID v4** na URL: `/credit-analyses/{id}`.
- Ações que não são CRUD viram sub-recursos ou endpoints de ação explícitos:
  `POST /credit-analyses/{id}/approve` (documentar bem; usar com parcimônia).

## Query params

- Sempre em **camelCase**: `?pageSize=20&sortBy=createdAt&sortOrder=desc`.
- Filtros: um param por campo (`status=approved`). Ranges com prefixo (`minScore`, `maxScore`).
- Ordenação: `sortBy` (campo) + `sortOrder` (`asc` | `desc`).
- Booleanos explícitos: `?includeArchived=true`.

## Versionamento

- Versão maior no caminho: `/v1/...`.
- Incremente para `/v2` **somente** em mudança incompatível (remover/renomear campo,
  mudar tipo, mudar semântica).
- Mudanças **aditivas** (novos campos opcionais, novos endpoints) ficam na mesma versão.
- Nunca quebre um contrato publicado sem nova versão e período de depreciação.

## Status codes

| Situação | Status |
|----------|--------|
| Sucesso GET/PATCH/PUT | 200 |
| Criação bem-sucedida | 201 |
| Sucesso sem corpo (ex.: DELETE) | 204 |
| Dados/validação inválidos | 400 |
| Não autenticado | 401 |
| Autenticado mas sem permissão | 403 |
| Recurso não encontrado | 404 |
| Conflito (ex.: duplicidade) | 409 |
| Payload semântico inválido | 422 |
| Rate limit excedido | 429 |
| Erro interno | 500 |

## Paginação: cursor vs offset

| Critério | Offset | Cursor |
|----------|--------|--------|
| Dataset | Pequeno/estável | Grande ou mutável |
| Params | `page`, `pageSize` | `cursor`, `pageSize` |
| Pular para página N | Sim | Não |
| Consistência sob escrita concorrente | Fraca | Forte |

- Escolha **uma** estratégia e aplique em toda a API.
- Retorne metadados de paginação em `meta.pagination` (ver `openapi-minimal.yaml`).
- Para cursor, devolva `nextCursor` e `hasMore`; o cursor é **opaco** para o cliente.

## Nesting de recursos

- Aninhe quando há relação de posse clara: `/customers/{id}/credit-analyses`.
- Limite a 1 nível de aninhamento. Para acessar o recurso diretamente, prefira
  a rota de topo: `/credit-analyses/{id}`.
- Evite aninhamentos profundos (`/a/{id}/b/{id}/c/{id}`) — usam IDs globais e ficam frágeis.

## Idempotência

- `GET`, `PUT`, `DELETE` devem ser idempotentes (repetir não muda o resultado).
- `POST` não é idempotente por natureza. Para criação segura sob retry, aceite um
  header `Idempotency-Key` e deduplique no servidor.
- `PATCH` deve ser determinístico para o mesmo corpo aplicado ao mesmo estado.

## Respostas

- Envelope de sucesso: `{ "data": ..., "meta": { "requestId", "timestamp", "pagination?" } }`.
- Envelope de erro: `{ "error": { "code", "message", "details[]", "requestId" } }`.
- `requestId` deve ser propagado em logs para correlação ponta a ponta.
- TODO: política de rate limiting e headers (`X-RateLimit-*`) padrão TradeRisk.
