# MCP Builder

## O que é

Skill para construir, configurar e integrar servidores e ferramentas MCP (Model
Context Protocol) usando o SDK oficial `@modelcontextprotocol/sdk`, expandindo as
capacidades de modelos com acesso a fontes de dados externas.

## Gatilhos

Use quando precisar:

- Criar um servidor MCP
- Expor ferramentas ou dados via MCP
- Definir tools com `inputSchema` (Zod) e handlers
- Integrar fontes externas (Supabase, APIs) a modelos via MCP

Não use para desenho de API REST tradicional → use a skill `api-design-restful`.

## Como usar (por plataforma)

- **Claude Code / Agent SDK**: registre o server no config de `mcpServers` do
  client com `command`, `args` e `env` (segredos via variável de ambiente).
- **Claude Desktop / outros clients MCP**: mesmo formato `mcpServers`; ver
  [`examples/mcp-config.json`](examples/mcp-config.json).

## Exemplo

Server mínimo com a tool `get_credit_analysis` (consulta por CNPJ), usando
`McpServer` + `StdioServerTransport` + Zod. Ver
[`examples/minimal-server.ts`](examples/minimal-server.ts).

## Exemplos

- [`examples/minimal-server.ts`](examples/minimal-server.ts) — MCP server mínimo e válido em TypeScript.
- [`examples/mcp-config.json`](examples/mcp-config.json) — config de cliente MCP registrando o server.

## Versão

**1.0.0**

## Estrutura

```
mcp-builder/
├── SKILL.md                  # Definição da skill
├── README.md                 # Este arquivo
└── examples/
    ├── minimal-server.ts     # MCP server mínimo (TypeScript)
    └── mcp-config.json       # Config de cliente MCP
```
