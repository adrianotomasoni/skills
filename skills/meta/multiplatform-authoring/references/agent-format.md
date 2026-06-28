# Formato Portável de Agente

Um **agente** orquestra um objetivo (pode usar várias skills). Fonte canônica:
`agents/<id>/` com `AGENT.md` + `agent.json` (+ `README.md`).

## AGENT.md
Frontmatter = superset do subagent do Claude Code:

```yaml
---
name: agent-id                # kebab-case, == pasta
description: "Quando acionar. Use SEMPRE que houver: [gatilhos]. Especialista em [domínio]."
tools: Read, Grep, Glob, Bash, WebSearch   # ferramentas permitidas
model: inherit                # inherit | sonnet | opus | haiku
---
```

Corpo: `## Identidade & Missão`, `## Quando me acione`, `## Como eu trabalho`
(referencie skills do repo pelo caminho), `## Skills vinculadas`, `## Formato de saída`.

## agent.json (sidecar)
Metadados de portabilidade:

```json
{
  "id": "agent-id",
  "linkedSkills": ["skill-a", "skill-b"],
  "platforms": {
    "claude-code": {"kind": "subagent", "path": "~/.claude/agents/<id>.md"},
    "openai":      {"kind": "assistant-or-custom-gpt"},
    "gemini":      {"kind": "system-instruction"},
    "cursor":      {"kind": "rules-or-mode"},
    "manus":       {"kind": "agent-config"}
  }
}
```

## Tradução por plataforma
| Plataforma | O que vira | `tools` → |
|---|---|---|
| Claude Code | subagent (`.md` com frontmatter) | campo `tools` |
| OpenAI | Assistant / Custom GPT (Instructions) | Functions / built-in tools |
| Gemini | system instruction | function calling |
| Cursor | rule/mode `.mdc` | ações do editor |
| Manus | agent config | tools do Manus |

**Agente x Skill:** skill = conhecimento/técnica reutilizável; agente = ator com
ferramentas e objetivo que *usa* skills. Quando possível, todo agente aponta para
uma ou mais skills via `linkedSkills`.
