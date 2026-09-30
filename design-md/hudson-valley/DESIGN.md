---
version: alpha
name: "Hudson Valley"
source_url: "https://hvlgroup.com"
captured_at: "2026-09-29T04:07:33.725845+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from a lighting-industry storefront (Hudson Valley Lighting Group) whose extracted CSS is dominated by shared library defaults — jQuery UI widget styling and Bootstrap's CSS-variable scaffolding — rather than bespoke brand tokens. No first-party brand color or type declarations were present in the supplied evidence, so all semantic role assignments below are inferred from the observed palette and font stack, not confirmed brand identity.
  The palette centers on deep charcoal-navy neutrals (#253746, #16232e, #212529) against warm off-whites (#fdfaf3, #f5f4f3, #f8f9fa), which reads as a quiet, editorial backdrop appropriate for photographing decorative fixtures. A muted terracotta (#8d3f2d) is proposed as an accent, echoing warm metal/finish tones common in lighting catalogs, though it is not confirmed as a brand accent. Standard Bootstrap state colors (success, warning, danger, info) are carried through for form and utility feedback.
  Typography draws on GT Super for display moments (an inferred serif pairing for headline elegance) and GT Eesti for structural UI text, with Roboto proposed for body copy and Arial/Helvetica retained for native form controls, matching the jQuery UI evidence directly. Layout tokens (spacing, radius, breakpoints) are proposed conventions, not measured from the live site.

colors:
  primary: "#253746"
  ink: "#212529"
  body: "#343434"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  surface-warm: "#f5f4f3"
  on-primary: "#ffffff"
  accent: "#8d3f2d"
  success: "#1e6531"
  warning: "#ffc107"
  danger: "#eb4034"
  info: "#0dcaf0"
typography:
  display-xl: {fontFamily: "GT Super, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "GT Super, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "GT Eesti, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Roboto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Roboto, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "GT Eesti, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
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
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  finish-swatch-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    activeBorderColor: "{colors.primary}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs}"

## Components
**button-primary** is proposed as the core call-to-action treatment (e.g., "Add to Cart," "Shop All") using the dark charcoal-navy primary against white text, giving a confident, low-saturation contrast consistent with the observed neutral-dominant palette.

**button-secondary** offers an outlined variant for lower-priority actions like "View Details" or filter toggles, keeping the same ink color for text/border so it reads as a lighter-weight sibling to the primary button. States (hover, disabled) are not observed and are proposed only.

**text-input** covers search fields, quantity selectors, and account forms; it uses the light hairline border and card-white background seen in Bootstrap defaults, with body copy typography for legibility.

**nav-bar** represents the extensive mega-menu structure implied by the page text (Shop by Brand, Shop by Room, Architectural Lighting, etc.). A white background with hairline dividers is proposed to separate the many category groupings; actual collapse/hover behavior for this menu was not observed.

**product-card** is the fixture-listing unit (chandeliers, pendants, sconces) pairing a title in the mid-weight title typography with a smaller price line; card padding and hairline border are proposed to create visual separation across dense catalog grids.

**hero** proposes a warm off-white banner background (echoing tones like #fdfaf3/#f5f4f3 in the palette) for homepage features such as "Meet Schoolhouse" or seasonal collection launches, using the display-xl serif treatment for editorial weight.

**footer** is proposed in the dark primary color with white text, a common pattern for anchoring a content-heavy site with many brand/category links (Hudson Valley, Mitzi, Troy, Corbett, Schoolhouse, Sonneman, CSL).

**badge** supports small status flags like "New" or "Sale," using the terracotta accent color pulled from the palette as an inferred warm highlight against the neutral UI.

**search** models the header search affordance implied by "Track Order" and account navigation text, using the soft surface background for a recessed, low-contrast field.

**finish-swatch-selector** is a category-specific component for the "Swatches & Catalogs → Finishes" section, representing circular finish/color options (e.g., bronze, brass, nickel) with a primary-colored ring to indicate the active selection — a pattern common to lighting/hardware selection UI but not directly observed in the supplied CSS.

## Responsive Behavior
The following breakpoint table is a recommendation for a catalog-heavy lighting site and is not measured from live site behavior:

| Breakpoint | Width | Layout guidance |
|---|---|---|
| Mobile | <576px | Single-column product grid; nav collapses to a hamburger/off-canvas menu given the large mega-menu taxonomy observed in page text |
| Tablet | 576–991px | 2-column product grid; category mega-menu likely condenses to an accordion |
| Desktop | 992–1439px | 3–4 column product grid; full horizontal mega-nav |
| Wide | ≥1440px | 4+ column grid; increased hero and section padding ({spacing.section}) |

Touch targets should be a minimum 44px height for buttons and swatch selectors given the fine-grained finish/color choices implied by the "Finishes" swatch catalog. Mega-menu collapse behavior, hover states, and mobile drawer patterns are proposed conventions only, not confirmed interactions.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Static extraction returned no brand-authored color or typography declarations for hvlgroup.com; nearly all supplied CSS rules originate from jQuery UI and Bootstrap CSS-variable scaffolding, so every semantic color/type role above is inferred, not confirmed.
- Font stacks for GT Super and GT Eesti are asserted as observed family names only; actual weights, styles, and licensing/availability were not verified.
- No layout, spacing, or breakpoint values were present in the evidence; all spacing, radius, and responsive figures are proposed defaults for a lighting e-commerce catalog.
- No interaction states (hover, focus, active, disabled) or mobile/collapsed navigation behavior were observed; all such behavior is proposed.
- The extensive mega-menu taxonomy is known from page text only; its visual/interactive implementation was not present in the supplied CSS and is not described here as observed.
