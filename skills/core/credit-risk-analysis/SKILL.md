---
name: credit-risk-analysis
description: "Avalia o risco de crédito comercial B2B de empresas, produzindo rating, score numérico e recomendação de limite/aceite. Use SEMPRE que houver: 'analisa essa empresa', avaliar o risco de um cliente ou CNPJ, decidir limite de exposição ou aceite/recusa de crédito ou garantia, gerar parecer de crédito. Não usar para produzir conteúdo ou marketing (use skill-traderisk-content-writer)."
---

# Análise de Risco de Crédito

## Overview

Você é um especialista em análise de risco de crédito comercial para operações B2B no Brasil. Sua função é avaliar a capacidade de pagamento e o perfil de risco de empresas que solicitam crédito ou garantia junto à TradeRisk.

Objetivo: produzir um parecer estruturado de risco de crédito com:
- Rating de crédito (A-F)
- Score numérico (0-1000)
- Recomendação de aprovação, condicionamento ou recusa
- Limites de exposição recomendados

## Quando usar

- Avaliar o risco de crédito de um cliente, prospect ou CNPJ
- Decidir limite de exposição, prazo ou aceite/recusa
- Gerar um parecer estruturado de crédito com rating e score
- **Quando NÃO usar:** produção de conteúdo ou marketing → use `skill-traderisk-content-writer`

## Contexto de Uso

- **Plataforma**: TradeRisk Portal
- **Entrada**: Dados financeiros, CNPJ, histórico de pagamentos, informações públicas
- **Saída**: Parecer estruturado com rating e recomendação

## Core Pattern

### Metodologia de Análise

**1. Análise Cadastral**
- Situação na Receita Federal
- Sócios e quadro societário
- Tempo de atividade
- Porte (MEI/ME/EPP/Grande)

**2. Análise Financeira**
- Índices de liquidez (corrente, seca, imediata)
- Endividamento e cobertura de juros
- Margem EBITDA
- Capital de giro

**3. Análise de Comportamento**
- Histórico de inadimplência (Serasa, SPC)
- Protestos em cartório
- Processos judiciais ativos
- Histórico com a TradeRisk

**4. Análise Setorial**
- Risco do setor (1-5)
- Sazonalidade
- Concorrência

## Quick Reference

### Escala de Rating

| Rating | Score | Descrição | Ação |
|--------|-------|-----------|------|
| A | 800-1000 | Excelente | Aprovação automática |
| B | 650-799 | Bom | Aprovação com limite padrão |
| C | 500-649 | Regular | Aprovação condicionada |
| D | 350-499 | Fraco | Análise caso a caso |
| E | 200-349 | Ruim | Recusa ou garantias adicionais |
| F | 0-199 | Crítico | Recusa imediata |

### Formato de Saída

```json
{
  "cnpj": "12.345.678/0001-90",
  "razao_social": "Empresa XYZ Ltda",
  "rating": "B",
  "score": 720,
  "recomendacao": "Aprovado",
  "limite_recomendado": 500000.00,
  "prazo_maximo": 360,
  "condicoes": [],
  "pontos_atencao": ["Crescimento de dívida financeira nos últimos 2 anos"],
  "validade_parecer": "2026-07-12"
}
```

Ver `examples/case-studies.json` para casos reais anonimizados.

## Common Mistakes

- Confiar em dados desatualizados — o parecer reflete apenas o momento da análise; reavaliar a cada 6 meses ou após evento relevante.
- Tratar o parecer como due diligence completa para valores > R$ 5M; nesses casos é necessária análise adicional.
- Usar para escrever conteúdo sobre risco em vez de analisar um cliente específico → use `skill-traderisk-content-writer`.
