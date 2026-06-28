# Casos-Referência (banco real — calibração)

## Caso de roteamento fase/evento

`0000288-16.2022.5.12.0034` (TRT-12): antes fase=recursal / evento=depósito recursal → após
PR #141, fase=execução / evento=garantia da execução → produto =
`seguro_garantia_execucao_trabalhista`.
**Lição:** "agravo de petição" e marcadores de execução vencem o rótulo recursal (trava C3).

## Casos de não-venda (EPAVI / HAVAN)

- Vários processos `status_analitico_v3 = encerrado` com `score 0` → corretamente fora de venda.
- Processos com `garantia_e_traderisk = true` → acompanhamento/renovação, não venda nova.
- EPAVI em polo "ativo" → corretamente `fora_escopo`; EPAVI em polo "passivo" → oportunidade legítima.

## Exemplo de entrada (dump V3 de um processo)

```json
{
  "numero_cnj": "0001487-41.2025.5.09.0652",
  "tribunal": "TRT-9",
  "esfera_v3": "trabalhista",
  "fase_v3": "execucao",
  "evento_garantia_v3": "deposito_recursal_trabalhista",
  "tipo_oportunidade_v3": "seguro_garantia_recursal_trabalhista",
  "status_analitico_v3": "oportunidade",
  "score_v3": 72,
  "urgencia_v3": "alta",
  "nivel_garantia_v3": "sem_garantia",
  "garantia_e_traderisk": false,
  "valor_causa": 128000.00,
  "valor_execucao": null,
  "valor_a_garantir": null,
  "fonte_valor": null,
  "partes": [
    { "nome": "HAVAN S.A.", "cnpj": "79379491000183", "polo": "passivo" }
  ]
}
```

## Golden output esperado (aplica a trava C3)

```
PROCESSO: 0001487-41.2025.5.09.0652  | TOMADOR: HAVAN S.A. (79.379.491/0001-83) | TRIBUNAL: TRT-9
─────────────────────────────────────────────────────────────────────
STATUS COMERCIAL : oportunidade
ESFERA / FASE    : trabalhista / execucao
GATILHO          : garantia_execucao_trabalhista — fase de execucao em curso (corrige rotulo de deposito recursal por incoerencia C3)
PRODUTO SUGERIDO : seguro_garantia_execucao_trabalhista
BASE LEGAL       : CLT art. 882 (Lei 13.467/2017); CPC art. 835 §2º
URGENCIA         : alta — execucao trabalhista com risco de penhora online (SISBAJUD)
VALOR A GARANTIR : indisponivel (valor_a_garantir nulo; valor_causa R$ 128.000,00) — estimar debito + 30% apos liquidacao
GARANTIA ATUAL   : sem_garantia | Traderisk? nao
PITCH (corretor) : Processo ja em execucao no TRT-9: o seguro garantia equivale a dinheiro (CLT 882) e bloqueia a penhora online, liberando o caixa da Havan. Substituimos qualquer constricao por apolice imediata.
RESSALVA         : valor_a_garantir nulo no banco — confirmar debito atualizado antes de cotar (+30%).
```

**Nota de calibração:** o dump trazia `evento = deposito_recursal_trabalhista` com `fase = execucao`
— combinação proibida. O agente aplicou C3 e rebaixou para `garantia_execucao_trabalhista`,
ajustando produto e base legal. Esse é exatamente o tipo de incoerência que o agente deve corrigir.
