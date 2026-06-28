# 📖 USAGE — Guia Completo de Uso das Skills e Agentes

> **Repositório-mãe multiplataforma.** Cada skill funciona em Claude, Claude Code, OpenAI (ChatGPT/Custom GPTs/Assistants), Google Gemini/Gemini CLI, Cursor, GitHub Copilot, Codex e Manus. Este guia descreve **o que cada skill faz**, **quando ela dispara** e **como usá-la em cada plataforma**.

Fonte da verdade: este repositório. A regra que governa o formato é a skill [`multiplatform-authoring`](../skills/meta/multiplatform-authoring/SKILL.md).


**Inventário atual:** 33 skills · 2 agentes · 7 categorias.


## 🚀 Como usar (resumo por plataforma)


| Plataforma | Instalar | Ativar |
|---|---|---|
| **Claude.ai** | Settings → Knowledge → upload do `SKILL.md` (e apoio) | descreva a tarefa; ative com "use a skill `<id>`" |
| **Claude Code** | `./scripts/sync-to-claude.sh` → `~/.claude/skills/<id>/` | ferramenta `Skill` / comando `/<id>` |
| **Codex** | copie p/ `~/.codex/skills/` ou `~/.agents/skills/` | nativo |
| **Gemini CLI** | copie p/ `~/.gemini/skills/` ou `~/.agents/skills/` | `activate_skill` |
| **Copilot CLI** | copie p/ `~/.copilot/skills/` ou `~/.agents/skills/` | ferramenta `skill` |
| **Cursor** | `python scripts/export-adapters.py --platform cursor` → `.cursor/rules/` | auto/@-mention |
| **OpenAI** | `python scripts/export-adapters.py --platform openai` → cole em Instructions | preâmbulo automático |
| **Manus** | aponte `manus.config.json` p/ `skills/` | `@load-skill <id>` |

> Detalhes por plataforma em [`skills/meta/multiplatform-authoring/references/`](../skills/meta/multiplatform-authoring/references/) e em [MULTIPLATFORM.md](MULTIPLATFORM.md).


## 📚 Catálogo de Skills


### 📐 Meta — Governança do Repositório

#### `multiplatform-authoring`  ·  v1.0.0 · stable

Regra-mãe de autoria deste repositório: define o formato canônico portável de TODA skill e agente para funcionar em Claude, Claude Code, OpenAI/ChatGPT, Gemini, Cursor, Copilot, Codex e Manus. Use SEMPRE que houver: criar uma skill ou agente novo, editar/revisar um existente, padronizar descrição, decidir onde um arquivo vai em cada plataforma, ou validar o repositório. É obrigatória antes de adicionar qualquer skill/agente. Não usar para o conteúdo de domínio de uma skill específica (isso vive na própria skill).


<sub>tags: `governanca` `multiplataforma` `autoria` `padrao` `regra` `skills` `agentes` · [SKILL.md](../skills/meta/multiplatform-authoring/SKILL.md)</sub>


### 🎯 Core — Negócio (Seguro de Crédito / Garantia / Risco)

#### `auditoria-de-seo-on-page`  ·  v1.0.0 · stable

Auditoria de SEO on-page de UMA página avulsa ou externa (qualquer site/cliente), analisando title, meta description, headings, conteúdo, imagens, links internos e schema, com score e plano de ação. Use quando houver: auditar uma página ou URL específica que NÃO seja do traderisk.com.br, checklist de SEO antes de publicar conteúdo novo, ou otimização pontual de uma página isolada. IMPORTANTE: para auditar o site traderisk.com.br e suas páginas estratégicas (/seguro-garantia, /seguro-credito etc.), use seo-audit-traderisk em vez desta.


<sub>tags: `seo` `on-page` `auditoria` `conteudo` `checklist` · [SKILL.md](../skills/core/auditoria-de-seo-on-page/SKILL.md)</sub>

#### `credit-risk-analysis`  ·  v2.1.0 · stable

Avalia o risco de crédito comercial B2B de empresas, produzindo rating, score numérico e recomendação de limite/aceite. Use SEMPRE que houver: 'analisa essa empresa', avaliar o risco de um cliente ou CNPJ, decidir limite de exposição ou aceite/recusa de crédito ou garantia, gerar parecer de crédito. Não usar para produzir conteúdo ou marketing (use skill-traderisk-content-writer).


<sub>tags: `credito` `risco` `b2b` `rating` `score` `cnpj` `brasil` · [SKILL.md](../skills/core/credit-risk-analysis/SKILL.md)</sub>

#### `judicial-monitoring`  ·  v4.0.0 · stable

Detecta eventos judiciais relevantes para operações de seguro garantia e crédito, classifica por níveis de criticidade e calcula score de risco. Use SEMPRE que houver: analisar movimentação processual, classificar um evento judicial, calcular impacto/score de risco de um processo, perguntas como 'esse processo é risco?' ou 'o que essa movimentação significa pra apólice?'. Não usar para substituir parecer jurídico especializado (apenas sinaliza e prioriza); aplica-se ao Brasil (sistema CNJ).


<sub>tags: `judicial` `monitoramento` `seguro-garantia` `credito` `risco` `cnj` `brasil` · [SKILL.md](../skills/core/judicial-monitoring/SKILL.md)</sub>

#### `licitaradar`  ·  v1.0.0 · beta

Monitora e classifica licitações públicas brasileiras via API do PNCP, identificando exigências de seguro garantia e oportunidades alinhadas ao portfólio. Use SEMPRE que houver: encontrar, monitorar ou classificar editais e oportunidades de licitação, analisar exigências de garantia em um edital, alertar clientes sobre licitações relevantes. Não usar para análise de risco de crédito de um cliente (use credit-risk-analysis) nem para monitoramento de processos judiciais (use judicial-monitoring).


<sub>tags: `licitacao` `pncp` `editais` `seguro-garantia` `monitoramento` `brasil` · [SKILL.md](../skills/core/licitaradar/SKILL.md)</sub>

#### `localiza-credor-rj`  ·  v1.0.0 · stable

Inteligência de prospecção para Seguro de Crédito a partir de Recuperação Judicial e falência. Use SEMPRE que houver: mapear credores de empresas em RJ/falência, extrair lista de credores de edital ou quadro-geral, transformar processo de RJ em leads B2B, identificar empresas expostas a inadimplência de um devedor em crise, qualificar credor PJ como prospect de Seguro de Crédito, ou cruzar Radar RJ com base de prospecção. A RJ é um mapa de exposição comercial: o credor PJ exposto é o alvo, NÃO o devedor. Acionar mesmo quando o usuário só menciona um edital de RJ, quadro de credores, ou nome de empresa em recuperação.


<sub>tags: `seguro-credito` `recuperacao-judicial` `prospeccao` `leads-b2b` `radar-rj` `lgpd` · [SKILL.md](../skills/core/localiza-credor-rj/SKILL.md)</sub>

#### `seo-audit-traderisk`  ·  v1.2.0 · stable

Audita e otimiza o SEO do site traderisk.com.br e suas páginas estratégicas (ex.: /seguro-garantia, /seguro-credito), gerando relatório com score e recomendações. Use SEMPRE que houver: auditar, revisar ou otimizar o SEO do site da TradeRisk, suas landing pages, blog ou conteúdo institucional. IMPORTANTE: para uma página avulsa ou externa que NÃO seja traderisk.com.br, use auditoria-de-seo-on-page.


<sub>tags: `seo` `auditoria` `traderisk` `on-page` `conteudo` `b2b` · [SKILL.md](../skills/core/seo-audit-traderisk/SKILL.md)</sub>


### ✍️ Content — Conteúdo & Copywriting

#### `internal-comms`  ·  v1.0.0 · stable

Redige comunicação interna corporativa da TradeRisk — comunicados, anúncios, atualizações de processo e mensagens para o time — de forma clara, objetiva e alinhada à cultura. Use SEMPRE que houver: redigir comunicado interno, anúncio para o time, atualização de processo ou de feature para colaboradores. Não usar para conteúdo externo, marketing ou social media (use skill-traderisk-content-writer).


<sub>tags: `comunicacao-interna` `comunicado` `anuncio` `time` `corporativo` `traderisk` · [SKILL.md](../skills/content/internal-comms/SKILL.md)</sub>

#### `skill-traderisk-content-writer`  ·  v2.0.0 · stable

Produz conteúdo técnico, estratégico e comercial da TradeRisk sobre Seguro de Crédito, inadimplência B2B, recuperação judicial, risco setorial, risco-país e proteção de recebíveis. Use SEMPRE que houver: escrever artigo, post, newsletter, e-mail comercial, material de blog ou texto institucional sobre esses temas; pedidos como 'escreve um artigo sobre', 'cria um conteúdo de', 'texto para o news.traderisk', 'post de LinkedIn sobre seguro de crédito/risco'. Não usar para propostas comerciais formais em .docx (essas seguem o fluxo de proposta de crédito) nem para análise de risco de um cliente específico (use credit-risk-analysis).


<sub>tags: `conteudo` `redacao` `seguro-credito` `b2b` `blog` `linkedin` `email` `traderisk` · [SKILL.md](../skills/content/skill-traderisk-content-writer/SKILL.md)</sub>


### 🎨 Frontend — Design & UI

#### `apresentacao-alto-impacto`  ·  v1.0.0 · stable

Cria apresentações corporativas e de produto com acabamento premium (nível consultoria/branding), a partir de briefings, PDFs, decks existentes ou links. Use SEMPRE que houver: criar/montar/refazer uma apresentação, deck, pitch ou slides comerciais; transformar um material institucional em apresentação; pedidos como 'monta um deck de', 'cria uma apresentação de produto', 'preciso de slides para reunião/cliente/investidor'. Não usar para documentos de texto corrido (use docx) nem para slides de dados puramente analíticos sem narrativa comercial.


<sub>tags: `apresentacao` `deck` `pitch` `slides` `b2b` `branding` · [SKILL.md](../skills/frontend/apresentacao-alto-impacto/SKILL.md)</sub>

#### `frontend-design`  ·  v1.1.0 · stable

Aplica princípios de design de interface (layout, hierarquia, responsividade, performance, acessibilidade) para web/app em geral. Use SEMPRE que houver: melhorar a aparência ou UX de uma interface genérica, definir breakpoints/responsividade, revisar acessibilidade de uma UI fora do produto. Não usar para o produto TradeRisk (use traderisk-frontend-design).


<sub>tags: `frontend` `ui` `ux` `responsive` `accessibility` `performance` · [SKILL.md](../skills/frontend/frontend-design/SKILL.md)</sub>

#### `traderisk-frontend-design`  ·  v3.1.0 · stable

Define o design system e a UI do produto TradeRisk — cores, tipografia e padrões de componentes. Use SEMPRE que houver: criar/ajustar telas ou componentes do produto TradeRisk, aplicar o design system, padronizar visual de dashboards financeiros internos. Não usar para apresentações/decks (use apresentacao-alto-impacto).


<sub>tags: `design-system` `ui` `traderisk` `tailwind` `shadcn` `nextjs` · [SKILL.md](../skills/frontend/traderisk-frontend-design/SKILL.md)</sub>


### 🛠️ Engineering — Código & Arquitetura

#### `api-design-restful`  ·  v1.2.0 · stable

Projeta APIs RESTful com boas práticas: nomenclatura de recursos, versionamento, erros padronizados, paginação e autenticação. Use SEMPRE que houver: desenhar uma API ou endpoints novos, 'como estruturar essa API', 'qual o melhor endpoint para', padronizar uma API que cresceu sem design, ou documentar contrato de API para time/cliente. Aplica-se a Edge Functions Supabase e backends do ecossistema TradeRisk. Não usar para revisar implementação de código já escrito (use code-review-checklist).


<sub>tags: `api` `rest` `design` `supabase` `edge-functions` `http` · [SKILL.md](../skills/engineering/api-design-restful/SKILL.md)</sub>

#### `code-review-checklist`  ·  v1.3.0 · stable

Revisa código com checklist estruturado (legibilidade, segurança, testabilidade, manutenibilidade), com feedback acionável e construtivo. Use SEMPRE que houver: revisar um PR ou trecho de código, pedir 'faz um code review', 'revisa esse código', 'esse código está bom?', avaliar qualidade antes de merge, ou padronizar o processo de review do time. Aplica-se ao stack TradeRisk (Python, Edge Functions Deno, React/TypeScript). Não usar para escrever código novo do zero nem para design de API (use api-design-restful).


<sub>tags: `code-review` `quality` `security` `pull-request` `checklist` `traderisk` · [SKILL.md](../skills/engineering/code-review-checklist/SKILL.md)</sub>

#### `doc-coauthoring`  ·  v1.0.0 · stable

Coautoria de documentação técnica — estruturar, redigir e revisar docs como README, ADR, runbooks e guias. Use SEMPRE que houver: escrever ou estruturar documentação técnica, criar/atualizar README, redigir um guia técnico ou ADR, documentar um processo de software. Não usar para conteúdo de marketing (use skill-traderisk-content-writer).


<sub>tags: `documentation` `readme` `adr` `runbook` `technical-writing` · [SKILL.md](../skills/engineering/doc-coauthoring/SKILL.md)</sub>


### 🧰 Tools — Ferramentas & Automação

#### `file-reading`  ·  v1.0.0 · stable

Lê e extrai conteúdo estruturado de arquivos (PDF, Excel/CSV, Word, imagens), retornando dados em JSON. Use SEMPRE que houver: ler/extrair dados de um documento ou planilha, identificar campos-chave em formulários, extrair tabelas de arquivos, transformar um documento em dados estruturados. Não usar para manipulação avançada específica de PDF (use pdf-operations).


<sub>tags: `file` `extraction` `parsing` `pdf` `excel` `csv` · [SKILL.md](../skills/tools/file-reading/SKILL.md)</sub>

#### `mcp-builder`  ·  v1.0.0 · beta

Constrói, configura e integra servidores e ferramentas MCP (Model Context Protocol) para expandir as capacidades de modelos. Use SEMPRE que houver: criar um servidor MCP, expor ferramentas/dados via MCP, definir tools com inputSchema e handlers, integrar fontes externas (Supabase, APIs) a modelos via MCP. Não usar para desenho de API REST tradicional (use api-design-restful).


<sub>tags: `mcp` `model-context-protocol` `tools` `integration` `server` · [SKILL.md](../skills/tools/mcp-builder/SKILL.md)</sub>

#### `pdf-operations`  ·  v1.0.0 · stable

Extrai, analisa e estrutura informações de documentos PDF — texto, tabelas e cláusulas de contratos, editais e documentos financeiros. Use SEMPRE que houver: extrair texto/tabelas de um PDF, rodar OCR em PDF escaneado, identificar cláusulas/datas/valores em contratos, converter tabelas de PDF para JSON/CSV. Não usar para parsing genérico de outros formatos como Excel/CSV (use file-reading).


<sub>tags: `pdf` `ocr` `extraction` `tables` `contracts` `documents` · [SKILL.md](../skills/tools/pdf-operations/SKILL.md)</sub>


### 🔄 Process — Engenharia de Processo (estilo superpowers)

#### `brainstorming`  ·  v1.0.0 · stable

You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation.


<sub>tags: `brainstorming` `ideation` `requirements` `design` `discovery` · [SKILL.md](../skills/process/brainstorming/SKILL.md)</sub>

#### `dispatching-parallel-agents`  ·  v1.0.0 · stable

Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies


<sub>tags: `agents` `parallelism` `orchestration` `concurrency` · [SKILL.md](../skills/process/dispatching-parallel-agents/SKILL.md)</sub>

#### `executing-plans`  ·  v1.0.0 · stable

Use when you have a written implementation plan to execute in a separate session with review checkpoints


<sub>tags: `planning` `execution` `workflow` `checkpoints` · [SKILL.md](../skills/process/executing-plans/SKILL.md)</sub>

#### `finishing-a-development-branch`  ·  v1.0.0 · stable

Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup


<sub>tags: `git` `branching` `merge` `workflow` `completion` · [SKILL.md](../skills/process/finishing-a-development-branch/SKILL.md)</sub>

#### `frontend-design-process`  ·  v1.0.0 · stable

Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choices that don't read as templated defaults.


<sub>tags: `frontend` `design` `ui` `aesthetics` `process` · [SKILL.md](../skills/process/frontend-design-process/SKILL.md)</sub>

#### `receiving-code-review`  ·  v1.0.0 · stable

Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation


<sub>tags: `code-review` `feedback` `quality` `workflow` · [SKILL.md](../skills/process/receiving-code-review/SKILL.md)</sub>

#### `requesting-code-review`  ·  v1.0.0 · stable

Use when completing tasks, implementing major features, or before merging to verify work meets requirements


<sub>tags: `code-review` `quality` `workflow` `collaboration` · [SKILL.md](../skills/process/requesting-code-review/SKILL.md)</sub>

#### `subagent-driven-development`  ·  v1.0.0 · stable

Use when executing implementation plans with independent tasks in the current session


<sub>tags: `subagents` `orchestration` `workflow` `execution` · [SKILL.md](../skills/process/subagent-driven-development/SKILL.md)</sub>

#### `systematic-debugging`  ·  v1.0.0 · stable

Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes


<sub>tags: `debugging` `troubleshooting` `root-cause` `workflow` · [SKILL.md](../skills/process/systematic-debugging/SKILL.md)</sub>

#### `test-driven-development`  ·  v1.0.0 · stable

Use when implementing any feature or bugfix, before writing implementation code


<sub>tags: `tdd` `testing` `workflow` `red-green-refactor` · [SKILL.md](../skills/process/test-driven-development/SKILL.md)</sub>

#### `using-git-worktrees`  ·  v1.0.0 · stable

Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback


<sub>tags: `git` `worktrees` `isolation` `workflow` · [SKILL.md](../skills/process/using-git-worktrees/SKILL.md)</sub>

#### `using-superpowers`  ·  v1.0.0 · stable

Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions


<sub>tags: `skills` `discovery` `meta` `workflow` · [SKILL.md](../skills/process/using-superpowers/SKILL.md)</sub>

#### `verification-before-completion`  ·  v1.0.0 · stable

Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always


<sub>tags: `verification` `quality` `completion` `discipline` · [SKILL.md](../skills/process/verification-before-completion/SKILL.md)</sub>

#### `writing-plans`  ·  v1.0.0 · stable

Use when you have a spec or requirements for a multi-step task, before touching code


<sub>tags: `planning` `specs` `workflow` `design` · [SKILL.md](../skills/process/writing-plans/SKILL.md)</sub>

#### `writing-skills`  ·  v1.0.0 · stable

Use when creating new skills, editing existing skills, or verifying skills work before deployment


<sub>tags: `skills` `authoring` `documentation` `meta` `process` · [SKILL.md](../skills/process/writing-skills/SKILL.md)</sub>


## 🤖 Catálogo de Agentes

Agentes orquestram objetivos usando uma ou mais skills. Formato portável: `AGENT.md` + `agent.json`. Ver [agent-format](../skills/meta/multiplatform-authoring/references/agent-format.md).


#### `credit-risk-analyst`  ·  v1.0.0 · stable

Aciona quando é preciso avaliar o risco de crédito comercial de uma empresa e recomendar limite/aceite. Use SEMPRE que houver: 'analisa o risco dessa empresa', avaliar limite ou aceite de crédito B2B, decidir exposição a um cliente/CNPJ, gerar parecer de crédito. Especialista em risco de crédito comercial.


<sub>skills vinculadas: `credit-risk-analysis` · tools: `Read, Grep, Glob, Bash, WebSearch` · [AGENT.md](../agents/credit-risk-analyst/AGENT.md)</sub>


#### `judicial-watcher`  ·  v1.0.0 · stable

Monitora movimentações judiciais e classifica eventos de risco para operações de seguro garantia e crédito. Use SEMPRE que houver: acompanhar processos, classificar uma movimentação processual, alertar sobre evento de risco, perguntas como 'esse processo é risco?' ou 'o que essa movimentação significa pra apólice?'. Especialista em monitoramento judicial para seguro garantia/crédito.


<sub>skills vinculadas: `judicial-monitoring` · tools: `Read, Grep, Glob, Bash, WebSearch` · [AGENT.md](../agents/judicial-watcher/AGENT.md)</sub>


## 🔄 Manter sincronizado


1. Edite a fonte canônica (`skills/<categoria>/<id>/`).
2. `python3 scripts/validate-skills.py --strict` e `python3 scripts/validate-agents.py`.
3. `python3 scripts/generate-registry.py` (atualiza `registry.json`).
4. `python3 scripts/export-adapters.py` (gera `dist/<plataforma>/`).
5. Commit + PR. O CI valida automaticamente.


---
*Catálogo gerado a partir de `registry.json`. Regenerar: ver `scripts/`.*
