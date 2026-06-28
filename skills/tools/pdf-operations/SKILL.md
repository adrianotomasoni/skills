---
name: pdf-operations
description: "Extrai, analisa e estrutura informações de documentos PDF — texto, tabelas e cláusulas de contratos, editais e documentos financeiros. Use SEMPRE que houver: extrair texto/tabelas de um PDF, rodar OCR em PDF escaneado, identificar cláusulas/datas/valores em contratos, converter tabelas de PDF para JSON/CSV. Não usar para parsing genérico de outros formatos como Excel/CSV (use file-reading)."
---

# PDF Operations

## Overview

Você é um especialista em processamento de arquivos PDF. Sua função é extrair, analisar e estruturar informações de documentos PDF, especialmente contratos, editais e documentos financeiros.

## Quando usar

- Extrair texto ou tabelas de um PDF
- Rodar OCR em um PDF escaneado
- Identificar cláusulas, datas e valores em contratos
- Converter tabelas de PDF para JSON/CSV
- **Quando NÃO usar:** parsing genérico de outros formatos (Excel/CSV/Word) → use `file-reading`

## Core Pattern

### Extração de Texto
- Texto corrido de PDFs nativos
- OCR para PDFs escaneados (via integração externa)
- Preservação de estrutura (parágrafos, listas, tabelas)

### Extração de Tabelas
- Detecção automática de tabelas
- Conversão para JSON/CSV
- Preservação de headers e merge cells

### Análise de Cláusulas
- Identificação de cláusulas-chave em contratos
- Extração de datas, valores, partes
- Detecção de cláusulas de garantia

## Método passo a passo

1. **Detectar nativo vs escaneado**: meça o texto extraível da 1ª página. Muito
   texto → nativo; quase nada → escaneado (vai precisar de OCR).
2. **Extração de texto** (nativo): extraia preservando layout (`-layout`) para
   manter colunas e tabelas legíveis.
3. **OCR se necessário** (escaneado): aplique OCR em português, depois extraia o
   texto do PDF com camada OCR. Só faça OCR quando o passo 1 indicar escaneado —
   evita latência desnecessária.
4. **Extração de tabelas**: detecte tabelas, trate cabeçalhos e merge cells,
   converta para JSON `{ "headers": [...], "rows": [[...]] }`.
5. **Análise de cláusulas**: mapeie cláusulas-chave para campos (partes, valor,
   vigência, garantias, datas) usando padrões/regex sobre o texto.
6. **Validação/saída**: normalize datas (ISO) e valores (número), valide CNPJ,
   registre `campos_nao_encontrados` e `confianca`; retorne JSON estruturado.

## Exemplos concretos

### Pseudo-fluxo de extração de um contrato (texto → tabela → cláusulas)

```bash
# 1. Detectar tipo
pdftotext -f 1 -l 1 contrato.pdf - | wc -c   # ~0 => escaneado

# 2/3. Texto (com fallback de OCR se escaneado)
ocrmypdf --language por contrato.pdf contrato-ocr.pdf   # só se escaneado
pdftotext -layout contrato-ocr.pdf contrato.txt
```

```python
# 4. Tabela -> JSON
import camelot
cronograma = camelot.read_pdf("contrato.pdf", pages="3")[0].df

# 5. Cláusula -> campo
import re
m = re.search(r"valor total de R\$\s*([\d.,]+)", texto)
valor = float(m.group(1).replace(".", "").replace(",", ".")) if m else None
```

**Exemplo de saída:**

```json
{
  "tipo_documento": "contrato",
  "partes": [{ "papel": "CONTRATANTE", "cnpj": "12.345.678/0001-90" }],
  "valor": 120000.0,
  "datas": { "assinatura": "2026-01-15", "fim_vigencia": "2027-01-31" },
  "vigencia": "12 meses",
  "confianca": 0.93,
  "campos_nao_encontrados": ["clausula_reajuste"]
}
```

Fluxo completo em [`examples/fluxo-extracao-contrato.md`](examples/fluxo-extracao-contrato.md);
tabela em [`examples/tabela-extraida.json`](examples/tabela-extraida.json).

## Quick Reference

| Operação | Saída |
|----------|-------|
| Extração de texto nativo | Texto com estrutura preservada |
| OCR (PDF escaneado) | Texto (latência adicional) |
| Extração de tabelas | JSON / CSV com headers |
| Análise de cláusulas | Datas, valores, partes, garantias |

### Limitações

- PDFs escaneados requerem OCR (latência adicional)
- Formatação complexa pode reduzir precisão
- Máximo de 200 páginas por operação

## Common Mistakes

- Tratar PDF escaneado como nativo → exige OCR, senão o texto vem vazio.
- Rodar OCR em todo PDF por padrão → latência desnecessária; só faça quando o passo 1 indicar escaneado.
- Extrair texto sem preservar layout → colunas e tabelas viram texto embaralhado.
- Ignorar merge cells em tabelas → quebra o mapeamento de headers.
- Não normalizar valores ("R$ 1.200,50" mantido como string) → quebra cálculos.
- Confundir valor de cronograma de pagamentos com valor total do contrato.
- Processar PDFs acima de 200 páginas em uma operação → dividir em lotes.
- Confiar em formatação complexa sem validar → revisar precisão da extração.
- Não registrar `confianca`/`campos_nao_encontrados` → esconde incerteza da extração.

## Referências / Embasamento

- [`examples/fluxo-extracao-contrato.md`](examples/fluxo-extracao-contrato.md) — pseudo-fluxo de extração de contrato (detectar → extrair → OCR fallback → tabelas → cláusulas → validar).
- [`examples/tabela-extraida.json`](examples/tabela-extraida.json) — exemplo de tabela (cronograma de pagamentos) extraída de PDF para JSON.
