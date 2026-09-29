---
version: alpha
name: "Maxbone"
source_url: "https://maxbone.com"
captured_at: "2026-09-28T04:17:38.358379+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Maxbone's storefront CSS shows a restrained, editorial palette built on true black
  (#000000) and near-black charcoal (#231f20) against white (#ffffff) and off-white
  surfaces (#fafafa, #f5f5f5, #f1d9b2). Buttons use sharp, un-rounded corners (no
  border-radius observed on .btn), 2px borders, and a color-swap hover pattern
  (dark-to-white, white-to-dark), suggesting a minimal, contrast-driven interaction
  language rather than soft, rounded affordances. Warm tan/gold tones (#b88b4e,
  #ceb198, #c6ae92) and a soft blush (#ecb4ac) appear in the palette and are treated
  here as inferred accent colors for pet-product imagery and seasonal callouts,
  since their exact UI role is not confirmed by the extracted rules. The body font
  is explicitly declared as GoodSans; the long list of additional families
  (Apercu, Graphik, Karla, Oswald, Ringside, Minion Pro, Berlingske Serif XCn,
  system stacks) is treated as inferred/uncertain — likely a mix of third-party
  widget fonts (reviews, icons) and system fallbacks rather than confirmed brand
  typefaces. This spec proposes a clean, high-contrast e-commerce system: black/
  charcoal actions on white canvas, tan/blush used sparingly as accent, sharp
  corners as default with a small rounded scale reserved for cards and inputs.

colors:
  primary: "#231f20"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#707070"
  hairline: "#e5e5e5"
  surface-soft: "#f5f5f5"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-blush: "#ecb4ac"
  accent-gold: "#b88b4e"
  accent-tan: "#f1d9b2"
  accent-navy: "#002d56"
  alert: "#9c0808"
typography:
  display-xl: {fontFamily: "GoodSans, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "GoodSans, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "GoodSans, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "GoodSans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "GoodSans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "GoodSans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "GoodSans, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.5px}
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
    padding: "{spacing.none} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.none} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineBottom: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    imageAspect: "1:1 (proposed)"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    overlayTint: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-blush}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  pet-size-selector:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    activeBorder: "{colors.primary}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.md}"

## Components
**button-primary** renders solid charcoal (#231f20) with white text, matching the observed `.btn-primary.m-black` border/color pair and its hover inversion to white; sharp corners follow the absence of border-radius on `.btn`. **button-secondary** mirrors the ghost/outline treatment seen in `.btn-ghost` and `.m-white` variants, using a 2px border and transparent fill, with hover swapping fill/border per the observed color-inversion pattern. **text-input** is a proposed pattern (no explicit input styling was captured); it borrows the hairline gray (#e5e5e5) and a small radius consistent with a minimal, editorial form language. **nav-bar** is inferred as a white, top-fixed bar with dark text and a thin hairline divider, typical of Shopify header patterns; exact sticky/scroll behavior is not observed. **product-card** proposes a soft off-white card surface (#fafafa) for grid listings, with title/price typography drawn from the body/title scale; image treatment and hover states are proposed, not measured. **hero** uses the dark ink background with white text for a bold, full-bleed banner feel appropriate to a lifestyle pet brand; copy hierarchy uses the display scale. **footer** is proposed as a dark, full-width block echoing the hero's ink/white contrast, with hairline separators between link columns. **badge** (e.g., "New" or "Sale" tags) uses the blush accent (#ecb4ac) as a soft, non-alarming highlight color, pill-shaped per the full-radius token. **search** proposes a light, bordered field distinct from primary CTAs. **pet-size-selector** is a category-specific proposed component for apparel/collar sizing, using bordered chips with a primary-colored active state, since size/fit selection is a functional need for pet apparel but was not present in the extracted CSS.

## Responsive Behavior
Recommended, not measured, breakpoints:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <768px | Single-column product grid, collapsed nav to hamburger menu, sticky add-to-cart bar (proposed) |
| Tablet | 768–1024px | Two-column product grid, condensed nav |
| Desktop | 1024–1440px | Full nav bar, 3–4 column product grid |
| Wide | >1440px | Max-width content container, increased whitespace |

Touch targets should maintain a minimum 40px height, matching the observed `.btn` height. Nav and filter menus are expected to collapse into an off-canvas or accordion pattern on mobile; this is a proposed convention, not confirmed by extracted markup.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS extraction only; no live rendering, DOM inspection, or JavaScript-driven state (hover, focus, open menus, cart drawer) was observed. Semantic color roles (primary, muted, hairline, surface tiers) are inferred from selector names and usage context, not confirmed via visual screenshots. Typography sizes beyond the single confirmed `font-size:16px` body rule are proposed, not measured. The large list of font families in evidence likely includes third-party widget/icon fonts (e.g., `oke-reviews-icons`) and generic system fallbacks; only `GoodSans` is confirmed as an intentionally declared brand body font, and its licensing/availability has not been verified. Mobile layout, breakpoint values, and interaction states (button hover beyond the two captured rules, form validation, cart behavior) are not observed and are marked as proposed throughout.
