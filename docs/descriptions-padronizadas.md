# Descriptions Padronizadas — Skills TradeRisk

Padrão aplicado (modelo da credit-risk-analysis, sua melhor skill):
**[O que faz] + "Use SEMPRE que houver: [gatilhos concretos]" + [fronteira/quando NÃO usar]**

Substitua APENAS a linha `description:` no frontmatter de cada SKILL.md.
O campo `name:` permanece inalterado em todas.

---

## 1. apresentacao-alto-impacto

### ANTES (descreve persona, sem gatilho)
> Você é um especialista sênior em apresentações corporativas de produtos, com nível de qualidade comparável a consultorias, times de branding premium, product marketing e sales enablement de alto padrão.

### DEPOIS
description: "Cria apresentações corporativas e de produto com acabamento premium (nível consultoria/branding), a partir de briefings, PDFs, decks existentes ou links. Use SEMPRE que houver: criar/montar/refazer uma apresentação, deck, pitch ou slides comerciais; transformar um material institucional em apresentação; pedidos como 'monta um deck de', 'cria uma apresentação de produto', 'preciso de slides para reunião/cliente/investidor'. Não usar para documentos de texto corrido (use docx) nem para slides de dados puramente analíticos sem narrativa comercial."

---

## 2. skill-traderisk-content-writer-seguro-de-credito-risco

### ANTES (lista temas, sem gatilho; nome longo)
> Você é a Traderisk Content Writer, uma skill especializada na produção de conteúdo técnico, estratégico e comercial para a Traderisk, com foco em: Seguro de Crédito Inadimplência B2B [...] inteligência de mercado

### DEPOIS
description: "Produz conteúdo técnico, estratégico e comercial da TradeRisk sobre Seguro de Crédito, inadimplência B2B, recuperação judicial, risco setorial, risco-país e proteção de recebíveis. Use SEMPRE que houver: escrever artigo, post, newsletter, e-mail comercial, material de blog ou texto institucional sobre esses temas; pedidos como 'escreve um artigo sobre', 'cria um conteúdo de', 'texto para o news.traderisk', 'post de LinkedIn sobre seguro de crédito/risco'. Não usar para propostas comerciais formais em .docx (essas seguem o fluxo de proposta de crédito) nem para análise de risco de um cliente específico (use credit-risk-analysis)."

---

## 3. code-review-estruturado-checklist

### ANTES (genérica, formato 'copie no ChatGPT')
> Realizar code reviews consistentes e construtivos usando um checklist estruturado — avaliando não só se o código funciona, mas se é legível, seguro, testável e manutenível — para elevar a qualidade do codebase e desenvolver a equipe.

### DEPOIS
description: "Revisa código com checklist estruturado (legibilidade, segurança, testabilidade, manutenibilidade), com feedback acionável e construtivo. Use SEMPRE que houver: revisar um PR ou trecho de código, pedir 'faz um code review', 'revisa esse código', 'esse código está bom?', avaliar qualidade antes de merge, ou padronizar o processo de review do time. Aplica-se ao stack TradeRisk (Python, Edge Functions Deno, React/TypeScript). Não usar para escrever código novo do zero nem para design de API (use design-de-api-restful-boas-praticas)."

---

## 4. design-de-api-restful-boas-praticas

### ANTES (genérica, formato 'copie no ChatGPT')
> Projetar uma API RESTful seguindo boas práticas de design — com nomenclatura consistente, versionamento, tratamento de erros padronizado, paginação e autenticação — para criar APIs que são fáceis de usar, manter e escalar.

### DEPOIS
description: "Projeta APIs RESTful com boas práticas: nomenclatura de recursos, versionamento, erros padronizados, paginação e autenticação. Use SEMPRE que houver: desenhar uma API ou endpoints novos, 'como estruturar essa API', 'qual o melhor endpoint para', padronizar uma API que cresceu sem design, ou documentar contrato de API para time/cliente. Aplica-se a Edge Functions Supabase e backends do ecossistema TradeRisk. Não usar para revisar implementação de código já escrito (use code-review-estruturado-checklist)."

---

## 5. auditoria-de-seo-on-page  (RESOLVE A DUPLICAÇÃO)

### ANTES (colide com seo-auditoria-traderisk)
> Fazer uma auditoria completa de SEO on-page de uma página específica — analisando título, meta description, headings, conteúdo, imagens, links internos e dados estruturados — com diagnóstico e recomendações práticas para melhorar o ranking no Google.

### DEPOIS (escopo diferenciado: página AVULSA/EXTERNA, não o site TradeRisk)
description: "Auditoria de SEO on-page de UMA página avulsa ou externa (qualquer site/cliente), analisando title, meta description, headings, conteúdo, imagens, links internos e schema, com score e plano de ação. Use quando houver: auditar uma página ou URL específica que NÃO seja do traderisk.com.br, checklist de SEO antes de publicar conteúdo novo, ou otimização pontual de uma página isolada. IMPORTANTE: para auditar o site traderisk.com.br e suas páginas estratégicas (/seguro-garantia, /seguro-credito etc.), use seo-auditoria-traderisk em vez desta."
