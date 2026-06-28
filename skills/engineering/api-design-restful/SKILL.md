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

## Common Mistakes

- Recursos no singular ou com verbos na URL → usar plural e substantivos (`/credit-analyses`).
- Misturar convenções (snake_case e camelCase em query params) → manter camelCase em query.
- Respostas sem envelope `data`/`meta` consistente → padronizar formato.
- Retornar 200 para erros → usar o status HTTP correto (400/401/403/404/500).
