---
version: alpha
name: "U-Turn Audio"
source_url: "https://www.uturnaudio.com"
captured_at: "2026-09-28T04:12:55.065011+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The extracted evidence is dominated by neutrals: black, white, and a
  tight run of grays (#333333, #3c3c3d, #999999, #e5e5e5, #f9f9f9,
  #f5f5f5) that structure buttons, borders, and body copy across
  product.scss.css. The single clearly-observed interactive color is
  #333333, used as both button border/text and the background a
  button transitions to on hover, with #f9f9f9 as the resulting
  on-dark text color. Typography is limited to Roboto for content
  (30px/500 product names, 19px/500 buttons, 16px/300 descriptions,
  19px/400 prices) and FontAwesome for iconography; no display or
  serif face was observed. Palette entries such as #fad31f, #31a8d2,
  #4bd963, and #c0363a are present in the evidence but not tied to
  any selector in the supplied rules, so they are treated here as
  inferred accent/status colors (likely social-share icons or
  sale/success/error UI) rather than confirmed brand hues. The
  resulting interpretation leans utilitarian and hardware-catalog in
  tone: dark-gray-on-white primary actions, generous whitespace
  implied by min-height rules, and a restrained accent system reused
  sparingly for badges and status feedback rather than as a loud
  brand color.

colors:
  primary: "#333333"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#999999"
  hairline: "#e5e5e5"
  surface-soft: "#f9f9f9"
  surface-card: "#f5f5f5"
  on-primary: "#f9f9f9"
  icon-dark: "#3c3c3d"
  accent: "#fad31f"
  info: "#31a8d2"
  success: "#4bd963"
  danger: "#c0363a"
typography:
  display-xl: {fontFamily: "Roboto, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Roboto, sans-serif", fontSize: 30px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Roboto, sans-serif", fontSize: 19px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, sans-serif", fontSize: 16px, fontWeight: 300, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Roboto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Roboto, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Roboto, sans-serif", fontSize: 19px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.3px}
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
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.display-md}"
    priceTypography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.hairline}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  wishlist-toggle:
    backgroundColor: "{colors.icon-dark}"
    hoverBackgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    activeTextColor: "{colors.primary}"
    rounded: "{rounded.none}"
    height: "38px"

## Components

**button-primary** models the filled state a `long-button` reaches on hover (`background-color:#333` with `#f9f9f9` text), presented here as the default primary action for adding-to-cart or checkout flows; the transparent-to-filled transition itself is an observed interaction, so this reflects that end state as the resting primary style.

**button-secondary** mirrors the resting `a.long-button button` style — transparent background, 2px `#333` border, `#333` text — used for lower-emphasis actions like "Learn More" links seen alongside product blocks.

**text-input** is a proposed pattern; no form-field CSS was supplied, so border, radius, and padding follow the hairline/spacing scale rather than any observed input rule.

**nav-bar** is proposed structurally. No header/navigation selectors were present in the evidence; the light canvas background and hairline divider are inferred from the site's overall neutral palette, not measured.

**product-card** draws directly on `.product-block .name a` (30px/500 Roboto) and `.product-price` (19px/400 Roboto) for its title and price typography, with a light gray card surface proposed to separate cards from the page canvas.

**hero** is proposed. The `long-button-hero` rule (white border/text button meant to sit on a non-white surface) implies a dark hero background, so `colors.ink` is used as an inferred hero backdrop with inverted text.

**footer** is proposed; no footer-specific selectors were observed, so its soft off-white background and muted text reuse tokens already confirmed elsewhere on the site.

**badge** and **search** are proposed ecommerce-support patterns; the accent yellow is reused here for a badge (e.g., "New" or "Sale") since no dedicated badge selector was captured, and search styling follows the general card/input treatment.

**wishlist-toggle** is grounded in `.product-block .functional-buttons .btn` (background `#3c3c3d`, hover `#000`, 38px height) and `.btn-wishlist.added` (`#333` active state), representing the product-card icon row for wishlist/cart actions typical of an accessories storefront.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| Mobile | <768px | Single-column product grid; nav collapses to a menu toggle (proposed). |
| Tablet | 768–1024px | Two-column product grid; hero padding reduces to `{spacing.xl}`. |
| Desktop | >1024px | Multi-column product grid; full nav-bar visible. |

Touch targets should be at least 44×44px, exceeding the observed 38px `.functional-buttons .btn` height on touch devices. Buttons and cards should stack vertically below the mobile breakpoint; no actual collapse or menu behavior was observed in the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is built from a partial CSS extract (`product.scss.css`) plus a raw color list, not a full stylesheet audit or rendered-page inspection. Layout, grid structure, header/footer markup, and any responsive/media-query behavior were not observed and are marked proposed throughout. Several palette entries (#fad31f, #31a8d2, #4bd963, #72c13d, #c0363a, #e55e5e, #78bfe8) appear in the source color list without an associated selector, so their semantic roles (accent, info, success, danger) are inferred guesses, not confirmed brand usage — they may belong to third-party widgets, social icons, or swatch/variant colors instead. Font sizes beyond the four directly observed (16px, 19px, 19px, 30px) are proposed extrapolations to fill out a type scale. FontAwesome's availability is confirmed only for icon glyphs (`content:"\f061"`), not as a general typeface. Roboto is an open, freely licensed font, but no `@font-face` or hosting details were supplied, so exact weight/style availability is unverified. No hover, focus, active, or disabled states were observed beyond the two button `:hover` rules and the `.added` wishlist state; all other interaction and mobile-menu behavior is unverified.
