# Arquiteto de Cibersegurança

## O que é

Skill de arquitetura de segurança de aplicações para projetos *vibe-coded* e full-stack,
com foco na stack **Lovable → Supabase → Vercel → Wasabi/S3**. Em vez de listar boas práticas
genéricas, encontra o caminho concreto pelo qual um atacante lê ou altera dados do projeto e
fecha esse caminho com o menor diff possível. Parte da premissa de que código gerado por IA
falha de forma previsível: a falha dominante não é XSS, é **autorização ausente na camada de
dados** — por isso a auditoria sempre começa pelo banco (RLS do Supabase), não pelo frontend.

## Gatilhos (quando dispara)

- Revisão de segurança de código; auditoria de projeto Lovable/Supabase/Vercel.
- Configuração de RLS, exposição de chaves/segredos, hardening de CI/CD no GitHub.
- Política de bucket Wasabi/S3, headers de segurança, CSP, checklist pré-deploy.
- Perguntas como "está seguro para publicar?", "alguém pode acessar meus dados?", ou antes de
  tornar um projeto público.
- Quando o usuário anexa código gerado por IA (Lovable, Claude Code, Codex, Cursor) e pede
  avaliação — mesmo sem dizer "segurança".

## Como usar por plataforma

- **Claude Code / Cursor:** rode sobre o repositório/projeto; a skill executa a ordem fixa
  (superfície de dados → segredos → SAST/deps → plataforma → storage) e entrega parecer com
  caminho de exploração e correção pronta (diff/SQL). Use o MCP do Supabase (`get_advisors`,
  `list_tables`) quando disponível.
- **Outros assistentes:** cole o código/config e referencie `SKILL.md` + os arquivos de
  `references/` para aplicar as policies e o pipeline de CI.

## Exemplo de uso

> "Anexei o código que o Lovable gerou. Está seguro para publicar?"

A skill começa pela superfície de dados (RLS em todas as tabelas do schema `public`, policies,
`service_role` fora do cliente), varre segredos com histórico completo, roda SAST/deps, valida
headers/CSP e política de bucket, e devolve um parecer priorizado pelos achados de autorização.

## Material de apoio

- [`SKILL.md`](SKILL.md) — ordem de execução, checagens críticas e regras do parecer.
- [`references/supabase-rls.md`](references/supabase-rls.md) — policies prontas por padrão de multi-tenancy.
- [`references/ci-pipeline.yml`](references/ci-pipeline.yml) — workflow GitHub Actions completo de segurança.
- [`references/analise-repos-seguranca.md`](references/analise-repos-seguranca.md) — análise dos repositórios open-source de AppSec e como integrá-los à stack.

## Tags

`seguranca`, `appsec`, `rls`, `supabase`, `lovable`, `vercel`, `wasabi`, `csp`, `secrets`,
`ci-cd`, `traderisk`
