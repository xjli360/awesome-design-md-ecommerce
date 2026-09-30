---
version: alpha
name: "Taza Chocolate"
source_url: "https://tazachocolate.com"
captured_at: "2026-09-28T10:04:02.459635+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Taza's observed palette centers on a warm ivory canvas (#fff9eb, defined as
  --color-background) paired with a near-black ink (#121212, --color-foreground
  and --color-button) for primary text and buttons, with white (#ffffff) as
  button-text and card surfaces. A cluster of muted blues (#467c99, #38637a,
  #90b0c2, #1990c6, #136f99) and softer tints (#b5cbd6, #d1dee6, #e3ebf0)
  appear alongside a warm rust (#ac532b), a golden yellow (#fed74d, matching
  the declared --color-background-contrast), a pale blush (#f7cbda), and a
  pale mint (#deebe7). These are treated here as inferred secondary/accent
  roles (flavor tags, category chips, seasonal callouts) since the supplied
  CSS shows only their existence as custom-property values, not confirmed
  usage context. Typography uses Roboto Condensed for headers (7.2rem/3.2rem
  rules) and Roboto for body copy (1.8rem, letter-spacing 0.06rem), both
  loaded with sans-serif fallback; no proprietary or licensed font is
  claimed. The interpretation favors a rustic-craft aesthetic: cream
  backgrounds, high-contrast ink type, condensed display headlines for bold
  product callouts, and restrained blue/rust/yellow accents echoing the
  brand's stone-ground, direct-trade positioning. Card and section geometry,
  spacing scale, and breakpoints below are proposed conventions, not measured
  layout observations.

colors:
  primary: "#121212"
  ink: "#121212"
  canvas: "#fff9eb"
  body: "#121212"
  muted: "#6b96ad"
  hairline: "#dedede"
  surface-soft: "#f9f8f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#fed74d"
  accent-blush: "#f7cbda"
  accent-mint: "#deebe7"
  brand-blue: "#467c99"
  brand-blue-dark: "#38637a"
  brand-blue-light: "#90b0c2"
  link-blue: "#1990c6"
  rust: "#ac532b"
  shadow: "#0000000d"
typography:
  display-xl: {fontFamily: "Roboto Condensed, sans-serif", fontSize: 72px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Roboto Condensed, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Roboto Condensed, sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.44, letterSpacing: 1px}
  body-sm: {fontFamily: "Roboto, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  caption: {fontFamily: "Roboto, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.4px}
  button-md: {fontFamily: "Roboto, sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    shadow: "{colors.shadow}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  cacao-percentage-tag:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components
**button-primary**: Solid ink-on-cream call to action (e.g. "SHOP NOW", "Check out"), mapped from the confirmed `--color-button: 18,18,18` / `--color-button-text: 255,255,255` custom properties. Hover/active states are proposed, not observed.

**button-secondary**: Outlined variant for secondary actions ("Continue shopping", "Learn More") using the cream secondary-button background and ink text/border declared in `--color-secondary-button`. Proposed for lower-emphasis CTAs beside a primary button.

**text-input**: Cart, checkout, and email-signup fields, styled with a light hairline border and card-white background inferred from the site's light, minimal aesthetic; no explicit input CSS was supplied.

**nav-bar**: Cream sticky header holding the Shop/About/Visit menu groups and cart/search icons seen in the text excerpt; typography and spacing are proposed conventions since header CSS beyond font-family variables was not supplied.

**product-card**: Bar/disc/snack listing tile (title, price "From $ X.99", unit price) inferred from the Best Sellers text list; white surface and subtle border proposed to separate cards on the cream canvas.

**hero**: Large condensed headline ("STONE GROUND CHOCOLATE") over cream background, matching the 7.2rem header rule found in `.fresh-header` selectors; used for the homepage intro and campaign banners.

**footer**: Dark ink background with white text, matching the `.fresh-header--header_fndHNy` / `.fresh-body--body_d6hBiL` rules that set `color: #ffffff`, holding newsletter signup, social links, and legal/policy link list.

**badge**: Small pill label (e.g. "Non-GMO", "Direct Trade", "Vegan") using an outlined ink-on-cream treatment; states such as filled/success are proposed, not confirmed by CSS.

**search**: Overlay or inline search field triggered by the header "Search" control referenced in the page text; input styling proposed to match text-input.

**cacao-percentage-tag**: Category-specific chip (e.g. "70%", "55% Dark") for flavor/cacao-content labeling on product cards and collection filters, using the yellow accent (`#fed74d`) tied to `--color-background-contrast` for visual distinction from standard badges.

## Responsive Behavior
Proposed breakpoints (not measured from live site):

| Breakpoint | Width      | Layout notes (proposed) |
|-----------|------------|--------------------------|
| Mobile    | 0–599px    | Single-column product grid, collapsed hamburger nav, stacked hero text |
| Tablet    | 600–959px  | 2-column product grid, condensed nav with icon-only search/cart |
| Desktop   | 960–1279px | 3–4 column product grid, full horizontal nav |
| Wide      | 1280px+    | 4+ column grid, max-width content container |

Touch targets should be a minimum of 44×44px for cart/nav icons. Navigation is assumed to collapse into a hamburger/drawer pattern below tablet width. These are standard e-commerce conventions applied to the observed component set, not confirmed interaction behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Color roles beyond the explicitly named CSS custom properties (`--color-background`, `--color-foreground`, `--color-button`, etc.) are inferred from hex presence only; blues, blush, mint, rust, and yellow accent usage/context is unconfirmed.
- No responsive CSS (media queries), grid, or flex layout rules were supplied; all breakpoint and grid-column figures above are proposed, not measured.
- Font weights for Roboto/Roboto Condensed beyond the single `font-weight: 700` button rule are assumed; actual weight availability and licensing were not verified.
- No hover, focus, active, disabled, or error states were present in the supplied CSS; all interaction states in this document are proposed.
- Mobile/tablet layout, navigation collapse behavior, and touch-target sizing were not observed and are recommended conventions only.
- Spacing and rounded-corner scales are proposed design-system values, not extracted from the supplied CSS, which contained no margin/padding/border-radius declarations.
