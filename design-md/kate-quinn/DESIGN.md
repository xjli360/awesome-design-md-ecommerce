---
version: alpha
name: "Kate Quinn"
source_url: "https://katequinn.com"
captured_at: "2026-09-29T03:57:57.059273+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Kate Quinn's storefront theme (Shopify) exposes a restrained, editorial palette anchored in near-black (#111111, #000000) buttons and text over a white (#ffffff) canvas, with a family of soft neutral grays (#f2f2f2, #f5f5f5, #fafafa, #e6e6e6, #c9c9c9) used for dimmed sections, cards, and hairlines per the theme's CSS custom properties (--colorBtnPrimary, --colorBodyDim, --colorBorder). A dark charcoal (#27282a) marks the announcement bar, and a muted slate (#45494c) appears in the review-widget's text/star color, suggested here as a secondary body-text tone. A single warm red (#d02e2e) is proposed as the sale/clearance accent, inferred from an inline "color: red" rule on the Seasonal Clearance link, since no literal red hex was declared there. Typography is serif-forward: Gilda Display drives both the --typeHeaderPrimary and --typeBasePrimary tokens (38px headers, 16px body, weight 400), while Goudy Old Style appears on product-recommendation titles (24px, uppercase, centered). Arial/Helvetica sans-serif fallbacks are assumed for compact UI text such as buttons and quantity controls, where a bold weight was observed. Buttons use a squared corner (--buttonRadius: 0), while a 5px radius appears on hotspot tooltips — both are preserved as distinct rounding tokens. This interpretation favors a quiet, heirloom-boutique feel consistent with the brand's "heirloom quality" customer language.

colors:
  primary: "#111111"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#45494c"
  muted: "#777777"
  hairline: "#c9c9c9"
  surface-soft: "#f2f2f2"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  surface-dim: "#f5f5f5"
  border-light: "#e6e6e6"
  announcement-bg: "#27282a"
  announcement-text: "#ffffff"
  accent-sale: "#d02e2e"
  alert-dot: "#ff4e4e"
typography:
  display-xl: {fontFamily: "'Gilda Display', serif", fontSize: "48px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "0em"}
  display-md: {fontFamily: "'Gilda Display', serif", fontSize: "38px", fontWeight: 400, lineHeight: 1.0, letterSpacing: "0em"}
  title-md: {fontFamily: "'Goudy Old Style', serif", fontSize: "24px", fontWeight: 400, lineHeight: 1.3, letterSpacing: "0.02em"}
  body-md: {fontFamily: "'Gilda Display', serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0.025em"}
  body-sm: {fontFamily: "'Gilda Display', serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.02em"}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.04em"}
  button-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "14px", fontWeight: 700, lineHeight: 1.0, letterSpacing: "0.05em"}
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
    padding: "{spacing.sm} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    borderBottom: "1px solid {colors.border-light}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    hoverElevation: "0 5px 5px #0000001a"
  hero:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-md}"
    subtitleTypography: "{typography.body-md}"
    overlayColor: "{colors.ink}"
    overlayOpacity: 0.1
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-dim}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.md}"

## Components

**button-primary**: Maps directly to the theme's `--colorBtnPrimary` (#111111) and `--colorBtnPrimaryText` (#ffffff) tokens, used for add-to-cart and checkout actions observed in `.spot-quick-view-add button`. Zero corner radius reflects the observed `--buttonRadius: 0`.

**button-secondary**: Proposed outline variant for secondary actions (e.g., "quick view," "more info") using the observed border gray; no direct CSS rule for a secondary button was captured, so styling is inferred from the primary pattern.

**text-input**: Proposed field style for search/newsletter forms; observed values are limited to border and background tokens from `:root`, so padding and radius are estimated.

**nav-bar**: Represents the top navigation/header bar implied by the extensive "shop by collection / gender / style / size" menu text; exact height and collapse behavior were not present in the CSS evidence.

**product-card**: Grounded in `.spot-product-recommendations .name` (Goudy Old Style, 24px, uppercase, centered) for the title; card background and hover shadow are inferred from theme dim/light tokens and the observed `.hero .flickity-button` box-shadow pattern.

**hero**: Proposed banner component for slideshow/preorder promotions ("preorder spring woods," "spooky shop now") referenced in page text; overlay opacity of 0.1 is taken directly from `--colorGridOverlayOpacity`.

**footer**: Built from `--colorFooter`/`--colorFooterText` tokens (white background, black text); link list structure (Company Info, Help) is inferred from page text, not measured layout.

**badge**: Proposed clearance/sale indicator using the inferred accent-sale red, standing in for the unresolved literal "color: red" rule applied to the Seasonal Clearance nav link.

**search**: Proposed search affordance keyed to the `icon-search` reference in page text; visual treatment (dim surface, rounded corners) is estimated, as no dedicated search-bar CSS was supplied.

**size-selector**: Category-appropriate component for the "shop by size" taxonomy (NB to 18-24m through XL/XXL); styled as a pill/chip toggle using primary-color selected state, entirely proposed since no size-swatch CSS was captured.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width       | Layout notes (proposed) |
|-----------|-------------|--------------------------|
| mobile    | ≤ 599px     | Single-column product grid, hamburger nav collapses full menu, touch targets ≥ 44px |
| tablet    | 600–999px   | 2–3 column product grid, size-selector chips wrap |
| desktop   | 1000–1439px | Persistent top nav with dropdown mega-menu (per observed collection/gender/style/size groupings) |
| wide      | ≥ 1440px    | Max content width constrained, hero imagery scales with `object-fit: cover` |

Touch targets for buttons and size-selector chips should maintain a minimum 44×44px hit area on mobile. Navigation collapse behavior (hamburger icon referenced as `icon-hamburger` in page text) is assumed standard for Shopify themes but was not confirmed via interaction testing.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- All CSS was extracted statically; no rendered layout, computed styles, or responsive breakpoints were observed directly.
- Color role assignments (e.g., `body`, `muted`, `accent-sale`) are inferred from partial selector context (review widget, inline `color: red`) and may not reflect true brand usage across all page states.
- Font availability and licensing for "Gilda Display" and "Goudy Old Style" were not verified; both may be third-party or self-hosted webfonts not confirmed as brand-proprietary.
- Typography sizes beyond the explicitly declared `--typeHeaderSize` (38px) and `--typeBaseSize` (16px) are proposed estimates for scale consistency.
- Rounded and spacing scales follow a standard proposed ramp; only `0px` (button radius) and `5px` (hotspot tooltip) were directly observed in CSS.
- No hover, focus, active, or error states were observed; all interactive state styling in components is labeled proposed.
- Mobile menu, cart drawer, and search overlay visual behavior were referenced in page text (`icon-X Close menu`, `Close cart`) but not styled in supplied CSS.
