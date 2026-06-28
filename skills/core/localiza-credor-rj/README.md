# localiza-credor-rj

> Categoria: `core` · Formato canônico multiplataforma (ver `skills/meta/multiplatform-authoring`).

## O que é
Inteligência de prospecção para Seguro de Crédito a partir de Recuperação Judicial e falência. Use SEMPRE que houver: mapear credores de empresas em RJ/falência, extrair lista de credores de edital ou quadro-geral, transformar processo de RJ em leads B2B, identificar empresas expostas a inadimplência de um devedor em crise, qualificar credor PJ como prospect de Seguro de Crédito, ou cruzar Radar RJ com base de prospecção. A RJ é um mapa de exposição comercial: o credor PJ exposto é o alvo, NÃO o devedor. Acionar mesmo quando o usuário só menciona um edital de RJ, quadro de credores, ou nome de empresa em recuperação.

## Gatilhos (quando acionar)
- "Mapeia os credores da empresa X que entrou em RJ"
- "Extrai a lista de credores deste edital / quadro-geral"
- "Transforma este processo de RJ em leads de Seguro de Crédito"
- Menção solta a um edital de RJ, quadro de credores ou empresa em recuperação.

## Quando NÃO usar
- Avaliar o risco do devedor (a RJ é fonte, não alvo) ou do prospect — risco é assunto da cotação.
- Análise de crédito de um cliente → `credit-risk-analysis`.
- Monitoramento de processos judiciais → `judicial-monitoring`.

## Como usar
- **Claude Code / Codex / Gemini / Copilot:** instale a pasta em `~/.claude/skills/localiza-credor-rj/` (ou `~/.agents/skills/localiza-credor-rj/`).
- **Claude.ai / OpenAI / Manus / Cursor:** veja `docs/USAGE.md` e `skills/meta/multiplatform-authoring/references/`.
- Conteúdo completo em [`SKILL.md`](SKILL.md); metadados em [`skill.json`](skill.json).

## Exemplo
Entrada: quadro-geral de credores (QGC) de uma RJ. Saída: lista de credores PJ qualificados com CNAE, porte, score de prospecção, prioridade e abordagem consultiva — sem expor ao lead a origem na RJ. Ver `examples/quadro-credores-exemplo.json` (fictício).

## Material de apoio
- `SKILL.md` — passos 0–5, score de prospecção, regras invioláveis e saída estruturada.
- `examples/quadro-credores-exemplo.json` — quadro de credores qualificado (fictício, marcado).

> Distinção devedor/credor, modelo de score e regras de LGPD/abordagem são definições internas — não alterar. Integrações (direct.data, COMEX STAT, schema `radar_rj`) e parâmetros de campanha: TODO: preencher com <configuração proprietária> da TradeRisk.
