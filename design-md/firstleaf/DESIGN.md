---
version: alpha
name: "Firstleaf"
source_url: "https://firstleaf.com"
captured_at: "2026-09-28T09:11:51.065304+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Firstleaf's storefront runs on Shopify with a Gotham-led sans-serif system
  (Gotham A / Gotham B, falling back to Calibri, Roboto, sans-serif) set at a
  spacious 2.8rem body line-height, giving copy a relaxed, editorial feel
  suited to a wine-club subscription flow. The observed CSS custom-property
  set (--c-orange, --c-purple, --c-blue, --c-gray-light, --c-sub-heading)
  indicates a small, deliberate brand palette: a burnt-orange primary
  (#d5440b, hover #ed654b) used on `.btn.primary`, and a deep aubergine
  purple family (#37024b down to lighter tints #a89aaf, #f2eff3, #f7f5f8)
  reserved for structural/secondary surfaces. A muted teal (#007180) and a
  savings-badge pairing (#00444d on #e6f1f2) appear in bundle/plan-comparison
  contexts, inferred here as accent and status colors rather than primary
  brand hues. Base text is #212121 on white canvas, with #a0a0a0 used for
  disabled states and sub-headings. This interpretation treats orange as the
  sole call-to-action color, purple as brand/structural chrome (nav, footer,
  quiz), and teal/badge tones as informational accents — semantic roles
  inferred from variable naming and component context, not confirmed from
  live layout screenshots.

colors:
  primary: "#d5440b"
  ink: "#212121"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#a0a0a0"
  hairline: "#e0e0e0"
  surface-soft: "#f7f5f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-purple: "#37024b"
  accent-purple-dark: "#342c38"
  accent-blue: "#007180"
  accent-orange-hover: "#ed654b"
  surface-purple-white: "#f2eff3"
  badge-bg: "#e6f1f2"
  badge-text: "#00444d"
typography:
  display-xl: {fontFamily: "Gotham A, Gotham B, Calibri, Roboto, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Gotham A, Gotham B, Calibri, Roboto, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Gotham A, Gotham B, Calibri, Roboto, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Gotham A, Gotham B, Calibri, Roboto, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.75, letterSpacing: 0px}
  body-sm: {fontFamily: "Gotham A, Gotham B, Calibri, Roboto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "Gotham A, Gotham B, Calibri, Roboto, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Gotham A, Gotham B, Calibri, Roboto, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1, letterSpacing: 0px}
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    ctaBackground: "{colors.primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.accent-purple-dark}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.surface-purple-white}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  quiz-flow-card:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.accent-blue}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg}"

## Components
**button-primary** maps directly to the observed `.btn.primary` rule (`background-color: var(--c-orange)`, white text, hover state `--c-orange-hover`); used for "Get Started" and quiz CTAs. **button-secondary** mirrors the observed `.btn.secondary` (transparent background, orange text and border) for lower-emphasis actions like "Skip personalization." **text-input** is proposed for quiz/email-capture fields; border and radius are inferred defaults since no dedicated input CSS was supplied. **nav-bar** is proposed from the site's "About / Club Plans / Wine School / Gifts / Wine Store / Log In" text structure; background and hairline values are inferred, not measured. **product-card** is a proposed pattern for wine bottle/tier tiles referenced in "Wine Store" and plan listings; padding and radius follow the general system scale. **hero** models the homepage "Get 12 wines for $60" intro banner; the soft purple-tinted background is inferred from `--c-purple-lightest`, not confirmed as the live hero background. **footer** uses the darkest purple token as an inferred brand-chrome color for the observed footer link list (Terms, Privacy, Accessibility); actual footer styling was not directly supplied. **badge** models the "Get 12 wines for $60" savings/discount callouts using the explicit `--bundle-savings-badge-color` / `--bundle-savings-badge-background` pair, one of the few semantically named color roles in the evidence. **search** and **quiz-flow-card** are proposed, category-appropriate components: search for the store's product catalog, and quiz-flow-card for the "Tell us your tastes" personalization steps central to Firstleaf's onboarding, using the teal accent as a light interactive highlight.

## Responsive Behavior
Recommended breakpoints (not measured from live site): mobile ≤599px, tablet 600–959px, desktop ≥960px, wide ≥1280px (site defines a 132rem max `--page-width`). Touch targets should be at least 44px tall, matching the Shopify accelerated-checkout button's `clamp(25px, 44px, 55px)` sizing pattern observed in vendor CSS. Nav items should collapse into a hamburger/off-canvas menu below tablet width; the quiz flow and product grids should stack to single-column below 600px. This section is a proposed responsive strategy, not an observation of actual breakpoint behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS and text extraction only; no rendered layout, computed styles, or interaction states (hover, focus, active, disabled beyond the one `.btn.primary:disabled` rule) were visually observed. Color-to-role mapping for purple, teal, and gray-purple tints is inferred from variable naming (e.g., `--c-purple`, `--c-blue`) and typical DTC subscription patterns, not confirmed against live screenshots. Typography sizes, weights, and line-heights beyond the single observed `body { line-height: 2.8rem; font-family: Gotham A, Gotham B, Calibri, Roboto, sans-serif; color: #212121 }` rule are proposed estimates following common editorial scale conventions. Gotham font availability, licensing, and exact weight files (Book/Light/Medium/Regular variants listed in evidence) were not verified — fallbacks (Calibri, Roboto, sans-serif) are assumed to render for most users. Mobile navigation, cart drawer, and quiz-step interaction patterns were not observed and are proposed only. Border-radius values or footer background were not directly confirmed for the marketing site; the `8px` radius seen is from a page-builder button widget selector, and footer color is an inferred reuse of the purple palette.
