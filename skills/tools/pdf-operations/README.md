# PDF Operations

## O que é

Skill para extrair, analisar e estruturar informações de documentos PDF — texto,
tabelas e cláusulas de contratos, editais e documentos financeiros, com suporte
a OCR para PDFs escaneados.

## Gatilhos

Use quando precisar:

- Extrair texto ou tabelas de um PDF
- Rodar OCR em um PDF escaneado
- Identificar cláusulas, datas e valores em contratos
- Converter tabelas de PDF para JSON/CSV

Não use para parsing genérico de outros formatos (Excel/CSV/Word) → use a skill
`file-reading`.

## Como usar (por plataforma)

- **Claude Code / Agent SDK**: a skill é carregada automaticamente quando a
  tarefa casa com os gatilhos; siga o método de 6 passos do `SKILL.md`.
- **Geral**: aplique o fluxo manualmente — detectar nativo/escaneado → extrair
  texto → OCR se necessário → tabelas → cláusulas → validar/saída.

## Exemplo

Entrada: `contrato.pdf` (escaneado). Fluxo: detectar escaneado → OCR → extrair
cronograma de pagamentos como tabela → JSON. Ver
[`examples/tabela-extraida.json`](examples/tabela-extraida.json).

## Exemplos

- [`examples/fluxo-extracao-contrato.md`](examples/fluxo-extracao-contrato.md) — pseudo-fluxo completo de extração de contrato.
- [`examples/tabela-extraida.json`](examples/tabela-extraida.json) — tabela (cronograma de pagamentos) extraída de PDF para JSON.

## Versão

**1.0.0**

## Estrutura

```
pdf-operations/
├── SKILL.md                          # Definição da skill
├── README.md                         # Este arquivo
└── examples/
    ├── fluxo-extracao-contrato.md    # Pseudo-fluxo de extração
    └── tabela-extraida.json          # Tabela extraída em JSON
```
