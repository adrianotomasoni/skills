# Cursor

**Formato:** converte para Project Rule `.mdc` (frontmatter próprio do Cursor).

## Adaptação (feita por export-adapters.py)
Gera `dist/cursor/<id>.mdc`:
```mdc
---
description: <description da skill>
globs:
alwaysApply: false
---
<corpo do SKILL.md>
```
- `alwaysApply: true` para regras que devem sempre valer (ex.: a skill-regra `multiplatform-authoring`).
- `globs` para limitar a tipos de arquivo quando fizer sentido.

## Instalar
Copie os `.mdc` para `.cursor/rules/` do projeto:
```bash
cp dist/cursor/*.mdc <projeto>/.cursor/rules/
```
Ou clone o repo e aponte as rules para ele. Use `scripts/sync-to-cursor.sh`.

## Usar
- Auto-attached pelas `globs`, ou via @-mention: `@<id>`.
