---
version: alpha
name: "Lick"
source_url: "https://lick.com"
captured_at: "2026-09-28T09:37:56.153188+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Lick's public storefront presents a neutral, gallery-like backdrop so that paint and wallpaper colour remains the visual protagonist. Observed CSS exposes a near-black ink (#1a2023) and a warmer slate (#354147) for text and structural chrome, set against whites and off-whites (#ffffff, #fafafa, #f2f2eb) with soft warm-grey hairlines (#dedede, #ebeced, #c2c6c8). A small saturated accent set — teal-blue (#1990c6/#136f99), coral (#ff6b64), green (#1db86a), mustard (#e8be62) and rust (#c05717) — appears alongside semantic red (#ff0000) and tinted state backgrounds (#e9fcf2, #ffe5e5), suggesting these are used for links, badges, status messaging and swatch-style accents rather than a single fixed brand colour. Two font families are declared: Basis Grotesque Pro (with a Mono variant) for interface text, and Clearface, a serif, reserved here for larger editorial headlines — an inferred pairing of utilitarian UI type with a more expressive display face, consistent with a design-led home brand. Component roles below (buttons, cards, swatches, nav) are proposed interpretations built from the token evidence; exact hex-to-role assignments, spacing, and radii are not directly measured from layout and are marked as inferred or proposed throughout.

colors:
  primary: "#1a2023"
  ink: "#354147"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#8f9699"
  hairline: "#dedede"
  surface-soft: "#f2f2eb"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  border-subtle: "#ebeced"
  border-strong: "#c2c6c8"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  accent-coral: "#ff6b64"
  accent-green: "#1db86a"
  accent-mustard: "#e8be62"
  accent-rust: "#c05717"
  error: "#ff0000"
  error-bg: "#ffe5e5"
  success-bg: "#e9fcf2"
  overlay-dark: "#0000004d"
  overlay-light: "#ffffffa6"
typography:
  display-xl: {fontFamily: "Clearface, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Clearface, serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Basis Grotesque Pro, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Basis Grotesque Pro, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Basis Grotesque Pro, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Basis Grotesque Pro Mono, monospace", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Basis Grotesque Pro, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    border: "1px solid {colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.border-subtle}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.border-subtle}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  colour-swatch:
    shape: "circle or rounded square, size proposed 40px-64px"
    rounded: "{rounded.full}"
    border: "1px solid {colors.border-subtle}"
    selectedRing: "2px solid {colors.accent-blue}"
    labelTypography: "{typography.caption}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    overlay: "{colors.overlay-dark}"
    titleTypography: "{typography.display-xl}"
    titleColorOnDark: "{colors.on-primary}"
    contentColorOnDark: "{colors.overlay-light}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.overlay-light}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.accent-green}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components
**button-primary** uses the near-black ink token as a stable, colour-neutral call-to-action background so it doesn't compete with paint colour imagery; hover/active states are proposed, not observed. **button-secondary** is an outlined variant for lower-emphasis actions such as "Add sample," using the same ink for text and a mid-grey border. **text-input** assumes a simple bordered field consistent with the light canvas and hairline greys seen across the palette; focus-state colour is proposed. **nav-bar** reflects the multi-level mega-menu structure implied by the extensive text excerpt (Paint, Wallpaper, Tools, Consultations, About, Trade), styled with a light background and subtle bottom border. **product-card** is inferred for basket/recommendation modules ("You may also like," tool add-ons), using the near-white card surface and subtle border to separate items on the white canvas. **colour-swatch** is a category-appropriate component for paint/wallpaper selection UI, proposed as circular chips since no literal shape was observed, with a blue selection ring drawn from the evidenced accent-blue. **hero** models the "cm-full-bleed" light/dark theme classes found in the CSS, where light-theme hero text uses an inverse (white) colour and dark-theme text uses standard ink tokens — this dual-theme hero pattern is directly evidenced by selector names, though exact colours are var()-driven and not hex-resolved. **footer** and **search** are structurally proposed from typical e-commerce conventions and the site's evidenced link list, using ink and surface tokens for consistency; interaction states throughout are labeled proposed.

## Responsive Behavior
Recommended, not measured: mobile <480px (single-column stacks, nav collapses to drawer per the "Back" menu labels in the text excerpt, which suggest a slide-in mobile navigation), tablet 480–1024px (2-column product grids), desktop >1024px (mega-menu nav bar, multi-column footer). Touch targets should be at least 44px; the mobile menu's repeated "Back" affordance implies a nested drawer pattern rather than flat dropdowns. All breakpoint values are proposed defaults, not extracted from the supplied CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom-property names, a color list, font-family declarations, and page text — no rendered layout, computed box model, or live interaction states were observed. Role assignments for individual hex values (e.g., which accent is "the" brand colour vs. a status or swatch colour) are inferred from naming context and general e-commerce convention, not confirmed usage. All font sizes, weights, line-heights, spacing, and radii are proposed design-system values unless a literal declaration was present, which was not the case here. Mobile menu, hover, focus, and error-state visuals are assumed patterns, not verified. Clearface and Basis Grotesque Pro are custom/licensed fonts; their availability, licensing terms, and exact weight range were not verified from the supplied evidence.
