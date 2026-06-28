---
name: auditoria-de-seo-on-page
description: "Auditoria de SEO on-page de UMA página avulsa ou externa (qualquer site/cliente), analisando title, meta description, headings, conteúdo, imagens, links internos e schema, com score e plano de ação. Use quando houver: auditar uma página ou URL específica que NÃO seja do traderisk.com.br, checklist de SEO antes de publicar conteúdo novo, ou otimização pontual de uma página isolada. IMPORTANTE: para auditar o site traderisk.com.br e suas páginas estratégicas (/seguro-garantia, /seguro-credito etc.), use seo-audit-traderisk em vez desta."
---

# Auditoria de SEO On-Page

## Overview

Esta skill faz a auditoria de SEO on-page de **uma única página** (própria, de cliente ou externa) e devolve um diagnóstico estruturado, um **score 0–100** e um **plano de ação priorizado**. O foco é exclusivamente o que está dentro da página — title, meta description, headings, corpo de texto, imagens, links internos e dados estruturados — não a estratégia de domínio inteiro nem SEO técnico de infraestrutura (sitemap, robots, Core Web Vitals avançados).

Princípio central: cada elemento on-page tem um peso fixo no score; a auditoria mede a presença e a qualidade de cada um, aponta o gap e dá a correção concreta.

## Quando usar

- Auditar uma página ou URL específica que **NÃO** seja do `traderisk.com.br`.
- Rodar um checklist de SEO **antes de publicar** um conteúdo novo (post, landing, artigo).
- Otimização pontual de uma página isolada que está performando mal em busca.
- Validar rapidamente um rascunho de copy quanto a fundamentos de SEO on-page.
- **Quando NÃO usar:**
  - Auditar o site `traderisk.com.br` ou suas páginas estratégicas (`/seguro-garantia`, `/seguro-credito` etc.) → use `seo-audit-traderisk`.
  - Auditoria técnica de domínio (sitemap, robots.txt, indexação, performance/Core Web Vitals em profundidade, arquitetura de links em escala) → escopo de SEO técnico, não on-page.
  - Pesquisa de palavras-chave/estratégia de conteúdo do zero → fase anterior à auditoria on-page.

## Core Pattern

Auditar a página seguindo o checklist abaixo, na ordem. Para cada item: **medir → comparar com a meta → registrar gap → propor correção**. Ao final, somar os pesos dos itens "OK" para o score e ordenar as correções por impacto.

1. **Title tag**
   - Existe, é único, 50–60 caracteres, contém a keyword-alvo perto do início.
   - Não duplica o H1 palavra por palavra; é atrativo para clique.

2. **Meta description**
   - Existe, 120–160 caracteres, descreve a página e inclui a keyword e um CTA.
   - Não está cortada nem genérica/duplicada.

3. **Headings (H1–H6)**
   - Exatamente **um H1**, contendo a keyword.
   - Hierarquia lógica (não pula de H1 para H3); subtítulos descrevem seções reais.

4. **Conteúdo / keywords**
   - Volume adequado ao tipo de página (geralmente 300+ palavras úteis).
   - Keyword-alvo e variações/semânticas presentes de forma natural (sem keyword stuffing).
   - Intenção de busca atendida; conteúdo original e escaneável (parágrafos curtos, listas).

5. **Imagens / alt text**
   - Toda imagem relevante tem `alt` descritivo (com keyword quando natural).
   - Nomes de arquivo descritivos; imagens comprimidas (peso razoável).

6. **Links internos**
   - Pelo menos alguns links internos contextuais para páginas relacionadas.
   - Âncoras descritivas (não "clique aqui"); sem links quebrados.

7. **Dados estruturados / schema**
   - Schema.org apropriado ao tipo (Article, Product, FAQPage, BreadcrumbList…).
   - Marcação válida (JSON-LD) e coerente com o conteúdo visível.

8. **Performance básica & mobile**
   - URL limpa e legível; canonical correto.
   - Página responsiva; sem peso excessivo óbvio que prejudique o carregamento.

Saída esperada: tabela de itens com status, **score total**, e lista de ações ordenadas por (peso × tamanho do gap).

## Quick Reference

| # | Item on-page | Meta / critério | Peso |
|---|---|---|---|
| 1 | Title tag | 50–60 chars, único, keyword no início | 15 |
| 2 | Meta description | 120–160 chars, keyword + CTA | 10 |
| 3 | H1 único + hierarquia | 1 H1 com keyword, H2–H6 lógicos | 15 |
| 4 | Conteúdo / keywords | Volume + intenção + uso natural da keyword | 25 |
| 5 | Imagens / alt | Alt descritivo, nomes e peso ok | 10 |
| 6 | Links internos | Links contextuais + âncoras descritivas | 10 |
| 7 | Schema / dados estruturados | JSON-LD válido e adequado ao tipo | 10 |
| 8 | Performance básica & mobile | URL limpa, canonical, responsivo | 5 |
|   | **Total** | | **100** |

Faixas de score: **80–100** boa (ajustes finos) · **60–79** mediana (gaps relevantes) · **40–59** fraca (priorizar correções) · **<40** crítica (refazer fundamentos).

## Common Mistakes

- **Confundir com auditoria do traderisk.com.br** → para o domínio próprio e páginas estratégicas use `seo-audit-traderisk`; esta skill é para páginas avulsas/externas.
- **Tratar como SEO técnico de domínio** → sitemap, robots, indexação e performance em profundidade estão fora do escopo on-page.
- **Keyword stuffing** → repetir a keyword artificialmente derruba a qualidade; priorize uso natural e variações semânticas.
- **Mais de um H1 ou hierarquia quebrada** → mantenha um único H1 e não pule níveis de heading.
- **Title = H1 idêntico** → o title deve ser otimizado para SERP/clique, não uma cópia do H1.
- **Alt text genérico ou ausente** → "imagem1.jpg" sem alt não ajuda acessibilidade nem SEO.
- **Score sem plano de ação** → o entregável útil é a lista priorizada de correções, não apenas o número.

---
<!-- Metadados estendidos ficam em skill.json (NÃO no frontmatter). -->
