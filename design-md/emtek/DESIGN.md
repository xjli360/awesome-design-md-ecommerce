---
version: alpha
name: "Emtek"
source_url: "https://emtek.com"
captured_at: "2026-09-28T04:20:54.933537+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Emtek's interface evidence points to a hardware brand built on warm,
  material-inspired neutrals rather than a saturated brand color. The
  observed palette centers on a brass/gold tone (#dbc598, used as the
  default button background) paired with a deep slate-teal (#1a4456,
  the footer background) and a muted stone gray (#697278) used for
  disabled and secondary states. White (#ffffff) and near-white grays
  (#f4f4f4, #e6e9eb) carry the canvas and card surfaces, while
  #b9bdc1 defines input borders. A small red (#922525) exists as a
  CSS custom property and is treated here as an inferred alert/error
  color, since no error-state usage was captured. Typography is
  explicitly declared: Lato as the base body font and Ophian as a
  secondary display/button font, both with sans-serif fallbacks;
  heading weight is observed at 300 (light), and button type is
  observed as uppercase with 0.07em letter-spacing at 14px. Because
  this is a hardware and finishes catalog, the design interpretation
  extends the observed brass/stone/teal palette into a finish-forward
  visual language: light, tactile surfaces, restrained typography, and
  a single warm accent color doing most of the interactive work.

colors:
  primary: "#dbc598"
  primary-hover: "#e2d1ad"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#6d706e"
  muted: "#697278"
  hairline: "#b9bdc1"
  surface-soft: "#f4f4f4"
  surface-card: "#e6e9eb"
  on-primary: "#000000"
  accent-deep: "#1a4456"
  accent-brass: "#8c734c"
  danger: "#922525"
  border-strong: "#a9a9a9"
typography:
  display-xl: {fontFamily: "Ophian, sans-serif", fontSize: 48px, fontWeight: 300, lineHeight: 1.15, letterSpacing: -0.5px}
  display-md: {fontFamily: "Ophian, sans-serif", fontSize: 32px, fontWeight: 300, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Lato, sans-serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Lato, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5em, letterSpacing: 0px}
  body-sm: {fontFamily: "Lato, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5em, letterSpacing: 0px}
  caption: {fontFamily: "Lato, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4em, letterSpacing: 0.02em}
  button-md: {fontFamily: "Ophian, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4em, letterSpacing: 0.07em}
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
    hoverBackgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "11px 30px"
  button-secondary:
    backgroundColor: "transparent"
    borderColor: "{colors.ink}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "11px 30px"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.accent-deep}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.accent-deep}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  finish-swatch:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-strong}"
    activeBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    size: "40px"

## Components

**button-primary** is styled directly from observed CSS: a brass-gold
fill (#dbc598), black text, uppercase Ophian type at 14px with wide
letter-spacing, and an observed hover state lightening to #e2d1ad. A
disabled state (background #e6e9eb, text #697278) is also directly
observed in the stylesheet.

**button-secondary** is proposed as an outline variant using the same
button typography, since only the filled/primary and disabled variants
were captured in evidence; the outline treatment is inferred to give
the UI a lower-emphasis action.

**text-input** uses the explicitly observed border color token
(`--text-input-border-color:#b9bdc1`) and a white background, matching
`--main-nav--search-input-background-color`. Focus and error states are
proposed, not observed.

**nav-bar** is inferred as a light, white-background bar with hairline
dividers, based on the search-input variables scoped to `main-nav`;
exact spacing and collapse behavior were not captured.

**product-card** is proposed for the catalog/finish-browsing context
implied by the page title ("Cabinet and Door Hardware, designed by
you"), using the light card surface (#e6e9eb) observed among the
flexihero color tokens.

**hero** maps to the `--flexihero-*` custom properties, which define a
dark teal/black text pairing (#1a4456 as `color1`) alongside light-mode
text (#fff) and dark-mode text (#000); the hero component here uses the
teal as an inferred full-bleed background with light text.

**footer** uses the explicitly observed `--footer-nav--bg-color:#1a4456`
with white primary and secondary text colors, directly matching
`--footer-nav--color-primary`/`--footer-nav--color-secondary`.

**badge**, **search**, and **finish-swatch** are proposed, category-
appropriate components: badges for stock/finish labeling, a search
affordance consistent with the observed search-input tokens, and a
circular finish-swatch selector suited to a hardware/finish-configurator
product, using the brass primary as an inferred "selected" indicator.

## Responsive Behavior

This is a recommendation based on common patterns for catalog/e-commerce
layouts, not measured site behavior:

| Breakpoint | Width       | Notes                                   |
|------------|-------------|------------------------------------------|
| sm         | 0–599px     | Single column, nav collapses to menu icon |
| md         | 600–959px   | 2-column product grid                    |
| lg         | 960–1279px  | 3-column grid, full nav visible          |
| xl         | 1280px+     | 4-column grid, max-width container       |

Touch targets should be at least 44×44px for buttons and swatches.
Navigation search and menu are assumed to collapse into an icon-driven
overlay below `md`, consistent with common patterns for this category,
but this has not been observed directly.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS extraction only; no rendered
page, breakpoint behavior, or interaction states (hover/focus/active
beyond the two observed button states) were verified. Color-role
assignments beyond the directly named CSS variables (`--color-red`,
`--footer-nav--bg-color`, `--text-input-border-color`, button
background/hover/disabled) are inferred from token naming patterns
(e.g., `--flexihero-color1..10`) and general layout convention, not
confirmed visual placement. Font availability and licensing for
"Ophian" were not verified — it is used here strictly because it
appears in the site's CSS custom property `--font-secondary`. All
component paddings, breakpoints, and the finish-swatch pattern are
proposed design recommendations, not measurements of the live site.
