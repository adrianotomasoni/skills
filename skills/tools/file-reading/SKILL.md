---
name: file-reading
description: "Lê e extrai conteúdo estruturado de arquivos (PDF, Excel/CSV, Word, imagens), retornando dados em JSON. Use SEMPRE que houver: ler/extrair dados de um documento ou planilha, identificar campos-chave em formulários, extrair tabelas de arquivos, transformar um documento em dados estruturados. Não usar para manipulação avançada específica de PDF (use pdf-operations)."
---

# File Reading

## Overview

Você é um especialista em leitura, processamento e extração de informações de arquivos. Sua função é analisar documentos e extrair dados estruturados de forma precisa.

## Quando usar

- Ler ou extrair dados de um documento ou planilha
- Identificar campos-chave em formulários
- Extrair tabelas de arquivos
- Transformar um documento em dados estruturados (JSON)
- **Quando NÃO usar:** manipulação avançada específica de PDF (OCR, cláusulas) → use `pdf-operations`

## Core Pattern

### Capacidades

- Leitura de PDFs (contratos, editais, balanços)
- Parsing de planilhas Excel/CSV
- Extração de tabelas de documentos
- Identificação de campos-chave em formulários

### Protocolo de Leitura

1. **Identificar tipo**: PDF, Excel, Word, imagem, etc.
2. **Extrair estrutura**: seções, tabelas, campos
3. **Verificar completude**: dados essenciais presentes?
4. **Validar formato**: valores numéricos, datas, CPF/CNPJ
5. **Retornar estruturado**: JSON com dados extraídos

## Método passo a passo

Aplique sempre os 5 passos abaixo, com as sub-ações específicas por tipo de arquivo.

### Passo 1 — Identificar tipo

- Inspecione extensão **e** conteúdo (não confie só na extensão).
- **PDF**: verifique se há camada de texto selecionável. Se for escaneado
  (somente imagem), encaminhe para a skill `pdf-operations` (OCR).
- **Excel/CSV**: liste as abas (`.xlsx`) ou detecte separador (`,`/`;`) e
  encoding (UTF-8/Latin-1) em `.csv`.
- **Imagem** (formulário escaneado): identifique que precisa de OCR/visão antes
  de extrair campos.

### Passo 2 — Extrair estrutura

- **PDF/contrato**: mapeie seções e cláusulas para campos-alvo (partes, valor,
  vigência, foro).
- **Excel/CSV**: trate a primeira linha como cabeçalho → chaves; demais linhas →
  registros. Marque ou ignore linhas de total/subtotal.
- **Imagem/formulário**: localize rótulos (labels) e seus valores associados
  (ex.: "Nome:", "CPF:", "Data:").

### Passo 3 — Verificar completude

- Liste os campos essenciais esperados para o tipo de documento.
- Tudo que não foi encontrado vai para `campos_nao_encontrados` — nunca invente.

### Passo 4 — Validar formato

- **Valores monetários**: "R$ 120.000,00" → `120000.00` (número, sem separador
  de milhar, ponto decimal).
- **Datas**: normalize para ISO `AAAA-MM-DD`.
- **CPF/CNPJ**: valide dígitos verificadores.
- **Percentuais**: defina e mantenha uma convenção (`12,5%` → `0.125` ou `12.5`).

### Passo 5 — Retornar estruturado

- Sempre JSON no formato de saída padrão (ver Quick Reference).
- Inclua `confianca` (0–1) e `campos_nao_encontrados`.

## Exemplos concretos

### PDF — Contrato

**Input:** `contrato-prestacao-servicos.pdf` (PDF nativo, 5 páginas).

**Saída esperada (resumida):**

```json
{
  "tipo_documento": "contrato",
  "campos_extraidos": {
    "partes": [
      { "papel": "CONTRATANTE", "cnpj": "12.345.678/0001-90" },
      { "papel": "CONTRATADA", "cnpj": "98.765.432/0001-10" }
    ],
    "valor": 120000.0,
    "datas": { "assinatura": "2026-01-15", "fim_vigencia": "2027-01-31" },
    "vigencia": "12 meses"
  },
  "confianca": 0.94,
  "campos_nao_encontrados": ["clausula_reajuste"]
}
```

Saída completa em [`examples/saida-contrato.json`](examples/saida-contrato.json).

### Excel/CSV — Planilha financeira

**Input:** `fluxo-caixa-2026.xlsx` (aba `fluxo_caixa`, cabeçalho na linha 1).

**Saída esperada (resumida):**

```json
{
  "tipo_documento": "planilha_financeira",
  "campos_extraidos": {
    "colunas": ["mes", "receita", "despesa", "saldo"],
    "linhas": [
      { "mes": "2026-01", "receita": 50000.0, "despesa": 32000.0, "saldo": 18000.0 }
    ]
  },
  "confianca": 0.92,
  "campos_nao_encontrados": []
}
```

### Imagem — Formulário escaneado

**Input:** `ficha-cadastral.png` (foto de formulário preenchido à mão).

**Saída esperada (resumida):**

```json
{
  "tipo_documento": "formulario_cadastral",
  "campos_extraidos": {
    "nome": "TODO: nome do cliente (dado proprietário)",
    "cpf": "123.456.789-09",
    "data_nascimento": "1985-03-22"
  },
  "confianca": 0.78,
  "campos_nao_encontrados": ["telefone"]
}
```

> Observação: imagens manuscritas tendem a `confianca` mais baixa — sinalize
> campos duvidosos em vez de afirmar com falsa certeza.

## Quick Reference

### Formato de Saída

```json
{
  "tipo_documento": "contrato",
  "campos_extraidos": {
    "partes": [],
    "valor": 0,
    "data": "",
    "vigencia": ""
  },
  "confianca": 0.95,
  "campos_nao_encontrados": []
}
```

## Common Mistakes

- Pular a identificação do tipo de arquivo → leva a parsing incorreto.
- Confiar só na extensão (ex.: PDF escaneado tratado como nativo) → texto vem vazio; era caso de OCR/`pdf-operations`.
- Não validar formato de valores/datas/CPF/CNPJ → dados extraídos inconsistentes.
- Manter separador de milhar ou vírgula decimal em números → quebra cálculos downstream.
- Inventar valores para campos ausentes em vez de listá-los em `campos_nao_encontrados`.
- Omitir `campos_nao_encontrados` → esconde lacunas na extração.
- Reportar `confianca` alta em extração de imagem manuscrita → falsa certeza.
- Em CSV, ignorar encoding/separador → acentuação corrompida ou colunas desalinhadas.
- Em Excel, processar a aba errada ou somar linhas de total como se fossem dados.
- Retornar texto livre em vez de JSON estruturado → quebra integrações downstream.

## Referências / Embasamento

- [`examples/protocolo-extracao.md`](examples/protocolo-extracao.md) — protocolo de 5 passos aplicado a um contrato e a uma planilha.
- [`examples/saida-contrato.json`](examples/saida-contrato.json) — exemplo de saída JSON estruturada para um contrato.
