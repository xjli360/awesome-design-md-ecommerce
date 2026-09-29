---
version: alpha
name: "Dremel"
source_url: "https://dremel.com"
captured_at: "2026-09-29T03:57:41.698740+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Dremel's site CSS evidence shows a utilitarian, high-contrast industrial-tool palette built on white canvases, near-black ink (#000, #232628), and a cool desaturated gray-blue neutral scale (#c1c7cc, #a4abb3, #71767c, #eff1f2) used for hairlines and soft surfaces. A steel blue (#005293, with darker #004975/#004276 variants) appears repeatedly as the interactive/link and hover color on gallery arrows and commerce buttons, so it is inferred here as the primary brand action color. Bright signal reds (#ed0007, #d50005) mark sale pricing and destructive/error states; a green pair (#006c3a on #e2f5e7) and amber pair (#806700 on #ffefd1) appear in modal headers, inferred as success and warning semantics respectively. Typography is set in the proprietary "boschsans" family with Helvetica Neue/Helvetica/Arial/sans-serif fallbacks, base 1rem body copy at 1.5 line-height — consistent with a functional, spec-driven power-tool retailer rather than a lifestyle brand. This interpretation proposes a rugged, information-dense UI: flat surfaces, small-radius controls, tight hairline dividers, and a restrained accent palette reserved for pricing, alerts, and calls to action, leaving neutrals to carry the bulk of the product-catalog and support-content layout.

colors:
  primary: "#005293"
  primary-dark: "#004975"
  ink: "#000000"
  body: "#232628"
  canvas: "#ffffff"
  muted: "#71767c"
  hairline: "#c1c7cc"
  surface-soft: "#eff1f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#ed0007"
  error: "#d50005"
  error-surface: "#ffecec"
  success: "#006c3a"
  success-surface: "#e2f5e7"
  warning: "#806700"
  warning-surface: "#ffefd1"
  border-strong: "#a4abb3"
  neutral-700: "#43464a"
typography:
  display-xl: {fontFamily: "boschsans, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "boschsans, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "boschsans, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0}
  body-md: {fontFamily: "boschsans, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0}
  body-sm: {fontFamily: "boschsans, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0}
  caption: {fontFamily: "boschsans, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.1px}
  button-md: {fontFamily: "boschsans, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.2px}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  none: 0px
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  base: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 64px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    height: "64px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    salePriceColor: "{colors.accent-red}"
  price-display:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    saleColor: "{colors.accent-red}"
    strikethroughColor: "{colors.neutral-700}"
    typography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.body}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.success-surface}"
    textColor: "{colors.success}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** is proposed as the steel-blue (`{colors.primary}`) fill with white text, matching the observed hover color on gallery arrows and the "Buy from Bosch" commerce link; used for cart, checkout, and primary CTAs like "Shop Now." Hover/pressed darkening to `{colors.primary-dark}` is proposed, not measured.

**button-secondary** is an outlined variant using the same primary blue for border/text on a transparent background, intended for lower-emphasis actions ("Learn more," "Explore rotary"). Focus and hover fills are proposed states, unobserved in the supplied CSS.

**text-input** follows generic form-field conventions: white background, hairline gray border, and body typography, since no dedicated input CSS was supplied — sizing and border color are inferred from the neutral palette.

**nav-bar** is inferred from the site's mega-menu structure implied by "Products / Shop / Projects / Service & Support" navigation text; a white bar with hairline underline is proposed since no header-specific styles were present in evidence.

**product-card** draws on the `ProductDisplayPrice` and `TableCell` classes: a bordered white card with title, spec, and price rows, where sale pricing switches to `{colors.accent-red}` as directly observed in `.ProductDisplayPrice_red__WmvmT`.

**price-display** isolates the observed pricing color logic (black base price, red sale price, gray strikethrough at 12px) into a reusable pattern for list and detail views, appropriate for a tool-catalog storefront.

**hero** is a proposed full-width banner pattern (e.g., "Carve Your Best Pumpkin Yet") using the soft neutral surface as background with large display type; exact hero styling was not present in the supplied CSS rules.

**footer** is inferred as a dark, information-dense block given the long link inventory (Manuals, Warranty, Careers, Newsroom); dark ink background with white text is proposed for contrast, not confirmed by supplied selectors.

**badge** reuses the modal success token pair (`#e2f5e7`/`#006c3a`) as a pill-shaped status indicator, suitable for "In Stock" or "New" labels on product tiles.

**search** is a proposed soft-surface input with rounded corners for the site's product/accessory finder tools (e.g., "Dremel Accessories Guide"), styled consistently with the neutral surface tokens.

## Responsive Behavior

The following breakpoint table is a **recommendation**, not measured site behavior, since no media queries were included in the supplied CSS:

| Breakpoint | Width      | Layout notes (proposed) |
|-----------|------------|--------------------------|
| mobile    | 0–599px    | Single-column stacks, collapsed hamburger nav, full-width buttons |
| tablet    | 600–959px  | 2-column product grids, condensed nav labels |
| desktop   | 960–1279px | 3–4 column product grids, full mega-nav |
| wide      | 1280px+    | Max-width content container, 4+ column grids |

Touch targets should be a minimum 44×44px for buttons and nav items (proposed, WCAG-aligned convention). Navigation is expected to collapse into a drawer or accordion below tablet width; this is a UX convention assumption, not an observed interaction.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- All CSS was extracted statically from bundled stylesheet fragments; no rendered DOM, computed styles, or JavaScript-driven states were captured.
- Semantic role mapping (primary, muted, hairline, surface-soft, etc.) is inferred from class-name context (e.g., modal headers, price colors) and may not reflect the site's actual design-token naming or full intended usage.
- Typography scale sizes beyond the observed `body { font-size:1rem; line-height:1.5 }` are proposed estimates for a tool-retail hierarchy, not measured from headings or components.
- Hero, nav-bar, footer, search, and button hover/focus states are proposed patterns based on common e-commerce conventions and page-text structure, not verified from layout or interaction CSS.
- Mobile/tablet layout behavior, breakpoints, and touch-target sizing are recommendations only; no responsive CSS rules were included in the supplied evidence.
- The "boschsans" font is a proprietary Bosch Group typeface; its availability, licensing, and exact weight/style variants were not verified — fallbacks (Helvetica Neue, Helvetica, Arial, sans-serif) are used as observed in the CSS `font-family` declaration.
- Rounded and spacing scales are proposed conventional systems, not derived from explicit `border-radius` or spacing values in the supplied CSS rules.
