---
version: alpha
name: "Methodical Coffee"
source_url: "https://methodicalcoffee.com"
captured_at: "2026-09-28T09:45:29.519279+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is built from Shopify theme CSS variables, a supplied color palette, and font-family declarations for Methodical Coffee, a Greenville, SC coffee roaster and cafe brand. No hex value below is invented; every color is drawn from the supplied observed palette, though the specific UI role assigned to each (primary action, hairline, surface) is inferred since button and link colors were only exposed as unresolved CSS custom properties (e.g. --btn-bg-color) rather than resolved rgb values.
  The palette leans warm and cafe-like: cream canvas tones (#fffaf3, #fbf2e7) paired with a dark warm-brown ink (#3e3a37), suggesting a roastery aesthetic rather than a stark white e-commerce look. A brown accent (#8a501d) is proposed as the primary action color, consistent with coffee/roast theming, with red (#c20000), green (#3ea36a), and gold (#dd9a1a) reserved as inferred secondary accents for badges, promo banners, and status indicators — all pulled directly from the observed swatch set.
  Typography pairs a serif display face, Canela-Light, for headings (confirmed via h1–h6 selectors, weight 300, tight letter-spacing) with Hanken Grotesk for body copy and buttons (confirmed via body and .btn selectors, weight 300–600). Sizes below are proposed, not measured.

colors:
  primary: "#8a501d"
  ink: "#3e3a37"
  canvas: "#fffaf3"
  body: "#3e3a37"
  muted: "#938d86"
  hairline: "#dbd2c7"
  surface-soft: "#fbf2e7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#c20000"
  accent-green: "#3ea36a"
  accent-gold: "#dd9a1a"
  accent-blue: "#3555c9"
typography:
  display-xl: {fontFamily: "Canela-Light, serif", fontSize: 48px, fontWeight: 300, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Canela-Light, serif", fontSize: 32px, fontWeight: 300, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "Canela-Light, serif", fontSize: 22px, fontWeight: 300, lineHeight: 1.25, letterSpacing: -0.2px}
  body-md: {fontFamily: "Hanken Grotesk, helvetica, arial, sans-serif", fontSize: 16px, fontWeight: 300, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Hanken Grotesk, helvetica, arial, sans-serif", fontSize: 14px, fontWeight: 300, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Hanken Grotesk, helvetica, arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Hanken Grotesk, helvetica, arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1em, letterSpacing: 0.4px}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  roast-profile-filter:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"

## Components
**button-primary** is proposed for primary CTAs like "Add to cart" and "Subscribe," using the inferred brown accent against a light on-primary text for warmth consistent with a roastery brand; the exact resolved theme color was not exposed in the supplied CSS, so this mapping is inferred from the broader palette.

**button-secondary** covers outlined actions such as "Quick buy" or "Learn more," using card-surface fill with a hairline border so it recedes against primary actions; hover/active states were not observed and are proposed only.

**text-input** models newsletter and search fields with a light surface, thin hairline border, and body typography; focus-state styling (e.g., border color shift) is unobserved and proposed.

**nav-bar** represents the top utility/mega-menu bar referenced by categories like Coffee, Tea, Goods, and Learn; background uses the cream canvas with a hairline divider, though the `.section-header` transparent-header variant (white text on hero) noted in the CSS suggests a state-dependent nav not fully modeled here.

**product-card** supports grid listings (e.g., Watercolor, Best Sellers) with card-surface background, rounded corners, and title/price typography split; rating/review display was present in page text but its visual styling was not observed.

**hero** models the homepage banner ("WE ARE METHODICAL") using dark ink background with light text, matching the `--transparent-header-text-color: #ffffff` rule found in the header CSS; actual hero imagery/overlay treatment is not confirmed from static CSS alone.

**footer** covers the multi-column footer (Methodical, Club Methodical, Visit, Legal) with dark ink background and light text for contrast; column layout is inferred, not measured.

**badge** is proposed for small labels like "Sold out" or review counts, using the gold accent; actual badge color/shape was not present in supplied CSS and is a proposed pattern.

**search** models the header search trigger/panel; background and border are proposed from surface and hairline tokens since no dedicated search-input CSS was supplied.

**roast-profile-filter** is a category-specific proposed component for filtering by roast style (Classic/Contemporary/Avant-Garde) or origin (South America, Africa, Asia), using pill-shaped toggles; this pattern is inferred from the page's taxonomy text, not from observed filter markup or styling.

## Responsive Behavior
Recommended, not measured — the CSS confirms only that `--gutter` and `--container-pad-x` scale across breakpoints (mobile 16px, desktop 30px, larger 50–60px gutters), implying at least three responsive tiers.

| Breakpoint | Range | Container padding (observed var) | Nav behavior (proposed) |
|---|---|---|---|
| Mobile | <768px | 16px | Collapse nav to hamburger; stack product grid to 1–2 columns |
| Tablet | 768–1023px | 30px | Condensed horizontal nav; 2–3 column product grid |
| Desktop | 1024–1439px | 50px | Full mega-menu; 3–4 column product grid |
| Large | ≥1440px | 60px | Full mega-menu with wider gutters; 4+ column grid |

Touch targets should be at least 44×44px for buttons and nav items per general accessibility guidance; this is a recommendation, not a verified measurement from the site.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS and page-text extraction only; no live rendering, computed styles, or interaction states (hover, focus, active, error, disabled) were observed. Button and link colors rely on unresolved CSS custom properties (e.g., `--btn-bg-color`, `--btn-text-color`); the specific role assignments in this document (primary, badge, accent colors) are inferred from the broader supplied palette, not confirmed resolved values. Layout structure (grid columns, mobile menu behavior, card spacing) is proposed based on common e-commerce/Shopify patterns and the taxonomy implied by page text, not measured from rendered DOM. Font availability, licensing, and web-font loading for Canela-Light/Medium and Hanken Grotesk were not verified — these are proprietary/licensed font names observed in CSS but not confirmed as self-hosted, subsetted, or properly licensed for reuse. Additional font families in evidence (Abril Fatface, Canela-Medium, Trirong) appear in the font list but their actual usage context on the site was not confirmed and are excluded from this interpretation's core typography scale.
