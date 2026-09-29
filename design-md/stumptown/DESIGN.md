---
version: alpha
name: "Stumptown"
source_url: "https://stumptowncoffee.com"
captured_at: "2026-09-29T03:55:26.854858+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Stumptown's storefront CSS shows a warm, matte-neutral palette anchored by a near-black ink (#1f1815) and an off-white canvas (#f6f5f3), with white (#ffffff) used for card and button surfaces. Secondary tones observed in the palette—an aged gold (#c0a868), a rust/terracotta (#cf4521), a muted forest green (#2e8b57), and a saturated link blue (#005fcc)—are treated here as inferred accent, tag, and link roles rather than confirmed brand colors, since their exact usage context in the source CSS is limited to isolated swatches. Typography is confirmed as GT Flexa (body copy, buttons, inherited by form controls), Windsor serif (all h1–h6 headings, weight 400), and GT Flexa Mono (used at least for a subscription panel heading, treated here as a label/caption face). The large list of "SC" decorative font names appears to be a theme font-picker inventory rather than confirmed in-use typography, so it is excluded from the applied type scale.
  Button styling in the CSS is inconsistent across contexts—fully pilled (50px radius) hero buttons, a 4px-radius secondary button, and a 0-radius `.btn--primary`—so this spec normalizes those into a shared radius scale while preserving both pill and soft-square button variants as legitimate, evidence-backed patterns for a coffee-subscription commerce site.

colors:
  primary: "#1f1815"
  ink: "#1f1815"
  canvas: "#f6f5f3"
  body: "#1f1815"
  muted: "#707070"
  hairline: "#d6d0c8"
  surface-soft: "#e3ded7"
  surface-card: "#ffffff"
  on-primary: "#f6f5f3"
  accent-gold: "#c0a868"
  accent-terracotta: "#cf4521"
  link: "#005fcc"
  error: "#e20000"
  success: "#2e8b57"
typography:
  display-xl: {fontFamily: "Windsor, serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Windsor, serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "'GT Flexa Mono', monospace", fontSize: 18px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.5px}
  body-md: {fontFamily: "'GT Flexa', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'GT Flexa', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "'GT Flexa Mono', monospace", fontSize: 12px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 1px}
  button-md: {fontFamily: "'GT Flexa', sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
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
    padding: "{spacing.base} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
    border: "1px solid {colors.ink}"
  button-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    border: "2px solid {colors.surface-card}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent-gold}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    typography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  subscription-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent-gold}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"

## Components
**button-primary** reflects the confirmed `.btn--primary` rule (dark ink background, off-white text, sharp corners). It is the highest-emphasis CTA, proposed for "Add to Cart" and "Subscribe" actions.

**button-secondary** mirrors the confirmed `.btn--secondary` treatment: transparent/light fill, ink border and text, smaller padding — proposed for tertiary actions like "Learn More."

**button-pill** captures the confirmed hero button pattern (50px radius, white fill, ink text, hover inversion to black/white). Proposed for promotional/hero CTAs distinct from standard commerce buttons.

**text-input** is not directly observed in the supplied CSS; its border and radius are proposed by extrapolation from the hairline and radius tokens observed elsewhere, intended for search and account forms.

**nav-bar** is inferred from the canvas background color and ink text color used sitewide; exact nav markup/height was not present in the evidence, so padding and hairline treatment are proposed.

**product-card** is inferred from the commerce content (blends, single origins, roast levels, size/quantity selectors) described in the page text; card surface, radius, and gold accent for tags are proposed, not measured.

**hero** uses the surface-soft tone as an inferred background for full-bleed promotional sections referenced in class names like `fullbleedherotwofccvfd`; typography scale is proposed since no explicit hero font-size was supplied.

**footer** is proposed as an ink-background, light-text region consistent with the dark/light contrast pattern seen in button hover states; no footer-specific CSS was supplied.

**badge** is proposed for roast-level and "EXCLUSIVE"/"MERCH" labels seen in the page text, using the terracotta accent for warmth and shelf differentiation.

**search** is proposed as a pill-shaped input consistent with the site's rounded, friendly button language; no search-bar CSS was supplied.

**subscription-selector** is a category-appropriate proposed component for the frequency dropdown ("Delivered every N weeks") and one-time/subscribe toggle referenced repeatedly in the page text, using the surface-soft and gold accent tokens.

## Responsive Behavior
Recommended (not measured) breakpoints: mobile <640px, tablet 640–1024px, desktop >1024px. Nav and filter panels are recommended to collapse into a drawer/accordion below 1024px. Touch targets for buttons and quantity steppers should be at least 44px. This is a proposed responsive strategy only; no live layout, media query, or mobile rendering was observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, JavaScript-driven interaction, or mobile viewport was observed. Several palette colors (blue #005fcc, red #e20000, green #2e8b57, blues #789bbc/#1990c6/#136f99) appear in the raw swatch list without clear selector context, so their semantic roles (link, error, success, informational) are inferred, not confirmed. The large "SC ..." font list is assumed to be an unused theme font-picker inventory rather than applied typography. Font licensing/availability for GT Flexa, GT Flexa Mono, and Windsor was not verified. All spacing and sizing values not directly tied to a supplied CSS declaration (hero type sizes, card padding, input styling, breakpoints) are proposed placeholders for design consistency, not measured facts.
