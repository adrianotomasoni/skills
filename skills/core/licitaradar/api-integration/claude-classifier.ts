/**
 * LicitaRadar Classifier
 * Uses Claude to classify and score licitacao opportunities
 */

export interface ClassificacaoOportunidade {
  classe: 'alta' | 'media' | 'baixa';
  score: number;
  exigeSeguroGarantia: boolean;
  percentualGarantia?: number;
  observacoes: string[];
}

export async function classificarOportunidade(
  editalTexto: string,
  claudeApiKey: string
): Promise<ClassificacaoOportunidade> {
  const prompt = `
Analise este edital de licitação e responda em JSON:

${editalTexto}

Responda:
{
  "classe": "alta|media|baixa",
  "score": 0-100,
  "exigeSeguroGarantia": true|false,
  "percentualGarantia": número ou null,
  "observacoes": ["..."]
}
`;

  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'x-api-key': claudeApiKey,
      'anthropic-version': '2023-06-01',
      'content-type': 'application/json',
    },
    body: JSON.stringify({
      model: 'claude-sonnet-4-5',
      max_tokens: 1024,
      messages: [{ role: 'user', content: prompt }],
    }),
  });

  const data = await response.json();
  return JSON.parse(data.content[0].text);
}
