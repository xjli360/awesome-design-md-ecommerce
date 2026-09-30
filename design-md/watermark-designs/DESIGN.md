---
version: alpha
name: "Watermark Designs"
source_url: "https://watermark-designs.com"
captured_at: "2026-09-28T04:49:57.610439+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The observed palette centers on a muted charcoal body tone (#58575a) against
  white canvas, with a desaturated teal-green (#0e977d) and a steel blue
  (#1b6f9f) used as the two button background colors in the supplied CSS.
  Headings (h1-h3) are set in "Leitura Display Roman," a serif display face,
  while body copy uses a "Leitura News Roman 1" stack falling back through
  Helvetica, Roboto, and Arial. A search input specifically calls "Dia
  Regular." A font token literally read as "Lato #000" appeared on the
  primary .button selector; because this string is not a resolvable font
  family (likely a CSS build artifact concatenating a font name with a hex
  color), it is treated as unreliable and not cited as a typography value
  anywhere in this spec — button typography instead inherits the observed
  body stack, which is a documented fallback behavior (button,input {
  font-family: inherit }) in the supplied rules.
  Given the brand's Brooklyn-manufactured, architect-collaborated luxury
  fixture positioning, this interpretation favors restrained neutrals,
  generous whitespace, sharp (unrounded) edges matching the observed
  border-radius:0 on buttons, and a light, material-forward surface palette
  (#f4f5f6, #e6e6e6) suited to product photography and finish/metal swatches.
  Secondary blue and additional accent colors are reused sparingly for
  interactive and informational states. All semantic role assignments
  (ink, muted, hairline, surface tiers) are inferred from usage context, not
  labeled as such in source CSS.

colors:
  primary: "#0e977d"
  secondary: "#1b6f9f"
  ink: "#3e3d41"
  body: "#58575a"
  muted: "#838287"
  hairline: "#dddddd"
  surface-soft: "#f4f5f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"
  canvas: "#ffffff"
typography:
  display-xl: {fontFamily: "Leitura Display Roman, serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Leitura Display Roman, serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Leitura Display Roman, serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Leitura News Roman 1, Helvetica, Roboto, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Leitura News Roman 1, Helvetica, Roboto, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Leitura News Roman 1, Helvetica, Roboto, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Leitura News Roman 1, Helvetica, Roboto, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1, letterSpacing: 0.5px}
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
    padding: "{spacing.lg} {spacing.base}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg} {spacing.base}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.body}"
    border: "none"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    hairline: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    titleColor: "{colors.on-primary}"
    bodyColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    iconColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.base}"
    typography: "{typography.body-sm}"
  finish-swatch:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    labelColor: "{colors.body}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs}"

## Components

**button-primary** uses the observed `.button` background (#0e977d) with white text and the CSS-confirmed sharp corners (`border-radius:0`) and `.875rem` font size; padding is scaled from the observed `1.572em 1.5em` proportions. Hover/active states are proposed, not observed.

**button-secondary** reuses the `.button.secondary` background-color (#1b6f9f) directly from the supplied CSS, keeping identical typography and shape rules as the primary button for visual consistency across dual-CTA sections such as the hero.

**text-input** is modeled on the header search field, which sets a light gray background (#f4f5f6), no border, and placeholder color matching body text (#58575a); this is extended here to general form inputs as an inferred, brand-consistent pattern.

**nav-bar** reflects the header's white-theme text handling, where `.header-theme--white` variants render brand slogan, search button, and other elements in white over a presumably transparent/dark-image top state, and in dark ink once scrolled. Exact scroll-triggered behavior is inferred from class naming, not directly observed in layout.

**product-card** is a proposed pattern for collection and product listing grids (e.g., Heritage/Watermark Collection tiles), using card-surface white, a hairline border, and the display-family title paired with muted body copy — consistent with a catalog-heavy, image-forward site structure implied by the extensive collection/product taxonomy in the text.

**hero** derives its dark background from `.hero-container .button.button--special` (#3e3d41) and the white hero title/paragraph color rule, giving a dark-overlay hero banner treatment typical of full-bleed lifestyle photography headers.

**footer** is proposed using the same ink tone as the hero for brand consistency, given the footer's dense sitemap-style link list (Collections, Products, Dealer Locator, About, etc.) suggested by the page text, though the actual footer background color was not directly isolated in the supplied CSS.

**search** wraps the documented `.header-search` styles directly: light surface, borderless input, and an icon-button whose color inherits from context, matching the described header search affordance.

**finish-swatch** is a category-appropriate addition for a luxury plumbing-fixture brand that markets extensive finish/plating options (e.g., "Polished Pearl Gold," "Satin Pearl Gold"); it proposes a small circular chip with a hairline border and caption-level label, since no literal swatch markup was present in the supplied CSS.

## Responsive Behavior

| Breakpoint | Width    | Notes (proposed) |
|-----------|----------|-------------------|
| small     | 0em      | Single-column nav, collapsed hamburger menu |
| medium    | 40em     | Two-column product grids begin |
| large     | 64em     | Full horizontal nav, three-column grids |
| xlarge    | 75em     | Wider hero and catalog imagery |
| xxlarge   | 90em     | Max-width content container |

These breakpoint values are taken from a CSS custom property string (`small=0em&medium=40em&large=64em&xlarge=75em&xxlarge=90em`) found in the source, but their actual application to layout, grid columns, and component collapse was not observed and is proposed here as standard Foundation-style breakpoint usage. Touch targets for buttons should be no smaller than 44px in height; the off-canvas menu variables (`--mm-ocd-width`, `--mm-spn-item-height:50px`) suggest a slide-out mobile navigation drawer is implemented, though its visual styling was not captured in the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.



- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This spec is derived solely from a static CSS/text snapshot; no rendered screenshots, computed styles, or interaction states (hover, focus, active, disabled) were observed. Heading font sizes, line-heights beyond the base body rule, and most spacing/padding values outside the `.button` rule are proposed estimates, not measured values. The `.button` font-family token literally read "Lato #000" in the source data; this was judged unreliable (not a valid, resolvable font family) and excluded from all typography definitions in favor of the documented `font-family:inherit` fallback and the observed body stack. Font availability and licensing for "Leitura Display Roman," "Leitura News Roman 1," and "Dia Regular" were not verified — these are proprietary-sounding names with no confirmed public CDN or license source in the supplied evidence. Mobile navigation, off-canvas drawer visuals, footer layout, and exact product-card/grid markup were not present in the supplied CSS and are inferred from page-text structure only.
