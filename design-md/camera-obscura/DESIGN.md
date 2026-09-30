---
version: alpha
name: "Camera Obscura"
source_url: "https://cameraobscurafilms.de/"
captured_at: "2026-09-29T04:12:13.289746+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Camera Obscura Filmdistribution is a German boutique Blu-ray/UHD label
  (Shopify-powered storefront) specializing in Mediabook editions of cult,
  arthouse, and horror cinema. The site's root CSS variables define a
  consistent dark, film-grain-adjacent palette: a near-black warm brown
  canvas (#16120a), a cream/parchment foreground for text and headings
  (#eadac0), and a muted gold-amber accent (#daa838) reused across buttons,
  links, and focus shadows. This restrained three-tone system reads as
  "vintage print label on dark stock," fitting a distributor whose product
  is physical collector packaging (Cover A/B/C mediabooks) rather than
  streaming content.
  Two font families are present in the served CSS: Aleo (a slab/serif
  display face) is inferred here as the heading family for its literary,
  editorial character, and Inter is inferred as the body/UI family for
  legibility in dense catalog grids. This mapping is inferred from font
  stack order and typical Shopify theme convention, not from a directly
  observed heading render.
  Secondary neutrals (#1c1c1c, #2c332f, #3f5147, #716a56) appear elsewhere
  in the supplied palette without confirmed role declarations; they are
  reused here as inferred card/hairline surfaces layered over the dark
  canvas to give product tiles and price badges separation without
  introducing new colors. Payment-network and cookie-consent-widget colors
  (e.g. #007bbc, #eb001b, #0071ce) are excluded from brand roles as
  third-party UI, not storefront branding.

colors:
  primary: "#daa838"
  ink: "#eadac0"
  canvas: "#16120a"
  body: "#eadac0"
  muted: "#716a56"
  hairline: "#3f5147"
  surface-soft: "#2c332f"
  surface-card: "#1c1c1c"
  on-primary: "#eadac0"
  on-secondary: "#daa838"
  badge-bg: "#16120a"
  badge-border: "#eadac0"
typography:
  display-xl: {fontFamily: "Aleo, serif", fontSize: 44px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.4px}
  display-md: {fontFamily: "Aleo, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0.4px}
  title-md: {fontFamily: "Aleo, serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.4px}
  body-md: {fontFamily: "Inter, -apple-system, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 1px}
  body-sm: {fontFamily: "Inter, -apple-system, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0.6px}
  caption: {fontFamily: "Inter, -apple-system, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.6px}
  button-md: {fontFamily: "Inter, -apple-system, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.8px}
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
    textColor: "{colors.on-secondary}"
    border: "1px solid {colors.primary}"
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
    padding: "{spacing.sm} {spacing.xl}"
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  price-tag:
    originalPriceColor: "{colors.muted}"
    salePriceColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    strikethrough: true
  hero:
    backgroundColor: "{colors.canvas}"
    overlayColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.badge-bg}"
    border: "1px solid {colors.badge-border}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"

## Components

**button-primary** renders on the observed `--color-button` gold with cream `--color-button-text`, matching the theme's own root variables; used for "In den Warenkorb" and checkout CTAs.

**button-secondary** is a ghost/outline variant using canvas background with a gold border and gold text, mirroring the theme's `--color-secondary-button` pairing; proposed for "Alle anzeigen" and filter actions.

**text-input** is proposed for the newsletter email field seen in the excerpt; dark card surface with a hairline border keeps it legible on the near-black canvas, though exact focus/error states were not observed.

**nav-bar** covers the top utility row (KATALOG, DEMNÄCHST, EXKLUSIV, MERCHANDISE, NEWS, ÜBER UNS) plus language/login/cart icons; a bottom hairline separates it from hero content, proposed rather than measured.

**product-card** models the repeating Mediabook tiles (title, "Anbieter" format label, price) seen across NEUHEITEN and BESTSELLER grids; dark card surface distinguishes tiles from the canvas.

**price-tag** is a category-specific component addressing the site's "Normaler Preis" / "Verkaufspreis" pattern on discounted Bestseller items — muted strikethrough original price beside a gold sale price.

**hero** is proposed for a top banner slot, using the same canvas/soft-surface relationship as the rest of the page since no distinct hero markup was present in evidence.

**footer** reflects the observed footer text list (Widerrufsrecht, Datenschutzerklärung, AGB, Versand, Impressum, payment methods, social icons) in muted body copy with gold links.

**badge** is proposed for labels like "Reduziert" or "EXKLUSIV" prefixes seen in product titles, using the theme's own `--color-badge-*` variables.

**search** is proposed for catalog filtering; no search-specific markup was in the supplied evidence, so styling follows the general input pattern.

## Responsive Behavior

| Breakpoint | Range | Layout guidance (proposed) |
|---|---|---|
| Mobile | <600px | Single-column product grid, collapsed nav behind a menu toggle, stacked footer links |
| Tablet | 600–1024px | 2–3 column product grid, nav condenses secondary items |
| Desktop | >1024px | Full horizontal nav, 4+ column product grid, persistent newsletter module in footer |

Touch targets for buttons and nav items should be at least 44px tall. Nav collapse behavior, sticky header state, and cart-drawer interaction were not observed and are recommendations only, not measured site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Extraction is static CSS/text only; no rendered screenshots, computed layout, or JS-driven states (hover, focus, cart drawer, mobile menu) were observed.
- Heading/body font-family assignment (Aleo vs. Inter) is inferred from stack order and common Shopify theme convention, not from a directly rendered heading sample.
- Root font-size scaling (theme often sets `html { font-size: X% }`) was not supplied, so the `1.5rem` body-text value's real pixel size is uncertain; body-md size above is a proposed approximation.
- Border-radius values (`--buttons-radius-outset`, `--product-card-corner-radius`) are theme variables whose resolved values were not present in evidence; the `rounded` scale is fully proposed.
- Several neutral colors (#1c1c1c, #2c332f, #3f5147, #716a56, #dedede, #f3f4f6, etc.) appear in the supplied palette without an explicit role declaration; their use here as surfaces/hairlines is inferred, not confirmed.
- Payment-network icon colors (Visa/Mastercard/PayPal) and the Iubenda cookie-consent widget colors (#007bbc, #0a0a0a, #ffffff) are third-party UI, excluded from brand role mapping.
- Custom font licensing/availability (Aleo, Inter) for production use was not verified from this evidence.
