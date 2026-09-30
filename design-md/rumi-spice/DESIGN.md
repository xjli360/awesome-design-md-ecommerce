---
version: alpha
name: "Rumi Spice"
source_url: "https://rumispice.com"
captured_at: "2026-09-28T09:46:04.148912+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Rumi Spice's storefront CSS centers on a warm, sun-baked palette: a pale golden-cream canvas (#fef7e5, #fdf9f2), a deep umber-brown ink (#251c14) used for both foreground text and heading color variables, and a saturated burnt-orange (#e65300) driving the --color-button and --color-link tokens throughout the Shopify Dawn-based theme. A secondary warm gold (#f2b41c) and a deeper cream (#f4edd8) appear in the supplied palette and are interpreted here as accent/surface tones consistent with a saffron-and-spice narrative, though their exact applied role on the live page was not confirmed. A cluster of blues (#1990c6, #136f99, #0071ce) originates from Shopify's accelerated-checkout/payment-button CSS rather than brand styling and is retained only as a payment-accent token, not a core brand color. Typography is set in Open Sans for body copy (font-size 1.5rem, letter-spacing 0.06rem, line-height ~1.53), with headings sharing the same family via CSS custom properties (--font-heading-family) since no distinct heading typeface was observed in the evidence — this is flagged as inferred rather than confirmed. The interpretation favors a warm, artisanal, ingredient-forward aesthetic: cream surfaces, umber text, and orange calls-to-action, echoing the site's sourcing/empowerment storytelling without fabricating unobserved visual detail.

colors:
  primary: "#e65300"
  ink: "#251c14"
  canvas: "#fef7e5"
  body: "#251c14"
  muted: "#333333"
  hairline: "#dedede"
  surface-soft: "#f4edd8"
  surface-card: "#fdf9f2"
  on-primary: "#ffffff"
  accent-gold: "#f2b41c"
  overlay: "#00000080"
  payment-accent: "#1990c6"
typography:
  display-xl: {fontFamily: "Open Sans, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Open Sans, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "Open Sans, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.6px}
  body-sm: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.4px}
  caption: {fontFamily: "Open Sans, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.6px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  sourcing-trust-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent-gold}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.base}"

## Components

**button-primary** renders the orange call-to-action (e.g. "SHOP NOW," "Add to cart") using the site's `--color-button` (#e65300) with white text, matching the observed CSS custom property mapping. Hover/active states were not observed and are proposed as a slight opacity or darken shift.

**button-secondary** is an outlined variant on the cream canvas with orange text/border, inferred from the theme's `--color-secondary-button` and `--color-secondary-button-text` tokens (both resolving to canvas/orange in the evidence), suited for "View cart" or "Continue shopping" actions.

**text-input** covers search and form fields (e.g. newsletter signup). Background, border, and radius are proposed defaults consistent with a warm, light theme; no explicit input CSS was supplied.

**nav-bar** reflects the persistent header pattern implied by the text excerpt ("Skip to content," "Find Rumi in a Store Near You," "SHOP / LEARN / STORE LOCATOR"), styled on the cream background with umber text and a hairline divider; sticky/scroll behavior is proposed, not observed.

**product-card** represents catalog tiles (e.g. "Spice Blend Sampler," "Signature Spices and Salts"), using the card surface tone and hairline border implied by `.product-card-wrapper .card` custom properties, though exact border-radius and shadow values were not resolved from the truncated CSS variables.

**hero** models the homepage banner ("Michelin-star quality, directly sourced spices from Afghanistan / SHOP NOW") on the soft cream surface with large display type; imagery and layout proportions are proposed.

**footer** is inferred as a dark, ink-toned band for legal/social links (Twitter, Facebook, Pinterest, Instagram, YouTube) reversing the palette for contrast; exact footer styling was not present in the supplied CSS.

**badge** covers small labels such as "Sale," "Welcome Offer 20% Off," or "1,000+ 5 Star Reviews," using the theme's badge foreground/background/border tokens (all mapping to ink/canvas in the evidence).

**sourcing-trust-strip** is a category-appropriate, proposed component for the "100% Pure Spices / Empowers Afghan Women / Michelin Chef Approved" value-proposition row, using the gold accent to underline the brand's ethical-sourcing narrative; this pattern is not a literal CSS selector from the evidence but a structural interpretation of the page text content.

## Responsive Behavior
Recommended, not measured, breakpoints:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <600px | Single-column hero/product grid, collapsed nav to hamburger, min 44px touch targets |
| tablet | 600–989px | 2-column product grid, nav may remain collapsed |
| desktop | ≥990px | Full horizontal nav, 3–4 column product grid |

Touch targets should be at least 44×44px for cart/add-to-cart buttons. Navigation collapse and mobile menu behavior are proposed conventions for a Shopify Dawn-based theme and were not observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered page, computed styles, or interaction states were observed. The distinction between body and heading font families is unconfirmed — both are assumed to be Open Sans since no separate heading typeface was present in the evidence. Numeric type scale values (display-xl, title-md, etc.) beyond the one confirmed body font-size (1.5rem/0.06rem letter-spacing) are proposed, not measured. Border-radius values for buttons and product cards reference Shopify theme CSS custom properties whose resolved values were not included in the evidence, so `rounded` assignments are inferred defaults. The blue payment-accent color originates from Shopify's generic accelerated-checkout button styling, not confirmed brand identity, and is retained only for completeness. Mobile menu behavior, hover/focus states, footer structure, and actual grid/column layout were not observed and are marked proposed throughout. Font licensing/availability for Open Sans (a widely available open-source font) was not independently verified against the site's font-loading configuration.
