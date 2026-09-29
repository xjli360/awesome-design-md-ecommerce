---
version: alpha
name: "Griot's Garage"
source_url: "https://griotsgarage.com"
captured_at: "2026-09-28T04:29:16.950660+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Griot's Garage presents as a high-contrast, red-accented commerce theme built on a
  BigCommerce Stencil base. The confirmed palette centers on a signature red
  (#ec0928, exposed as the --gg-main custom property and the primary button
  color) paired with a near-black ink (#343434) used for both body copy and
  heading text, set against a plain white canvas. Two deeper brand tones —
  a dark red (#690412) and a dark navy (#0f1435) — are declared as CSS
  variables alongside the main red and white, suggesting a secondary
  accent/shadow role, though their exact usage is unconfirmed from static
  evidence. Grays from #cccccc through #f1f1f1 recur across borders, close
  buttons, and disabled states, giving the interface a utilitarian,
  garage-supply feel rather than a soft lifestyle aesthetic. Typography is
  clearly split: BentonSansStdCondensedBlack (condensed, uppercase-leaning,
  letter-spaced) drives headings and carousel labels, BentonSansStdBold
  drives buttons, and BentonSansStdRegular carries body copy, with Arial/
  Helvetica as declared fallbacks. This interpretation treats red as the
  sole primary action color, condensed black type as the brand's shouting
  voice, and the gray scale as structural/utility color — all semantic
  labels here are inferred from observed CSS, not verified live rendering.

colors:
  primary: "#ec0928"
  ink: "#343434"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#707070"
  hairline: "#dddddd"
  surface-soft: "#eeeeee"
  surface-card: "#f1f1f1"
  on-primary: "#ffffff"
  border-strong: "#000000"
  disabled: "#cccccc"
  accent-dark-red: "#690412"
  accent-dark-blue: "#0f1435"
  success: "#008a06"
  success-bg: "#d5ffd8"
  warning: "#f1a500"
  info: "#007dc6"
  danger-soft: "#f27474"
  danger-bg: "#ffdddd"
typography:
  display-xl: {fontFamily: "BentonSansStdCondensedBlack, Arial, Helvetica, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: 0.25px}
  display-md: {fontFamily: "BentonSansStdCondensedBlack, Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0.25px}
  title-md: {fontFamily: "BentonSansStdCondensedBlack, Arial, Helvetica, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.25px}
  body-md: {fontFamily: "BentonSansStdRegular, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "BentonSansStdRegular, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "BentonSansStdRegular, Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.15px}
  button-md: {fontFamily: "BentonSansStdCondensedBold, Arial, Helvetica, sans-serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.0, letterSpacing: 0.25px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.accent-dark-blue}"
    overlayColor: "{colors.border-strong}"
    headlineTypography: "{typography.display-xl}"
    ctaColor: "{colors.on-primary}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  trust-badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"

## Components
**button-primary** renders Griot's red (#ec0928) as a filled, condensed-bold call-to-action, matching the confirmed `.button--primary` rule and its white-on-hover inversion. **button-secondary** mirrors the base `.button` style — transparent fill with an ink-colored border — used for lower-emphasis actions like "Learn More" or filter toggles; hover-to-red state is proposed by extension of the confirmed primary hover pattern. **text-input** is a proposed pattern for search and account forms, using the observed hairline gray for borders since no explicit input CSS was supplied. **nav-bar** is inferred as a white header bar with dark text and gray dividers, consistent with the plain-canvas body style; sticky/mega-menu behavior is not confirmed. **product-card** proposes a bordered white tile using condensed-black titles for product names and regular-weight body type for pricing, appropriate to a catalog-heavy detailing retailer. **hero** is speculative, using the dark-navy CSS variable as a background option for banner sections beneath the confirmed carousel/`heroCarousel-content` button styling. **footer** assumes an inverted dark-on-light footer using the ink token as background, a common e-commerce pattern, but no footer CSS was supplied. **badge** and **trust-badge** are proposed components for stock/sale labels and certification marks (e.g., "Made in USA," warranty icons), drawing on the confirmed green/success and card-gray tokens respectively — car-care retailers commonly foreground such trust signaling near add-to-cart controls.

## Responsive Behavior
Breakpoint evidence in the supplied CSS references matched media widths of 375px, 719px, and 1024–1681px, suggesting mobile, tablet, and desktop tiers. A recommended (not measured) table:

| Tier | Width | Notes |
|---|---|---|
| Mobile | up to 719px | Single-column product grid, collapsed nav to hamburger, full-width buttons |
| Tablet | 719–1024px | Two-column grid, condensed nav |
| Desktop | 1024–1681px | Multi-column grid, full nav bar |
| Wide | 1681px+ | Max-width container, unchanged nav |

Touch targets should meet a 44px minimum height, consistent with the observed button padding (`.875rem 3rem`). Navigation collapse to a hamburger/off-canvas menu below the tablet threshold is a proposed pattern, not an observed interaction.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/color extraction only; no live page rendering, computed styles, or DOM screenshots were available. Semantic role assignments (e.g., which grays are "hairline" vs. "muted," or how dark-red/dark-navy variables are actually applied) are inferred from variable naming and adjacency, not confirmed usage sites. All typographic sizes beyond the confirmed 1.25rem button size are proposed estimates, not measured. Mobile menu behavior, hover/focus states beyond the two confirmed button rules, carousel interaction, and modal/close-button placement are not verified beyond the single `.close` button rule supplied. Availability, licensing, and web-font loading of BentonSansStdRegular/Condensed families are unverified and may require licensed font files rather than open-source substitutes.
