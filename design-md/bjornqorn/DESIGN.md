---
version: alpha
name: "BjornQorn"
source_url: "https://bjornqorn.com"
captured_at: "2026-09-29T04:04:47.343398+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  BjornQorn is a Shopify-hosted popcorn/snack storefront built on a plain-goods
  aesthetic: white canvas, black body text, and a single high-visibility yellow
  accent (#f0ea1d) used for primary buttons and header-bar backgrounds. A dark
  green (#03684a) appears explicitly as the secondary-button background in the
  observed CSS, giving the brand a two-color commerce system (yellow action,
  green alternate action) against black-on-white content. Typography is a
  single observed sans stack, Montserrat with HelveticaNeue/Helvetica Neue
  fallbacks, used uniformly for body copy, headings, and buttons at a small
  15px base size with generous 1.7 line-height, consistent with a dense
  product-grid storefront rather than an editorial site.

  Border/hairline gray (#808080) and disabled grays (#f6f6f6, #b6b6b6) are
  taken directly from CSS custom properties and disabled-button rules. Roles
  beyond primary/secondary buttons and header bar are inferred: card surfaces,
  hover states, and section rhythm are proposed extrapolations for a
  chips/snacks catalog with many SKUs (Classic, Spicy, Cloudy, Maple, Earth,
  Ruby), bundles, and light apparel cross-sell, not measured page layout.

colors:
  primary: "#f0ea1d"
  primary-hover: "#f0ea1dcc"
  secondary: "#03684a"
  secondary-dark: "#024f38"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#555555"
  hairline: "#808080"
  surface-soft: "#f6f6f6"
  surface-card: "#f9fafb"
  on-primary: "#000000"
  on-secondary: "#ffffff"
  border-light: "#cccccc"
  disabled-text: "#b6b6b6"
  disabled-bg: "#f6f6f6"
  danger: "#d02e2e"
typography:
  display-xl: {fontFamily: "Montserrat, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.4, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  title-md: {fontFamily: "Montserrat, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  body-md: {fontFamily: "Montserrat, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.7, letterSpacing: 0px}
  body-sm: {fontFamily: "Montserrat, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.7, letterSpacing: 0px}
  caption: {fontFamily: "Montserrat, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Montserrat, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.42, letterSpacing: 0px}
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
    padding: "{spacing.sm} {spacing.base}"
    hover: "backgroundColor: {colors.primary-hover}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    hover: "proposed backgroundColor: {colors.secondary-dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.base}"
    borderBottom: "1px solid {colors.border-light}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    border: "1px solid {colors.border-light}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.base}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid transparent"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.md}"
  flavor-swatch:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.border-light}"
    rounded: "{rounded.full}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.md}"

## Components

**button-primary** — The yellow (#f0ea1d) filled button is the confirmed primary action style from the theme CSS, used for "Buy" and add-to-cart style actions, with a lighter hover tint (#f0ea1dcc) also directly observed.

**button-secondary** — A dark green (#03684a) background is explicitly declared for `.btn--secondary`. Hover-state darkening to #024f38 is proposed by analogy, as no secondary hover rule was captured.

**text-input** — Search and form fields are inferred to follow the flat, low-radius (2px) style seen on buttons and the header search box, with the observed #808080 border variable applied as a hairline.

**nav-bar** — The `.header-bar` class confirms a white background, black text/links, and small (~14px) Montserrat type; the full storefront nav (logo, mega-menu) beyond this bar is proposed, not observed in the CSS excerpt.

**product-card** — Given the many SKU listings (Classic, Ruby, Spicy, Cloudy, Maple, Earth, Mix Pack) at fixed price points, a card pattern with a light surface, thin border, and stacked title/price is proposed to organize the catalog; no card-specific selector was present in evidence.

**hero** — A large introductory band using the display typography scale is proposed for the homepage; no hero-specific CSS was supplied, so sizing and imagery treatment are inferential.

**footer** — Footer link groups (Press, Wholesale, Accessibility, Terms, Returns, Privacy) are evidenced in page text; the muted-gray, hairline-topped styling is a proposed treatment consistent with the site's restrained palette.

**badge** — A rounded yellow "NEW!" tag (referencing the "NEW! BjornQorn Ruby" text) is proposed using the primary color at small caption size, since promotional badges are common in this catalog but no dedicated selector was observed.

**flavor-swatch** — Given the flavor-driven product line, a pill-shaped swatch component is proposed for filtering/labeling flavors (Classic, Spicy, Cloudy, Maple, Earth, Ruby) on listing pages; this is a category-appropriate addition, not derived from a captured selector.

## Responsive Behavior
Recommended, not measured:

| Breakpoint | Width      | Layout guidance                          |
|-----------|-----------|-------------------------------------------|
| sm        | 0–599px   | Single-column stack; nav collapses to menu icon |
| md        | 600–959px | 2-column product grid; header-bar sep visible |
| lg        | 960–1279px| 3-column product grid; inline nav          |
| xl        | 1280px+   | 4-column product grid; wider hero padding  |

Touch targets should be at least 44px tall; buttons using `{spacing.sm} {spacing.lg}` padding should be checked against this minimum on small screens. Nav collapse and mobile menu behavior are proposed patterns; no mobile markup or media queries were included in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is built from static CSS/text extraction only; no rendered layout, mobile view, or interaction states (focus, active, animation) were observed. Several `:root` custom properties (`--color-accent`, `--color-main-background`, `--font-heading`, `--font-body`) were empty in the source and have been inferred from concrete rule usage elsewhere (e.g., button and header-bar colors) rather than measured directly. Card, hero, badge, and flavor-swatch components are proposed for category fit and are not backed by matching selectors in evidence. Montserrat's licensing/self-hosting and actual font-loading behavior were not verified. All spacing and rounded scale values beyond the confirmed 2px button radius are proposed conventions, not extracted measurements.
