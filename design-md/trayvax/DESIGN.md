---
version: alpha
name: "Trayvax"
source_url: "https://trayvax.com"
captured_at: "2026-09-28T10:08:34.562904+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Trayvax's storefront is a Shopify (Dawn-derived) theme built on a neutral,
  high-contrast grayscale system — pure black (#000000), near-black ink
  (#121212), and a stack of mid-grays (#333333, #757575, #dedede) against
  white and off-white surfaces (#ffffff, #f5f5f5, #fcfcfc). This reads as a
  utilitarian, tactical-adjacent aesthetic consistent with a made-in-USA
  metal/leather EDC wallet brand: minimal color, heavy reliance on
  photography and material swatches to carry visual interest. A single red
  (#c62828, with alpha variants) appears tied to sale pricing and is treated
  here as the accent/sale color; a muted blue (#2c6ecb) is inferred as the
  default text-link color; an amber (#eaad15) is inferred as a rating/star
  color. Payment-network brand colors present in the CSS (Mastercard/Visa
  hues) are excluded from the brand palette as third-party marks. Typography
  is Inter for UI and headings, with a monospace fallback stack
  (SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono) inferred for
  small technical/price or code-style elements. Heading and body sizes are
  taken directly from the site's `--text-*` custom properties across two
  breakpoint sets. Spacing/radius scales below are proposed conventions, not
  measured pixel values, since only variable names (`--spacing-*`) were
  present in evidence.

colors:
  primary: "#000000"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#757575"
  hairline: "#dedede"
  surface-soft: "#f5f5f5"
  surface-card: "#fcfcfc"
  on-primary: "#ffffff"
  accent-sale: "#c62828"
  accent-sale-soft: "#c6282814"
  accent-sale-border: "#c6282873"
  link: "#2c6ecb"
  link-soft: "#f2f7fe"
  rating: "#eaad15"
  border-strong: "#999999"
  overlay-dark: "#00000066"
typography:
  display-xl: {fontFamily: "Inter, sans-serif", fontSize: 80px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Inter, sans-serif", fontSize: 60px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Inter, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: 17px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Inter, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.1px"}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.2, letterSpacing: "0.2px"}
  price-mono: {fontFamily: "SFMono-Regular, Menlo, Monaco, Consolas, monospace", fontSize: 15px, fontWeight: 500, lineHeight: 1.3, letterSpacing: "0px"}
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
    borderColor: "{colors.hairline}"
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
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price-mono}"
    salePriceColor: "{colors.accent-sale}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    overlayColor: "{colors.overlay-dark}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    hairlineColor: "#ffffff1f"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-sale-soft}"
    borderColor: "{colors.accent-sale-border}"
    textColor: "{colors.accent-sale}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  swatch-selector:
    itemShape: "{rounded.full}"
    itemBorderColor: "{colors.hairline}"
    itemBorderColorSelected: "{colors.primary}"
    labelTypography: "{typography.caption}"
    gap: "{spacing.xs}"

## Components

**button-primary** is the black-on-white call-to-action pattern ("SHOP WALLETS", add-to-cart) inferred from the dominant `#000000`/`#121212` tones and the theme's `--button-background` hover-opacity variable (0.85), which is proposed here as a hover state.

**button-secondary** is an outline variant for lower-emphasis actions (e.g. "View All Wallets"), using the hairline gray border rather than a filled background; hover/focus treatment is proposed, not observed.

**text-input** covers search and account/login fields; padding and radius are proposed conventions since no explicit input CSS was supplied, sized to align with the `--input-gap: 1rem` variable seen in the evidence.

**nav-bar** reflects the two header grid templates found in evidence (`logo` + `main-nav` + `secondary-nav`), with a responsive logo that grows from 170×61px to 210×75px; this is treated as an observed breakpoint-driven behavior rather than an assumption.

**product-card** models the collection/PLP tiles (e.g. "Traverse - Black Magsafe Kickstand Wallet") showing strike-through regular price alongside a red-accented sale price, matching the repeated "Sale price / Regular price" text pattern in the evidence.

**hero** is proposed as a full-bleed dark image banner ("USA Made Multi-Functional Wallets & Gear, Built To Last!") using the ink/overlay tones, since large `--text-h0` sizes (64–80px) strongly imply a big hero headline treatment.

**footer** is inferred as a dark footer band paralleling the hero, using the same ink background and a semi-transparent white hairline (`#ffffff1f`) for divider lines between link columns.

**badge** covers "Sale," "New," and "Sold out" labels seen across product listings; the soft/border alpha values (`#c6282814`, `#c6282873`) directly reuse the accent-sale hue at different opacities, so this component is grounded rather than invented.

**swatch-selector** is a category-specific pattern for wallet material/color options (e.g. "Tobacco Brown," "Stealth Black," "Titanium," "Brass") repeated extensively in the product evidence; circular swatches with a bordered selected state are proposed as a standard e-commerce convention, not a measured interaction.

## Responsive Behavior

| Breakpoint | Approx width | Notes (proposed) |
|---|---|---|
| Mobile | < 750px | Single-column product lists (`--product-list-items-per-row: 1`), carousel item width ~74vw, as seen in evidence. |
| Tablet | 750–999px | Two-column product grids (`--product-list-items-per-row: 2`, ~36vw carousel items); header logo remains compact. |
| Desktop | ≥ 1000px | Up to 5-column product grids; enlarged logo (210×75px) and expanded `--section-*` spacing tokens observed in root variables. |

Touch targets are recommended at a minimum 44×44px for nav, cart, and swatch controls. Mobile navigation is assumed to collapse into a hamburger/off-canvas menu ("Open navigation menu" text was present in evidence), but the actual collapse mechanics, animation, and menu layout were not observed and are proposed conventions only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties and page text only; no rendered layout, computed styles, or interaction states (hover, focus, active, disabled) were directly observed. Color-to-role mapping (e.g. designating `#000000` as primary, `#2c6ecb` as link, `#eaad15` as rating) is inferred from conventional e-commerce usage and variable naming, not confirmed via screenshots. Spacing and radius scales are proposed numeric conventions; the site only exposes named `--spacing-*` tokens without resolved pixel values, so exact spacing is unverified. Typography sizes are taken from `--text-*` rem values (assuming a 16px root) across two responsive variable blocks, but which block applies at which breakpoint was not fully disambiguated. The monospace font stack's actual usage location (price, code, or countdown timers) is inferred, not confirmed. Custom font licensing/self-hosting for Inter was not verified. Mobile menu, cart drawer, and swatch-selector interaction behavior were not observed and are marked proposed throughout.
