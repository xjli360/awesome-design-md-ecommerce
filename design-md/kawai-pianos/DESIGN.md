---
version: alpha
name: "Kawai Pianos"
source_url: "https://www.kawai-global.com"
captured_at: "2026-09-28T05:07:58.168474+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from Kawai Musical Instruments Manufacturing's
  global corporate site, which lists Digital Pianos among its product
  categories. The only confirmed brand color is a saturated red
  (#e11922/#e11923, with close variants #d6121b/#d60e17) used for header
  accents and interactive states on mobile; the base palette is otherwise
  neutral, built from white, near-black body text (#323232), and a family of
  light grays (#f2f2f2, #e6e6e6, #e0dfdf, #dbdbdb, #cccccc, #c8c8c8, #d3d0ca)
  used for panels, hover states, and dividers. The single confirmed typeface
  is Source Sans Pro with Calibri and sans-serif fallbacks, applied globally
  to body copy.

  Because no heading, card, or hero styling was present in the supplied CSS,
  this design proposes a restrained editorial system: red is reserved as a
  focal accent (primary CTAs, active nav, badges) rather than a dominant
  brand color, gray surfaces organize content density, and generous
  whitespace supports imagery of acoustic and digital instruments. Sizing,
  spacing, radii, and most component states below are inferred/proposed to
  extend the minimal confirmed evidence into a usable system, not observed
  layout.

colors:
  primary: "#e11922"
  accent: "#d6121b"
  ink: "#323232"
  canvas: "#ffffff"
  body: "#323232"
  muted: "#646464"
  hairline: "#dbdbdb"
  surface-soft: "#f2f2f2"
  surface-card: "#e6e6e6"
  divider: "#e0dfdf"
  border: "#cccccc"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "'Source Sans Pro', Calibri, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Source Sans Pro', Calibri, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Source Sans Pro', Calibri, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Source Sans Pro', Calibri, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Source Sans Pro', Calibri, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Source Sans Pro', Calibri, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Source Sans Pro', Calibri, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "transparent"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    activeIndicatorColor: "{colors.primary}"
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    overlayColor: "{colors.accent}"
    titleTypography: "{typography.display-xl}"
    ctaComponent: "button-primary"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    hoverColor: "{colors.hairline}"
    padding: "{spacing.none} {spacing.lg}"
    typography: "{typography.body-md}"
  spec-comparison-table:
    backgroundColor: "{colors.canvas}"
    rowAltBackground: "{colors.surface-soft}"
    hairlineColor: "{colors.divider}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.body-sm}"
    cellTypography: "{typography.body-sm}"

## Components

**button-primary** carries the site's one confirmed brand color as a solid red fill, used for primary calls to action such as "Find a Dealer" or "Explore Digital Pianos." Hover/active states are proposed, not observed.

**button-secondary** is an outlined variant reusing the same red for text and border on a transparent field, intended for lower-emphasis actions like "Compare Models." State transitions are proposed.

**text-input** mirrors the confirmed search input pattern: a flat light-gray fill with no border and zero corner radius, matching the explicit `border-radius: 0` rule observed in the header search field.

**nav-bar** proposes a white bar with dark ink text and a hairline underline, with the confirmed red reserved for the active link indicator, consistent with the red mobile header band seen in evidence.

**product-card** is inferred for listing grand, upright, digital, and hybrid piano models, using the light-gray surface tone as a card background against the white canvas to create subtle separation without borders.

**hero** proposes a full-width introductory banner using the white canvas with dark text, reserving the red accent for a single CTA or thin overlay bar, appropriate for showcasing instrument photography.

**footer** is inferred as a plain white footer with muted gray text for legal links (Privacy Policy, Disclaimer), separated from body content by a light hairline.

**badge** proposes a small red pill label for tags like "New" or competition announcements, reusing the primary/on-primary pairing already confirmed in header contexts.

**search** formalizes the observed header search box: gray fill, no visible border, square corners, with a confirmed hover-darkening behavior on its button (`#dbdbdb`).

**spec-comparison-table** is a category-specific proposal for digital piano spec sheets (keys, polyphony, sound engine), using alternating light-gray rows and thin dividers to support scanability, styled consistently with the neutral gray system observed elsewhere.

## Responsive Behavior

This is a recommended breakpoint structure, not measured site behavior:

| Breakpoint | Width       | Notes                                      |
|-----------|-------------|---------------------------------------------|
| mobile    | ≤480px      | Single column; nav collapses to hamburger  |
| tablet    | 481–1024px  | Two-column product grids; search full-width|
| desktop   | 1025px+     | Multi-column layout; persistent top nav    |

Touch targets should be at least 44px, matching the mobile search input height already observed (44px). Navigation is expected to collapse behind a menu toggle on narrow viewports, consistent with the mobile "close" control present in evidence, though its expanded/collapsed visual states were not captured.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from static CSS/text extraction only; no rendered layout, real breakpoints, or interaction states (hover, focus, active, disabled) were directly observed beyond the two hover/focus rules present in the evidence. Font sizes, weights, letter-spacing, spacing scale, and radii (aside from the confirmed `border-radius: 0` on inputs) are proposed extrapolations, not measured values. Semantic color roles (primary vs. accent, ink vs. body) are inferred groupings of a small confirmed palette and may not match Kawai's actual brand guidelines. Component definitions for hero, product-card, footer, badge, and spec-comparison-table are proposed patterns suited to a piano manufacturer's digital catalog, not verified site elements. Availability and licensing of Source Sans Pro for production use were not verified against Kawai's actual font-serving or licensing setup.
