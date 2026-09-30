---
version: alpha
name: "Battle Born Batteries"
source_url: "https://battlebornbatteries.com"
captured_at: "2026-09-28T10:19:14.716670+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Battle Born Batteries is a Shopify-built storefront for LiFePO4 lithium
  batteries and power-system components, serving RV, marine, trucking, and
  off-grid customers. The observed palette centers on a deep navy-to-blue
  family (#081d4d, #02267e, #005695, #013c82) suited to a technical,
  trustworthy "American-engineered" positioning, paired with near-black text
  (#151515), mid-gray body copy (#4f5055), and light neutral surfaces
  (#f4f4f6, #ededf3, #f2f2f2) for card and section backgrounds. Accent reds
  (#d90400, #ffeeed) appear tied to sale pricing and "Best Seller" badges,
  while a saturated green (#39b54a) is inferred as an availability/success
  signal common to commerce templates of this kind. Only Poppins was observed
  in the font evidence, so all typographic roles are mapped to Poppins with
  system sans-serif fallback; weight and size values beyond what CSS exposed
  (e.g. checkbox sizing, badge padding) are proposed, not measured. The
  interpretation favors a clean, spec-driven commerce layout: strong
  navy/blue CTAs, generous white space, gray-bordered product cards, and
  compact badges for pricing and stock callouts, reflecting the technical,
  catalog-heavy nature of the product line without asserting any unverified
  layout or interaction detail.

colors:
  primary: "#005695"
  ink: "#151515"
  canvas: "#ffffff"
  body: "#4f5055"
  muted: "#888b95"
  hairline: "#dedede"
  surface-soft: "#f4f4f6"
  surface-card: "#ededf3"
  on-primary: "#ffffff"
  accent-sale: "#d90400"
  accent-sale-soft: "#ffeeed"
  accent-success: "#39b54a"
  deep-navy: "#081d4d"
  border-subtle: "#c9cad4"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Poppins, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Poppins, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Poppins, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Poppins, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-subtle}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    salePriceColor: "{colors.accent-sale}"
  hero:
    backgroundColor: "{colors.deep-navy}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.deep-navy}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-sale-soft}"
    textColor: "{colors.accent-sale}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-callout:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-subtle}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the observed blue (#005695) as the primary interactive color, inferred from the theme's `--color-primary-hover` and Shopify payment-button variable patterns; text is white for contrast. This is the proposed treatment for "Shop Best Sellers" and add-to-cart actions.

**button-secondary** is an outlined variant sharing the primary blue for border and text on a transparent background, proposed for lower-emphasis actions like "Explore Resources" or "Find a Dealer" where a filled button would compete with a nearby primary CTA.

**text-input** is proposed for search and account/login fields, using a light border (#c9cad4) and white background consistent with the neutral, uncluttered surfaces implied by the light gray tokens in the palette; no live form styling was captured.

**nav-bar** reflects the multi-level "Shop / Solar / Components / Accessories / Learn / Support" mega-menu structure named in the page text, styled with a white background and hairline underline (#dedede); dropdown/mega-menu visual treatment itself was not observed and is inferred from menu-drawer CSS variable names.

**product-card** is grounded in the `.product-grid__card` rules, which define flex layout, gap, and padding tokens; card background, border, and sale-price coloring are inferred, mapping the observed red (#d90400) to strikethrough/sale pricing seen in "Sale price / Regular price" text pairs.

**hero** is proposed for the homepage banner ("400,000+ Batteries Deployed... More Than a Battery"), using the deep navy (#081d4d) as a confident, technical backdrop with white display type; exact hero imagery and layout were not present in the evidence.

**footer** shares the deep-navy treatment for brand consistency across dark sections, a common commerce pattern; actual footer content, columns, and link styling were not in the supplied CSS and are inferred.

**badge** models the "Best Seller" label and sale callouts using the soft red tint (#ffeeed) with red text (#d90400), a pill shape being a proposed default since no explicit badge radius was captured beyond generic `--badge-*-padding` tokens.

**search** is proposed as a light, low-contrast field styled from the light-gray surface tokens (#f4f4f6), reflecting the "Search" entry point named in the header but without observed input styling.

**spec-callout** is a category-specific component for battery/electrical specs (Ah rating, voltage, chemistry, warranty) shown in cards like "100Ah 12V LiFePO4 Deep Cycle Battery," using the light structured surface (#ededf3) and a bordered card to visually separate technical specifications from marketing copy; this pattern is proposed to suit a spec-heavy power/electrical catalog.

## Responsive Behavior

Recommended breakpoints (not measured from the live site):

| Range        | Width           | Notes (proposed)                                  |
|--------------|-----------------|----------------------------------------------------|
| Mobile       | up to 599px     | Single-column product grid, collapsed nav drawer   |
| Tablet       | 600px – 989px   | 2-column product grid, condensed mega-menu         |
| Desktop      | 990px – 1279px  | 3–4 column product grid, full horizontal nav       |
| Wide         | 1280px+         | Up to 5-column zoom-out grid variant               |

Touch targets should target a minimum 40–44px height (aligned with the observed `min-height:40px` on payment buttons). Mega-menu items are recommended to collapse into an accordion-style drawer below tablet width, consistent with the `--menu-drawer-animation-index` variables present in the CSS. This table is a design recommendation only, not an observation of actual responsive behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction; no rendered screenshots, computed layout, or interaction states (hover, focus, active, disabled) were observed beyond the few pseudo-class rules supplied.
- Semantic color roles (e.g., which blue is "primary" vs. a secondary brand color, green as success vs. decorative) are inferred from variable naming conventions and general e-commerce patterns, not confirmed brand documentation.
- Typography sizes, weights, and letter-spacing for all roles beyond "Poppins" as a family are proposed values; no font-size or font-weight declarations were present in the supplied CSS rules.
- Rounded and spacing scales are proposed defaults aligned to common Shopify theme conventions; only a few explicit tokens (e.g., `--checkbox-border-radius: 5px`, `--product-grid-gap: 16px`) were directly observed.
- Mobile menu drawer, cart drawer, and quick-view modal visual treatments were referenced by class/selector names but their actual appearance was not captured.
- Custom font licensing/self-hosting for Poppins was not verified; it is treated as a Google Fonts-style family with generic fallback only.
