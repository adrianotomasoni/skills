# Análise de Risco de Crédito

Skill para análise de risco de crédito comercial B2B, gerando pareceres estruturados com rating A-F e recomendações de exposição.

## Versão

**2.1.0**

## Como Usar

### Exemplo de Prompt
```
Analise o risco de crédito da seguinte empresa:

CNPJ: 12.345.678/0001-90
Razão Social: Construtora XYZ Ltda
Faturamento anual: R$ 8.500.000
Dívida financeira: R$ 1.200.000
Histórico Serasa: sem restrições
Processos ativos: 2 trabalhistas (R$ 150.000 total)
Setor: Construção civil
```

## Estrutura

```
credit-risk-analysis/
├── SKILL.md              # Definição da skill
├── README.md             # Este arquivo
├── templates/
│   ├── credit-assessment.md   # Template de parecer
│   └── score-calculator.js    # Calculadora de score
└── examples/
    └── case-studies.json
```

## Tags

`credit` `risk` `rating` `parecer` `b2b`
