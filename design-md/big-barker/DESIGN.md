---
version: alpha
name: "Big Barker"
source_url: "https://bigbarker.com"
captured_at: "2026-09-28T04:17:31.246359+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Big Barker's storefront CSS exposes a neutral, high-contrast base (white canvas, near-black
  ink and button colors) paired with a small set of warm, muted accent tones — a sage-green
  dark accent, a terracotta light accent, and a slate blue — defined as root custom properties
  and applied to headings, hover states, and feature-row buttons. Supporting neutrals (light
  grays, warm off-white "EFEDEA") structure dividers, dimmed panels, and card backgrounds.
  A small red/orange pair (#ff4f33, #d02e2e) appears tied to cart and alert affordances,
  while a green (#56ad6a) is treated here as an inferred success/availability color since no
  explicit role was declared.

  Typography evidence lists DM Sans, Fraunces, Outfit, Ovo, and monospace/Consolas as loaded
  families; a `--typeHeaderPrimary` variable references a font not present in the observed
  family list, so it is excluded here per policy. This interpretation assigns Fraunces (an
  observed serif) to display headings for a warm, editorial tone befitting a premium pet-
  furniture brand, and DM Sans to body copy and UI text, consistent with `--typeBasePrimary`.
  Outfit is proposed for compact UI labels (buttons, nav) as a geometric sans contrast to
  Fraunces. All spacing, radius, and several semantic-role assignments below are inferred
  and marked as proposed, not measured.

colors:
  primary: "#111111"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6b6f73"
  hairline: "#e8e8e1"
  surface-soft: "#f2f2f2"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  accent-dark: "#657b72"
  accent-light: "#ae633d"
  accent-blue: "#486988"
  neutral-warm: "#efedea"
  alert: "#d02e2e"
  alert-strong: "#c20000"
  success: "#56ad6a"
  cart-dot: "#ff4f33"
  overlay-scrim: "#0000001a"
typography:
  display-xl: {fontFamily: "'Fraunces', serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Fraunces', serif", fontSize: 34px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0em}
  title-md: {fontFamily: "'Outfit', sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0em}
  body-md: {fontFamily: "'DM Sans', sans-serif", fontSize: 15px, fontWeight: 300, lineHeight: 1.4, letterSpacing: 0.025em}
  body-sm: {fontFamily: "'DM Sans', sans-serif", fontSize: 13px, fontWeight: 300, lineHeight: 1.4, letterSpacing: 0.025em}
  caption: {fontFamily: "'DM Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.05em}
  button-md: {fontFamily: "'Outfit', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.05em}
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
    backgroundColor: "{colors.accent-light}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "none"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.neutral-warm}"
    textColor: "{colors.accent-dark}"
    titleTypography: "{typography.display-xl}"
    ctaButton: "button-primary"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  comparison-slider:
    backgroundColor: "{colors.canvas}"
    handleColor: "{colors.primary}"
    accentColor: "{colors.accent-blue}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"

## Components

**button-primary** uses the dark near-black `colorBtnPrimary` fill with white text, matching the theme's `--colorBtnPrimary`/`--colorBtnPrimaryText` pair; hover and active states are proposed, not observed in the supplied rules.

**button-secondary** maps to the terracotta `colorLightAccent`, directly evidenced by `.barker-tni-alternate .feature-inner-row__text .btn` and its `:hover` rule, both setting this same accent as background with white text — a confirmed brand accent-button pattern.

**text-input** is a proposed pattern; no input-field CSS was supplied, so border, radius, and padding follow the general hairline/neutral system inferred from `--colorBorder` and body typography.

**nav-bar** is inferred from the announcement-bar and drawer color tokens (`--colorAnnouncement`, `--colorDrawers`); actual navigation markup, sticky behavior, and breakpoints were not observed.

**product-card** infers a light card surface from `--colorBodyLightDim`/`--colorBodyMediumDim` and border from `--colorBorder`; grid gutter (22px) is evidenced by `--grid-gutter`, supporting card spacing assumptions.

**hero** draws on `.barker-tni-h1` (color: `--colorDarkAccent`) and the warm `--colorLightNeutral` background used elsewhere (`.bsg-product-page`), plus the observed `.hero .flickity-button` carousel-control styling, confirming a hero section contains a slider.

**footer** is proposed using `--colorFooter`/`--colorFooterText` tokens (both effectively white/black), extended with the observed hairline border for section separation; column layout is not observed.

**badge** is proposed for stock/availability or sale flags, borrowing the red family (`#d02e2e`, `#ff4f33`) seen on cart-dot and alert-adjacent tokens; no literal badge component was present in evidence.

**search** is inferred from the icon-search reference in page title metadata only; no search-bar CSS was supplied, so styling is a proposed neutral pill treatment.

**comparison-slider** is grounded in the observed `.comparison__button:before/:after` rules (white overlay fills), suggesting an interactive before/after or durability-comparison widget appropriate to a dog-bed durability narrative; exact interaction mechanics were not observed.

## Responsive Behavior
Proposed breakpoints (not measured from the live site): mobile ≤480px, tablet 481–768px, desktop 769–1200px, wide ≥1201px. Navigation is assumed to collapse into a hamburger/drawer below tablet width, consistent with the `icon-hamburger` and drawer color tokens present in evidence. Touch targets for buttons and nav items should be at least 44×44px. Product grids likely reduce from multi-column to single/double column on mobile, using the observed 22px grid gutter as a baseline. This section is a recommendation only; no responsive CSS or viewport behavior was captured.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/custom-property extraction only; no rendered DOM, computed styles, or interaction states were observed. The `--typeHeaderPrimary` variable references "Urbanist," a font not present in the supplied font-family evidence, and was therefore excluded from typography roles per policy — actual header rendering may differ from this interpretation. Several color-to-role assignments (success, alert, badge, search) are inferred from adjacent naming or isolated tokens rather than confirmed component usage. All spacing and radius values follow a standard proposed scale, not measured pixel values from the site. Hover/focus/active states beyond the two documented button `:hover` rules are proposed. Mobile menu behavior, carousel mechanics beyond button color, and checkout/cart flows were not observed. Font licensing and self-hosting/CDN availability for DM Sans, Fraunces, Outfit, and Ovo were not verified.
