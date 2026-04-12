# Skill: API Design RESTful
# ID: api-design-restful
# Version: 1.2.0
# Category: engineering
# Status: stable

## Padrões de URL

```
GET    /api/v1/resources          # Listar
POST   /api/v1/resources          # Criar
GET    /api/v1/resources/:id      # Detalhar
PUT    /api/v1/resources/:id      # Atualizar completo
PATCH  /api/v1/resources/:id      # Atualizar parcial
DELETE /api/v1/resources/:id      # Deletar
```

## Convenções de Nomenclatura

- Recursos em **plural** e **kebab-case**: `/credit-analyses`
- IDs em UUID v4
- Parâmetros de query em **camelCase**: `?pageSize=20&sortBy=createdAt`

## Resposta Padrão

```json
{
  "data": {},
  "meta": {
    "requestId": "uuid",
    "timestamp": "ISO8601"
  }
}
```

## Erros Padrão

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Credit analysis not found",
    "details": []
  }
}
```

## HTTP Status Codes

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

---

**Versão**: 1.2.0 | **Última atualização**: 2026-03-25
