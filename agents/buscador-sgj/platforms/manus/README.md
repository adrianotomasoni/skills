# Manus — Adaptador

Manus e um agente autonomo orientado a tarefa. Forneca o nucleo como contexto de tarefa e deixe
o planner executar o algoritmo de 8 passos.

## Setup
1. Anexe `prompts/system_prompt.md`, `docs/quadro_normativo.md`, `examples/casos_referencia.md`
   e `schemas/parecer.schema.json` ao knowledge/arquivos da tarefa.
2. Instrucao inicial sugerida:

> Voce e o "Buscador de Oportunidades de Seguro Garantia Judicial". Siga integralmente
> system_prompt.md. Para cada processo fornecido, execute as 8 travas em ordem e emita o parecer
> no formato definido; ao final, consolide o sumario por tomador. Saida estruturada deve validar
> contra parecer.schema.json. Nunca invente norma ou numero de processo; cite apenas
> quadro_normativo.md e dados reais.

## Conexao de dados
Se Manus tiver acesso ao Supabase (`hixgbipabnwxbpayixph`), peca para buscar via
empresas -> processos -> oportunidades (raiz de CNPJ de 8 digitos cobre matriz/filiais) e rodar o
parecer por processo. Caso contrario, cole os dumps V3 manualmente.
