# Comunicação Interna

> Categoria: `content` · Redige comunicação interna corporativa da TradeRisk.

## O que é

Skill para redigir comunicação interna da TradeRisk — anúncios, mudanças de processo, comunicados urgentes e mensagens para o time — de forma clara, objetiva e acionável. Aplica o princípio BLUF (mensagem principal primeiro), sempre com contexto + ação + prazo.

## Gatilhos (quando acionar)

- "Escreve um comunicado para o time sobre..."
- "Preciso anunciar [feature/mudança/novidade] internamente"
- "Comunica a mudança do processo de [X]"
- "Manda um comunicado urgente sobre [incidente]"

## Quando NÃO usar

- Conteúdo externo, marketing, blog ou social media → `skill-traderisk-content-writer`.
- Análise de risco de um cliente → `credit-risk-analysis`.

## Como usar por plataforma

- **Claude Code / Codex / Gemini / Copilot:** instale a pasta em `~/.claude/skills/internal-comms/` (ou `~/.agents/skills/...`).
- **Claude.ai:** faça upload de `SKILL.md` em Settings → Knowledge e descreva o comunicado.
- **Cursor:** referencie `@skills/content/internal-comms/SKILL.md` e cole o contexto da mensagem.

## Exemplo

Prompt: *"Comunica ao time comercial que o novo módulo de relatórios de exposição está no ar."*
Saída esperada: comunicado no formato de anúncio (assunto + BLUF + para quem + como acessar + ação + dúvidas), seguindo `templates/anuncio.md`.

## Material de apoio

- `SKILL.md` — método passo a passo, princípios e exemplos.
- `templates/anuncio.md` — anúncio/novidade.
- `templates/mudanca-de-processo.md` — mudança de processo ou política.
- `templates/comunicado-urgente.md` — comunicado urgente/incidente.

## Tags

`communication` `internal` `templates` `culture`
