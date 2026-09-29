---
version: alpha
name: "ChargePoint"
source_url: "https://chargepoint.com"
captured_at: "2026-09-28T04:30:54.348117+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  ChargePoint's evidenced CSS shows a utilitarian, product-navigation-heavy site built on a
  white canvas (#FFFFFF) with a dominant dark-blue accent (#0F588A) used for active states,
  hover links, underline indicators, and selected product-nav tabs. A secondary blue
  (#0076A8 / #2A84B8) and a warm orange (#FF7A14) appear in the broader palette, suggesting
  orange is reserved for high-emphasis calls to action while blue governs navigation and
  selection states (inferred, not confirmed by supplied rules). Body copy uses a near-black
  (#000000 / var(--black)) on white, with grays (#777777, #555555, #999999, #CBD6DF,
  #EEEEEE) forming hairlines, muted text, and card/section dividers observed in
  `.cp-ProductNav_Wrapper` and `.cp-nav-products` rules. Typography is set in the licensed
  Gotham Narrow SSm stack (A/B fallback cuts) at a 16px/1.43 base, with sans-serif fallback;
  no display-weight or heading sizes were present in the evidence, so heading scale, letter
  spacing, and button/card treatments below are proposed and clearly labeled. Alert-style
  colors (#3C763D, #A94442, #8A6D3B, #DFF0D8, #F2DEDE, #FCF8E3) are retained as inferred
  status/utility tokens rather than brand colors. Rounded corners and spacing scale are
  proposed conventions layered onto the observed flat, low-radius navigation aesthetic.

colors:
  primary: "#0f588a"
  accent: "#ff7a14"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#eeeeee"
  hairline-strong: "#cbd6df"
  surface-soft: "#f6f8f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border-default: "#dddddd"
  link-secondary: "#0076a8"
  info-bg: "#e7f6fd"
  info-border: "#95d4e9"
  success-bg: "#dff0d8"
  success-text: "#3c763d"
  warning-bg: "#fcf8e3"
  warning-text: "#8a6d3b"
  danger-bg: "#f2dede"
  danger-text: "#a94442"
  charcoal: "#495e6b"
typography:
  display-xl: {fontFamily: "'Gotham Narrow SSm A', 'Gotham Narrow SSm B', sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Gotham Narrow SSm A', 'Gotham Narrow SSm B', sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "'Gotham Narrow SSm A', 'Gotham Narrow SSm B', sans-serif", fontSize: "22px", fontWeight: 500, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "'Gotham Narrow SSm A', 'Gotham Narrow SSm B', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.42857143, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Gotham Narrow SSm A', 'Gotham Narrow SSm B', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0px"}
  caption: {fontFamily: "'Gotham Narrow SSm A', 'Gotham Narrow SSm B', sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "'Gotham Narrow SSm A', 'Gotham Narrow SSm B', sans-serif", fontSize: "16px", fontWeight: 500, lineHeight: 1.2, letterSpacing: "0.2px"}
rounded:
  none: "0px"
  xs: "2px"
  sm: "4px"
  md: "8px"
  lg: "16px"
  full: "9999px"
spacing:
  none: "0px"
  xxs: "2px"
  xs: "4px"
  sm: "8px"
  md: "12px"
  base: "16px"
  lg: "24px"
  xl: "32px"
  xxl: "48px"
  section: "64px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.border-default}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    activeIndicatorColor: "{colors.primary}"
    typography: "{typography.body-md}"
    padding: "{spacing.none} {spacing.lg}"
  product-nav-dropdown:
    backgroundColor: "{colors.canvas}"
    itemDividerColor: "{colors.hairline-strong}"
    activeTabBorderLeft: "3px solid {colors.primary}"
    activeTabTextColor: "{colors.primary}"
    gridGap: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline-strong}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.hairline-strong}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.info-bg}"
    border: "1px solid {colors.info-border}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.border-default}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  station-status-tag:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-text}"
    rounded: "{rounded.xs}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components
**button-primary** is the dark-blue (#0F588A) filled action used for primary conversions such as "Get a Quote"; its hover/focus states are proposed, not observed in the supplied rules. **button-secondary** is an outlined variant sharing the same blue for text and border on a white fill, suited to lower-emphasis actions alongside a primary button. **button-accent** applies the observed orange (#FF7A14) sparingly for the single highest-priority CTA per view, inferred from the palette's limited warm-color usage. **text-input** is a proposed flat, thin-bordered field using the neutral #DDDDDD border and base body typography, since no form-field CSS was supplied. **nav-bar** reflects the evidenced `.cp-ProductNav_Wrapper` pattern: white background, thin #EEEEEE bottom hairline, and blue active/hover text. **product-nav-dropdown** mirrors the `.cp-nav-products` mega-menu rules directly observed—three-column grid, blue left-border active tab, and #CBD6DF section dividers. **product-card** is a proposed container for accessory/product listings, using a card border and radius not present in evidence but consistent with the site's boxed, gridded navigation style. **hero** is a proposed top-of-page banner on the light #F6F8F9 surface tone seen in the palette, pairing a large display headline with supporting body text. **footer** is inferred to use the darker charcoal-blue (#495E6B) for contrast, since no footer rules were supplied. **badge** and **station-status-tag** are proposed utility components drawing on the observed info (#E7F6FD/#95D4E9) and success (#DFF0D8/#3C763D) alert colors, useful for charger-availability or promotional labeling.

## Responsive Behavior
Recommended breakpoints (not measured): mobile ≤480px, tablet 481–1024px, desktop 1025–1400px, wide ≥1401px (matching the observed 1400px max content width in `.cp-ProductNav_Wrapper`). Touch targets should be at least 44px tall for buttons and nav items. Below tablet width, the product mega-menu should collapse into a stacked accordion rather than the three-column grid, and the utility/nav-bar row should condense into a hamburger-triggered panel. These behaviors are proposed conventions, not confirmed interactions.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is derived solely from static CSS declarations and a color/font extraction; no rendered page, responsive breakpoint, or interaction state (hover, focus, open menu) was directly observed beyond the literal selectors supplied. Semantic role assignments—such as treating #FF7A14 as an accent CTA color or #495E6B as a footer background—are inferred from typical usage patterns, not confirmed by layout screenshots. All typography sizes, weights, and letter-spacing outside the observed 16px/1.4286 body rule are proposed placeholders. Component definitions for text-input, hero, footer, product-card, badge, and station-status-tag are proposed patterns with no corresponding CSS evidence. Gotham Narrow SSm's licensing and availability were not verified; fallback to generic sans-serif is assumed for any environment lacking the licensed font.
