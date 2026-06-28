# File Reading

## O que é

Skill para ler e extrair conteúdo estruturado de arquivos (PDF, Excel/CSV, Word,
imagens), retornando os dados em JSON com indicador de confiança e lista de
campos não encontrados.

## Gatilhos

Use quando precisar:

- Ler ou extrair dados de um documento ou planilha
- Identificar campos-chave em formulários
- Extrair tabelas de arquivos
- Transformar um documento em dados estruturados (JSON)

Não use para manipulação avançada específica de PDF (OCR, cláusulas) → use a
skill `pdf-operations`.

## Como usar (por plataforma)

- **Claude Code / Agent SDK**: a skill é carregada automaticamente quando a
  tarefa casa com os gatilhos; siga o protocolo de 5 passos do `SKILL.md`.
- **Geral**: aplique o protocolo manualmente — identificar tipo → extrair
  estrutura → validar → retornar JSON.

## Exemplo

Entrada: `contrato-prestacao-servicos.pdf`. Saída: JSON com `partes`, `valor`,
`datas`, `vigencia`, `confianca` e `campos_nao_encontrados`. Ver
[`examples/saida-contrato.json`](examples/saida-contrato.json).

## Exemplos

- [`examples/protocolo-extracao.md`](examples/protocolo-extracao.md) — protocolo aplicado a um contrato e a uma planilha.
- [`examples/saida-contrato.json`](examples/saida-contrato.json) — saída JSON de extração de contrato.

## Versão

**1.0.0**

## Estrutura

```
file-reading/
├── SKILL.md                      # Definição da skill
├── README.md                     # Este arquivo
└── examples/
    ├── protocolo-extracao.md     # Protocolo de leitura aplicado
    └── saida-contrato.json       # Exemplo de saída JSON
```
