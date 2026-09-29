---
version: alpha
name: "Rick Steves"
source_url: "https://ricksteves.com"
captured_at: "2026-09-28T09:49:11.108859+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Rick Steves' Europe is a long-running travel-planning publisher and small-group tour operator with an integrated online store for guidebooks and travel accessories. The observed CSS shows a utilitarian, content-dense site: white canvas (#ffffff), near-black body copy (#252525), and a signature steel-blue (#005A84) used for headings, the mobile header bar, and tile hover states, paired with a brighter working blue (#007AA3) for tile backgrounds and tab states. A marigold-yellow (#FEBE11) appears as a 3px accent rule under h1 headings and the mobile header border, functioning as the brand's single strong accent against an otherwise restrained blue/gray/white system. Neutral grays (#f7f7f7, #eeeeee, #d1d1d1, #717171) support cards, dividers, and secondary text; muted status colors (#cc0000 error red, #165f2b/#20883e greens) appear in jQuery UI widget states and are inferred as reusable alert/success tokens rather than confirmed brand semantics. Typography is set in ProximaNova (Regular/Bold/Light) with Arial/helvetica/sans-serif fallbacks; Baskerville appears in the family list but its usage context is not evidenced, so it is treated as a possible editorial/serif accent only. This interpretation proposes a practical, information-first component system — tiles, tabs, and form widgets — matching the evidenced jQuery UI and tile-grid patterns, appropriate for a travel-accessories storefront layered onto a publishing site.

colors:
  primary: "#005a84"
  secondary: "#007aa3"
  accent: "#febe11"
  ink: "#252525"
  canvas: "#ffffff"
  body: "#252525"
  muted: "#717171"
  hairline: "#d1d1d1"
  surface-soft: "#f7f7f7"
  surface-card: "#f6f6f6"
  surface-info: "#e6f5fb"
  on-primary: "#ffffff"
  alert: "#cc0000"
  success: "#165f2b"
  warning: "#f39c12"
typography:
  display-xl: {fontFamily: "ProximaNova-Bold, arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "ProximaNova-Bold, arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "ProximaNova-Bold, arial, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "ProximaNova-Regular, helvetica, arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "ProximaNova-Regular, helvetica, arial, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  caption: {fontFamily: "ProximaNova-Light, arial, sans-serif", fontSize: 13px, fontWeight: 300, lineHeight: 1.3, letterSpacing: 0.1px}
  button-md: {fontFamily: "ProximaNova-Bold, arial, sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.25px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    borderBottom: "3px solid {colors.accent}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  content-tile:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    hoverBackgroundColor: "{colors.primary}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} 3.125%"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentRule: "3px solid {colors.accent}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    hairline: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components
**button-primary** is proposed for primary calls to action ("Shop Now," "Add to Cart") using the steel-blue #005A84 seen driving headings and tile hover states, with white text for contrast; hover/active/disabled states are proposed, not observed.

**button-secondary** offers an outlined alternative for secondary actions (e.g., "View Details"), reusing primary blue as border/text on a white field to stay within the observed two-blue palette without introducing new hues.

**text-input** follows the light hairline-bordered pattern (#d1d1d1) seen in jQuery UI widget borders, applied here to search boxes and form fields; focus-ring styling is proposed and not evidenced.

**nav-bar** is grounded directly in the `#mobile-header` rule: steel-blue background, white text, and a 3px marigold bottom border — the clearest observed navigation treatment in the evidence, extended here to a general nav bar pattern.

**content-tile** generalizes the evidenced `.regular-tile`/`.map-tile`/`.video-tile`/`.product-tile` pattern: a semi-opaque `#007AA3` info panel over imagery with white tile-title text, darkening to `#005A84` on hover/active per the transition rule — a strong candidate for a travel-accessories product grid.

**hero** is inferred: a soft-neutral background with the same marigold accent rule used under h1, scaled up for a landing banner; no hero-specific CSS was supplied, so layout and copy hierarchy are proposed.

**footer** is proposed using the light gray card surface and muted gray text for secondary link columns, consistent with the site's dense-links footer content noted in the page text (About Us, Travel Help, Media Partners, etc.).

**badge** is proposed for small status labels (e.g., "New," "Sale") using the accent yellow with dark text for legibility, rounded fully; no badge component was directly observed.

**search** reuses the text-input treatment for a site search field, referenced in the page's "Go!" search prompt; exact styling is not evidenced and is proposed for consistency.

**product-card** is proposed for the travel-accessories storefront, combining the observed card border/background neutrals with title/body typography tokens; no dedicated product-card CSS was present in the supplied evidence.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| Mobile | 320–599px | Single-column tiles, `#mobile-header` pattern applies, min-width:320px is the only observed floor |
| Tablet | 600–959px | Two-column tile grid, nav collapses to a header bar |
| Desktop | 960px+ | Multi-column tile/product grid, full nav visible |

Touch targets are proposed at a minimum 44×44px for buttons and tile links. Navigation collapse (hamburger vs. full menu) is proposed, not confirmed by supplied CSS, which only shows a fixed-height `#mobile-header` without documented breakpoint media queries.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is static CSS/text extraction only; no rendered layout, interaction states, or real breakpoints were observed.
- Color roles (muted, surface-card, alert, success, warning) are inferred from jQuery UI widget usage and general neutrals, not confirmed brand-semantic assignments.
- Baskerville's usage context is unknown; it may be editorial/serif content rather than a UI font, so it is excluded from primary typography tokens.
- Font sizes beyond the h1 `2em` rule and body `1em`/`1.5em` line-height are proposed estimates, not directly measured.
- Rounded and spacing scales are conventional proposals; no border-radius or spacing-scale values were present in the supplied CSS rules.
- Component states (hover/focus/active/disabled) beyond the documented tile hover transition are proposed, not observed.
- Custom font (ProximaNova) availability, licensing, and self-hosting status were not verified from the supplied evidence.
