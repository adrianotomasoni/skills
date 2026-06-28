# Auditoria de SEO On-Page

> Categoria: `core` · Auditoria de SEO on-page de uma página avulsa ou externa.

## O que é

Skill que audita o SEO on-page de **uma única página** (própria, de cliente ou externa que NÃO seja `traderisk.com.br`) e devolve diagnóstico estruturado, **score 0–100** e **plano de ação priorizado**. Avalia title, meta description, headings, conteúdo/keywords, imagens/alt, links internos, dados estruturados (schema) e performance básica — cada item com peso fixo no score.

## Gatilhos (quando acionar)

- "Audita o SEO desta URL/página"
- "Checklist de SEO antes de publicar este conteúdo"
- "Por que esta página não ranqueia?"
- "Revisa esse rascunho quanto a SEO on-page"

## Quando NÃO usar

- Auditar `traderisk.com.br` ou suas páginas estratégicas → `seo-audit-traderisk`.
- SEO técnico de domínio (sitemap, robots, indexação, performance em profundidade) — fora do escopo on-page.
- Pesquisa de palavras-chave do zero — fase anterior à auditoria.

## Como usar por plataforma

- **Claude Code / Codex / Gemini / Copilot:** instale em `~/.claude/skills/auditoria-de-seo-on-page/`.
- **Claude.ai:** upload de `SKILL.md` e cole o HTML/conteúdo da página ou a URL.
- **Cursor:** `@skills/core/auditoria-de-seo-on-page/SKILL.md` + o conteúdo da página.

## Exemplo

Prompt: *"Audita o SEO on-page de exemplo.com.br/blog/post."*
Saída esperada: tabela de itens com status, score total (ex.: 57/100) e plano de ação ordenado por impacto. Ver `examples/auditoria-exemplo.md`.

## Material de apoio

- `SKILL.md` — checklist completo, tabela de pesos, faixas de score e erros comuns.
- `examples/auditoria-exemplo.md` — auditoria preenchida (genérica).

## Tags

`seo` `on-page` `audit` `checklist` `content`
