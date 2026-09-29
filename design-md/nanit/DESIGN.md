---
version: alpha
name: "Nanit"
source_url: "https://nanit.com"
captured_at: "2026-09-28T09:21:42.403432+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Nanit's storefront evidence shows a deep navy foundation (#000041, #111d41) paired
  with a warm off-white canvas (#fbfbf6) and cream surface (#faf7f3), reflecting a
  calm, nursery-appropriate palette rather than a clinical tech aesthetic. The
  observed hero CTA uses a muted slate-blue (#334874) with a darker hover state
  (#233251), which this spec treats as the primary action color; cream (#faf7f3)
  is the confirmed on-primary text color from that same button rule. A soft gold
  (#f5de9e / #f0cd6e) appears in the palette and is inferred here as an optional
  accent for badges or highlight chips, not confirmed as a CTA color. Borders use
  a light gray (#e5e7eb) seen on a promo-banner rule, adopted as the hairline
  token. Typography exposes two custom family tokens: a heading family (declared
  with a serif fallback, matched here to "Cotford Light") and a body family
  (sans-serif fallback, matched to "Neue Plak"), with Inter present in the CSS as
  a likely UI/system font for inputs or search. All pixel sizes, weights, spacing
  scale, and radii below are proposed conventions for a monitor/tech commerce
  site and are explicitly labeled inferred, since no computed layout metrics were
  supplied.

colors:
  primary: "#334874"
  primary-hover: "#233251"
  ink: "#000041"
  canvas: "#fbfbf6"
  body: "#111d41"
  muted: "#666666"
  hairline: "#e5e7eb"
  surface-soft: "#faf7f3"
  surface-card: "#f4f3ef"
  on-primary: "#faf7f3"
  accent-gold: "#f0cd6e"
  accent-gold-soft: "#f5de9e"
  border-subtle: "#dedede"
  neutral-gray: "#9ca3af"
typography:
  display-xl: {fontFamily: "Cotford Light, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Cotford Light, serif", fontSize: 34px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Cotford Light, serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Neue Plak, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Neue Plak, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Inter, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Neue Plak, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
    hairlineColor: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    borderColor: "{colors.border-subtle}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-gold-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  plan-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    accentColor: "{colors.accent-gold}"

## Components

**button-primary** reflects the confirmed hero CTA rule, using the slate-blue fill (#334874) with cream text (#faf7f3); the darker hover state (#233251) is directly observed in the CSS and should be preserved on interaction states.

**button-secondary** is a proposed outline variant using the same primary blue for border and text on a transparent background, matching typical paired-CTA patterns seen alongside the primary button in the hero slide markup; hover fill-to-primary behavior is inferred from the `.btn-fill` rule but not fully specified.

**text-input** is a proposed pattern for account, search, and checkout fields, using the light canvas background and the observed hairline gray border; no input-specific CSS was supplied, so padding and radius are conventions.

**nav-bar** is inferred from the site's header section variables (cream/transparent background, navy foreground) and the extensive nav label list in the page text (Shop, Features, Resources); exact height, sticky behavior, and dropdown styling were not observed.

**product-card** is proposed for the Smart Baby Monitor, Breathing Wear, and bundle listings referenced in the text (e.g., "Smart Baby Monitor System From $289.99"); card surface and border use neutral palette tokens since no dedicated product-tile CSS was in evidence.

**hero** models the slideshow/banner region referenced by "Pause slideshow / Play slideshow" and the hero button selectors; background and display typography are proposed, while the button colors within it are directly observed.

**footer** is a proposed dark-navy footer using the ink color as background, inverted for legibility; no footer-specific selectors were supplied, so structure and link styling are conventions only.

**badge** is proposed for promotional labels like "SAVE 15%" and "HSA/FSA Eligible," using the soft gold accent color present in the palette as a plausible highlight tone, not confirmed against a badge selector.

**search** mirrors the site's visible search affordance ("Search Nanit," "Clear") using canvas/hairline tokens consistent with the input pattern; no distinct search-bar CSS was captured.

**plan-card** is a category-appropriate addition for the Nanit Insights membership/FAQ content (Sleep Plan, trial messaging), using a soft card surface with a gold accent to differentiate subscription tiers; this component is entirely proposed since no membership-page CSS was in the evidence set.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width       | Layout notes (proposed)                          |
|-----------|-------------|---------------------------------------------------|
| mobile    | <480px      | Single-column stack, nav collapses to menu icon   |
| tablet    | 480–1024px  | 2-column product grids, condensed hero copy        |
| desktop   | 1024–1280px | Multi-column grids, full nav bar visible           |
| wide      | >1280px     | Content capped near the `--page-width` token seen in CSS custom properties |

Touch targets should be at least 44×44px for cart, nav, and quantity controls. Navigation and search are assumed to collapse into an icon-triggered overlay below tablet width. None of this was directly observed in rendered markup or media queries.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Static CSS/text extraction only; no rendered DOM, computed styles, or real breakpoints were available.
- Actual pixel values for `--sp-9`, `--sp-12`, `--sp-14`, and `--page-width` custom properties were not resolved from evidence.
- Semantic role assignment for `#334874` as "primary" and `#f5de9e`/`#f0cd6e` as "accent" is inferred from limited button/promo context, not a full style guide.
- Heading font "Cotford Light" and body font "Neue Plak" are named in evidence but their license, loading method, and true visual weight/style were not verified.
- Interaction states beyond the one observed hover rule (primary button) are proposed, not confirmed.
- Mobile/tablet layout, grid columns, and menu collapse behavior were not observed and are conventional recommendations only.
- Spacing and radius scales are proposed design-system defaults, not extracted from measured layout.
