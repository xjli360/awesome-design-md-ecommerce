---
version: alpha
name: "Smalls"
source_url: "https://smalls.com"
captured_at: "2026-09-28T04:17:17.873619+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Smalls presents as a warm, editorial DTC pet-food brand built on a cream
  canvas rather than clinical white, paired with near-black ink and slate-gray
  body copy for a grounded, human-grade tone. The palette observed in the
  stylesheet includes a deliberate bright yellow (`--color-yellow`, #ffec66)
  used explicitly for focus-visible outlines and expanded-state borders,
  making it the most defensible interactive/accent color in the system; a
  deeper gold (#f2ba36) likely serves as a secondary accent or CTA fill. Sage
  and olive tones (#bbc692, #c9d6ab, #61704d) suggest a nature/ingredient
  motif appropriate to a fresh-food brand, while burnt orange (#c75100) and
  blue (#155dfc) appear as supporting accent or link colors. Colors matching
  PayPal's brand (#003087, #ffc439) are treated as third-party payment-badge
  artifacts, not part of Smalls' own identity, and are excluded from the core
  token set. Typography draws on three observed font families — Adieu,
  Monument, and Yorick — mapped here by inferred role: Monument for bold
  display headlines, Yorick as a serif accent for editorial moments, and
  Adieu for body and UI text. All sizing, weights, and component patterns
  below are proposed conventions, not measured layout.

colors:
  primary: "#ffec66"
  ink: "#1a1d21"
  canvas: "#efece6"
  body: "#363b42"
  muted: "#6a7282"
  hairline: "#0000001a"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#1a1d21"
  accent-gold: "#f2ba36"
  accent-sage: "#bbc692"
  accent-olive: "#61704d"
  accent-orange: "#c75100"
  accent-blue: "#155dfc"
  success: "#0a7b09"
  surface-dark: "#23272c"
  overlay-scrim: "#000000b3"
typography:
  display-xl: {fontFamily: "Monument, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Monument, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Yorick, serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Adieu, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Adieu, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Adieu, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Adieu, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineBottom: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  plan-builder-step:
    backgroundColor: "{colors.surface-card}"
    accentBorder: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"

## Components
- **button-primary** — proposed as the main conversion action (e.g. "Get Started"), using the observed bright-yellow interactive color for strong contrast against the cream canvas.
- **button-secondary** — an outline pattern for lower-priority actions, sharing the canvas background with a hairline border for restrained emphasis.
- **text-input** — a card-toned field for account, checkout, or plan-builder forms; focus-state styling in the source CSS suggests visible outline treatment, proposed here as a border-color swap.
- **nav-bar** — cream-toned header assumed from canvas usage sitewide; sticky/collapse behavior is not observed and is proposed only.
- **product-card** — used for meal or product tiles; white surface against cream canvas creates card separation, rounded corners proposed for a soft, approachable feel.
- **hero** — large display headline area on the homepage; typography scale is proposed since no explicit hero selector was captured in evidence.
- **footer** — dark surface variant reversing text to white, consistent with the darker palette entries (#1a1d21/#23272c) observed.
- **badge** — small sage-toned pill for tags like "human-grade" or "fresh," a proposed ingredient/quality callout rather than an observed component.
- **search** — pill-shaped input, proposed for site or help-center search, not confirmed present on the page.
- **plan-builder-step** — a category-specific component for the cat-profile/subscription flow typical of Smalls' funnel, using the primary yellow as a step-accent border; content and states are proposed, not observed.

## Responsive Behavior
Recommended breakpoints (not measured): mobile ≤480px, tablet 481–768px, desktop 769–1200px, wide ≥1201px. Nav and plan-builder steps are expected to collapse to single-column stacks below tablet width, with product-card grids reducing from multi-column to 1–2 columns. Touch targets should maintain a minimum 44×44px hit area for buttons and badges. This section is a general recommendation only; no live responsive or interaction behavior was observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived solely from static CSS/color extraction and a single page title; no rendered layout, spacing, or interaction states were observed. Role assignments for colors (e.g., primary vs. secondary accent, success/error) are inferred from usage context in CSS selectors and general DTC-brand convention, not confirmed via design files. Font-to-role mapping (Adieu/Monument/Yorick) is inferred from naming and typical display/body pairing, not from explicit selector-to-family CSS rules. All typographic sizes, weights, spacing scale, and rounded-corner values are proposed conventions unless a matching CSS declaration was directly supplied. Component states (hover, disabled, error) are proposed and unverified. Font licensing, availability, and self-hosting status for Adieu, Monument, and Yorick were not verified. Mobile layout, breakpoint behavior, and any JavaScript-driven interactions (e.g., the focus/expand selectors seen in evidence) were not observed in a live browser session.
