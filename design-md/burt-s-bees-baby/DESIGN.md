---
version: alpha
name: "Burt's Bees Baby"
source_url: "https://burtsbeesbaby.com"
captured_at: "2026-09-28T04:23:08.693407+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Burt's Bees Baby's storefront CSS exposes a warm, apothecary-inspired palette
  built around a muted taupe-brown "Brand" tone (#564e4c) used for primary
  actions and ink, paired with a golden "Honey" accent (#fed16d) reserved for
  hover states across newsletter, registry, and challenge buttons. A deeper
  amber (#c9871a) and a forest teal (#095345) suggest an organic, eco-conscious
  secondary palette, while soft creams (#fcf8f2, #f2ece4) and warm neutrals
  (#dedede, #d3c9bc) form card and hairline surfaces against a white canvas.
  A muted berry red (#a22f33) appears positioned for sale or error accents.
  Typography is anchored by proxima-nova for UI text and buttons (13px/500,
  18.2px line-height, confirmed in CSS), with proxima-soft and its condensed
  variants inferred for headings, and a distinct script face, "Nicky Laatz -
  Gotcha Standup" (confirmed at 38px, lowercase text-transform), reserved for
  celebratory registry and gift-list moments — a fitting flourish for a baby
  goods brand. This interpretation extends the confirmed tokens into a full
  system: soft 4px rounding (observed on primary and challenge buttons),
  generous touch-friendly spacing, and a card-based product/registry layout
  appropriate for organic baby apparel. Hover interactions beyond the honey
  inset-shadow pattern, mobile behavior, and additional weights are inferred,
  not observed live.

colors:
  primary: "#564e4c"
  ink: "#222222"
  canvas: "#ffffff"
  body: "#555555"
  muted: "#76706a"
  hairline: "#dedede"
  surface-soft: "#fcf8f2"
  surface-card: "#f2ece4"
  on-primary: "#ffffff"
  accent-honey: "#fed16d"
  accent-honey-deep: "#c9871a"
  accent-berry: "#a22f33"
  accent-forest: "#095345"
  border-soft: "#d3c9bc"
  error: "#b0170c"
  success: "#2e7d32"
typography:
  display-xl: {fontFamily: "proxima-soft, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "proxima-soft-condensed, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  script-accent: {fontFamily: "Nicky Laatz - Gotcha Standup, cursive", fontSize: 38px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "proxima-nova, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "proxima-nova, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "proxima-nova, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "proxima-nova, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "proxima-nova, sans-serif", fontSize: 13px, fontWeight: 500, lineHeight: 18.2px, letterSpacing: 0px}
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
    padding: "13px 20px"
  button-secondary:
    backgroundColor: "transparent"
    borderColor: "{colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "13px 20px"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    accentTypography: "{typography.script-accent}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-berry}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  registry-cta:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.primary}"
    textColor: "{colors.primary}"
    accentTypography: "{typography.script-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "13px 20px"

## Components

**button-primary** uses the brand taupe as its resting fill with white text, matching the confirmed `.shopify-challenge__button` styling (13px/500 weight, 4px radius). A proposed hover state swaps to the honey accent as an inset glow with brand-colored text, mirroring the observed `:hover` shadow pattern used across newsletter and challenge buttons.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "View details"), reusing the same border and hover-honey logic inferred from primary but without a filled background.

**text-input** is a proposed form field style using the neutral hairline border and white canvas, sized for the same 13px/16px UI type scale; focus and error states are not observed and are proposed only.

**nav-bar** is inferred from typical Shopify header structure; it reuses brand-colored text on a white canvas with a light hairline division, since no header-specific selectors were captured in evidence.

**product-card** is a proposed pattern for the baby-apparel grid, using the warm cream surface-card tone and soft border to differentiate product tiles from the white page canvas, with title/price type drawn from the confirmed UI scale.

**hero** pairs the inferred display heading with the confirmed script accent face (38px, lowercase) for a warm, storybook-style banner treatment, appropriate to a baby-brand landing section; exact hero copy hierarchy is not observed.

**footer** is proposed as a brand-taupe band with white text and links, consistent with the brand color's dominant role as a dark UI surface elsewhere in the CSS (e.g., swym registry buttons).

**badge** proposes the berry accent for sale/new-arrival flags, since `#a22f33` and related red-family tones (`#d90000`, `#b0170c`) appear only as isolated palette entries with no confirmed selector role.

**search** is inferred from standard e-commerce conventions, reusing input styling; no dedicated search-bar selector was present in evidence.

**registry-cta** is a category-appropriate component directly grounded in observed evidence: the Swym registry/gift-list CSS confirms a 4px-radius, uppercase, 13px/500 button with honey-hover-inset styling, and a script-face page title at 38px lowercase — a distinctive baby-registry feature worth preserving as its own component.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | 0–599px | Single-column product grid, nav collapses to hamburger, buttons full-width |
| tablet | 600–1023px | 2-column product grid, condensed nav |
| desktop | 1024px+ | Multi-column grid, full horizontal nav, hero at full display-xl scale |

Touch targets should maintain a minimum 44px hit area on buttons and nav items (`padding: 13px 20px` plus line-height satisfies this). Navigation and filter panels are proposed to collapse into off-canvas or accordion patterns below 1024px; this is a UX recommendation, not an observed interaction.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.



- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS extraction only; no live page render, computed layout, or interaction states (hover, focus, active, error, loading) were directly observed beyond the few hover rules present in the CSS (honey inset-shadow on buttons). Font-family role assignments (proxima-nova vs. proxima-soft vs. condensed variants) are inferred from naming and typical heading/body pairing conventions, not confirmed per-selector. Spacing scale and most component padding/margins beyond the one confirmed button padding (`13px 20px`) are proposed defaults, not measured. Mobile/responsive layout, breakpoints, and menu collapse behavior are recommendations only. Availability and licensing of the custom script font "Nicky Laatz - Gotcha Standup," proxima-nova, and proxima-soft families were not verified and should be confirmed before implementation. Color-to-role mapping (e.g., which neutral serves as primary "ink" vs. "muted") is a best-effort semantic inference from CSS variable usage patterns (`--Color_Brand`, `--Color_Honey`, `--Color_White`) rather than confirmed design documentation.
