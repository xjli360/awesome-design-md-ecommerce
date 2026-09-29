---
version: alpha
name: "Mothers Polish"
source_url: "https://mothers.com"
captured_at: "2026-09-29T04:16:00.104226+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation reads Mothers.com as a heritage automotive-care brand (est. 1974) built on a Shopify storefront layered with Bootstrap-derived utility classes. The observed palette is dominated by a strong red (#dc1831, reinforced by #ce1126, #ee1616, #f8353e) against near-black body text (#1f1f1f) and pure white canvas — a combination consistent with a garage/performance-product identity, though the exact brand-red role is inferred from frequency and contrast rather than a labeled brand token. Bootstrap system colors (#28a745, #dc3545, #17a2b8, #ffc107, #007bff) appear in the CSS and are treated here as functional/status colors rather than brand expression, since they follow standard Bootstrap button-state naming (.btn-success, .btn-info, .btn-warning).
  Typography combines system sans stacks (Arial, sans-serif) with loaded webfonts: Oswald and Muli/Open Sans for structured UI and body copy, plus a Typekit-served eurostile-condensed (italic, weight 800) whose presence suggests a condensed, motorsport-flavored display treatment for hero or promotional headlines. This role is inferred, not confirmed by a screenshot.
  The proposed system favors a light canvas, red primary actions, dark ink for readability, and soft gray surfaces for product-grid separation, echoing an automotive parts-catalog layout without asserting any unverified interaction or breakpoint behavior.

colors:
  primary: "#dc1831"
  ink: "#000000"
  body: "#1f1f1f"
  canvas: "#ffffff"
  muted: "#707070"
  hairline: "#e9e7e7"
  surface-soft: "#f7f8fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#ce1126"
  highlight-yellow: "#ffd658"
  success: "#28a745"
  danger: "#dc3545"
  info: "#17a2b8"
  link: "#007bff"
  dark: "#191919"
  border-strong: "#dee2e6"
typography:
  display-xl: {fontFamily: "eurostile-condensed, Arial, sans-serif", fontSize: 48px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Oswald, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Oswald, Arial, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Muli, Open Sans, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Oswald, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.border-strong}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.highlight-yellow}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  product-line-filter:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.md}"

## Components
**button-primary** anchors purchase actions ("Add to Cart") using the observed brand red on white text, matching the site's likely emphasis on conversion in a Shopify catalog. **button-secondary** is a proposed lower-emphasis variant using a bordered white surface for actions like "Learn More," since no distinct secondary color was confirmed in evidence. **text-input** models search and account fields with a neutral border and white background, inferred from generic Bootstrap form conventions present in the CSS. **nav-bar** proposes a white top bar with dark text and hairline divider, reflecting the multi-tier navigation labels seen in the page text (Product Line, Applications, How-To). **product-card** is a category-appropriate component for the dense product grid evidenced by repeated "Product No:" entries, pairing a card surface with title and price typography scales. **hero** proposes a dark, full-bleed band using the condensed display font for campaign messaging (e.g., "GET 20% OFF SITEWIDE"), though exact hero styling was not directly observed. **footer** reuses the dark surface with a yellow link accent, an inferred pairing meant to echo automotive signage without asserting a confirmed color rule. **badge** covers promotional or "New" product flags using the accent red on a pill shape. **search** and **product-line-filter** are proposed utility components supporting the "Explore Products" filtering UI referenced in the page text, using soft surface backgrounds to visually separate filter controls from the main canvas.

## Responsive Behavior
This is a recommended breakpoint structure, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <576px | single-column product grid; nav collapses to a hamburger/drawer pattern (proposed) |
| tablet | 576–991px | two-column product grid; filters may collapse into an accordion |
| desktop | 992–1439px | multi-column grid; full horizontal nav with dropdown mega-menu |
| wide | ≥1440px | max-width content container; additional whitespace, no new columns assumed |

Touch targets should be at minimum 44px in height for cart and filter controls (proposed). Navigation collapse thresholds and mega-menu behavior mirror the multi-level menu labels found in the page text but were not verified through direct interaction testing.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered screenshots, computed styles, or live interaction states were captured. Role assignments for `primary`, `ink`, `body`, and `muted` are inferred from frequency and typical semantic pairing, not from labeled design tokens. Bootstrap-style status colors (`success`, `danger`, `info`, `link`) follow standard framework class naming and may not represent intentional brand choices. Font role assignments (display vs. body) are inferred from common industry convention (condensed display faces for automotive branding); the eurostile-condensed face is confirmed only via a Typekit `@font-face` import, and licensing/availability for reuse outside Mothers.com is not verified. All spacing, rounding, and breakpoint values are proposed defaults, not measured from the live site. Mobile menu behavior, hover/focus states, and cart-drawer interactions referenced in the page text were not directly observed and are marked proposed throughout.
