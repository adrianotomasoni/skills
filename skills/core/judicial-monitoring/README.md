# Monitoramento Judicial Proativo

Skill para detecção automática de eventos relevantes em processos judiciais, com classificação de risco e recomendações de ação para operações de seguro garantia e crédito comercial.

## Versão

**4.0.0** – Unified engine com classificação multinível

## Como Usar

### Em Claude.ai
1. Faça upload de `SKILL.md` em Settings → Knowledge
2. Envie movimentações processuais para análise

### Em Cursor
```
@skills/core/judicial-monitoring/SKILL.md
Analise esta movimentação: [cole o texto aqui]
```

### Exemplo de Prompt
```
Analise a seguinte movimentação e classifique o risco:

Processo: 0001234-56.2026.8.26.0100
Movimento: "Penhora sobre bem imóvel, avaliado em R$ 450.000,00"
Parte garantida: Construtora XYZ Ltda
Apólice: TRK-2026-001234
```

## Estrutura

```
judicial-monitoring/
├── SKILL.md           # Definição da skill
├── README.md          # Este arquivo
├── prompts/           # Prompts especializados por fase
│   ├── fase-1-v4-unified.md
│   ├── fase-1-v3-spec.md
│   └── melhorias-motor-judicial-2026.md
├── examples/          # Casos de estudo reais anonimizados
│   └── case-studies.json
└── tests/             # Suite de avaliação
    └── eval-suite.json
```

## Tags

`judicial` `monitoring` `seguro-garantia` `risco` `eventos`

## Dependências

- `credit-risk-analysis` (para contexto de risco do garantido)
