# OpenAI — Adaptador (GPT personalizado / Assistants / Responses API)

O núcleo do agente é `prompts/system_prompt.md`. Para OpenAI, use-o como **system / developer
message** e ative saída estruturada com `schemas/parecer.schema.json`.

## 1. GPT personalizado (ChatGPT → "Explore GPTs → Create")

- **Instructions:** cole o conteúdo de `prompts/system_prompt.md`.
- **Knowledge:** suba `docs/quadro_normativo.md` e `examples/casos_referencia.md`.
- **Capabilities:** desative navegação/imagem se não usar; mantenha apenas o necessário.
- **Conversation starters:**
  - "Analise este dump V3 e diga se é oportunidade."
  - "Gere o sumário priorizado deste tomador."
  - "Aplique a trava C3 neste processo."

## 2. Responses API (recomendado) — saída estruturada

```python
from openai import OpenAI
import json, pathlib

client = OpenAI()
system_prompt = pathlib.Path("prompts/system_prompt.md").read_text(encoding="utf-8")
schema = json.loads(pathlib.Path("schemas/parecer.schema.json").read_text(encoding="utf-8"))

resp = client.responses.create(
    model="gpt-4.1",
    input=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "<<cole aqui o JSON do processo / dump V3>>"},
    ],
    text={
        "format": {
            "type": "json_schema",
            "name": "ParecerSGJ",
            "strict": True,
            "schema": schema,
        }
    },
)
print(resp.output_text)
```

> Nota: para `strict: true` a OpenAI exige `additionalProperties: false` e que todo objeto liste
> suas chaves em `required`. O schema já usa `additionalProperties: false`. Se o validador `strict`
> reclamar de campos opcionais, use o schema em modo não-estrito (`strict: false`) ou promova os
> opcionais a `required` com `type` aceitando `null`.

## 3. Assistants API

```python
assistant = client.beta.assistants.create(
    name="Buscador SGJ",
    instructions=system_prompt,
    model="gpt-4.1",
    tools=[{"type": "file_search"}],   # anexe quadro_normativo.md e casos_referencia.md
)
```

## 4. Lote (carteira de um tomador)

Itere processo a processo (cada um é uma trava independente) e só então consolide o sumário por
tomador. Não envie a carteira inteira num único turno se quiser um parecer por processo — envie
um processo por requisição e agregue do lado do cliente, ou peça explicitamente o "sumário por
tomador" num turno final passando os pareceres já gerados.
