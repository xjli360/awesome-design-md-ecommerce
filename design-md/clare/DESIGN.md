---
version: alpha
name: "Clare"
source_url: "https://clare.com"
captured_at: "2026-09-28T04:20:58.011139+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Clare's observed stylesheet centers on a warm marigold accent (#f5be18) paired
  with a deep navy (#003149) used as both button text and footer/announcement
  surfaces, set against a clean white canvas (#ffffff) and near-black body copy
  (#1b1d1e). A soft teal secondary (#8ac7cb, dimming to #3a7e82) appears on
  carousel controls, giving the interface a friendly, paint-swatch character
  rather than a strictly corporate one. Neutral grays (#cccccc, #4e5457,
  #f2f2f2) support borders, secondary text, and dimmed surfaces.

  Typography is CSS-variable driven: a serif/humanist display face named
  "Reader" (falling back to Montserrat) carries large headline moments at a
  72px base size, while body copy uses "Freight" with generic sans-serif
  fallback per the theme's font stack. Button radius is fully pill-shaped
  (50px), reinforcing a soft, rounded, approachable aesthetic consistent with
  a DTC paint brand.

  This interpretation infers card, nav, and footer treatments from the
  documented CSS custom properties (--colorFooter, --colorNav, --colorBody,
  etc.) rather than from direct visual layout observation. Spacing scale,
  breakpoints, and hover/focus states beyond the flickity button examples are
  proposed conventions, not confirmed site behavior.

colors:
  primary: "#f5be18"
  primary-light: "#f7cc49"
  primary-dim: "#e9b20a"
  on-primary: "#003149"
  secondary: "#8ac7cb"
  secondary-dim: "#3a7e82"
  ink: "#1b1d1e"
  body: "#1b1d1e"
  muted: "#4e5457"
  savings: "#c20000"
  hairline: "#cccccc"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#f5f9fa"
  footer: "#003149"
  footer-text: "#ffffff"
  announcement: "#003149"
  announcement-text: "#ffffff"
typography:
  display-xl: {fontFamily: "'Reader', Montserrat, sans-serif", fontSize: "72px", fontWeight: 500, lineHeight: 1.2, letterSpacing: "0em"}
  display-md: {fontFamily: "'Reader', Montserrat, sans-serif", fontSize: "40px", fontWeight: 500, lineHeight: 1.2, letterSpacing: "0em"}
  title-md: {fontFamily: "'Reader', Montserrat, sans-serif", fontSize: "24px", fontWeight: 500, lineHeight: 1.3, letterSpacing: "0em"}
  body-md: {fontFamily: "'Freight', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0em"}
  body-sm: {fontFamily: "'Freight', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0em"}
  caption: {fontFamily: "'Freight', sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: 1.6, letterSpacing: "1.75px"}
  button-md: {fontFamily: "'Reader', Montserrat, sans-serif", fontSize: "14px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.2px"}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    hover:
      backgroundColor: "{colors.secondary-dim}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    priceColor: "{colors.muted}"
    savingsColor: "{colors.savings}"
    titleTypography: "{typography.title-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    controlBackground: "{colors.canvas}"
    controlColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.footer}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  announcement-bar:
    backgroundColor: "{colors.announcement}"
    textColor: "{colors.announcement-text}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
  badge:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  swatch-picker:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    selectedBorderColor: "{colors.primary}"
    padding: "{spacing.xxs}"

## Components
**button-primary** uses the observed `--colorBtnPrimary`/`--colorBtnPrimaryText` pair with the documented 50px pill radius, matching the `.ocu-popup button.ocu-cta__buy` rule. **button-secondary** reuses the teal token set (`--colorBtnSecondary` → `--colorBtnSecondaryDim` on hover), directly evidenced by `.flickity-button:hover`. **text-input** is a proposed pattern; no input styling was captured in evidence, so border and padding values are inferred from the general border/spacing tokens. **nav-bar** derives its white background and dark text from `--colorNav`/`--colorNavText`; sticky behavior and mobile menu state are not observed. **product-card** infers a bordered white card from `--colorBorder` and `--colorPrice`, with savings text mapped to `--colorTextSavings`; card shadow/elevation is proposed, not measured. **hero** is inferred from `.hero .flickity-button` styling (white circular controls with soft shadow) combined with the large 72px display type variable; overall hero composition (image position, copy alignment) is not observed. **footer** and **announcement-bar** both draw from `--colorFooter`/`--colorAnnouncement`, sharing the same navy token, which is an inferred but CSS-supported pairing. **badge** is a proposed sale/label treatment built from the `--colorSaleTag`/`--colorSaleTagText` pair. **swatch-picker** is a proposed, category-appropriate component for a paint retailer, styled with the pill radius and primary accent as a selected-state ring; no swatch markup was present in the supplied evidence.

## Responsive Behavior
The following breakpoint table is a recommendation only; no responsive CSS or viewport behavior was present in the supplied evidence.

| Breakpoint | Width       | Notes (proposed)                          |
|------------|-------------|--------------------------------------------|
| mobile     | 0–599px     | Single-column stack, nav collapses to menu |
| tablet     | 600–959px   | 2-column product grid                      |
| desktop    | 960–1279px  | 3-column grid, full nav                    |
| wide       | 1280px+     | 4-column grid, max-width container         |

Touch targets should be at least 44px in the proposed scale (roughly `{spacing.xl}`), and primary/secondary buttons should retain the pill radius across breakpoints. Mobile nav collapse, drawer patterns, and swatch-picker touch interactions are proposed conventions, not confirmed from the site.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from static CSS/JSON evidence only; no live page render, DOM interaction, or JavaScript-driven state was observed. The "Reader" and "Freight" font families are referenced by name in CSS custom properties but their actual availability, licensing, and full weight range are not verified — generic sans-serif fallbacks are used per constraint. The mapping of colors to semantic roles (e.g., surface-soft, surface-card) is inferred from variable naming conventions (`--colorBodyDim`, sale-tag colors) rather than confirmed visual usage. All spacing, rounded corner scale (aside from the observed 50px button radius), and breakpoint values are proposed design conventions. Component states such as hover/focus/disabled are only confirmed for `.flickity-button` and `.ocu-cta__buy`; all other interactive states are proposed. Mobile layout, menu behavior, and card grid structure were not present in the supplied evidence and are therefore inferred from common e-commerce patterns.
