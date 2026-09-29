---
version: alpha
name: "Henry Street Studio"
source_url: "https://henrystreetstudio.com"
captured_at: "2026-09-29T04:05:31.962507+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  The available evidence for Henry Street Studio is limited to Squarespace
  platform CSS (cookie-banner and tooltip utility rules) rather than
  brand-authored page styling, so this interpretation is deliberately
  restrained and neutral. The observed palette is dominated by grayscale
  values (#ffffff, #111111, #222222, #272727, #3e3e3e, #999999, #dddddd,
  #f6f6f6), which are used here as ink, body, muted, hairline, and surface
  roles — all inferred, since no rule explicitly labels a "brand" color.
  Bright hues in the raw palette (social-network blues, reds, pinks) belong
  to Squarespace's social-icon font and are excluded as non-brand system
  colors. Typography draws on the directly observed body stack
  (font-family: sans-serif; color: #222) and the cookie-banner stack
  ('Helvetica Neue', Helvetica, sans-serif), with Georgia used as an
  inferred serif display option since it appears in the site's loaded font
  list, suiting a handmade, mother-daughter ceramics studio's understated,
  paper-and-clay aesthetic. Button and caption sizing (11px uppercase
  buttons, 12px tracked captions) are taken directly from observed tooltip
  and banner rules. The resulting system favors quiet neutrals, generous
  whitespace, and unobtrusive UI chrome appropriate to a small Brooklyn
  ceramics studio's product photography.

colors:
  primary: "#272727"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#999999"
  hairline: "#dddddd"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border-strong: "#3e3e3e"
  overlay-dark: "#000000"
typography:
  display-xl: {fontFamily: "Georgia, serif", fontSize: "48px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Georgia, serif", fontSize: "32px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "0px"}
  title-md: {fontFamily: "'Helvetica Neue', Helvetica, sans-serif", fontSize: "20px", fontWeight: 500, lineHeight: 1.3, letterSpacing: "0.2px"}
  body-md: {fontFamily: "sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0px"}
  body-sm: {fontFamily: "sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'Helvetica Neue', Helvetica, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: "1.5em", letterSpacing: "0.05em"}
  button-md: {fontFamily: "sans-serif", fontSize: "11px", fontWeight: 500, lineHeight: "22px", letterSpacing: "0.5px", textTransform: "uppercase"}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border-bottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
    border-top: "1px solid {colors.border-strong}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    border: "1px solid {colors.hairline}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  gallery-tile:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.sm}"

## Components

**button-primary** uses the dark neutral `#272727` as an inferred brand-action color (no confirmed accent hue exists in the evidence), paired with the directly-observed 11px uppercase, letter-spaced button typography from the tooltip CSS. Hover/active states are proposed, not observed.

**button-secondary** offers a lighter, bordered alternative for less prominent actions (e.g., "Add to wishlist"), reusing the same button typography with a hairline border and soft surface background — a common low-emphasis pattern, proposed here.

**text-input** is a plain bordered field using the observed hairline gray (`#dddddd`) and body sans-serif type, suited to a minimal contact/FAQ form; focus and error states are proposed and unobserved.

**nav-bar** is inferred as a simple horizontal bar (the page text lists "henry street studio contact FAQ Menu" twice, suggesting a compact top nav plus a collapsed menu trigger) on a white canvas with a hairline bottom border; no scroll or sticky behavior was observed.

**product-card** anticipates a grid of handmade ceramic pieces, using a card surface, hairline border, and a title/price typographic pairing; imagery, hover zoom, or quick-view states are proposed, not confirmed.

**hero** proposes a large display-type introduction on the soft surface tone, referencing the site's own tagline ("Handmade ceramics from a Brooklyn based mother-daughter team"); actual hero imagery, cropping, or overlay treatment were not observed.

**footer** is inferred as a dark, high-contrast band (using ink and on-primary tokens) for closing navigation/social links, consistent with the "Powered by Squarespace" credit line present in the page text; actual footer structure is unconfirmed.

**badge** is a small pill label (e.g., "Sold Out," "New") using the caption typography directly observed in the cookie-banner CSS; this is a proposed reuse for merchandising, not a confirmed UI element.

**search** and **gallery-tile** are proposed, category-appropriate components: a pill-shaped search field for product lookup, and a bordered gallery tile for showcasing individual ceramic pieces with a caption — both extrapolated from typical small-studio storefront needs rather than observed markup.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width       | Behavior (proposed)                          |
|-----------|-------------|-----------------------------------------------|
| mobile    | < 600px     | Single-column stack; nav collapses to menu icon |
| tablet    | 600–1024px  | 2-column product grid; nav remains horizontal   |
| desktop   | > 1024px    | 3–4 column product grid; full nav visible       |

Touch targets should be at least 44×44px for buttons and nav items. The nav-bar's "Menu" label suggests a collapsible mobile menu pattern, but its exact trigger, animation, and breakpoint were not observed and are inferred from convention only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence consists almost entirely of generic Squarespace platform CSS (cookie-banner and tooltip utility rules), not page-specific or brand-authored styles; no hero, nav, or product-card markup was directly observed.
- No distinct brand accent color was identifiable in the evidence; bright hues in the raw palette are Squarespace social-icon-font colors and were excluded as non-brand.
- Font roles (Georgia for display, sans-serif/Helvetica Neue for body) are inferred from the site's loaded font list and the one directly observed body rule; actual heading font usage was not confirmed.
- Font licensing/availability for Clarkson, futura-pt, proxima-nova, and Oswald (listed in the site's font stack but not tied to any supplied rule) was not verified.
- All spacing, rounding, and sizing values beyond the directly observed 11px button/12px caption rules are proposed conventions, not measured layout.
- No interaction states (hover, focus, active, mobile menu open/close) were observed; all are proposed defaults.
- No confirmation of actual product grid, checkout, or cart UI was possible from the supplied evidence.
