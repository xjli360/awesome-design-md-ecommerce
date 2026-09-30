---
version: alpha
name: "Roverlund"
source_url: "https://roverlund.com"
captured_at: "2026-09-28T04:48:10.663346+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Roverlund's storefront runs on a Shopify Dawn-derived theme with a light, neutral base (#ffffff canvas, #000000 foreground) accented by a warm amber (#ffbc44) used for the CSS custom-property `--color-button` and the review-star color, confirming it as the primary brand accent. Body copy uses `--color-foreground` at a measured 1.5rem/0.06rem letter-spacing, while a secondary text tone (#414141) appears in the Judge.me review widget for reviewer names and star fills. Supporting grays (#dddddd, #eeeeee, #f4f4f4, #7b7b7b) form hairlines and soft surfaces typical of a minimal outdoor-gear aesthetic. Two additional hues, a muted sage (#809986) and a coral-pink (#ff5268), appear in the palette and are treated as inferred secondary accents, likely tied to product colorway swatches or promotional badges rather than core UI. Typography pairs a declared custom display face, Argent Pixel (with an explicit @font-face rule), against sans-serif fallbacks; Oswald and Titillium Web are present in the stylesheet font list and are inferred as heading/body candidates given their common Shopify-theme pairing, though the exact `--font-heading-family` and `--font-body-family` values were not resolved in the supplied CSS. All payment-network hex values (Visa/Amex/PayPal blues and reds) are excluded from the brand palette as third-party checkout iconography.

colors:
  primary: "#ffbc44"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#414141"
  muted: "#7b7b7b"
  hairline: "#dddddd"
  surface-soft: "#f4f4f4"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent-coral: "#ff5268"
  accent-sage: "#809986"
  accent-gold-light: "#ffc762"
  warm-canvas: "#e5e3df"
  deep-ink: "#1c1c1c"
typography:
  display-xl: {fontFamily: "'Nineties Headliner', 'Argent Pixel', sans-serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Argent Pixel', sans-serif", fontSize: 36px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Oswald, sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.96px}
  body-md: {fontFamily: "'Titillium Web', sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.53, letterSpacing: 0.96px}
  body-sm: {fontFamily: "'Titillium Web', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.6px}
  caption: {fontFamily: "'Titillium Web', sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.8px}
  button-md: {fontFamily: "Oswald, sans-serif", fontSize: 15px, fontWeight: 500, lineHeight: 1, letterSpacing: 1px}
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.warm-canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.deep-ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  fit-checker-panel:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    stepIndicatorColor: "{colors.primary}"
    labelTypography: "{typography.caption}"
    inputTypography: "{typography.body-sm}"

## Components
**button-primary** maps directly to the CSS custom properties `--color-button: 255,188,68` and `--color-button-text: 255,255,255`, giving a solid amber call-to-action button (e.g. "SHOP THE PET CARRIER"). Hover/active state darkening is proposed, not observed.

**button-secondary** inverts the primary treatment to a white background with amber text/border, matching the `--color-secondary-button` / `--color-secondary-button-text` pairing found in the root variables; used for lower-emphasis actions like "Continue shopping."

**text-input** is a proposed pattern for cart, search, and the pet-fit-checker numeric fields (weight, body length, shoulder height), styled with the neutral hairline border and standard body typography since no dedicated input CSS was supplied.

**nav-bar** reflects the sticky header implied by the menu list (Shop, Bundle & Save, See Us In The Wild, Reviews, Our Story) sitting on a white background with a thin hairline divider; exact height and scroll behavior are not observed.

**product-card** is inferred from the theme's `.product-card-wrapper .card` selector, which exposes border-radius, border-width and shadow custom properties without concrete values — treated here as a flat card on a light gray surface with no radius, consistent with the square-cornered button styling seen elsewhere.

**hero** represents the large "TRAVEL TOGETHER" landing banner; background is proposed as the warm off-white (#e5e3df) sampled from the palette, since no hero-specific selector was supplied.

**footer** is proposed as a dark, near-black panel (#1c1c1c) with white text, following common Shopify footer conventions; this specific styling was not confirmed in the extracted CSS.

**badge** models the accolade ticker ("People's Best Pet Carrier," "Oprah's Favorite Things") as an outlined pill using the foreground/background badge variables (`--color-badge-foreground`, `--color-badge-background`, `--color-badge-border`) explicitly present in `:root`.

**search** is a proposed lightweight input treatment for the header search icon/overlay referenced in the page text ("Search").

**fit-checker-panel** is a category-specific component modeling the four-step "Check Your Pet's Fit" flow (pet type, weight, body length, shoulder height) unique to Roverlund's travel-carrier sizing tool; layout and step-indicator color are proposed based on the primary accent, not measured.

## Responsive Behavior
Recommended, not measured breakpoints:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–599px | single-column hero, stacked nav collapsed to hamburger (proposed) |
| tablet | 600–989px | 2-column product grid (proposed) |
| desktop | 990px+ | full nav row, 3–4 column product grid (proposed) |

Touch targets should be a minimum 44×44px for the fit-checker inputs and cart controls. Header navigation is expected to collapse into a drawer/menu icon below the tablet breakpoint; this behavior is standard for Shopify Dawn-family themes but was not directly observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived from static CSS/text extraction only; no rendered page, computed styles, or interaction states (hover, focus, error, loading beyond the skeleton animation) were observed. The exact values of `--font-heading-family` and `--font-body-family` were never resolved in the supplied CSS, so Oswald/Titillium Web/Argent Pixel role assignments are inferred from their presence in the stylesheet's font list rather than confirmed selector output. `Nineties Headliner` and `JudgemeStar` appear only as font-family names without accompanying rules and are treated as unconfirmed display/icon fonts respectively. Border-radius and shadow values for product cards reference undefined CSS custom properties (`--product-card-corner-radius`, etc.) whose actual pixel values were not supplied, so all `rounded` tokens are proposed defaults. Payment-brand colors (Visa, Amex, PayPal, Meta, Twitter/X) were deliberately excluded from the brand palette as third-party checkout iconography. Mobile menu behavior, breakpoint pixel values, and any animation timing beyond the documented CSS duration variables are proposed conventions, not confirmed observations. Licensing and self-hosting terms for Argent Pixel were not verified.
