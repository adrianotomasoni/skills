# GitHub Copilot CLI

**Formato:** mantém o frontmatter.

## Instalar
Instale em `~/.copilot/skills/<id>/` ou no alias `~/.agents/skills/<id>/`
(o Copilot CLI reconhece o alias).
```bash
cp -r skills/<categoria>/<id> ~/.agents/skills/<id>
```
- Skills são auto-descobertas a partir de plugins instalados.

## Usar
- Ferramenta `skill`.

## Notas
- Mantém frontmatter; sem strip.
- Para o Copilot no IDE (Chat), use os arquivos como contexto/instruções do repo.
