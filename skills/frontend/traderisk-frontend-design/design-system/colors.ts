// TradeRisk Design System – Colors
export const colors = {
  primary: {
    50: '#EFF6FF',
    100: '#DBEAFE',
    500: '#3B82F6',
    600: '#2563EB',
    700: '#1D4ED8',
    800: '#1E40AF',
    900: '#1E3A8A',
  },
  secondary: {
    500: '#0EA5E9',
    600: '#0284C7',
  },
  success: '#16A34A',
  warning: '#D97706',
  danger: '#DC2626',
  neutral: {
    50: '#F8FAFC',
    100: '#F1F5F9',
    200: '#E2E8F0',
    500: '#64748B',
    700: '#334155',
    900: '#0F172A',
  },
};

/**
 * Tokens semânticos — referenciados na UI em vez de hex soltos.
 * Mapeiam para as CSS variables do shadcn/ui (ver bloco no fim do arquivo).
 */
export const semanticColors = {
  // Superfícies
  background: '#FFFFFF',        // --background — fundo da aplicação
  foreground: colors.neutral[900], // --foreground — texto principal
  card: '#FFFFFF',              // --card
  cardForeground: colors.neutral[900], // --card-foreground
  popover: '#FFFFFF',           // --popover
  popoverForeground: colors.neutral[900],

  // Marca / ações
  primary: colors.primary[800], // --primary — TODO: confirmar hex exato da marca TradeRisk
  primaryForeground: '#FFFFFF', // --primary-foreground
  secondary: colors.secondary[500], // --secondary
  secondaryForeground: '#FFFFFF',

  // Estados de feedback
  success: colors.success,      // verde — valores positivos / sucesso
  warning: colors.warning,      // âmbar — atenção
  danger: colors.danger,        // vermelho — erro / valores negativos
  destructive: colors.danger,   // --destructive (shadcn)
  destructiveForeground: '#FFFFFF',

  // Neutros utilitários
  muted: colors.neutral[100],          // --muted — fundo sutil (linhas zebradas, disabled)
  mutedForeground: colors.neutral[500], // --muted-foreground — texto secundário
  border: colors.neutral[200],         // --border — bordas e divisórias
  input: colors.neutral[200],          // --input — borda de campos
  ring: colors.primary[600],           // --ring — anel de foco (focus-visible)
} as const;

/**
 * Paleta para gráficos (Tremor / Recharts).
 * Ordem pensada para distinção e contraste em séries categóricas.
 * TODO: validar ordem/hex com a identidade visual oficial TradeRisk.
 */
export const chartColors = [
  colors.primary[600],   // série 1
  colors.secondary[500], // série 2
  colors.success,        // série 3
  colors.warning,        // série 4
  colors.danger,         // série 5
  colors.neutral[500],   // série 6 / "outros"
] as const;

// Mapeamento para o Tremor (prop `colors`): use os nomes da paleta do Tremor
// ou injete os hex acima via classes/config conforme o setup do projeto.
export const tremorChartPalette = ['blue', 'sky', 'emerald', 'amber', 'red', 'slate'] as const;

/**
 * Mapeamento para as CSS variables do shadcn/ui (globals.css, formato HSL):
 *
 *   :root {
 *     --background: 0 0% 100%;
 *     --foreground: 222 47% 11%;            // neutral.900
 *     --primary: 226 71% 40%;               // primary.800  (TODO: hex exato da marca)
 *     --primary-foreground: 0 0% 100%;
 *     --secondary: 199 89% 48%;             // secondary.500
 *     --muted: 210 40% 96%;                 // neutral.100
 *     --muted-foreground: 215 16% 47%;      // neutral.500
 *     --border: 214 32% 91%;                // neutral.200
 *     --input: 214 32% 91%;                 // neutral.200
 *     --ring: 221 83% 53%;                  // primary.600
 *     --destructive: 0 72% 51%;             // danger
 *   }
 *
 * E no tailwind.config.ts (theme.extend.colors), conectando os tokens:
 *
 *   colors: {
 *     border: 'hsl(var(--border))',
 *     input: 'hsl(var(--input))',
 *     ring: 'hsl(var(--ring))',
 *     background: 'hsl(var(--background))',
 *     foreground: 'hsl(var(--foreground))',
 *     primary: { DEFAULT: 'hsl(var(--primary))', foreground: 'hsl(var(--primary-foreground))' },
 *     muted: { DEFAULT: 'hsl(var(--muted))', foreground: 'hsl(var(--muted-foreground))' },
 *     destructive: { DEFAULT: 'hsl(var(--destructive))', foreground: 'hsl(var(--destructive-foreground))' },
 *   }
 *
 * TODO: converter os hex acima para os valores HSL exatos da marca TradeRisk.
 */
