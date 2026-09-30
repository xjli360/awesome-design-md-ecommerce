---
version: alpha
name: "TOTO"
source_url: "https://totousa.com"
captured_at: "2026-09-29T04:06:53.182056+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from TOTO USA's homepage stylesheet, which sets a white canvas
  (#ffffff) and black body copy (#000) in a quoted "gotham" family falling back to Arial and
  sans-serif, at a spacious 16px/1.8 line-height typical of long-form product and technology copy.
  A cool institutional blue (#005da8), reinforced with a darker `--blue` custom property
  (#13449d), is used for content links styled bold, uppercase, and underline-free — this is
  treated here as the primary brand action color. Accordion and toggle controls show a
  uppercase, 700-weight treatment on a white background with thin gray dividers, suggesting a
  clinical, engineered aesthetic appropriate to plumbing fixtures. Grays (#f4f4f4, #dddddd,
  #6e6e6e) supply soft surfaces, hairlines, and secondary text. A small accent set — teal
  (#44b0ac), orange (#e46c2f), and alert red (#cf2020) — appears in the wider palette and is
  mapped here as optional status/highlight colors, not confirmed as core brand accents. Heading
  fonts (Montserrat, Lato) are present in the evidence as loaded families but their applied
  role is inferred, not directly observed on headline elements. The overall interpretation
  favors a restrained, technical-luxury tone: bright white surfaces, precise blue calls-to-
  action, and uppercase structural labels.

colors:
  primary: "#005da8"
  secondary: "#13449d"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6e6e6e"
  hairline: "#dddddd"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#44b0ac"
  accent-orange: "#e46c2f"
  alert: "#cf2020"
  focus-ring: "#5897fb"
typography:
  display-xl: {fontFamily: "Montserrat, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "gotham, Arial, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "gotham, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.8, letterSpacing: 0px}
  body-sm: {fontFamily: "gotham, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "gotham, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.2px}
  button-md: {fontFamily: "gotham, Arial, sans-serif", fontSize: 18px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
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
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  showroom-locator-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** — Solid blue call-to-action (e.g., "Shop Now," "Explore") on white canvas, using the observed link blue as fill and white text, matching the bold uppercase treatment seen on content links. Hover/active states are proposed, not observed.

**button-secondary** — Outlined variant for lower-emphasis actions ("See Product," "View All") pairing the same primary blue as text and border on a white fill, preserving the brand's uppercase button convention inferred from accordion-title styling.

**text-input** — A bordered field using the hairline gray for its outline and near-white surface, sized for form use (warranty registration, contact forms) referenced in the site's Support navigation; states such as focus/error are proposed.

**nav-bar** — A white, hairline-bottomed bar hosting the mega-menu structure evidenced by the extensive product taxonomy (NEOREST, WASHLET, Toilets, Faucets, etc.); dropdown chevrons and multi-level flyouts are proposed patterns to accommodate the observed menu depth.

**product-card** — A white card with a thin hairline border, product title in title-md, and short descriptive copy in body-sm; intended for grids of toilets, faucets, and lavatories referenced throughout the product catalog text. Hover elevation is proposed, not measured.

**hero** — A full-width banner region using a soft surface background and display-xl headline typography, matching the homepage's rotating carousel content (e.g., "Aurora," "NEOREST Collection"); slide dot controls follow the observed `.slick-dots` pattern with an orange focus state from the CSS evidence.

**footer** — A dark, ink-colored band with white text at body-sm scale, intended to house global/regional links, legal text, and site-map style navigation consistent with the multi-region "Global Network" list found in the page content.

**badge** — A small pill using the teal accent for callouts such as "Award-Winning" or "Top Pick," referencing the homepage's award and press-mention copy; exact badge usage on-site is inferred.

**search** — A rounded, soft-surface search field matching the "Begin typing to search" prompt text, styled with generous horizontal padding for a pill-shaped input; keyboard/typeahead behavior is proposed, not observed.

**showroom-locator-card** — A category-appropriate card for "Find A Showroom" / "View Online Retailers" flows referenced in the Where to Buy menu, combining a bordered card, primary-blue accent, and compact title/body typography suited to location or retailer listings.

## Responsive Behavior

_Recommendation only — no responsive/mobile layout was directly observed in the supplied evidence._

| Breakpoint | Width        | Notes (proposed) |
|-----------|--------------|-------------------|
| xs        | <480px       | Single-column stacks; nav collapses to a hamburger/menu icon per the "Open menu / Close menu" labels seen in page text. |
| sm        | 480–767px    | Two-column product grids; hero copy narrows, CTA buttons full-width. |
| md        | 768–1023px   | Three-column product grids; mega-menu flyouts may remain collapsed behind a toggle. |
| lg        | 1024–1439px  | Full mega-navigation visible; four-column product grids. |
| xl        | ≥1440px      | Max-width content container with increased whitespace at section spacing. |

Touch targets should be at least 44×44px for nav and button components. The mega-menu's deep category structure (NEOREST, WASHLET, WASHLET+, Toilets, Faucets, Shower & Bath, Lavatories, Commercial) implies an accordion-style collapse on mobile, consistent with the `.Accordion` button pattern found in the CSS, but this collapse behavior was not directly measured.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This document is derived from static CSS/text extraction only; no rendered layout, computed spacing, or breakpoint behavior was measured.
- Semantic color roles (primary vs. secondary blue, accent teal/orange, alert red) are inferred from limited selector context and may not reflect TOTO's actual brand guidelines.
- Typography sizes beyond the observed body (16px/1.8) and content-link (~18px bold uppercase) values are proposed for scale consistency, not measured from rendered headings.
- Heading font-family assignment (Montserrat/Lato) is inferred from the font-families list; no CSS rule tying these families to headline elements was supplied.
- Interaction states (hover, focus, active, disabled) for buttons, inputs, and cards are proposed conventions, not observed, aside from the documented `.slick-dots` orange focus state.
- Mobile/responsive navigation collapse behavior is inferred from menu-toggle text labels, not from observed media queries.
- Licensing/availability of the "gotham" font family for production use was not verified; fallback to Arial/sans-serif is assumed necessary.
