---
version: alpha
name: "Sakara Life"
source_url: "https://sakara.com"
captured_at: "2026-09-29T04:00:50.287849+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Sakara Life's storefront presents a high-contrast, editorial aesthetic built
  almost entirely on black-and-white value contrast, evidenced by repeated use
  of #000000 and #ffffff across primary buttons, hero buying-panel actions, and
  bundle add-to-cart controls, each swapping fill/text on hover. A small set of
  accent hues appears in supporting UI: a muted sage-lime (#5bab5d) used for a
  video play button, plus a coral-orange (#ff6341) and deeper forest green
  (#00873b) drawn from the broader observed palette — likely reserved for
  promotional badges or category tags; this specific role is inferred, not
  confirmed by component-level CSS. Neutral surfaces (#f7f7f7 product-card
  background, #fafaf8, #f5f5f1) and soft borders (#d9d9d9, #ebebe4) form a
  quiet, paper-like canvas typical of a wellness/nutrition brand. Muted gray
  (#747474) marks struck-through compare prices. Typography combines a
  proprietary-looking display serif, "Gestura Headline," confirmed in a dialog
  header at 28px/line-height 1, with "Gestura Text" and "Rework Text" inferred
  as the body/UI sans families from the font-family list; exact body sizing is
  not observed and is proposed. The interpretation favors generous whitespace,
  thin hairlines, and monochrome CTAs, reserving color for merchandising
  accents — consistent with a premium meal-program and supplement retailer.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#747474"
  hairline: "#d9d9d9"
  surface-soft: "#f7f7f7"
  surface-card: "#fafaf8"
  on-primary: "#ffffff"
  accent-lime: "#5bab5d"
  accent-coral: "#ff6341"
  accent-forest: "#00873b"
  surface-alt: "#f5f5f1"
  border-soft: "#ebebe4"
typography:
  display-xl: {fontFamily: "Gestura Headline, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Gestura Headline, serif", fontSize: 28px, fontWeight: 600, lineHeight: 1, letterSpacing: 0px}
  title-md: {fontFamily: "Gestura Text, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Gestura Text, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Gestura Text, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Gestura Text, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Gestura Text, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    hover:
      backgroundColor: "{colors.on-primary}"
      textColor: "{colors.primary}"
      border: "1px solid {colors.primary}"
  button-secondary:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    hover:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
    focus:
      border: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"
    priceTypography: "{typography.body-md}"
    comparePriceColor: "{colors.muted}"
    titleTypography: "{typography.title-md}"
  hero:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  buying-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    primaryAction:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      hoverBackgroundColor: "{colors.on-primary}"
      hoverTextColor: "{colors.primary}"
    secondaryAction:
      backgroundColor: "{colors.on-primary}"
      textColor: "{colors.primary}"
      hoverBackgroundColor: "{colors.primary}"
      hoverTextColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    padding: "{spacing.lg}"

## Components
**button-primary** is the solid black call-to-action seen on hero buying-panel controls, inverting to white-on-white-with-black-border on hover; this hover swap is directly evidenced in the supplied CSS. **button-secondary** mirrors the bundle add-to-cart pattern (white fill, black text, black 1px border) and is proposed to invert on hover for consistency with the primary button's confirmed behavior. **text-input** is a proposed minimal-bordered field for search and newsletter capture, styled from the hairline/canvas pairing; no input-specific CSS was supplied. **nav-bar** is inferred from the page's listed navigation labels (Weekly Menu, Learn About Us, Blog, Podcast, Our Standards, Sign In/Sign Up) and uses the canvas/ink/hairline system for a light, low-chrome header; exact height and layout are not observed. **product-card** reflects the one directly observed pattern: a 3:4 image wrapper on a light gray (#f7f7f7) background, with muted-gray strikethrough compare pricing, extended here with proposed title/price typography. **hero** is a proposed full-bleed section using the soft neutral surface and a large display headline, generalized from the homepage's promotional banners (e.g., "Join Level II: Detox") described in the text excerpt but not measured in CSS. **footer** is inferred from the listed footer links (FAQ, Return Policy, Careers, Privacy) and styled as a light, hairline-divided multi-column block consistent with the rest of the neutral palette. **badge** is a proposed small pill for "BEST SELLER" and "BUNDLE & SAVE" labels seen in the page text, assigned the coral accent as a plausible but unconfirmed brand highlight color. **search** is a proposed lightweight input variant sharing the text-input treatment. **buying-panel**, the category-appropriate component, is grounded directly in the observed `.nutrition-hero-section .buying-panel__action-button` rules, modeling the program/subscription purchase flow with confirmed primary/secondary hover-inversion states.

## Responsive Behavior
| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | <640px | Single-column stacks; nav collapses to a hamburger/drawer; buying-panel actions stack full-width. |
| Tablet | 640–1024px | Two-column product grids; slide widths align with observed `--mobile-slide-width:140px` / `--desktop-slide-width:180px` custom properties for carousels. |
| Desktop | >1024px | Multi-column grids (3–4 up product cards); nav fully expanded; buying-panel primary/secondary actions shown side by side. |

Touch targets should be at least 44px in height; the primary/secondary button padding (`{spacing.md} {spacing.lg}`) supports this at typical font sizes. This table is a recommendation based on the two supplied slide-width tokens and general e-commerce convention, not measured site behavior at any breakpoint.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from a static snippet of CSS rules, page text, and a color/font-family list — no rendered layout, computed styles, or interaction states beyond the explicitly supplied hover rules were observed. Semantic color roles (e.g., treating #000000 as "primary" and #ff6341/#00873b/#5bab5d as accent/badge colors) are inferred from limited component usage and may not match the brand's actual design-system naming or intended hierarchy. All typography sizes except the 28px/line-height-1 "Gestura Headline" dialog rule are proposed, not measured. The "Gestura Headline," "Gestura Text," and "Rework Text" families appear custom/proprietary; their licensing, exact weights, and availability outside this site are not verified, and only the generic sans-serif/serif system-font fallbacks should be assumed safe for reuse. Mobile navigation collapse, carousel behavior, cart/checkout flows, and form validation states were not observed and are proposed conventions only. Rounded and spacing scales are standard proposed defaults, not extracted from the source CSS.
