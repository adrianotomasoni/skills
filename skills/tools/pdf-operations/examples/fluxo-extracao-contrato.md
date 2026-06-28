# Pseudo-fluxo de extração de contrato (PDF)

Fluxo documentado de ponta a ponta para extrair dados de um contrato em PDF:
detectar tipo → extrair texto → OCR fallback → tabelas → cláusulas → validar.
Os comandos são ilustrativos (ferramentas variam por ambiente).

---

## 1. Detectar nativo vs escaneado

```bash
# Conta caracteres de texto extraível na primeira página.
pdftotext -f 1 -l 1 contrato.pdf - | wc -c
```

- Saída com muitos caracteres → **PDF nativo** (siga ao passo 2).
- Saída ~0 → **PDF escaneado** (pule para o passo 3, OCR).

## 2. Extração de texto (nativo)

```bash
pdftotext -layout contrato.pdf contrato.txt
```

- `-layout` preserva a disposição em colunas, ajudando na leitura de tabelas.
- Resultado: texto corrido com parágrafos e cláusulas.

## 3. OCR (fallback para escaneado)

```bash
# Renderiza páginas como imagens e aplica OCR em português.
ocrmypdf --language por --force-ocr contrato.pdf contrato-ocr.pdf
pdftotext -layout contrato-ocr.pdf contrato.txt
```

- OCR adiciona latência; aplique somente quando o passo 1 indicar escaneado.
- TODO: usar o serviço de OCR proprietário TradeRisk quando disponível.

## 4. Extração de tabelas

```python
# Exemplo ilustrativo com uma lib de extração de tabelas.
import camelot
tabelas = camelot.read_pdf("contrato.pdf", pages="3-4")
cronograma = tabelas[0].df  # cabeçalho + linhas
```

- Detecte cabeçalhos e trate merge cells.
- Converta para JSON no formato `{ "headers": [...], "rows": [[...]] }`.
- Exemplo de saída em [`tabela-extraida.json`](tabela-extraida.json).

## 5. Análise de cláusulas

A partir do texto, mapeie cláusulas-chave para campos:

| Cláusula / trecho | Campo extraído |
|-------------------|----------------|
| Qualificação das partes | `partes[]` (nome, CNPJ, papel) |
| "valor total de R$ ..." | `valor` |
| "vigência de N meses" | `vigencia` |
| Cláusula de garantia | `garantias[]` |
| Datas de assinatura/início/fim | `datas` |

```python
import re
m = re.search(r"valor total de R\$\s*([\d.,]+)", texto)
valor = float(m.group(1).replace(".", "").replace(",", ".")) if m else None
```

## 6. Validação e saída

- Normalize datas para ISO `AAAA-MM-DD` e valores para número.
- Valide dígitos verificadores de CNPJ.
- TODO: cruzar partes com a base cadastral proprietária TradeRisk.
- Campos ausentes vão para `campos_nao_encontrados`.

```json
{
  "tipo_documento": "contrato",
  "partes": [
    { "papel": "CONTRATANTE", "cnpj": "12.345.678/0001-90" }
  ],
  "valor": 120000.0,
  "datas": { "assinatura": "2026-01-15", "fim_vigencia": "2027-01-31" },
  "vigencia": "12 meses",
  "cronograma_pagamentos": "ver tabela-extraida.json",
  "confianca": 0.93,
  "campos_nao_encontrados": ["clausula_reajuste"]
}
```
