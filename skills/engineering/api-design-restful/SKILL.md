---
name: api-design-restful
description: "Projeta APIs RESTful com boas práticas: nomenclatura de recursos, versionamento, erros padronizados, paginação e autenticação. Use SEMPRE que houver: desenhar uma API ou endpoints novos, 'como estruturar essa API', 'qual o melhor endpoint para', padronizar uma API que cresceu sem design, ou documentar contrato de API para time/cliente. Aplica-se a Edge Functions Supabase e backends do ecossistema TradeRisk. Não usar para revisar implementação de código já escrito (use code-review-checklist)."
---

# API Design RESTful

## Overview

Esta skill orienta o desenho de APIs RESTful consistentes para o ecossistema TradeRisk, incluindo Edge Functions Supabase e backends. Cobre nomenclatura de recursos, versionamento, formatos de resposta e erro, e códigos HTTP.

## Quando usar

- Desenhar uma API ou endpoints novos
- Decidir "como estruturar essa API" ou "qual o melhor endpoint para"
- Padronizar uma API que cresceu sem design
- Documentar contrato de API para time/cliente
- **Quando NÃO usar:** revisar implementação de código já escrito → use `code-review-checklist`

## Core Pattern

### Padrões de URL

```
GET    /api/v1/resources          # Listar
POST   /api/v1/resources          # Criar
GET    /api/v1/resources/:id      # Detalhar
PUT    /api/v1/resources/:id      # Atualizar completo
PATCH  /api/v1/resources/:id      # Atualizar parcial
DELETE /api/v1/resources/:id      # Deletar
```

### Convenções de Nomenclatura

- Recursos em **plural** e **kebab-case**: `/credit-analyses`
- IDs em UUID v4
- Parâmetros de query em **camelCase**: `?pageSize=20&sortBy=createdAt`

### Resposta Padrão

```json
{
  "data": {},
  "meta": {
    "requestId": "uuid",
    "timestamp": "ISO8601"
  }
}
```

### Erros Padrão

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Credit analysis not found",
    "details": []
  }
}
```

## Quick Reference

### HTTP Status Codes

| Situação | Status |
|----------|--------|
| Sucesso GET/PATCH/PUT | 200 |
| Criação | 201 |
| Sem conteúdo | 204 |
| Dados inválidos | 400 |
| Não autenticado | 401 |
| Não autorizado | 403 |
| Não encontrado | 404 |
| Erro interno | 500 |

## Método passo a passo

1. **Modelar recursos.** Identifique os substantivos do domínio (ex.: `credit-analyses`, `customers`, `invoices`). Cada recurso é uma entidade com identidade própria. Evite modelar ações como recursos; ações viram verbos HTTP ou, em último caso, sub-recursos.
2. **Definir verbos/URLs.** Mapeie cada operação para um método HTTP e uma URL plural em kebab-case. CRUD básico: `GET /v1/resources`, `POST /v1/resources`, `GET /v1/resources/{id}`, `PATCH /v1/resources/{id}`, `DELETE /v1/resources/{id}`. Use `PUT` apenas para substituição completa idempotente.
3. **Versionamento.** Prefixe a rota com a versão maior (`/v1`). Só incremente para `v2` quando houver mudança **incompatível** (breaking change). Mudanças aditivas (novos campos opcionais, novos endpoints) ficam na mesma versão.
4. **Formato de resposta/erro.** Padronize o envelope de sucesso (`data` + `meta`) e o envelope de erro (`error` com `code`, `message`, `details[]`, `requestId`). Documente os `code`s de erro como contrato estável.
5. **Paginação/filtros/ordenação.** Escolha cursor (datasets grandes, dados que mudam) ou offset (datasets pequenos/estáveis) e seja consistente em toda a API. Defina convenções de filtro e ordenação em query params camelCase.
6. **Autenticação.** Defina o esquema (ex.: Bearer JWT) e os escopos/roles. Garanta que toda rota protegida valide o token e a autorização do recurso (não só autenticação).
7. **Documentar contrato OpenAPI.** Escreva o contrato em OpenAPI 3.1 antes ou junto da implementação. O contrato é a fonte de verdade para o time e clientes.
8. **Revisar.** Cheque consistência de nomes, status codes, paginação, exemplos e segurança. Valide o contrato e gere documentação a partir dele.

## Quando NÃO usar

- Revisar implementação de código já escrito → use `code-review-checklist`.
- APIs internas RPC de altíssima performance entre serviços onde gRPC/mensageria faz mais sentido que REST.
- Operações que não mapeiam bem para CRUD de recursos (ex.: processamento em lote complexo) podem precisar de endpoints de ação dedicados — documente-os explicitamente.

## Exemplos concretos

### Paginação por offset

Boa para datasets pequenos e estáveis. Cliente controla `page` e `pageSize`.

```
GET /v1/credit-analyses?page=2&pageSize=20
```

```json
{
  "data": [ { "id": "..." } ],
  "meta": {
    "pagination": {
      "type": "offset",
      "page": 2,
      "pageSize": 20,
      "totalItems": 137,
      "totalPages": 7
    },
    "requestId": "b3f1...",
    "timestamp": "2026-06-28T12:00:00Z"
  }
}
```

### Paginação por cursor

Boa para datasets grandes ou que mudam durante a navegação. O servidor devolve um cursor opaco.

```
GET /v1/credit-analyses?pageSize=20
GET /v1/credit-analyses?pageSize=20&cursor=eyJpZCI6IjEyMyJ9
```

```json
{
  "data": [ { "id": "..." } ],
  "meta": {
    "pagination": {
      "type": "cursor",
      "pageSize": 20,
      "nextCursor": "eyJpZCI6IjE0MyJ9",
      "hasMore": true
    },
    "requestId": "c9a2...",
    "timestamp": "2026-06-28T12:00:00Z"
  }
}
```

### Filtros e ordenação em query params

```
GET /v1/credit-analyses?status=approved&minScore=700&sortBy=createdAt&sortOrder=desc
```

- Filtros simples: um param por campo (`status=approved`).
- Ordenação: `sortBy` (campo) + `sortOrder` (`asc`/`desc`).
- Ranges: prefixos consistentes (`minScore`, `maxScore`) ou operadores documentados.

### PATCH parcial

`PATCH` atualiza apenas os campos enviados; o que não vem no corpo permanece inalterado.

```
PATCH /v1/credit-analyses/9c1f-...
Content-Type: application/json
```

```json
{
  "status": "approved",
  "reviewerNotes": "Renda comprovada"
}
```

Resposta `200`:

```json
{
  "data": {
    "id": "9c1f-...",
    "status": "approved",
    "reviewerNotes": "Renda comprovada",
    "score": 742,
    "updatedAt": "2026-06-28T12:05:00Z"
  },
  "meta": { "requestId": "d0e3...", "timestamp": "2026-06-28T12:05:00Z" }
}
```

## Common Mistakes

- Recursos no singular ou com verbos na URL → usar plural e substantivos (`/credit-analyses`).
- Misturar convenções (snake_case e camelCase em query params) → manter camelCase em query.
- Respostas sem envelope `data`/`meta` consistente → padronizar formato.
- Retornar 200 para erros → usar o status HTTP correto (400/401/403/404/500).
- Versionar quebrando compatibilidade dentro da mesma versão → mudanças incompatíveis exigem nova versão maior (`/v2`); na mesma versão só mudanças aditivas.
- Paginação inconsistente (offset em um endpoint, cursor em outro, nomes de params variando) → escolher uma convenção e aplicar em toda a API.
- Não documentar o contrato (OpenAPI) ou deixá-lo desatualizado → manter o contrato como fonte de verdade, versionado junto do código.

## Referências / Embasamento

- [`templates/openapi-minimal.yaml`](templates/openapi-minimal.yaml) — contrato OpenAPI 3.1 mínimo de exemplo (recurso CRUD paginado, schemas, erro e segurança Bearer JWT).
- [`templates/error-response.json`](templates/error-response.json) — exemplos do envelope de erro padrão (validation_error, not_found, unauthorized).
- [`templates/endpoint-conventions.md`](templates/endpoint-conventions.md) — convenções de nomenclatura, versionamento, status codes, paginação, nesting e idempotência.
