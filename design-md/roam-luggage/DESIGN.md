---
version: alpha
name: "Roam Luggage"
source_url: "https://roamluggage.com"
captured_at: "2026-09-28T10:07:12.939897+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  ROAM's public site presents a monochrome-forward premium aesthetic: near-black and white anchor the layout, with warm off-white surfaces (#f7f5f4, #fcfcf9) providing soft section backgrounds against a pure white canvas. A restrained red family (#df0a0a, #d21404, #b71616, #bc2e2e) appears on promotional and sale badges ("20% Off," "Save $200/$300"), which this spec treats as an accent rather than the core brand color, since the reviews-widget CSS shows default interactive buttons defaulting to black-on-white. Deep navy tones (#152368, #10233e, #172341) and a warm tan (#9b6740, #cd9f76) recur across what are likely color-swatch imagery for the brand's signature "customizable colorways" feature, so they are mapped as accent tokens rather than UI chrome. Typography is inferred from two systems: 'Area' is confirmed as the site-wide body/heading font via a broad selector rule, while 'Bebas Neue' is proposed for display headlines based on its condensed, all-caps character fitting the site's uppercase navigation and campaign copy; 'Figtree' and 'Work Sans' are treated as secondary/utility fonts of uncertain application. Numeric heading and body scales come directly from observed CSS custom properties. All component states beyond default (hover, focus, disabled, mobile) are proposed, not observed.

colors:
  primary: "#1c1c1e"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#3d3d3d"
  muted: "#8291a0"
  hairline: "#e8e8e8"
  surface-soft: "#f7f5f4"
  surface-card: "#fcfcf9"
  on-primary: "#ffffff"
  accent-red: "#df0a0a"
  accent-navy: "#152368"
  accent-tan: "#9b6740"
typography:
  display-xl: {fontFamily: "Bebas Neue, sans-serif", fontSize: 46px, fontWeight: 400, lineHeight: 1.1, letterSpacing: 0.3px}
  display-md: {fontFamily: "Bebas Neue, sans-serif", fontSize: 36px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0.25px}
  title-md: {fontFamily: "Area, sans-serif", fontSize: 27px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Area, sans-serif", fontSize: 17px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Area, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Figtree, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Area, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.ink}"
    badgeSlot: "top-left, uses badge component"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaButton: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderTop: "1px solid {colors.hairline}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "transparent"
    textColor: "{colors.accent-red}"
    typography: "{typography.caption}"
    border: "1px solid {colors.accent-red}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  colorway-swatch:
    size: "32px"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    selectedRing: "2px solid {colors.primary}"
    gap: "{spacing.xs}"

## Components

**button-primary** is the near-black, white-text call-to-action used for "SHOP NOW" / "CUSTOMIZE YOURS" style actions; its color is inferred from the site's monochrome tone and a confirmed default-black button rule in the reviews widget CSS, not from a captured on-page button screenshot.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Discover" links), sharing the ink border and text color with no fill, for use on light surfaces.

**text-input** covers form fields such as search or newsletter capture; border and placeholder colors are drawn from the observed hairline and muted-gray tokens, with states (focus, error) proposed and unobserved.

**nav-bar** models the sticky/top navigation implied by the "LUGGAGE / BAGS / ACCESSORIES / CUSTOMIZE / ABOUT" menu structure in the page text; exact height, sticky behavior, and dropdown styling are not measured and are proposed.

**product-card** represents bestseller tiles (e.g., "The Carry-On $595") with a soft card background, title and price typography drawn from the heading/body scale, and a badge slot for sale or best-seller callouts.

**hero** models the top promotional banner ("Pack for the Season Ahead") using the soft off-white surface and the largest display typography token; copy layout and image placement are proposed, not observed.

**footer** is a light, hairline-bordered proposed pattern; the actual footer background (light vs. dark) was not present in the supplied evidence and should be treated as a placeholder.

**badge** reuses the accent-red token for promotional and discount labels ("Save $200," "20% Off"), consistent with the product-badge selectors in the evidence, though exact badge shapes/fills beyond color were not captured.

**search** is a proposed lightweight input pattern for product/site search, styled consistently with text-input but on the soft surface background.

**colorway-swatch** is a category-appropriate component representing ROAM's core "build-your-own" color picker (referenced in "Customizable Colorways," "Curated Colorways," monogramming copy); the circular swatch with a primary-colored selection ring is proposed to support this signature interaction, not observed directly.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | < 768px | Single-column product grid; nav collapses to hamburger/off-canvas menu; hero stacks headline above CTA. |
| Tablet | 768–1024px | Two-column product grid; nav may remain horizontal with condensed spacing. |
| Desktop | > 1024px | Three–four column product grid; full horizontal nav with dropdown mega-menus implied by "SHOP BY SIZE / SHOP BY COLLECTION" groupings. |

Touch targets should be at least 44×44px for buttons, swatches, and nav items. Colorway swatches should wrap onto multiple rows on narrow viewports. All of the above is a suggested pattern only; no live responsive layout was observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS variables, color values, and page text only — no rendered screenshots, computed layout, or DOM structure were available. Several role assignments are inferred rather than confirmed: the primary/black CTA color is extrapolated from an Okendo reviews-widget default rather than a captured site button; the distinction between "accent-red" (sale) and other red hexes (#d21404, #bc2e2e, #b71616) is a best guess, as the source data does not label which red belongs to which UI element; and navy/tan tones assumed to represent colorway imagery could instead belong to unrelated illustration or photography. Font weights, letter-spacing, and line-heights are proposed defaults since no computed font-weight or spacing values were present in the evidence. Breakpoints, hover/focus/active states, and mobile navigation behavior are entirely proposed and not observed. Licensing and actual availability of 'Area', 'Figtree', 'Work Sans', and 'Bebas Neue' for reuse were not verified; 'Area' in particular may be a licensed/proprietary typeface and should not be assumed freely distributable.
