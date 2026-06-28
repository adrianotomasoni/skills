# Regras de Nomenclatura & Descrição

## Nome (`name`)
- `^[a-z0-9-]+$` — só minúsculas, números e hífens. Sem espaços, acentos, parênteses.
- **Igual ao nome da pasta.** `skills/core/credit-risk-analysis/` → `name: credit-risk-analysis`.
- Voz ativa / por aquilo que a skill FAZ. Gerúndios funcionam para processos.
  - ✅ `requesting-code-review`, `condition-based-waiting`, `credit-risk-analysis`
  - ❌ `code-review-helper`, `async-utils`, `Skill_CreditRisk`

## Descrição (`description`)
Padrão: **[o que faz] + "Use SEMPRE que houver: [gatilhos]" + [fronteira]**.

- Terceira pessoa (vai injetada no system prompt).
- Comece pelos **gatilhos concretos**: pedidos típicos do usuário, sintomas, verbos.
- Inclua **palavras que o agente buscaria**: mensagens de erro, sinônimos, nomes de ferramentas.
- Declare a **fronteira**: quando NÃO usar e qual skill usar no lugar.

### NUNCA resuma o workflow
Se o `description` resume o passo a passo, o agente segue o resumo e **não lê** a
skill. Exemplo real: "code review entre tarefas" fez o agente rodar UM review,
embora a skill mandasse DOIS. Mantenha o `description` só com *quando usar*.

```yaml
# ❌ resume workflow
description: Use ao executar planos - dispara um subagente por tarefa com review entre tarefas
# ✅ só gatilho
description: Use ao executar planos de implementação com tarefas independentes na sessão atual
```

```yaml
# ❌ primeira pessoa / vago
description: Eu ajudo com testes assíncronos quando estão instáveis
# ✅ terceira pessoa, problema concreto
description: Use quando testes têm race conditions, dependência de timing, ou passam/falham de forma inconsistente
```

## Limite de tamanho
O bloco de frontmatter inteiro (`name` + `description`) deve ter **≤ 1024 caracteres**.
Se passar, encurte o `description` preservando os gatilhos principais.
