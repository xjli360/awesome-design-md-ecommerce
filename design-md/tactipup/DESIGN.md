---
version: alpha
name: "Tactipup"
source_url: "https://tactipup.com"
captured_at: "2026-09-28T10:33:58.656593+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Tactipup's storefront evidence points to a utilitarian, high-contrast retail
  system built on Shopify's Dawn-derived theme conventions. The measured
  palette centers on pure black (#000000) and white (#ffffff), consistent
  with the dark top bar and light content canvas. A teal (#108474) appears
  in judge.me review-widget CSS variables (star color, write-review button,
  reviewer name) and is treated here as an inferred accent/primary color for
  interactive and trust-signal elements, since no other CSS-confirmed brand
  hue was observed at comparable prominence. A warm gold (#eebe13) and pale
  yellow (#fddc65) appear in the announcement-bar message header and are
  proposed as a secondary "sale/alert" accent family, fitting a tactical/
  outdoor gear brand. Neutral grays (#7a7a7a, #dbdbdb, #eeeeee, #f5f5f5)
  supply muted text, hairlines, and soft surfaces. A muted red (#ae3333) is
  reserved for destructive/sale-tag use.

  Typography draws on the observed font stack of Avenir, Helvetica Neue,
  Arial and sans-serif for body and display text, with Roboto Condensed
  (confirmed at 10px/400 in the top bar) repurposed for compact UI labels,
  captions, and buttons to echo the brand's rugged, condensed-caps
  tactical styling. Sizes beyond the confirmed 10px caption are proposed.

colors:
  primary: "#108474"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#7a7a7a"
  hairline: "#dbdbdb"
  surface-soft: "#f5f5f5"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent-gold: "#eebe13"
  accent-gold-soft: "#fddc65"
  danger: "#ae3333"
  border-dark: "#363636"
  overlay-dark: "#00000080"
typography:
  display-xl: {fontFamily: "Avenir, Helvetica Neue, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Avenir, Helvetica Neue, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Avenir, Helvetica Neue, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Avenir, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Avenir, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Roboto Condensed, sans-serif", fontSize: 10px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  button-md: {fontFamily: "Roboto Condensed, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "#c3c3c3"
    hoverTextColor: "{colors.canvas}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.base}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    accentColor: "{colors.accent-gold}"
    titleTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "#c3c3c3"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  personalization-panel:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    accentColor: "{colors.accent-gold-soft}"
    labelTypography: "{typography.caption}"
    inputTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the inferred teal accent (#108474) sourced from the judge.me review-widget variables, repurposed as the storefront's primary call-to-action color (e.g., "Add to Cart," "Sign Up"). Proposed hover/active/disabled states are not confirmed in the evidence.

**button-secondary** is an outlined black button for lower-emphasis actions ("View All," "Learn More"), consistent with the site's black/white contrast base. Hover fill-in behavior is proposed, not observed.

**text-input** reflects a plain white field with a light gray hairline border, matching the neutral gray family in the palette; used for the newsletter email field and search. Focus-state styling is proposed.

**nav-bar** models the confirmed dark top bar (#000000 background, #c3c3c3 link color, white on hover) plus a Roboto Condensed 10px caption typographic treatment taken directly from CSS. The main product-menu bar below it is inferred to share this dark treatment given the single-page evidence sample.

**product-card** is a proposed white card with a subtle hairline border for the featured-products grid (collars, leashes, harnesses), sized to show title, review count, and sale/strike-through pricing as seen in the page text excerpt.

**hero** proposes a full-bleed black section with white display type and a gold accent rule or badge, echoing the brand's "Over-Built," "Military Grade" messaging tone. Exact hero layout and imagery were not present in the CSS evidence.

**footer** mirrors the nav-bar's dark/light-gray link treatment for the "For Customers" and "Resources" columns and newsletter signup, based on the shared #000000/#c3c3c3 pairing found in the top-bar rules.

**badge** uses the muted red (#ae3333) for "Sale" or "Sold Out" tags referenced in the page text; no CSS rule for this component was directly observed, so color assignment is inferred by proximity to typical e-commerce sale-tag conventions.

**search** is a proposed pill-shaped light-gray field for the header search icon/expand pattern common to Shopify themes; no direct search-input CSS was supplied.

**personalization-panel** is a category-specific proposed component for collar/leash text-embroidery selection (name, phone number, color, width), styled with the light gray surface-card background and gold-soft accent to highlight customization steps described in the FAQ text.

## Responsive Behavior

The following breakpoints are a **recommendation only**; no responsive CSS or viewport behavior was present in the supplied evidence.

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | 0–599px | Single-column product grid, collapsed hamburger nav, sticky bottom cart bar |
| Tablet | 600–989px | 2-column product grid, condensed top bar retained |
| Desktop | 990px+ | Full horizontal nav with mega-menu categories (Collars, Leashes & Harnesses, Accessories, Applications) |

Touch targets should be a minimum 44px height for buttons and nav links on mobile. Mega-menu navigation is expected to collapse into an accordion-style disclosure below 990px, matching the `.disclosure__toggle` class name observed in CSS, though its collapsed visual behavior itself was not measured.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- All CSS was extracted statically; no rendered layout, hover, focus, or animation states were observed, only rule declarations.
- The primary accent color (#108474) is sourced from judge.me review-widget variables, not a confirmed site-wide brand token; its promotion to "primary" is an inferred semantic mapping.
- Font-role assignments (display, body, caption/button) are inferred from the observed font-family stack and one confirmed selector (top bar, Roboto Condensed 10px); no confirmed heading or body-copy font-size/weight rules were supplied.
- All spacing and rounded-corner scales are proposed defaults, not derived from measured CSS box-model values.
- Social/payment brand colors present in the palette (e.g., #1da1f1, #4266b2, #e50122, #f14336, #007ace) were excluded from the design tokens as they likely represent third-party icon sets (social/payment), not Tactipup brand colors.
- Mobile menu collapse behavior, cart drawer, and product-page layout were not present in the supplied evidence and are marked proposed.
- Custom font licensing/availability (Avenir, Avenir Next) was not verified; system fallbacks (Helvetica Neue, Arial, sans-serif) should be assumed for implementation.
