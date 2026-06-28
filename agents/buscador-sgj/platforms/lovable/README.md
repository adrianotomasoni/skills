# Lovable — Adaptador

Lovable nao tem "system prompt" persistente como um agente de chat; voce embute o comportamento
do agente em (a) Knowledge do projeto e (b) prompts de geracao.

## 1. Knowledge do projeto
Em Project Settings -> Knowledge, cole o conteudo de:
- `prompts/system_prompt.md` (definicao do agente)
- `docs/quadro_normativo.md` (base de citacao)

Assim toda geracao herda as travas e o vocabulario do dominio.

## 2. Gerando a UI do parecer
Prompt sugerido no chat do Lovable:

> Construa uma tela "Parecer SGJ" que recebe um JSON de processo (saida do motor V3) e renderiza
> um card de parecer comercial seguindo EXATAMENTE o schema em parecer.schema.json (campos:
> status_comercial, esfera, fase, gatilho, produto_sugerido, base_legal, urgencia, valor,
> garantia_atual, pitch, ressalva). Aplique as travas do agente: polo passivo obrigatorio,
> encerrado=score 0, RJ/falencia exclui, coerencia C3 (em execucao nao rotular deposito recursal),
> fiscal nunca promete suspensao de exigibilidade tributaria. Cores de urgencia: critica=vermelho,
> alta=laranja, media=amarelo, baixa=cinza.

## 3. Integracao Supabase
O projeto ja usa Supabase (`hixgbipabnwxbpayixph`). Aponte o Lovable para as tabelas
`oportunidades`/`processos`/`partes` e use a query padrao empresas -> processos -> oportunidades.
A logica de classificacao NAO deve ser reimplementada no front: o front so renderiza o parecer; a
analise vem do agente (Edge Function chamando a API de IA com `prompts/system_prompt.md`).
