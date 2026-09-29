---
version: alpha
name: "Ruffwear"
source_url: "https://ruffwear.com"
captured_at: "2026-09-28T09:17:20.725822+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Ruffwear's observed palette centers on a deep navy (#00263e), explicitly
  declared as the button background color in the site's review-widget CSS
  variables, paired with a warm gold/amber (#f2a900) used as the hover and
  active state accent. Surrounding neutrals range from near-black navy
  (#0e1f2c) through mid grays (#6a6d6e, #84898c) to soft off-white surfaces
  (#f7f9fa, #ebeef0), suggesting an outdoor-technical, trail-worn aesthetic
  rather than a soft pet-boutique look. A wider secondary palette of oranges
  (#e08823, #d97b1e), reds (#cd0a0a, #9d2e24), teals (#00aea9, #0b5258), and
  olives (#7e7e3e, #868a3a) appears tied to product color-variant swatches
  (e.g. Blaze Orange, River Rock Green, Basalt Gray) rather than core UI
  chrome; these are treated as inferred accent/utility colors, reused
  sparingly for badges and status states.

  Typography evidence includes the custom family "niveau-grotsek" alongside
  system stacks (Geist, Open Sans, Verdana/Arial fallbacks) and the default
  browser sans-serif chain. This interpretation assigns niveau-grotsek to
  display/heading roles and Open Sans/Geist to body and UI text, both
  inferred pairings since no direct heading-to-body CSS rule was supplied.
  Buttons use a fully rounded pill (5rem radius) per the observed
  --oke-button-borderRadius token, extended here as the primary button
  shape across the system.

colors:
  primary: "#00263e"
  ink: "#0e1f2c"
  canvas: "#ffffff"
  body: "#303030"
  muted: "#6a6d6e"
  hairline: "#cfd4d8"
  surface-soft: "#f7f9fa"
  surface-card: "#ebeef0"
  on-primary: "#ffffff"
  accent: "#f2a900"
  accent-strong: "#e08823"
  error: "#cd0a0a"
  warning: "#eaa22e"
  teal: "#00aea9"
  coral: "#f58765"
  border-strong: "#abb0b4"
typography:
  display-xl: {fontFamily: "niveau-grotsek, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "niveau-grotsek, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Geist, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Geist, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.3px}
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
    hover:
      backgroundColor: "{colors.accent}"
      textColor: "{colors.primary}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    hover:
      backgroundColor: "{colors.surface-soft}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    focus:
      border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    hairline: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch:
    size: "{spacing.lg}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.border-strong}"
    selectedBorder: "2px solid {colors.primary}"

## Components

**button-primary** is the dominant call-to-action, modeled directly on the
observed `--oke-button-*` CSS variables: navy fill, white text, a fully
rounded (5rem) pill shape, and a gold hover/active swap. This mapping is
directly evidenced by the review-widget theme tokens and extended here as
the site-wide primary button.

**button-secondary** is a proposed outline variant for lower-emphasis
actions (e.g. "Learn More"), reusing the primary navy for border/text with
a soft-surface hover fill; no outline button was directly observed, so this
pattern is inferred from the primary button's shape language.

**text-input** proposes a light, bordered field using the observed
hairline gray (#cfd4d8) and canvas white, with a navy focus ring — the
focus state color is inferred from the primary brand color, not measured.

**nav-bar** is inferred as a white top bar with navy text and a hairline
bottom border, consistent with the deep multi-level menu structure evident
in the page text (Shop, Collections, Stories, Search, Cart), though exact
nav layout/height was not observed.

**product-card** reflects the repeating product-grid pattern implied by the
page text (harness/coat listings with names, star ratings, and prices),
using the light gray surface-card background and a hairline border; card
elevation/shadow was not observed and is omitted.

**hero** proposes a full-navy banner treatment for seasonal campaign
messaging (e.g. "Fully Vested," "Fall/Winter '26 Collection") referenced in
the text, using display-xl type on white — the specific hero layout and
imagery were not observed.

**footer** mirrors the primary navy with white text for the extensive
footer link groups (About, Learn More, Pro Purchase, Store Locator)
implied by the page text; column structure is proposed, not measured.

**badge** supports rating/discount callouts such as "UP TO 30% off" and
star-rating chips seen in the text, using the gold accent for visibility
against both light and dark surfaces.

**search** is a proposed light input treatment for the site's search
overlay (referenced via "Search suggestions" in the page text), styled
consistently with text-input but slightly more compact.

**color-swatch** is a category-specific component addressing Ruffwear's
per-product color-variant lists (Blaze Orange, River Rock Green, Basalt
Gray, etc.); rendered as small rounded swatches with a navy selected-state
ring, since swatch colors are unique per product and cannot be fixed to a
single token set.

## Responsive Behavior

Recommended, not measured, breakpoint table:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–599px | Single-column product grid, collapsed hamburger nav, sticky search icon |
| tablet | 600–1023px | 2-column product grid, condensed top nav |
| desktop | 1024–1439px | 3–4 column grid, full mega-menu nav |
| wide | 1440px+ | Max-width content container, generous section spacing |

Touch targets should be at least 44px in height for primary buttons and
color swatches. Navigation is expected to collapse into a slide-in drawer
below tablet width, consistent with the "Left Arrow / Close icon" menu
markers present in the page text, though the actual collapse behavior and
animation were not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS extraction and page text only;
no rendered layout, computed styles, or JavaScript-driven states were
observed. The primary/accent color mapping is grounded in explicit
`--oke-button-*` variables, but broader UI role assignments (ink, muted,
surface-soft/card) are inferred by proximity and typical usage patterns,
not confirmed against live components. Typography pairing of
niveau-grotsek to display and Geist/Open Sans to body text is inferred;
actual heading/body CSS rules were not supplied. All font availability and
licensing (particularly niveau-grotsek, a possible custom/licensed
typeface) are unverified. Spacing, rounded, and responsive breakpoint
values are proposed conventions, not measured from the site. Mobile menu
behavior, hero imagery, and product-grid column counts are inferred from
page text only and were not visually confirmed.
