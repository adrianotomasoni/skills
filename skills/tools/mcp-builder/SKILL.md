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
import { MCPServer } from '@anthropic/mcp-sdk';

const server = new MCPServer({
  name: 'traderisk-skills',
  version: '1.0.0',
  tools: [
    {
      name: 'get_credit_analysis',
      description: 'Retorna análise de crédito por CNPJ',
      inputSchema: {
        type: 'object',
        properties: {
          cnpj: { type: 'string' }
        }
      },
      handler: async ({ cnpj }) => {
        // implementação
      }
    }
  ]
});
```

## Quick Reference

### Use Cases TradeRisk

1. **PNCP MCP**: consultar licitações em tempo real
2. **Supabase MCP**: acessar dados do portal
3. **Skills MCP**: carregar skills dinamicamente
4. **Brevo MCP**: enviar alertas por email/WhatsApp

## Common Mistakes

- Tool sem `inputSchema` bem definido → o modelo não sabe como chamá-la.
- `description` vaga na tool → reduz a taxa de acerto na seleção da ferramenta.
- Handler sem tratamento de erro/validação → falhas silenciosas em produção.
- Expor dados sensíveis sem controle de acesso → MCP deve conectar de forma segura.
