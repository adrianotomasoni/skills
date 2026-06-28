# Agente: Analista de Risco de Crédito

Agente especialista em risco de crédito comercial B2B da TradeRisk. Recebe dados
de uma empresa (CNPJ, financeiros, histórico) e devolve um parecer estruturado
com rating, score e recomendação de limite/aceite.

## Arquivos

- `AGENT.md` — definição do agente. O frontmatter segue o superset de subagentes
  do Claude Code (`name`, `description`, `tools`, `model`).
- `agent.json` — metadados de portabilidade por plataforma e skills vinculadas.

## Skill vinculada

- `credit-risk-analysis` (`skills/core/credit-risk-analysis/`) — fornece a
  metodologia, a escala de rating/score e o formato do parecer.

## Saída

Parecer JSON com `rating` (A–F), `score` (0–1000), `recomendacao`,
`limite_recomendado`, `prazo_maximo` e pontos de atenção.
