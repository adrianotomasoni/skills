# Agente `buscador-sgj` — Buscador de Oportunidades de Seguro Garantia Judicial

Agente **comercial-jurídico** que consome a saída do **motor V3 / pipeline V4** da TradeRisk
(`oportunidades` + `processos` + `partes` + `movimentacoes` + `documentos`) e produz **pareceres
comerciais acionáveis** de **seguro garantia judicial** nas esferas **trabalhista, fiscal e cível**.

Não substitui o motor V3 — interpreta sua saída em linguagem de corretor, explicando o gatilho
processual e a base legal de cada oportunidade.

## Não confundir (sem duplicação)
- **Risco** de apólice/processo já garantido → agente `judicial-watcher`.
- **Prospecção de Seguro de Crédito** via RJ/falência → skill `localiza-credor-rj`.
- **Venda de garantia judicial** (este agente) → `buscador-sgj`.

## Estrutura
```
buscador-sgj/
├── AGENT.md                    ← definição canônica do agente (formato do repo)
├── agent.json                  ← metadados + mapa de portabilidade
├── reference/
│   ├── system_prompt.md        ← NÚCLEO CANÔNICO (fonte da verdade do comportamento)
│   ├── quadro_normativo.md     ← base de citação (revisar periodicamente)
│   ├── parecer.schema.json     ← schema da saída por processo
│   └── exemplos.md             ← calibração / golden output
├── examples/                   ← processo_exemplo.json + casos_referencia.md
├── docs/REVISAO_NORMATIVA.md   ← checklist de itens normativos em transição
├── platforms/                  ← guia por plataforma (claude, openai, gemini, cursor, lovable, manus)
├── run_agent.py                ← runner provider-agnóstico
└── requirements.txt
```

## Como invocar em cada novo projeto
Veja **[docs/USAGE.md → Instalar um agente num projeto](../../docs/USAGE.md)** e o script
`scripts/install-into-project.sh`. Resumo:

```bash
# Claude Code: instala o agente em ~/.claude/agents e o disponibiliza no projeto atual
./scripts/install-into-project.sh --agent buscador-sgj --target .

# API (qualquer provider) a partir do núcleo canônico
pip install -r agents/buscador-sgj/requirements.txt
python agents/buscador-sgj/run_agent.py --provider anthropic \
  --input agents/buscador-sgj/examples/processo_exemplo.json
```

## Travas inegociáveis
Polo passivo obrigatório · encerrado alta confiança = 0 · RJ/falência exclui · fiscal nunca promete
suspensão da exigibilidade tributária · coerência fase×evento · valor execução>condenação>causa.

## Manutenção
Ao mudar o comportamento, edite **apenas** `reference/system_prompt.md` e propague para os
adaptadores. Quadro normativo (jun/2026) tem itens em transição — rode `docs/REVISAO_NORMATIVA.md`.
