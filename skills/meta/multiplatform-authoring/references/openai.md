# OpenAI — ChatGPT / Custom GPTs / Assistants API

**Formato:** **remove** o frontmatter. O `description` vira um preâmbulo.

## Adaptação (feita por export-adapters.py)
O exportador gera, em `dist/openai/<id>.md`:
```
# <Título da skill>
Use esta skill quando: <description sem o "Use SEMPRE que houver:" formatado>.

<corpo do SKILL.md>
```

## Instalar
- **Custom GPT:** GPT Builder → *Instructions* → cole `dist/openai/<id>.md`.
  Arquivos de apoio (`references/`, `templates/`) → *Knowledge* (upload).
- **Assistants API:** use o texto como `instructions` do Assistant; suba apoio
  via File Search; mapeie `tools` do agente para *Functions*.
- **ChatGPT (avulso):** cole o conteúdo no início da conversa.

## Notas
- Sem frontmatter YAML — ChatGPT não o interpreta; deixá-lo confunde o modelo.
- `tools` de um agente viram Functions/ferramentas nativas (code interpreter, web).
