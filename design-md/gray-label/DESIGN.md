---
version: alpha
name: "Gray Label"
source_url: "https://gray-label.com"
captured_at: "2026-09-29T04:33:38.482107+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Gray Label's storefront CSS shows a restrained, monochrome-first palette built around
  explicit design tokens (--color-white, --color-dark, --color-almost-black,
  --color-dark-grey, --color-grey, --color-light-grey, --color-off-white), plus a small
  set of functional accents (--color-sale #CC3314, --color-green #67A98D,
  --color-orange #EBCB5A, --color-blue #3B82F6, --color-red #AF6A6A). This confirms a
  minimalist, editorial brand voice consistent with the "Organic Apparel for the little
  Minimalist" positioning, where black-and-white contrast carries the interface and
  color is reserved for status/sale signaling rather than decoration.
  Headings use the proprietary GT America family (observed on .wysiwyg h1 and button
  classes); body copy inherits an unset font-family that falls back to system sans-serif
  before webfonts load, so GT America is treated as the intended but unverified body
  font. Buttons use a 2px border-radius and an 8px/16px (spacing-1x/2x) padding rhythm
  that is explicitly tokenized (--spacing-1x through --spacing-10x), which this spec
  reuses directly for the spacing scale.
  Two inverse button treatments exist (.button--primary as a light/outline style,
  .button--secondary as a solid dark style); role names below follow conventional UI
  meaning (primary = dominant solid CTA) rather than the site's literal class names,
  and this divergence is called out explicitly as inferred.

colors:
  primary: "#000000"
  ink: "#242424"
  canvas: "#ffffff"
  body: "#676767"
  muted: "#a8a8a8"
  hairline: "#e1e0e0"
  surface-soft: "#fcfaf6"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  sale: "#cc3314"
  success-green: "#67a98d"
  accent-gold: "#ebcb5a"
  info-blue: "#3b82f6"
  alert-red: "#af6a6a"
typography:
  display-xl: {fontFamily: "GT America, sans-serif", fontSize: 44.8px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  display-md: {fontFamily: "GT America, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "GT America, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "GT America, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "GT America, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "GT America, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "GT America, sans-serif", fontSize: 22.4px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
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
    padding: "{spacing.sm} {spacing.base}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineBottom: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    badgeSlot: "{components.badge}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
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
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.xs}"
  search:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  age-category-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.ink}"
    activeBorder: "1px solid {colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"

## Components

**button-primary** is the dominant solid CTA (e.g. "Shop collectie", add-to-cart), using ink-on-white contrast inverted to a solid dark fill per conventional primary-action styling; hover/active states are proposed to swap fill/text per the site's observed `.button--secondary:hover` inversion pattern.

**button-secondary** is an outlined, canvas-background variant for secondary actions (e.g. "Discover more"), matching the observed `.button--primary` light treatment; a dark hover fill is proposed, not directly observed in this excerpt.

**text-input** covers newsletter/email capture and account forms; border and radius are proposed from the shared 2px button radius and light-grey hairline token, since no dedicated input CSS was supplied.

**nav-bar** represents the persistent top navigation carrying locale/language selectors, "New / Baby / Kids / Adults / Cadeaus / Gray Label Club" links; background and hairline are inferred from base tokens since `.header` background-color was left empty in evidence.

**product-card** models the repeating grid items seen in the text excerpt (e.g. "Polo Dress € 78", "New Arrival" flag, size-swatch counts like "+3"); card surface and hairline border are proposed for visual separation, price and title typography are proposed body-scale values.

**hero** models the seasonal campaign banner ("Autumn Edit"/"Shop nieuw binnen") using the off-white surface token as a soft, editorial backdrop distinct from pure white product areas; large-scale display typography reuses the observed `.wysiwyg h1` values.

**footer** groups the extensive sitemap content (Over, Customer Service, Wholesale, Betaalmethoden, locale list) on an inverted dark background for visual closure; this inversion is proposed, not confirmed by the supplied `.header`-only background rule.

**badge** covers "New Arrival," "Runs Large," and "GL Exclusive" labels seen throughout the product feed; gold accent is proposed from the available `--color-orange` token as a plausible label tint, with actual badge colors unverified.

**search** is a proposed component for the site's implied search/discovery entry point; no dedicated search CSS was present in evidence, so styling mirrors the text-input pattern.

**age-category-filter** is a category-appropriate component for the Baby/Kids/Adults segmentation visible in the navigation and body copy, styled as a pill-shaped toggle group using the full-radius token and muted/ink text-state contrast; interaction states are proposed.

## Responsive Behavior

Recommended (not measured) breakpoints: mobile ≤ 480px, tablet 481–1024px, desktop ≥ 1025px. Below tablet, the nav-bar and age-category-filter are proposed to collapse into a hamburger/drawer pattern, and product-card grids reduce from a proposed 4-up to 2-up layout. Touch targets for button-primary/secondary and age-category-filter should maintain a minimum 44×44px hit area, achieved by combining `{spacing.sm}` vertical and `{spacing.base}` horizontal padding with the observed button font-size. This section is a general responsive recommendation only; no live breakpoint, resize, or mobile-menu behavior was observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS/text extraction only; no rendered layout, real viewport behavior, or interaction states (hover, focus, active, disabled) were directly observed beyond the two button classes' explicit hover rules. The `.header` background-color and root body `font-family` were both present as empty declarations in the supplied CSS, so canvas/nav background and the primary body font are inferred from adjacent tokens rather than confirmed. GT America is used as a proprietary custom font per evidence but its licensing, hosting, and full availability across weights were not verified. Badge, search, footer-inversion, and card-surface colors are proposed applications of the observed neutral/accent tokens rather than confirmed brand rules — the true product-card, badge, and footer color roles are unverified and should be treated as placeholders pending live-site inspection. All spacing and radius values not explicitly present in the supplied CSS tokens are proposed for internal consistency only.
