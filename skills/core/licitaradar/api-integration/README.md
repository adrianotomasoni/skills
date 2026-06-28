# Integração PNCP — clients

Esta pasta contém os clients TypeScript que dão suporte à skill LicitaRadar para buscar e classificar editais do PNCP (Portal Nacional de Contratações Públicas).

## Arquivos

### `pncp-client.ts`
Cliente HTTP da API pública do PNCP (`https://pncp.gov.br/api/pncp/v1`).

- **`buscarContratacoes({ dataInicial, dataFinal, pagina?, tamanhoPagina? })`** — lista contratações publicadas em uma janela de datas, paginada. Retorna `{ data: Contratacao[]; totalRegistros }`. Itere sobre `pagina` enquanto houver registros.
- **`buscarContratacao(numeroControlePNCP)`** — detalhe de uma contratação específica.
- **`interface Contratacao`** — campos relevantes: `numeroControlePNCP`, `orgaoEntidade`, `modalidadeNome`, `objetoCompra`, `valorTotalEstimado`, `dataPublicacaoPncp`, `dataEncerramentoProposta`, `linkSistemaOrigem`.

A API é pública e não exige autenticação. Trate erros de status (`!response.ok`) e respeite limites de paginação.

### `claude-classifier.ts`
Classificador que envia o texto do edital ao Claude e recebe a classificação estruturada.

- **`classificarOportunidade(editalTexto, claudeApiKey)`** — retorna `ClassificacaoOportunidade`: `{ classe, score, exigeSeguroGarantia, percentualGarantia?, observacoes[] }`.
- Usa o endpoint `POST https://api.anthropic.com/v1/messages`. Modelo configurado no arquivo; mantenha o id de modelo atualizado conforme a documentação vigente da Anthropic.
- A `claudeApiKey` deve vir de variável de ambiente/secret — nunca commitar a chave.

## Fluxo típico

1. `buscarContratacoes` na janela desejada → pré-filtrar por modalidade/valor.
2. Para os candidatos, obter o texto do edital (`buscarContratacao` + fonte de origem).
3. `classificarOportunidade` para classe + detecção de garantia.
4. Persistir e disparar alerta conforme a cadência da skill.

> Parâmetros de pré-filtro (valor mínimo, modalidades elegíveis, mapeamento de setor) e destino da persistência/alerta: TODO: preencher com <configuração proprietária> da TradeRisk.
