---
version: alpha
name: "Pfister"
source_url: "https://pfisterfaucets.com"
captured_at: "2026-09-29T04:14:58.715010+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Pfister's public site presents a clean, utilitarian home-improvement retail interface built on a light neutral canvas (#ffffff, #f4f5f5, #fcfbfb) with dark charcoal body copy (#3d3d3c) and near-black icon accents (#222222). The only strongly brand-distinct hue observed in live component CSS is a warm red (#e24747) used for a modal-close glyph; this is treated here as the proposed primary accent for calls-to-action, since no other UI-applied brand color was captured. A secondary cluster of muted teal-gray tones (#0f8c98, #487d95, #8caeb7) and a cream/gold pairing (#f6e3c1, #ecc800) appear in the raw palette and are inferred to support collection imagery, seasonal promotions, or category badges rather than core chrome. A long tail of saturated reds, greens, blues, and oranges in the extracted palette matches standard Bootstrap alert/button defaults (#5cb85c, #337ab7, #d9534f, #f0ad4e, etc.) and is treated as inherited framework scaffolding, not confirmed brand identity — included for completeness but deprioritized in role assignment. Typography is anchored on Helvetica Neue/Helvetica/Arial with headings inheriting the same stack at weight 500; observed custom family names (Lato, Pfont, claire_hand-light/bold/regular) suggest a decorative script accent font family, whose actual application, weighting, and licensing are unverified. Layout, spacing, and radii below are proposed conventions consistent with a carousel-and-card e-commerce structure, not measured breakpoints.

colors:
  primary: "#e24747"
  ink: "#222222"
  canvas: "#ffffff"
  body: "#3d3d3c"
  muted: "#767271"
  hairline: "#cccccc"
  surface-soft: "#f4f5f5"
  surface-card: "#fcfbfb"
  on-primary: "#ffffff"
  accent-teal: "#0f8c98"
  accent-teal-muted: "#8caeb7"
  accent-blue-teal: "#487d95"
  accent-gold: "#ecc800"
  accent-cream: "#f6e3c1"
  accent-orange: "#ff5a00"
  border-strong: "#dddddd"
  overlay-dark: "#000000"
typography:
  display-xl: {fontFamily: "\"Helvetica Neue\", Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "\"Helvetica Neue\", Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: "0px"}
  title-md: {fontFamily: "\"Helvetica Neue\", Helvetica, Arial, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "\"Helvetica Neue\", Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.42857, letterSpacing: "0px"}
  body-sm: {fontFamily: "\"Helvetica Neue\", Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "0px"}
  caption: {fontFamily: "\"Helvetica Neue\", Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: "0.2px"}
  button-md: {fontFamily: "\"Helvetica Neue\", Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.2, letterSpacing: "0.5px"}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  collection-card:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.accent-gold}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xl}"
  hero:
    backgroundColor: "{colors.overlay-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    overlayOpacity: 0.25
    navButton:
      backgroundColor: "rgba(255,255,255,0.25)"
      borderColor: "rgba(255,255,255,0.5)"
      rounded: "{rounded.full}"
      size: "2.5rem"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-finder-module:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    description: |-
      A category-specific lookup panel (model-number / case-lookup style)
      pairing a text-input with a primary button, proposed for the
      "Buy Parts Online" and "Case Lookup" flows referenced in the
      navigation content; visual treatment is inferred, not observed.

## Components

**button-primary** is proposed as the site's chief conversion action (e.g. "Explore," "View Details," "Ask a Question"), using the red accent (#e24747) captured from a live close-icon rule as its fill, since no other applied CTA color was directly observed. **button-secondary** is an outlined, ink-on-transparent variant for lower-emphasis actions like "Learn more," inferred from typical retail pairing conventions rather than a captured selector. **text-input** covers search and model-number entry fields; border and radius values are proposed defaults matching the hairline gray already present in the palette. **nav-bar** models the mega-menu header implied by the Kitchen/Bathroom/Parts & Support structure in the page text; background and hairline are drawn from observed neutrals, but exact height, sticky behavior, and dropdown mechanics are not confirmed. **product-card** represents individual faucet/collection tiles (e.g. Winter Park, Colfax, Bruton) using the near-white card surface (#fcfbfb) against the light gray page background for subtle separation — a proposed pattern, not a measured shadow or border rule. **collection-card** is a category-appropriate module for the featured-collection blocks seen in the content (Ametrine, Tenet, Holliston), using the observed gold accent to suggest premium/award-badge styling ("Best of KBIS"). **hero** reflects the confirmed `.hero-image-rotator` carousel: translucent white circular nav buttons over a dark image overlay, matching the real CSS provided. **footer** and **badge** are proposed using the muted grays and teal accent respectively, since no footer-specific selectors were supplied. **search** mirrors the header's global search affordance implied by "Search / View All Matching Products." **spec-finder-module** is a category-relevant addition for plumbing hardware, addressing the site's model-lookup and pro-tools content; its styling is fully inferred.

## Responsive Behavior

| Breakpoint | Width       | Notes (proposed) |
|---|---|---|
| mobile     | < 576px     | Single-column stacks; nav collapses to a hamburger/off-canvas pattern; hero nav buttons enlarge for touch. |
| tablet     | 576–991px   | Two-column product grids; mega-menu likely condenses to accordion groups. |
| desktop    | 992–1199px  | Three/four-column product and collection grids; full mega-menu visible. |
| wide       | ≥ 1200px    | Max-width content container with generous section padding (`{spacing.section}`). |

Minimum touch targets are recommended at 44×44px for nav buttons and form controls. This table is a design recommendation only; no live responsive behavior, JavaScript breakpoints, or mobile menu interaction was observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is limited to static CSS/text extraction; no rendered screenshots, computed styles, or DOM hierarchy were available, so real component sizing, shadows, and spacing are unconfirmed.
- Primary accent selection (#e24747) rests on a single close-icon rule; the true CTA/brand color could differ and should be re-verified against live rendered buttons and hero banners.
- Many supplied hex values (e.g. #5cb85c, #337ab7, #d9534f, #f0ad4e, #dff0d8) match default Bootstrap alert/button colors and are likely inherited framework scaffolding rather than intentional brand palette — flagged, not used for primary roles.
- Custom font names (Lato, Pfont, claire_handlight/bold/regular) were found in font-family declarations but their actual visual usage, weight availability, and licensing/webfont delivery are unverified.
- Heading typography inherits `font-family: inherit` with only weight/line-height specified in CSS; the display/title font sizes above are proposed, not measured.
- No interaction states (hover/focus/active/disabled) beyond the hero nav button and its `:hover` rule were observed; all other component states are proposed.
- Mobile navigation collapse, menu accordion behavior, and product filtering UI were referenced only in page text, not in structural or interactive CSS.
