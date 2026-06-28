# writing-plans

> Categoria: `process` · Formato canônico multiplataforma.

## O que é
Transforma uma spec/requisitos em um plano de implementação executável: tarefas em passos pequenos, caminhos de arquivo exatos, critérios de verificação e restrições globais. O plano é o que executing-plans e subagent-driven-development consomem depois.

## Quando dispara
- Você tem uma spec ou requisitos de uma tarefa multi-etapas.
- ANTES de tocar no código.
- Logo após brainstorming, quando o design já está fechado.

## Como usar
- **Claude Code / Codex / Cursor:** invoque a skill com a spec em mãos; ela produz o plano em `docs/superpowers/plans/`.
- **Gemini CLI / Copilot CLI:** ativada nativamente.
- **claude.ai / OpenAI / Manus:** cole `SKILL.md` e gere o plano seguindo o formato (tarefas numeradas, passos, verificação).

## Exemplo
Spec de "retry com backoff" → plano com Task 1 (config), Task 2 (função de retry), Task 3 (integração), cada uma com arquivos exatos e como verificar.

## Material de apoio
- [`plan-document-reviewer-prompt.md`](plan-document-reviewer-prompt.md) — prompt para revisar o plano antes de executá-lo.
- Conteúdo completo em [`SKILL.md`](SKILL.md); metadados em [`skill.json`](skill.json).
