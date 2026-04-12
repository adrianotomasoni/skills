# Arquitetura e Filosofia – Skills Repository

## Visão Geral

Este repositório é o **sistema nervoso central** das capacidades de IA da TradeRisk. Ele centraliza todas as skills customizadas usadas em Claude, Cursor, Manus e outras plataformas.

## Estrutura de Diretórios

```
skills/                              # Raiz do repositório
├── README.md                        # Visão geral
├── registry.json                    # Índice master (auto-gerado)
├── LICENSE                          # MIT
├── .gitignore
│
├── skills/                          # Skills organizadas por categoria
│   ├── core/                        # Negócio core (alto valor, alta criticidade)
│   │   ├── judicial-monitoring/
│   │   ├── credit-risk-analysis/
│   │   ├── seo-audit-traderisk/
│   │   └── licitaradar/
│   │
│   ├── frontend/                    # Design e interfaces
│   │   ├── traderisk-frontend-design/
│   │   ├── apresentacao-alto-impacto/
│   │   └── frontend-design/
│   │
│   ├── content/                     # Conteúdo e copywriting
│   │   ├── skill-traderisk-content-writer/
│   │   └── internal-comms/
│   │
│   ├── engineering/                 # Código e arquitetura
│   │   ├── code-review-checklist/
│   │   ├── api-design-restful/
│   │   └── doc-coauthoring/
│   │
│   └── tools/                       # Ferramentas e automação
│       ├── file-reading/
│       ├── pdf-operations/
│       └── mcp-builder/
│
├── docs/                            # Documentação de suporte
│   ├── USAGE.md                     # Como usar as skills
│   ├── INTEGRATION.md               # Guia de integração por plataforma
│   ├── CONTRIBUTING.md              # Como contribuir
│   └── ARCHITECTURE.md              # Este arquivo
│
├── scripts/                         # Automação
│   ├── validate-skills.py
│   ├── generate-registry.py
│   ├── test-skills.py
│   ├── sync-all.sh
│   ├── sync-to-claude.sh
│   └── sync-to-cursor.sh
│
└── .github/
    └── workflows/
        ├── validate.yml             # CI de validação
        └── update-registry.yml     # CI de atualização do registry
```

## Anatomia de uma Skill

Cada skill é um diretório autocontido com:

```
skill-id/
├── SKILL.md        # OBRIGATÓRIO: definição completa da skill
├── README.md       # OBRIGATÓRIO: documentação para humanos
├── examples/       # Casos de uso e exemplos reais
├── tests/          # Suite de avaliação/evals
└── [assets]/       # Templates, prompts, código específico
```

### SKILL.md

O `SKILL.md` é o coração de cada skill. É o arquivo que é carregado nos modelos de IA. Deve conter:

1. **Identidade**: quem é o modelo quando usa esta skill
2. **Objetivo**: o que a skill faz
3. **Protocolo**: como o modelo deve agir
4. **Formato de saída**: estrutura esperada das respostas
5. **Limitações**: o que a skill não faz

## Versionamento Semântico

Cada skill segue **semver** (MAJOR.MINOR.PATCH):

| Tipo | Quando | Exemplo |
|------|--------|---------|
| PATCH | Correção de texto, typo, clareza | 1.0.0 → 1.0.1 |
| MINOR | Nova funcionalidade compatível | 1.0.0 → 1.1.0 |
| MAJOR | Mudança de comportamento, breaking change | 1.0.0 → 2.0.0 |

## Registry.json

O `registry.json` é o índice master de todas as skills. É gerado automaticamente por `scripts/generate-registry.py` e atualizado pelo CI a cada merge.

Estrutura de cada skill no registry:
```json
{
  "id": "skill-id",
  "category": "core",
  "name": "Nome Legível",
  "version": "1.0.0",
  "description": "O que faz em uma linha",
  "path": "skills/core/skill-id",
  "file": "SKILL.md",
  "status": "stable",
  "tags": ["tag1", "tag2"],
  "maintainer": "email@traderisk.com.br",
  "lastModified": "YYYY-MM-DD"
}
```

## Categorias

| Categoria | Descrição | Exemplos |
|-----------|-----------|---------|
| `core` | Skills de negócio estratégico | Análise judicial, crédito |
| `frontend` | Design e interfaces | Design system, apresentações |
| `content` | Conteúdo e comunicação | Copywriting, comunicação interna |
| `engineering` | Código e arquitetura | Code review, APIs |
| `tools` | Ferramentas e automação | PDF, MCP, arquivos |

## Ciclo de Vida de uma Skill

```
experimental → beta → stable → deprecated
```

- **experimental**: Testando hipótese, pode mudar radicalmente
- **beta**: Funciona, sendo refinado com uso real
- **stable**: Produção, mudanças controladas por semver
- **deprecated**: Será removida, use alternativa indicada

## Fluxo de Trabalho

```
1. main (produção)
       ↑
2. feature/skill-name (desenvolvimento)
       ↑
3. Editor local (Cursor/VS Code)
```

Nenhuma mudança vai direto para `main`. Sempre via PR.

## Sincronização entre Plataformas

```
GitHub (source of truth)
    ↓ git pull
Claude.ai → upload manual / knowledge base
Cursor → ~/.cursor/skills (git clone)
Manus → manus.config.json
```

## Filosofia

1. **GitHub é a fonte da verdade**: qualquer mudança começa aqui
2. **Skills são vivas**: evoluem com o uso e feedback
3. **Qualidade sobre quantidade**: melhor 5 skills excelentes que 50 mediocres
4. **Documentação é código**: README e SKILL.md são tão importantes quanto o código
