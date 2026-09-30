---
version: alpha
name: "Shoei Helmets"
source_url: "https://shoei-helmets.com"
captured_at: "2026-09-29T03:59:46.678710+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The site runs on a Bootstrap-derived utility framework: the :root variable
  block shows Bootstrap's standard gray/blue/red/green defaults with one
  brand override — --primary set to #a3832a, a dark gold/bronze, replacing
  Bootstrap's default blue. This is the only clear brand-color signal in the
  evidence and is treated here as the primary accent (inferred role, since no
  selector ties it to a specific rendered button or link). Headings use
  'Roboto Condensed', bold, uppercase, colored #333, while body copy uses
  'Open Sans' at a compact .9rem base size and Bootstrap's default ink
  (#212529). The remainder of the palette is neutral grayscale
  (#f8f9fa–#343a40) typical of unstyled Bootstrap chrome, plus standard
  state colors (danger #dc3545, warning #ffd65a, success #28a745, info
  #17a2b8) presumably reserved for form validation rather than brand
  expression. Two near-identical reds (#e20613, #e20714) appear in the raw
  palette without a captured selector; they may be a SHOEI red logo/CTA
  accent but are left unused here since their role is unconfirmed. The
  resulting interpretation favors a restrained, technical, spec-sheet-driven
  catalog aesthetic (weights, shells, shields) over decorative color use,
  with the gold primary reserved for a single interactive accent role.

colors:
  primary: "#a3832a"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#495057"
  muted: "#868e96"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  heading: "#333333"
  dark: "#343a40"
  border-strong: "#ced4da"
  danger: "#dc3545"
  warning: "#ffd65a"
  success: "#28a745"
  info: "#17a2b8"
typography:
  display-xl: {fontFamily: "'Roboto Condensed', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: 0px}
  display-md: {fontFamily: "'Roboto Condensed', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "'Roboto Condensed', sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Open Sans', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.3px}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.warning}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    headerBackground: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rowStripe: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** is the gold-accent call-to-action, mapped to the CSS `--primary` override (#a3832a); proposed for "Find a Dealer," "Add to Cart," and similar single-emphasis actions. **button-secondary** is an outline variant using the same gold on a white ground, proposed for lower-priority actions like "View All." **text-input** follows Bootstrap-default border-gray styling (#dee2e6) with white fill, used for search and account forms; focus/error states are not observed and are proposed only. **nav-bar** is a white top bar with a light hairline bottom border, holding the Helmets/Accessories/Technology/Racing Support/Find a Dealer links seen in the text excerpt; sticky/collapsed states are inferred, not observed. **product-card** wraps individual helmet listings (model name, Shield, Weight, Shell fields visible in the excerpt) in a bordered white card with condensed title type. **hero** is a proposed dark full-bleed band for homepage messaging ("premium quality handmade in Japan"), using the dark gray-900/gray-800 tone as background since no hero-specific color was captured. **footer** reuses the dark neutral for the Helmet House/SHOEI corporate footer (address, distributor legal text, policy links), with warning-yellow links proposed for contrast against dark background. **badge** is a small pill for tags like shell type (AIM/AIM+) or "Free Shipping Over $100," using muted gray on light gray. **search** is a simple bordered field, likely paired with the dealer locator. **spec-table** is a category-specific component for the recurring Shield/Weight/Shell technical rows seen across every helmet listing, styled with Bootstrap's `.table-striped` pattern (rgba(0,0,0,.05) stripe) reinterpreted as `{colors.surface-soft}`.

## Responsive Behavior

Recommended, not measured from live rendering:

| Breakpoint | Width    | Layout notes (proposed) |
|-----------|----------|--------------------------|
| xs        | 0–575px  | Single-column stacked cards, nav collapses to menu icon |
| sm        | 576px    | 2-column product grid |
| md        | 768px    | Nav links inline; 3-column product grid |
| lg        | 992px    | Full nav bar; spec-table shown inline |
| xl        | 1200px   | Max-width container, 4-column product grid |

Touch targets should be at least 44px for nav/menu and button components; the mobile nav collapse pattern is proposed based on the Bootstrap breakpoint variables in `:root`, not observed interaction.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no rendered screenshots, hover states, or JS-driven interactions (carousel behavior, mobile nav toggle, form validation) were observed.
- The gold `--primary` (#a3832a) is inferred as the intended brand accent from variable naming alone; no selector confirms it renders on any visible button or link.
- The reds `#e20613`/`#e20714` and yellow `#ffeb44` appear in the raw palette without associated selectors; their design role is unknown and they are excluded from the component mapping.
- Font list includes Playfair Display, Saira, Inter, and monospace stacks, but only `'Open Sans'` and `'Roboto Condensed'` are tied to confirmed selectors (`body` and heading rules); other listed fonts are not used in this spec.
- All pixel sizes for typography beyond the confirmed `3rem`/`.9rem` values are proposed estimates, not measured.
- Font licensing/self-hosting status for Open Sans and Roboto Condensed was not verified from the supplied evidence.
- Breakpoint and responsive layout guidance is a proposed convention derived from Bootstrap's default `--breakpoint-*` variables, not observed page behavior.
