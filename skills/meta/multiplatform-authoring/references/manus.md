# Manus (Local)

**Formato:** **remove** o frontmatter (Manus usa config própria).

## Instalar
1. Clone/aponte o repo:
```bash
git clone https://github.com/adrianotomasoni/skills.git ~/projects/skills
```
2. `manus.config.json` no projeto:
```json
{
  "skillsPath": "~/projects/skills/skills",
  "skillsRegistry": "~/projects/skills/registry.json",
  "autoLoadSkills": true,
  "categories": ["core", "frontend", "content", "engineering", "tools", "process", "meta"]
}
```

## Usar
```
@load-skill <id>
```
ou referencie a pasta da skill diretamente.

## Notas
- O exportador gera `dist/manus/<id>.md` sem frontmatter.
- Agentes: corpo do `AGENT.md` (sem frontmatter) no campo de instruções do agente.
