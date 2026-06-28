/**
 * MCP server mínimo e válido usando o SDK oficial.
 *
 * Dependências:
 *   npm install @modelcontextprotocol/sdk zod
 *
 * Execução (stdio): node dist/minimal-server.js
 */
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({
  name: "traderisk-skills",
  version: "1.0.0",
});

// Tool de exemplo: análise de crédito por CNPJ.
server.registerTool(
  "get_credit_analysis",
  {
    description: "Retorna a análise de crédito de uma empresa a partir do CNPJ.",
    inputSchema: {
      cnpj: z
        .string()
        .regex(/^\d{2}\.?\d{3}\.?\d{3}\/?\d{4}-?\d{2}$/, "CNPJ inválido")
        .describe("CNPJ da empresa, com ou sem máscara"),
    },
  },
  async ({ cnpj }) => {
    // Normaliza o CNPJ (apenas dígitos) antes de consultar.
    const cnpjDigits = cnpj.replace(/\D/g, "");
    if (cnpjDigits.length !== 14) {
      return {
        isError: true,
        content: [{ type: "text", text: "CNPJ deve conter 14 dígitos." }],
      };
    }

    try {
      // TODO: substituir pelo query real no Supabase (dado proprietário TradeRisk).
      // const { data, error } = await supabase
      //   .from("credit_analysis")
      //   .select("*")
      //   .eq("cnpj", cnpjDigits)
      //   .single();
      const data = {
        cnpj: cnpjDigits,
        score: 0, // TODO: score real
        risco: "TODO: classificação de risco proprietária",
      };

      return {
        content: [{ type: "text", text: JSON.stringify(data, null, 2) }],
      };
    } catch (err) {
      return {
        isError: true,
        content: [
          {
            type: "text",
            text: `Falha ao consultar análise de crédito: ${
              err instanceof Error ? err.message : String(err)
            }`,
          },
        ],
      };
    }
  }
);

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  // O servidor agora escuta requisições MCP via stdio.
}

main().catch((err) => {
  console.error("Erro fatal ao iniciar o MCP server:", err);
  process.exit(1);
});
