---
name: frontend-design
description: "Aplica princípios de design de interface (layout, hierarquia, responsividade, performance, acessibilidade) para web/app em geral. Use SEMPRE que houver: melhorar a aparência ou UX de uma interface genérica, definir breakpoints/responsividade, revisar acessibilidade de uma UI fora do produto. Não usar para o produto TradeRisk (use traderisk-frontend-design)."
---

# Frontend Design Patterns

## Overview

Você é um especialista em design de interfaces web modernas, com foco em produtos B2B, dashboards financeiros e aplicações de dados complexos. Esta skill reúne princípios gerais de design aplicáveis a qualquer interface web/app.

## Quando usar

- Melhorar a aparência ou a UX de uma interface genérica
- Definir responsividade, breakpoints e comportamento mobile
- Revisar performance percebida e acessibilidade de uma UI
- **Quando NÃO usar:** trabalho no produto TradeRisk com seu design system → use `traderisk-frontend-design`

## Core Pattern

### Responsividade
- Mobile-first com breakpoints: sm(640) md(768) lg(1024) xl(1280)
- Componentes collapsíveis em mobile
- Touch targets mínimo 44x44px

### Performance
- Lazy loading para imagens e componentes pesados
- Skeleton loading em vez de spinners
- Optimistic UI para ações do usuário

### Acessibilidade
- ARIA labels em todos os elementos interativos
- Contraste mínimo 4.5:1 (WCAG AA)
- Suporte a navegação por teclado

## Quick Reference

| Área | Diretriz |
|------|----------|
| Breakpoints | sm 640 / md 768 / lg 1024 / xl 1280 |
| Mobile | Mobile-first, componentes collapsíveis |
| Touch target | Mínimo 44x44px |
| Loading | Skeleton em vez de spinner |
| Feedback | Optimistic UI |
| Contraste | Mínimo 4.5:1 (WCAG AA) |
| Teclado | Navegação completa suportada |

## Método passo a passo

1. **Entender objetivo e usuário.** Antes de desenhar, responda: qual é a tarefa principal do usuário nesta tela? Qual é a ação prioritária (a "estrela" da tela)? Qual o contexto de uso (desktop em escritório, mobile em campo, alta frequência)? Tudo que não serve a essa tarefa compete por atenção e deve ser reduzido.
2. **Layout e hierarquia.** Estabeleça uma hierarquia visual clara: o olho deve cair primeiro no elemento mais importante. Use tamanho, peso, cor e espaço em branco — não apenas cor. Agrupe itens relacionados (lei da proximidade) e mantenha um único call-to-action primário por tela.
3. **Responsividade mobile-first.** Desenhe primeiro para a menor tela e vá adicionando complexidade nos breakpoints maiores (`sm 640 / md 768 / lg 1024 / xl 1280`). Em mobile, empilhe colunas, colapse navegação em drawer e priorize o conteúdo essencial acima da dobra.
4. **Estados (loading / empty / error).** Toda tela que busca dados precisa dos quatro estados: carregando (skeleton), com dados, vazio (empty state com orientação) e erro (mensagem clara + ação de retry). Projetar só o "caminho feliz" é o erro mais comum.
5. **Acessibilidade.** HTML semântico, contraste ≥ 4.5:1, foco visível, navegação completa por teclado, labels associados a inputs e ARIA apenas quando o HTML nativo não basta. Veja o checklist em `reference/ui-accessibility-checklist.md`.
6. **Performance percebida.** Skeleton no lugar de spinner, optimistic UI em ações rápidas, lazy loading de imagens/componentes pesados e priorização do conteúdo above-the-fold. A sensação de rapidez vale tanto quanto a rapidez real.
7. **Revisão final com checklist.** Antes de entregar, passe pelo `reference/ui-accessibility-checklist.md`: semântica, contraste, foco, teclado, formulários, alt, responsividade, touch targets, estados e motion.

## Exemplos concretos

### Hierarquia tipográfica

Estabeleça uma escala consistente e use peso/cor para reforçar a importância — não invente tamanhos arbitrários por tela.

```tsx
<section>
  <h1 className="text-3xl font-bold tracking-tight text-slate-900">Título da página</h1>
  <p className="mt-1 text-base text-slate-600">Subtítulo / contexto da página</p>

  <h2 className="mt-8 text-xl font-semibold text-slate-900">Seção</h2>
  <p className="mt-2 text-sm leading-relaxed text-slate-700">Texto de apoio (body).</p>

  <span className="mt-4 block text-xs font-medium uppercase tracking-wide text-slate-500">
    Rótulo / caption
  </span>
</section>
```

### Grid responsivo (mobile-first)

```tsx
{/* 1 coluna no mobile, 2 em tablet, 4 em desktop */}
<div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
  {items.map((item) => (
    <Card key={item.id}>{/* ... */}</Card>
  ))}
</div>
```

### Estado de loading com skeleton

Reproduza o formato do conteúdo real para evitar "salto" de layout (CLS) quando os dados chegam.

```tsx
function CardSkeleton() {
  return (
    <div className="rounded-lg border p-4" aria-hidden="true">
      <div className="h-4 w-24 animate-pulse rounded bg-slate-200" />
      <div className="mt-3 h-8 w-32 animate-pulse rounded bg-slate-200" />
    </div>
  );
}

{isLoading ? <CardSkeleton /> : <Card>{/* dados */}</Card>}
```

### Componente acessível (botão e input com ARIA)

```tsx
{/* Botão de ícone: precisa de label acessível porque não tem texto visível */}
<button
  type="button"
  aria-label="Fechar"
  className="inline-flex h-11 w-11 items-center justify-center rounded-md
             focus-visible:outline focus-visible:outline-2 focus-visible:outline-blue-600"
>
  <X className="h-5 w-5" aria-hidden="true" />
</button>

{/* Input: label associado por htmlFor/id + descrição de erro via aria-describedby */}
<div>
  <label htmlFor="email" className="block text-sm font-medium text-slate-700">
    E-mail
  </label>
  <input
    id="email"
    type="email"
    aria-invalid={!!error}
    aria-describedby={error ? "email-error" : undefined}
    className="mt-1 block w-full rounded-md border px-3 py-2
               focus-visible:outline focus-visible:outline-2 focus-visible:outline-blue-600"
  />
  {error && (
    <p id="email-error" className="mt-1 text-sm text-red-600">
      {error}
    </p>
  )}
</div>
```

### Empty state e error state

```tsx
{/* Vazio: explica o porquê e oferece próxima ação */}
<div className="flex flex-col items-center py-12 text-center">
  <Inbox className="h-10 w-10 text-slate-400" aria-hidden="true" />
  <p className="mt-3 text-sm font-medium text-slate-900">Nenhum item ainda</p>
  <p className="mt-1 text-sm text-slate-500">Crie o primeiro para começar.</p>
  <Button className="mt-4">Novo item</Button>
</div>

{/* Erro: mensagem clara + retry, com role="alert" para leitores de tela */}
<div role="alert" className="rounded-md border border-red-200 bg-red-50 p-4">
  <p className="text-sm text-red-800">Não foi possível carregar os dados.</p>
  <Button variant="outline" className="mt-2" onClick={retry}>Tentar novamente</Button>
</div>
```

## Common Mistakes

- Projetar desktop-first e adaptar depois → começar mobile-first.
- Usar spinners para carregamento longo → preferir skeleton loading.
- Touch targets menores que 44x44px → dificultam uso em mobile.
- Esquecer ARIA labels e contraste → quebra acessibilidade WCAG AA.
- Projetar apenas o "caminho feliz" e esquecer loading/empty/error → toda tela com dados precisa dos quatro estados.
- Comunicar significado só por cor (ex.: vermelho = erro) → reforce com ícone, texto ou padrão para daltônicos.
- Hierarquia "plana" (tudo com o mesmo peso) → defina um único foco primário por tela.
- Skeleton com formato diferente do conteúdo real → causa layout shift (CLS) e sensação de quebra.
- `aria-label` em botões com ícone esquecido → leitor de tela anuncia "botão" sem propósito.
- Remover o outline de foco (`outline: none`) sem substituir por `focus-visible` → usuários de teclado se perdem.
- Animações sem respeitar `prefers-reduced-motion` → desconforto e acessibilidade comprometida.

## Referências / Embasamento

- [Checklist de UI e acessibilidade (WCAG 2.1 AA)](reference/ui-accessibility-checklist.md)
