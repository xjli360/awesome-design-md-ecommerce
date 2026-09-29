---
version: alpha
name: "Josh's Frogs"
source_url: "https://joshsfrogs.com"
captured_at: "2026-09-29T04:02:16.754755+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Josh's Frogs presents as a high-volume specialty e-commerce site for captive-bred
  amphibians, reptiles, arachnids, and their live-animal supply chain (feeders,
  bioactive substrates, terrariums). The observed palette is utilitarian and
  Tailwind-derived: a near-black heading ink (#111827), slate body/gray text
  (#374151, #6b7280), light hairline grays (#e5e7eb, #eeeeee), and a white canvas.
  A single strong brand green (#7ac144) drives the primary call-to-action button
  (".button-jf"), while a secondary blue (#2563eb) powers an alternate button
  variant. A wide band of saturated pastel hues (cyans, limes, ambers, pinks) is
  present in the palette and is inferred here as a category/pet-type tagging
  system, since the site text enumerates many pet categories (Frogs, Reptiles,
  Arachnids, Plants, Feeders, Habitat Kits, Terrariums, Bioactive). A vivid
  red-pink (#ff253a) is treated as an inferred clearance/sale accent given the
  "Clearance" navigation item. Typography is dominated by the system UI stack
  (system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial) for body copy;
  "niveau-grotesk" appears in the font list and is treated as a possible display
  typeface, though its actual usage context was not confirmed in the supplied
  selectors, so it is labeled inferred. Rounded corners are modest (4-12px range
  observed), fitting a functional, catalog-dense pet-supply storefront rather
  than a boutique aesthetic.

colors:
  primary: "#7ac144"
  secondary: "#2563eb"
  ink: "#111827"
  canvas: "#ffffff"
  body: "#374151"
  muted: "#6b7280"
  hairline: "#e5e7eb"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#0066cc"
  alert: "#ff253a"
  success-bg: "#d1fae5"
  warning-bg: "#fef3c7"
  error-bg: "#fee2e2"
  info-bg: "#dbeafe"
  category-cyan: "#6cd9f5"
  category-lime: "#83ed82"
  category-amber: "#f7d188"
  category-coral: "#f0ad84"
  category-pink: "#f298f4"
typography:
  display-xl: {fontFamily: "niveau-grotesk, system-ui, sans-serif", fontSize: 48px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif", fontSize: 36px, fontWeight: 800, lineHeight: 1.111, letterSpacing: 0px}
  title-md: {fontFamily: "system-ui, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0px}
  body-md: {fontFamily: "system-ui, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "system-ui, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.43, letterSpacing: 0px}
  caption: {fontFamily: "system-ui, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.43, letterSpacing: 0.05em}
  button-md: {fontFamily: "system-ui, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.5, letterSpacing: 0px}
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
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
    border: "1px solid transparent"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineBottom: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.md}"
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
    titleTypography: "{typography.title-md}"
    priceColor: "{colors.ink}"
  category-tile:
    backgroundColor: "{colors.category-cyan}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    typography: "{typography.title-md}"
  badge:
    backgroundColor: "{colors.category-lime}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.lg}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    linkColor: "{colors.link}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"

## Components

**button-primary** renders the brand green (#7ac144, matching the observed `.button-jf` rule) with white text and medium weight, used for primary catalog actions like "Add to Cart." Hover/active darkening is proposed and not confirmed in the supplied CSS.

**button-secondary** reuses the observed blue variant (`.button-jf.button-blue`, #2563eb) for secondary or alternate-path actions (e.g., "Learn More," AutoDelivery signup). Its hover state was observed darkening toward a navy not present in the supplied palette, so no new hex is introduced; the darkening behavior itself is treated as confirmed intent, not a specific color.

**text-input** is a proposed field style using the neutral hairline border and white canvas, sized for search and account forms; no explicit input CSS was supplied, so padding and radius are inferred from the general spacing/rounded scale.

**nav-bar** is inferred from the page's textual structure ("Search products… Cart Account Shop By Pet Shop By Category"), styled as a light bar with dark ink text and a bottom hairline; no header layout CSS was directly supplied.

**search** proposes a soft-gray input affordance sitting inside the nav bar, matching the "Search products Go" pattern in the extracted text; exact visual treatment is not confirmed.

**product-card** is a proposed catalog-grid unit (used heavily given the long best-seller/new-product lists in the text) with a white surface, hairline border, and title typography matching the `.match-header p` scale.

**category-tile** and **badge** are inferred components built from the wide pastel swatch set in the palette, mapped to the site's many pet/category groupings (Frogs, Reptiles, Arachnids, Plants, Feeders, Habitat Kits, Terrariums, Bioactive). No CSS selector confirms these swatches map to categories; this is a plausible but unverified interpretation.

**hero** proposes a dark value-proposition band (AutoDelivery, Live Arrival Guarantee, Low Shipping) using the ink color as background, since the page text lists exactly this kind of trio of trust statements near the top.

**footer** uses the same dark ink background with muted gray links, matching the extensive footer link list (Information, Partner Programs, Careers, social icons) found in the page text; link color reuses the observed blue-adjacent link hex (#0066cc).

## Responsive Behavior

This is a proposed breakpoint scheme, not measured from live site behavior:

| Breakpoint | Width      | Layout guidance                                  |
|-----------|------------|---------------------------------------------------|
| sm        | 0–639px    | Single-column product lists; nav collapses to a hamburger/menu icon; search bar full-width. |
| md        | 640–1023px | 2-column product/category grids; sticky top nav.  |
| lg        | 1024–1279px| 3–4 column product grids; persistent nav with category dropdowns. |
| xl        | 1280px+    | 4–5 column grids; wider hero and footer link columns. |

Touch targets should be at least 44x44px for cart/account/search icons. Category and pet-type navigation (Shop By Pet, Shop By Category) should collapse into an accordion or drawer below `md`. None of this is confirmed from captured layout CSS; it is a standard responsive recommendation for a catalog-heavy storefront.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, DOM structure, or interaction states (hover, focus, active, disabled) were directly observed beyond the few `:hover`/`:focus` rules supplied. Several palette hexes appearing in the CSS (e.g., the orange `rgba(251,146,60)` used in `.match-header`) could not be mapped to an exact hex in the supplied observed-palette array and were therefore omitted rather than approximated. The semantic role of the pastel color cluster (cyan/lime/amber/pink) as a category-tagging system is an inference based on the site's textual category list, not a confirmed selector-to-color mapping. The "niveau-grotesk" font family appears in the extracted font list but its actual selector usage, licensing, and availability were not verified; it may be a third-party/licensed font not safely redistributable. All font sizes and line heights not explicitly present in a supplied `declarations` string (e.g., display-xl, body-sm) are proposed values consistent with the scale, not measured. Mobile menu behavior, cart drawer design, and product-image treatment were not present in the supplied evidence and are therefore not described as components.
