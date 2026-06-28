# ADR-0001: Adotar Supabase Edge Functions para webhooks de entrada

- Status: Aceito
- Data: 2026-06-28
- Autores: TODO: nome(s) do(s) responsável(is) pela decisão

## Contexto

Precisamos receber webhooks de provedores externos (ex.: gateway de pagamento e
bureau de crédito) e processá-los de forma confiável. Os requisitos:

- Endpoint HTTPS público, com baixa latência de resposta (o provedor espera `2xx`
  rapidamente, senão reenvia).
- Validação de assinatura/segredo do provedor antes de processar.
- Acesso ao banco para gravar o evento e disparar processamento posterior.
- Operação com o menor custo de infraestrutura e manutenção possível, já que o
  restante do produto já roda sobre Supabase (Postgres + Auth + Storage).

Hoje não há um padrão definido: cada integração nova exigiria provisionar e manter
um serviço HTTP próprio, o que aumenta a superfície operacional.

TODO: volume esperado de webhooks por provedor (req/min) no ambiente TradeRisk.

## Decisão

Vamos usar **Supabase Edge Functions (Deno)** como camada de recebimento de
webhooks de entrada. Cada provedor terá uma function dedicada que:

1. Valida a assinatura/segredo do provedor (segredo via `Deno.env`).
2. Responde `2xx` rapidamente após persistir o evento bruto.
3. Enfileira/dispara o processamento pesado de forma assíncrona, sem bloquear a
   resposta ao provedor.

## Alternativas consideradas

- **Serviço HTTP dedicado (container em provedor de cloud)** — descartado pelo
  custo operacional: provisionamento, deploy, escala e observabilidade próprios
  para algo que o Supabase já oferece integrado.
- **Database Webhooks / triggers diretos do Postgres** — descartado para
  *entrada*: bons para reagir a mudanças internas no banco, não para receber e
  validar requisições HTTP externas.
- **Funções serverless de outro provedor (ex.: outra cloud)** — descartado por
  fragmentar o stack e duplicar configuração de secrets e acesso ao banco.

## Consequências

### Positivas

- Reuso do stack já existente (mesmo projeto, mesmo acesso ao banco e secrets).
- Escala automática e custo proporcional ao uso.
- Deploy simples e versionável (ver runbook de deploy de Edge Function).
- Validação e persistência próximas do banco, reduzindo latência.

### Negativas

- Runtime Deno tem ecossistema/limitações diferentes de Node; algumas libs não
  rodam sem adaptação.
- Limites de tempo de execução exigem desenhar processamento pesado de forma
  assíncrona (a function só recebe e enfileira).
- Observabilidade depende dos logs do Supabase; pode exigir instrumentação extra.
- TODO: limites de tempo/recursos contratados no plano TradeRisk a confirmar.
