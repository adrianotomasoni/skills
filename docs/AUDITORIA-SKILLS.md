# Auditoria Completa de Skills e Agentes

> Análise estruturada do repositório `adrianotomasoni/skills`.
> Gerada em 2026-07-20. Escopo: todas as skills e agentes versionados no repo.

## 1. Resumo executivo

| Métrica | Valor |
|---|---|
| Skills | **34** (era 33; +1 nesta entrega) |
| Agentes | **3** |
| Categorias | 7 (`core`, `engineering`, `frontend`, `content`, `tools`, `process`, `meta`) |
| Skills válidas (`validate-skills.py`) | 34 / 34 ✅ |
| Agentes válidos (`validate-agents.py`) | 3 / 3 ✅ |
| Links relativos (`check-links.py`) | 174 alvos, 0 quebrados ✅ |
| Cobertura de testes (`test-skills.py`) | 1 com validação estrutural, 33 sem `eval-suite.json` ⚠️ |

Estado geral: **saudável**. Todas as skills e agentes seguem o contrato canônico
(`SKILL.md` + `README.md` + `skill.json`; frontmatter só com `name` + `description`, ≤ 1024 chars;
`skill.json` com categoria/status/tipo/plataformas válidos). A única não-conformidade material era
uma skill ausente por falha de migração — recuperada nesta entrega (§5).

## 2. Inventário por categoria

Cada skill possui os 3 arquivos obrigatórios (`SKILL.md`, `README.md`, `skill.json`) salvo indicação.

### core (6) — domínio de negócio TradeRisk

| Skill | Status | Função |
|---|---|---|
| `auditoria-de-seo-on-page` | stable | Auditoria de SEO on-page de uma página avulsa (qualquer site), com diagnóstico e recomendações. |
| `credit-risk-analysis` | stable | Avalia risco de crédito comercial B2B: rating, score numérico e recomendação de limite. |
| `judicial-monitoring` | stable | Detecta e classifica eventos judiciais relevantes para seguro garantia e crédito. |
| `licitaradar` | beta | Monitora e classifica licitações públicas (API PNCP), identificando exigências de garantia. |
| `localiza-credor-rj` | stable | Prospecção de Seguro de Crédito a partir de credores em Recuperação Judicial/falência. |
| `seo-audit-traderisk` | stable | Audita e otimiza o SEO do site traderisk.com.br e páginas estratégicas. |

### engineering (4) — engenharia de software

| Skill | Status | Função |
|---|---|---|
| `api-design-restful` | stable | Projeta APIs RESTful com boas práticas (nomenclatura, versionamento, erros, paginação, auth). |
| `arquiteto-ciberseguranca` | stable | **[NOVO]** Arquiteto de segurança para stack Lovable→Supabase→Vercel→Wasabi; começa pela RLS. |
| `code-review-checklist` | stable | Code review estruturado (legibilidade, segurança, testabilidade, manutenibilidade). |
| `doc-coauthoring` | stable | Coautoria de documentação técnica (README, ADR, specs) em fluxo iterativo. |

### frontend (3)

| Skill | Status | Função |
|---|---|---|
| `apresentacao-alto-impacto` | stable | Apresentações corporativas/de produto com acabamento premium. |
| `frontend-design` | stable | Princípios de design de interface (layout, hierarquia, responsividade, performance, a11y). |
| `traderisk-frontend-design` | stable | Design system e UI dos produtos TradeRisk (cores, tipografia, componentes). |

### content (2)

| Skill | Status | Função |
|---|---|---|
| `internal-comms` | stable | Comunicação interna corporativa da TradeRisk (comunicados, atualizações, FAQs). |
| `skill-traderisk-content-writer` | stable | Conteúdo técnico/comercial sobre Seguro de Crédito, inadimplência e risco. |

### tools (3)

| Skill | Status | Função |
|---|---|---|
| `file-reading` | stable | Lê e extrai conteúdo estruturado de arquivos (PDF, Excel/CSV, Word, imagens). |
| `mcp-builder` | beta | Constrói e integra servidores/ferramentas MCP (Model Context Protocol). |
| `pdf-operations` | stable | Extrai e estrutura informações de PDFs (texto, tabelas, cláusulas). |

### process (15) — metodologia de desenvolvimento (base "superpowers")

| Skill | Status | Função |
|---|---|---|
| `brainstorming` | stable | Exploração estruturada antes de qualquer trabalho criativo. |
| `dispatching-parallel-agents` | stable | Paraleliza 2+ tarefas independentes sem estado compartilhado. |
| `executing-plans` | stable | Executa um plano de implementação escrito, com revisão. |
| `finishing-a-development-branch` | stable | Decide como integrar uma branch após implementação completa. |
| `frontend-design-process` | stable | Processo de design visual distinto ao construir/reformular UI. |
| `receiving-code-review` | stable | Como agir sobre feedback de code review antes de implementar. |
| `requesting-code-review` | stable | Verifica o trabalho antes de pedir review/merge. |
| `subagent-driven-development` | stable | Executa planos com tarefas independentes via subagentes. |
| `systematic-debugging` | stable | Investigação sistemática de bugs antes de propor correções. |
| `test-driven-development` | stable | TDD antes de escrever código de implementação. |
| `using-git-worktrees` | stable | Isolamento de workspace com git worktrees. |
| `using-superpowers` | stable | Estabelece como localizar e usar skills no início da conversa. |
| `verification-before-completion` | stable | Verificação antes de declarar trabalho concluído. |
| `writing-plans` | stable | Escreve plano para tarefa multi-etapas antes de tocar no código. |
| `writing-skills` | stable | Cria/edita/verifica skills antes do deploy. |

### meta (1)

| Skill | Status | Função |
|---|---|---|
| `multiplatform-authoring` | stable | Regra-mãe: define o formato canônico portável de toda skill/agente do repo. |

## 3. Agentes (3)

| Agente | Função | Validade |
|---|---|---|
| `buscador-sgj` | Caça oportunidades comerciais de seguro garantia judicial (trabalhista, fiscal, cível). | ✅ |
| `credit-risk-analyst` | Avalia risco de crédito comercial e recomenda limites. | ✅ |
| `judicial-watcher` | Monitora movimentações judiciais e classifica eventos de risco. | ✅ |

## 4. Resultado dos validadores

```
validate-skills.py  → 🔍 34 skill(s)  → ✅ All skills valid!
validate-agents.py  → 🔍 3 agent(s)   → ✅ All agents valid!
check-links.py      → 🔗 174 alvos    → ✅ Nenhum link quebrado.
test-skills.py      → 🧪 34 skill(s)  → 1 passed, 0 failed, 33 skipped (sem eval-suite.json)
generate-registry.py→ ✅ registry.json: 34 skills, 3 agents
```

## 5. Lacunas, falhas de migração e bugs sinalizados

### 5.1 [RECUPERADO] Skill ausente por falha de migração — `arquiteto-ciberseguranca`

A skill existia como **skill global do Claude** do usuário, mas **nunca havia sido migrada para o
repositório** — não aparecia em nenhuma categoria nem no `registry.json`. Era a lacuna central do
pedido ("evidências de erros de migração pro repositório").

**Recomposição feita nesta entrega**, a partir do material-fonte (`ARQUIT1.zip`):
- `skills/engineering/arquiteto-ciberseguranca/SKILL.md` (fonte original, íntegro).
- `references/ci-pipeline.yml`, `references/supabase-rls.md` (fonte original).
- `references/analise-repos-seguranca.md` (pesquisa de repos AppSec anexa, preservada como apoio).
- `README.md` e `skill.json` criados no padrão canônico (antes inexistentes).
- `registry.json` regenerado (33 → 34 skills). Validação: **all valid**.

Categoria escolhida: `engineering` — é a única categoria válida (`VALID_CATEGORIES` em
`scripts/_common.py`) que cobre segurança/revisão de código; não existe categoria "security".

### 5.2 [CORRIGIDO ✅] Cobertura de testes — 33/34 skills sem `eval-suite.json`

`test-skills.py` só fazia validação estrutural de `core/judicial-monitoring` (única com
`eval-suite.json`). As demais eram puladas — não é bug, é ausência de asset de teste, mas impedia
detectar regressão de comportamento.

**Correção aplicada:** adicionados `tests/eval-suite.json` para as duas outras skills de maior
risco de negócio apontadas na recomendação §6.1: `core/credit-risk-analysis` (4 casos cobrindo
ratings A/C/E/F) e `engineering/arquiteto-ciberseguranca` (4 casos cobrindo RLS ausente, segredo
`service_role` vazado, bucket público e o caso "sem achado crítico"). `test-skills.py` agora passa
estruturalmente em 3/34 skills. As 31 restantes continuam sem asset de teste — ver §6.

### 5.4 [CORRIGIDO ✅] `check-links.py` não validava referências a `.yml`/`.yaml`

O regex de menções em crase (`BACKTICK_PATH`) só cobria `md|ts|js|json|py|sh|mdc|txt` — uma
referência quebrada a `references/ci-pipeline.yml` (citado em `SKILL.md`/`README.md` da skill
`arquiteto-ciberseguranca`) passaria despercebida pelo CI. Corrigido em `scripts/check-links.py`
adicionando `yml`/`yaml` às extensões verificadas (174 → 182 alvos verificados). Isso é o que
garante, na prática, que o `references/ci-pipeline.yml` da skill se mantenha corretamente linkado
e detectável se for movido/apagado — ver recomendação §6.2.

### 5.3 [CORRIGIDO ✅] Divergência de nomenclatura entre skills globais e do repo

Ao migrar as skills globais para o repo, alguns nomes foram normalizados. **Não era erro** — mas
faltava registro durável do mapeamento. **Correção aplicada:** criado
[`docs/MAPEAMENTO-NOMENCLATURA.md`](MAPEAMENTO-NOMENCLATURA.md) e referenciado no passo 0 de
`docs/CONTRIBUTING.md`, para que uma nova migração confira a tabela antes de criar uma pasta
nova (evita duplicar skill com nome diferente).

| Skill global (Claude) | Skill no repositório |
|---|---|
| `code-review-estruturado-checklist` | `engineering/code-review-checklist` |
| `design-de-api-restful-boas-praticas` | `engineering/api-design-restful` |
| `seo-auditoria-traderisk` / `seo-traderisk` | `core/seo-audit-traderisk` |
| `skill-traderisk-content-writer-seguro-de-credito-risco` | `content/skill-traderisk-content-writer` |

As demais skills autorais globais (`apresentacao-alto-impacto`, `auditoria-de-seo-on-page`,
`credit-risk-analysis`, `localiza-credor-rj`, `traderisk-frontend-design`, `doc-coauthoring`,
`mcp-builder`) já possuem correspondente 1:1 no repo. Nenhuma outra ausência foi detectada.

## 6. Recomendações priorizadas — status

1. ✅ **`eval-suite.json` adicionado** às skills de maior risco de negócio
   (`credit-risk-analysis`, `judicial-monitoring` já tinha, `arquiteto-ciberseguranca`), no molde
   estrutural (`id` + `input` + campos de expectativa por domínio). `test-skills.py` passa
   estruturalmente em 3/34 skills. Inferência real contra a API (`--api-key`) ainda não está
   implementada no runner (`TODO` já existente em `scripts/test-skills.py`) — pendente, fora do
   escopo desta correção.
2. ✅ **`arquiteto-ciberseguranca` mantida íntegra e verificável no CI** — o
   `references/ci-pipeline.yml` continua sendo um *template* para ser copiado no projeto-alvo
   (Lovable/Supabase/Vercel), não algo que rode neste repo-registro de skills (que não tem projeto
   Supabase próprio). O que passou a rodar no CI **deste repo** é a garantia de que o link para
   `ci-pipeline.yml` nunca fica quebrado silenciosamente — corrigido o gap do validador (§5.4).
3. ✅ **Mapeamento de nomenclatura registrado** em `docs/MAPEAMENTO-NOMENCLATURA.md` e linkado no
   fluxo de contribuição (§5.3).

### Pendente (fora do escopo desta rodada, para priorizar depois)

- Estender `eval-suite.json` às 31 skills restantes (maior esforço; comece pelas de `core`).
- Implementar a chamada real à API Anthropic em `scripts/test-skills.py` (hoje só valida estrutura).
