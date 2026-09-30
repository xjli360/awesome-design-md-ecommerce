---
version: alpha
name: "House of Noa"
source_url: "https://houseofnoa.com"
captured_at: "2026-09-28T09:22:17.241842+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  House of Noa's evidence shows a warm, neutral storefront built on Shopify's Dawn-derived theme. The root palette pairs a soft cream canvas (#f7f4eb) with a near-black ink (#161414), giving a quiet, editorial contrast typical of a home-goods brand. Two observed font families drive type: "minerva-modern" (a serif, used here for headings per the h1-h5 CSS binding to --font-heading-family) and "nimbus-sans" (a sans-serif, bound to --font-body-family for body copy and UI text). No numeric font sizes were present in the supplied CSS beyond body's 1.2rem base and .text-body's 1.5rem, so all display/title/body sizes below are proposed and labeled as such, scaled from that base.
  Accent colors are inferred from functional CSS rather than declared brand tokens: #1990c6/#136f99 appear only on a Shopify payment-button skeleton (hover state), so they are treated here as a secondary "action-blue" utility rather than the primary brand accent, which remains the dark ink button (rgb 22,20,20) confirmed in the :root button variables. Surface variants (#ece9de, #fbf9f5, #ffe3d0) are drawn from the broader palette array and assigned to soft/card roles by proximity to the cream canvas, since no selector evidence ties them to a specific component. Rounded and spacing scales are proposed defaults, not measured, since the CSS exposes only custom-property variable names (e.g., --buttons-radius-outset) without resolved pixel values.

colors:
  primary: "#161414"
  ink: "#161414"
  canvas: "#f7f4eb"
  body: "#161414"
  muted: "#545351"
  hairline: "#dedede"
  surface-soft: "#ece9de"
  surface-card: "#fbf9f5"
  on-primary: "#f7f4eb"
  accent-warm: "#ffe3d0"
  accent-action: "#1990c6"
  accent-action-hover: "#136f99"
  accent-red: "#eb260c"
  accent-green-deep: "#0a452b"
  accent-blue-pale: "#bcd6e3"
  border-strong: "#000000"
  surface-white: "#ffffff"
typography:
  display-xl: {fontFamily: "'minerva-modern', serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'minerva-modern', serif", fontSize: 34px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'minerva-modern', serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'nimbus-sans', sans-serif", fontSize: 19.2px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-sm: {fontFamily: "'nimbus-sans', sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "'nimbus-sans', sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'nimbus-sans', sans-serif", fontSize: 15px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.3px}
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
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-tertiary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  text-input:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    imagePadding: "{spacing.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    overlayTextColor: "{colors.surface-white}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    hairline: "{colors.muted}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  variant-swatch:
    size: "32px"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.ink}"
    gap: "{spacing.xs}"

## Components
**button-primary** renders the dark-ink filled action used for "Add to Cart" and primary CTAs, mapped from the observed `--color-button: 22,20,20` / `--color-button-text: 247,244,235` root variables. **button-secondary** inverts this for lighter-weight actions (e.g. "Continue Shopping"), using the `--color-secondary-button` pairing observed in the same root block. **button-tertiary** is proposed for low-emphasis links/filters, following the theme's `.button--tertiary` pattern of transparent background with a reduced-opacity border (`--alpha-button-background: 0`).

**text-input** is a proposed field style for search, email capture (the "$30 off" list-join prompt), and account forms; no explicit input CSS was supplied, so border and padding are inferred from general spacing conventions.

**nav-bar** reflects the cream canvas persisting into the header, with the announcement-bar height (`--announcement-bar-height: 4rem`) as the only measured structural value; link color is inferred from `--color-link: 22,20,20`.

**product-card** models the repeating best-seller tiles (e.g. "Little Nomad Play Mat | Winslow $129+"), using the `.product-card-wrapper .card` custom-property hooks for radius, border, and shadow, though their resolved pixel values were not present in evidence — treated as proposed defaults.

**hero** covers the large seasonal promo banners ("Your floors, upgraded," "Colors of fall are here"), where a white-on-image foreground override (`--color-foreground: 255,255,255`) was observed for a specific section, justifying the separate `overlayTextColor` token.

**footer** is proposed as a dark-ink block inverting the canvas/ink relationship, consistent with the brand's two-tone palette; no footer-specific selectors were supplied.

**badge** supports promotional pill labels like "Sale" or "Pre-order," using the observed badge variables (`--color-badge-background`, `--color-badge-border`) at 1:1 with the root tokens.

**variant-swatch** is a proposed pattern for the many color-variant pickers seen in the evidence (e.g. "Bennett in Taupe & Sable," "Dover in Chestnut"), since the underlying swatch CSS itself was not included, only product/variant text.

## Responsive Behavior
The following breakpoint table is a **recommendation**, not measured site behavior — no media queries were included in the supplied CSS evidence.

| Breakpoint | Width       | Layout guidance (proposed) |
|---|---|---|
| mobile | <600px | Single-column stacking; nav collapses to hamburger; product grid 1–2 cols |
| tablet | 600–959px | Product grid 2–3 cols; hero text scales to display-md |
| desktop | 960–1279px | Product grid 3–4 cols; full nav visible |
| wide | ≥1280px | Max content width constrained; section spacing increases to `{spacing.section}` |

Touch targets should be a minimum 44px height (aligned with the observed `--shopify-accelerated-checkout-button-block-size:44px` default on the payment button). Nav and filter drawers are assumed to collapse into off-canvas panels below tablet width; this is proposed, not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Static CSS extraction did not include resolved pixel values for most spacing, radius, or typographic sizes; all such values above are proposed defaults scaled from the one confirmed base font-size (1.2rem body, 1.5rem `.text-body`).
- Only two font families were observed in evidence ("minerva-modern", "nimbus-sans"); no weights, styles, or web-font source/licensing were confirmed, and generic fallbacks are used per requirement.
- Semantic color roles (surface-soft, surface-card, accent-warm, etc.) are inferred by matching palette entries to plausible UI roles; no selector evidence ties these specific hexes to specific components.
- The #1990c6/#136f99 blue pair is confirmed only for a Shopify accelerated-checkout button skeleton, not for general brand accent usage — its role here is scoped narrowly (`accent-action`).
- No interaction states (hover/focus/active beyond the checkout button), mobile navigation behavior, or real rendered layout were observed; all such claims are explicitly labeled proposed.
- Component definitions (product-card, hero, footer, variant-swatch) are structurally plausible given page-text content but not confirmed against actual DOM/CSS selectors beyond the custom-property hooks cited.
