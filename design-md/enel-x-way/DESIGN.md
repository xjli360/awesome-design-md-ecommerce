---
version: alpha
name: "Enel X Way"
source_url: "https://enelxway.com"
captured_at: "2026-09-28T04:59:31.041332+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Evidence from Enel X Way's compiled stylesheet shows a Bootstrap-derived
  design system layered with a proprietary "Roobert ENEL" font family
  (declared via multiple weight-specific faces: Black, Bold, Light,
  Regular, with italics) and a standard system-font fallback stack
  (-apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans).
  The CSS custom properties expose an electric-blue primary (#3a16ff),
  a neutral gray secondary (#6c757d), and Bootstrap-style state colors
  (success green #2afd95, info cyan #2cfef9, warning yellow #fef367,
  danger/red #ff006e) alongside a magenta accent (#ef2ac1) and a
  slate dark (#313b49) with light-blue-gray (#c2cddd). Base document
  color is #212529 on a #ffffff canvas, consistent with default
  Bootstrap body styling.
  This interpretation proposes reusing #3a16ff as the primary brand
  and CTA color, #212529 for ink/body text, and #f7f7f7/#eff2f7 as
  soft and card surfaces — these surface assignments are inferred,
  not directly observed as component backgrounds. Hairline borders
  are inferred from the shared Bootstrap gray #dee2e6. Rounded
  corners follow the observed .btn border-radius of .25rem (4px).
  Typography scale sizes below .btn/body defaults are proposed, not
  measured.

colors:
  primary: "#3a16ff"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#212529"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f7f7f7"
  surface-card: "#eff2f7"
  on-primary: "#ffffff"
  secondary: "#6c757d"
  accent-magenta: "#ef2ac1"
  accent-red: "#ff006e"
  accent-green: "#2afd95"
  accent-cyan: "#2cfef9"
  dark: "#313b49"
  light: "#c2cddd"
  warning: "#fef367"
typography:
  display-xl: {fontFamily: "Roobert ENEL, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Roobert ENEL, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Roobert ENEL, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Roobert ENEL, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.5, letterSpacing: 0px}
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    hairline: "{colors.hairline}"
    headerBackground: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** uses the observed brand blue (#3a16ff, the CSS `--primary` token) as its fill with white text, matching the site's default Bootstrap `.btn` shape (0.25rem radius, confirmed in evidence) but with brand-specific padding proposed for a charging-accessory storefront's CTAs such as "Shop Chargers" or "Check Compatibility."

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Learn More"), reusing the primary blue for border and text on a transparent field so it sits quietly beside primary CTAs without new color introduction.

**text-input** is inferred for account, address, and configurator forms; it uses the neutral Bootstrap hairline gray (#dee2e6) for its border, since no explicit input styling was present in the extracted rules.

**nav-bar** is proposed as a white bar with dark ink text and a hairline bottom border, consistent with the light canvas/dark-text pairing shown in the `body` rule; actual navigation markup and behavior were not present in the evidence.

**product-card** (proposed) covers charger/cable/accessory listings, using a very light card surface (#eff2f7) distinct from pure white to create subtle separation in a grid, with a hairline border and medium rounding.

**hero** is proposed as a dark, high-contrast band (#313b49) for homepage/category banners, since Enel X Way's palette includes several saturated accent colors (green, cyan, magenta) that would read best against a dark ground; this is a stylistic proposal, not an observed hero layout.

**footer** reuses the same dark tone as hero for brand consistency across top and bottom of page, an inferred pairing rather than a confirmed pattern.

**badge** is proposed for status labels (e.g., "In Stock," "Fast Charging") using the success green from the CSS custom properties, pill-shaped per the `rounded.full` token.

**search** is a proposed pill-shaped input for product/site search, using the soft gray surface color to visually recede from primary content.

**spec-table** is a category-appropriate component for EV charger technical specifications (amperage, cable length, connector type), using alternating hairline dividers consistent with the observed `.table-striped`/`.table-hover` Bootstrap rules, though exact table styling on this domain was not directly inspected.

## Responsive Behavior

This is a recommended breakpoint structure informed by the `--breakpoint-*` custom properties found in the stylesheet, not measured rendering:

| Token | Width | Notes |
|---|---|---|
| xxs | 280px | proposed, matches `--breakpoint-xxs` |
| xs | 320px | proposed, matches `--breakpoint-xs` |
| sm | 360px | proposed, matches `--breakpoint-sm` |
| s | 576px | proposed, matches `--breakpoint-s` |
| md | 768px | proposed, matches `--breakpoint-md` |
| lg | 1024–1025px | proposed, matches `--breakpoint-lg-new`/`--breakpoint-lg` |
| xl | 1200px | proposed, matches `--breakpoint-xl` |
| xxl | 1440px | proposed, matches `--breakpoint-xxl` |

Nav should collapse to a hamburger/drawer pattern below `md`; product-card grids should reduce from multi-column to single-column below `s`. Touch targets should be at least 44×44px on buttons and search fields. This table is a recommendation derived from custom-property names, not an observed layout.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was limited to a compiled clientlib CSS bundle and a minimal page-text excerpt; no rendered screenshots, DOM structure, or component markup were available.
- Font role assignments (e.g., "Roobert ENEL" for headings vs. system stack for body) are inferred from font-face naming conventions, not confirmed usage on specific elements.
- Custom font ("Roobert ENEL," "digitalecosystem") availability, license terms, and self-hosting rights were not verified.
- All font sizes above the observed `body { font-size:1rem }` and `.btn` declarations (16px/.25rem radius) are proposed, not measured.
- Semantic color roles (surface-soft, surface-card, hairline) are inferred from generic Bootstrap gray values present in the palette, not from confirmed component-specific CSS.
- No interaction states (hover, focus, active, disabled), animation behavior, or mobile/tablet layout were observed; only static desktop-oriented CSS declarations were supplied.
- Breakpoint table is derived from CSS custom-property names only; actual responsive behavior was not tested.
