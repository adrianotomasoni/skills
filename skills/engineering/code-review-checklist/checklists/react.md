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

## Estado e dados
- [ ] Derivar estado durante o render em vez de duplicar em `useState` + `useEffect`
- [ ] Sem estado redundante (o que pode ser calculado de props/outro estado não é armazenado)
- [ ] Lifting state up: estado vive no ancestral comum mais próximo, não duplicado em irmãos
- [ ] Estado do servidor gerenciado por lib de data fetching (React Query/SWR), não em `useState` manual
- [ ] `useEffect` usado só para sincronizar com sistemas externos, não para lógica derivável
- [ ] Atualizações de estado imutáveis (sem mutar objetos/arrays diretamente)
- [ ] Estado mínimo e normalizado (sem cópias profundas desnecessárias)

## Acessibilidade
- [ ] HTML semântico (`<button>`, `<nav>`, `<main>`, `<label>`) em vez de `<div>` clicável
- [ ] Elementos interativos acessíveis por teclado (foco e Enter/Espaço funcionam)
- [ ] `aria-*` apenas quando a semântica nativa não basta; sem `aria` redundante
- [ ] Inputs com `<label>` associado (`htmlFor`) ou `aria-label`
- [ ] Foco gerenciado em modais/diálogos (trap de foco, retorno do foco ao fechar)
- [ ] Imagens com `alt`; ícones decorativos com `alt=""`/`aria-hidden`
- [ ] Contraste e estados de foco visíveis preservados

## Performance
- [ ] Sem re-renders desnecessários (props/contexto que mudam de identidade a cada render)
- [ ] `React.memo` em componentes puros caros; `useMemo`/`useCallback` onde a identidade importa
- [ ] Context dividido para evitar re-render de toda a árvore ao mudar um valor
- [ ] Listas longas virtualizadas (react-window/react-virtual)
- [ ] Code splitting com `React.lazy`/`dynamic` em rotas/telas pesadas
- [ ] Sem funções/objetos recriados inline passados para componentes memoizados
- [ ] Imagens e assets pesados carregados sob demanda

## Formulários
- [ ] Controlled vs uncontrolled escolhido de forma consistente (sem misturar no mesmo input)
- [ ] React Hook Form + Zod para forms não triviais (validação e tipos compartilhados)
- [ ] Validação no submit e feedback de erro por campo
- [ ] Estado de submitting/disabled para evitar double submit
- [ ] Mensagens de erro associadas ao campo (acessibilidade)

## Erros e loading
- [ ] Todo fetch trata loading, sucesso e erro explicitamente
- [ ] ErrorBoundary cobre seções que podem falhar no render
- [ ] Mensagens de erro úteis ao usuário (não stack trace cru)
- [ ] Retry/fallback quando faz sentido
- [ ] Estados vazios (empty state) tratados além de loading/erro

## Testes
- [ ] React Testing Library testando comportamento, não implementação
- [ ] Queries por papel/acessibilidade (`getByRole`, `getByLabelText`) em vez de `getByTestId`
- [ ] Interações simuladas com `userEvent` (não `fireEvent` direto quando evitável)
- [ ] Asserções sobre o que o usuário vê, não sobre estado interno
- [ ] Casos de erro e loading cobertos, não só o caminho feliz
