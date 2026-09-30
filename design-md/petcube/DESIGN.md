---
version: alpha
name: "Petcube"
source_url: "https://petcube.com"
captured_at: "2026-09-28T04:47:22.622933+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Petcube's storefront presents smart pet-camera and GPS-tracker products against a
  bright, neutral base. The evidence shows a near-black text ink (#171716) on
  white/off-white canvases (#ffffff, #f8f8f9, #f1f1f1), with warm amber/gold
  (#f9b72f, #f4a614, #ffc55a) used for primary buttons, checked states, and hover
  fills — this is treated as the observed brand accent. Secondary alert-style
  colors appear in the palette (#da4848, #ff574a, #46c786, #5bce3e) and are
  inferred here as status/badge colors (error, success) since no selector
  confirms their semantic use. Typography is set in Montserrat with sans-serif
  fallback; a Comic Sans reference also appears in the font list but is not
  tied to any confirmed selector, so it is excluded from primary type roles and
  noted only as a gap. Buttons use bold, uppercase, letter-spaced labels with
  6px rounded corners and a 2px border matching the fill color, per the
  `.button,button` rule. A 70px header height is confirmed via a CSS custom
  property. Card, hero, and grid layouts are proposed interpretations suited to
  a device e-commerce site, not measured DOM structure. Overall the design
  interpretation favors a clean, high-contrast retail aesthetic with a single
  warm accent color driving calls to action.

colors:
  primary: "#f9b72f"
  primary-hover: "#ffc55a"
  ink: "#171716"
  canvas: "#ffffff"
  body: "#29292b"
  muted: "#6e6e6f"
  hairline: "#e0e0e2"
  surface-soft: "#f8f8f9"
  surface-card: "#f1f1f1"
  on-primary: "#ffffff"
  accent-secondary: "#f4a614"
  success: "#46c786"
  error: "#da4848"
  badge-cream: "#fff4de"
  border-strong: "#d0d0d0"
typography:
  display-xl: {fontFamily: "Montserrat, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "Montserrat, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 800, lineHeight: 20px, letterSpacing: 0.08075em}
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
    border: "2px solid {colors.primary}"
    hover:
      backgroundColor: "{colors.primary-hover}"
      borderColor: "{colors.primary-hover}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "2px solid {colors.hairline}"
    hover:
      borderColor: "{colors.border-strong}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
    focus:
      borderColor: "{colors.primary}"
  nav-bar:
    height: "70px"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    salePriceColor: "{colors.error}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.badge-cream}"
    textColor: "{colors.accent-secondary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.md}"
  countdown-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.base}"

## Components
**button-primary** renders the site's amber CTA fill directly from the `.button,button` rule, with the observed hover swap to `#ffc55a`; bold uppercase letter-spaced label and 6px radius are directly evidenced.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Learn more" links), using the hairline border color; no direct selector confirms this variant.

**text-input** is inferred from generic form conventions since only `.selectize` dropdown styling was supplied; padding, focus ring, and border are proposed.

**nav-bar** uses the confirmed `--header-height:70px` custom property; background, border, and link styling are proposed based on the light canvas palette.

**product-card** is a proposed pattern for the device grid (Cam, Play 2, GPS Tracker, etc.) referenced in the page text; card surface and border colors reuse observed neutrals, and the sale-price treatment uses the red palette entry as an inferred discount color.

**hero** models the homepage banner ("Too Much Love? No Such Thing.") using the soft surface tone and display typography; exact hero layout/imagery is not observed.

**footer** is proposed as a dark-ink block reversing text to white for contrast; no footer-specific CSS was supplied.

**badge** covers promotional labels like "Save up to $67," using a warm cream background with the amber-gold text color; both are present in the palette but the pairing is inferred.

**search** and **countdown-banner** are proposed utility components; the countdown banner draws directly from the visible "Promo ends in..." timer text, styled with the dark ink background and amber numerals for visibility.

## Responsive Behavior
Recommendation only — no measured breakpoints were supplied.

| Breakpoint | Width | Behavior (proposed) |
|---|---|---|
| mobile | <640px | Single-column product grid, collapsed hamburger nav, stacked hero text/CTA |
| tablet | 640–1024px | 2-column product grid, nav-bar links may condense into icons |
| desktop | >1024px | 3–4 column product grid, full horizontal nav, sticky header at 70px |

Touch targets should be at least 44px tall (buttons already meet this via 14px padding + line-height). Nav collapses to a drawer/menu icon below tablet width; countdown banner should remain single-line and truncate gracefully on narrow viewports.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no live rendering, computed layout, or interaction testing was performed. Color-to-role assignments (e.g., success/error/badge colors) are inferred from typical e-commerce conventions and hue association, not from confirmed class usage. Font sizes for display/title/body/caption tiers beyond the confirmed 16px base and 14px button size are proposed, not measured. The "Comic Sans"/"Comic Sans MS" entries in the font list are not tied to any supplied selector and are excluded from typography roles pending further evidence. Mobile menu behavior, carousel/owl-nav visual states, and hover/focus states beyond the documented button hover are not observed. Licensing and self-hosted availability of Montserrat were not verified in the supplied evidence.
