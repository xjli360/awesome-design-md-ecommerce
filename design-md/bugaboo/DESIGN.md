---
version: alpha
name: "Bugaboo"
source_url: "https://bugaboo.com"
captured_at: "2026-09-28T04:22:09.233612+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Bugaboo's storefront CSS points to a restrained, monochrome-led palette anchored by a near-black
  (#0f0f02) used for primary buttons and loading states, set against white and warm off-white
  surfaces (#f2f1ef, #fafaf7, #eeeeee). Text and disabled states draw from a muted stone gray
  (#93938d) and mid gray (#4a4a44), while a light gray (#d8d8d8) marks hairlines and disabled
  button fills. The custom "AeonikPro" typeface (falling back to Helvetica Neue/Arial/sans-serif)
  drives interface text, with a confirmed button style of 14px/500-weight/1.35 line-height and
  100px pill radius. Beyond this neutral core, the extracted palette contains scattered saturated
  hues (greens, reds, ambers, blues) that appear to belong to messaging, badges, or seasonal
  campaign accents rather than the primary brand system; here they are mapped conservatively to
  semantic roles (success, error, warning, info) as an inferred convention, not a confirmed design
  token set. Layout structure (grids, breakpoints, header heights) is inferred from CSS custom
  properties, not from direct visual inspection. This interpretation favors a quiet, premium
  neutral base with restrained color accents suited to a considered parenting/lifestyle product
  brand.

colors:
  primary: "#0f0f02"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#4a4a44"
  muted: "#93938d"
  hairline: "#d8d8d8"
  surface-soft: "#f2f1ef"
  surface-card: "#fafaf7"
  on-primary: "#ffffff"
  divider-soft: "#eeeeee"
  disabled-bg: "#d8d8d8"
  accent-success: "#0f956a"
  accent-error: "#cc0000"
  accent-warning: "#fab855"
  accent-info: "#4f99ff"
typography:
  display-xl: {fontFamily: "AeonikPro, Helvetica Neue, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "AeonikPro, Helvetica Neue, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "AeonikPro, Helvetica Neue, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "AeonikPro, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "AeonikPro, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "AeonikPro, Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "AeonikPro, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.35, letterSpacing: 0.16px}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    height: "64px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.divider-soft}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
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
    dividerColor: "{colors.body}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  stroller-configurator-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    labelTypography: "{typography.caption}"
    optionTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"

## Components
**button-primary**: The near-black pill button (100px radius, confirmed in CSS) is the core call-to-action, used for "Add to cart" or "Shop now" actions; disabled state is directly observed as a light-gray fill (#d8d8d8) with muted text.

**button-secondary**: Proposed outline variant using the same ink color as a border on a white field, for lower-emphasis actions like "Learn more," inferred from the primary button's structure but not directly observed.

**text-input**: Proposed form field styling for account, newsletter, and checkout inputs, using the observed hairline gray for borders and muted gray for placeholder text, consistent with the site's neutral disabled/muted tone.

**nav-bar**: Inferred from the `--header-offset-height` custom properties (54px, 64px, 128px observed across breakpoints), suggesting a fixed or sticky header that resizes; exact content and behavior not observed.

**product-card**: Proposed pattern for stroller/accessory listings, pairing a warm off-white card surface with title, price, and a caption-level muted label, styled after the observed `.dynamic-price-button__label` treatment.

**hero**: Proposed full-width banner using the soft off-white surface and large display type for homepage/category storytelling; no hero markup or imagery was present in the supplied evidence.

**footer**: Proposed dark ink-on-white-text footer for site-wide navigation and legal links, inverting the primary button palette; not confirmed from extracted CSS.

**badge**: Proposed small pill label (e.g., "New," "Bestseller," "In Stock") using the observed green accent (#0f956a) as a confirmed-in-palette but inferred-in-role success color.

**search**: Proposed pill-shaped search field echoing the button radius convention, for product/site search; interaction states not observed.

**stroller-configurator-card**: A category-specific proposed component for color/fabric or bundle selection common to stroller PDPs, using the primary ink as a selected-state border; entirely inferred from product-category convention, not from supplied CSS.

## Responsive Behavior
This is a recommendation based on inferred conventions and the observed `--container-width` (1440px) and `--header-offset-height` variants (54px, 64px, 128px), not measured live site behavior.

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | <768px | Single-column stacking, header ~54–64px, collapsed hamburger nav |
| Tablet | 768–1023px | Two-column grids begin, header ~64px |
| Desktop | 1024–1439px | Full nav visible, multi-column product grids |
| Wide | ≥1440px | Content capped at `--container-width:1440px`, larger header (~128px) |

Touch targets should be at minimum 44x44px for buttons and nav items; the pill button and search patterns should collapse to icon-only or full-width variants on mobile. Navigation is assumed to collapse into a toggle/hamburger pattern given the repeated "Toggle navigation" text in the page title metadata, though the exact mobile menu structure was not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS and metadata extraction only; no live rendering, DOM inspection, or interaction testing was performed. Breakpoint values are inferred from CSS custom-property redefinitions of `--header-offset-height` and `--container-width`, not from confirmed `@media` ranges. Many palette colors (greens, reds, ambers, blues) appear only in isolated rules and their semantic roles (success/error/warning/info) are inferred from common convention, not confirmed usage. Hover, focus-visible, and loading-state styles exist in CSS (e.g., `.c-button.is--loading`) but their visual/motion behavior was not directly observed. Mobile menu structure, hero content, footer layout, and product-card markup are proposed patterns, not extracted layouts. The "AeonikPro" font's licensing, availability, and full weight range are not verified; fallback stacks are provided for resilience. All typography sizes beyond the confirmed button style (14px/500/1.35) are proposed, not measured.
