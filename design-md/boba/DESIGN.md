---
version: alpha
name: "Boba"
source_url: "https://boba.com"
captured_at: "2026-09-28T10:16:50.819544+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Boba's observed palette centers on warm, muted neutrals — off-white canvas
  (#f4efe9), warm parchment (#ede5db, #f1eae2), and soft sage (#a2beb2, #84a999)
  used as the review-widget primary accent — paired with near-black ink
  (#171d20) and a deep red (#c32121) that reads as a promotional/sale accent
  rather than a core brand color. Grays (#333333, #666666, #999999) form a
  supporting text/border scale. Font evidence shows distinct heading and body
  stacks via CSS custom properties (--FONT-STACK-HEADING /
  --FONT-STACK-BODY); observed families across the stylesheet are Raleway,
  Nunito Sans, Baskerville, Pacifico, and monospace utility fonts (Consolas,
  Space Mono) plus icon fonts. This interpretation assigns Raleway to
  headings and Nunito Sans to body copy as the most plausible sans pairing
  for a modern DTC babywear brand; this mapping is inferred, not confirmed
  by a direct font-family declaration on h1/body in the supplied evidence.
  Baskerville and Pacifico are treated as unused/alternate assets pending
  further confirmation. Radius and spacing values are proposed conventions
  scaled to the soft, rounded, approachable tone suggested by the sage/cream
  palette and generous heading sizes (3rem base) observed in the theme
  variables.

colors:
  primary: "#a2beb2"
  ink: "#171d20"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f4efe9"
  surface-card: "#f1eae2"
  on-primary: "#ffffff"
  accent-sale: "#c32121"
  accent-warm: "#c65a12"
  sage-deep: "#84a999"
  parchment: "#ede5db"
  border-light: "#e9e9e9"
  text-faint: "#999999"
typography:
  display-xl: {fontFamily: "Raleway, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.25, letterSpacing: -0.5px}
  display-md: {fontFamily: "Raleway, sans-serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  title-md: {fontFamily: "Raleway, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5625, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Nunito Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.625, letterSpacing: 0.3px}
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: "63px"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  fit-consultation-cta:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    description: |-
      A proposed callout module for "Book a Fit Consultation," styled as a
      soft-bordered card distinct from standard product cards, using the
      sage primary as an accent border or icon color to signal a service
      rather than a product.

## Components
**button-primary** uses the sage primary (#a2beb2) as background, matching the review-widget accent color observed in the `--jdgm-primary-color` custom property, suggesting sage is the brand's functional accent beyond reviews; treated here as the general CTA color — this extension is inferred.

**button-secondary** is an outline variant using ink text on transparent background with a hairline border, proposed for lower-emphasis actions like "Shop All" or filter toggles seen in the navigation text.

**text-input** follows the flat, minimal bordered style typical of the Shopify theme evidenced by the shared `border-radius:var(--RADIUS)` declaration on form elements; exact radius value not confirmed, so `{rounded.sm}` is used as a conservative default.

**nav-bar** reflects the measured `--header-height: 63px` custom property, giving a real observed dimension; background and hairline colors are proposed to match the canvas/border palette.

**product-card** is proposed for wrap/carrier listings (e.g., "Boba Classic Wrap," "Boba X Carrier") using the parchment surface-card tone to differentiate cards from the pure-white canvas, consistent with warm off-white tones present in the palette.

**hero** models the homepage banners ("Boba Bliss," "Boba Auri") with large heading typography sized from the observed `--heading-size: calc(3rem * var(--adjust-heading))` variable, scaled down responsively per the theme's own heading-size overrides at narrower widths.

**footer** is proposed as a dark ink-background band for site-wide links (Support, Babywearing Safety, Gift Cards) with light text for contrast; this pattern is not directly observed in the supplied CSS but is a common e-commerce convention.

**badge** covers "SALE" and promotional labels (e.g., "30% off") using the red accent (#c32121) distinct from the sage primary, consistent with red appearing only in a promotional-adjacent context in the evidence.

**search** models the "Open search bar" interaction referenced in the page text, styled consistently with text-input.

**fit-consultation-cta** is a category-specific proposed component supporting Boba's "Book a Fit Consultation" and "Free Fit Consultations" messaging, distinguishing service-oriented content from standard product merchandising.

## Responsive Behavior
This is a proposed, non-measured breakpoint recommendation:

| Breakpoint | Width | Layout notes |
|---|---|---|
| mobile | <600px | Single-column product grid, collapsed hamburger nav, stacked hero text/CTA |
| tablet | 600–1024px | 2-column product grid, condensed top-level nav |
| desktop | >1024px | Multi-column product grid, full horizontal nav with dropdowns |

Touch targets should be a minimum 44×44px for nav icons (cart, search, account) referenced in the page text ("Open cart," "Open search bar"). Navigation should collapse into a hamburger/off-canvas menu below tablet width; this behavior is standard for the observed Shopify theme structure but was not directly measured.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This design interpretation is derived from static CSS custom properties, a color list, and page text extracted from a single crawl; no rendered layout, computed styles, or interaction states were observed. The mapping of Raleway to headings and Nunito Sans to body text is inferred from the presence of these families in the font list combined with typical heading/body CSS variable patterns (`--FONT-STACK-HEADING`, `--FONT-STACK-BODY`); the actual variable values were not present in the supplied evidence. Baskerville and Pacifico appear in the font list but their usage context (e.g., logo, special promotions) is unconfirmed and they are excluded from the core type scale. All rounded and spacing scale values beyond the observed `--header-height: 63px` are proposed conventions, not measured. Hover, focus, active, and error states for buttons and inputs are not observed and are marked proposed by omission. Mobile menu behavior, cart drawer interaction, and product-grid responsive breakpoints were not observed and are recommendations only. Licensing and self-hosting status of Raleway, Nunito Sans, Baskerville, and Pacifico were not verified.
