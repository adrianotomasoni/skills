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

## Exemplos de Componentes

Stack: Next.js App Router + Tailwind + shadcn/ui. Tokens em `colors.ts` / `typography.ts`.

### StatCard financeiro

```tsx
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ArrowUpRight } from "lucide-react";

export function StatCard({ label, value, delta }: { label: string; value: string; delta?: string }) {
  return (
    <Card className="border-l-4 border-l-primary">
      <CardHeader className="pb-2">
        <CardTitle className="text-sm font-medium text-muted-foreground">{label}</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="font-mono text-2xl font-bold tabular-nums">{value}</div>
        {delta && (
          <p className="mt-1 flex items-center gap-1 text-xs text-success">
            <ArrowUpRight className="h-3 w-3" aria-hidden="true" />
            {delta}
          </p>
        )}
      </CardContent>
    </Card>
  );
}
```

### DataTable — cabeçalho e coluna numérica (mono, à direita)

```tsx
import { ColumnDef } from "@tanstack/react-table";
import { Button } from "@/components/ui/button";
import { ArrowUpDown } from "lucide-react";

type Operacao = { id: string; ativo: string; valor: number };

export const columns: ColumnDef<Operacao>[] = [
  { accessorKey: "ativo", header: "Ativo" },
  {
    accessorKey: "valor",
    // Cabeçalho de coluna numérica: ordenável e alinhado à direita
    header: ({ column }) => (
      <div className="text-right">
        <Button
          variant="ghost"
          className="-mr-2"
          onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
        >
          Valor
          <ArrowUpDown className="ml-2 h-4 w-4" aria-hidden="true" />
        </Button>
      </div>
    ),
    // Célula numérica: mono + tabular-nums + alinhada à direita
    cell: ({ row }) => (
      <div className="text-right font-mono tabular-nums">
        {new Intl.NumberFormat("pt-BR", { style: "currency", currency: "BRL" }).format(
          row.getValue("valor"),
        )}
      </div>
    ),
  },
];
```

### Badge de status

```tsx
import { Badge } from "@/components/ui/badge";

const statusStyles = {
  stable: "bg-green-100 text-green-800 hover:bg-green-100",
  beta: "bg-yellow-100 text-yellow-800 hover:bg-yellow-100",
  deprecated: "bg-red-100 text-red-800 hover:bg-red-100",
} as const;

export function StatusBadge({ status }: { status: keyof typeof statusStyles }) {
  return <Badge className={statusStyles[status]}>{status}</Badge>;
}
```

### Form field com React Hook Form + Zod

```tsx
"use client";
import { z } from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import {
  Form, FormControl, FormField, FormItem, FormLabel, FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

const schema = z.object({
  ativo: z.string().min(1, "Informe o ativo"),
  valor: z.coerce.number().positive("Valor deve ser positivo"),
});

export function OperacaoForm() {
  const form = useForm<z.infer<typeof schema>>({
    resolver: zodResolver(schema),
    defaultValues: { ativo: "", valor: 0 },
  });

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit((v) => console.log(v))} className="space-y-4">
        <FormField
          control={form.control}
          name="ativo"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Ativo</FormLabel>
              <FormControl>
                <Input {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="valor"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Valor</FormLabel>
              <FormControl>
                <Input type="number" className="text-right font-mono" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        {/* Submit no canto inferior direito */}
        <div className="flex justify-end">
          <Button type="submit" disabled={form.formState.isSubmitting}>
            {form.formState.isSubmitting ? "Salvando..." : "Salvar"}
          </Button>
        </div>
      </form>
    </Form>
  );
}
```

### Loading state (skeleton no formato da tabela)

```tsx
import { Skeleton } from "@/components/ui/skeleton";

export function TableSkeleton({ rows = 5 }: { rows?: number }) {
  return (
    <div className="space-y-2" aria-hidden="true">
      {Array.from({ length: rows }).map((_, i) => (
        <div key={i} className="flex items-center justify-between gap-4 py-2">
          <Skeleton className="h-4 w-32" />
          <Skeleton className="h-4 w-24" />
        </div>
      ))}
    </div>
  );
}
```

### Empty state

```tsx
import { Inbox } from "lucide-react";
import { Button } from "@/components/ui/button";

export function EmptyState() {
  return (
    <div className="flex flex-col items-center rounded-lg border border-dashed py-12 text-center">
      <Inbox className="h-10 w-10 text-muted-foreground" aria-hidden="true" />
      <p className="mt-3 text-sm font-medium">Nenhuma operação registrada</p>
      <p className="mt-1 text-sm text-muted-foreground">Cadastre a primeira para começar.</p>
      <Button className="mt-4">Nova operação</Button>
    </div>
  );
}
```

## Acessibilidade

- HTML semântico via componentes shadcn/ui; ARIA apenas quando o nativo não basta.
- Contraste mínimo 4.5:1 (WCAG 2.1 AA); badges de status não dependem só de cor (texto sempre presente).
- Foco visível com `focus-visible` (anel via token `--ring`); nunca remover outline sem substituto.
- Navegação completa por teclado; em modais o foco entra ao abrir, fica preso e retorna ao gatilho ao fechar (shadcn Dialog já cobre).
- Ícones decorativos com `aria-hidden="true"`; botões de ícone com `aria-label`.
- Inputs sempre com `<FormLabel>` associado; erros via `FormMessage` (ligado por `aria-describedby` no shadcn Form).

## Densidade (data-first)

- Usuários B2B esperam alta densidade de informação — priorize tabelas e KPIs visíveis sem rolagem excessiva.
- Espaçamento compacto e controlado: `py-2` em linhas de tabela, `gap-4` em grids de cards.
- Números sempre em `font-mono tabular-nums` e alinhados à direita para leitura em coluna.
- Use zebra striping sutil (`odd:bg-muted/40`) em tabelas longas para rastreio de linha.
- Evite cards "inflados" com muito espaço em branco quando o objetivo é comparar muitos valores.
- Densidade não justifica baixo contraste ou alvos de toque < 44px em telas touch.
