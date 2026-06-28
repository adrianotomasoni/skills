---
name: mcp-builder
description: "Constrói, configura e integra servidores e ferramentas MCP (Model Context Protocol) para expandir as capacidades de modelos. Use SEMPRE que houver: criar um servidor MCP, expor ferramentas/dados via MCP, definir tools com inputSchema e handlers, integrar fontes externas (Supabase, APIs) a modelos via MCP. Não usar para desenho de API REST tradicional (use api-design-restful)."
---

# MCP Builder

## Overview

Você é um especialista em Model Context Protocol (MCP). Sua função é ajudar a construir, configurar e integrar MCP servers para expandir as capacidades dos modelos de linguagem nos projetos TradeRisk.

Model Context Protocol é um padrão aberto que permite que modelos de IA se conectem a fontes de dados externas (bancos de dados, APIs, arquivos) de forma segura e padronizada.

## Quando usar

- Criar um servidor MCP
- Expor ferramentas ou dados via MCP
- Definir tools com `inputSchema` e handlers
- Integrar fontes externas (Supabase, APIs) a modelos via MCP
- **Quando NÃO usar:** desenho de API REST tradicional → use `api-design-restful`

## Core Pattern

### Estrutura de um MCP Server

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({
  name: "traderisk-skills",
  version: "1.0.0",
});

server.registerTool(
  "get_credit_analysis",
  {
    description: "Retorna a análise de crédito de uma empresa a partir do CNPJ.",
    inputSchema: {
      cnpj: z.string().describe("CNPJ da empresa, com ou sem máscara"),
    },
  },
  async ({ cnpj }) => {
    // TODO: query real no Supabase (dado proprietário TradeRisk)
    const data = { cnpj, score: 0 };
    return {
      content: [{ type: "text", text: JSON.stringify(data, null, 2) }],
    };
  }
);

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
```

> O pacote oficial é `@modelcontextprotocol/sdk` (instale com
> `npm install @modelcontextprotocol/sdk zod`). `inputSchema` é definido com Zod;
> as tools são registradas via `server.registerTool(name, { description, inputSchema }, handler)`.

## Método passo a passo

1. **Definir capacidades/tools**: liste as tools que o server vai expor, com
   nome claro (verbo + objeto, ex.: `get_credit_analysis`) e o que cada uma faz.
2. **Inicializar projeto/SDK**: `npm install @modelcontextprotocol/sdk zod`.
   Configure TypeScript (`tsc`) e o entrypoint do server.
3. **Definir `inputSchema` com Zod**: descreva cada parâmetro com `z.*` e
   `.describe(...)`. Use validações (`regex`, `min`, `enum`) — o schema é o
   contrato que o modelo usa para chamar a tool.
4. **Implementar handlers com validação e erros**: valide entrada, trate
   exceções e retorne `{ content: [...] }`; em falha use
   `{ isError: true, content: [...] }`. Nunca deixe a exceção vazar.
5. **Transport (stdio)**: conecte via `StdioServerTransport` em `main()` com
   `await server.connect(transport)`.
6. **Registrar no client/config**: adicione o server em `mcpServers` do client
   (Claude Desktop, etc.) com `command`, `args` e `env`. Segredos vão por
   variável de ambiente, nunca hardcoded.
7. **Testar**: rode o server e exercite cada tool (inputs válidos e inválidos)
   para confirmar validação, retorno e tratamento de erro.

## Quando NÃO usar

- Para desenho de API REST tradicional → use `api-design-restful`.
- Quando o consumidor não é um modelo/agente MCP (ex.: front-end web chamando
  endpoint HTTP) — MCP agrega complexidade sem ganho.
- Para um script pontual de ETL que roda uma vez — não precisa de servidor MCP.

## Quick Reference

### Use Cases TradeRisk

1. **PNCP MCP**: consultar licitações em tempo real
2. **Supabase MCP**: acessar dados do portal
3. **Skills MCP**: carregar skills dinamicamente
4. **Brevo MCP**: enviar alertas por email/WhatsApp

## Common Mistakes

- Usar o pacote errado: o import correto é `@modelcontextprotocol/sdk`, não `@anthropic/mcp-sdk`.
- Tool sem `inputSchema` bem definido → o modelo não sabe como chamá-la.
- `description` vaga na tool → reduz a taxa de acerto na seleção da ferramenta.
- Handler sem tratamento de erro/validação → falhas silenciosas em produção.
- Retornar erro como exceção crua em vez de `{ isError: true, content: [...] }`.
- Esquecer de conectar o `transport`/`main()` → o server não responde.
- Hardcodar segredos no código ou no config → use variáveis de ambiente.
- Expor dados sensíveis sem controle de acesso → MCP deve conectar de forma segura.

## Referências / Embasamento

- [`examples/minimal-server.ts`](examples/minimal-server.ts) — MCP server mínimo e válido (McpServer + StdioServerTransport + Zod) com a tool `get_credit_analysis`.
- [`examples/mcp-config.json`](examples/mcp-config.json) — exemplo de config de cliente MCP (`mcpServers`) registrando o server.
