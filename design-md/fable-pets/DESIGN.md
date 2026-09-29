---
version: alpha
name: "Fable Pets"
source_url: "https://fablepets.com/"
captured_at: "2026-09-29T04:15:34.513798+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Fable Pets presents a modern, design-forward pet-gear catalog (crates, beds, leashes, toys) built on a Shopify storefront layered with an Okendo reviews widget. The observed palette centers on a deep navy ink (#030e28) paired with near-white and light-gray surfaces, giving copy a quiet, editorial tone consistent with the "premium pet brand" positioning quoted in customer testimonials. A cool blue (#2563ed) and its pastel cousin (#b0c7fa, used as the Okendo button background) suggest a primary/interactive accent family, while a cluster of soft pastels (mint #b2f9e9, sage #cfecb2, yellow #ffd303) likely map to category or badge accents ("Best Seller," "Wirecutter Pick") given the product-grid copy referencing multiple shop categories (Rest, Play, Walk, Eat, Cats). Two font families are declared beyond system/monospace stacks: Gelica (serif) and Moderat (sans-serif); Gelica is inferred as the display/headline face for its editorial serif character, and Moderat as the workhorse body/UI sans-serif, consistent with review-widget CSS inheriting a single body font. All spacing, radius, and component states below are proposed conventions for a clean, photography-led e-commerce layout, not measured DOM values; the 4px button radius is the one concrete measurement, drawn directly from the Okendo `--oke-button-borderRadius` token.

colors:
  primary: "#2563ed"
  ink: "#030e28"
  canvas: "#ffffff"
  body: "#515357"
  muted: "#7c7f85"
  hairline: "#e5e5e5"
  surface-soft: "#fafafa"
  surface-card: "#f7f7f7"
  on-primary: "#ffffff"
  accent-blue-soft: "#b0c7fa"
  accent-mint: "#b2f9e9"
  accent-sage: "#cfecb2"
  accent-yellow: "#ffd303"
  border-subtle: "#dedede"
  overlay-scrim: "#000e28"
typography:
  display-xl: {fontFamily: "Gelica, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Gelica, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Moderat, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Moderat, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Moderat, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Moderat, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Moderat, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.2px}
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
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    badge: "{components.badge}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.overlay-scrim}"
    titleTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    linkColor: "{colors.accent-blue-soft}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  bundle-card:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.display-md}"
    ctaButton: "{components.button-primary}"

## Components
**button-primary** is the primary "Add to Cart" / "Shop Now" action, using the deep-blue primary against a light text color; state changes (hover/active) are proposed, not observed, though the Okendo button tokens confirm a similar hover/active swap pattern exists elsewhere on the storefront. **button-secondary** is an outlined variant for lower-emphasis actions like "See Details," inheriting the ink color for both border and text. **text-input** covers newsletter and search fields, kept minimal with a hairline border and soft corner radius consistent with the 4px Okendo button radius token. **nav-bar** is a light, hairline-bordered header proposed to hold the "Shop / Sets / Our Story / Blog" navigation referenced in the footer text, with a persistent promo strip for the WELCOME10 code. **product-card** wraps individual PDP tiles (Crate, Puffin Game, Magic Link) with a soft card surface, title in the serif title style, and a badge slot for "Best Seller" / "Wirecutter Pick" labels. **hero** is the dark, full-bleed banner pattern implied by testimonial and lifestyle-photography copy, pairing the ink background with large serif display type. **footer** is a dark ink block mirroring the hero treatment, holding the multi-column link groups (Support, Company, Products) visible in the page text. **badge** is a small pill for merchandising callouts, proposed in the yellow accent to stand out against both light and dark card surfaces. **bundle-card**, the category-appropriate component, models the "Rest Set" / "Save on sets" bundle promotions using the sage accent as a differentiator from single-product cards.

## Responsive Behavior
Recommended (not measured) breakpoints: mobile ≤599px (single-column stack, full-width buttons, touch targets ≥44px), tablet 600–1023px (2-column product grid, collapsed nav into a hamburger/drawer), desktop ≥1024px (3–4 column product grid, persistent horizontal nav, cart drawer overlay). Hero and bundle-card sections are proposed to collapse to stacked text-over-image on mobile. This table is a design recommendation only; no actual responsive/mobile layout was observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This is a static, evidence-based interpretation from a supplied color list, font-family list, page text, and a partial CSS rule set (largely third-party Okendo review-widget and Shopify accelerated-checkout styles), not a full DOM/layout capture. Semantic color roles (primary, muted, hairline, surface-soft/card) are inferred from limited context clues (e.g., `.head_color`/`.sub_color` rules) and general palette position, not confirmed via computed styles on live components. Gelica and Moderat are listed as observed font-family names but their weights, exact usage (heading vs. body), licensing, and availability were not verified. All spacing, radius (beyond the confirmed 4px Okendo token), typography sizes, and component states (hover/focus/active/disabled) are proposed conventions, not measured. No interaction, animation, or actual mobile/responsive behavior was observed; the responsive table above is a recommendation only.
