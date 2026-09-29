---
version: alpha
name: "Connor McGinn Studios"
source_url: "https://connormcginnstudios.com"
captured_at: "2026-09-28T09:31:43.375074+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Connor McGinn Studios sells handmade ceramic tableware for restaurants and homes,
  produced in Tarrytown, New York. The supplied CSS evidence shows a Shopify-based
  storefront with squared-off product cards and buttons (corner-radius tokens set
  to 0px) and an uppercase title-case convention, suggesting a restrained, workshop-
  like presentation rather than a decorative one. The observed palette is dominated
  by warm near-blacks (#1a1714, #2a2520), off-white and paper-toned neutrals
  (#f9f9f9, #e9e7e4, #f5f5f5), and mid-grays for secondary text (#666666, #8a8a8a).
  A muted slate-teal (#3d4b4b) appears repeatedly as the review-widget's primary
  and CTA color and is adopted here, inferred, as the closest available brand
  accent. A small red/coral pair (#e94560 and its low-alpha tints) recurs near sale
  pricing and is mapped, inferred, to a sale/badge role rather than a primary
  action color. Font evidence includes Neue Haas Grotesk Display Pro (sans, UI and
  body), Nicholas/NicholasPro (a serif/italic family, inferred as a display face for
  hero and section headings), and IBM Plex Mono (inferred for price and label
  accents). Generic fallbacks (Georgia, Helvetica, Arial, monospace) are retained
  per family. No live layout, hover, or mobile behavior was observed; all
  interaction states below are proposed conventions consistent with the token
  evidence, not measurements.

colors:
  primary: "#3d4b4b"
  ink: "#1a1714"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#e6e6e6"
  surface-soft: "#f9f9f9"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  surface-warm: "#e9e7e4"
  border-strong: "#2a2520"
  muted-2: "#8a8a8a"
  accent-sale: "#e94560"
  accent-sale-tint: "#e945600a"
  success: "#006400"
  danger: "#8b0000"
typography:
  display-xl: {fontFamily: "'Nicholas', Georgia, serif", fontSize: "56px", fontWeight: 400, lineHeight: 1.05, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Nicholas', Georgia, serif", fontSize: "36px", fontWeight: 400, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "'Neue Haas Grotesk Display Pro', 'Helvetica Neue', Arial, sans-serif", fontSize: "20px", fontWeight: 500, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "'Neue Haas Grotesk Display Pro', 'Helvetica Neue', Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Neue Haas Grotesk Display Pro', 'Helvetica Neue', Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'IBM Plex Mono', 'SFMono-Regular', monospace, ui-monospace", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.5px"}
  button-md: {fontFamily: "'Neue Haas Grotesk Display Pro', 'Helvetica Neue', Arial, sans-serif", fontSize: "14px", fontWeight: 500, lineHeight: 1.0, letterSpacing: "0.5px"}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    gap: "{spacing.sm}"
    priceTypography: "{typography.caption}"
    titleTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.muted-2}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-sale-tint}"
    textColor: "{colors.accent-sale}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  glaze-swatch:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
    size: "{spacing.xl}"
    labelTypography: "{typography.caption}"

## Components

**button-primary** carries the slate-teal accent (#3d4b4b) already used for the review widget's write-review button, applied here to the sitewide add-to-cart and checkout actions; square corners (rounded.none) match the observed `--card-corner-radius: 0` / `--jdgm-border-radius: 0` convention. **button-secondary** is a low-contrast outline variant for tertiary actions (e.g., "More" product links) on light surfaces. **text-input** is proposed for account, newsletter, and registry forms; no live focus or validation styling was observed, so states are inferred. **nav-bar** reflects a light, hairline-bordered header consistent with a white canvas and dark ink text, holding the Shop/Studio/Hospitality menu structure named in the evidence; sticky/mobile-drawer behavior is not confirmed and is proposed. **product-card** uses the warm off-white surface for grid tiles shown in "Signature collection" (mugs, bowls, pourers), pairing a small caption-weight mono price with a sans title, per the mono/sans family split in the font evidence. **hero** targets the homepage's "Handmade Ceramics / Tarrytown, New York" banner, using the inferred display serif (Nicholas) for the headline over a warm neutral background rather than pure white, to differentiate from grid sections. **footer** inverts to the darkest observed ink (#1a1714) with muted-gray links, matching the long footer link list (Support, Studio, Terms) in the page text. **badge** is proposed for sale/2nds-and-overstock labeling, using the low-alpha coral tint variables (`#e945600a`, `#e9456014`) found in the CSS as evidence of an existing sale-highlight treatment. **search** follows the same square, hairline-bordered input pattern as text-input. **glaze-swatch** is a category-specific proposed component for selecting ceramic glaze/colorways (e.g., Meringue, Agave, Butter, Dusk platters named in the evidence), rendered as small circular swatches with a primary-colored active ring.

## Responsive Behavior

Recommendation only; no live breakpoints, resize, or mobile interaction were observed in the supplied evidence.

| Breakpoint | Width | Layout guidance |
|---|---|---|
| Mobile | up to 599px | Single-column product grid, collapsed nav into a hamburger drawer, stacked hero text over image, full-width buttons (min 44px touch target). |
| Tablet | 600–1023px | 2–3 column product grid, inline top nav with condensed spacing, hero text/image side-by-side optional. |
| Desktop | 1024–1439px | Standard multi-column grid (evidence references up to `repeat(10,...)` zoom-out grid variants), full horizontal nav, hospitality project grid in 3 columns. |
| Wide | 1440px+ | Increased gutters/margins only; content max-width capped, no new column behavior assumed. |

All interactive elements should target a minimum 44×44px touch area; nav and filter menus are assumed to collapse below tablet width as a standard e-commerce pattern, not as an observed behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/token evidence and page text only; no rendered page, computed layout, or DOM screenshot was inspected. Font-family-to-element mapping (e.g., which headings actually render in Nicholas vs. NeueHaasDisplay) is inferred from variable names and family lists, not confirmed computed styles. The "primary" brand color (#3d4b4b) is inferred from a third-party review widget's configuration variables and may not represent an intentional core brand color. All font sizes, line-heights, letter-spacing, and component paddings are proposed defaults consistent with token evidence, not measured values. Hover, focus, active, error, and mobile-menu states are proposed conventions and were not observed. Licensing and web-font availability for Nicholas/NicholasPro and Neue Haas Grotesk Display Pro were not verified and may require confirmation before production use. The glaze-swatch component's exact interaction model (radio buttons vs. swatches vs. dropdown) was not observed and is a category-informed proposal only.
