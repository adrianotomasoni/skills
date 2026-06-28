# Matriz de Plataformas — Skills & Agentes

Fonte canônica = este repo. Cada plataforma consome a mesma `SKILL.md`; só muda
**onde o arquivo fica** e se o **frontmatter** é mantido ou removido. O script
`scripts/export-adapters.py` automatiza a conversão para `dist/<plataforma>/`.

## Skills

| Plataforma | Caminho de instalação | Frontmatter | Como é ativada | Observações |
|---|---|---|---|---|
| **Claude.ai** | Upload em *Knowledge* (Project/Workspace) | mantém | Claude lê o `description` e carrega sob demanda | Web; pode também colar em Custom Instructions |
| **Claude Code** | `~/.claude/skills/<id>/` | mantém | ferramenta `Skill` | **NÃO** lê o alias `~/.agents/skills/` |
| **Codex** | `~/.codex/skills/<id>/` ou `~/.agents/skills/<id>/` | mantém | nativo | reconhece o alias cross-runtime |
| **Gemini CLI** | `~/.gemini/skills/<id>/` ou `~/.agents/skills/<id>/` | mantém | `activate_skill`; metadados carregados no início | mapa de ferramentas via `GEMINI.md` (precedência do alias) |
| **Copilot CLI** | `~/.copilot/skills/<id>/` ou `~/.agents/skills/<id>/` | mantém | ferramenta `skill` (auto-discovery de plugins) | reconhece o alias |
| **Cursor** | `.cursor/rules/<id>.mdc` | `.mdc` (frontmatter próprio) | regra do projeto / @-mention | converter para `.mdc`: `description` + `globs`/`alwaysApply` |
| **OpenAI (ChatGPT / Custom GPT / Assistants)** | campo *Instructions* ou arquivo em *Knowledge* | **remove** | colado como instrução / upload | strip do frontmatter → vira preâmbulo "Use esta skill quando: <description>" |
| **Manus** | config local do agente (`skillsPath`) | **remove** | `@load-skill <id>` ou referência direta | strip do frontmatter |

### Alias cross-runtime `~/.agents/skills/`
Codex, Copilot CLI e Gemini CLI reconhecem `~/.agents/skills/` como pasta comum.
Claude Code **não** — para ele use sempre `~/.claude/skills/`. Instalar uma vez em
`~/.agents/skills/` cobre os três; instale separadamente para Claude Code.

## Agentes

| Plataforma | Forma | Caminho/Local | Frontmatter |
|---|---|---|---|
| **Claude Code** | subagent | `~/.claude/agents/<id>.md` | mantém (`name`/`description`/`tools`/`model`) |
| **OpenAI** | Assistant ou Custom GPT | painel / API | remove → *Instructions*; `tools` → Functions |
| **Gemini** | system instruction + function calling | app/CLI | remove → system instruction |
| **Cursor** | rule/mode | `.cursor/rules/<id>.mdc` | converte p/ `.mdc` |
| **Manus** | agent config | config local | remove |

## Regra de ouro
Escreva **uma vez** no formato canônico. Nunca edite os arquivos em `dist/` à mão —
eles são gerados. Mudou a skill? Edite a fonte e rode `export-adapters.py`.
