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
- Não validar formato de valores/datas/CPF/CNPJ → dados extraídos inconsistentes.
- Omitir `campos_nao_encontrados` → esconde lacunas na extração.
- Retornar texto livre em vez de JSON estruturado → quebra integrações downstream.
