---
version: alpha
name: "Fatso"
source_url: "https://eatfatso.com"
captured_at: "2026-09-28T09:10:47.529839+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Fatso's public CSS shows a plain, utilitarian WordPress/Divi foundation rather
  than a heavily custom brand skin. The confirmed rules set body copy in Open
  Sans over Arial/sans-serif fallbacks at 14px, weight 500, with a generous
  1.7em line-height, colored a soft #666 gray on a white canvas. Headings
  (#333) share the body's line-height reset but no distinct heading font was
  present in the supplied rules, so heading typography is treated as inferred
  continuity of Open Sans rather than a confirmed separate display face.
  Interactive accents (link/hover states, the password-form submit color) use
  a single confirmed blue, #2ea3f2, which is adopted here as the primary
  action color. The Divi default button background (#32373c) and its white
  text are preserved as an available dark/secondary button pattern. Beyond
  these confirmed values, the supplied palette is dominated by the WordPress
  core color-picker defaults (oranges, purples, greens, reds), which are
  documented but not claimed as brand-authored; two non-default, distinctive
  hues — a pink (#f35198) and a soft teal (#7ebec5) — are carried forward as
  inferred flavor/accent colors suited to a playful, Canadian-made nut-butter
  brand, given the product line's Classic/Salted Caramel/Maple/Cinnamon
  variety and community-driven tone.

colors:
  primary: "#2ea3f2"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#666666"
  muted: "#999999"
  hairline: "#dddddd"
  surface-soft: "#f3f3f3"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent-pink: "#f35198"
  accent-teal: "#7ebec5"
  surface-dark: "#32373c"
typography:
  display-xl: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.7, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 13px, fontWeight: 500, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.5, letterSpacing: 0.2px}
  button-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.7, letterSpacing: 0px}
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
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "2px solid {colors.surface-dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    height: "72px"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent-teal}"
    display: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    hairline: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    iconColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    accentColor: "{colors.accent-teal}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components
**button-primary** uses the confirmed interactive blue (#2ea3f2) as its fill with white text, matching the observed button-md sizing (20px/500/1.7 line-height) pulled directly from the `.et_pb_button` rule. Hover/focus darkening is proposed, not observed.

**button-secondary** reuses the Divi-default dark slate (#32373c) background with white text, mirroring the `.wp-element-button` rule found in the theme's root styles; intended for lower-emphasis or footer-context actions.

**text-input** is a proposed pattern: white fill, hairline border, and body-md typography, since no explicit form-field CSS was present in the supplied evidence beyond generic `button,input,select,textarea{font-family:inherit}`.

**nav-bar** is inferred as a light, white-canvas bar with ink-colored labels and a hairline underline; the site text implies primary nav items (Our Products, Find Fatso, About, Community, FAQ, Contact) but no header CSS block was supplied, so layout and height are proposed.

**hero** is proposed as a full-bleed light section using display-xl for the "WE'VE STUFFED SO MUCH GOODNESS..." headline treatment implied by the page copy, with the teal accent reserved for a secondary graphic or underline detail; no hero-specific selector was in evidence.

**product-card** represents the Classic / Salted Caramel / Maple / Cinnamon flavor tiles referenced in the page text ("OUR PRODUCTS", "FIND FATSO" repeated per flavor). A soft gray card surface and hairline edge are proposed since no card-specific selector was supplied.

**footer** is proposed dark (using the same #32373c surface as button-secondary) with white text, a common Divi pattern, though no footer selector appeared in the evidence.

**badge** applies the pink accent as a small pill label, useful for flavor callouts like "NEW FLAVOUR" or "FAMILY FAVOURITE" seen in the copy; fully proposed, no badge CSS observed.

**search** is a light, soft-surface field styled to match the confirmed `#2ea3f2` icon/link color noted in `#et_search_icon:hover`; overall field chrome is proposed.

**testimonial-card** supports the multiple star-rated customer quotes visible in the page text (Naomi A, Jen M, Terry F, etc.), using a soft surface with a teal accent rule; card geometry is proposed since testimonial markup/CSS was not included in the supplied rules.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior (no media queries were supplied):

| Breakpoint | Width      | Nav          | Product grid | Touch target |
|-----------|------------|--------------|--------------|--------------|
| mobile    | <600px     | collapsed/hamburger | 1 column | ≥44px |
| tablet    | 600–1024px | condensed inline | 2 columns | ≥44px |
| desktop   | >1024px    | full inline nav | 3–4 columns | ≥40px |

Buttons and search inputs should maintain at least a 44px tap height on touch devices; the nav should collapse to a hamburger/drawer pattern below 600px. These are conventions applied to fill gaps, not confirmed against live responsive CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Supplied evidence is a static CSS/text snapshot; no rendered layout, real breakpoints, or interaction states (hover/focus/active) were observed beyond the two hover rules quoted above.
- The bulk of the supplied color list matches the WordPress core default color palette (oranges, purples, greens, reds) rather than confirmed brand usage; only #2ea3f2, #32373c, #333333, #666666, #fff, and the grays tied to explicit selectors are treated as confirmed.
- #f35198 and #7ebec5 are carried forward as plausible brand/flavor accents based on their distinctiveness from the WP default set, but their actual on-site usage was not confirmed in the supplied rules.
- No heading-specific font-family rule was supplied; Oswald, Poppins, and other listed families may be the true heading/display fonts in a Divi theme customizer setting, but this could not be verified from the given CSS, so headings default to the confirmed body font (Open Sans).
- All font sizes above body copy (14px) and the button (20px) are proposed, not measured.
- Custom font licensing/availability (e.g., ETmodules, divipixel icon fonts) was not verified and these are excluded from the typography tokens as they are icon/utility fonts, not text faces.
- Component geometry (radii beyond the observed 3px button radius, spacing, card shadows) is proposed to fit the fixed scale, not extracted from measured layout.
