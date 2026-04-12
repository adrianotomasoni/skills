/**
 * TradeRisk Credit Score Calculator
 * Calculates credit score based on financial and behavioral indicators
 */

function calculateCreditScore(data) {
  let score = 0;

  // 1. Cadastral (max 200 pts)
  if (data.situacaoReceita === 'ATIVA') score += 100;
  if (data.anosAtividade >= 5) score += 60;
  else if (data.anosAtividade >= 2) score += 30;
  if (data.capitalSocial >= 100000) score += 40;

  // 2. Financial (max 400 pts)
  const liquidezCorrente = data.ativoCirculante / data.passivoCirculante;
  if (liquidezCorrente >= 2) score += 100;
  else if (liquidezCorrente >= 1.2) score += 60;
  else if (liquidezCorrente >= 1) score += 20;

  const endividamento = data.dividaFinanceira / data.receitaLiquida;
  if (endividamento <= 0.1) score += 120;
  else if (endividamento <= 0.3) score += 80;
  else if (endividamento <= 0.5) score += 40;

  const margemEBITDA = data.ebitda / data.receitaLiquida;
  if (margemEBITDA >= 0.2) score += 100;
  else if (margemEBITDA >= 0.1) score += 60;
  else if (margemEBITDA >= 0.05) score += 20;

  const coberturaJuros = data.ebitda / (data.despesasFinanceiras || 1);
  if (coberturaJuros >= 5) score += 80;
  else if (coberturaJuros >= 2) score += 40;

  // 3. Behavior (max 300 pts)
  if (!data.restricoesSerasa) score += 120;
  else score -= 50;

  if (data.protestos === 0) score += 80;
  else score -= data.protestos * 20;

  if (data.processosAtivos === 0) score += 60;
  else score -= Math.min(data.processosAtivos * 15, 60);

  if (data.historicoPagamentoTradeRisk === 'sem_atrasos') score += 40;

  // 4. Sector (max 100 pts)
  const riscoSetor = { baixo: 100, medio: 60, alto: 20 };
  score += riscoSetor[data.riscoSetor] || 60;

  // Clamp to 0-1000
  return Math.max(0, Math.min(1000, Math.round(score)));
}

function getRating(score) {
  if (score >= 800) return 'A';
  if (score >= 650) return 'B';
  if (score >= 500) return 'C';
  if (score >= 350) return 'D';
  if (score >= 200) return 'E';
  return 'F';
}

module.exports = { calculateCreditScore, getRating };
