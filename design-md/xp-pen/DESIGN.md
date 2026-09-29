---
version: alpha
name: "XP-Pen"
source_url: "https://www.xp-pen.com"
captured_at: "2026-09-28T04:04:23.773698+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  The XP-Pen site draws from a large, utility-driven palette dominated by
  near-black text (#151414, #333333), neutral grays (#777777, #999999,
  #cccccc, #ebebeb) and white (#ffffff) surfaces, with a saturated
  red-orange (#fd4627) and secondary orange (#ff6c00) appearing as accent
  colors in navigation and promotional elements. A cooler blue (#44abe2)
  and the Bootstrap-derived state colors (#5cb85c, #d9534f, #f0ad4e,
  #5bc0de) are present in the evidence but their production usage
  (alerts, links, form validation) is inferred from Bootstrap component
  conventions rather than directly observed on the live page. Typography
  is system-first: Helvetica Neue/Arial/sans-serif for body copy, with
  Gilroy referenced for a specific labeled overlay element, suggesting a
  geometric display face reserved for marketing callouts. This
  interpretation treats #fd4627 as the primary brand accent (most
  visually assertive, non-neutral, non-utility color in the set) and
  #151414 as the primary ink, with #ebebeb standing in for hairline
  borders and soft dividers, since it is the only light-gray value
  explicitly tied to a border declaration in the evidence. All component
  states beyond what is shown (hover, focus, disabled) are proposed
  patterns, not confirmed observations.

colors:
  primary: "#fd4627"
  accent-orange: "#ff6c00"
  accent-blue: "#44abe2"
  ink: "#151414"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#ebebeb"
  surface-soft: "#f5f5f5"
  surface-card: "#f7f7f7"
  on-primary: "#ffffff"
  border-mid: "#cccccc"
  success: "#5cb85c"
  danger: "#d9534f"
  warning: "#f0ad4e"
  info: "#5bc0de"
typography:
  display-xl: {fontFamily: "Gilroy, Helvetica Neue, Arial, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Gilroy, Helvetica Neue, Arial, sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
  title-md: {fontFamily: "Helvetica Neue, Arial, sans-serif", fontSize: "20px", fontWeight: 500, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.42857143, letterSpacing: "0px"}
  body-sm: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "13px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0px"}
  caption: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.3, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Gilroy, Helvetica Neue, Arial, sans-serif", fontSize: "14px", fontWeight: 700, lineHeight: 1, letterSpacing: "0.3px"}
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.border-mid}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
    border: "1px solid {colors.border-mid}"
  carousel-control:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    padding: "{spacing.md}"

## Components

**button-primary** uses the red-orange accent (#fd4627) as a strong call-to-action color against white text, matching the site's most saturated non-neutral hue; hover/pressed states are proposed (darkened tint) and not directly observed.

**button-secondary** is an outlined variant on white with dark ink text, intended for lower-emphasis actions alongside primary CTAs; the border color reuses the mid-gray (#cccccc) observed in the general palette.

**text-input** proposes a hairline-bordered field on white, sized to the 14px body type observed sitewide; focus-ring styling is not present in the evidence and is a proposed accessibility affordance.

**nav-bar** reflects the header's white background and bordered dropdown panels (evidenced by `.application_list`'s `border-top:1px solid #EBEBEB`), extended here into a full navigation bar treatment with dark ink labels.

**product-card** is a category-appropriate component for a tablet/hardware catalog, using the light card surface (#f7f7f7) and a subtle hairline border to separate product tiles; imagery, price, and rating rows are proposed, not measured.

**hero** applies the near-black ink (#151414) as a full-bleed background with white display type, an inferred pattern for promotional/banner sections given the dark tone's presence in the palette but not confirmed as a hero background.

**footer** uses the soft gray surface (#f5f5f5) with muted gray text (#777777), a common utility pattern; column structure and link states are proposed.

**badge** and **search** are supporting components: badge borrows the secondary orange (#ff6c00) for small status/promo labels; search proposes a pill-shaped input consistent with the `border-radius` patterns seen in `.jumpIndiaBox .btn a` (25px pill buttons).

**carousel-control** reflects the swiper navigation affordance evidenced by `.golden-sentence .swiper-button-prev/next` (circular, `border-radius:50%`), reusing the hairline gray (#ebebeb) in place of the unlisted `#EAEAEA` value found only in that declaration.

## Responsive Behavior

Proposed breakpoint table (not measured from live responsive behavior):

| Breakpoint | Width      | Notes                                   |
|------------|------------|------------------------------------------|
| xs         | <576px     | Single-column, collapsed nav, stacked cards |
| sm         | 576–767px  | Two-column product grid                  |
| md         | 768–991px  | Nav shows partial mega-menu, 3-col grid  |
| lg         | 992–1199px | Full desktop nav, 4-col grid             |
| xl         | ≥1200px    | Max-width container, full mega-menu      |

Touch targets should be at least 44×44px for nav items and buttons; the mega-menu-style `.application_list` and `.commodity-list` panels are assumed to collapse into an accordion or drawer pattern on smaller viewports. This table is a design recommendation only, not an observation of XP-Pen's actual responsive CSS or JavaScript behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/DOM evidence only; no live rendering, computed styles, or interaction (hover, focus, active, JS-driven states) were observed. Semantic color roles (primary, muted, hairline, etc.) are inferred by matching hex values to their most plausible usage context, not confirmed brand guidelines. Typography sizes beyond the 14px body value from Bootstrap defaults are proposed, not measured. The Gilroy font's licensing/availability for production use is unverified. Mobile/responsive layout, breakpoints, and menu-collapse behavior are proposed patterns, not tested against the live site. The #EAEAEA value referenced in one carousel-control declaration was excluded from the palette (not present in the supplied observed color list) and substituted with the closest verified neutral, #ebebeb.
