---
version: alpha
name: "Strymon"
source_url: "https://www.strymon.net"
captured_at: "2026-09-28T09:14:26.637901+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Strymon's storefront runs on WooCommerce/WordPress, and its CSS custom
  properties expose a WooCommerce theme layer rather than a fully bespoke
  brand system: a saturated violet-purple (#720eec) is set as the WooCommerce
  primary/accent color and drives buttons and links, paired with a warm
  near-white content background (#fcfbfe) and a soft lavender-grey secondary
  surface (#e9e6ed). Body copy uses a muted charcoal (#515151) with a lighter
  grey subtext tone (#767676), and hairlines/tab borders use a pale
  purple-grey (#cfc8d8). A near-black WordPress default (#32373c) appears as
  a fallback button background, suggesting a dark, technical, no-nonsense
  utility layer beneath the purple accent. Status colors (green #007518, red
  #cc1818/#a00, amber #ffba00, blue #2ea2cc) are WooCommerce form/notice
  defaults, inferred as functional rather than brand-expressive. Font stacks
  list "DIN OT" and "museo-sans" as loaded families; DIN OT is proposed here
  for display/headline use given its geometric, technical character common to
  audio-gear branding, while museo-sans is proposed for body copy. All sizes,
  weights, and letter-spacing beyond what CSS states are proposed, not
  measured.

colors:
  primary: "#720eec"
  ink: "#2b2d2f"
  canvas: "#ffffff"
  body: "#515151"
  muted: "#767676"
  hairline: "#cfc8d8"
  surface-soft: "#e9e6ed"
  surface-card: "#fcfbfe"
  on-primary: "#ffffff"
  dark-surface: "#32373c"
  border-strong: "#cccccc"
  destructive: "#cc1818"
  success: "#007518"
  warning: "#ffba00"
  info: "#2ea2cc"
typography:
  display-xl: {fontFamily: "'DIN OT', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'DIN OT', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'DIN OT', sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "'museo-sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'museo-sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'museo-sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'DIN OT', sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.3px}
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
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.dark-surface}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-sm}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    rowAltBackground: "transparent"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components
**button-primary** uses the WooCommerce accent purple (#720eec) as its background with white text, mirroring the `--e-global-color-accent` variable applied to `.wp-block-button__link`; a 4px radius approximates the observed 5px button radius. **button-secondary** falls back to the dark near-black (#32373c) seen as the default `.wp-element-button` background, useful for secondary CTAs like "Compare" or "Find a Dealer" — states (hover/active) are proposed, not observed. **text-input** is proposed from generic form conventions, using the hairline lavender-grey border seen in `.woocommerce-tabs` styling; focus/error states are not observed. **nav-bar** is inferred from the site's flat product mega-menu text list (Reverb, Delay, Drive & Compression, etc.); no scroll/sticky behavior was observed. **product-card** uses the near-white `#fcfbfe` content background with an 8px radius matching the `--wc-card-border-radius` token, suited to displaying pedal thumbnails, names, and prices. **hero** is proposed for homepage banners (e.g. "TimeLine MX has arrived") using the dark surface for contrast against white product photography; copy hierarchy is speculative. **footer** reuses the dark surface tone for the observed multi-column link list (About, Jobs, Press, Dealer, Legal, Support). **badge** is proposed for "New," "In Stock," or category tags using the soft lavender surface and muted body text. **search** is proposed generically for the product catalog search field. **spec-table** is a category-appropriate addition for guitar-pedal technical specifications (I/O, power draw, dimensions), styled after the observed `.woocommerce-tabs` tab list bordering and soft background.

## Responsive Behavior
Recommended, not measured from the live site:

| Breakpoint | Width | Layout guidance |
|---|---|---|
| mobile | <600px | Single-column product grid, collapsed hamburger nav, stacked spec tables |
| tablet | 600–960px | 2-column product grid, condensed mega-menu |
| desktop | 960–1200px | 3–4 column product grid, full mega-menu, content max-width 1200px per observed `--wp--style--global--wide-size` |
| wide | >1200px | Content capped at wide-size token; hero/banner imagery may extend full-bleed |

Touch targets should be at least 44×44px; primary/secondary buttons should retain the `{spacing.md} {spacing.lg}` padding at all sizes. Mega-menu (Products with many sub-categories) should collapse to an accordion on mobile. All breakpoint values are proposed conventions, not extracted from responsive CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom-property extraction and a text snapshot only; no rendered layout, computed styles, hover/focus/active states, or JavaScript-driven interactions were observed. Many supplied hex values (e.g. `#fcb900`, `#f78da7`, `#00d084`) originate from the default WordPress block-editor palette rather than confirmed Strymon brand usage, and were excluded from the token set where redundant or clearly generic. The purple accent (#720eec) is a WooCommerce theme-config variable and is treated as the brand primary by inference, not by direct visual confirmation of logo or header color. Font sizes, weights, letter-spacing, and the specific role assignments for "DIN OT" vs. "museo-sans" are proposed, since no font-size/weight declarations were present in the supplied CSS rules. Availability and licensing of "DIN OT" and "museo-sans" as web fonts were not verified. Responsive breakpoints, mobile navigation behavior, and grid column counts are proposed conventions only. The `"WooCommerce"` and `"star"` font entries are icon fonts and were intentionally excluded from typography roles.
