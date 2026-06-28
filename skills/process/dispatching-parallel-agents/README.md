# dispatching-parallel-agents

> Categoria: `process` · Formato canônico multiplataforma.

## O que é
Padrão para paralelizar trabalho: quando há 2+ tarefas genuinamente independentes (sem estado compartilhado nem dependência sequencial), você as despacha em subagents simultâneos em vez de fazê-las em série.

## Quando dispara
- "Investigue A, B e C" onde A/B/C não dependem um do outro.
- Refatorar vários módulos isolados, rodar buscas amplas em paralelo, gerar variações independentes.
- NÃO dispara quando as tarefas tocam os mesmos arquivos ou uma precisa do resultado da outra.

## Como usar
- **Claude Code:** múltiplas chamadas `Agent` numa mesma resposta.
- **Codex:** múltiplas `spawn_agent` + `wait_agent`. **Copilot CLI:** múltiplas `task`. **Gemini CLI:** múltiplas `invoke_agent`.
- **claude.ai / OpenAI / Manus / Cursor:** sem subagents nativos — execute sequencialmente ou avise que a capacidade não está disponível.

## Exemplo
"Levante o uso de `formatDate` em três pacotes diferentes" → três subagents read-only em paralelo, cada um varrendo um pacote, resultados consolidados no fim.

## Material de apoio
- Mapeamento de subagents por plataforma: `../using-superpowers/references/`.
- Conteúdo completo em [`SKILL.md`](SKILL.md); metadados em [`skill.json`](skill.json).
