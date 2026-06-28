# Agente: Monitor Judicial

Agente especialista em monitoramento judicial proativo para operações de seguro
garantia e crédito da TradeRisk. Recebe movimentações processuais (sistema CNJ) e
devolve a classificação do evento, o score de risco e a recomendação de ação.

## Arquivos

- `AGENT.md` — definição do agente. O frontmatter segue o superset de subagentes
  do Claude Code (`name`, `description`, `tools`, `model`).
- `agent.json` — metadados de portabilidade por plataforma e skills vinculadas.

## Skill vinculada

- `judicial-monitoring` (`skills/core/judicial-monitoring/`) — fornece a
  taxonomia de eventos (Níveis A–D), a fórmula de score e o formato de saída.

## Saída

JSON com `evento`, `nivel` (A–D), `score` (0–100), `valor_impacto`,
`recomendacao` e `prazo_acao`. Não substitui parecer jurídico — sinaliza e
prioriza.
