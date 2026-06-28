# Checklist de UI e Acessibilidade (WCAG 2.1 AA)

Checklist acionável para revisar qualquer interface web/app. Marque cada item antes de
considerar a tela pronta. Itens marcados com **(AA)** são critérios diretos do WCAG 2.1
nível AA.

## Semântica HTML

- [ ] Usar elementos nativos pelo significado: `<button>` para ações, `<a>` para navegação, `<nav>`, `<main>`, `<header>`, `<footer>`, `<section>`.
- [ ] Um único `<h1>` por página; headings em ordem hierárquica (`h1 → h2 → h3`), sem pular níveis. **(AA)**
- [ ] Listas em `<ul>`/`<ol>`, tabelas de dados em `<table>` com `<th scope=...>`.
- [ ] Landmarks presentes (`main`, `nav`, `header`) para navegação por leitores de tela.
- [ ] Idioma da página declarado (`<html lang="pt-BR">`). **(AA)**

## Contraste de cor

- [ ] Texto normal com contraste ≥ 4.5:1 contra o fundo. **(AA)**
- [ ] Texto grande (≥ 24px ou ≥ 18.66px bold) com contraste ≥ 3:1. **(AA)**
- [ ] Ícones e bordas de componentes funcionais com contraste ≥ 3:1. **(AA)**
- [ ] Significado nunca transmitido só por cor — reforçar com texto, ícone ou padrão. **(AA)**
- [ ] Estados (hover, foco, disabled, erro) mantêm contraste suficiente.

## Foco visível

- [ ] Todo elemento interativo tem indicador de foco visível (`focus-visible`). **(AA)**
- [ ] Nunca usar `outline: none` sem substituto visível.
- [ ] Indicador de foco com contraste ≥ 3:1 contra o fundo adjacente. **(AA)**
- [ ] Ordem de foco segue a ordem visual/lógica da página. **(AA)**

## Navegação por teclado

- [ ] Toda funcionalidade acessível apenas com teclado (Tab, Shift+Tab, Enter, Espaço, setas). **(AA)**
- [ ] Sem "armadilhas de teclado" (foco preso em um componente). **(AA)**
- [ ] Modais/drawers: foco move para dentro ao abrir, fica preso enquanto aberto e retorna ao gatilho ao fechar.
- [ ] `Esc` fecha modais, popovers e menus.
- [ ] Skip link ("Pular para o conteúdo") disponível no topo. **(AA)**

## ARIA

- [ ] Preferir HTML nativo; usar ARIA só quando não houver elemento nativo adequado.
- [ ] Botões de ícone (sem texto) têm `aria-label`.
- [ ] Ícones decorativos têm `aria-hidden="true"`.
- [ ] Estados dinâmicos comunicados: `aria-expanded`, `aria-selected`, `aria-checked`, `aria-current`.
- [ ] Conteúdo que muta dinamicamente usa `aria-live` ou `role="status"`/`role="alert"`.
- [ ] Não usar `role` que contradiz o elemento (ex.: `role="button"` num `<a>` sem necessidade).

## Formulários acessíveis

- [ ] Todo input tem `<label>` associado por `htmlFor`/`id` (não só placeholder). **(AA)**
- [ ] Campos obrigatórios sinalizados visualmente e com `aria-required`/`required`.
- [ ] Erros associados ao campo via `aria-describedby` e marcados com `aria-invalid`. **(AA)**
- [ ] Mensagens de erro são textuais, específicas e sugerem correção. **(AA)**
- [ ] Agrupamentos relacionados usam `<fieldset>` + `<legend>` (ex.: radio group).
- [ ] Autocomplete apropriado em campos pessoais (`autocomplete="email"`). **(AA)**

## Imagens e alt

- [ ] Imagens informativas têm `alt` descritivo. **(AA)**
- [ ] Imagens decorativas têm `alt=""` (alt vazio, não ausente).
- [ ] Ícones funcionais têm texto acessível (label ou texto adjacente).
- [ ] Gráficos/charts têm alternativa textual (resumo, tabela ou `aria-label`).

## Responsividade

- [ ] Layout mobile-first; sem scroll horizontal em telas pequenas. **(AA)**
- [ ] Conteúdo legível a 320px de largura e a 400% de zoom. **(AA)**
- [ ] Breakpoints consistentes (sm 640 / md 768 / lg 1024 / xl 1280).
- [ ] Navegação colapsa em drawer/menu no mobile.
- [ ] Texto não fica truncado de forma que perca significado ao redimensionar.

## Touch targets

- [ ] Alvos de toque com no mínimo 44x44px (ideal 48px).
- [ ] Espaçamento suficiente entre alvos adjacentes para evitar toques errados.
- [ ] Ações principais ao alcance do polegar em mobile.

## Estados (loading / empty / error)

- [ ] Loading com skeleton no formato do conteúdo (evita layout shift), não spinner isolado.
- [ ] Empty state explica o motivo e oferece a próxima ação.
- [ ] Error state com mensagem clara, `role="alert"` e ação de retry.
- [ ] Estados disabled visualmente distintos e com contraste adequado.
- [ ] Feedback imediato em ações (toast, optimistic UI) anunciado a leitores de tela.

## Motion / prefers-reduced-motion

- [ ] Respeitar `@media (prefers-reduced-motion: reduce)` — reduzir/remover animações. **(AA)**
- [ ] Nenhum conteúdo pisca mais de 3 vezes por segundo. **(AA)**
- [ ] Animações de auto-play (carrossel) podem ser pausadas/paradas. **(AA)**
- [ ] Transições essenciais mantêm-se funcionais mesmo com motion reduzido.

## Revisão final

- [ ] Testado com navegação só por teclado.
- [ ] Testado com zoom de 200%–400%.
- [ ] Verificado com ferramenta automática (axe, Lighthouse) — sem violações críticas.
- [ ] Verificação manual de contraste nos componentes-chave.
