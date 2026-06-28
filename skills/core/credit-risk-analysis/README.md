# Análise de Risco de Crédito

> Categoria: `core` · Análise de risco de crédito comercial B2B com rating, score e recomendação de exposição.

## O que é

Skill que avalia o risco de crédito comercial B2B de empresas brasileiras e produz parecer estruturado: rating A–F, score 0–1000 e recomendação de aprovação, condicionamento ou recusa, com limite de exposição e prazo sugeridos. Combina análise cadastral, financeira, comportamental e setorial.

## Gatilhos (quando acionar)

- "Analisa o risco de crédito desta empresa / CNPJ"
- "Qual limite de exposição para o cliente X?"
- "Aprovo ou recuso esse crédito/garantia?"
- "Gera um parecer de crédito"

## Quando NÃO usar

- Produzir conteúdo ou marketing sobre risco → `skill-traderisk-content-writer`.
- Classificar movimentação judicial → `judicial-monitoring`.

## Como usar por plataforma

- **Claude Code / Codex / Gemini / Copilot:** instale em `~/.claude/skills/credit-risk-analysis/`.
- **Claude.ai:** upload de `SKILL.md` em Settings → Knowledge e envie os dados da empresa.
- **Cursor:** `@skills/core/credit-risk-analysis/SKILL.md` + os dados do CNPJ.

## Exemplo

Prompt: *"Analisa: Construtora XYZ Ltda, faturamento R$ 8,5M, dívida R$ 1,2M, sem restrições Serasa, 2 trabalhistas (R$ 150k), construção civil."*
Saída esperada: JSON com rating, score, recomendação, limite e pontos de atenção (ver formato no `SKILL.md`). Casos de referência em `examples/case-studies.json`.

## Material de apoio

- `SKILL.md` — metodologia, escala de rating e formato de saída.
- `templates/credit-assessment.md` — template de parecer.
- `templates/score-calculator.js` — calculadora de score.
- `examples/case-studies.json` — casos reais anonimizados.

> O parecer reflete o momento da análise; reavaliar a cada 6 meses ou após evento relevante. Não substitui due diligence completa em valores altos. Escala de rating e score são definições internas — não alterar. Benchmarks setoriais e dados de fonte: TODO: preencher com <parâmetros proprietários> da TradeRisk.

## Tags

`credit` `risk` `rating` `parecer` `b2b`
