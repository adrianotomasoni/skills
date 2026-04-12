/**
 * PNCP API Client
 * Portal Nacional de Contratações Públicas
 * https://pncp.gov.br/api/pncp/swagger-ui/index.html
 */

const PNCP_BASE_URL = 'https://pncp.gov.br/api/pncp/v1';

export interface Contratacao {
  numeroControlePNCP: string;
  orgaoEntidade: { cnpj: string; razaoSocial: string };
  unidadeOrgao: { nomeUnidade: string };
  modalidadeNome: string;
  objetoCompra: string;
  valorTotalEstimado: number;
  dataPublicacaoPncp: string;
  dataEncerramentoProposta: string;
  linkSistemaOrigem: string;
}

export async function buscarContratacoes(params: {
  dataInicial: string;
  dataFinal: string;
  pagina?: number;
  tamanhoPagina?: number;
}): Promise<{ data: Contratacao[]; totalRegistros: number }> {
  const query = new URLSearchParams({
    dataInicial: params.dataInicial,
    dataFinal: params.dataFinal,
    pagina: String(params.pagina ?? 1),
    tamanhoPagina: String(params.tamanhoPagina ?? 50),
  });

  const response = await fetch(`${PNCP_BASE_URL}/contratacoes/publicacao?${query}`);
  if (!response.ok) {
    throw new Error(`PNCP API error: ${response.status}`);
  }
  return response.json();
}

export async function buscarContratacao(numeroControlePNCP: string): Promise<Contratacao> {
  const response = await fetch(`${PNCP_BASE_URL}/contratacoes/${numeroControlePNCP}`);
  if (!response.ok) {
    throw new Error(`PNCP API error: ${response.status}`);
  }
  return response.json();
}
