# Documentação Co-Autoria

## O que é

Skill para co-autorar e manter documentação técnica de alta qualidade nos
projetos TradeRisk: README, ADR (decisões de arquitetura), runbooks e guias.
Cobre definição de público, estrutura, rascunho, validação de exemplos, revisão
de clareza e manutenção.

## Gatilhos (quando dispara)

- Escrever ou estruturar documentação técnica.
- Criar ou atualizar um README.
- Redigir um guia técnico, runbook ou ADR.
- Documentar um processo de software.

Não dispara para conteúdo de marketing (use `skill-traderisk-content-writer`).

## Como usar por plataforma

- **Claude Code / Cursor:** abra o repositório e peça a doc; a skill estrutura,
  rascunha e valida exemplos/comandos no contexto do código.
- **Outros assistentes:** referencie `SKILL.md` e os exemplos como modelo.

## Exemplo de uso

> "Escreve um ADR sobre adotar Edge Functions para webhooks e um runbook de deploy."

A skill define o tipo e público, monta a estrutura, preenche com conteúdo
concreto e marca dados proprietários com `TODO:`.

## Material de apoio

- [`SKILL.md`](SKILL.md) — método passo a passo e templates inline (ADR e runbook).
- [`examples/adr-0001-exemplo.md`](examples/adr-0001-exemplo.md) — ADR completo de exemplo.
- [`examples/runbook-deploy-exemplo.md`](examples/runbook-deploy-exemplo.md) — runbook completo de exemplo.

## Tags

`documentation` `coauthoring` `technical-writing` `adr` `runbook`
