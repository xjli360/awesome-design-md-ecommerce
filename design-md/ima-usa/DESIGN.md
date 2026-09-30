---
version: alpha
name: "IMA-USA"
source_url: "https://www.ima-usa.com"
captured_at: "2026-09-28T04:13:36.909337+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  International Military Antiques presents itself as a utilitarian, catalog-driven commerce site rather than a heavily styled brand experience. The observed CSS is dominated by neutral grayscale values (#ffffff, #f8f8f8, #fafafa, #e0e0e0, #767676) used for backgrounds, cards, and borders, with body copy set in a near-black #231f20 and menu/heading text in pure #000000. The single recurring accent is a brick-red #bf2e1a, applied to cart CTAs and surcharge warnings, which this spec treats as the primary action color. A secondary navy (#212c64/#243a80) appears only on a PayPal checkout button and is treated as an inferred, low-frequency secondary/link color rather than a core brand hue. Small traces of gold (#c89c00) and green (#10bb07) exist in the palette but have no confirmed role in the supplied rules; they are mapped here to accent and success states as reasonable, clearly-labeled inferences. Typography is exclusively Roboto with sans-serif fallback, spanning 400–900 weights; no display or serif face is evidenced. The interpretation below proposes a restrained, document-like layout system (sharp-to-moderate corners, tight letter-spacing on buttons, uppercase CTAs) consistent with the observed uppercase/bold cart button and outlined "continue shopping" pattern, without asserting any unverified page layout.

colors:
  primary: "#bf2e1a"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#231f20"
  muted: "#767676"
  hairline: "#e0e0e0"
  surface-soft: "#fafafa"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  accent-navy: "#212c64"
  accent-gold: "#c89c00"
  success: "#10bb07"
  danger: "#e20808"
  overlay: "#000000bf"
typography:
  display-xl: {fontFamily: "Roboto, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Roboto, sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
  title-md: {fontFamily: "Roboto, sans-serif", fontSize: "18px", fontWeight: 500, lineHeight: 1.56, letterSpacing: "0px"}
  body-md: {fontFamily: "Roboto, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Roboto, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Roboto, sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: 1.0, letterSpacing: "1px"}
  button-md: {fontFamily: "Roboto, sans-serif", fontSize: "16px", fontWeight: 700, lineHeight: 1.5, letterSpacing: "1px"}
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
    textColor: "{colors.body}"
    borderColor: "{colors.body}"
    borderWidth: "2px"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
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
    typography: "{typography.button-md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.overlay}"
    ctaRounded: "{rounded.sm}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  provenance-callout:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.primary}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"

## Components

**button-primary** reflects the observed `.update-cart-info .btn` pattern: solid brick-red fill, white uppercase text, and heavy weight. It is the only high-saturation actionable surface evidenced in the CSS and should be reserved for checkout/purchase actions.

**button-secondary** mirrors the "continue shopping" pattern — a transparent fill with a 2px dark border and uppercase bold label. Hover/focus states (e.g., fill inversion) are proposed, not observed.

**text-input** is inferred from general form conventions; no explicit `input` selectors were supplied, so border color, radius, and padding are proposed defaults consistent with the site's flat, low-radius aesthetic.

**nav-bar** is grounded in `.main-menu-level-1` rules: bold 16px Roboto labels with 0.5px tracking and a light `#fafafa` hover/open background. Multi-level flyout or mobile drawer behavior beyond the supplied `.pm-open` push-menu class is not verified.

**product-card** draws on `.home-category-discovery-product-title` and `.product-price` rules — medium-weight 18px clamped titles and bold 20px pricing. Card chrome (shadow, exact border) is not evidenced and is treated as a light-hairline proposal.

**hero** is inferred from `.military-hero-content .cta-button`, which shows a white-bordered pill/rounded button over presumably a dark or photographic background; the dark overlay token is proposed to ensure text contrast, not confirmed from a screenshot.

**footer** styling is not directly evidenced; the soft gray background and muted text are proposed extrapolations from the site's general neutral surface palette (`#fafafa`, `#767676`) to keep visual consistency with observed menu backgrounds.

**badge** (e.g., "New," "Rare," or condition labels) is a proposed component using the otherwise-unassigned gold accent (`#c89c00`) for a small pill marker; no supplied selector confirms this usage.

**search** is proposed as a pill-shaped field consistent with the rounded, minimal button language seen in `.home-about-video-btn button` (rounded-100px pill with blurred translucent fill).

**provenance-callout** is a category-appropriate proposed component for militaria/historical items — a bordered info box (using the primary red as an accent rule) intended for authentication or historical-provenance notes, not present in the supplied CSS.

## Responsive Behavior

This is a recommended breakpoint structure, not measured site behavior; no media queries were present in the supplied evidence.

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <600px | Single-column product grid; nav collapses into the observed `.pm-open` push-menu pattern. |
| tablet | 600–959px | Two-column product grid; sticky search proposed. |
| desktop | 960–1279px | Multi-column grid; full horizontal nav. |
| wide | ≥1280px | Max-width content container; increased section spacing (`{spacing.section}`). |

Touch targets should meet a minimum 44px hit area for cart/menu icons; the `.close-menu` icon (28px glyph) likely needs padding to reach this, which is a proposed adjustment. Menu collapse below tablet is expected to reuse the existing `.pm-open` slide-in drawer class family observed in the CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/HTML extraction only; no rendered screenshots, computed layout, or interaction states (hover, focus, active, error) were observed or verified.
- Several palette values (e.g., `#e20063`, `#f8981d`, `#d02e2e`, `#917148`) appear in the supplied colors but have no associated selector in the evidence and were intentionally excluded from role mapping rather than guessed.
- The navy (`#212c64`) and gold (`#c89c00`) role assignments are inferred from single, low-frequency, non-primary usages (PayPal button, unclear origin) and may not reflect true brand secondary colors.
- Rounded and spacing scales follow a standard proposed system; only `4px` (review-button) and `100px`/pill (video button) radii are directly evidenced.
- Mobile/responsive layout, grid column counts, and breakpoint pixel values are proposed conventions, not measured from the live site.
- Font availability is limited to Roboto plus icon fonts (`ima-icons`, `icons`, `stamped-font`, Glyphicons); no display/serif typeface was evidenced, and web font licensing/self-hosting was not verified.
- Typography sizes for `display-xl`, `display-md`, `body-sm`, and `text-input` are proposed extrapolations, not directly present in the supplied CSS rules.
