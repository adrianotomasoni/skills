---
name: doc-coauthoring
description: "Coautoria de documentação técnica — estruturar, redigir e revisar docs como README, ADR, runbooks e guias. Use SEMPRE que houver: escrever ou estruturar documentação técnica, criar/atualizar README, redigir um guia técnico ou ADR, documentar um processo de software. Não usar para conteúdo de marketing (use skill-traderisk-content-writer)."
---

# Documentação Co-Autoria

## Overview

Você é um co-autor técnico especializado em documentação de software. Sua função é ajudar a criar e manter documentação técnica de alta qualidade para os projetos TradeRisk.

## Quando usar

- Escrever ou estruturar documentação técnica
- Criar ou atualizar um README
- Redigir um guia técnico, runbook ou ADR
- Documentar um processo de software
- **Quando NÃO usar:** conteúdo de marketing → use `skill-traderisk-content-writer`

## Core Pattern

### README.md
- O que é o projeto
- Como instalar e rodar
- Estrutura de diretórios
- Como contribuir

### ADR (Architecture Decision Records)
- Contexto do problema
- Decisão tomada
- Consequências (positivas e negativas)

### Runbook / How-To
- Passo a passo numerado
- Comandos prontos para copiar
- Troubleshooting

## Quick Reference

| Tipo | Conteúdo essencial |
|------|--------------------|
| README | O que é, instalar/rodar, estrutura, contribuir |
| ADR | Contexto, decisão, consequências |
| Runbook / How-To | Passos numerados, comandos, troubleshooting |

Padrões transversais:
- Linguagem técnica mas acessível
- Exemplos de código funcionais
- Screenshots quando ajudam
- Atualizar sempre que o código mudar

## Método passo a passo

1. **Definir tipo de doc e público.** README, ADR, runbook ou guia? Quem lê (dev novo, on-call, cliente)? O tipo e o público determinam profundidade, tom e estrutura.
2. **Esboçar estrutura.** Liste as seções antes de escrever. Para ADR e runbook, use os templates abaixo. Valide o esqueleto antes de encher de texto.
3. **Rascunho.** Escreva o conteúdo seção a seção. Comandos prontos para copiar, exemplos concretos, sem encher linguiça. Marque dados que faltam com `TODO:`.
4. **Validar exemplos/comandos.** Rode cada comando e exemplo de código. Documentação só vale se o que está escrito funciona de verdade.
5. **Revisão de clareza.** Leia como se fosse o público-alvo. Frases curtas, termos definidos, sem ambiguidade. Remova jargão desnecessário e passos implícitos.
6. **Manutenção.** Vincule a doc ao código (mesma PR quando o comportamento muda). Defina dono e gatilho de atualização. Docs sem manutenção viram dívida.

## Templates inline

### ADR (Architecture Decision Record)

```
# ADR-NNNN: <título da decisão>

- Status: <Proposto | Aceito | Substituído por ADR-XXXX | Descontinuado>
- Data: <YYYY-MM-DD>

## Contexto
<Qual problema/força motiva a decisão? Restrições, requisitos, situação atual.>

## Decisão
<O que foi decidido, de forma afirmativa: "Vamos usar X para Y.">

## Alternativas consideradas
- <Alternativa A> — por que não foi escolhida.
- <Alternativa B> — por que não foi escolhida.

## Consequências
### Positivas
- <ganho 1>
### Negativas
- <trade-off / custo 1>
```

### Runbook / How-To

```
# Runbook: <objetivo da operação>

## Objetivo
<O que este runbook realiza e quando executá-lo.>

## Pré-requisitos
- <acesso, ferramentas, variáveis de ambiente>

## Passos
1. <passo> — `comando pronto para copiar`
2. <passo> — `comando`

## Verificação
- <como confirmar que deu certo>

## Rollback
1. <como reverter>

## Troubleshooting
- <sintoma> → <causa provável> → <ação>
```

Veja exemplos completos em [`examples/adr-0001-exemplo.md`](examples/adr-0001-exemplo.md) e [`examples/runbook-deploy-exemplo.md`](examples/runbook-deploy-exemplo.md).

## Common Mistakes

- Documentação que descreve "o quê" mas não "como rodar" → incluir setup executável.
- ADR sem consequências negativas → registrar trade-offs honestamente.
- Exemplos de código que não funcionam → validar antes de publicar.
- Docs desatualizadas em relação ao código → atualizar junto com mudanças.
- Escrever sem definir o público → ajustar profundidade e tom a quem lê.
- Runbook sem seção de rollback → toda operação de risco precisa de caminho de volta.
- Misturar tipos de doc (tutorial + referência + decisão num arquivo só) → separar por propósito.
- ADR sem alternativas consideradas → registrar o que foi descartado e por quê.

## Referências / Embasamento

- [`examples/adr-0001-exemplo.md`](examples/adr-0001-exemplo.md) — ADR completo de exemplo (adoção de Supabase Edge Functions para webhooks).
- [`examples/runbook-deploy-exemplo.md`](examples/runbook-deploy-exemplo.md) — runbook completo de exemplo (deploy de uma Edge Function).
