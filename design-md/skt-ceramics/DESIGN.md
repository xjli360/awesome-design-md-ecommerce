---
version: alpha
name: "SKT Ceramics"
source_url: "https://www.sktceramics.com"
captured_at: "2026-09-29T04:17:47.925592+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation reads SKT Ceramics' evidence as a quiet, gallery-like Shopify storefront built for a handmade porcelain and illustration studio. The measured palette centers on a near-black ink (#121212) over white and off-white surfaces (#ffffff, #f5f5f5, #fcfcfc), with a muted sage-green (#8fc2b0) appearing as the theme's --color-button token and treated here as the primary accent, echoing glaze and botanical illustration tones without asserting a brand-verified meaning. Hairlines and card surfaces draw from the neutral grays present (#dfdfdf, #e6e6e6, #cccccc). Typography is inferred from two evident stacks: a custom heading token, GTStandard-M, driving h1–h5 per the CSS, and a classic serif fallback chain (Iowan Old Style, Apple Garamond, Baskerville, Times New Roman, Droid Serif) that governs body copy, consistent with the theme's --font-body-family variable resolving to a system serif on this install. Base body type is set at 1.5rem with 0.06rem letter-spacing, confirmed in base.css. Buttons, cards, and badges follow Shopify Dawn-style CSS custom-property patterns (--buttons-radius-outset, --border-radius) whose resolved pixel values are not exposed in the supplied evidence, so radius and spacing scales below are proposed, not measured. All component states beyond static declarations (hover, focus, mobile collapse) are proposed conventions suited to an artisan pottery e-commerce context.

colors:
  primary: "#8fc2b0"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#757575"
  hairline: "#dfdfdf"
  surface-soft: "#f5f5f5"
  surface-card: "#fcfcfc"
  on-primary: "#ffffff"
  border-strong: "#bbbbbb"
  link: "#2c6ecb"
  focus-ring: "#121212"
  error: "#d82c0d"
typography:
  display-xl: {fontFamily: "GTStandard-M, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.3px}
  display-md: {fontFamily: "GTStandard-M, sans-serif", fontSize: 34px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.2px}
  title-md: {fontFamily: "GTStandard-M, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.06rem}
  body-md: {fontFamily: "Iowan Old Style, Apple Garamond, Baskerville, Times New Roman, Droid Serif, serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.06rem}
  body-sm: {fontFamily: "Iowan Old Style, Apple Garamond, Baskerville, Times New Roman, Droid Serif, serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0.04rem}
  caption: {fontFamily: "Iowan Old Style, Apple Garamond, Baskerville, Times New Roman, Droid Serif, serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.06rem}
  button-md: {fontFamily: "Iowan Old Style, Apple Garamond, Baskerville, Times New Roman, Droid Serif, serif", fontSize: 15px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.06rem}
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
    border: "1px solid {colors.border-strong}"
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
    typography: "{typography.body-sm}"
    hairlineBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-sm}"
  glaze-color-swatch:
    shape: "circle"
    size: "24px"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    selectedRing: "2px solid {colors.primary}"

## Components
**button-primary** renders the sage accent as a filled call-to-action (e.g. "Add to Cart," "Shop Made-to-Order"), matching the theme's --color-button token; hover/active states are proposed, not observed. **button-secondary** is an outlined variant for lower-emphasis actions like "About Us," using ink text on white per the --color-secondary-button variables in the CSS. **text-input** covers search and newsletter email fields, styled with a light hairline border consistent with the theme's neutral border tokens. **nav-bar** proposes a white header with serif or heading-family wordmark links (Home, Illustrations, Ready-to-Ship, Made-to-Order, Personalized Pottery, Contact), separated by a hairline bottom border; mobile collapse into a hamburger menu is a convention, not confirmed. **product-card** wraps individual pottery/illustration listings with a soft card surface and border-radius token echoing --product-card-corner-radius; image, title, and price hierarchy follow the heading/body type pair. **hero** proposes the homepage introduction ("SKT Ceramics is a pottery and illustration studio...") on the off-white surface with generous section padding, appropriate to the long-form editorial copy in the evidence. **footer** uses inverted ink-on-white-text coloring for the newsletter, social, and legal links (Journal, Privacy policy, © 2026 SKT Ceramics), matching common dark-footer patterns seen in Shopify Dawn-derived themes. **badge** is a pill-shaped tag for states like "Ready-to-Ship" or "Made-to-Order" labels referenced in the site navigation and copy. **search** proposes a lightweight input matching the header's minimal chrome. **glaze-color-swatch** is a category-specific proposed component for selecting porcelain glaze colors on Made-to-Order product pages, styled as small bordered circles with a primary-color selection ring — this pattern is not directly evidenced but is a reasonable extrapolation from the "your choice of glaze color" copy.

## Responsive Behavior
Proposed breakpoints (not measured): mobile ≤599px, tablet 600–989px, desktop ≥990px, matching common Shopify Dawn-theme conventions implied by the CSS variable structure. At mobile widths, the nav-bar is expected to collapse into a drawer/hamburger menu, product-card grids reduce to 1–2 columns, and hero padding tightens toward {spacing.xl}. Touch targets for button-primary/secondary and glaze-color-swatch should maintain a minimum 44px tappable area per common accessibility guidance. This section is a recommendation based on typical Shopify theme behavior, not an observation of the live site's responsive layout.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no live rendering, computed layout, or interaction testing was performed. Semantic role assignments (e.g., treating --color-button as "primary," --color-foreground as "ink") are inferred from variable naming conventions, not confirmed brand guidance. Numeric values for rounded and spacing scales are proposed defaults, since the actual --buttons-radius-outset, --product-card-corner-radius, and spacing custom properties resolve to values not present in the supplied CSS. Typography sizes beyond the confirmed 1.5rem body base are estimated. Mobile/responsive and hover/focus interaction behavior were not observed. The custom heading font "GTStandard-M" is used verbatim from evidence but its licensing, availability, and correct display name are unverified; generic fallbacks are included per instructions.
