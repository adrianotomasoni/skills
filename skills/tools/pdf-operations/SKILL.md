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
- Ignorar merge cells em tabelas → quebra o mapeamento de headers.
- Processar PDFs acima de 200 páginas em uma operação → dividir em lotes.
- Confiar em formatação complexa sem validar → revisar precisão da extração.
