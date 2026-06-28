# Claude Code (CLI / IDE)

**Formato:** mantém o frontmatter (padrão agentskills.io).

## Instalar skills
Copie a pasta da skill para `~/.claude/skills/<id>/`:
```bash
cp -r skills/<categoria>/<id> ~/.claude/skills/<id>
```
Ou use o script de sync do repo (`scripts/sync-to-claude.sh`).

> **Importante:** Claude Code **não** lê o alias `~/.agents/skills/`. Use sempre
> `~/.claude/skills/`.

## Instalar agentes
Copie `agents/<id>/AGENT.md` para `~/.claude/agents/<id>.md`.

## Usar
- Skills: ferramenta `Skill` (ou invocação `/<id>` quando exposta como comando).
- Agentes: ferramenta `Agent` com `subagent_type: <id>`.

## Notas
- Mantenha `references/` ao lado do `SKILL.md`; os caminhos relativos continuam válidos.
