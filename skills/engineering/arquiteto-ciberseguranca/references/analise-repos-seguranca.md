# Arquitetura de Cibersegurança para a Stack Lovable → Supabase → Vercel → Wasabi

Análise de repositórios open-source de alta adoção e como integrá-los.
Contagens de estrelas conforme levantamento de abril/2026 do AppSec Santa (64 ferramentas auditadas).

---

## Parte 1 — Por que a stack precisa disso

O risco dominante em projetos gerados por IA não é XSS nem dependência vulnerável.
É **autorização ausente no banco**.

Um levantamento de 1.645 projetos públicos do showcase do Lovable encontrou **170 (10,3%)
com Row Level Security inadequada**, expondo 303 endpoints. Vazaram nomes, e-mails,
telefones, endereços residenciais, dados de pagamento e chaves de API de terceiros.

A causa é estrutural: o Lovable gera apps que consultam o Postgres **direto do cliente**
com a chave pública, confiando apenas na RLS. Tabelas criadas via SQL bruto, migration ou
por um agente de IA **não recebem RLS automaticamente**. Sem policy, a chave pública — que
está no bundle, visível para qualquer um — puxa a tabela inteira.

Consequência prática: qualquer auditoria nesta stack começa no banco. Ferramenta de SAST
não enxerga esse problema.

---

## Parte 2 — Repositórios analisados

### Camada 1 — Autorização e banco (onde o risco realmente está)

| Repositório | Estrelas | Papel |
|---|---|---|
| `supabase/supabase` — advisors nativos | ~90k (projeto) | O lint de segurança do próprio Supabase detecta RLS ausente, policy sem índice e `search_path` mutável em funções `security definer`. Gratuito, já está no seu projeto, e a maioria dos usuários nunca abriu. |

**Integração:** MCP do Supabase → `get_advisors` com `type: "security"`. Ou Dashboard →
Advisors → Security. Rode antes de cada deploy. É o teste de maior retorno da lista inteira.

### Camada 2 — Segredos

| Repositório | Estrelas | Observação |
|---|---|---|
| `trufflesecurity/trufflehog` | ~24,5k | Diferencial: **verifica** a credencial contra o provedor. Reduz falso positivo drasticamente. |
| `gitleaks/gitleaks` | ~19k | Padrão de fato em CI. Ressalva: o autor original migrou para o Betterleaks e o projeto desacelerou — continua funcional e amplamente usado. |

**Integração:**
```bash
trufflehog git file://. --only-verified
docker run --rm -v "$PWD:/repo" zricethezav/gitleaks:latest detect --source /repo -v
```
Sempre com histórico completo (`fetch-depth: 0` no CI). Segredo apagado no último commit
continua no histórico do git.

**Armadilha específica desta stack:** `VITE_*` e `NEXT_PUBLIC_*` vão para o bundle. São
públicos por definição. Um `service_role` do Supabase com esse prefixo é comprometimento
total do banco — RLS não se aplica ao service_role.

### Camada 3 — SAST e dependências

| Repositório | Estrelas | Papel |
|---|---|---|
| `aquasecurity/trivy` | ~32,2k | Mais estrelado da categoria. Scanner único para deps, containers, IaC e segredos. |
| `projectdiscovery/nuclei` | ~26,9k | DAST por templates. Roda contra a URL já publicada na Vercel. |
| `semgrep/semgrep` | — (referência de SAST em 2026) | Regras que se parecem com o código-alvo. `p/react`, `p/typescript`, `p/owasp-top-ten`. |
| `google/osv-scanner` | — | Consulta a base OSV do Google. Menos ruído que `npm audit`. |
| `bridgecrewio/checkov` | — | IaC. Relevante se você versiona config de infra. |

**Integração:**
```bash
semgrep --config=auto --severity=ERROR .
osv-scanner scan source -r .
trivy fs --scanners vuln,secret,misconfig .
nuclei -u https://seu-app.vercel.app -severity critical,high
```

### Camada 4 — Revisão com IA no PR

| Repositório | Papel |
|---|---|
| `anthropics/claude-code-security-review` | GitHub Action oficial da Anthropic. Analisa o diff do PR com contexto semântico — pega falha de lógica de autorização que regra estática não pega. Comenta no PR. |
| `efij/awesome-claude-code-security` | Curadoria de hardening, threat research e governança para Claude Code. Bom ponto de partida para política interna de uso de agentes. |
| `VoltAgent/awesome-claude-code-subagents` | Subagentes por categoria, incluindo quality-security. Útil como referência de estrutura. |

**Integração:** ver `arquiteto-ciberseguranca/references/ci-pipeline.yml`, job `revisao-claude`.
Requer `ANTHROPIC_API_KEY` nos secrets do repo.

O comando `/security-review` já existe nativamente no Claude Code — se você quer só o
básico, comece por ele antes de montar Action.

---

## Parte 3 — Configuração por plataforma

### Vercel / Next.js

**CVE-2025-29927** (CVSS 9.1): o header `x-middleware-subrequest` permite pular **todo** o
middleware. Se sua autenticação está no middleware, isso é bypass completo de auth.
Afeta 11.1.4–12.3.4, 13.0.0–13.5.8, 14.0.0–14.2.24, 15.0.0–15.2.2.
Corrigido em 12.3.5 / 13.5.9 / 14.2.25 / 15.2.3. **Confirme sua versão hoje.**

Headers, via middleware (aplica em rotas e assets na borda):
`Content-Security-Policy`, `Strict-Transport-Security`, `X-Frame-Options`,
`X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`.

CSP: suba primeiro em `Content-Security-Policy-Report-Only`, colete violações, só então
aplique. Nonce por request. `unsafe-eval` é necessário em dev (HMR, React DevTools) e nunca
deve chegar em produção — use CSP condicionada ao ambiente.

Preview deployments são URLs públicas. Se apontam para o banco de produção, seu ambiente
de staging é uma porta aberta.

### Wasabi

Diferença crítica em relação à AWS: **Wasabi não suporta bloqueio central de acesso público**.
Não existe o equivalente ao "Block Public Access" que barra ACL e policy de uma vez, nem
garantia de que objetos novos não sejam expostos. Cada bucket precisa de auditoria individual,
por ACL **e** por policy.

- Sub-usuários: acesso API-only, sem console.
- Force HTTPS via policy (Deny quando `aws:SecureTransport = false`).
- Object Lock em **Compliance Mode**. Governance Mode pode ser desativado por quem tenha IAM
  suficiente — o que anula a proteção contra ransomware. A própria Wasabi recomenda evitar
  Governance salvo necessidade específica.
- Teste policies com a action `ValidatePolicy` antes de aplicar.

### GitHub

- Fixe actions por **SHA**, não por tag (tag é mutável — quem controla o repo da action
  controla seu CI).
- `permissions: read-all` no topo; eleve por job.
- Nunca `pull_request_target` com checkout do código do PR.
- Ligue Dependabot, secret scanning e **push protection** (bloqueia o segredo antes do push).

### Agentes de IA (Claude Code, Cursor, Codex, VS Code)

- Auditar `.mcp.json` e configs de MCP: um servidor MCP malicioso lê tudo que o agente lê.
- Prompt injection: conteúdo de issues, PRs e páginas web é entrada não confiável. Um agente
  com acesso a shell e a uma página hostil é um caminho de execução remota.
- Nunca dê ao agente uma credencial mais ampla do que a tarefa exige. `service_role` do
  Supabase no ambiente do agente é o erro mais comum.

---

## Parte 4 — Ordem de implantação

Nesta sequência. Cada passo pressupõe o anterior.

1. **Hoje** — `get_advisors` no Supabase + o teste de curl com ANON key. Se voltar dado de
   terceiro, pare tudo e corrija.
2. **Hoje** — `trufflehog --only-verified` no histórico. Achou? **Rotacione primeiro**,
   corrija o código depois.
3. **Esta semana** — versão do Next.js vs CVE-2025-29927.
4. **Esta semana** — pipeline de CI (`references/ci-pipeline.yml`), começando pelos jobs
   `segredos` e `rls-supabase`.
5. **Este mês** — `revisao-claude` no PR, headers/CSP na Vercel, auditoria dos buckets Wasabi.
6. **Contínuo** — skill `arquiteto-ciberseguranca` acionada antes de cada publicação.

---

## Fontes

- [64 Open Source AppSec Tools: Complete 2026 Guide — AppSec Santa](https://appsecsanta.com/open-source-tools)
- [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review)
- [Automated Security Reviews in Claude Code — Anthropic](https://support.claude.com/en/articles/11932705-automated-security-reviews-in-claude-code)
- [efij/awesome-claude-code-security](https://github.com/efij/awesome-claude-code-security)
- [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents)
- [Row Level Security — Supabase Docs](https://supabase.com/docs/guides/database/postgres/row-level-security)
- [Supabase RLS Best Practices — MakerKit](https://makerkit.dev/blog/tutorials/supabase-rls-best-practices)
- [Supabase RLS Security Checklist 2026 — Unico Connect](https://unicoconnect.com/blogs/supabase-rls-security-checklist)
- [Content Security Policy — Next.js Docs](https://nextjs.org/docs/pages/guides/content-security-policy)
- [Security Headers — Vercel Docs](https://vercel.com/docs/headers/security-headers)
- [Next.js Security Best Practices 2026 — Authgear](https://www.authgear.com/post/nextjs-security-best-practices/)
- [Vercel Deployment Security Checklist — CheckVibe](https://checkvibe.dev/blog/vercel-deployment-security-checklist)
- [Wasabi — Recommended General User Security Best Practices](https://docs.wasabi.com/docs/what-are-wasabis-recommended-general-user-security-best-practices)
- [Wasabi — Bucket Access Restriction Based on a Resource Policy](https://docs.wasabi.com/docs/how-do-i-restrict-bucket-access-with-resource-based-policies)
- [Security Scanning with GitHub Actions — OneUptime](https://oneuptime.com/blog/post/2026-01-25-security-scanning-github-actions/view)
