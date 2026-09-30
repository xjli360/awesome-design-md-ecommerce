---
version: alpha
name: "Poppi"
source_url: "https://drinkpoppi.com"
captured_at: "2026-09-28T09:28:06.452244+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is built from decovostatic.com CSS (the production Next.js
  bundle for drinkpoppi.com) plus a third-party SmartCart widget stylesheet. The
  confirmed brand system centers on a hot pink primary (#ec008c) used as the fixed
  header background, paired with a bright yellow (#fff200) used as the on-primary
  text/icon color and CSS custom property `--color-secondary`. A lime-green
  (#cafe26) appears as a rounded marquee/announcement bar background, and a
  yellow-green (#e5fc0f) marks a small cart-count badge with near-black (#111111)
  text. Body copy and default ink render in a soft near-black (#222222) against a
  white (#ffffff) canvas. Two font roles are declared via CSS variables:
  `font-primary` (ITC Avant Garde Gothic, Helvetica Neue, Helvetica, Arial,
  sans-serif) for UI text and lowercase nav links, and `font-secondary` (Recoleta,
  Georgia, Times New Roman, serif) for all headings — a serif/display pairing
  against sans-serif body text, common in flavor-forward CPG branding.
  Neutral grays (#85888a, #f2f2f2, #f6f6f6) and a stray blue (#007aff, a Swiper
  library default, not necessarily brand) round out the supplied palette. Card
  radii, spacing, and most component states beyond the header/nav/marquee are
  inferred and clearly labeled as proposed rather than observed.

colors:
  primary: "#ec008c"
  ink: "#222222"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#85888a"
  hairline: "#f2f2f2"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#fff200"
  accent-lime: "#cafe26"
  accent-chartreuse: "#e5fc0f"
  accent-blue: "#007aff"
  deep-ink: "#111111"
  border-dark: "#333333"
typography:
  display-xl: {fontFamily: "Recoleta, Georgia, Times New Roman, serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Recoleta, Georgia, Times New Roman, serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Recoleta, Georgia, Times New Roman, serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "ITC Avant Garde Gothic, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: "24px", letterSpacing: "0px"}
  body-sm: {fontFamily: "ITC Avant Garde Gothic, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: "20px", letterSpacing: "0px"}
  caption: {fontFamily: "ITC Avant Garde Gothic, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "10px", fontWeight: 700, lineHeight: "16px", letterSpacing: "0.2px"}
  button-md: {fontFamily: "ITC Avant Garde Gothic, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: "24px", letterSpacing: "0px"}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "0 0 {rounded.lg} {rounded.lg}"
    padding: "{spacing.none} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-chartreuse}"
    textColor: "{colors.deep-ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  benefit-callout:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** uses the observed header background pink (`#ec008c`) with the observed on-primary yellow (`#fff200`) text, matching the confirmed nav-link color-on-primary pairing. Rounded is proposed as fully pill-shaped, consistent with a playful CPG tone, though no button radius was directly observed. Hover/active states are not observed and are proposed as a slight opacity or underline treatment mirroring the observed wavy-underline nav hover.

**button-secondary** flips to a white surface with pink text/border, an inferred outline variant for lower-emphasis actions (e.g., "learn more"). No secondary button markup was present in evidence; this is a proposed complement to button-primary.

**text-input** is proposed using the soft gray surface (`#f6f6f6`) and light hairline border, since no form input styling was captured in the supplied CSS rules. Sizing and radius follow the small-radius convention used elsewhere in the system.

**nav-bar** is grounded directly in `.header_bar` — fixed position, pink background, rounded bottom corners (24px, mapped to `rounded.lg`), and lowercase nav links in the secondary yellow. The drop-shadow filter using the yellow token is noted but not reproduced as a literal box-shadow here since exact blur/spread beyond the CSS `drop-shadow` value is not fully re-derivable as a portable shadow token.

**product-card** (flavor tile) is proposed as a white card with a hairline border and heading-weight title, intended to house a flavor name, can art, and short descriptor — inferred from the page's flavor list (Sour Apple, Cherry Cola, etc.) but no card markup/CSS was in the supplied evidence.

**hero** is proposed as a full-bleed canvas section using the large serif display type for campaign headlines like "taste the unexpected," inferred from page copy; no hero-specific CSS was supplied.

**footer** is proposed dark-on-light-inverted, using ink as background and canvas as text, to visually anchor the site's utility links (shop, story, careers, legal) observed in the page text; no footer CSS rules were supplied, so styling is inferred from general layout convention.

**badge** is grounded in `.header_cartCount`, reproducing its precise chartreuse background, near-black text, pill radius, and bold caption typography exactly as observed.

**search** is proposed as a pill-shaped soft-surface field for a flavor/product search affordance; not present in supplied evidence, included as a category-appropriate utility component.

**benefit-callout** is the category-specific component: a lime-green inline tag intended to surface functional-beverage claims (e.g., "prebiotic," "gut health," "5g sugar") referenced in the page's marketing copy. Its color is drawn from the observed marquee background; the component pattern itself is proposed, not observed as literal markup.

## Responsive Behavior

Proposed breakpoints (not measured from live responsive behavior):

| Breakpoint | Width      | Notes |
|-----------|------------|-------|
| Mobile    | 0–599px    | Single-column stacking; hamburger (`.header_hamburger`, observed but `display:none` at the captured breakpoint) likely toggles at this range. |
| Tablet    | 600–1023px | Two-column product/flavor grids proposed. |
| Desktop   | 1024px+    | Full nav links visible inline, matching `.header_navLink` styling captured in evidence. |

Touch targets should be a minimum of 44px per side for buttons and nav icons, aligning with the observed `--swiper-navigation-size:44px` variable. Collapse of the horizontal nav into the hamburger menu is inferred from the presence of `.header_hamburger__MLpR5` in CSS, but the exact trigger breakpoint was not present in the supplied rules.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS/text extraction across two sources (a Next.js production bundle and a third-party SmartCart widget) and does not reflect live rendering, JavaScript-driven states, or verified responsive breakpoints. Semantic role assignment (e.g., which grays serve as "muted" vs. "hairline") is inferred from typical usage patterns, not confirmed via computed styles. Font sizes for display/title/body-sm/hero levels are proposed defaults, not all directly observed in the supplied CSS (only nav-link 16px/24px and cart-count 10px/16px were explicit). Hover, focus, active, disabled, and error states were not observed and are proposed conventions only. Mobile menu behavior, product grid layout, and footer structure were not present in the supplied evidence and are inferred from page text alone. Availability and licensing of "ITC Avant Garde Gothic" and "Recoleta" as web fonts were not verified; fallback stacks are used as declared in the CSS.
