---
name: agent-id-em-kebab-case
description: "Quando este agente deve ser acionado. Use SEMPRE que houver: [gatilhos]. Especialista em [domínio]."
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
---

# Nome Legível do Agente

## Identidade & Missão

Quem é o agente, seu domínio de especialidade e o objetivo central.

## Quando me acione

- Gatilho 1
- Gatilho 2

## Como eu trabalho

Passos / protocolo que o agente segue. Referencie skills do repo quando aplicável
(ex.: "uso a skill `credit-risk-analysis` em skills/core/").

## Skills vinculadas

- `nome-da-skill` — para quê

## Formato de saída

O que o agente entrega e em que formato.

---
<!-- Metadados de portabilidade ficam em agent.json. -->
