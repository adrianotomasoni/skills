# Checklist TypeScript – Code Review

## Tipagem
- [ ] Sem uso de `any` (use `unknown` se necessário)
- [ ] Interfaces para objetos de dados, types para unions
- [ ] Generics ao invés de any quando possível
- [ ] Return types explícitos em funções públicas

## Padrões
- [ ] Enums ou const objects para valores fixos
- [ ] Null checks explícitos (optional chaining `?.`)
- [ ] Type guards para narrowing
- [ ] Discriminated unions para state machines

## Tipagem avançada
- [ ] Utility types em vez de redefinir formas (`Pick`, `Omit`, `Partial`, `Record`, `ReturnType`)
- [ ] `satisfies` para validar um literal contra um tipo sem perder o tipo estreito
- [ ] `as const` para literais imutáveis e tuplas/uniões derivadas
- [ ] Tipos derivados da fonte de verdade (ex.: `z.infer<typeof schema>`) em vez de duplicados
- [ ] Generics com restrições (`extends`) em vez de `any`
- [ ] Template literal types onde agregam segurança real (sem complexidade gratuita)

## Segurança de tipos
- [ ] Sem `any` em boundaries (APIs, props públicas, retornos exportados) — use `unknown` + narrowing
- [ ] Dados de I/O (fetch, request body, env, localStorage) validados em runtime com Zod (não só cast)
- [ ] Sem `as` (type assertion) escondendo incompatibilidade real; preferir validação/guards
- [ ] `JSON.parse` tipado via parse/validação, nunca `as T` direto
- [ ] Sem `!` (non-null assertion) sem garantia de que o valor existe

## Configuração
- [ ] `strict: true` habilitado no tsconfig
- [ ] `noUncheckedIndexedAccess` para acesso indexado seguro (`arr[i]` pode ser `undefined`)
- [ ] `noImplicitAny`, `strictNullChecks` ativos
- [ ] `exactOptionalPropertyTypes` quando aplicável ao projeto
- [ ] Sem `// @ts-ignore`; usar `// @ts-expect-error` com justificativa quando inevitável

## Tratamento de erros
- [ ] Result/discriminated unions (`{ ok: true, data } | { ok: false, error }`) em fluxos previsíveis
- [ ] `throw` reservado para erros excepcionais, não controle de fluxo esperado
- [ ] Erros tipados (classes ou union) em vez de `catch (e: any)`; usar `catch (e: unknown)` + narrowing
- [ ] Funções async sempre tratam rejeição ou propagam de forma tipada

## Imports e módulos
- [ ] `import type` para imports usados apenas em tipos (evita side effects e melhora tree-shaking)
- [ ] Sem dependências circulares entre módulos
- [ ] Barrel files (`index.ts`) sem reexportar mundo inteiro a ponto de quebrar tree-shaking
- [ ] Paths/aliases consistentes com o tsconfig do projeto
