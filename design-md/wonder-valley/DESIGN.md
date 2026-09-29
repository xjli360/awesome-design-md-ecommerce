---
version: alpha
name: "Wonder Valley"
source_url: "https://welcometowondervalley.com/"
captured_at: "2026-09-29T03:58:28.705618+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Wonder Valley is a California olive-oil and skincare brand (Joshua Tree, since 2014) presented on a
  Shopify-hosted storefront. The supplied CSS exposes a warm, sand-and-desert palette: near-black ink
  (#221f1f), soft warm whites and creams (#f3f0eb, #fefaf5, #f4ebcd, #e8d09c), and accent tones spanning
  amber/marigold (#f2c94c, #f79b2e, #f9c636, #ca7d26) alongside a small set of cooler utility colors used
  by third-party widgets (Okendo reviews: #676986, #272d45, #dbdde4; Shopify accelerated checkout: #1990c6,
  #136f99). Typography evidence shows a serif display pairing, "Le Jeune Deck" and "Caslons Egyptian",
  alongside "Inter"/"InterDisplay" as the sans workhorse and monospace stacks (Consolas, Menlo, covik-sans-mono)
  used incidentally by code/system UI. No brand font sizes or weights beyond widget CSS variables were
  observed, so all display/body scale values below are proposed for a functioning specification, not
  measured. Semantic color roles (primary, ink, canvas, surfaces) are inferred by frequency and contrast
  from the supplied swatches, since no computed styles for headers, buttons, or product cards were provided
  outside of the Okendo/Shopify widget variables. The resulting interpretation favors a quiet, sunlit
  editorial feel appropriate to an olive-oil and self-care brand: warm neutral canvases, dark warm-black
  text, amber accents reserved for calls-to-action, and restrained hairlines borrowed from the review
  widget's border tokens.

colors:
  primary: "#ca7d26"
  ink: "#221f1f"
  canvas: "#fefaf5"
  body: "#383232"
  muted: "#676986"
  hairline: "#ebe5d3"
  surface-soft: "#f3f0eb"
  surface-card: "#f4ebcd"
  on-primary: "#ffffff"
  accent-amber: "#f2c94c"
  accent-orange: "#f79b2e"
  accent-gold: "#f9c636"
  sand-deep: "#e8d09c"
  link-blue: "#1990c6"
  link-blue-hover: "#136f99"
  widget-ink: "#272d45"
  widget-border: "#dbdde4"
  alert-red: "#dc0807"
typography:
  display-xl: {fontFamily: "Le Jeune Deck, Caslons Egyptian, serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Le Jeune Deck, Caslons Egyptian, serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Inter, InterDisplay, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, InterDisplay, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, InterDisplay, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Inter, InterDisplay, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Inter, InterDisplay, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.2px}
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
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    priceColor: "{colors.primary}"
    rounded: "{rounded.md}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base}"
    typography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.accent-orange}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  subscription-widget:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components
**button-primary** renders the amber/ochre call-to-action ("Add To Cart", "Shop Now") against a light background; hover/active/loading states are proposed, not observed. **button-secondary** is an outline variant for lower-emphasis actions like "Read More". **text-input** covers newsletter/email capture fields; padding and border come from the hairline token, sized for touch. **nav-bar** models the top utility/shop navigation (SHOP, SUBSCRIBE & SAVE, RECIPES, ABOUT) on a warm canvas background with a thin hairline divider; sticky behavior is not confirmed. **product-card** represents the grid of bottles, towels, and skincare SKUs seen in the excerpt (e.g., "Oil Tin $74", "Barrier Balm $88"), with price rendered in the primary accent and a soft card surface distinct from the page canvas. **hero** is the large introductory panel ("Welcome to Wonder Valley…California grown & family owned"), using the serif display type against a soft sand background. **footer** is inferred from the multi-column link list (SHOP, SUPPORT, SUSTAINABILITY, FOLLOW, VISIT, TERMS) and the observed `--footer-background` image asset, set dark for contrast with light text and amber links. **badge** is a proposed pill treatment for promotional text such as "Free Domestic Shipping on Orders $100+". **search** is a proposed pattern for product lookup, styled consistently with text-input. **subscription-widget** models the "Sign Up… Receive 10% off" email capture block, using the card surface and primary accent for its action button.

## Responsive Behavior
Recommended, not measured: mobile <480px (single-column product grid, stacked nav collapsing behind a menu toggle, min touch target 44px), tablet 480–1024px (2-column product grid, condensed nav), desktop >1024px (4+ column product grid per the observed dense product list, full horizontal nav). Buttons and inputs should maintain minimum 44px hit area on touch; the promotional ticker ("Free Domestic Shipping…") is assumed to marquee or repeat horizontally on narrow viewports.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived from static CSS/text extraction only; no rendered layout, computed box model, or breakpoint behavior was observed. Semantic role assignments (primary, ink, canvas, surfaces) are inferred from color frequency and typical e-commerce contrast patterns, not from confirmed component screenshots. Type sizes, weights, and line-heights beyond the Okendo widget variables are proposed defaults, not measured from the live site. Interaction states (hover, focus, active, loading) for buttons and inputs beyond the Okendo/Shopify widget definitions are proposed. Mobile/responsive layout, menu collapse behavior, and touch interactions were not observed and are recommendations only. Availability and licensing of "Le Jeune Deck" and "Caslons Egyptian" as web fonts were not verified from the supplied evidence; both are used here only because they appear in the observed font_families list, with system serif/sans-serif fallbacks applied per usage.
