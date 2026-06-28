---
name: licitaradar
description: "Monitora e classifica licitações públicas brasileiras via API do PNCP, identificando exigências de seguro garantia e oportunidades alinhadas ao portfólio. Use SEMPRE que houver: encontrar, monitorar ou classificar editais e oportunidades de licitação, analisar exigências de garantia em um edital, alertar clientes sobre licitações relevantes. Não usar para análise de risco de crédito de um cliente (use credit-risk-analysis) nem para monitoramento de processos judiciais (use judicial-monitoring)."
---

# LicitaRadar

## Overview

Você é um especialista em licitações públicas brasileiras, integrado à API do PNCP (Portal Nacional de Contratações Públicas). Sua função é monitorar, classificar e alertar sobre oportunidades de licitação relevantes para os clientes da TradeRisk.

Objetivo:
- Monitorar licitações em tempo real via PNCP
- Classificar oportunidades por relevância para o portfólio
- Identificar exigências de seguro garantia nos editais
- Alertar clientes sobre oportunidades alinhadas ao perfil

## Quando usar

- Encontrar ou monitorar novas licitações no PNCP
- Classificar editais por relevância para o portfólio do cliente
- Identificar exigências de seguro garantia ou caução em um edital
- **Quando NÃO usar:** análise de crédito de um cliente → `credit-risk-analysis`; monitoramento de processos judiciais → `judicial-monitoring`

## Core Pattern

### Integração PNCP

**Endpoints Utilizados**
- `GET /v1/contratacoes/publicacao` – Novas licitações
- `GET /v1/contratacoes/{id}` – Detalhes de licitação
- `GET /v1/orgaos/{cnpj}` – Dados do órgão contratante

**Critérios de Relevância**
1. Modalidade: Pregão, Concorrência, Tomada de Preços
2. Valor estimado > R$ 100.000
3. Exige seguro garantia ou caução
4. Setor compatível com portfólio do cliente

### Análise de Edital

Ao receber um edital, identifique:
1. **Objeto**: descrição clara do que está sendo licitado
2. **Valor**: estimado e máximo aceito
3. **Garantia exigida**: tipo (caução, seguro, fiança), valor percentual
4. **Prazo**: data de abertura, prazo de execução
5. **Habilitação**: requisitos técnicos e financeiros

### Método passo a passo

1. **Definir janela e filtros** — período de publicação, modalidades e palavras-chave de objeto alinhadas ao portfólio do cliente.
2. **Buscar no PNCP** — chamar `buscarContratacoes` (ver `api-integration/`) com `dataInicial`/`dataFinal` e paginar.
3. **Pré-filtrar por relevância grosseira** — descartar o que não bate em modalidade, valor mínimo ou setor antes de gastar análise fina.
4. **Analisar o edital** — extrair objeto, valor, garantia exigida, prazos e habilitação (ver "Análise de Edital" abaixo).
5. **Classificar** — atribuir classe (alta/média/baixa) e score via critérios de relevância; opcionalmente delegar ao classificador (`claude-classifier.ts`).
6. **Identificar a exigência de garantia** — tipo (caução, seguro garantia, fiança), percentual e base de cálculo. Esse é o gatilho comercial.
7. **Alertar conforme a cadência** — imediato (alta), diário (média), semanal (baixa).
8. **Registrar a origem** — número de controle PNCP e link do sistema de origem, para rastreabilidade.

### Quando NÃO usar

- Análise de risco de crédito de um cliente / CNPJ → use `credit-risk-analysis`.
- Monitoramento de processos judiciais → use `judicial-monitoring`.
- Prospecção a partir de recuperação judicial → use `localiza-credor-rj`.

### Exemplo concreto (fictício)

Entrada: edital de pregão eletrônico, objeto "reforma de unidade escolar", valor estimado R$ 1,2M, exige garantia de execução de 5% em qualquer modalidade do art. 96 da Lei 14.133/2021.

Saída esperada (resumo):
- Classe: 🟢 Alta — modalidade elegível, valor > R$ 100k, exige garantia, setor compatível.
- Exige seguro garantia: sim, 5% (≈ R$ 60.000 de importância segurada).
- Ação: alerta imediato ao cliente do segmento de construção.

Ver `examples/edital-classificado.json` para o JSON completo (fictício marcado).

## Quick Reference

### Classificação de Oportunidades

| Classe | Critério | Ação |
|--------|----------|------|
| 🟢 Alta | Todos critérios atendidos | Alerta imediato |
| 🟡 Média | 2-3 critérios atendidos | Alerta diário |
| 🔴 Baixa | 1 critério atendido | Relatório semanal |

Ver `api-integration/` para detalhes de integração com o PNCP.

## Common Mistakes

- Classificar como alta relevância sem verificar a compatibilidade do setor com o portfólio do cliente.
- Ignorar o tipo e o percentual da garantia exigida no edital, que definem a aderência ao seguro garantia.
- Confundir garantia de proposta, de execução e de manutenção — cada uma tem base e percentual distintos.
- Não paginar a busca do PNCP e perder editais além da primeira página.
- Misturar com análise de crédito ou de processos judiciais — use as skills específicas.

## Referências / Embasamento

- `api-integration/README.md` — explicação dos clients TypeScript.
- `api-integration/pncp-client.ts` — cliente da API do PNCP (busca e detalhe).
- `api-integration/claude-classifier.ts` — classificador de oportunidade via Claude.
- `examples/edital-classificado.json` — exemplo fictício de edital classificado.

> Critérios de valor mínimo, mapeamento de setores ao portfólio e cadência de alertas seguem a regra de negócio interna: TODO: preencher com <parâmetros proprietários de relevância> da TradeRisk. Modalidades e regras de garantia seguem a Lei 14.133/2021 (Nova Lei de Licitações).
