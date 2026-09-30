---
version: alpha
name: "Shure"
source_url: "https://www.shure.com"
captured_at: "2026-09-28T04:08:01.395065+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Shure's public CSS evidence reveals a utilitarian, high-contrast commerce
  interface layered over a technical audio-brand identity. The dominant
  neutral is near-black (#151515) paired with pure white (#ffffff), producing
  strong legibility for product data — titles, prices, and quantity labels
  all render in this ink tone. A single vivid signature accent, lime-green
  (#b2ff33), appears consistently as an underline bar beneath CTA buttons and
  as the hover fill for add-to-cart controls, marking it as Shure's primary
  interactive color despite its rarity in the raw palette. Supporting
  neutrals (#b2b2b4, #626264, #f7f7f8, #ececed, #dddddd) form a layered gray
  system for borders, muted text, and card surfaces. A broader secondary
  palette (blues, reds, greens, warm tans) appears only in isolated
  third-party widget contexts (reviews, retail-solutions) and is treated here
  as inferred status/accent color, not confirmed core brand identity.
  Typography relies almost entirely on a proprietary DinRegular/DinBold
  pairing — bold for buttons, prices, and headlines; regular for body copy —
  with an OstrichProper display family present in the font stack, interpreted
  as an inferred large-headline face pending live confirmation. The resulting
  system favors dense, functional product-commerce patterns over decorative
  styling, consistent with a professional audio-equipment retailer.

colors:
  primary: "#b2ff33"
  ink: "#151515"
  canvas: "#ffffff"
  body: "#626264"
  muted: "#8c8c8e"
  hairline: "#dddddd"
  surface-soft: "#f7f7f8"
  surface-card: "#ececed"
  on-primary: "#000000"
  ink-soft: "#404041"
  border-strong: "#b2b2b4"
  overlay: "#151515bf"
  accent-blue: "#0969a9"
  accent-cyan: "#00bbff"
  success: "#319e01"
  danger: "#c01f22"
  warning: "#ffaa00"
typography:
  display-xl: {fontFamily: "'OstrichProperExtraBold', 'DinBold', Arial, sans-serif", fontSize: 56px, fontWeight: 800, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "'DinBold', Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "'DinBold', Arial, Helvetica, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'DinRegular', Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'DinRegular', Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "'DinRegular', Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  button-md: {fontFamily: "'DinBold', Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    hoverBackgroundColor: "{colors.primary}"
    hoverTextColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    hoverBackgroundColor: "{colors.surface-soft}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleColor: "{colors.ink}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.display-md}"
    priceColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    accentUnderlineColor: "{colors.primary}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink-soft}"
    textColor: "{colors.muted}"
    dividerColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  product-carousel:
    arrowBackgroundColor: "{colors.overlay}"
    arrowTextColor: "{colors.canvas}"
    arrowRounded: "{rounded.full}"
    bulletColor: "{colors.ink-soft}"
    bulletActiveColor: "{colors.primary}"
    priceTypography: "{typography.display-md}"
    priceColor: "{colors.ink}"

## Components

**button-primary** is the core add-to-cart / conversion action, defaulting to an ink-on-white treatment and swapping to the lime accent with black text on hover — the hover values are directly observed in the retail-solutions stylesheet; the default (non-hover) fill is a proposed inference for visual balance.

**button-secondary** proposes an outlined, low-emphasis alternative for secondary actions (e.g., "Learn more"), using the same hairline gray as card and input borders observed across components.

**text-input** models form fields (search, forms, quantity entry) on the light gray surface tone used elsewhere for cards, with a primary-colored focus ring proposed for accessibility since no focus state was captured in the evidence.

**nav-bar** is inferred from general e-commerce convention combined with the observed light canvas and dark-ink text pairing; no header markup or scroll-state styling was present in the supplied CSS.

**product-card** reflects directly observed rules: 14px ink-colored product titles and bold ink-colored pricing, wrapped in a soft neutral surface with a subtle hairline border — the card container styling itself is a proposed structural interpretation.

**hero** is a proposed large-format banner pattern using the display typography scale and the lime accent bar seen underlining CTA buttons, projected here as a section-level accent treatment; no hero markup was observed.

**footer** proposes a dark, low-contrast informational band consistent with the darker neutrals (#404041, #222222 family) present in the palette; footer content and structure were not present in the evidence.

**badge** repurposes the primary lime accent as a small pill label (e.g., "New," "Best Seller"), a proposed pattern justified by the accent's existing use as a high-visibility highlight color.

**search** is a proposed lightweight input variant sharing styling with text-input, appropriate for a product-catalog site of this type; not directly observed.

**product-carousel** is the category-appropriate component, grounded in directly observed retail-solutions carousel CSS: circular semi-transparent arrow buttons (#151515bf), small bullet indicators, and bold Din-family pricing at 1.5rem — the active/inactive bullet color logic is proposed.

## Responsive Behavior

This is a recommended structure, not measured site behavior — no live breakpoints, container queries, or responsive markup were present in the supplied evidence.

| Breakpoint | Range | Layout guidance (proposed) |
|---|---|---|
| Mobile | <480px | Single-column stacking; nav collapses to a hamburger/menu icon; carousels become swipeable single-item views. |
| Tablet | 481–1024px | 2-column product grids; condensed nav with visible primary actions. |
| Desktop | 1025–1440px | 3–4 column product grids; full horizontal nav; carousel arrows visible on hover. |
| Wide | >1440px | Content max-width container with increased whitespace; grid columns unchanged from desktop. |

Touch targets should maintain a minimum 44×44px hit area for carousel arrows, bullets, and buttons, as the observed 30px arrow width and 13px bullet size are visually small and likely rely on padding for usable touch area. Navigation collapse and menu interaction patterns are proposed conventions, not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS fragments and a page title; no live DOM, computed layout, or JavaScript-driven interaction states were captured. The mapping of colors to semantic roles (primary, danger, success, warning, accent-blue, accent-cyan) is inferred from typical usage patterns and limited third-party widget context, not confirmed brand guidelines — several colors (e.g., warm tans, pinks, additional blues) originate from unidentified components and may not represent core Shure brand colors at all. Typography sizes for display-xl, display-md, title-md, and hero contexts are proposed estimates; only body-sm (14px), caption (12px), button-md (16px/700), and a 24px/1.5rem heading size were directly observed. The OstrichProper font family's actual rendered usage, weight mapping, and licensing/availability were not verified — it is included in the stack but no selector-level usage was captured. Hero, nav-bar, footer, search, and badge components are structurally proposed and were not present in the supplied CSS. No responsive breakpoints, hover/focus states beyond the documented add-to-cart hover, or mobile navigation behavior were observed; all such guidance above is a recommendation only.
