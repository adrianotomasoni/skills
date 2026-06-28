# Template de Agente

Este diretório é o ponto de partida para criar um novo agente portável. Copie
`_template/` para `agents/<id-do-agente>/` e preencha os três arquivos.

## Formato

Cada agente vive em seu próprio diretório (`agents/<id>/`) e é composto por:

- **`AGENT.md`** — o agente em si. O frontmatter (YAML no topo) segue o
  **superset de subagentes do Claude Code**: os campos `name`, `description`,
  `tools` e `model` são lidos diretamente pelo Claude Code quando o arquivo é
  instalado como subagente (`~/.claude/agents/<id>.md`). O corpo em Markdown
  descreve identidade, gatilhos, protocolo de trabalho, skills vinculadas e
  formato de saída.
- **`agent.json`** — metadados de **portabilidade por plataforma**. Mantém o
  `id`, versão, status, maintainer, as `linkedSkills` (skills do repo que o
  agente usa) e o bloco `platforms`, que descreve como converter o `AGENT.md`
  para cada destino (Claude Code, OpenAI, Gemini, Cursor, Manus).
- **`README.md`** — explicação curta e específica do agente.

## Por que dois arquivos?

O `AGENT.md` é a fonte única do comportamento do agente e é compatível com o
Claude Code sem conversão. O `agent.json` carrega tudo que é específico de
plataforma ou de governança (versão, status, mapeamento de instalação), mantendo
o `AGENT.md` limpo e portável para outros runtimes.

## Convenções

- `id`/`name` do frontmatter em kebab-case.
- Conteúdo voltado a humanos em português.
- `linkedSkills` deve referenciar skills existentes em `skills/core/`.
