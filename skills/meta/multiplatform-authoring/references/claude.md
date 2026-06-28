# Claude.ai (Web / App)

**Formato:** mantém o frontmatter. Claude lê o `description` para decidir carregar.

## Instalar
- **Project/Workspace Knowledge:** Settings → Knowledge → Upload Files → suba o
  `SKILL.md` (e arquivos de apoio) da skill.
- **Custom Instructions:** cole o conteúdo do `SKILL.md` (com ou sem frontmatter)
  no campo de instruções.
- **Conectar repo (Team/Enterprise):** ligue este GitHub como Knowledge base.

## Usar
Basta descrever a tarefa; com um bom `description` Claude ativa a skill. Para
forçar: "use a skill <id>".

## Notas
- Suba também `references/` e `templates/` citados pela skill, senão os links quebram.
- Não precisa de adaptação de frontmatter.
