---
version: alpha
name: "Wild Alaskan Company"
source_url: "https://wildalaskancompany.com"
captured_at: "2026-09-28T04:34:36.765634+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Wild Alaskan Company's marketing stylesheet establishes a coastal, editorial palette anchored by a deep navy (#0d334c) used for all headings and primary buttons, paired with a warm red-orange (#d63518) as the Bootstrap "danger" accent. Body copy runs in a near-black (#212529) on white (#ffffff), with light grey-blue surfaces (#f8f9fa, #e7edf1) available for cards and sectioning, and a soft hairline (#dee2e6) for dividers and input borders. A muted slate (#6f828f) doubles as the Bootstrap secondary color and a probable caption/label tone.

  Typography is explicitly dual-family: headings use "adonis-web, serif" at a forced 400 weight, giving the brand a quieter editorial serif voice rather than a bold display face, while body text and UI controls use "canada-type-gibson, sans-serif." A monospace stack (SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New) is present for code/tabular contexts. Additional families ("Wild Alaskan Sans," "Wild Alaskan Serif") appear in the asset bundle but are not confirmed mapped to specific selectors, so they are treated as available-but-unverified.

  This interpretation proposes a clean, trust-forward e-commerce system: navy-led CTAs, generous whitespace, rounded-sm controls (.25rem observed on buttons), and success/warning/info accents reserved for order-status and freshness messaging.

colors:
  primary: "#0d334c"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#212529"
  muted: "#6f828f"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#e7edf1"
  on-primary: "#ffffff"
  secondary: "#6f828f"
  danger: "#d63518"
  danger-strong: "#a82a13"
  success: "#23d080"
  success-strong: "#1ca465"
  warning: "#ffc107"
  info: "#17a2b8"
  dark: "#343a40"
  accent-orange: "#ed6226"
  accent-teal: "#00ccc5"
  overlay-primary: "#0d334c40"
typography:
  display-xl: {fontFamily: "adonis-web, serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "adonis-web, serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "adonis-web, serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "canada-type-gibson, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "canada-type-gibson, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "canada-type-gibson, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "canada-type-gibson, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
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
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
    border: "1px solid {colors.secondary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    hairline: "{colors.hairline}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    overlay: "{colors.overlay-primary}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    hairline: "{colors.muted}"
  badge:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  subscription-plan-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent-orange}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    hairline: "{colors.hairline}"

## Components

**button-primary** uses the observed `.btn-primary` navy fill with white text, matching the confirmed hover-darkening pattern (#071d2b/#061620) from the stylesheet; radius follows the `.25rem` Bootstrap default (`rounded.sm`). Proposed as the default checkout/add-to-box action.

**button-secondary** maps to the observed `.btn-secondary` slate (#6f828f) fill, intended for lower-emphasis actions like "Skip a Delivery" or "Edit Plan." Hover/focus darkening states are proposed by analogy to the primary button's documented pattern, not independently confirmed.

**text-input** is a proposed pattern using the Bootstrap hairline (#dee2e6) as border color, since dedicated input styling was not present in the supplied CSS excerpt; padding and radius follow the button system for visual consistency.

**nav-bar** is proposed as a white, primary-navy-text header bar, inferred from the heading color token and absence of any dark-mode header rule in the evidence; hairline divider uses the observed `#dee2e6`.

**product-card** (e.g., a seafood SKU tile) uses the light blue-tinted `#e7edf1` surface for differentiation from pure white canvas, with a serif title and sans-serif body—an inferred pairing based on the confirmed heading/body font split.

**hero** is a proposed full-bleed navy section using `overlay-primary` (`#0d334c40`) for image-darkening treatments, consistent with the alpha-variant primary color present in the palette (`#0d334c40`).

**footer** uses the observed dark gray (`#343a40`, the Bootstrap `--dark`/`--gray-dark` token) as background with white text, a common pattern though not directly observed in the supplied rule set.

**badge** proposes the success green (`#23d080`) for freshness/availability tags ("Wild-Caught," "In Stock"), fully rounded per `rounded.full`; this semantic use of green-as-positive is inferred from Bootstrap convention, not brand-specific evidence.

**search** is a proposed light (`#f8f9fa`) input treatment for site search, distinguished from standard form fields by background only.

**subscription-plan-card**, a category-specific component for this seafood-subscription business, proposes an orange accent (`#ed6226`, observed in palette but unmapped) to highlight plan tiers or "Most Popular" flags, on an otherwise neutral white card.

## Responsive Behavior

*Recommendation only — no responsive/mobile layout was observed in the supplied evidence.* Bootstrap's default breakpoints are present in `:root` (`--breakpoint-sm:576px; -md:768px; -lg:992px; -xl:1200px`) and are proposed as the structural basis:

| Breakpoint | Width | Layout guidance |
|---|---|---|
| xs | 0–575px | Single-column stack; nav collapses to a hamburger/drawer (proposed) |
| sm | 576–767px | Two-column product grids begin |
| md | 768–991px | Three-column product/subscription grids |
| lg | 992–1199px | Full nav bar, four-column grids |
| xl | 1200px+ | Max-width container, generous section padding (`spacing.section`) |

Touch targets should maintain a minimum 44px height for buttons and inputs on xs/sm; the nav should collapse below `md` per typical Bootstrap-derived patterns. None of this collapse/drawer behavior was directly verified in the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from a static CSS/color/font extraction only; no live rendering, computed layout, or DOM structure was observed. Component states (hover, focus, active, disabled) are documented only where the source CSS explicitly provided them (e.g., `.btn-primary`, `.btn-secondary`); all other interaction states are proposed by pattern-matching to Bootstrap conventions and are not verified. Semantic color-role mapping (e.g., treating `#e7edf1` as a card surface, `#ed6226` as a subscription accent) is inferred from adjacency in the palette, not from confirmed selector usage. All pixel sizes in `typography` beyond the confirmed `1rem` body/button size are proposed defaults, not measured values. Mobile/tablet layout, navigation collapse behavior, and touch interactions were not observed. Availability, licensing, and web-embedding rights for "adonis-web," "canada-type-gibson," "Wild Alaskan Sans," and "Wild Alaskan Serif" have not been verified; generic serif/sans-serif fallbacks are assumed in production use.
