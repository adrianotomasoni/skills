// TradeRisk Design System – Typography
export const typography = {
  fontFamily: {
    sans: ['Inter', 'system-ui', 'sans-serif'],
    mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
  },
  fontSize: {
    xs: '0.75rem',
    sm: '0.875rem',
    base: '1rem',
    lg: '1.125rem',
    xl: '1.25rem',
    '2xl': '1.5rem',
    '3xl': '1.875rem',
  },
  fontWeight: {
    normal: '400',
    medium: '500',
    semibold: '600',
    bold: '700',
  },
  lineHeight: {
    none: '1',
    tight: '1.25',   // títulos / display
    snug: '1.375',   // subtítulos
    normal: '1.5',   // body
    relaxed: '1.625', // texto longo
  },
  letterSpacing: {
    tighter: '-0.05em', // display grande
    tight: '-0.025em',  // headings
    normal: '0',
    wide: '0.025em',
    wider: '0.05em',    // labels / captions em uppercase
  },
};

/**
 * Escala de uso semântico — qual estilo aplicar a cada papel de texto,
 * com as classes Tailwind equivalentes. Use esta tabela em vez de escolher
 * tamanhos ad-hoc por tela.
 *
 * Números financeiros usam `font-mono tabular-nums` para alinhar dígitos
 * em colunas (essencial em tabelas e StatCards).
 */
export const typographyScale = {
  // Hero / números de destaque em dashboards
  display: {
    tailwind: 'text-4xl font-bold tracking-tighter leading-tight',
    usage: 'Título de impacto, número-herói de KPI',
  },
  h1: {
    tailwind: 'text-3xl font-bold tracking-tight leading-tight',
    usage: 'Título de página',
  },
  h2: {
    tailwind: 'text-2xl font-semibold tracking-tight leading-snug',
    usage: 'Título de seção',
  },
  h3: {
    tailwind: 'text-xl font-semibold leading-snug',
    usage: 'Subtítulo / título de card',
  },
  body: {
    tailwind: 'text-base font-normal leading-normal',
    usage: 'Texto corrido padrão',
  },
  bodySmall: {
    tailwind: 'text-sm font-normal leading-normal text-muted-foreground',
    usage: 'Texto de apoio, descrições',
  },
  caption: {
    tailwind: 'text-xs font-medium uppercase tracking-wider text-muted-foreground',
    usage: 'Rótulos, legendas, cabeçalhos de tabela',
  },
  // Valores financeiros / monetários / códigos
  mono: {
    tailwind: 'font-mono tabular-nums',
    usage: 'Números financeiros, valores monetários, IDs — alinhamento de dígitos',
  },
  monoLarge: {
    tailwind: 'font-mono tabular-nums text-2xl font-bold',
    usage: 'Valor principal de StatCard / KPI',
  },
} as const;
