---
name: localiza-credor-rj
description: "Inteligência de prospecção para Seguro de Crédito a partir de Recuperação Judicial e falência. Use SEMPRE que houver: mapear credores de empresas em RJ/falência, extrair lista de credores de edital ou quadro-geral, transformar processo de RJ em leads B2B, identificar empresas expostas a inadimplência de um devedor em crise, qualificar credor PJ como prospect de Seguro de Crédito, ou cruzar Radar RJ com base de prospecção. A RJ é um mapa de exposição comercial: o credor PJ exposto é o alvo, NÃO o devedor. Acionar mesmo quando o usuário só menciona um edital de RJ, quadro de credores, ou nome de empresa em recuperação."
---

# Localiza Credor RJ — Inteligência Preventiva de Seguro de Crédito

## Propósito

Recuperação judicial e falência não são apenas eventos jurídicos. São **mapas de exposição comercial**: cada empresa em RJ tem dezenas ou centenas de credores que vão sofrer o calote ou o deságio. Esses credores PJ são os compradores naturais de Seguro de Crédito — eles acabaram de descobrir, na pele, o que é risco de inadimplência B2B.

Esta skill transforma o quadro de credores de uma RJ em **leads consultivos qualificados** para Seguro de Crédito, preservando origem dos dados, conformidade LGPD B2B e abordagem não-sensacionalista.

---

## Distinção fundamental (nunca confundir)

| Entidade | O que é | Papel nesta skill |
|---|---|---|
| **Devedor** | Empresa em RJ/falência | Fonte do mapa. NÃO é alvo comercial. NÃO é avaliado por risco aqui |
| **Credor PJ** | Empresa listada no quadro-geral de credores | **O ALVO.** Lead de Seguro de Crédito |
| **Documento-fonte** | Edital, quadro-geral, lista do AJ, processo CNJ | Rastreabilidade. Sempre preservar |
| **Lead comercial** | Credor PJ qualificado + score + abordagem | Entregável final |

> O credor aparecer em uma RJ é **sinal de timing**, não de risco do próprio credor. No modelo de score de prospecção, esse sinal vale apenas o **bônus 5** (timing). O risco/score/protesto do prospect pertence à fase de **cotação**, nunca à prospecção.

---

## PASSO 0 — Identificar o documento de origem

Antes de qualquer extração, classifique o que foi recebido:

1. **Edital de convocação de AGC** — lista resumida, pode ter só nomes
2. **Quadro-geral de credores (QGC)** — fonte mais rica: nome, CNPJ, classe, valor
3. **Relação de credores do Administrador Judicial** — frequentemente em PDF/site do AJ
4. **Processo CNJ / DataJud** — exige navegar até a peça correta
5. **Menção solta** (ex.: "empresa X entrou em RJ") — exige localizar o processo primeiro

A confiança do resultado depende diretamente da qualidade da fonte. QGC com CNPJ e valor = alta confiança. Edital só com nomes = exige enriquecimento por CNPJ.

---

## PASSO 1 — Localizar processo e documentos públicos

Priorize fontes públicas rastreáveis, nesta ordem:

- **DataJud / CNJ** — metadados processuais (já integrado ao stack Radar RJ)
- **Site do Administrador Judicial** — costuma publicar QGC em PDF
- **Diário de Justiça / publicações de edital**
- **Juntas comerciais / Receita Federal** — para validar CNPJ do credor

Sempre registre a URL/origem de cada dado. Nenhum lead entra na base sem documento-fonte rastreável.

---

## PASSO 2 — Extrair e estruturar credores

Do quadro de credores, extraia para cada credor PJ:

| Campo | Origem | Obrigatório |
|---|---|---|
| Razão social | QGC | Sim |
| CNPJ | QGC ou enriquecimento | Sim (enriquecer se faltar) |
| Classe do crédito | QGC (I–IV) | Quando disponível |
| Valor habilitado | QGC | Quando disponível |
| Devedor (processo de origem) | Documento-fonte | Sim (interno, NÃO exposto ao lead) |
| Documento-fonte / URL | Passo 1 | Sim |

Descarte credores que sejam:
- Pessoas físicas (fora do escopo B2B)
- Instituições financeiras (não compram seguro de crédito)
- Fazenda Pública / órgãos (classe tributária)
- O próprio grupo econômico do devedor

---

## PASSO 3 — Enriquecer (CNPJ → perfil de prospecção)

Para cada credor PJ com CNPJ válido, enriquecer via **direct.data — Cadastro PJ Básica (R$0,16/CNPJ)**:
- CNAE principal e secundários
- Porte / faturamento presumido
- Situação cadastral

Seletivamente, **QSA (R$2,80)** apenas para credores de alto valor, para nome de decisor.
Para flag de exportador, cruzar com **COMEX STAT (MDIC, gratuito)**.

> direct.data consulta POR CNPJ — enriquece a lista, não a gera. A lista vem do quadro de credores (Passo 2).

---

## PASSO 4 — Score de prioridade (0–100)

Aplicar o modelo de prospecção de Seguro de Crédito. O credor é avaliado por **quão bom prospect ele é** (vende a prazo? B2B? porte certo?), não pelo risco dele:

| Critério | Peso |
|---|---|
| Exporta / vende a prazo (CNAE indicativo) | 30 |
| CNAE industrial / atacadista | 25 |
| Faixa de valor de exportação | 15 |
| Porte R$20M–500M | 15 |
| Perfil B2B | 10 |
| **Sinal credor em RJ (bônus de timing)** | **5** |

Faixas: 80–100 prioridade máxima · 60–79 alta · 40–59 média · <40 descartar ou nutrir.

---

## PASSO 5 — Sugestão de abordagem (consultiva, não sensacionalista)

Gere a abordagem comercial respeitando **regras invioláveis**:

- ❌ **NUNCA** expor que o lead apareceu como credor de processo específico ("vi que você é credor da Empresa X na RJ...")
- ❌ Sem sensacionalismo, sem medo, sem "você vai tomar calote"
- ✅ Abordagem por **risco setorial e prevenção**: "empresas do seu setor têm enfrentado aumento de inadimplência B2B; o Seguro de Crédito protege o fluxo de recebíveis"
- ✅ Campanhas agregadas por setor/CNAE, nunca individualizando a origem do dado
- ✅ Conformidade LGPD B2B: dado público, finalidade legítima, sem exposição de origem sensível

---

## Saída estruturada

Retornar sempre:

```json
{
  "devedor_origem": { "razao_social": "", "processo": "", "comarca": "" },
  "documento_fonte": { "tipo": "QGC", "url": "" },
  "credores_qualificados": [
    {
      "razao_social": "",
      "cnpj": "",
      "cnae_principal": "",
      "porte": "",
      "exportador": false,
      "valor_habilitado": null,
      "classe_credito": "",
      "score_prospeccao": 0,
      "prioridade": "alta|media|baixa",
      "abordagem_sugerida": "",
      "origem_exposta_ao_lead": false
    }
  ]
}
```

---

## Integração com o stack Radar RJ

- Persistir no schema **`radar_rj`** do projeto Supabase de Seguro de Crédito
- Reaproveitar a Edge Function de qualificação (`alvo-qualificar`) para a chamada direct.data
- pg_cron para reprocessamento periódico de novos editais
- O sinal "credor em RJ" entra como campo de timing, somando o bônus 5 ao score — nunca substituindo a lógica de prospecção principal

## Regras invioláveis (resumo)

1. Devedor é fonte, credor PJ é alvo — nunca inverter
2. Toda origem de dado é rastreável e preservada
3. Nunca expor ao lead que ele apareceu como credor
4. Sem sensacionalismo; campanhas por risco setorial
5. Risco do prospect é assunto da cotação, não da prospecção
6. LGPD B2B: dado público, finalidade legítima
