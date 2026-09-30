---
version: alpha
name: "Husky Liners"
source_url: "https://huskyliners.com"
captured_at: "2026-09-28T04:58:27.212311+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Husky Liners' storefront runs on a Nuxt/Tailwind-based design system exposing
  CSS custom properties for color, type scale, and spacing. The functional
  palette centers on a bright automotive yellow (#ffc600, --colorPrimary)
  against near-black text (#1e1e1e, --colorBlack) and a pure white canvas,
  reinforced by mid-gray body copy (#333333) and lighter grays for muted UI
  (#767676, #d5d5d5, #f3f3f3). A cyan/blue action color (#0194ca) and a small
  status set (success #15884f, warning #fa6400, danger #f2603e, info #31b7d1)
  are defined as CSS variables, inferred here to drive links, alerts, and
  fitment-tool states. Typography uses two vendor-labeled tokens,
  'PlatformFont' and 'PlatformBrandFont', with a numeric scale from 12px to
  72px and weights 400/700/900; h1 is confirmed uppercase, extrabold, and
  forced to line-height 1, which anchors the display styles below. Spacing is
  built on an observed 4px root unit (--spacing: .25rem). Rounded corners are
  not demonstrated beyond a 0px reset on form controls, so the radius scale
  here is a restrained, proposed convention for a rugged, functional
  truck/SUV-accessory brand rather than a soft consumer-lifestyle one.

colors:
  primary: "#ffc600"
  ink: "#1e1e1e"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#767676"
  hairline: "#d5d5d5"
  surface-soft: "#f3f3f3"
  surface-card: "#fafafa"
  on-primary: "#1e1e1e"
  action: "#0194ca"
  success: "#15884f"
  warning: "#fa6400"
  danger: "#f2603e"
  info: "#31b7d1"
  info-dark: "#23889b"
  tint-info: "#ecf6fd"
  tint-warning: "#fff8de"
typography:
  display-xl: {fontFamily: "'PlatformBrandFont', sans-serif", fontSize: "60px", fontWeight: 900, lineHeight: 1, letterSpacing: "-0.025em"}
  display-md: {fontFamily: "'PlatformBrandFont', sans-serif", fontSize: "36px", fontWeight: 900, lineHeight: 1, letterSpacing: "-0.025em"}
  title-md: {fontFamily: "'PlatformFont', sans-serif", fontSize: "24px", fontWeight: 700, lineHeight: 1.25, letterSpacing: "normal"}
  body-md: {fontFamily: "'PlatformFont', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "normal"}
  body-sm: {fontFamily: "'PlatformFont', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "normal"}
  caption: {fontFamily: "'PlatformFont', sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.375, letterSpacing: "normal"}
  button-md: {fontFamily: "'PlatformFont', sans-serif", fontSize: "14px", fontWeight: 700, lineHeight: 1, letterSpacing: "0.5px"}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkColor: "{colors.action}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.tint-warning}"
    textColor: "{colors.warning}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.md}"
  vehicle-selector:
    backgroundColor: "{colors.canvas}"
    accentColor: "{colors.action}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"

## Components
button-primary is the yellow, extrabold-weighted call-to-action ("Shop Now") used against dark or white backgrounds; hover/active states are proposed, not observed. button-secondary is an outlined variant for lower-emphasis actions like "Browse by Vehicle." text-input represents standard form fields (e.g., search, contact); border and radius values are proposed conventions since the reset CSS only confirms `border-radius:0` on raw form elements. nav-bar models the top utility bar and mega-menu trigger row ("Shop All," "Browse by Make and Model"); its light background and dark text follow the body/canvas tokens directly. product-card covers listing tiles for items like Weatherbeater and X-act Contour floor liners, using the off-white surface-card tone to separate it from the pure-white canvas. hero maps to large campaign banners such as "TOTAL VEHICLE PROTECTION," pairing the near-black ink background with the primary yellow accent for headline emphasis. footer is a muted, low-contrast band for legal and secondary links. badge is a small pill for labels like "ALL-NEW," styled from the warning/tint-warning pair already present as CSS variables. search reuses the muted surface token for the header search affordance. vehicle-selector is a category-specific component for the "Shop Your Vehicle" make/model picker central to this fitment-driven catalog; its interaction pattern (dropdown vs. multi-step) is proposed only.

## Responsive Behavior
Recommended, not measured: mobile <640px (single-column cards, hamburger nav, vehicle-selector collapses to a full-width stacked control), tablet 640–1024px (2-column product grids, condensed mega-menu), desktop >1024px (full mega-menu with make/model columns, multi-column hero and footer). Touch targets should be a minimum of 44px in both dimensions, spacing driven by `{spacing.md}`–`{spacing.lg}`. Navigation collapse and menu behavior are inferred conventions for e-commerce sites of this structure, not confirmed from captured markup.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS variables and a text excerpt only; no rendered layout, computed styles, or interaction states (hover, focus, open menu, cart drawer) were observed. Font files for 'PlatformFont' and 'PlatformBrandFont' are vendor-neutral placeholder names from the CSS build; actual typeface identity, availability, and licensing are unverified. Several palette entries (e.g., #4a4af4, #7f0180, #69cadd, #ba2d0d) appear in the supplied swatches but have no confirmed selector/role, so they were omitted from the semantic token set rather than guessed. The rounded-corner scale is proposed, since the only direct evidence is a `border-radius:0` reset on native form controls. All spacing values beyond the root `.25rem` unit, and all component-level padding/border assignments, are inferred design conventions for an automotive-accessories storefront, not measured from a live page.
