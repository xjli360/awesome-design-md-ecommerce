---
version: alpha
name: "Toddlekind"
source_url: "https://toddlekind.com"
captured_at: "2026-09-28T09:59:12.589681+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Toddlekind's storefront evidence points to a warm, muted, "quiet luxury" palette built
  around a deep cocoa-brown (#66402e), used as both primary accent and default text/body
  color, set against a soft warm-ivory canvas (#f1ece5) and off-white card surfaces. A
  secondary taupe-brown (#6f5e54) drives primary buttons, while a dusty sage (#a8b8a3)
  appears explicitly as a hover/interaction accent, reinforcing an organic, nursery-safe
  feel appropriate to a non-toxic playmat brand. Panel and header backgrounds (#ede7de,
  #f6eee9, #f7f3ec) are inferred as layered "soft surface" tones for footers, side panels,
  and section backgrounds. A muted gray (#8a8a8a) is used for subheader/secondary text,
  and a bright red (#e93636) is treated here as an inferred sale/error accent.
  Typography pairs a serif display face, "Canela Deck" (headings h1-h5, weight 400, zero
  letter-spacing), with a grotesk sans body face, "Neue Haas Grotesk Text Pro" (18px,
  180% line-height, 1px letter-spacing) — an editorial-meets-clean-DTC pairing consistent
  with a premium, design-forward baby-gear brand. All sizes beyond the two CSS-confirmed
  values are proposed and labeled as such. Border-radius is inferred as subtle (4px
  observed on a hero button) rather than sharp or fully rounded.

colors:
  primary: "#66402e"
  ink: "#66402e"
  canvas: "#f1ece5"
  body: "#66402e"
  muted: "#6f5e54"
  hairline: "#e6e6e6"
  surface-soft: "#f7f3ec"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#a8b8a3"
  surface-panel: "#ede7de"
  surface-header: "#f6eee9"
  muted-text: "#8a8a8a"
  border-strong: "#cacaca"
  sale: "#e93636"
typography:
  display-xl: {fontFamily: "Canela Deck, serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: 0px}
  display-md: {fontFamily: "Canela Deck, serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Canela Deck, serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Neue Haas Grotesk Text Pro, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.8, letterSpacing: 1px}
  body-sm: {fontFamily: "Neue Haas Grotesk Text Pro, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.5px}
  caption: {fontFamily: "Neue Haas Grotesk Text Pro, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Neue Haas Grotesk Text Pro, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 1px}
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
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    hoverBackgroundColor: "{colors.accent-sage}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    hoverBackgroundColor: "{colors.accent-sage}"
    hoverTextColor: "{colors.on-primary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border-strong}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    priceTypography: "{typography.body-md}"
    titleTypography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    headlineTypography: "{typography.display-xl}"
    subtextTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-panel}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  trust-badge-strip:
    backgroundColor: "{colors.surface-header}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"

## Components

**button-primary** — Uses the taupe-brown `muted` tone (observed as `--color-btn-prime-bg`) against white text, matching the site's confirmed primary CTA styling; hover state to sage (`accent-sage`) is directly observed in supplied CSS on hero/background-video buttons. Radius is set to the observed 4px value.

**button-secondary** — An outline treatment on the warm canvas background, using the cocoa `primary` color for border and text. Hover-to-sage fill is proposed by extension of the observed primary hover pattern, not separately confirmed for outline buttons.

**text-input** — Proposed form-field styling using card-white background and a neutral gray border (`border-strong`, from the observed `#cacaca` small-heading color, repurposed here as a hairline/border tone). Sizing and padding are proposed, not measured.

**nav-bar** — Inferred top navigation bar on the warm canvas background, holding the mega-menu structure implied by the "Shop by Collection / Shop by Color" text content. Exact height, sticky behavior, and mobile collapse are not observed.

**product-card** — Represents the playmat/essentials grid items (e.g., "Haven Playmat Linear - Linen $135"). Title uses the serif display typography per the site's heading rule; price uses body typography. Card chrome (border, radius, padding) is proposed based on general Shopify-card conventions, not directly measured.

**hero** — Large homepage banner ("A better playmat for modern homes") using the soft cream (`surface-soft`) background and serif display headline, consistent with the accent-bg token observed in `:root`. Copy block width, image placement, and CTA alignment are inferred, not measured.

**footer** — Uses the darker panel tone (`surface-panel`, from `--bg-color-side-panel-footer`) which is explicitly defined in the CSS as a footer/side-panel background, paired with body-sm typography for link lists.

**badge** — A sale/discount marker (e.g., "$108 $135") styled with the red tone (`sale`) present in the observed palette; role as a discount badge is inferred, as the source CSS does not explicitly label this color's usage.

**search** — Proposed search input treatment, styled consistently with `text-input`, for the site's predicted header search affordance; not directly observed in supplied evidence.

**trust-badge-strip** — A category-appropriate component reflecting the repeated "100 DAY RISK-FREE TRIAL • FREE SHIPPING OVER $150" announcement bar and the "Tested to EU & US standards / Non-toxic / EcoPure®" certification list seen in page text. Uses the light header tone (`surface-header`, from `.side-panel-header` background) and caption-scale typography for dense, small-print trust messaging typical of a safety-certified children's gear brand.

## Responsive Behavior

Breakpoint values below are a proposed convention only; a font-family token string in the supplied evidence (`small=0em&medium=48em&large=66.75em&xlarge=75em`) suggests a 4-tier system, which this table approximates:

| Tier | Width | Notes (proposed) |
|------|-------|-------------------|
| small | 0–47.9em | Single-column stack, nav collapses to hamburger/side-panel |
| medium | 48em–66.7em | 2-column product grid, condensed nav |
| large | 66.75em–74.9em | 3-column product grid, full nav visible |
| xlarge | ≥75em | 4-column product grid, max-width content container |

Touch targets for buttons and nav items should maintain a minimum 44px hit area on small/medium tiers. Mega-menu category lists ("Shop by Collection", "Shop by Color") are expected to collapse into an accordion or side-panel drawer below the medium breakpoint. This table is a recommendation derived from a size-token naming convention found in the evidence, not a measurement of actual rendered layout.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is generated from static CSS/text extraction only; no live rendering, interaction states, or responsive behavior were observed. The semantic roles assigned to several colors (e.g., `sale` as a discount-badge color, `hairline`/`border-strong` as border tones) are inferred from adjacent CSS usage, not explicit design labels. All typography sizes beyond the two directly confirmed values (heading font-family/weight/letter-spacing, and body 18px/180%/1px) are proposed placeholders following a conventional type scale. Component padding, radius (beyond the one observed 4px button radius), hover/focus/active states for most components, mobile navigation behavior, and search-affordance existence are not confirmed by supplied evidence. Availability and licensing of "Canela Deck" and "Neue Haas Grotesk Text Pro" as web fonts have not been verified; generic serif/sans-serif fallbacks are provided per instruction. The breakpoint table is a proposed convention, not a measured layout.
