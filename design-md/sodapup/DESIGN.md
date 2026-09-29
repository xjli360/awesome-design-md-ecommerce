---
version: alpha
name: "SodaPup"
source_url: "https://sodapup.com"
captured_at: "2026-09-28T10:12:37.406698+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  SodaPup is a Shopify-based DTC storefront for durable dog-enrichment
  products (lick mats, chew toys, treat dispensers) sold under several
  house brands. The extracted CSS is Shopify Dawn-derived: a neutral
  near-black/white base (--color-foreground: 18,18,18 on
  --color-background: 255,255,255) drives text, buttons, and links,
  with no distinct brand hue defined at the theme-variable level. The
  one recurring accent, #2f7594 (a muted teal-blue), appears only in
  the Judge.me review-widget variables (star color, review CTA,
  reviewer name), so it is treated here as an inferred secondary/accent
  color for ratings and trust signals rather than a confirmed primary
  brand color. #1990c6/#136f99 come from the Shopify accelerated
  checkout button and are proposed as an interactive-blue for
  wallet/CTA states. Grays (#f3f3f3, #f9f9f9, #dedede, #cccccc,
  #7b7b7b) supply surfaces, hairlines, and muted text. Typography uses
  the observed font-family token pointing to Murecho with system
  sans-serif fallback; JudgemeStar is an icon font for review stars,
  not body/heading text. Border-radius variables resolve toward 0 in
  the sampled rules (Judge.me, payment button default), so the
  interpretation leans toward a squared, utilitarian retail aesthetic.

colors:
  primary: "#121212"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#7b7b7b"
  hairline: "#dedede"
  surface-soft: "#f3f3f3"
  surface-card: "#f9f9f9"
  on-primary: "#ffffff"
  accent: "#2f7594"
  accent-hover: "#136f99"
  interactive: "#1990c6"
  border-strong: "#cccccc"
typography:
  display-xl: {fontFamily: "Murecho, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: 0.5px}
  display-md: {fontFamily: "Murecho, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.4px}
  title-md: {fontFamily: "Murecho, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0.3px}
  body-md: {fontFamily: "Murecho, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.44, letterSpacing: 0.6px}
  body-sm: {fontFamily: "Murecho, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  caption: {fontFamily: "Murecho, sans-serif", fontSize: 11px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.5px}
  button-md: {fontFamily: "Murecho, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.6px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  review-rating:
    starColor: "{colors.accent}"
    linkColor: "{colors.accent}"
    reviewerNameColor: "{colors.accent}"
    ctaBackground: "{colors.accent}"
    ctaTextColor: "{colors.on-primary}"
    typography: "{typography.caption}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaButton: "button-primary"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    borderTop: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    resultSurface: "{colors.surface-card}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"

## Components

**button-primary** uses the theme's `--color-button` (near-black) and `--color-button-text` (white) variables directly observed in `:root`; this is the highest-confidence component since the values are explicit CSS custom properties rather than inference.

**button-secondary** mirrors the observed `--color-secondary-button`/`--color-secondary-button-text` pair (white fill, dark text/border) confirmed by the `.button--secondary,.button--tertiary` rule that swaps these variables in.

**text-input** is proposed: no explicit input-border rule was supplied, so hairline gray and an ink focus border are inferred from the general `--color-foreground`/border-token conventions in the Dawn base stylesheet, including the observed `.2rem solid rgba(foreground,.5)` focus-outline pattern.

**nav-bar** is inferred layout; only the presence of a large country/currency selector in the page text confirms a header-level localization control exists. Visual placement, sticky behavior, and icon set are not observed.

**announcement-bar** responds to the visible copy "Free Shipping On Orders Over $40" in the page excerpt, indicating a top utility bar exists; the ink-on-white inversion (dark bg, white text) is a proposed treatment, not a measured style.

**product-card** references the theme's card CSS variables (`--product-card-corner-radius`, shadow tokens) whose actual values were not resolved in the supplied evidence, so radius/shadow are treated as proposed defaults (square, flat) consistent with the 0-radius pattern seen elsewhere (Judge.me widget, payment button fallback).

**review-rating** is grounded in the Judge.me (`--jdgm-*`) variables, all set to `#2F7594`. Since this is the only distinct non-neutral color defined at the root level, it is promoted to the palette's `accent` role for star ratings, review CTAs, and reviewer-name text — a reasonable, evidence-based but inferred semantic assignment.

**hero** is a proposed compositional pattern (large heading, supporting copy, primary CTA) typical of Shopify home templates; no hero-specific selector was present in the supplied CSS, so background and spacing are proposed.

**footer** styling is unobserved at the color level (color-scheme-2 through -5 exist but their variable values were not supplied); a neutral light-gray surface with muted text is proposed rather than confirmed.

**badge** and **search** reuse the explicit `--color-badge-*` root variables and a proposed input/result-surface treatment consistent with the text-input component; search overlay behavior itself was not observed.

## Responsive Behavior
Recommended, not measured from live rendering:

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| mobile | <750px | single-column product grid, collapsed nav into a menu button, announcement bar text may truncate |
| tablet | 750–989px | 2-column product grid, condensed nav links |
| desktop | ≥990px | full horizontal nav, 3–4 column product grid |

Touch targets should be at least 44×44px for buttons and nav icons; the country/currency selector (very long list observed in page text) should collapse into a searchable dropdown on small screens rather than a full inline list. None of this reflow behavior was captured in the supplied static CSS/text and is a recommendation only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is static CSS/text extraction only; no rendered screenshots, computed layout, or interaction states (hover/focus/active, cart drawer, mobile menu) were observed.
- `--product-card-corner-radius`, `--buttons-radius`, `--inputs-radius`, and `--popup-corner-radius` are referenced but their resolved pixel values were not present in the supplied rules; the `rounded` scale is therefore largely proposed, leaning toward 0 based on the one confirmed 0-radius instance (Judge.me).
- The teal `#2f7594` accent is confirmed only for the third-party Judge.me review widget; treating it as a general site "accent" color is an inferred semantic extension, not a confirmed brand-color declaration.
- Several palette entries (`#eb001b`, `#f79e1b`, `#ff5f00`, `#0071ce`, `#334fb4`, `#142fbd`, `#1532cb`) closely resemble standard payment-network mark colors (e.g., card-brand icons) and were excluded from the design token set as they likely belong to third-party payment badges rather than brand styling.
- Font family "Murecho" is used per the observed `--font-body-family`/`--font-heading-family` token references; actual font-weight availability, licensing, and whether it is self-hosted or a Google Font were not verified. "JudgemeStar" is a third-party icon font for star ratings and is excluded from the typography scale.
- Root `font-size` (rem base) was not directly supplied; body-md pixel values assume a common Shopify Dawn 10px root convention and are labeled inferred.
- Footer, hero, and nav visual styling (background color, spacing, breakpoints) are proposed compositions based on typical Shopify theme structure, not confirmed by supplied selectors.
