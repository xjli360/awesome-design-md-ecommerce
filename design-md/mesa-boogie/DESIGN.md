---
version: alpha
name: "Mesa Boogie"
source_url: "https://www.mesaboogie.com"
captured_at: "2026-09-28T09:02:55.231342+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation reflects Mesa/Boogie's amplifier and cabinet storefront as
  presented within the Gibson brand family's commerce shell. The observed palette
  is dominated by high-contrast neutrals — pure black and white, a near-black
  foreground token (#121212) used at reduced opacity for body copy, and a family
  of greys (#707070, #e7e7e7, #cccccc, #f2f2f2) for hairlines and soft surfaces.
  A muted antique-gold (#86764e, with a near-duplicate #877648) is the only
  chromatic accent evidenced in CSS variables (--tw-color-gold) and a background
  gradient, and is treated here as the brand primary. A secondary gradient stop
  (#d6d0c2) supports warm surface tinting. Payment-badge colors (e.g. PayPal blue,
  Mastercard red/orange) are excluded from brand roles as they belong to
  third-party marks, not brand identity.
  Two font families are observed: Inter Tight (a grotesque sans, used for UI and
  body text) and League Gothic (a condensed display face) paired with a
  sans-serif fallback stack. League Gothic is inferred for large display/heading
  moments given its condensed, poster-like character suited to amp/cabinet
  product presentation; this role assignment is not confirmed by layout
  screenshots. Buttons use a fully rounded (pill) shape per the observed
  border-radius token. Overall the interpretation favors a stark, high-contrast,
  gear-catalog aesthetic with gold as a restrained premium accent.

colors:
  primary: "#86764e"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#707070"
  muted: "#999999"
  hairline: "#e7e7e7"
  surface-soft: "#f7f8f9"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  accent-warm: "#d6d0c2"
  contrast-black: "#000000"
  border-strong: "#cccccc"
  surface-dark: "#191919"
typography:
  display-xl: {fontFamily: "League Gothic, sans-serif", fontSize: 64px, fontWeight: 600, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "League Gothic, sans-serif", fontSize: 40px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.25px}
  title-md: {fontFamily: "Inter Tight, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Inter Tight, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.8, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter Tight, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "Inter Tight, sans-serif", fontSize: 11px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Inter Tight, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.contrast-black}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.contrast-black}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.border-strong}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base} {spacing.xl}"
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.contrast-black}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  spec-sheet:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"

## Components

**button-primary** is a solid black, fully pill-shaped call-to-action ("Shop Now") matching the observed `--tw-color-black` background and semibold weight from `.btn` rules; hover/active states use opacity/mix darkening, proposed here as a subtle `color-mix` darken consistent with the CSS's own hover treatment.

**button-secondary** inverts to a white fill with a black label and a light border, for lower-emphasis actions like "Learn More," reusing the same pill radius for visual consistency across the button family.

**text-input** is a plain-bordered field using the light hairline grey, intended for search or account forms; corner radius is modest (sm) to contrast with the pill buttons, a proposed distinction not confirmed in the CSS.

**nav-bar** represents the top utility/mega-menu bar implied by the extensive nested menu text (Amplifiers, Cabinets, Tone Tools, Discover); a bottom hairline separates it from page content, and it is proposed as a white bar with dark text for legibility over product photography.

**product-card** models the catalog tiles seen in the text excerpt (amp head/combo listings with price pairs); a soft grey card surface and thin hairline border give products visual separation on the light canvas without introducing new colors.

**hero** reflects the homepage banner pattern ("Accept No Imitations," "Triple Threat") using the documented gradient-background tokens as a soft canvas, with large condensed display type for impact, per League Gothic's inferred display role.

**footer** is proposed as a dark surface (using the darkest observed grey, #191919) with white text, giving the amp-brand a heavier, gear-catalog close to the page; this darkness level is inferred, not measured from the supplied CSS.

**badge** is a small gold pill for tags like "New" or "Exclusive," which appear repeatedly in the product excerpt; gold is reused from the primary token rather than introducing a separate accent.

**spec-sheet** is a category-specific component proposed for amplifier/cabinet technical specs (wattage, tube complement, speaker configuration) common to this product type; it borrows the card surface and hairline border for consistency with product-card.

## Responsive Behavior

Proposed breakpoints (not measured from live site):

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | < 640px | Single-column product grid, collapsed mega-menu into a drawer/accordion |
| Tablet | 640–1024px | Two-column product grid, nav condenses to icon + hamburger |
| Desktop | 1024–1440px | Full mega-menu with nested category flyouts as implied by menu text |
| Wide | > 1440px | Max-width container, extra horizontal padding per `--container-space-x` variants (1.25rem / 3.125rem observed) |

Touch targets for buttons and nav items are recommended at a minimum 44×44px hit area. The mega-menu's deep nesting (Amplifiers → Heads/Combos/Bass, Cabinets → Boogie/Rectifier/Bass sub-groups) should collapse into a multi-level accordion on mobile rather than a hover flyout. This section is a recommendation only; no responsive/mobile layout was observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS variables, class declarations, and page text only — no rendered screenshots, computed layout, or interaction states were observed. Semantic role mapping (e.g., gold as "primary," League Gothic as "display") is inferred from variable naming and typographic character, not confirmed usage on specific elements. Font availability, licensing, and whether League Gothic is a licensed/custom asset were not verified. All font sizes, line-heights, spacing scale values, and rounded-corner steps beyond the button pill radius are proposed defaults, not measured. Hover/active/disabled button states are approximated from partial CSS rules (`color-mix` darkening) and may not reflect final rendered behavior. Mobile menu collapse behavior, breakpoint values, and touch-target sizing are proposed UX conventions, not observed from the source. The near-duplicate gold hexes (#86764e, #877648, #86764b) suggest minor inconsistency in the source design tokens; a single representative value was chosen for the primary role.
