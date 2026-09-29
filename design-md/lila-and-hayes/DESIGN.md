---
version: alpha
name: "Lila & Hayes"
source_url: "https://lilaandhayes.com"
captured_at: "2026-09-29T04:33:44.774810+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Lila & Hayes presents itself as a Southern-preppy family apparel label built on Pima cotton, monogramming, and seasonal "collection drop" merchandising (Fall, Game Day, Preppy Pumpkins). The observed CSS exposes a navy-blue theme family — {colors.primary} "#3b5789" alongside related steps "#203450" and "#4b6ca0" — used consistently across header, line, and button custom-property groups (--colors-text-header, --colors-line-header, --colors-button), which is why navy is treated as the brand's structural color rather than the many app-injected hues also present in the palette (Loop Returns' "#3256e5"/grays, Swym wishlist teals like "#2cb29b"/"#1990c6", and generic Tailwind neutrals such as "#374151"/"#d1d5db"). Those third-party colors are excluded from brand claims. Neutrals lean on a near-black body ink "#282928," a warm mid-gray "#767474," and very light blue-tinted surfaces "#eff2f7"/"#f9fafb," giving a soft, laundered, catalog-like canvas typical of children's apparel photography.

  Typography mixes a classic serif — "big-caslon-fb" with "Playfair Display" as a secondary serif — for headings, against a geometric sans ("futura-pt"/"untitled sans") for body and UI copy; the sticky header forces --font-body-weight: 700, supporting bold, likely uppercase navigation. A distinct script face, "CafeParadis-SlantedScript," appears only for monogram-preview purposes and is treated as a special-purpose asset, not part of the core type scale. A red accent ("#bf122a") is proposed for sale/bestseller badges but is unverified as an official brand color.

colors:
  primary: "#3b5789"
  primary-deep: "#203450"
  primary-mid: "#4b6ca0"
  ink: "#282928"
  body: "#767474"
  muted: "#9ca3af"
  hairline: "#e5e7eb"
  surface-soft: "#eff2f7"
  surface-card: "#f9fafb"
  surface-alt: "#ececec"
  on-primary: "#ffffff"
  canvas: "#ffffff"
  accent-sale: "#bf122a"
typography:
  display-xl: {fontFamily: "'big-caslon-fb', 'Playfair Display', serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'big-caslon-fb', 'Playfair Display', serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "'futura-pt', 'untitled sans', sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0.2px}
  body-md: {fontFamily: "'untitled sans', 'futura-pt', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'untitled sans', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'untitled sans', Arial, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "'untitled sans', 'futura-pt', Arial, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.6px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    hairlineBottom: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    badgeBackground: "{colors.accent-sale}"
    badgeTextColor: "{colors.on-primary}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaButton: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  monogram-personalizer:
    backgroundColor: "{colors.surface-card}"
    accentTextColor: "{colors.primary}"
    labelTypography: "{typography.caption}"
    previewFont: "'CafeParadis-SlantedScript', cursive"
    border: "1px dashed {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"

## Components
**button-primary** maps to the theme's `--colors-button`/`--colors-button-text` pair confirmed in `.button-solid` and `.button-action` rules; used for "Add to Cart," "Shop Now," and newsletter sign-up actions.

**button-secondary** is a proposed outline variant using the same navy for text/border on a white fill, intended for secondary CTAs like "View All Products" where a solid button would compete with the primary action.

**text-input** covers newsletter and account-form fields; border color and radius are proposed conventions since no explicit input CSS was supplied.

**nav-bar** reflects the header's scoped custom properties (`.header` overriding `--colors-text`/`--colors-line-and-border`) and the sticky header's bold (700-weight) body font, supporting the observed all-caps category list (GIRLS, BOYS, LH SPORT, WOMEN, MEN, GIFTS, MONOGRAMS, SALE).

**product-card** is inferred from the repeated bestseller/personalize-it labeling pattern in the page text; badge color uses the unverified sale-red accent.

**hero** is a proposed pattern for the "Game Day Color Sale" / "New Arrivals: Fall Collection" promotional banners referenced in the announcement bar text.

**footer** uses the deep navy step as background, matching the multi-shade navy family, for the "Let's Stay in Touch!" sign-up region and utility link list (Size Chart, FAQ, Returns and Exchanges, Wholesale Inquiries).

**badge** is a small rounded label for "bestseller," "NEW!," and sale callouts seen throughout the product grid text.

**search** is a proposed header/utility search field pattern; no dedicated search CSS was in evidence.

**monogram-personalizer** is a category-specific proposed component for the "personalize it!" flow tied to monogrammed apparel, using the observed script typeface (CafeParadis-SlantedScript) for live monogram previews, distinct from body/heading fonts.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| sm | 375px | Single-column product grid, hamburger nav |
| md | 768px | 2-column grid, condensed nav |
| lg | 1024px | Full horizontal nav-bar, 3–4 column grid |
| xl | 1440px | Max-width container, 4+ column grid |

Touch targets should be at least 44×44px for buttons and nav items on sm/md. The announcement/promo bar and mega-menu (COLLECTIONS, GIRLS, BOYS, LH SPORT, etc.) likely collapse into an accordion-style mobile menu below `lg`, but this collapse behavior was not directly observed and is a UX recommendation only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no live page, hover, or mobile-menu interaction was observed. CSS custom properties (`--colors-button`, `--colors-text-header`, etc.) reference variables whose resolved runtime values were not supplied, so button/header colors are inferred from the most frequently repeated navy hexes rather than confirmed computed output. Several palette entries (Loop Returns modal blues/grays, Swym wishlist teals, generic Tailwind-style neutrals like `#374151`/`#d1d5db`/`#9ca3af`) are attributable to third-party app widgets and were deliberately excluded from brand-identity claims. The sale/badge accent color is unverified as an official brand color. Font usage (`big-caslon-fb`, `futura-pt`, `untitled sans`, `CafeParadis-SlantedScript`) is based on family names present in CSS; actual licensing, hosting, and per-element application were not verified. All spacing and radius values follow a proposed standard scale, not measured site dimensions.
