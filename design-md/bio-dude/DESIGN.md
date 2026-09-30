---
version: alpha
name: "The Bio Dude"
source_url: "https://thebiodude.com"
captured_at: "2026-09-28T10:13:20.724829+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The Bio Dude's storefront runs on a stock Shopify/Bootstrap-derived CSS bundle (apps.css), so most of the 60 supplied hex values are generic UI-state colors (Bootstrap's default success/info/warning/danger greens, blues, oranges and reds used for alerts and buttons) rather than confirmed brand marks. Within that set, a small cluster reads as brand-specific: a deep forest green (#017749) and a saturated leaf green (#4bd20f) align with the "bioactive/living habitat" positioning, while a warm orange (#f17a06) and an alert red (#ff1c32) suit promotional callouts like the "Spend $75" shipping banner and clearance tags. The confirmed body typography is a sans-serif stack (Helvetica Neue, Helvetica, Arial) at 14px/1.43 with #333 ink on a white canvas — this is the only text styling actually declared in the supplied CSS; all heading sizes, display scale, and component sizing below are proposed and inferred to fit a plant/terrarium-forward pet-supply catalog. Serif families (Georgia, Baskerville, Times) appear only as fallback stacks and are not treated as an intentional display face. Rounded corners of 16px are the one observed radius (chat widget); other radii are proposed for consistency.

colors:
  primary: "#017749"
  ink: "#282727"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#f3f6f6"
  on-primary: "#ffffff"
  accent-leaf: "#4bd20f"
  accent-orange: "#f17a06"
  alert-red: "#ff1c32"
  link-blue: "#337ab7"
  state-success: "#5cb85c"
  state-danger: "#d9534f"
  state-info: "#5bc0de"
  state-warning: "#f0ad4e"
typography:
  display-xl: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: "0px"}
  title-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.42857143, letterSpacing: "0px"}
  body-sm: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "0px"}
  caption: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.3, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.2, letterSpacing: "0.2px"}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
  care-sheet-callout:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.accent-leaf}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** uses the deep green as the dominant call-to-action color (e.g. "Shop now" links) with white text, proposed for consistency with the brand's bioactive/green identity; hover/active states were not observed and are unspecified.

**button-secondary** is a low-emphasis outline/ghost pattern (white fill, hairline border, ink text) proposed for secondary actions like "Learn More" or filter toggles; no such button was directly observed in the supplied evidence.

**text-input** models a standard bordered field for search, login, and account forms; border color and radius are inferred from the generic Bootstrap hairline/gray tokens present in the CSS bundle, not from a confirmed input rule.

**nav-bar** is proposed as a white top bar holding the mega-menu of categories (Bioactive Soils, Kits, Live Animals, Flora, Lighting & Heating, etc.) implied by the page's extensive navigation text; exact height, sticky behavior, and dropdown styling are not confirmed.

**product-card** reflects the "Quick View" product tiles referenced in the excerpt (e.g. "Background Blend 6 quarts – $13.95"), using a soft card surface, hairline border, and a title/price typographic pairing; card shadow and hover-lift are proposed, not observed.

**hero** represents the homepage banner area ("Curated bioactive kits — Go bioactive") using a soft background tint and the largest inferred display type; actual hero imagery, overlay treatment, and copy placement were not measured.

**footer** is proposed as a dark, ink-colored band for account/contact/legal links, contrasting the mostly white body; this inverts the primary ink-on-white pattern and is a common convention rather than an observed rule.

**badge** covers promotional flags such as "CLEARANCE" or sale/free-shipping callouts, using the orange accent pill; the alert-red token is reserved for more urgent flags (e.g. stock warnings) and both are proposed mappings, not confirmed component styles.

**search** models the header search field using a soft gray fill to differentiate it from standard white text inputs, matching the light neutral tokens (#f5f5f5/#efefef) present in the palette; no dedicated search-bar CSS was supplied.

**care-sheet-callout** is a category-appropriate component for this reptile/amphibian retailer, styled as a card with a green accent rule to surface blog/"Care sheets, Tips and Tricks" content linked from the homepage; layout and accent placement are proposed.

## Responsive Behavior
Recommended, not measured, breakpoint table:

| Breakpoint | Width      | Notes (proposed) |
|-----------|------------|-------------------|
| mobile    | 0–599px    | Single-column product grid, collapsed hamburger nav, stacked hero copy over full-width image. |
| tablet    | 600–959px  | Two-column product grid, nav collapses into a toggled mega-menu drawer. |
| desktop   | 960–1279px | Full horizontal nav with mega-menu dropdowns, 3–4 column product grid. |
| wide      | 1280px+    | Max-width content container, 4+ column grid, larger hero display type. |

Touch targets should be a minimum of 44×44px for nav items, quick-view buttons, and cart controls. The large category mega-menu implied by the navigation text should collapse to an accordion or drawer pattern below the tablet breakpoint. This table is a design recommendation only; no live responsive CSS or JS breakpoints were captured in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from a static, partial CSS/text extraction and does not reflect a rendered or interactive view of the site. The majority of supplied hex values originate from a generic Bootstrap-style vendor stylesheet (apps.css) and represent UI alert/button states rather than confirmed brand colors; the green/orange/red brand mapping above is an inferred interpretation, not a verified brand palette. Only the body font stack (Helvetica Neue/Helvetica/Arial) and 14px base size are confirmed by the supplied CSS; all heading sizes, the display scale, letter-spacing, and font-weights are proposed. The 16px radius is the sole observed corner value (chat widget); all other radii are proposed. No hover, focus, active, or error states, no mobile/responsive layout, and no actual product-card, hero, or nav markup were observed—these are inferred from page text and generic e-commerce convention. No custom or licensed font usage is confirmed, and no typeface licensing was verified.
