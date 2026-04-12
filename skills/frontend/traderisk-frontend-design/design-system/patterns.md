# Padrões de Design – TradeRisk

## Layout

- Sidebar fixa de 240px (desktop) / drawer (mobile)
- Header com breadcrumb e ações contextuais
- Conteúdo principal em grid responsivo

## Formulários

- Labels sempre acima do campo
- Validação inline com Zod
- Botão de submit no canto inferior direito
- Loading state em todos os botões assíncronos

## Tabelas de Dados

- shadcn/ui DataTable com paginação
- Colunas ordenáveis clicando no header
- Filtros no topo, exportar CSV à direita
- Célula numérica sempre alinhada à direita, fonte mono

## Feedback ao Usuário

- Toast (sonner) para confirmações
- Dialog modal para ações destrutivas
- Skeleton loading, nunca spinner isolado
