---
version: alpha
name: "Plungie"
source_url: "https://plungie.com"
captured_at: "2026-09-28T04:04:23.773866+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Plungie's observed CSS centers on a deep navy palette (`#13294b`, `#11284b`,
  `#0d1d38`, `#1d3765`) paired with a saturated cyan (`#00bad2` / `#39c2d4`)
  used as the primary call-to-action color, and a warm coral (`#f17051`) held
  in reserve as a secondary accent. Two near-identical navy hex values appear
  across separate stylesheets (a CSS custom property `--navy: #13294b` on the
  homepage vs. `#11284B` in the theme-override body/heading/button rules);
  both are preserved as distinct tokens since the evidence does not confirm
  they are meant to be identical. Typography is set in 'Plus Jakarta Sans'
  with Arial/sans-serif fallback, headings shown at 64px/700 weight and a
  conflicting fluid clamp() rule suggesting a lighter-weight hero variant —
  both interpretations are noted. Buttons use a 32px pill radius on a cyan
  fill with navy text, inverting to a teal hover (`#007786`) with white text,
  a concrete observed interaction. This interpretation extends that
  navy/cyan/coral system into a calm, premium poolside aesthetic: dark
  hero surfaces, light card surfaces for product/spec content, and pill
  buttons as the dominant interactive shape. Card layouts, nav, search, and
  the model-selector pattern below are proposed and inferred for the
  pools/spas category, not observed in the supplied CSS.

colors:
  primary: "#00bad2"
  ink: "#11284b"
  canvas: "#ffffff"
  body: "#11284b"
  muted: "#61789b"
  hairline: "#ededed"
  surface-soft: "#ddecf0"
  surface-card: "#f1f1f1"
  on-primary: "#11284b"
  navy-deep: "#0d1d38"
  navy-soft: "#1d3765"
  navy-alt: "#13294b"
  cyan-accent: "#39c2d4"
  cyan-light: "#5cd3e2"
  coral: "#f17051"
  hover-state: "#007786"
  disabled-bg: "#f1f1f1"
  disabled-text: "#d0d0d0"
  cream: "#f2e1d1"
  overlay-navy: "#11284b94"
typography:
  display-xl: {fontFamily: "'Plus Jakarta Sans', sans-serif", fontSize: "64px", fontWeight: 700, lineHeight: 1.05, letterSpacing: "-0.025em"}
  display-md: {fontFamily: "'Plus Jakarta Sans', sans-serif", fontSize: "40px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.02em"}
  title-md: {fontFamily: "'Plus Jakarta Sans', sans-serif", fontSize: "24px", fontWeight: 700, lineHeight: 1.3, letterSpacing: "0em"}
  body-md: {fontFamily: "'Plus Jakarta Sans', Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0em"}
  body-sm: {fontFamily: "'Plus Jakarta Sans', Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0em"}
  caption: {fontFamily: "'Plus Jakarta Sans', Arial, sans-serif", fontSize: "13px", fontWeight: 600, lineHeight: 1.4, letterSpacing: "0.01em"}
  button-md: {fontFamily: "'Plus Jakarta Sans', Arial, sans-serif", fontSize: "16px", fontWeight: 700, lineHeight: 1, letterSpacing: "0em"}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  pill: 32px
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
    rounded: "{rounded.pill}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.navy-alt}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.navy-alt}"
    textColor: "{colors.canvas}"
    accentColor: "{colors.cyan-accent}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.muted}"
    borderColor: "{colors.overlay-navy}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.coral}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.base}"
  model-selector:
    backgroundColor: "{colors.surface-soft}"
    activeColor: "{colors.cyan-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"

## Components

**button-primary** reflects the theme-override CSS directly: a cyan (`#00bad2`) fill, navy text, and a pronounced 32px pill radius, with an observed hover state that inverts to teal (`#007786`) background and white text. This is the strongest CTA pattern in the evidence and should anchor "Get a Quote" and "Book a Consultation" actions.

**button-secondary** is inferred from the `input[type=file]` control styling — a transparent background with a 2px navy border and navy text, switching border/text to cyan on hover/focus. Reused here as a lower-emphasis action pattern (e.g. "Learn More") since no dedicated secondary-button rule was supplied.

**text-input** is proposed. No form-field border/background rules were present in the evidence beyond the file-picker; a light hairline border and white background are assumed to match the site's generally light-on-white content sections implied by `template_theme-overrides.css` body styling.

**nav-bar** is inferred to sit on the dark navy hero background (`--navy` / `#13294b`), consistent with the homepage `body` background-color, with white text for contrast. Actual nav markup, sticky behavior, and mobile menu were not present in the supplied CSS.

**product-card** proposes a light card surface (`#f1f1f1`, matching the observed disabled/background utility color) with a soft hairline border and generous radius, suited to displaying individual plunge-pool models, dimensions, and pricing tiers — a category-appropriate pattern not directly observed.

**hero** uses the confirmed navy background and white heading color, with the cyan accent reserved for emphasized inline text (`h1 strong { color: var(--cyan) }` was directly observed). Gradient or radial treatment using `navy-deep`/`navy-soft` is a plausible but unconfirmed extension.

**footer** is inferred to use the deepest navy (`#0d1d38`) with muted text, mirroring the `--mute`/`--line` custom properties defined at `:root` (translated here to the closest available hex, `#11284b94`, since the RGBA custom properties themselves aren't expressible as flat hex tokens).

**badge** and **search** are both proposed, unobserved patterns included for completeness of a commerce-adjacent product site; badge borrows the coral accent for promotional labels, search borrows the light cyan-tinted surface (`#ddecf0`) seen elsewhere in the palette.

**model-selector** is a category-specific, fully proposed component for choosing between pool ranges (e.g. plunge, lap, swim spa), using the cyan accent to indicate an active/selected state against the soft surface tint.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior — no media queries or mobile markup were present in the supplied evidence.

| Breakpoint | Range | Notes |
|---|---|---|
| Mobile | up to 640px | Single-column stacking; nav collapses to a hamburger/drawer (proposed) |
| Tablet | 641–1024px | Two-column product grids; hero heading scales via clamp() as suggested by the observed `h1` rule |
| Desktop | 1025px+ | Full multi-column layout; pill buttons and hero at full display-xl scale |

Touch targets should be at minimum 44×44px for all interactive elements (buttons, nav links, form controls); the observed 8px/24px button padding should be increased on touch devices to meet this. Collapse behavior for navigation and filtering UI is a proposal, not an observed interaction.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- All CSS was extracted statically from delivered stylesheets/inline styles; no rendered layout, real breakpoints, or JavaScript-driven interactions (menus, carousels, quote configurators) were observed.
- Two visually similar navy hex values (`#13294b` from a `:root` custom property and `#11284b` from a separate theme-override stylesheet) could not be confirmed as intentionally distinct or a duplication artifact; both are retained as separate tokens.
- The `h1` rule contains conflicting `font-weight` declarations (300, then 700) within the same supplied rule block; the 700 weight was treated as authoritative per the more specific theme-override file, but this is an inference, not a confirmed cascade result.
- `--mute`, `--mute-strong`, `--line`, and `--line-strong` are defined as RGBA custom properties and could not be mapped to hex tokens; only the one RGBA-derived hex present in the observed palette (`#11284b94`) was reused for overlay/footer purposes.
- Component definitions for nav-bar, text-input, footer, badge, search, and model-selector are proposed/inferred design patterns appropriate to a pools/spas commerce site, not confirmed from supplied selectors.
- Spacing and radius scales beyond the directly observed button values (8px/24px padding, 32px radius, 8px radius on file input) are proposed conventions, not measured.
- 'Plus Jakarta Sans' availability, self-hosting terms, and licensing were not verified; it is treated as an observed font-family declaration only.
