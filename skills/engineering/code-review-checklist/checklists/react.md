# Checklist React – Code Review

## Componentes
- [ ] Props tipadas com TypeScript interface/type
- [ ] PropTypes ou defaultProps necessários?
- [ ] Keys únicas em listas (não usar index)
- [ ] Memo/useMemo/useCallback onde performance importa

## Hooks
- [ ] useEffect com dependências corretas
- [ ] Cleanup de side effects (abort controllers, timers)
- [ ] Custom hooks para lógica reutilizável
- [ ] useState inicializado corretamente

## Renderização
- [ ] Sem conditional rendering aninhado excessivo
- [ ] Suspense + ErrorBoundary em async components
- [ ] Loading e error states tratados
