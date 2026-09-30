---
version: alpha
name: "Zinc Flyte"
source_url: "https://zincsports.com/en-us/pages/flyte"
captured_at: "2026-09-29T04:11:15.958333+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This specification interprets the Flyte kids' scooter-suitcase range as presented on
  zincsports.com, the current parent brand site for Zinc/Flyte products (not a
  reconstruction of a former standalone flyte.com site). The observed CSS shows a
  playful, high-contrast commerce theme: a warm yellow primary action color (#f8d05b)
  paired with pure black text and borders, set against a white canvas with light gray
  surface tones for cards and hover skeletons. Buttons are hard-edged (border-radius:
  0px, confirmed in source) and invert to solid black on hover/active, giving a bold,
  scooter-brand energy rather than a soft rounded aesthetic. Typography is anchored on
  "Nunito Sans" (self-hosted @font-face, confirmed) with Arial/sans-serif fallback;
  button copy is explicitly 15px/400 weight in the source. Other font names present in
  the raw evidence (GT Walsheim, Jost, Archivo, Antique Olive Nord D, Font Awesome
  families) are not tied to any confirmed selector on this page and are treated as
  third-party/app or icon-font artifacts, not brand type. Review-widget colors (mustard
  #d3ce1d, star #f8d05b) are reused here as accent tokens. Card, hairline, and muted
  text roles are inferred from generic surface/gray values in the palette since no
  dedicated component selectors for cards were supplied. All spacing, rounding (beyond
  the confirmed 0px), and most typographic sizes are proposed, not measured.

colors:
  primary: "#f8d05b"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#5c5c5c"
  hairline: "#e2e2e2"
  surface-soft: "#f8f8f8"
  surface-card: "#fcfcfc"
  on-primary: "#000000"
  accent-dark: "#282828"
  rating: "#d3ce1d"
  link: "#4787ed"
  danger: "#d32d2d"
  success: "#108043"
typography:
  display-xl: {fontFamily: "\"Nunito Sans\", Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "\"Nunito Sans\", Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "\"Nunito Sans\", Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "\"Nunito Sans\", Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "\"Nunito Sans\", Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "\"Nunito Sans\", Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "\"Nunito Sans\", Arial, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1em, letterSpacing: 0px}
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
    border: "1.5px solid {colors.primary}"
    hoverBackgroundColor: "{colors.ink}"
    hoverBorderColor: "{colors.ink}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1.5px solid {colors.accent-dark}"
    hoverBackgroundColor: "{colors.accent-dark}"
    hoverTextColor: "{colors.canvas}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: "82px"
    borderBottomColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    shadow: "none"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.accent-dark}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  price-display:
    currentPriceColor: "{colors.ink}"
    currentPriceTypography: "{typography.title-md}"
    comparePriceColor: "{colors.muted}"
    comparePriceTypography: "{typography.body-sm}"
    discountBadgeBackground: "{colors.rating}"
    discountBadgeTextColor: "{colors.ink}"

## Components

**button-primary** renders the confirmed source pattern: `#f8d05b` fill, black 1.5px border, black text, sharp corners (`border-radius: 0px` is directly observed in the stylesheet), with an active/hover state that inverts to solid black fill and border. This is the primary "Shop Now" / add-to-cart affordance.

**button-secondary** is inferred from the `.btn--secondary` rule set: white background, dark ink (`#282828`) border and text, inverting to solid dark on hover/active. Proposed for tertiary actions like "Learn More" or filter toggles.

**text-input** is a proposed pattern since no dedicated input selector was supplied. It borrows the hairline gray for resting border and the primary yellow for focus state, consistent with the brand's single confirmed accent color.

**nav-bar** uses the confirmed `--theme-header-height: 82px` custom property. Background and text colors are inferred as white-on-black-ink given the confirmed light canvas and dark button-hover ink; a hairline bottom border is proposed for separation from hero content.

**product-card** is a proposed layout for the Flyte Midi listing grid (seen repeated in page text: character-themed suitcases with price and compare-price). Card surface uses a near-white tone (`#fcfcfc`) with a subtle hairline border since no shadow values were present in evidence.

**hero** models the "THE ORIGINAL SCOOTER SUITCASE" banner area referenced in the page text, using the largest proposed display type against a soft surface background; exact hero markup/colors were not directly observed.

**footer** is inferred as a dark-ink block reversing text to white, matching the confirmed dark hover/active state color (`#282828`) reused here for footer background, since no footer-specific selector was supplied.

**badge** covers the "24% OFF" and "SOLD OUT" labels visible in the page text. Color is proposed using an observed red tone (`#d32d2d`) for urgency; pill shape is proposed, not confirmed.

**search** is a proposed light-surface input pattern for the header search icon/field referenced in page text ("Search"), reusing the hairline/surface-soft tokens for consistency with text-input.

**price-display** is a category-appropriate component modeling the visible "$105.99 / $139.99, 24% OFF" pattern from the product listing text: current price in ink, struck-through compare price in muted gray, and a mustard-yellow discount badge reusing the review-widget accent color.

## Responsive Behavior

This is a recommended breakpoint structure, not measured site behavior (no media queries were included in the supplied evidence):

| Breakpoint | Width       | Layout guidance                                  |
|------------|-------------|---------------------------------------------------|
| mobile     | < 480px     | Single-column product grid, stacked nav, collapsed search into icon-triggered overlay |
| tablet     | 480–959px   | 2-column product grid, condensed nav with hamburger menu |
| desktop    | 960–1279px  | 3-column product grid, full horizontal nav        |
| wide       | ≥ 1280px    | 3–4 column product grid, max-width content container |

Touch targets for buttons and nav items should be a minimum of 44px in height, aligning with the button skeleton `min-height:25px; max-height:55px` range observed in the Shopify accelerated-checkout CSS. Nav collapse to a hamburger/drawer pattern below tablet width is a proposed convention, not confirmed from this evidence set.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was gathered via static CSS/text extraction; no live rendering, computed layout, or DOM screenshots were available, so actual grid structure, hero composition, and breakpoints are not observed.
- Only one @font-face (`Nunito Sans`) is confirmed in use; other listed font names (GT Walsheim, Jost, Archivo, Antique Olive Nord D, Google Sans, Font Awesome families) could not be tied to a confirmed selector on this page and were excluded from typography tokens.
- Most typographic sizes (display-xl, display-md, title-md, body-sm, caption) are proposed conventions scaled around the one confirmed button-md value (15px/400); actual heading sizes were not present in the supplied CSS.
- Card, hero, footer, nav-bar, search, and badge components are inferred patterns built from generic palette values and general Shopify theme conventions; no component-specific selectors for these areas were included in the evidence.
- Rounded values beyond `none` (confirmed `border-radius: 0px`) are proposed scale conventions, not observed in source.
- Interaction states beyond button `:hover`/`:active` (confirmed) — including focus rings, transitions, and mobile menu behavior — are not observed and are marked proposed.
- Custom font licensing, hosting rights, and cross-device availability for "Nunito Sans" were not verified beyond the presence of a self-hosted woff2/woff source path.
- Color role assignments (e.g., which gray serves as "muted" vs. "hairline") are inferred from typical usage patterns in the supplied declarations, not confirmed via visual inspection.
