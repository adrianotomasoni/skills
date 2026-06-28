# TradeRisk Content Writer

> Categoria: `content` · Redação de conteúdo com o tom e a voz oficiais da TradeRisk.

## O que é

Skill que produz conteúdo técnico, estratégico e comercial da TradeRisk sobre seguro de crédito, inadimplência B2B, recuperação judicial, risco setorial, risco-país e proteção de recebíveis. Adapta estrutura e tom por canal (blog/SEO, LinkedIn, newsletter, e-mail comercial, institucional) seguindo o vocabulário aprovado.

## Gatilhos (quando acionar)

- "Escreve um artigo sobre [tema de risco/crédito]"
- "Cria um post de LinkedIn sobre seguro garantia"
- "Texto para o news.traderisk" / "monta a newsletter"
- "Faz um e-mail comercial sobre proteção de recebíveis"

## Quando NÃO usar

- Proposta comercial formal em .docx (fluxo de proposta de crédito).
- Análise de risco de um cliente específico → `credit-risk-analysis`.
- Comunicação interna para o time → `internal-comms`.
- Auditoria de SEO de uma página → `seo-audit-traderisk` / `auditoria-de-seo-on-page`.

## Como usar por plataforma

- **Claude Code / Codex / Gemini / Copilot:** instale em `~/.claude/skills/skill-traderisk-content-writer/`.
- **Claude.ai:** upload de `SKILL.md` + `tone-voice.md` em Settings → Knowledge.
- **Cursor:** `@skills/content/skill-traderisk-content-writer/SKILL.md` + o briefing do conteúdo.

## Exemplo

Prompt: *"Escreve um post de LinkedIn sobre por que vender a prazo no feeling é arriscado."*
Saída esperada: post com gancho na 1ª linha, 3–5 parágrafos curtos, CTA único e hashtags, conforme `templates/post-linkedin.md` e o tom de `tone-voice.md`.

## Material de apoio

- `SKILL.md` — método, públicos-alvo, padrões por canal, exemplos.
- `tone-voice.md` — vocabulário aprovado, princípios e exemplos de escrita.
- `templates/artigo-blog.md` · `templates/post-linkedin.md` · `templates/newsletter.md`.

> Regra de dados: nunca inventar números, benchmarks ou casos. Sem dado real, marcar `TODO: preencher com <dado proprietário> da TradeRisk`.

## Tags

`content` `copywriting` `traderisk` `tone-of-voice` `seo`
