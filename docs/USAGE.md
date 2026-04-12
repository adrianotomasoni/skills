# 🚀 QUICK START - Setup em 5 Minutos

## 1️⃣ Clone o Repositório

```bash
git clone https://github.com/adrianotomasoni/skills.git
cd skills
```

## 2️⃣ Escolha Sua Plataforma

### 📱 Claude.ai (Mais Fácil)

```bash
# 1. Vá em Settings → Knowledge
# 2. Clique "Upload Files"
# 3. Selecione skills/core/[skill-name]/SKILL.md
# 4. Pronto!
```

**Alternativa**: Copie o conteúdo inteiro do SKILL.md e cole em Custom Instructions.

---

### 💻 Cursor (Melhor para Desenvolvimento)

```bash
# 1. Clone para ~/.cursor/
git clone https://github.com/adrianotomasoni/skills.git ~/.cursor/skills

# 2. Restart Cursor

# 3. Use em qualquer projeto:
#    @skill judicial-monitoring como implementar isso?
```

---

### 🖥️ Manus (Local)

```bash
# 1. Configure em seu projeto:
cat > manus.config.json << 'EOF'
{
  "skillsPath": "~/projects/skills/skills",
  "autoLoadSkills": true
}
EOF

# 2. Use:
#    @load-skill credit-risk-analysis
#    Analisa essa empresa...
```

---

### 🌐 GitHub (Source of Truth)

```bash
# Clone para editar
git clone https://github.com/adrianotomasoni/skills.git

# Configure Git
git config user.name "Seu Nome"
git config user.email "seu@email.com"

# Crie uma branch para mudanças
git checkout -b feature/sua-mudanca

# Faça edições, commit e push
git add skills/
git commit -m "feat: Seu commit aqui"
git push origin feature/sua-mudanca

# Abra PR no GitHub
```

---

## 3️⃣ Valide Tudo

```bash
# Instalar dependências (opcional, para validação)
# Nenhuma dependência necessária!

# Validar skills
python3 scripts/validate-skills.py

# Gerar registry
python3 scripts/generate-registry.py --summary
```

---

## 4️⃣ Comece a Usar!

### Em Claude.ai
```
Você acabou de fazer upload da skill de análise de crédito.

Prompt:
"Analisa essa empresa para mim: Fabrica XYZ CNPJ 12.345.678/0001-90"

Claude vai usar a skill automaticamente!
```

### Em Cursor
```
# Abra seu projeto
cd seu-projeto

# No chat:
@skill judicial-monitoring como funciona a detecção de eventos?

# Ou referencie diretamente:
@~/cursor/skills/skills/core/judicial-monitoring/SKILL.md
```

### Em Manus
```
@load-skill credit-risk-analysis
@load-skill judicial-monitoring

Tenho um caso novo: [descrição]
```

---

## 📊 Estrutura Rápida

```
skills/
├── skills/
│   ├── core/                    ← Skills de negócio
│   ├── frontend/                ← Design e UI
│   ├── content/                 ← Copywriting
│   └── engineering/             ← Código e arquitetura
├── registry.json                ← Índice master
├── scripts/                     ← Ferramentas
├── README.md                    ← Este arquivo
└── LICENSE
```

---

## ✨ Próximos Passos

### Para Usar Skills Existentes
1. ✅ Clone o repo
2. ✅ Escolha sua plataforma
3. ✅ Configure skills
4. ✅ Comece a usar!

### Para Criar Novas Skills
1. Crie diretório: `mkdir -p skills/categoria/nova-skill`
2. Copie template: `cp SKILL-TEMPLATE.md skills/categoria/nova-skill/SKILL.md`
3. Edite e customize
4. Valide: `python3 scripts/validate-skills.py`
5. Commit e push para GitHub

### Para Melhorar Skills Existentes
1. Crie branch: `git checkout -b feature/melhoria`
2. Edite arquivo `.md`
3. Valide: `python3 scripts/validate-skills.py`
4. Commit: `git commit -am "improve: descrição"`
5. Push e abra PR

---

## 🆘 Troubleshooting Rápido

### "Skill não aparece em Cursor"
```bash
# Force sync
cd ~/.cursor/skills
git pull origin main
# Restart Cursor
```

### "Erro ao validar"
```bash
# Verifique estrutura
ls -la skills/core/sua-skill/
# Deve ter SKILL.md

# Valide manualmente
python3 scripts/validate-skills.py --skill core/sua-skill
```

### "Merge conflict no GitHub"
```bash
# Atualize sua branch
git fetch origin
git rebase origin/main
# Resolva conflitos em seu editor
git rebase --continue
```

---

## 📱 Plataformas Suportadas

| Plataforma | Suporte | Setup |
|-----------|---------|-------|
| Claude.ai | ✅ Excelente | 2 min |
| Cursor | ✅ Excelente | 2 min |
| Manus | ✅ Perfeito | 5 min |
| VS Code | ✅ Ótimo | 2 min |
| GitHub | ✅ Essencial | 3 min |

---

## 🎯 Atalhos Úteis

```bash
# Validar todas as skills
python3 scripts/validate-skills.py

# Validar uma skill específica
python3 scripts/validate-skills.py --skill core/judicial-monitoring

# Regenerar registry
python3 scripts/generate-registry.py --summary

# Ver status de tudo
git status

# Última mudança
git log --oneline -5
```

---

## 📞 Ajuda Rápida

- 📖 Leia [README.md](README.md) para detalhes completos
- 🔗 Veja [INTEGRATION.md](INTEGRATION.md) para cada plataforma
- 🚀 Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para contribuir
- 📋 Use [SKILL-TEMPLATE.md](SKILL-TEMPLATE.md) para criar skills

---

**Você está pronto! 🎉 Comece a usar suas skills agora!**
