# Protocolo de extração aplicado

Este documento mostra o protocolo de 5 passos aplicado a dois casos reais:
um contrato em PDF e uma planilha financeira em Excel. Use-o como referência
ao extrair dados de documentos.

---

## Caso 1 — Contrato (PDF)

**Entrada:** `contrato-prestacao-servicos.pdf` (5 páginas, PDF nativo).

### Passo 1 — Identificar tipo

- Extensão `.pdf` + presença de camada de texto → **PDF nativo**.
- Confirmar que não é escaneado (texto selecionável presente). Se fosse
  escaneado, encaminhar para `pdf-operations` (OCR).

### Passo 2 — Extrair estrutura

- Localizar seções típicas de contrato: qualificação das partes, objeto,
  valor, prazo/vigência, foro.
- Mapear cada cláusula a um campo-alvo do JSON de saída.

| Trecho do documento | Campo-alvo |
|---------------------|-----------|
| "CONTRATANTE: ... CONTRATADA: ..." | `partes[]` |
| "valor total de R$ ..." | `valor` |
| "assinado em DD/MM/AAAA" | `datas.assinatura` |
| "vigência de 12 (doze) meses" | `vigencia` |

### Passo 3 — Verificar completude

- Conferir se os campos essenciais (`partes`, `valor`, `vigencia`) foram
  encontrados. Campos ausentes vão para `campos_nao_encontrados`.

### Passo 4 — Validar formato

- `valor`: converter "R$ 120.000,00" → `120000.00` (número).
- Datas: normalizar para ISO `AAAA-MM-DD`.
- CNPJ das partes: validar dígitos verificadores.
- TODO: validar CNPJ contra base cadastral proprietária TradeRisk.

### Passo 5 — Retornar estruturado

Resultado em `saida-contrato.json` (mesma pasta).

---

## Caso 2 — Planilha financeira (Excel/CSV)

**Entrada:** `fluxo-caixa-2026.xlsx` (1 aba, 13 colunas, 1 linha de cabeçalho).

### Passo 1 — Identificar tipo

- Extensão `.xlsx` → planilha. Listar abas; selecionar a aba relevante.
- Para `.csv`, detectar separador (`,` ou `;`) e encoding (UTF-8/Latin-1).

### Passo 2 — Extrair estrutura

- Primeira linha = cabeçalho → vira chaves dos objetos.
- Demais linhas = registros. Ignorar linhas de total/subtotal ou marcá-las.

### Passo 3 — Verificar completude

- Conferir nº de colunas esperado e ausência de linhas vazias no meio dos
  dados. Reportar lacunas em `campos_nao_encontrados`.

### Passo 4 — Validar formato

- Valores monetários: remover separador de milhar e converter vírgula decimal.
- Datas: normalizar para ISO.
- Percentuais "12,5%" → `0.125` ou `12.5` (definir convenção e ser consistente).
- TODO: aplicar regras de classificação contábil proprietárias TradeRisk.

### Passo 5 — Retornar estruturado

```json
{
  "tipo_documento": "planilha_financeira",
  "campos_extraidos": {
    "aba": "fluxo_caixa",
    "colunas": ["mes", "receita", "despesa", "saldo"],
    "linhas": [
      { "mes": "2026-01", "receita": 50000.0, "despesa": 32000.0, "saldo": 18000.0 },
      { "mes": "2026-02", "receita": 47000.0, "despesa": 35000.0, "saldo": 12000.0 }
    ]
  },
  "confianca": 0.92,
  "campos_nao_encontrados": []
}
```
