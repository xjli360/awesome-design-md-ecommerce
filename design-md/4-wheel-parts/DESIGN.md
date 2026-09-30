---
version: alpha
name: "4 Wheel Parts"
source_url: "https://4wheelparts.com"
captured_at: "2026-09-28T04:59:19.770065+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  4 Wheel Parts' site CSS exposes three declared brand variables: --primary (#F50028, a saturated red), --secondary (#FAE703, a bright safety-yellow), and --tertiary (#0058B3, a mid blue), layered over a large neutral gray-scale system (from #111827 through #f3f4f6) used for text, borders, and surfaces. The confirmed heading font is Barlow (h1 rule: font-family Barlow, sans-serif, 700 weight, 1.75rem), a condensed-leaning grotesque suited to bold automotive/off-road messaging. Roboto and system sans-serif stacks appear in the font list and are treated here as the inferred body font family, since no body-text rule was supplied. Button variables show a clear pattern: primary actions use --primary with white text, "add to cart" actions use --secondary with black text (inverting to black background with white text on hover), and default/secondary buttons use a neutral gray (#6b7280). This palette is interpreted as a utilitarian, high-contrast industrial catalog design: red for primary calls-to-action and urgency (sales, price match), yellow for transactional/commerce actions (cart, pricing), blue as a supporting link/accent tone, and grays for the dense navigation and vehicle-fitment tooling implied by the page text (Year/Make/Model selectors, store locator). All roles beyond the three CSS variables and the h1 rule are inferred, not measured.

colors:
  primary: "#F50028"
  secondary: "#FAE703"
  tertiary: "#0058B3"
  ink: "#111827"
  canvas: "#ffffff"
  body: "#374151"
  muted: "#6b7280"
  hairline: "#e5e7eb"
  surface-soft: "#f3f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-secondary: "#000000"
  accent-blue: "#1979c2"
  surface-dark: "#0f172a"
  border-strong: "#d1d5db"
  disabled: "#d2d2d2"
typography:
  display-xl: {fontFamily: "Barlow, sans-serif", fontSize: 48px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Barlow, sans-serif", fontSize: 28px, fontWeight: 700, lineHeight: 1.0, letterSpacing: 0px}
  title-md: {fontFamily: "Barlow, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Roboto, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Roboto, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Roboto, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.0, letterSpacing: 0.5px}
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
    borderColor: "{colors.primary}"
    hoverBackgroundColor: "{colors.primary}"
    hoverTextColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-cart:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    hoverBackgroundColor: "{colors.ink}"
    hoverTextColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
    hoverShadow: "proposed subtle elevation on image zoom"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.tertiary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.border-strong}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  vehicle-fit-selector:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border-strong}"
    accentColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** carries the red --primary token as background with white text, matching the observed `.pagebuilder-button-primary` rule, and is proposed for the highest-priority actions like "Shop Now" and checkout CTAs.

**button-secondary** is an outlined inversion of the primary button, using red text/border on transparent background, filling solid on hover — a proposed pattern consistent with `.action.secondary,.btn-secondary` variable definitions in the CSS.

**button-cart** maps directly to the observed `.btn-tocart` rule: yellow (--secondary) background with black text, inverting to black background/white text on hover, reserved specifically for add-to-cart actions.

**text-input** is a proposed form-field pattern using the light hairline gray for borders and near-black ink for typed text, sized for the vehicle/search fields implied in the page content (Year/Make/Model, email/password sign-in).

**nav-bar** is inferred from the presence of "Shop By Category," "Shop By Brand," and account/cart affordances in the extracted text; a white bar with dark text and red accent hover states is proposed, though no header layout was directly measured.

**product-card** is proposed for the catalog grid implied by "Add to Cart," SKU, and price text; it reuses the observed group-hover image-scale behavior (`.group:hover .product-item .product-image-photo`) as a subtle zoom-on-hover interaction.

**hero** is proposed as a full-bleed dark section (using the near-black background values seen in multiple `[data-pb-style]` rules) to host the "Let Us Build the Package" promotional banner referenced in the page text.

**footer** groups Company/Support/Sales links against a dark surface, echoing the black-background utility blocks found in the CSS and the extensive footer link list in the page text (About Us, Careers, Track Order, etc.).

**badge** is a small yellow pill, proposed for stock/promo labeling (e.g., price-match or sale callouts referenced in the hero copy), not directly observed as a component but consistent with --secondary usage.

**search** is a proposed compact input+icon pattern for the header search box implied by the "Search" text in the extraction.

**vehicle-fit-selector** is the category-specific component for 4 Wheel Parts' Year/Make/Model vehicle-fitment tool, directly evidenced by the long list of vehicle years and "Select Vehicle / Vehicle Make / Vehicle Model" strings; styled with a soft gray surface and red accent to emphasize its role as a primary shopping utility.

## Responsive Behavior
This is a recommended breakpoint strategy, not a measured observation of the live site.

| Breakpoint | Width      | Behavior (proposed) |
|------------|-----------|----------------------|
| sm         | ≤ 640px   | Single-column stack; nav collapses to hamburger + slide-out; vehicle selector becomes a full-width modal/sheet. |
| md         | 641–1024px| Two-column product grids; sticky condensed header; vehicle selector as an inline bar. |
| lg         | 1025–1440px| Standard multi-column catalog grid (3–4 up); full nav with mega-menu categories. |
| xl         | ≥ 1441px  | Wider gutters, 4–5 up product grids, larger hero imagery. |

Touch targets should be at least 44×44px for cart, quantity, and store-locator controls. Primary/cart buttons should retain full-width sizing on mobile. All breakpoint values and collapse behaviors are proposed defaults, not verified against rendered markup.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is generated from static CSS/text extraction only; no live rendering, computed layout, or DOM interaction was observed. Only three color variables (--primary, --secondary, --tertiary) and one heading rule (h1 font-family/size/weight) are directly confirmed; all other color-role assignments (ink, body, muted, hairline, surfaces) are inferred by matching common gray-scale conventions to the supplied hex list and may not reflect actual usage. Border-radius values were not present in the supplied CSS and are proposed placeholders. Spacing scale beyond the observed `.75rem`/`.375rem` button paddings is proposed. Body font-family (Roboto/Arial) is inferred from the global font-family list, not from a rule explicitly targeting body text. No mobile navigation, modal, or hover interaction was observed beyond the two CSS hover rules cited (button hover and product-image group-hover scale). Font licensing/self-hosting availability for Barlow and Roboto was not verified in this extraction and should be confirmed before implementation.
