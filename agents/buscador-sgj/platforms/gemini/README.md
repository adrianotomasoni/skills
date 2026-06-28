# Google Gemini — Adaptador (Gem / API system_instruction)

O núcleo é `prompts/system_prompt.md`. No Gemini ele entra como **system instruction**.

## 1. Gem (Gemini app → "Gems → New Gem")

- **Instructions:** cole `prompts/system_prompt.md`.
- **Knowledge / arquivos:** anexe `docs/quadro_normativo.md` e `examples/casos_referencia.md`.

## 2. API (google-genai) — saída estruturada

```python
from google import genai
from google.genai import types
import json, pathlib

client = genai.Client()
system_prompt = pathlib.Path("prompts/system_prompt.md").read_text(encoding="utf-8")
schema = json.loads(pathlib.Path("schemas/parecer.schema.json").read_text(encoding="utf-8"))

resp = client.models.generate_content(
    model="gemini-2.5-pro",
    contents="<<cole aqui o JSON do processo / dump V3>>",
    config=types.GenerateContentConfig(
        system_instruction=system_prompt,
        response_mime_type="application/json",
        response_schema=schema,
    ),
)
print(resp.text)
```

> Notas Gemini:
> - O `response_schema` do Gemini é um subconjunto do JSON Schema (OpenAPI 3.0). Se a API recusar
>   algum construto (`enum` com `null`, `$id`, `additionalProperties`), use uma versão simplificada
>   do schema sem esses campos, ou peça JSON livre no prompt e valide do lado do cliente contra
>   `schemas/parecer.schema.json`.
> - Mantenha `temperature` baixa (0.1–0.3) para estabilidade das travas.

## 3. Vertex AI

Mesma `system_instruction`. Aponte `genai.Client(vertexai=True, project=..., location=...)` e
mantenha o restante idêntico.
