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

## Common Mistakes

- Documentação que descreve "o quê" mas não "como rodar" → incluir setup executável.
- ADR sem consequências negativas → registrar trade-offs honestamente.
- Exemplos de código que não funcionam → validar antes de publicar.
- Docs desatualizadas em relação ao código → atualizar junto com mudanças.
