---
version: alpha
name: "Manfrotto"
source_url: "https://manfrotto.com"
captured_at: "2026-09-28T09:13:20.358865+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Manfrotto's storefront CSS exposes a Bootstrap-derived variable system layered under a Hyva/Magento theme, with `--primary` and `--danger` both mapped to a saturated signal red (#f51928) against a neutral gray-scale body (#252525 ink, #505050 secondary text, #6e6e6e muted, #f1f1f1 light surfaces). The base stylesheet explicitly sets `body { font-family: "Inter", ... sans-serif }` at 16px/1.5, with headings inheriting the family at weight 500 and line-height 1.2 — the only typographic facts confirmed by the evidence. Additional families (Open Sans, Karla-Bold, Roboto, Helvetica Neue) appear in the asset manifest but are not tied to specific selectors here, so they are treated as unverified and excluded from primary tokens.
  This interpretation reads Manfrotto as a technical, professional-gear brand: a compact neutral palette punctuated by a single confident red for calls-to-action and alerts, functional Bootstrap status colors (success green, warning amber, info cyan) reused for stock/shipping-style badges relevant to bag inventory, and restrained 4px input radii carried through as the base rounding unit. Layout, breakpoints beyond the declared Bootstrap variables, and any live interaction states are inferred, not observed.

colors:
  primary: "#f51928"
  ink: "#252525"
  canvas: "#ffffff"
  body: "#505050"
  muted: "#6e6e6e"
  hairline: "#d1d1d1"
  surface-soft: "#f1f1f1"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  dark: "#3a3a3a"
  border: "#e0e0e0"
  success: "#006600"
  warning: "#ffc107"
  info: "#17a2b8"
  accent: "#f8971d"
typography:
  display-xl: {fontFamily: "'Inter', -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.2, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Inter', -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "'Inter', -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'Inter', -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Inter', -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Inter', -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Inter', -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.5, letterSpacing: 0.2px}
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
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    focusRingColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-md}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  bag-fit-finder:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.accent}"
    borderColor: "{colors.border}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components
**button-primary** carries the confirmed `--primary`/`--danger` red as its fill, intended for primary conversion actions (Add to Bag, Checkout); the 4px radius matches the input `border-radius: 0.25rem` observed in the stylesheet. **button-secondary** is a proposed outline variant using the observed hairline gray border for tertiary actions like "Compare" or "Save."

**text-input** directly reflects the observed form-control rules: white background, `#505050` text, `#d1d1d1` border, and a red-tinted focus shadow (derived from the `rgba(245,25,40,0.25)` focus box-shadow present in the CSS). Placeholder color `#6e6e6e` is taken verbatim from the placeholder selectors.

**nav-bar** is a proposed structural component (header height, hairline divider) since no header-specific selectors were supplied; it reuses confirmed body/ink colors for continuity.

**product-card** is proposed for bag/tripod listings, using a soft off-white surface (`#fafafa`) distinct from pure white canvas to imply subtle elevation, with title weight/line-height matching the confirmed h1–h6 rule (`font-weight: 500; line-height: 1.2`).

**hero** is proposed for category/landing banners, using the dark neutral (`#3a3a3a`) as a full-bleed background with white text, appropriate for product photography overlays; padding uses the largest spacing token to suggest generous vertical rhythm — not measured.

**footer** proposes the same dark neutral for brand consistency, with muted-gray links, matching Bootstrap's `--gray`/`--gray-dark` variable pairing found in `:root`.

**badge** repurposes the confirmed Bootstrap `--success` green for stock/availability flags (e.g., "In Stock"), a plausible reuse of the theme's existing semantic color rather than a new invented hue.

**bag-fit-finder** is a category-specific proposed component for the camera-bag vertical — a compatibility/capacity helper module using the observed orange accent (`#f8971d`, Bootstrap `--orange`) to visually separate it from primary red CTAs, on the same card surface as product listings.

## Responsive Behavior
Recommendation only — no live breakpoint behavior was observed. Based on the Bootstrap variables present (`--breakpoint-sm: 576px`, `--breakpoint-md: 768px`, `--breakpoint-lg: 992px`, `--breakpoint-xlg: 1024px`, `--breakpoint-xl: 1200px`, `--breakpoint-xxl: 1980px`):

| Range | Behavior (proposed) |
|---|---|
| < 576px | Single-column stack, nav collapses to hamburger, touch targets ≥ 44px |
| 576–991px | Two-column product grids, search bar full-width |
| 992–1199px | Three-column grids, persistent top nav |
| ≥ 1200px | Four-column grids, max-width container, hover states enabled |

Touch targets should maintain minimum 44×44px hit areas on interactive elements (buttons, badges) at all widths under 992px; this guidance is a general practice recommendation, not a measured constraint.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived solely from static CSS/text evidence supplied for the splash-page bundle; no rendered layout, JavaScript-driven interaction, or mobile viewport was observed. Semantic color roles (e.g., which gray serves "body" vs. "muted") are inferred from Bootstrap variable naming conventions and selector context, not confirmed via visual inspection. Font sizes, weights (outside the explicitly declared 16px body and h1–h6 weight-500/line-height-1.2 rule), letter-spacing, and component paddings are proposed defaults, not measured. Additional font families listed in the asset manifest (Open Sans, Karla-Bold, Roboto, Helvetica Neue, Font Awesome variants) appear in the CSS bundle but lack selector-level evidence tying them to specific text roles, so they were excluded from typography tokens. Custom font licensing/availability (including Inter's actual delivery method — self-hosted vs. system fallback) was not verified. Component states (hover, active, disabled, error) are proposed conventions, not observed pseudo-class rules beyond the table-hover/table-striped opacity rules present in the source CSS.
