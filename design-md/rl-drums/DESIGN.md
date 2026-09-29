---
version: alpha
name: "RL Drums"
source_url: "https://www.rldrums.com"
captured_at: "2026-09-28T09:33:37.160548+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  RL Drums runs on a Shopify Dawn-derived theme whose CSS custom properties define
  a near-monochrome storefront: white canvas (#ffffff), near-black ink (#121212)
  used for both foreground text and primary buttons, and white text on those
  buttons (on-primary). Supporting neutrals (#f3f3f3, #eeeeee, #dedede, #cccccc,
  #7b7b7b) appear in loading skeletons, card backgrounds and muted UI chrome,
  and are reused here for surface, hairline and muted-text roles. A red
  (#dd1d1d) and a blue pairing (#1990c6 / #136f99, the latter a hover state on
  Shopify's unbranded accelerated-checkout button) are present in the CSS and
  are inferred as an alert/promo accent and a secondary interactive accent,
  respectively, since no explicit brand-accent variable was supplied. Payment-
  network colors (Visa/Mastercard/Amex hues) were excluded as brand roles.
  Typography is inferred from two observed families: "Archivo Narrow" (a
  condensed sans well suited to headings/display type) and "Assistant" (a
  humanist sans used for body copy); JudgemeStar is an icon font for the
  review-star widget only, not prose type. The interpretation favors a flat,
  square-cornered, high-contrast utilitarian aesthetic consistent with the
  0px button/skeleton radii found in the CSS.

colors:
  primary: "#121212"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#121212"
  muted: "#7b7b7b"
  hairline: "#cccccc"
  surface-soft: "#f3f3f3"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent-alert: "#dd1d1d"
  accent-info: "#1990c6"
  accent-info-hover: "#136f99"
  surface-dark: "#1c1c1c"
  surface-dark-alt: "#232323"
  skeleton: "#dedede"
  overlay: "#00000080"
typography:
  display-xl: {fontFamily: "Archivo Narrow, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Archivo Narrow, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Archivo Narrow, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.3px}
  body-md: {fontFamily: "Assistant, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.3px}
  body-sm: {fontFamily: "Assistant, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0.2px}
  caption: {fontFamily: "Assistant, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "Assistant, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark-alt}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  review-stars:
    iconColor: "{colors.ink}"
    trackColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.none}"

## Components

**button-primary** renders the site's dominant call-to-action (e.g. "SHOP", "CHECK OUT") using the near-black `--color-button` value against white text, matching the Shopify-CSS pairing of `--color-button: 18,18,18` / `--color-button-text: 255,255,255`. Corner radius is set to none, reflecting the 0px default seen in the accelerated-checkout and skeleton CSS. Hover/active states are proposed, not observed.

**button-secondary** is inferred from the theme's `--color-secondary-button` (white) / `--color-secondary-button-text` (near-black) pair, giving an outlined, inverse treatment for lower-emphasis actions like "Continue shopping."

**text-input** covers search and form fields such as the newsletter signup ("BE A LEGEND... EMAIL"). Border color and radius are proposed conventions since no explicit input CSS was supplied.

**nav-bar** represents the persistent header with the deep drums/cymbals mega-menu (Drum Sets, Bass Drums, Cajon, Cymbals, Gongs, etc.). Layout and collapse behavior are proposed; only color/typography variables are grounded in evidence.

**product-card** models the featured-product grid (e.g. "Soundwave Master Custom Glory Sound... $3,835.00"), using the light gray card surface and hairline border implied by the theme's card CSS variables (`--product-card-corner-radius`, border/shadow tokens), whose concrete values were not resolved in the supplied CSS.

**hero** covers the homepage banner ("SUPERIOR DRUMS & CYMBALS"). A dark surface is proposed for visual contrast against the product photography; this is a design proposal, not a captured background color.

**footer** groups site links (About Us, Endorsements, Affiliates, Location, Contact) and social icons. A dark surface variant is proposed to visually separate it from the white body canvas.

**badge** is proposed for promotional flags such as "FREE SHIPPING ON ALL ORDERS" or B-Stock/Used labeling, using the one clearly non-neutral palette color (#dd1d1d) as an attention accent — its actual UI usage was not confirmed in the evidence.

**search** models the header search affordance ("Search" link in nav), using the soft surface color for visual separation from the pure-white canvas.

**review-stars** is a category-appropriate component for the customer-review carousel (Scott S., Todd H., etc.), reflecting the JudgemeStar icon font and the `--jdgm-star-color: #000` / `--jdgm-primary-color: #000` tokens found in the CSS.

## Responsive Behavior

Recommendation only — no mobile/tablet layout was observed in the supplied evidence.

| Breakpoint | Width      | Notes (proposed) |
|-----------|------------|-------------------|
| mobile    | <600px     | Single-column product grid; nav collapses to a hamburger/drawer menu covering the deep Drums/Cymbals category tree. |
| tablet    | 600–999px  | 2-column product grid; mega-menu may condense to accordion sections. |
| desktop   | 1000–1439px| 3–4 column product grid; full horizontal nav with mega-menu dropdowns. |
| wide      | ≥1440px    | 4+ column grid; increased section padding using `{spacing.section}`. |

Touch targets should be at least 44px in the block dimension, matching the `clamp(25px, ..., 55px)` sizing pattern seen on the Shopify payment button. Category mega-menus (Drums, Cymbals) should collapse to expandable accordions below tablet width. All figures above are proposed conventions, not measured breakpoints.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no rendered layout, real breakpoints, hover/focus states, or JavaScript-driven interactions (cart drawer, mega-menu behavior, product carousels) were observed.
- Mapping of "Archivo Narrow" to headings and "Assistant" to body text is inferred from typical usage patterns of condensed vs. humanist sans fonts; the exact `--font-heading-family` / `--font-body-family` assignments were not directly resolvable from the supplied rules.
- Font licensing/availability (whether these are Google Fonts or custom-licensed) was not verified.
- Actual root font-size (affecting rem-to-px conversion for the 1.5rem body size) was not supplied, so all pixel values in `typography` are proposed approximations, not measured.
- Card, button, and skeleton corner-radius values are driven by unresolved CSS custom properties (e.g. `--product-card-corner-radius`, `--buttons-radius-outset`); `rounded.none` was chosen only because the one concrete default seen (accelerated-checkout/skeleton) was 0px.
- The red (#dd1d1d) and blue (#1990c6/#136f99) accent roles are inferred; the blue pair specifically originates from Shopify's generic "unbranded" payment-button CSS and may not represent an intentional brand accent.
- Payment-network brand colors present in the raw palette (Visa/Mastercard/Amex-associated hues) were deliberately excluded from the design system as non-brand.
- No confirmation of actual product-grid column counts, container widths, or spacing scale beyond the fixed template values requested.
