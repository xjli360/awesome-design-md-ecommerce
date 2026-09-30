---
version: alpha
name: "Virtue Drums"
source_url: "https://www.virtuedrums.com"
captured_at: "2026-09-28T09:14:55.324444+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Evidence from the VIRTUE Drums storefront (built on an EditMySite/Weebly-family
  platform) exposes a neutral, high-contrast palette dominated by near-black
  (#000000, #1b1b1b, #2b333f) and white (#ffffff, #f8f8f8, #f1f1f1), with a
  desaturated slate-blue (#73859f) and a single saturated accent, #006aff,
  appearing alongside a warning red (#d92b2b). No brand color documentation was
  supplied, so role assignments below are inferred: #2b333f is treated as the
  primary/header tone because it recurs as a dark structural color distinct from
  pure black; #006aff is treated as the interactive accent (links, focus states)
  since bright saturated blue is atypical for body chrome and typical for
  actionable elements; #d92b2b is reserved for destructive/alert use only. Body
  copy defaults to the observed Inter with Arial/Helvetica/sans-serif fallbacks,
  consistent with a workmanlike, craftsman-shop tone appropriate to a
  handcrafted-drum retailer. Layout, spacing, and component geometry are not
  confirmed from static CSS and are proposed as sensible defaults for a small
  specialty retail/repair site, not claimed observations.

colors:
  primary: "#2b333f"
  ink: "#1b1b1b"
  canvas: "#ffffff"
  body: "#000000cc"
  muted: "#6b7280"
  hairline: "#e6e6e6"
  surface-soft: "#f8f8f8"
  surface-card: "#f1f1f1"
  on-primary: "#ffffff"
  accent: "#006aff"
  danger: "#d92b2b"
  border: "#cccccc"
  slate: "#73859f"
  overlay-dark: "#000000b3"
typography:
  display-xl: {fontFamily: "Inter, Arial, Helvetica, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Inter, Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Inter, Arial, Helvetica, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Inter, Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Inter, Arial, Helvetica, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.2px}
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.lg}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xl} {spacing.lg}"
    typography: "{typography.body-sm}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  repair-service-tile:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.slate}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"

## Components
**button-primary** is proposed as the dark slate-on-white call-to-action pairing seen implicitly in the palette's contrast structure; used for primary actions like "Shop Now" or "Book Repair." **button-secondary** is an outlined variant for lower-emphasis actions, sharing the primary ink color for border and text. **text-input** assumes a light canvas field with a light gray border, typical of form fields for contact or repair-intake forms; focus/error states are not observed and are proposed only. **nav-bar** is inferred as a white header with a hairline bottom border, holding logo, category links, and cart/search entry points; sticky/scroll behavior is not confirmed. **product-card** represents a drum or hardware listing tile with a light card surface and hairline border, proposed for the shop grid; hover elevation is not observed. **hero** uses the dark primary tone as a full-bleed banner background suited to showcasing handcrafted drum photography, with white display type; this is a proposed pattern, not a captured screenshot. **footer** mirrors the near-black ink tone with white text for site-wide links (hours, location, contact), consistent with the Jackson, Michigan storefront context in the page text. **badge** applies the single observed saturated accent (#006aff) for small status labels such as "In Stock" or "New," reserving it as the sole bright-color signal against the otherwise neutral palette. **search** is a compact light-gray affordance proposed for product lookup, distinct from the darker nav-bar. **repair-service-tile** is a category-appropriate addition for the repair-service offering explicitly mentioned in the source text, using the slate-blue (#73859f) as a secondary accent to differentiate service content from retail product content.

## Responsive Behavior
Recommended, not measured: `sm` ≤480px (single-column stack, hamburger nav, full-width buttons), `md` 481–768px (two-column product grid, condensed nav), `lg` 769–1200px (three/four-column grid, full nav bar), `xl` >1200px (max-width container, generous section spacing using {spacing.section}). Touch targets should be at least 44px tall for repair-booking and cart actions; nav collapses to a drawer or accordion below `md`. These breakpoints are proposed defaults for a small e-commerce/service site and are not derived from observed media queries.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
Evidence was limited to static CSS from a shared platform CSS bundle (largely cookie-consent dialog styling) plus a page title and text excerpt; no product grid, hero, or nav markup/CSS was directly captured, so component layouts above are proposed patterns rather than observed structure. Color-to-role mapping (primary, accent, danger, etc.) is inferred from value characteristics, not from confirmed usage in brand-specific selectors. Font sizes, weights, and the full type scale are proposed, not measured, apart from the general use of Inter/Arial/Helvetica/sans-serif as observed font families. No interaction states (hover, focus, active, disabled) or mobile/responsive behavior were observed. Custom font licensing and self-hosting status for Inter were not verified. Spacing and radius scales are conventional proposals, not extracted token values.
