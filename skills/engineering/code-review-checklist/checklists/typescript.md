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
