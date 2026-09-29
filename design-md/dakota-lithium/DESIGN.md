---
version: alpha
name: "Dakota Lithium"
source_url: "https://dakotalithium.com"
captured_at: "2026-09-28T10:02:09.648735+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Dakota Lithium's storefront evidence shows a rugged, high-contrast palette built on deep navy-charcoal ink (#0e252c), white canvas, and a saturated red/orange (#c8210a family, alongside #ce2b37, #a31126, #ab1718, #e2401c) used for alerts, badges, and calls to action across the WooCommerce and review-plugin CSS. A secondary green pair (#31856c active, #276a56 hover) appears explicitly as the review-form submit button, giving a "go/confirm" action color distinct from the red urgency color. Teal accents (#18b394/#19b394) and a soft warning yellow (#ffce00/#ffbc00) round out the palette, likely for in-stock or promotional badges, though exact usage is inferred. Neutral surfaces range from #f7f7f7 and #eeeeee through #d8e2e7, the latter confirmed as a border/hairline color in the review widget.
  Typography combines the condensed display face "Bebas-neue" (flagged !important in the stylesheet, suggesting brand headlines and product-category labels) with a body stack of Helvetica Neue/Helvetica and Inter, falling back to system sans-serif fonts per the WooCommerce block defaults. The overall interpretation is an outdoor-industrial, technical-spec-sheet aesthetic: bold condensed headers over dense, utilitarian body copy, red for urgency/CTA, green for confirmation, and generous neutral surfaces to let product photography and warranty/spec callouts read clearly. All semantic role assignments (primary vs. accent vs. success) are inferred from limited component CSS, not a full observed style guide.

colors:
  primary: "#c8210a"
  ink: "#0e252c"
  canvas: "#ffffff"
  body: "#272d36"
  muted: "#4d5d64"
  hairline: "#d8e2e7"
  surface-soft: "#f7f7f7"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  success: "#31856c"
  success-hover: "#276a56"
  accent-teal: "#18b394"
  alert: "#ce2b37"
  warning: "#ffce00"
  border-soft: "#e4e1e3"
typography:
  display-xl: {fontFamily: "Bebas-neue, sans-serif", fontSize: 56px, fontWeight: 400, lineHeight: 1.1, letterSpacing: 0.5px}
  display-md: {fontFamily: "Bebas-neue, sans-serif", fontSize: 36px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0.3px}
  title-md: {fontFamily: "Inter, Helvetica Neue, Helvetica, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Helvetica Neue, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica Neue, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Helvetica Neue, Helvetica, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Helvetica Neue, Helvetica, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0.3px}
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
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-confirm:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    ctaButton: "button-primary"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-callout:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"

## Components

**button-primary** carries the red/orange brand color forward from category badges and alert-style UI in the evidence, used here for primary purchase and "Shop" actions; hover/active states are proposed, not observed.

**button-secondary** is a bordered, white-background variant for lower-emphasis actions (e.g., "See product" links), using the confirmed hairline border color from the review-widget CSS.

**button-confirm** repurposes the explicitly observed green review-submit button (#31856c, hover #276a56) for confirmation-style actions such as form submission or "Add to Cart" success states.

**text-input** is a proposed pattern for search and account forms; border and text colors are drawn from confirmed evidence, but padding/rounding are inferred defaults.

**nav-bar** assumes a white top navigation given the extensive mega-menu category list in the page text (Batteries by Voltage, Marine & Deep Cycle, etc.); no header CSS was directly supplied, so layout is inferred.

**product-card** models the many "Featured Products" listings (price, weight, review count) seen in the text excerpt, using the WooCommerce product-title CSS (font-weight 700, line-height 1.2) as a basis for title styling.

**hero** reflects the repeated "Relentless Power. Zero Compromise." headline and dark background implied by the ink/navy tones in the palette; exact hero markup and background were not observed.

**footer** proposes a dark ink footer for contrast with the white body, consistent with the navy/charcoal tones present throughout the palette; actual footer structure is not confirmed by supplied CSS.

**badge** supports in-stock, warranty, and sale labels referenced in the text ("In Stock", "11-year warranty"); the observed onsale-badge pattern from WooCommerce (bordered pill, uppercase caption) informs this proposal, though its exact color was outside the confirmed palette so ink/white were substituted.

**search** is a proposed lightweight input treatment for the "Search" affordance mentioned in the navigation text; no dedicated search-bar CSS was supplied.

**spec-callout** is a category-appropriate component for battery specification blocks (Ah, CCA, weight, cycle count) seen repeatedly in product descriptions, using soft surface and hairline colors for a technical, data-sheet feel.

## Responsive Behavior

Proposed breakpoints (not measured from live site): mobile ≤480px, tablet 481–960px, desktop 961–1280px, wide ≥1281px. Navigation is assumed to collapse into a hamburger/off-canvas menu below the tablet breakpoint given the size of the observed category taxonomy. Product-card grids are assumed to reflow from 4-column (desktop) to 2-column (tablet) to 1-column (mobile). Touch targets for buttons and nav items should meet a 44px minimum height. This section is a design recommendation only; no responsive or interaction behavior was directly observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is derived from static CSS/text extraction only; no rendered layout, computed styles, or DOM structure were observed. Role assignments for primary, muted, and surface colors are inferred from limited component-level CSS (WooCommerce blocks, review plugin) and may not match the brand's actual design system. The "Bebas-neue" display family's availability, exact weight range, and licensing were not verified—only its presence as a forced (!important) font-family declaration was observed. Breakpoints, spacing scale, rounding scale, and most component states (hover, focus, disabled, error) are proposed defaults, not measured. Mobile navigation collapse, header structure, and hero layout are inferred from page text and category volume, not from observed markup.
