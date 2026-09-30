---
version: alpha
name: "Minaal"
source_url: "https://minaal.com"
captured_at: "2026-09-28T10:22:39.592933+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Minaal's evidence points to a restrained, monochrome-first system built around near-black neutrals (#212121, #1c1b1b, #323230) on white and off-white grounds (#ffffff, #f2f2f2, #fcfbfb), consistent with a minimalist travel-gear positioning ("Carry less, go further"). Header CSS variables confirm a white header background with a dark charcoal text color and layered opacity tints for hover/disabled states, which this spec treats as the primary UI neutrals. A warm terracotta (#b04228) and a muted rust (#9b3a23) appear in the palette and are inferred here as an accent/CTA family distinct from the default near-black button, since Shopify buttons default to #222/#212121. Judge.me review widget variables surface a gold star color (#f0ab00), reused for rating/review UI. Typography evidence shows a serif family, 'Ivar', explicitly forced at weight 500 in at least one rule, inferred as the display/heading face for editorial warmth; 'GT America' and 'Nunito Sans' also appear in font stacks and are inferred as the workhorse sans for body copy, UI labels, and buttons, since base.css otherwise references only generic var(--font--body). Border-radius is largely undeclared or explicitly 0 (Judge.me), so corners are treated as flat-to-subtle by default, with buttons/cards allowed a small radius only where component CSS implies it (e.g., skeleton loaders at .5em).

colors:
  primary: "#212121"
  ink: "#1c1b1b"
  canvas: "#ffffff"
  body: "#323230"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f2f2f2"
  surface-card: "#fcfbfb"
  on-primary: "#ffffff"
  accent: "#b04228"
  accent-deep: "#9b3a23"
  star: "#f0ab00"
  success: "#00964d"
  danger: "#d12328"
  sand: "#e9e0cf"
typography:
  display-xl: {fontFamily: "'Ivar', serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Ivar', serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'GT America', sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'GT America', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'GT America', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  caption: {fontFamily: "'Nunito Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'GT America', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  compatibility-badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.md}"

## Components

**button-primary** uses the near-black brand neutral (#212121) matching the Shopify default button variable fallback (#222), rendered with white text; this is the default add-to-cart / checkout affordance, with hover state (darkening toward #212121b3 per observed opacity token) proposed but not measured.

**button-secondary** is an outlined variant using the same ink color for border and text on a transparent field, proposed for lower-emphasis actions like "Continue shopping" or filter toggles seen in the nav/cart copy; no direct outline-button CSS was supplied, so this is an inferred pattern.

**text-input** is proposed as a flat white field with a light hairline border (#dddddd), suited to newsletter/search/quantity fields; the quantity-input CSS confirms centered text and generic sizing but not border color, so border/background are inferred defaults.

**nav-bar** reflects the explicit header CSS variables: white background (#ffffff), charcoal text (#323230) with graduated opacity tints (0.7/0.5/0.1) for secondary links and disabled states, and a sticky behavior flag (--header-is-sticky:1) — sticky positioning is evidenced by the variable name, not by measured scroll behavior.

**product-card** is proposed using the near-white card surface (#fcfbfb) distinct from pure white, giving bag imagery slight visual separation on category/grid pages implied by "Bags," "Carry-ons," and "Accessories" navigation groupings.

**hero** uses the dark ink background with white text and the serif display type, proposed for full-bleed lifestyle imagery banners (e.g., "Carry less, go further") though no hero-specific CSS block was supplied — this is a category-typical, evidence-adjacent pattern for a premium travel brand.

**footer** uses the darker header surface tone (#f2f2f2) and muted gray text, sized for the long "Info"/"About" link list observed in the page text (Owner, Reviews, FAQ, Shipping, Returns, Warranty, Gift Cards, Contact Us).

**badge** repurposes the terracotta accent (#b04228) for promotional or "Most Popular" style tags implied by the "Most Popular" navigation label; color choice is inferred since no badge-specific CSS was supplied.

**search** is a proposed light-gray input pattern for the header search affordance implied by standard Shopify header structure; no search-input CSS was directly supplied.

**compatibility-badge** is a category-specific component proposed for the "Approved carry-on bags for US, EU & APAC" claim — a bordered, low-emphasis stamp-style badge distinguishing regulatory/compliance information from promotional badges.

## Responsive Behavior

Recommended breakpoints (not measured from live layout):

| Breakpoint | Width      | Notes |
|---|---|---|
| Mobile     | 0–599px    | Single-column product grid, collapsed hamburger nav, sticky header per --header-is-sticky |
| Tablet     | 600–959px  | 2-column product grid (matches --per-row:2 hint in supplied CSS context) |
| Desktop    | 960–1279px | Full nav bar visible, 3–4 column grids |
| Wide       | 1280px+    | Max-width content container, generous section spacing (`{spacing.section}`) |

Touch targets should meet a minimum 44px height, applying `{spacing.md}` vertical padding to buttons and nav items. Navigation collapses to a drawer or accordion below the tablet breakpoint given the deep "By Type / By Usage / By Research" mega-menu structure implied in the sitemap text; this collapse behavior is proposed, not observed in rendered markup.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS variables, a text excerpt, and a color/font inventory only — no rendered layout, computed styles, animation, or interaction states were observed. Semantic role assignments (e.g., which neutral is "primary" vs. "ink," which warm tone is "accent") are inferred from variable naming and typical e-commerce usage, not confirmed via visual inspection. Font sizes, weights (aside from the one explicit `font-weight:500 !important` on 'Ivar'), letter-spacing, and line-heights in the typography table are proposed conventions, not extracted values, since base.css referenced only CSS custom properties (`var(--font--body)`, etc.) without supplied resolved values. Border-radius values largely default to the generic scale requested, since only Judge.me's explicit `border-radius: 0` was supplied. Mobile menu behavior, hover/focus states, cart drawer interaction, and checkout flow are not observed. Availability and licensing of 'Ivar' and 'GT America' as custom/licensed webfonts were not verified and should be confirmed before implementation.
