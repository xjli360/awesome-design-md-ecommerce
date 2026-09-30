---
version: alpha
name: "Sennheiser"
source_url: "https://www.sennheiser.com"
captured_at: "2026-09-29T04:26:43.172502+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from Sennheiser's Next.js CSS bundle, which exposes a compact
  design-token system built on pure black and white with a signature "sennheiser-blue"
  (#0096d6) accent and a petrol tone (#003746) for deeper brand moments. Hover/active states
  use documented blues (#037cc2, #35a0d8) and neutrals (#262626, #454545). Text and surface
  roles reference light/very-light greys (#ececf0, #f4f4f6) and an error red (#c20000). The
  broader supplied palette includes many additional hues (e.g. #c1001b, #967000, #12ca0a)
  that appear to belong to category, badge, or chart contexts; only colors with clear
  structural roles in the CSS (buttons, backgrounds, text) are mapped to primary semantic
  slots here, and the rest are retained as available accents. Typography is the proprietary
  SennheiserNeue family with a system sans-serif fallback stack, plus a separate
  sennheiserMonoFont referenced in the bundle for monospaced/technical text; no other
  monospace or serif faces were observed. The interpretation favors a clean, high-contrast
  black/white product-catalog layout with a pill-shaped primary button, thin hairlines, and
  restrained blue accents for links and interactive states, appropriate for a technical audio
  and microphone storefront. Layout, spacing rhythm, and responsive breakpoints below are
  proposed, not measured.

colors:
  primary: "#0096d6"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#545252"
  hairline: "#ececf0"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  petrol: "#003746"
  hover-blue: "#037cc2"
  active-blue: "#35a0d8"
  hover-black: "#262626"
  active-black: "#454545"
  grey-on-dark: "#999999"
  disabled-grey: "#adadad"
  error-red: "#c20000"
  accent-red: "#c1001b"
  accent-green: "#00ae00"
  accent-gold: "#d9a300"
typography:
  display-xl: {fontFamily: "SennheiserNeue, sennheiserFont, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "SennheiserNeue, sennheiserFont, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "SennheiserNeue, sennheiserFont, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "SennheiserNeue, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.75, letterSpacing: 0px}
  body-sm: {fontFamily: "SennheiserNeue, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "sennheiserMonoFont, SennheiserNeue, monospace", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.2px}
  button-md: {fontFamily: "SennheiserNeue, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif", fontSize: 10.4px, fontWeight: 500, lineHeight: 1.07692, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    hover: "proposed: color shifts toward {colors.hover-black}, per observed .button:hover rule"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
    focusBorder: "proposed: 1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: "94px (observed --header-height token)"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    shadow: "proposed: none by default, subtle elevation on hover"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    overlay: "proposed: dark scrim using {colors.petrol} for legibility over imagery"
    ctaButton: "button-primary or button.blur variant"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.grey-on-dark}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairline: "proposed: 1px {colors.active-black} divider between columns"
  badge:
    backgroundColor: "{colors.error-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    iconColor: "{colors.muted}"
  microphone-spec-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    divider: "1px solid {colors.hairline}"
    description: "proposed: technical spec table/list pattern for microphone frequency response, polar pattern, and connector data"

## Components
**button-primary** is a black pill-shaped button with white text, matching the observed `.button` rule (border-radius 50rem, dark fill, inline-flex layout); hover state is proposed to darken per the observed `button:hover` color token. **button-secondary** reuses the observed `.button.secondary` pairing of very-light-grey background with black text, for lower-emphasis actions like "Learn more." **text-input** is a proposed pattern since no form-field CSS was supplied; it uses the hairline grey border and sennheiser-blue focus ring inferred from the `accent-color` token. **nav-bar** reflects the one measured layout constant, `--header-height:94px`, with a white background and black wordmark/link text; sub-menu chevrons observed in the text excerpt suggest a mega-menu, but its visual styling is not in the CSS evidence. **product-card** is a proposed grid-tile pattern sized for the observed featured-product carousel ("HD 490 PRO," "e 835," etc.), using an 8px card radius and hairline border since no card-specific CSS was supplied. **hero** is proposed for the homepage banner ("Build the ultimate guitar rig," "AMBEO Spatial Audio") using black background and white display type, with `.button.blur` as an optional translucent CTA per the observed blur-button rule. **footer** matches the site's dense link-column structure (About us, Support, Information, Stay informed) with proposed dark styling and grey-on-dark secondary text. **badge** is proposed for "new" or sale flags using the observed error-red as a high-visibility accent. **search** is a proposed pill search field styled consistently with the button radius language. **microphone-spec-panel** is a category-specific proposed component for presenting technical microphone specifications (polar pattern, frequency response, connector type) in a structured label/value list, using caption typography for labels.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Nav | Product grid |
|---|---|---|---|
| Mobile | <600px | Collapsed hamburger, single-column | 1 column |
| Tablet | 600–1024px | Condensed horizontal nav | 2 columns |
| Desktop | 1024–1440px | Full mega-menu, 94px header | 3–4 columns |
| Wide | >1440px | Full mega-menu, max-width container | 4+ columns |

Touch targets are recommended at a minimum 44×44px for nav and button elements; the observed pill-button padding (`1rem .9rem .9rem`) should scale comfortably to this minimum. Mobile nav collapse and mega-menu-to-accordion behavior are proposed conventions, not observed interactions.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from a static CSS bundle and a text excerpt, not a rendered or interactive session, so hover/focus/active states beyond the explicitly supplied `:hover` rules are proposed. Layout structure (grid columns, card composition, hero sizing, footer column count) is inferred from the page-text outline of homepage modules, not from measured DOM or breakpoint CSS. Many palette entries (e.g. golds, greens, reds beyond error-red) appear in the supplied color list without a confirmed CSS role and are treated as available secondary/status accents rather than assigned primary roles. Font rendering of "SennheiserNeue" and "sennheiserMonoFont" is proprietary and self-hosted per the bundle reference; actual glyph availability, weights, and licensing terms were not verified beyond the family names appearing in `font-family` declarations. All spacing, radius, and typography scale values beyond the observed button padding and header height are proposed defaults for a technical audio product catalog, not extracted measurements.
