#!/usr/bin/env python3
"""
Runner de referência, provider-agnóstico, para o Agente Buscador de SGJ.

Lê o system prompt canônico e um dump V3 (JSON de processo) e emite o parecer.
Suporta Anthropic, OpenAI e Gemini via flag --provider. Saída estruturada quando possível.

Uso:
    python run_agent.py --provider anthropic --input examples/processo_exemplo.json
    python run_agent.py --provider openai    --input examples/processo_exemplo.json --json
    python run_agent.py --provider gemini     --input examples/processo_exemplo.json --json

Chaves via env: ANTHROPIC_API_KEY | OPENAI_API_KEY | GOOGLE_API_KEY
"""
import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
SYSTEM_PROMPT = (ROOT / "prompts" / "system_prompt.md").read_text(encoding="utf-8")
SCHEMA = json.loads((ROOT / "schemas" / "parecer.schema.json").read_text(encoding="utf-8"))


def build_user_message(payload: dict) -> str:
    return (
        "Analise o(s) processo(s) abaixo e produza o parecer de SGJ seguindo o algoritmo "
        "de 8 travas e o formato de saída. Se for pedido JSON, valide contra o schema.\n\n"
        "```json\n" + json.dumps(payload, ensure_ascii=False, indent=2) + "\n```"
    )


def run_anthropic(user_msg: str, as_json: bool) -> str:
    from anthropic import Anthropic

    client = Anthropic()
    sys_prompt = SYSTEM_PROMPT
    if as_json:
        sys_prompt += (
            "\n\nIMPORTANTE: responda APENAS com um objeto JSON válido conforme o schema "
            "ParecerSGJ, sem texto antes ou depois, sem cercas de código."
        )
    resp = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=2000,
        system=sys_prompt,
        messages=[{"role": "user", "content": user_msg}],
    )
    return "".join(b.text for b in resp.content if b.type == "text")


def run_openai(user_msg: str, as_json: bool) -> str:
    from openai import OpenAI

    client = OpenAI()
    kwargs = dict(
        model="gpt-4.1",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_msg},
        ],
    )
    if as_json:
        kwargs["text"] = {
            "format": {"type": "json_schema", "name": "ParecerSGJ", "strict": False, "schema": SCHEMA}
        }
    resp = client.responses.create(**kwargs)
    return resp.output_text


def run_gemini(user_msg: str, as_json: bool) -> str:
    from google import genai
    from google.genai import types

    client = genai.Client()
    cfg = dict(system_instruction=SYSTEM_PROMPT, temperature=0.2)
    if as_json:
        cfg["response_mime_type"] = "application/json"
        # schema completo pode ser recusado; em produção use versão simplificada se necessário
    resp = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=user_msg,
        config=types.GenerateContentConfig(**cfg),
    )
    return resp.text


PROVIDERS = {"anthropic": run_anthropic, "openai": run_openai, "gemini": run_gemini}


def main() -> int:
    ap = argparse.ArgumentParser(description="Runner do Agente Buscador de SGJ")
    ap.add_argument("--provider", choices=PROVIDERS, required=True)
    ap.add_argument("--input", required=True, help="JSON de processo (dump V3) ou lista de processos")
    ap.add_argument("--json", action="store_true", help="Pede saída estruturada (ParecerSGJ)")
    args = ap.parse_args()

    payload = json.loads(pathlib.Path(args.input).read_text(encoding="utf-8"))
    user_msg = build_user_message(payload)
    out = PROVIDERS[args.provider](user_msg, args.json)
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
