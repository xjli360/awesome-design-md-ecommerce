---
version: alpha
name: "Rubio Monocoat"
source_url: "https://rubiomonocoatusa.com"
captured_at: "2026-09-28T04:49:23.956140+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Rubio Monocoat USA is a Shopify-built storefront for a hardwax-oil wood
  finish and stain brand, selling interior/exterior protection products,
  application tools, and an extensive shade catalog (Oil Plus 2C, DuroGrit,
  WoodCream). The observed CSS exposes a header with --text-color: 24 48 41
  (#183029), a white --bg-color, and an --header-accent-color of rgb(57 106
  72), a deep forest green close to the palette's #24443a; the exact accent
  hex is not present in the supplied palette array, so #24443a is used as an
  inferred stand-in for brand-forward elements. Supporting neutrals (#f2f2f2,
  #f5f5f5, #f7f7f7, #e1e1e1, #dedede) and a soft sage family (#b9cbc5,
  #c7d4ce, #e8f6ea) suggest a natural, matte, workshop-adjacent tone
  consistent with a wood-care brand. Payment-network hexes (Visa/Mastercard/
  PayPal blues, reds, oranges) are excluded from brand tokens as they are
  third-party icon colors, not brand palette. No proprietary heading or body
  typeface was found in evidence; only Arial, Helvetica, Times and
  sans-serif appear, so all typography here uses generic system fallbacks.
  The stylesheet default of --btn-border-radius: 0 is treated as an observed
  signal favoring squared, utilitarian button geometry. Component padding,
  breakpoints, and most type sizes are proposed and clearly labeled as such.

colors:
  primary: "#24443a"
  ink: "#183029"
  canvas: "#ffffff"
  body: "#183029"
  muted: "#777777"
  hairline: "#e1e1e1"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  surface-tint: "#e8f6ea"
  accent-sage: "#b9cbc5"
  accent-sage-light: "#c7d4ce"
  surface-muted-2: "#f2f2f2"
  border-strong: "#d5d5d5"
  ink-alt: "#1c1c1c"
typography:
  display-xl: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 34px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.2px}
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.surface-tint}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-sage-light}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "#e8eaea"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs}"
    border: "1px solid {colors.hairline}"

## Components

**button-primary** is the main call-to-action treatment (e.g. "View Oil Plus 2C", "Order a sample"), using the inferred deep-green brand color at full opacity with white text. The `rounded.none` value reflects the observed `--btn-border-radius, 0` fallback in the button-select CSS, indicating squared corners are the default, not a rounded pill.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g. "Learn more"), derived from the `.btn--secondary` rule showing `background-color: transparent` and an alt text color equal to the button background variable — reproduced here as an outlined primary-color button.

**text-input** models generic form fields (search, email capture, quantity) using the observed `--input-bg-color` / `--input-text-color` pattern tied to the page's bg/text variables, with a hairline border; exact border-radius and padding are proposed.

**nav-bar** represents the site header, grounded in the explicit `--nav-bg-color: 255 255 255` and `--nav-text-color: 24 48 41` variables — a white bar with dark forest-green text and links. Dropdown/mega-menu behavior for categories like Interior, Exterior, Tools, Colors, and Learn is proposed, not observed in static CSS.

**product-card** covers listing tiles for items like "Oil Plus 2C – 390 mL" or "DuroGrit," which in the page text show star ratings, review counts, and "From $X" pricing plus a color-swatch strip. Card background, border, and radius are proposed conventions layered on the observed white/hairline neutrals.

**hero** is the top-of-page promotional band (e.g. "Durable color & protection"), proposed to sit on the pale mint tint (`#e8f6ea`) to differentiate it from the pure white body background, using the largest display typography.

**footer** is proposed as a dark, brand-green band reversing the header's light treatment, providing contrast for legal links, newsletter signup, and social icons; this inversion is a common Shopify-theme pattern, not confirmed from evidence.

**badge** supports labels seen in the text excerpt such as "Best Seller" and "New arrival," rendered as a small pill using the light sage accent for a soft, natural-product feel; shape and color are proposed.

**search** reflects the explicit `--search-bg-color: #e8eaea` token from the header CSS, applied to the search input/trigger area distinct from the white nav background.

**color-swatch-selector** is a category-appropriate component for this brand: the page text lists dozens of stain/finish shade names (Pure, Espresso-adjacent tones like "Cortado," "Mocha," greys like "Ash Grey," "Charcoal") per product. This component proposes a compact grid of small swatch tiles with hairline borders on a soft neutral background, letting shoppers pick a finish color before purchase — an interaction pattern strongly implied by the repeated shade lists but not visually confirmed.

## Responsive Behavior

Recommended breakpoints (not measured from live layout, proposed for a typical Shopify theme):

| Breakpoint | Width       | Behavior (proposed) |
|-----------|-------------|----------------------|
| Mobile    | < 750px     | Single-column stacking, nav collapses to a hamburger/drawer, gutter ≈ `{spacing.base}`–`{spacing.lg}` |
| Tablet    | 750–999px   | 2-column product grids, gutter ≈ `{spacing.xl}` (aligns loosely with observed `--gutter-md: 32px`) |
| Desktop   | 1000–1535px | 3–4 column grids, full mega-menu nav, gutter ≈ `{spacing.xxl}`–`{spacing.section}` (aligns loosely with observed `--gutter-lg: 80px`) |
| Wide      | ≥ 1536px    | Max content width governed by the observed `--fluid-max-vw: 1536` fluid-type ceiling |

Touch targets for buttons and swatch tiles should be at least 44px per side, matching the `.rebuy-select-dropdown__button` `min-height: 44px` seen in evidence. Category mega-menus (Interior/Exterior/Tools/Colors/Learn) should collapse to an accordion pattern on mobile; this is a recommendation only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS/text extraction and carries several limitations: no live-rendered layout, spacing, or interaction states (hover, focus, open menus, cart drawer) were observed. The `--header-accent-color` (rgb 57 106 72 / #396a48) appears in CSS but is not present in the supplied hex palette, so `#24443a` was substituted as the nearest inferred brand-green primary — this mapping is unverified. No proprietary heading or body typeface was found; all typography uses generic Arial/Helvetica/sans-serif fallbacks, and font licensing/availability for any future custom face is unverified. Numeric type sizes, the full spacing scale, component padding, and border-radius values beyond the observed `0` button default are proposed conventions, not measured pixels. Payment-network colors (Visa, Mastercard, PayPal) were deliberately excluded from brand tokens as third-party iconography. Mobile menu structure, swatch-selector interaction, and card grid column counts are inferred from typical e-commerce/Shopify conventions rather than confirmed site behavior.
