# Runbook: Deploy de uma Supabase Edge Function

## Objetivo

Fazer o deploy (ou atualização) de uma Edge Function para o projeto Supabase de
produção de forma segura e verificável, com caminho de rollback definido.

Use este runbook ao publicar uma function nova ou ao atualizar uma existente
(ex.: a function de recebimento de webhooks descrita no ADR-0001).

## Pré-requisitos

- Supabase CLI instalado e autenticado (`supabase --version`, `supabase login`).
- Acesso de deploy ao projeto de produção.
- `project-ref` do projeto de produção. TODO: project-ref do ambiente TradeRisk.
- Segredos da function já configurados no ambiente (ver passo 2).
- Branch com a alteração revisada e mergeada (ou tag de release).

## Passos

1. Selecione/anote o projeto de destino e confirme o ambiente:

   ```bash
   supabase projects list
   ```

2. Configure/atualize os secrets usados pela function (não comitar valores):

   ```bash
   supabase secrets set WEBHOOK_SIGNING_SECRET=<valor> --project-ref <project-ref>
   ```

   TODO: lista completa de secrets exigidos pela function no padrão TradeRisk.

3. Faça um deploy de teste em staging antes de produção:

   ```bash
   supabase functions deploy <nome-da-function> --project-ref <project-ref-staging>
   ```

4. Após validar em staging, faça o deploy em produção:

   ```bash
   supabase functions deploy <nome-da-function> --project-ref <project-ref-prod>
   ```

## Verificação

- Confirme que a function aparece como ativa:

  ```bash
  supabase functions list --project-ref <project-ref-prod>
  ```

- Faça uma chamada de teste e confirme resposta `2xx`:

  ```bash
  curl -i -X POST \
    "https://<project-ref-prod>.functions.supabase.co/<nome-da-function>" \
    -H "Content-Type: application/json" \
    -d '{ "ping": true }'
  ```

- Acompanhe os logs em tempo real durante o teste:

  ```bash
  supabase functions logs <nome-da-function> --project-ref <project-ref-prod>
  ```

- Confirme no banco que o evento de teste foi persistido (TODO: tabela/critério).

## Rollback

1. Identifique a versão anterior conhecida como boa (commit/tag).

   ```bash
   git checkout <tag-ou-commit-anterior>
   ```

2. Faça o redeploy a partir dela:

   ```bash
   supabase functions deploy <nome-da-function> --project-ref <project-ref-prod>
   ```

3. Repita a seção **Verificação** para confirmar que voltou ao estado bom.

## Troubleshooting

- **Deploy falha com erro de autenticação** → token expirado; rode
  `supabase login` e tente de novo.
- **Function responde 401/403 ao provedor** → secret de assinatura ausente ou
  errado; verifique `supabase secrets list` e reconfigure.
- **Resposta 5xx / timeout** → cheque os logs; processamento pesado deve ser
  assíncrono, a function só recebe e enfileira (ver ADR-0001).
- **Provedor reenvia o webhook repetidamente** → a function não está respondendo
  `2xx` a tempo; confirme que a resposta acontece antes do processamento pesado.
- **Evento não aparece no banco** → verifique RLS/credenciais usadas pela
  function e os logs de erro de escrita.
