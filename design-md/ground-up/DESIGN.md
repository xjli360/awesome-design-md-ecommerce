---
version: alpha
name: "Ground Up"
source_url: "https://grounduppdx.com"
captured_at: "2026-09-28T04:32:34.193812+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Ground Up's storefront CSS shows a bright, high-contrast palette anchored
  by a signature yellow (#fdd700) — used as the review-star/rating icon
  color in the site's own custom property — against a stark white/black
  foundation (#ffffff, #000000, #222222 body text). Secondary accents
  surface through Shopify's accelerated-checkout component: a cyan-blue
  (#1990c6, hover #136f99) button and a neutral skeleton-loading gray
  (#dedede). A small set of deeper tones (#4e3c98 purple, #73033b berry,
  #cb1f2b red) appear in the wider palette and are treated here as
  inferred secondary/accent colors for badges or seasonal flavor cues,
  since their exact page role is not confirmed by the supplied CSS.
  Typography is dominated by system sans stacks (Helvetica Neue, Helvetica,
  Arial) for body copy, with Figtree present in the font manifest and
  proposed here as the heading/accent family given the theme's uppercase,
  letter-spaced button and section-heading rules. A decorative script
  family (Grove Script Medium) also appears and is treated as an
  unverified, possibly licensed display/logo font, not used in core UI
  typography. Buttons observed with 0px radius, uppercase 14px labels,
  and 1px letter-spacing inform the button-md and rounded tokens below.

colors:
  primary: "#fdd700"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#888888"
  hairline: "#dddddd"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#000000"
  accent-blue: "#1990c6"
  accent-blue-hover: "#136f99"
  accent-purple: "#4e3c98"
  accent-berry: "#73033b"
  success: "#01c753"
  alert: "#cb1f2b"
  skeleton: "#dedede"
typography:
  display-xl: {fontFamily: "Figtree, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Figtree, sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Figtree, sans-serif", fontSize: "22px", fontWeight: 600, lineHeight: 1.25, letterSpacing: "0.5px"}
  body-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.25px"}
  button-md: {fontFamily: "Figtree, sans-serif", fontSize: "14px", fontWeight: 500, lineHeight: 1, letterSpacing: "1px"}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.accent-blue}"
    borderColor: "{colors.accent-blue}"
    borderWidth: "2px"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
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
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  jar-label:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.accent-berry}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
    typography: "{typography.caption}"

## Components

**button-primary** uses the signature yellow (`#fdd700`) with black text, matching the site's own `--lxs-rating-icon-color` accent and the flat, zero-radius button treatment seen in the Shopify checkout CSS (`border-radius:0`). Hover/active darkening is proposed, not observed.

**button-secondary** mirrors the theme's `.font--secondary-button` rule directly: transparent background, 2px border in the accent blue, uppercase 14px label. It is intended for lower-emphasis actions like "Learn More" or "View Ingredients."

**text-input** is a proposed pattern for newsletter/search fields; background and border colors are drawn from the observed neutral palette (`#ffffff`, `#dddddd`) since no explicit input CSS was supplied.

**nav-bar** proposes a clean white bar with a hairline divider, consistent with the light `body{background:#fff}` base and neutral grays present in the palette; actual header layout was not observed in the evidence.

**product-card** is inferred for the nut-butter jar grid: white surface, subtle hairline border, and title/price typography scaled from the theme's heading and paragraph font rules.

**hero** proposes a soft off-white section (`#f7f7f7`) for large introductory banners, using the display-xl scale for headline type; no hero markup or imagery was present in the supplied CSS.

**footer** inverts to a dark surface using the ink/black tone with yellow link accents, echoing the primary/on-primary contrast pattern established by the button styles; this is a proposed convention, not a confirmed footer capture.

**badge** repurposes the primary yellow as a pill-shaped tag, suitable for "Best Seller" or allergen call-outs; rounded-full matches common badge conventions and is proposed.

**search** is a rounded, soft-background field proposed for a product search affordance; no search-bar CSS was included in the evidence.

**jar-label** is a category-specific, inferred component representing the small flavor/ingredient chip often used on nut-butter product pages, using the berry accent (`#73033b`) as a distinguishing color drawn from the observed palette.

## Responsive Behavior

The following breakpoints are a **recommendation**, not measured site behavior:

| Breakpoint | Width      | Notes |
|-----------|------------|-------|
| mobile    | 0–599px    | Single-column layout; nav collapses to a hamburger/drawer pattern (proposed). |
| tablet    | 600–959px  | Two-column product grids; hero text scales to `display-md`. |
| desktop   | 960–1279px | Multi-column grids; full nav bar visible. |
| wide      | 1280px+    | Max-width container centers content; spacing increases to `{spacing.section}`. |

Touch targets should be a minimum of 44px in height, consistent with the Shopify accelerated-checkout button's own `clamp(25px, …, 55px)` sizing logic observed in the CSS. Collapse of secondary nav items into a menu below tablet width is proposed for usability, not confirmed by captured markup.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from static CSS/theme evidence only; no live DOM, computed layout, or interaction states were observed. Semantic color roles (e.g., which grays are hairlines vs. surfaces, and the exact use of purple/berry/red tones) are inferred from typical e-commerce patterns, not confirmed page usage. Font-family values for `--font--heading--family`, `--font--paragraph--family`, and `--font--accent--family` were not resolved to literal names in the supplied CSS; Figtree was inferred as the heading/accent face based on its presence in the site's font manifest. The decorative "Grove Script" family's licensing and actual usage context are unverified and excluded from core UI typography. All spacing, rounded, and responsive breakpoint values are proposed design-system defaults, not measurements extracted from the live site. Mobile navigation, hover/focus states beyond the two documented button rules, and product-page layout were not present in the supplied evidence.
