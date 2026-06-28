# API Design RESTful

## O que é

Skill para projetar APIs RESTful consistentes no ecossistema TradeRisk (Edge
Functions Supabase e backends). Cobre modelagem de recursos, verbos/URLs,
versionamento, formato de resposta e erro, paginação, filtros, autenticação e
documentação de contrato OpenAPI.

## Gatilhos (quando dispara)

- Desenhar uma API ou endpoints novos.
- Perguntas como "como estruturar essa API" ou "qual o melhor endpoint para".
- Padronizar uma API que cresceu sem design.
- Documentar contrato de API para time ou cliente.

Não dispara para revisar implementação de código já escrito (use
`code-review-checklist`).

## Como usar por plataforma

- **Claude Code / Cursor:** abra o repositório da API e peça o desenho dos
  endpoints; a skill aplica as convenções e gera o contrato.
- **Outros assistentes:** referencie o `SKILL.md` e os templates como contexto.

## Exemplo de uso

> "Preciso de uma API para análises de crédito com listagem paginada, criação e
> atualização parcial de status."

A skill modela `/v1/credit-analyses`, define os verbos, escolhe paginação,
padroniza o envelope de resposta/erro e produz um contrato OpenAPI.

## Material de apoio

- [`SKILL.md`](SKILL.md) — método passo a passo, padrões e exemplos.
- [`templates/openapi-minimal.yaml`](templates/openapi-minimal.yaml) — contrato OpenAPI 3.1 mínimo.
- [`templates/error-response.json`](templates/error-response.json) — exemplos do envelope de erro.
- [`templates/endpoint-conventions.md`](templates/endpoint-conventions.md) — convenções de endpoints.

## Tags

`api` `rest` `design` `standards` `engineering`
