---
version: alpha
name: "Finn + Emma"
source_url: "https://finnandemma.com"
captured_at: "2026-09-28T04:53:16.485483+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Finn + Emma is a Shopify-hosted organic baby apparel and toy retailer. The
  observed CSS custom properties define a warm, muted palette: a soft ecru
  canvas (#f7f4ed) paired with a dark warm-gray ink (#383734) used for both
  foreground text and the primary button. This ink-on-ecru pairing reads as
  quiet, natural, and organic-cotton-adjacent rather than high-contrast retail.
  A terracotta accent (#945e45) appears in the palette and is inferred here as
  a secondary brand accent for callouts or hover states, since its concrete
  usage role was not confirmed in the supplied rules. A distinct blue
  (#1990c6, hover #136f99) is confirmed as the Shopify accelerated-checkout
  button color, and a gold (#ebbf20) is confirmed as the review-star icon
  color. Card and section surfaces are proposed from lighter near-white grays
  in the palette (#f4f0eb, #fafaf9, #ffffff) since exact background-per-
  component values were not itemized in the evidence.

  Typography includes two distinctive named families ("Catchy Mager" and
  "TAN - MON CHERI") alongside conventional web sans fonts (Poppins, Jost,
  Nunito, Open Sans, Inter, Helvetica). The exact CSS-variable-to-role mapping
  (which family serves --font-heading-family vs --font-body-family) was not
  present in the supplied evidence, so all family-to-role assignments below
  are inferred and should be treated as proposed, not confirmed, typography.

colors:
  primary: "#383734"
  ink: "#383734"
  canvas: "#f7f4ed"
  body: "#6e6e6e"
  muted: "#949494"
  hairline: "#dedede"
  surface-soft: "#f4f0eb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#945e45"
  accent-blue: "#1990c6"
  accent-blue-hover: "#136f99"
  rating: "#ebbf20"
  danger: "#f21111"
typography:
  display-xl: {fontFamily: "'TAN - MON CHERI', serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Catchy Mager', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Jost, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.06rem}
  body-sm: {fontFamily: "'Open Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.02rem}
  caption: {fontFamily: "Nunito, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.04rem}
  button-md: {fontFamily: "Helvetica, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.04rem}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    ratingColor: "{colors.rating}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.md}"

## Components

**button-primary** uses the confirmed ink color (#383734) as background with white text, matching the observed `--color-button` / `--color-button-text` variables. Radius is proposed since `--buttons-radius-outset` value was not itemized.

**button-secondary** inverts the primary treatment (ecru background, ink border and text), mirroring the observed `--color-secondary-button` variables. Hover/focus states are proposed, not observed.

**text-input** is a proposed pattern for newsletter and account forms; surface, hairline border, and radius are inferred defaults consistent with the theme's soft, low-contrast aesthetic.

**nav-bar** reflects the deep navigation structure evidenced in the page text (Apparel, Gear + Toys, Gifts, age/gender mega-menus). Layout (sticky, mega-menu columns) is proposed; only color/typography roles are grounded in evidence.

**product-card** is proposed for the categories referenced in navigation (Footies, Onepieces, Dresses, Booties). Card background, corner radius, and shadow rely on CSS custom properties (`--product-card-corner-radius`, `--product-card-shadow-*`) whose resolved values were not supplied, so treatment is a reasonable default.

**hero** proposes a soft-surface banner suited to a lifestyle/organic-goods homepage, pairing the decorative display font with a primary CTA button. Imagery, overlay, and copy are not observed.

**footer** is proposed as a dark ink-background footer for contrast against the light site body, holding utility links (currency selector, holiday shop links) noted in the page text. Multi-column layout is inferred, not observed.

**badge** supports labels such as "Organic," "New," or "Sale," using an outlined pill treatment consistent with the badge CSS variables observed (`--color-badge-*`).

**search** is a proposed input treatment for the site's search affordance noted in navigation text; no distinct search-specific CSS was supplied.

**filter-chip** is the category-appropriate component for baby apparel: toggleable pills for Gender (Girl/Boy/Gender Neutral) and Age (Toddler) filters referenced directly in the navigation text. State colors are proposed, not observed in interaction.

## Responsive Behavior
This is a recommended breakpoint structure, not measured site behavior:

| Breakpoint | Width      | Nav                         | Product grid |
|-----------|------------|------------------------------|--------------|
| Mobile    | <600px     | Collapsed hamburger + drawer | 1–2 columns  |
| Tablet    | 600–959px  | Condensed horizontal nav     | 2–3 columns  |
| Desktop   | ≥960px     | Full mega-menu nav           | 3–4 columns  |

Touch targets should be a minimum 44px height (matching the observed `clamp(25px, 44px, 55px)` accelerated-checkout button sizing). Mega-menus (Apparel, Gear + Toys, Gifts) should collapse into accordion sections on mobile; this collapse behavior is proposed and was not observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS variables and text content only; no rendered layout, computed styles, or JavaScript-driven interaction states were observed. The mapping of `--font-heading-family` and `--font-body-family` to specific named fonts (Catchy Mager, TAN - MON CHERI, Poppins, Jost, Nunito, Open Sans, Inter, Helvetica) was not present in the supplied CSS and is inferred by convention; actual role assignment may differ. The `--color-background-contrast` value (rgb 208,190,149) did not correspond to a supplied hex swatch and was therefore omitted from the token set. Corner-radius and shadow values for buttons and product cards reference undefined CSS custom properties, so all `rounded` values are proposed defaults, not extracted measurements. Hover, focus, error, and mobile-drawer interaction states are proposed patterns, not observed behavior. Availability and licensing of the two proprietary display fonts have not been verified.
