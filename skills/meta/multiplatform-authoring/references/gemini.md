# Google Gemini / Gemini CLI

**Formato:** mantém o frontmatter.

## Gemini CLI
Instale em `~/.gemini/skills/<id>/` ou no alias `~/.agents/skills/<id>/`
(o Gemini reconhece o alias; em conflito, o alias tem precedência).
```bash
cp -r skills/<categoria>/<id> ~/.agents/skills/<id>
```
- Ativação: ferramenta `activate_skill`. Os metadados são carregados no início da
  sessão; o conteúdo completo é ativado sob demanda.
- O mapa de ferramentas por runtime pode ser carregado automaticamente via `GEMINI.md`.

## Gemini (app / API)
- Use o corpo do `SKILL.md` como *system instruction*.
- `tools` de agentes → function calling.

## Notas
- Mantém o frontmatter; não precisa strip.
