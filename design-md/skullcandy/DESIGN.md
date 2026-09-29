---
version: alpha
name: "Skullcandy"
source_url: "https://skullcandy.com"
captured_at: "2026-09-29T03:53:30.965249+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Skullcandy's storefront pairs a stark black-and-white base with a single
  saturated action color, "#0081ff", used consistently for primary CTAs and
  their darker hover state "#006dd9". Headings use "Archivo Black" at a fixed
  400 weight with tight, slightly negative letter-spacing on hero type,
  reflecting the brand's bold, graphic tone; body and UI copy fall back to
  "Archivo" with generic sans-serif support. A small set of near-white grays
  ("#f4f4f4", "#f5f5f5", "#e5e5e5") appears repeatedly for surfaces and
  hairlines, suggesting a light, card-based product-grid layout rather than
  heavy chrome. A saturated yellow ("#f6d309") and red ("#f44336") are present
  in the palette and are interpreted here as sale/badge accents rather than
  primary brand colors, since no CSS role ties them to core UI. Rounded pill
  buttons (observed radius up to 30px) and 8px-radius CTA blocks suggest two
  button treatments: a pill-shaped cart/checkout action and a squarer inline
  rich-text button. Body font-size and weight are driven by CSS custom
  properties not resolved in the supplied evidence, so base body sizing below
  is proposed, not measured.

colors:
  primary: "#0081ff"
  primary-hover: "#006dd9"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666565f7"
  hairline: "#e5e5e5"
  surface-soft: "#f4f4f4"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  accent-yellow: "#f6d309"
  sale: "#f44336"
  dark-surface: "#121212"
typography:
  display-xl: {fontFamily: "Archivo Black, sans-serif", fontSize: 56px, fontWeight: 400, lineHeight: 1.05, letterSpacing: -1.7px}
  display-md: {fontFamily: "Archivo Black, sans-serif", fontSize: 36px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -1px}
  title-md: {fontFamily: "Archivo Black, sans-serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Archivo, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Archivo, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Archivo, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "Archivo, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    activeBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    size: "{spacing.lg}"

## Components

**button-primary** is the pill-shaped, high-contrast CTA seen on the cart-drawer checkout action and inline rich-text buttons, using the observed "#0081ff" fill with "#006dd9" as the (proposed) hover state, uppercase bold text, and a large radius drawn from the observed 30px checkout-button radius.

**button-secondary** is a proposed lower-emphasis action (e.g. "Continue shopping") using a white fill with dark ink text and a smaller 8px radius, matching the milder rounding seen on `.rich-text__buttons`.

**text-input** covers cart, search, and account form fields; background and border are inferred from the neutral gray/hairline palette since no explicit input styling was supplied.

**nav-bar** represents the mega-menu header (Headphones, Earbuds, Gaming, Speakers, Explore) on a white canvas with black text; submenu grouping and hover states are proposed, not observed in the CSS.

**product-card** models grid tiles like "Crusher® 1080 ANC" — light card surface, hairline border, bold title, and a smaller price line reflecting the sale/regular price pairs in the page text; card elevation/shadow is not evidenced and is omitted.

**hero** models full-bleed banners such as the Peanuts collection and video banners, which set white text (`color:#ffffff` observed on `.video-banner-heading h1`) over a dark or image background; the dark-surface fill here is a proposed stand-in since the actual hero background is likely an image/video not captured in static CSS.

**footer** is proposed as a dark band carrying social links and support text; no footer-specific selectors were supplied, so background and spacing are inferred from the site's general dark/light contrast pattern.

**badge** represents sale/discount labels like "-28%" and "-42%" shown throughout the product feed; the red accent color is present in the palette and assigned this role by inference, not by a matched selector.

**search** is the header search affordance; pill radius and soft-gray fill are proposed to match the rounded, minimal button language seen elsewhere on the site.

**color-swatch-selector** is a category-appropriate component for products listed with "4 Colors" / "3 Colors" options; swatch shape, border, and active-state ring are proposed conventions, not verified against captured markup.

## Responsive Behavior

Recommended, not measured, breakpoints:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–599px | single-column product grid, collapsed hamburger nav, sticky cart icon |
| tablet | 600–959px | 2-column product grid, mega-menu may collapse to accordion |
| desktop | 960–1279px | full mega-menu, 3–4 column grid |
| wide | 1280px+ | 4+ column grid, wider hero banners |

Touch targets should be at least 44px in height for buttons and swatches (`{spacing.xl}`-scale hit areas); mega-menu items should collapse into an accordion under ~960px. This table is a proposed responsive strategy consistent with the observed component sizing, not an observation of live breakpoints or actual mobile rendering.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from a static homepage capture: no rendered layout, computed styles, JavaScript-driven states, or mobile viewport behavior were observed. Body font-size and weight rely on unresolved CSS custom properties (`--font-body-family`, `--font-body-weight`), so `body-md` values are proposed defaults rather than measured facts. Hero, footer, nav-bar, and search components are inferred from partial selector evidence and general e-commerce convention, not confirmed markup. The "#f6d309" and "#f44336" accent-role assignments (badge/sale) are inferred from palette presence and typical usage, not from a matched selector proving their function. Hover, focus, active, and disabled states beyond the two documented button hovers are proposed, not observed. "Digital-7 V5" (countdown timer) and "Archivo Black" licensing/availability were not verified and should be confirmed before production use.
