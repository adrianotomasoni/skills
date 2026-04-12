# TradeRisk Skills Repository

Um repositório centralizado para todas as skills customizadas da TradeRisk, organizadas para uso em Claude, Cursor, Manus e outras plataformas de IA.

## 📁 Estrutura do Repositório

```
skills/
├── README.md
├── .gitignore
├── registry.json                          # Índice master de todas as skills
├── LICENSE
│
├── skills/
│   ├── core/                              # Skills estratégicas de core business
│   │   ├── judicial-monitoring/
│   │   │   ├── SKILL.md
│   │   │   ├── README.md
│   │   │   ├── prompts/
│   │   │   │   ├── fase-1-v4-unified.md
│   │   │   │   ├── fase-1-v3-spec.md
│   │   │   │   └── melhorias-motor-judicial-2026.md
│   │   │   ├── examples/
│   │   │   │   └── case-studies.json
│   │   │   └── tests/
│   │   │       └── eval-suite.json
│   │   │
│   │   ├── credit-risk-analysis/
│   │   │   ├── SKILL.md
│   │   │   ├── README.md
│   │   │   ├── templates/
│   │   │   │   ├── credit-assessment.md
│   │   │   │   └── score-calculator.js
│   │   │   └── examples/
│   │   │       └── case-studies.json
│   │   │
│   │   ├── seo-audit-traderisk/
│   │   │   ├── SKILL.md
│   │   │   ├── README.md
│   │   │   ├── templates/
│   │   │   └── benchmarks.json
│   │   │
│   │   └── licitaradar/
│   │       ├── SKILL.md
│   │       ├── README.md
│   │       ├── api-integration/
│   │       │   ├── pncp-client.ts
│   │       │   └── claude-classifier.ts
│   │       └── examples/
│   │
│   ├── frontend/                           # Skills de design/frontend
│   │   ├── traderisk-frontend-design/
│   │   │   ├── SKILL.md
│   │   │   ├── README.md
│   │   │   ├── design-system/
│   │   │   │   ├── colors.ts
│   │   │   │   ├── typography.ts
│   │   │   │   ├── components/
│   │   │   │   └── patterns.md
│   │   │   └── templates/
│   │   │
│   │   ├── apresentacao-alto-impacto/
│   │   │   ├── SKILL.md
│   │   │   ├── README.md
│   │   │   └── templates/
│   │   │
│   │   └── frontend-design/
│   │       ├── SKILL.md
│   │       ├── README.md
│   │       └── design-patterns/
│   │
│   ├── content/                            # Skills de conteúdo/copywriting
│   │   ├── skill-traderisk-content-writer/
│   │   │   ├── SKILL.md
│   │   │   ├── README.md
│   │   │   ├── tone-voice.md
│   │   │   ├── templates/
│   │   │   └── examples/
│   │   │
│   │   └── internal-comms/
│   │       ├── SKILL.md
│   │       ├── README.md
│   │       └── templates/
│   │
│   ├── engineering/                       # Skills técnicas/code
│   │   ├── code-review-checklist/
│   │   │   ├── SKILL.md
│   │   │   ├── README.md
│   │   │   ├── checklists/
│   │   │   │   ├── react.md
│   │   │   │   ├── typescript.md
│   │   │   │   └── supabase.md
│   │   │   └── examples/
│   │   │
│   │   ├── api-design-restful/
│   │   │   ├── SKILL.md
│   │   │   ├── README.md
│   │   │   ├── standards/
│   │   │   └── templates/
│   │   │
│   │   └── doc-coauthoring/
│   │       ├── SKILL.md
│   │       ├── README.md
│   │       └── workflows/
│   │
│   └── tools/                              # Skills de ferramentas/automação
│       ├── file-reading/
│       ├── pdf-operations/
│       └── mcp-builder/
│
├── docs/
│   ├── USAGE.md                            # Como usar as skills
│   ├── INTEGRATION.md                      # Integração em diferentes plataformas
│   ├── CONTRIBUTING.md                     # Como contribuir
│   └── ARCHITECTURE.md                     # Arquitetura e filosofia
│
├── scripts/
│   ├── validate-skills.py                  # Validar todas as skills
│   ├── generate-registry.py                # Gerar registry.json
│   ├── sync-to-claude.sh                   # Script de sincronização
│   └── test-skills.py                      # Testar skills
│
└── .github/
    └── workflows/
        ├── validate.yml                    # CI para validação
        └── update-registry.yml             # CI para atualizar registry
```

## 🚀 Como Usar Este Repositório

### 1. **Em Claude (claude.ai)**
```
1. Vá em Settings → Knowledge → Upload Files
2. Faça upload de /skills/{categoria}/{skill}/SKILL.md
3. Refira-se à skill pelo nome: @skill-name
```

### 2. **Em Cursor**
```
1. Clone o repositório:
   git clone https://github.com/adrianotomasoni/skills.git ~/.cursor/skills

2. Configure no .cursor/rules.md:
   {projeto} deve usar skills do repositório em ~/.cursor/skills

3. Referencie na conversa: @skills/judicial-monitoring
```

### 3. **Em Manus (Local)**
```
1. Configure o caminho no manus.config.json:
   {
     "skillsPath": "~/projects/skills/skills"
   }

2. Use: @skill-judicial-monitoring
```

### 4. **No GitHub (Source of Truth)**
```
git clone https://github.com/adrianotomasoni/skills.git
cd skills
git checkout -b feature/improve-credit-risk
# edite skills
git commit -am "Improve credit risk skill"
git push origin feature/improve-credit-risk
# crie PR
```

## 📋 Registry.json (Índice Master)

O arquivo `registry.json` funciona como um índice que lista TODAS as skills:

```json
{
  "version": "1.0.0",
  "lastUpdated": "2026-04-12T10:00:00Z",
  "skills": [
    {
      "id": "judicial-monitoring",
      "category": "core",
      "name": "Monitoramento Judicial Proativo",
      "version": "4.0.0",
      "description": "Detecção de eventos e oportunidades em processos judiciais",
      "path": "skills/core/judicial-monitoring",
      "file": "SKILL.md",
      "status": "stable",
      "tags": ["judicial", "monitoring", "eventos", "v4"],
      "dependencies": ["credit-risk-analysis"],
      "maintainer": "adriano@traderisk.com.br",
      "lastModified": "2026-04-12"
    },
    {
      "id": "credit-risk-analysis",
      "category": "core",
      "name": "Análise de Risco de Crédito",
      "version": "2.1.0",
      "path": "skills/core/credit-risk-analysis",
      "file": "SKILL.md",
      "status": "stable",
      "tags": ["credit", "risk", "analysis"],
      "maintainer": "adriano@traderisk.com.br"
    }
    // ... mais skills
  ]
}
```

## 🔄 Fluxo de Versionamento

Cada skill segue **semantic versioning** (MAJOR.MINOR.PATCH):

- **MAJOR**: Mudanças quebra-compatibilidade ou novo approach
- **MINOR**: Novas features mantendo compatibilidade
- **PATCH**: Bug fixes

Exemplo: `credit-risk-analysis` v2.1.0 → v2.2.0 (nova métrica adicionada)

## ✅ Checklist para Adicionar uma Nova Skill

- [ ] Criar diretório em `skills/{categoria}/{skill-id}/`
- [ ] Escrever `SKILL.md` com descrição clara
- [ ] Criar `README.md` com exemplos de uso
- [ ] Adicionar exemplos em `examples/`
- [ ] Adicionar testes/evals em `tests/` se aplicável
- [ ] Atualizar `registry.json`
- [ ] Criar branch feature e PR
- [ ] Passar validação automática
- [ ] Merge para main

## 🛠️ Automação

### Validar Todas as Skills
```bash
python scripts/validate-skills.py
```

### Gerar Registry Automaticamente
```bash
python scripts/generate-registry.py
```

### Sincronizar com Claude
```bash
./scripts/sync-to-claude.sh --api-key $CLAUDE_API_KEY
```

## 📊 Status das Skills

| Skill | Versão | Status | Última Atualização |
|-------|--------|--------|-------------------|
| judicial-monitoring | 4.0.0 | ✅ Stable | 2026-04-12 |
| credit-risk-analysis | 2.1.0 | ✅ Stable | 2026-04-08 |
| seo-audit-traderisk | 1.2.0 | ✅ Stable | 2026-03-15 |
| licitaradar | 1.0.0 | 🚀 Beta | 2026-04-10 |
| traderisk-frontend-design | 3.1.0 | ✅ Stable | 2026-04-05 |

## 🔐 Segurança

- Nunca commite credentials (APIs, tokens)
- Use `.gitignore` para arquivos sensíveis
- Coloque secrets em `.env.example` (sem valores)
- Valide antes de fazer push

## 📝 Documentação

- [USAGE.md](docs/USAGE.md) - Como usar as skills em cada plataforma
- [INTEGRATION.md](docs/INTEGRATION.md) - Guia de integração
- [CONTRIBUTING.md](docs/CONTRIBUTING.md) - Contribuir com novas skills
- [ARCHITECTURE.md](docs/ARCHITECTURE.md) - Filosofia e design

## 🤝 Contribuindo

1. Fork o repositório
2. Crie branch: `git checkout -b feature/skill-name`
3. Faça commits claros
4. Push: `git push origin feature/skill-name`
5. Abra PR com descrição do que foi feito

## 📄 Licença

MIT License - Veja [LICENSE](LICENSE) para detalhes

## 📞 Contato

- **Maintainer**: Adriano Tomasoni (@adriano.tomasoni)
- **Email**: adriano@traderisk.com.br
- **Issues**: Use GitHub Issues para bugs ou sugestões
- **Discussions**: Use GitHub Discussions para perguntas

---

**Última atualização**: 2026-04-12  
**Versão do repo**: 1.0.0
