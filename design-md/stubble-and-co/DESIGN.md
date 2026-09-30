---
version: alpha
name: "Stubble & Co"
source_url: "https://stubbleandco.com"
captured_at: "2026-09-28T05:04:02.933245+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Stubble & Co's storefront CSS shows a stark black-and-white base (#000000 ink on #ffffff canvas) punctuated by a single warm accent, #FF4800, used for the theme accent color, sale/discount badges, and low-stock flags. Two typefaces are declared: "Stubble Sans" for body copy (400 weight, 12px/150%) and "Stubble Mono" for small uppercase UI labels such as filter/option buttons (10px/140%, pill-shaped border). Neutral grays (#818181, #f5f5f5, #f3f3f3, #d7dadd, #c9c9c9) are inferred here as muted text, soft surfaces, card backgrounds, and hairlines, since the source CSS does not label their semantic roles explicitly. A large secondary swatch set (#213037, #e41843, #eaff36, #ffd800, #6f785d, #dbcbb9, #cd1719) appears tied to product color-variant swatches (bag colorways like Midnight Blue, Garnet Red, Volt, Sand) rather than core UI chrome; they are retained here as accent/utility tokens for swatch and badge components only. Buttons follow an observed black/white inversion pattern on hover (.button--style-black, .button--style-accent) which this spec generalizes into primary/secondary button states. Rounded corners, spacing scale, and most component sizing are proposed conventions layered onto the observed tokens, not measured page geometry.

colors:
  primary: "#ff4800"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#1f1f1f"
  muted: "#818181"
  hairline: "#d7dadd"
  surface-soft: "#f5f5f5"
  surface-card: "#f3f3f3"
  on-primary: "#ffffff"
  sale: "#e41843"
  navy: "#213037"
  accent-volt: "#eaff36"
  swatch-yellow: "#ffd800"
  swatch-sand: "#dbcbb9"
  swatch-garnet: "#cd1719"
  overlay-dark: "#0000004d"
  overlay-light: "#ffffff4d"
typography:
  display-xl: {fontFamily: "'Stubble Sans', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Stubble Sans', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Stubble Sans', sans-serif", fontSize: 18px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Stubble Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Stubble Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Stubble Mono', monospace", fontSize: 10px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "'Stubble Mono', monospace", fontSize: 10px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderRadius: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    ratingTypography: "{typography.caption}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.overlay-dark}"
    headlineTypography: "{typography.display-xl}"
    ctaButton: "button-primary"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    borderColor: "{colors.navy}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    saleBackgroundColor: "transparent"
    saleTextColor: "{colors.sale}"
    lowStockTextColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    optionBorderColor: "{colors.hairline}"
    optionSelectedBorderColor: "{colors.ink}"
    swatchColorsSource: "product variant palette (e.g. {colors.navy}, {colors.sale}, {colors.accent-volt}, {colors.swatch-yellow}, {colors.swatch-sand}, {colors.swatch-garnet})"
    size: "20px"
    rounded: "{rounded.full}"
    gap: "{spacing.xs}"

## Components
**button-primary** renders the theme's #FF4800 accent as a filled, pill-shaped call-to-action (e.g. "Shop Now"), using the Stubble Mono caption typography observed on `.button--style-option`. Hover inversion to black is proposed by analogy with the observed `.button--style-accent:hover` rule.

**button-secondary** mirrors the observed `.button--style-black` pattern: solid black fill with white text, inverting to white-on-black on hover per the CSS. Used for lower-emphasis actions like "Add to Cart" secondary variants.

**text-input** is a proposed pattern for account/newsletter fields; no input-specific CSS was supplied, so border, radius, and padding are inferred defaults consistent with the theme's minimal aesthetic.

**nav-bar** represents the top navigation (Shop, Bags & Backpacks, Luggage, About) implied by the page text; sticky behavior, search/cart drawer toggles, and exact height are not confirmed by the supplied CSS and are proposed.

**product-card** is inferred from the repeating listing pattern (name, star rating, review count, price, color swatches) visible in the page-text excerpt for items like "The Roll Top 20L." Card background and radius are proposed since no card-specific selector was supplied.

**hero** models the homepage banner ("Back to routine / Work-ready gear") as a full-bleed dark section with an overlay and large display type; the dark overlay token reuses the observed `#0000004d` value from `.button--style-white`.

**footer** is proposed as a dark section reusing ink/navy tokens; no footer-specific selectors were present in the evidence, so structure and content grouping are assumptions typical of DTC ecommerce sites.

**badge** covers sale, discount, and low-stock indicators, directly reusing the observed CSS custom properties `--sale-badge-foreground-color`, `--discount-badge-foreground-color`, and `--low-stock-badge-foreground-color`, all set to the orange/red family in the palette.

**color-swatch-selector** is a category-appropriate component for duffel/backpack variant pickers, inferred from the extensive per-product colorway lists (Midnight Blue, Garnet Red, Urban Green, Volt, etc.) in the page text; swatch fill colors are drawn from the supplied palette but exact hex-to-colorway mapping was not confirmed by CSS.

## Responsive Behavior
Recommended, not measured: mobile <480px (single-column product grid, collapsed hamburger nav, cart/search as full-screen drawers); tablet 480–1024px (2-column product grid, horizontal color-swatch scroller as suggested by "Scroll to previous/next" UI text); desktop >1024px (multi-column grid, persistent top nav). Touch targets for buttons and swatches should be at least 44px regardless of the smaller visual swatch/button sizing implied by the 10px caption typography. This breakpoint table is a proposal for implementation guidance only; no responsive CSS or viewport behavior was included in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This spec is derived from a static CSS/text snapshot only; no live rendering, computed layout, or DOM structure was observed. Font availability and licensing for "Stubble Sans" and "Stubble Mono" (custom/proprietary names) were not verified and may require confirmation with Stubble & Co before implementation. Several palette colors (e.g. navy #213037, sale #e41843, volt #eaff36, swatch yellows/reds) appear only implicitly via product-swatch listings in page text, not explicit CSS role declarations, so their assignment to "colorway" versus potential UI use is inferred. Component padding, radii, breakpoints, hover/focus states beyond the few explicitly observed (.button--style-black, .button--style-accent, .button--style-white variants), and all spacing-scale values are proposed conventions, not measurements from the live site. Mobile menu, cart drawer, and search panel interactions mentioned in page text ("Toggle cart drawer," "Toggle search panel") were not accompanied by layout or interaction CSS, so their visual behavior is unconfirmed.
