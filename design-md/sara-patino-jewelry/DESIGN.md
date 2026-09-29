---
version: alpha
name: "Sara Patino Jewelry"
source_url: "https://sarapatinojewelry.com"
captured_at: "2026-09-28T09:31:42.925597+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Sara Patino Jewelry's storefront CSS exposes a minimal, monochrome utility
  layer typical of a stripped Shopify theme: pure black (#000000) and white
  (#ffffff) anchor the palette, with soft neutral overlays (#0000000d,
  #00000033, #00000066, #3636364d) supplying muted text, scrims, and soft
  surfaces, plus a light hairline gray (#dedede) for dividers. Blue swatches
  (#1990c6/#136f99) and the multi-hue chips (#0071ce, #eb001b, #f79e1b,
  #ff5f00, #142fbd, #1532cb) originate from Shopify's accelerated-checkout
  button and card-network icons rather than the brand's own design language;
  they are retained only as functional/inferred accent options, never as
  primary identity colors. Typography centers on "Tenor Sans," a light,
  wide-set sans used for display and heading treatments that suits the
  brand's stated "simple, minimal, modern" positioning; body copy falls back
  to the generic sans-serif stack since no named body font was captured in
  evidence. Observed root tokens (--text-xs through --text-xl, roughly
  11–19px) anchor the smaller end of the type scale; larger display sizes
  below are proposed extrapolations, not measured headings. The resulting
  interpretation favors generous whitespace, thin black-on-white contrast,
  and restrained neutral tone rather than invented metallic/gold hex values,
  none of which were present in the supplied palette.

colors:
  primary: "#000000"
  ink: "#1c1c1c"
  canvas: "#ffffff"
  body: "#232323"
  muted: "#00000066"
  hairline: "#dedede"
  surface-soft: "#0000000d"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-checkout: "#1990c6"
  accent-checkout-hover: "#136f99"
  overlay-scrim: "#00000033"
  overlay-heavy: "#3636364d"
typography:
  display-xl: {fontFamily: "'Tenor Sans', sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Tenor Sans', sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "'Tenor Sans', sans-serif", fontSize: 19px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "sans-serif", fontSize: 13px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.3px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "4:5"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.overlay-scrim}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.overlay-heavy}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
  materials-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
    description: "Small inline label proposed for callouts like 'Recycled Gold' or 'Responsible Gemstones', matching the brand's mission copy."

## Components

**button-primary** is proposed as solid black on white, squared corners, reflecting the site's monochrome, no-radius aesthetic seen in the accelerated-checkout button's default 0px radius token. Hover/focus states are not observed and should be treated as proposed (e.g., inverse to `{colors.body}`).

**button-secondary** offers an outlined variant for lower-emphasis actions (e.g., "Add to Wishlist"), reusing ink-on-canvas contrast rather than a second brand color, since none was supplied.

**text-input** uses the light hairline gray for its border, a thin, minimal treatment consistent with the brand's "simple, minimal" language; focus-ring styling is not observed and is proposed only.

**nav-bar** reflects the header's CSS grid (`primary-nav logo secondary-nav`) and sticky positioning found in root tokens (`--header-is-sticky: 1`), with a hairline bottom border; exact link spacing/typography weight is inferred from the base text scale.

**product-card** is proposed for the Earrings/Rings/Necklaces/Bracelets grid implied by the nav taxonomy; no card-level CSS (image ratio, hover states) was present in evidence, so dimensions are inferred defaults suited to jewelry photography.

**hero** assumes a full-bleed dark or scrim-overlaid banner using the observed scrim alpha token (#00000033) over an image, consistent with a homepage lead section; text is set in the display scale, proposed at 48px since no explicit hero heading size was captured.

**footer** is proposed dark-on-light-text, mirroring the header's inverse contrast pattern; the newsletter/insider signup ("SPJ Insiders") implied by page text would live here, but its exact markup was not observed.

**badge** supports promotional or free-shipping messaging (e.g., the announcement bar text "FREE shipping on orders $150+"), using a soft neutral fill rather than a saturated accent color, since no such color was in the observed palette.

**search** is a standard minimal search field; no distinct search UI CSS was captured, so styling mirrors `text-input` conventions.

**materials-tag** is a category-appropriate addition for a sustainability-forward handmade jewelry brand, surfacing phrases like "recycled gold" and "responsible gemstones" drawn directly from the page's mission copy; visual treatment is proposed, not observed.

## Responsive Behavior

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | < 480px | Single-column nav collapses to a hamburger/drawer pattern; header grid shifts to stacked `logo` + `primary-nav` rows, consistent with the alternate `--header-grid` rule seen in evidence. |
| Small tablet | 480–767px | Two-column product grid; container gutter narrows toward the `2rem` root token. |
| Tablet/Desktop | 768–1023px | Three-column product grid; container gutter at `3rem` per root token. |
| Desktop | ≥ 1024px | Full three-part header grid (`primary-nav logo secondary-nav`); section vertical spacing approaches the `4–6rem` values seen in root tokens. |

Touch targets should meet a 44px minimum height, matching the `clamp(25px, …, 55px)` range used by Shopify's accelerated-checkout button. Mobile navigation collapse behavior, drawer animation, and exact grid column counts are **recommendations only** and were not measured from live rendered layout.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This document is derived from static CSS/custom-property extraction only; no rendered page, computed layout, or interaction states (hover, focus, active, disabled) were observed.
- Several palette hexes (#0071ce, #eb001b, #f79e1b, #ff5f00, #142fbd, #1532cb, #1990c6, #136f99) originate from Shopify checkout/payment-widget CSS, not confirmed brand identity colors; they are included per evidence but labeled as functional/inferred, not primary.
- No distinct body-copy font family was found in evidence beyond the generic `sans-serif` keyword; actual rendered body font could differ.
- "Tenor Sans" availability, licensing, and actual weight range were not verified beyond its presence in the `font_families` list.
- Display/heading font sizes (48px, 32px) are proposed extrapolations; only smaller `--text-xs` through `--text-xl` (11–19px) root tokens were directly observed.
- Rounded and spacing scales largely follow a standard proposed system; only a subset (e.g., 16px chat radius, 48px/64–96px spacing hints) align with observed root tokens.
- Mobile drawer/menu behavior, product grid column counts, and card hover states are proposed patterns based on common Shopify theme conventions, not confirmed for this specific store.
