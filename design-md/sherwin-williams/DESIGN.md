---
version: alpha
name: "Sherwin-Williams"
source_url: "https://sherwin-williams.com"
captured_at: "2026-09-28T10:14:57.301584+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is built from static CSS and markup evidence for the
  Sherwin-Williams storefront, a paint, stain and coatings retailer serving
  homeowners, professionals and industrial buyers. The evidence shows a
  neutral, utilitarian UI system: a white canvas, dark near-black text
  (#2f2f30/#333333), light gray hairlines and surface fills, and a cluster of
  blues (#0069af, #0067b1, #336699, #33bbff) used inconsistently across
  components, suggesting a primary brand blue with lighter link/accent
  variants. Body copy relies on the system-font stack (system-ui, Segoe UI,
  Roboto, Arial) with Arial/Helvetica explicitly set for mega-menu text and a
  condensed "Frutiger Neue Condensed" family reserved for compact header
  labels — both treated here as observed. "Playfair Display" appears in the
  font list and is proposed here as a serif display option for hero/marketing
  headlines, an inferred editorial role not confirmed by any captured
  selector. Icon-only families (Phosphor, icomoon, tagicons, SW Dropcloth
  variants) are excluded from text typography. Given the product category —
  color selection is core to the business — this spec adds a proposed
  color-swatch component so palette/product browsing patterns have a defined
  target, though no swatch-grid CSS was captured directly.

colors:
  primary: "#0069af"
  ink: "#2f2f30"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#cccccc"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-link: "#33bbff"
  navy-deep: "#071c51"
  warm-sand: "#eeefea"
  neutral-border: "#e5e7eb"
typography:
  display-xl: {fontFamily: "Playfair Display, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Playfair Display, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Frutiger Neue Condensed, Arial, Helvetica, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 11px, fontWeight: 700, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.25px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.neutral-border}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.warm-sand}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    resultBackground: "{colors.canvas}"
    categoryChipBackground: "#eaeaea"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-picker:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.neutral-border}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs}"

## Components
**button-primary** renders the primary brand blue with white text for key calls to action such as "Shop Products & Color" or "Find A Store"; hover/active states are not observed and are proposed as a slightly darkened fill. **button-secondary** is an outlined variant for lower-priority actions, using the same blue for border and label on a white ground. **text-input** covers search and form fields, using the light hairline gray for borders and standard body typography, consistent with the captured `.cmp-header__search-container` styling. **nav-bar** reflects the extensive mega-menu structure evidenced in the page text (Shop, Explore Color, Get Inspired, Professional, Industrial); it uses the condensed header font for compact label density and a white background with a hairline bottom border, proposed since no explicit nav background color was captured. **product-card** is proposed for paint/product and color-family tiles, using a soft border and generous internal padding suited to image-forward merchandising. **hero** applies the warm off-white (#eeefea) surface tone observed in the palette as a banner background with large display type, appropriate for seasonal or campaign promotion; the serif display font is inferred as an editorial accent, not confirmed against any hero-specific selector. **footer** uses the deep navy (#071c51) found in the palette as an inferred footer/utility background with white text, a common retail pattern though not directly observed in a footer selector. **badge** supports small status or category labels (e.g., "NEW HOURS") using the neutral gray surface and muted text. **search** is modeled directly on the captured `#autoSuggest_Result_div` styles: white dropdown, soft shadow, gray category chips (#eaeaea), and dashed-border "see all" affordance. **color-swatch-picker** is a category-specific, fully proposed component representing the paint-color browsing experience (color families, collections, "Top 50 Colors") implied by the navigation text but not backed by captured swatch-grid CSS.

## Responsive Behavior
Recommended, not measured, breakpoints:

| Range | Target | Notes |
|---|---|---|
| <640px | Mobile | Nav collapses to a hamburger/menu drawer; search and color tools stack full-width. |
| 640–1024px | Tablet | Mega-menu likely condenses to grouped accordions; product/color grids reduce to 2 columns. |
| >1024px | Desktop | Full mega-menu with multi-column dropdowns, as implied by the deep category listing (Rooms, Exterior, Collections, etc.). |

Touch targets should be at least 44px in the mobile drawer; the mega-menu's many nested links suggest an accordion collapse pattern on small screens, but this interaction is inferred from content volume, not observed markup or breakpoints.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This spec is derived from static CSS/text extraction only; no rendered layout, JavaScript-driven states, or responsive behavior was observed. Hover, focus, active, and disabled states for buttons and inputs are proposed, not measured. The role of several near-duplicate blues (#0069af, #0067b1, #0068b3, #336699, #005896) is ambiguous — one was selected as `primary` and others omitted; the true design-token mapping may differ. The navy (#071c51) assigned to `footer` and the sand tone (#eeefea) assigned to `hero` are inferred surface pairings, not confirmed against footer/hero-specific selectors. "Playfair Display" is listed in the font stack but its actual usage context (headlines vs. incidental) is unverified. Custom families (SW Dropcloth variants, tagicons, icomoon, Phosphor) appear to be icon or proprietary display fonts; their licensing and web-availability were not verified and they are excluded from text typography roles. Mobile menu collapse, swatch-grid layout, and product-card imagery were not present in the supplied evidence and are therefore proposed patterns only.
