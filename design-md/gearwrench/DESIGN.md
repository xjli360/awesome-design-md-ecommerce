---
version: alpha
name: "GearWrench"
source_url: "https://gearwrench.com"
captured_at: "2026-09-28T09:05:06.370370+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  GearWrench presents as a utilitarian, trade-focused hand tool brand under Apex Tool Group, and the evidence
  supports a high-contrast, industrial visual system. The observed palette centers on black (#000000) and
  white (#ffffff), with a saturated safety-orange accent (#eb8900) used for product-image borders and the
  primary buy-now button background — inferred here as the brand's primary call-to-action color. A near-black
  ink (#1d201f) appears on SKU/title text, and a muted slate-green (#949e9b) marks disabled button states,
  inferred as a general muted/disabled role. A soft gray-green (#e9eceb) backs a "featured product" full-bleed
  section, inferred as a surface-soft tone for content bands. Card borders use a mid-gray (#b4bbb9), inferred
  as the hairline token. Typography is confirmed as Akrobat (bold/800 display weight, condensed industrial feel)
  for product titles and buttons, paired with Arial/sans-serif fallbacks; Aktiv Grotesk is also present in
  source but its exact application is not confirmed from the supplied rules, so it is treated as a secondary
  observed family for body text. The design direction favors bold uppercase labels, hard-edged rectangular
  cards (no observed corner-radius values), and orange-on-black hover inversions, reflecting a rugged,
  no-nonsense professional-tools aesthetic rather than a soft consumer-retail look.

colors:
  primary: "#eb8900"
  ink: "#1d201f"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#949e9b"
  hairline: "#b4bbb9"
  surface-soft: "#e9eceb"
  surface-card: "#ffffff"
  on-primary: "#000000"
  accent-dark-orange: "#e09600"
  accent-deep: "#a51b00"
  accent-red: "#e62600"
  border-neutral: "#d4d8d7"
  gray-mid: "#333333"
typography:
  display-xl: {fontFamily: "Akrobat, Arial, sans-serif", fontSize: "48px", fontWeight: 800, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Akrobat, Arial, sans-serif", fontSize: "32px", fontWeight: 800, lineHeight: 1.2, letterSpacing: "0px"}
  title-md: {fontFamily: "Akrobat, Arial, sans-serif", fontSize: "24px", fontWeight: 800, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "Aktiv Grotesk, Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Aktiv Grotesk, Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Aktiv Grotesk, Arial, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Akrobat, Arial, sans-serif", fontSize: "16px", fontWeight: 700, lineHeight: 1, letterSpacing: "0.03rem"}
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
    padding: "{spacing.base} {spacing.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.base} {spacing.md}"
    border: "1px solid {colors.hairline}"
  button-disabled:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.base} {spacing.md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    imageBorder: "2px solid {colors.primary}"
    titleTypography: "{typography.title-md}"
    skuTypography: "{typography.caption}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.body}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    linkColor: "{colors.primary}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.title-md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the observed orange (#eb8900) background with black text, matching the confirmed
`.node__buy-now-button` rule; hover state (inferred as standard, but CSS-confirmed) inverts to black
background with orange text. **button-secondary** is proposed as a white/outline variant for lower-emphasis
actions like "Where to Buy," using the hairline gray border observed on product cards. **button-disabled**
directly reflects the confirmed `.ps-disabled` muted slate-green background rule. **text-input** and
**search** are proposed patterns for the header search bar referenced in nav text ("Open Header Search Bar")
— visual treatment (border, radius) is inferred from the card hairline color since no input-specific CSS was
supplied. **nav-bar** is proposed based on the presence of "Main navigation," "Tools," and "Country Toggle"
menu items in page text; exact colors/heights are not confirmed. **product-card** is directly grounded in the
`.node--type-product` card rules: white background, gray hairline border, orange image border, and Akrobat
bold titles. **hero** is proposed using the confirmed `.component-featured-product` full-bleed soft-gray
section background for large promotional banners like "Meet the New GEARWRENCH Power & Utility Tools."
**footer** is proposed as black-background/white-text given the dark Apex Tool Group corporate footer content
observed in page text, with orange links for visual consistency with the primary CTA color. **badge** is a
proposed small-label pattern (e.g., "NEW") using primary orange, not directly observed but consistent with
the accent usage. **category-tile** is proposed for the "Shop Tools by Industry" and category-grid sections
referenced in page text, styled with the surface-soft background observed elsewhere on the page.

## Responsive Behavior

Recommended (not measured) breakpoints:

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| Mobile | <600px | Single-column product cards; nav collapses to hamburger ("Open Menu / Close Menu" text confirms a toggle pattern exists) |
| Tablet | 600–1024px | 2-column product grid; search bar toggle remains icon-triggered |
| Desktop | 1024–1440px | 3–4 column product grid; full horizontal nav with mega-menu-style "Tools" dropdown |
| Wide | >1440px | Max-width content container; hero/featured sections remain full-bleed per `.component-featured-product` 100vw rule |

Touch targets should be a minimum 44×44px for buy-now buttons and nav toggles. Menu collapse behavior
(hamburger, expand/collapse for "Tools" and "Country Toggle") is confirmed present in text labels only —
actual collapse thresholds and animation are not observed and are proposed conventions.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is derived solely from static CSS excerpts and page text; no rendered layout, responsive
behavior, or interaction states (hover/focus/active beyond the two confirmed button rules) were directly
observed. Font sizes, spacing scale, and rounded-corner values are proposed conventions, not measured from
the site, since no explicit `font-size`, `padding`, or `border-radius` scale was supplied beyond the specific
rules shown. The role of "Aktiv Grotesk" as body text is inferred from its presence in the font-family list;
its actual application to body copy is unconfirmed. Several palette colors (e.g., #c9e1bd, #f4daa6, #f9c9bf,
#007aff, #ffff00) appear in the supplied palette but have no associated selector evidence, so they are
omitted from role assignment pending further evidence. Custom font licensing/availability (Akrobat, Aktiv
Grotesk as web fonts) was not verified. Mobile menu, search overlay, and country-selector interaction
patterns are described only from ARIA-style label text ("Open/Close Menu," "Open/Close Header Search Bar")
and not from actual behavior.
