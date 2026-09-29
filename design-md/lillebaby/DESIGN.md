---
version: alpha
name: "Lillebaby"
source_url: "https://lillebaby.com"
captured_at: "2026-09-28T09:58:51.115467+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  LÍLLÉbaby's storefront runs on a Shopify theme exposing explicit CSS custom
  properties, giving strong confidence in the core palette: a warm gold
  (#cfb52c) drives primary buttons and the cart indicator, paired with near-black
  text (#111111) for links, prices, and body copy on a white canvas. A dusty
  rose (#d67972) marks sale tags and savings text, while footer and
  announcement bands use a soft off-white (#efefed). Borders and dividers use a
  light gray (#dddddd), and secondary surfaces use #f2f2f2. Typography is set
  in Rubik with a sans-serif fallback, using a 36px/400/1.2 header style and an
  18px/400/1.4 base style per the theme's root variables; all larger display
  sizes and weight variations below are proposed extrapolations, not directly
  observed. Buttons are explicitly flat (0px radius) except circular slideshow
  navigation controls (50% radius). This interpretation treats the gold/ink/rose
  triad as the brand's functional palette (commerce, price, promotion) and
  infers a soft, nursery-adjacent neutral background system around it,
  appropriate for a baby-gear retailer emphasizing trust, safety, and product
  clarity over decoration.

colors:
  primary: "#cfb52c"
  primary-light: "#dbc553"
  primary-dim: "#baa328"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#111111"
  muted: "#73706d"
  accent-savings: "#d67972"
  hairline: "#dddddd"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  surface-footer: "#efefed"
  surface-subtle: "#f9f9f9"
  on-primary: "#111111"
  on-accent: "#ffffff"
typography:
  display-xl: {fontFamily: "Rubik, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Rubik, sans-serif", fontSize: 36px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0em}
  title-md: {fontFamily: "Rubik, sans-serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0em}
  body-md: {fontFamily: "Rubik, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0em}
  body-sm: {fontFamily: "Rubik, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0em}
  caption: {fontFamily: "Rubik, sans-serif", fontSize: 12px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.05em}
  button-md: {fontFamily: "Rubik, sans-serif", fontSize: 12px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0em}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    priceColor: "{colors.ink}"
    salePriceColor: "{colors.accent-savings}"
  hero:
    backgroundColor: "{colors.surface-footer}"
    textColor: "{colors.on-accent}"
    overlayColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    ctaButton: "button-secondary"
  footer:
    backgroundColor: "{colors.surface-footer}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-savings}"
    textColor: "{colors.on-accent}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  fit-quiz-module:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    ctaButton: "button-primary"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"

## Components

**button-primary** uses the observed gold (`--colorBtnPrimary: #cfb52c`) with dark-ink text, matching the theme's own primary-button token pair. Radius is flat (0px) per the observed `--buttonRadius` variable; hover/active states are proposed (e.g., darkening toward `{colors.primary-dim}`) and not confirmed from static CSS.

**button-secondary** reflects the white-background, black-border, black-text pattern seen repeatedly in slideshow and flex-grid `.btn` overrides (`background:#fff;color:#000;border:none` or `border:black 2px solid`). This is treated as the outline/ghost variant used over hero imagery.

**text-input** is inferred from newsletter input placeholder rules (`color:#1c1d1d`) with border and radius proposed, since no explicit input border-radius or fill color was observed.

**nav-bar** infers a white nav (`--colorNav:#ffffff`, `--colorNavText:#111111`) with a light hairline divider from `--colorBorder`; sticky/mobile-collapse behavior is not observed.

**product-card** models the trending-product grid pattern (title, regular price, strikethrough/sale price, "Save $X") using `--colorPrice` and `--colorTextSavings`; card border and radius are proposed since no card-container CSS was captured.

**hero** is inferred from `--colorHeroText:#ffffff` and `--colorImageOverlay:#111111`, describing a full-bleed slideshow with light overlay text and a white outline CTA button, consistent with the captured `.slideshow__slide .btn` rules.

**footer** uses the observed `--colorFooter:#efefed` / `--colorFooterText:#111111` pair; column layout and link states are proposed.

**badge** represents the "Sale" / "New Arrival" tags using `--colorSaleTag:#d67972` and `--colorSaleTagText:#ffffff`; uppercase caption styling is drawn from the observed bold/uppercase/letter-spacing snippet.

**search** is inferred from modal/drawer background (`--colorModalBg:#efefed`) and general input conventions; no dedicated search-bar CSS was present in evidence.

**fit-quiz-module** is a category-appropriate, proposed component representing the site's repeated "Take the Quiz" / "Find My Carrier" prompts, styled with the soft neutral surface and primary CTA button; no dedicated quiz-module CSS was observed, so styling is extrapolated from global tokens.

## Responsive Behavior

Proposed breakpoints (not measured from live site):
| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <600px | Single-column product grid, collapsed nav into drawer/menu icon |
| tablet | 600–999px | 2-column product grid, condensed nav |
| desktop | 1000px+ | Full nav bar, 3–4 column product grid |

Touch targets should be at least 44x44px for cart/quantity controls; nav and drawer collapse behavior, slideshow swipe gestures, and exact grid column counts are proposed conventions only, not confirmed from captured CSS or screenshots.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, a limited rule sample, and page text; no live rendering, computed layout, or interaction testing was performed. Semantic role assignments (e.g., `muted`, `surface-card`) are inferred from variable naming and usage context, not verified against rendered UI. Most typography sizes beyond the two root-declared values (36px header, 18px base) are proposed, not observed. Spacing scale values are a proposed convention; the theme's own `--grid-gutter:22px` and `--drawer-gutter:30px` do not align exactly with this scale. Rubik's availability, license, and loading method (self-hosted vs. Google Fonts) were not verified. Hover, focus, error, and disabled states for all components are proposed and unconfirmed. Mobile menu, quiz-module, and search-bar markup/CSS were not present in the supplied evidence, so those components are extrapolated from adjacent patterns only.
