---
version: alpha
name: "Orange Amps"
source_url: "https://www.orangeamps.com"
captured_at: "2026-09-28T09:14:50.741242+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  The evidence shows a high-contrast, functional Shopify storefront built on a
  near-black-on-white foundation (#272727 on #ffffff) with a single saturated
  brand accent, #f57e20, reused across the review-star widget, form focus
  states, and the primary CTA affordance. Supporting neutrals (#f1f1f1,
  #f8f8f8, #eeeeee, #dedede, #cccccc, #e3e3e3, #7b7b7b) form a restrained
  card/surface/hairline system typical of a product-catalog site. A cluster of
  blues (#1773b0, #1990c6, #136f99) appears only in Shopify's accelerated
  checkout button and is treated here as a secondary/link accent rather than
  brand identity. A warm cream (#fff1e3) and dark brown (#412d00) pairing is
  also present in the raw palette and is mapped, as an inferred role, to a
  soft warm surface/ink pair for editorial or promo content. Typography is
  built entirely from the observed font stack: SofiaSans-Bold is inferred as
  the heading family (uppercase, bold, tracked headings match its character),
  Lato/Lato-Bold/Lato-Black cover UI and body text, and Calisto MT is retained
  as an available serif for incidental long-form or legal copy. JudgemeStar is
  a review-icon glyph font, not prose. No live layout, spacing, or breakpoint
  behavior was observed; all structural values below are proposed.

colors:
  primary: "#f57e20"
  ink: "#272727"
  canvas: "#ffffff"
  body: "#272727"
  muted: "#7b7b7b"
  hairline: "#dedede"
  surface-soft: "#f8f8f8"
  surface-card: "#f1f1f1"
  on-primary: "#f1f1f1"
  ink-strong: "#000000"
  border-subtle: "#e3e3e3"
  neutral-200: "#eeeeee"
  neutral-300: "#cccccc"
  link: "#1773b0"
  link-hover: "#136f99"
  accent-blue: "#334fb4"
  surface-warm: "#fff1e3"
  ink-warm: "#412d00"
typography:
  display-xl: {fontFamily: "SofiaSans-Bold, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "SofiaSans-Bold, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "SofiaSans-Bold, sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.96px}
  body-md: {fontFamily: "Lato, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0.96px}
  body-sm: {fontFamily: "Lato, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.3px}
  caption: {fontFamily: "Lato, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "Lato-Bold, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-subtle}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink-strong}"
    textColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    rounded: "{rounded.none}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-comparison-table:
    backgroundColor: "{colors.surface-soft}"
    headerBackgroundColor: "{colors.ink}"
    headerTextColor: "{colors.on-primary}"
    rowHairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components
**button-primary** uses the confirmed brand orange (#f57e20) with the observed
button-text color (#f1f1f1) and a square corner (buttons observed with
`border-radius: var(--buttons-radius-outset)`, which the evidence does not
resolve to a nonzero value, so `none` is used as the safer default).
**button-secondary** proposes an outline treatment against white, reusing ink
for both text and border, appropriate for "Learn more" or comparison actions
common on amp/cabinet product pages. **text-input** is a proposed form field
style built from the neutral hairline and surface tokens; no focus-ring color
was directly observed beyond the generic `--focused-base-outline` using
foreground at 50% alpha, so hover/focus states are proposed, not measured.
**nav-bar** is inferred from the grid-based `body` layout (`grid-template-rows:
auto auto 1fr auto`) which implies a stacked header region; exact nav styling
is not observed. **product-card** derives padding and radius conventions from
the `.product-card-wrapper .card` custom-property scaffold (corner radius,
border width, shadow, image padding all wired to CSS variables whose resolved
values were not supplied), so the concrete radius/shadow here is proposed.
**hero** is a proposed full-bleed banner pattern suited to amp-head/cabinet
imagery, using ink-strong as a dramatic dark background consistent with the
brand's amp-panel aesthetic; this is an interpretive choice, not an observed
section. **footer** reuses the ink/on-primary pair already confirmed in the
root button tokens. **badge** mirrors the observed judge.me review-badge
variables (`--jdgm-border-radius: 0`, primary color #f57e20), generalized into
a reusable label component for "New," "In Stock," or series tags. **search**
is a proposed pattern with no direct selector evidence. **spec-comparison-table**
is a category-appropriate proposed component for amp/cabinet wattage, valve
type, and speaker-size comparisons, styled from the same neutral/hairline
system as the rest of the interface; no table markup was present in the
supplied evidence.

## Responsive Behavior
Recommended, not measured:
| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–599px | single-column product grid, nav collapses to a toggled menu |
| tablet | 600–959px | two-column product grid, condensed nav |
| desktop | 960–1279px | full nav bar, three/four-column product grid |
| wide | 1280px+ | max content width aligned to `--max-width-xl` (100rem) observed in base.css |

Touch targets should be a minimum 44px hit area for nav and cart controls;
the mega-menu structure implied by the "Products / Play / Listen / Wear /
About / Artists / Support" text should collapse into an accordion on mobile.
This table is a design recommendation only; no actual responsive CSS or
media-query breakpoints were included in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is built from static CSS custom properties and a text
excerpt only; no rendered page, computed styles, or DOM screenshots were
available. The mapping of SofiaSans-Bold to heading roles is inferred from
the uppercase/bold heading rule and the presence of that family in the font
list, not from a direct `--font-heading-family` value. Actual `--buttons-radius-outset`,
`--product-card-corner-radius`, and other CSS custom-property values referenced
in base.css were not resolved in the supplied evidence, so radius and shadow
values on buttons/cards are proposed defaults. The blue palette (#1773b0,
#1990c6, #136f99, #334fb4) is confirmed only for a third-party Shopify
checkout widget, not core brand UI, and its broader use here is an inferred
extension. The cream/brown pair (#fff1e3, #412d00) has no confirmed role and
is speculative. No interaction states (hover, focus, active, disabled), mobile
navigation behavior, or breakpoint values were observed. Licensing and
availability of Calisto MT, Lato weights, and SofiaSans-Bold for production
use were not verified.
