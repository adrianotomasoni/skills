# LicitaRadar

> Categoria: `core` · Monitoramento e classificação de licitações públicas via PNCP.

## O que é

Skill que monitora licitações públicas brasileiras pela API do PNCP, classifica oportunidades por relevância para o portfólio do cliente e identifica exigências de seguro garantia (proposta, execução, manutenção). Transforma editais em alertas comerciais acionáveis.

## Gatilhos (quando acionar)

- "Encontra/monitora licitações que exijam seguro garantia"
- "Classifica este edital" / "esse edital é relevante pro cliente X?"
- "Quais oportunidades de licitação saíram essa semana"
- "Quanto de garantia este edital exige?"

## Quando NÃO usar

- Análise de risco de crédito de um cliente → `credit-risk-analysis`.
- Monitoramento de processos judiciais → `judicial-monitoring`.
- Prospecção a partir de recuperação judicial → `localiza-credor-rj`.

## Como usar por plataforma

- **Claude Code / Codex / Gemini / Copilot:** instale em `~/.claude/skills/licitaradar/`; os clients em `api-integration/` rodam em ambiente Node/TS.
- **Claude.ai:** upload de `SKILL.md` e cole o texto do edital para classificação.
- **Cursor:** `@skills/core/licitaradar/SKILL.md` + o edital ou os filtros de busca.

## Exemplo

Prompt: *"Classifica este pregão: reforma de escola, R$ 1,2M, garantia de execução de 5%."*
Saída esperada: classe Alta, score, `exigeSeguroGarantia: true`, percentual 5%, ação de alerta imediato. Ver `examples/edital-classificado.json`.

## Material de apoio

- `SKILL.md` — método, critérios de relevância e cadência de alertas.
- `api-integration/README.md` — explicação dos clients TypeScript.
- `api-integration/pncp-client.ts` · `api-integration/claude-classifier.ts`.
- `examples/edital-classificado.json` — exemplo fictício classificado.

> Modalidades e regras de garantia seguem a Lei 14.133/2021. Parâmetros de relevância e mapeamento de setor: TODO: preencher com <regras proprietárias> da TradeRisk.

## Tags

`licitacao` `pncp` `monitoring` `government` `seguro-garantia`
