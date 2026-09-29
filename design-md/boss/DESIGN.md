---
version: alpha
name: "Boss"
source_url: "https://www.boss.info"
captured_at: "2026-09-28T04:06:41.384620+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from static CSS served on Roland's shared
  infrastructure (static.roland.com) that powers the BOSS global site. The
  evidence shows a monochrome-first system: black ink (#000000) on white
  canvas (#ffffff), with grayscale surfaces (#e5e5e5, #f2f2f2, #cccccc,
  #e0e0e0) building headers, backgrounds, and hairlines. Two accent hues
  recur in interactive states: an orange (#ff5a00, with a near variant
  #ff3c00) used for hover and active icon states across the shared Roland
  header, and a blue (#0064ff) that is explicitly scoped to `.boss-global`
  selectors, suggesting BOSS treats blue as its own sub-brand accent
  layered over Roland's default orange. No proprietary font family was
  observed; only generic `sans-serif`, `serif`, `monospace`, and an icon
  font (`glyphicon`) appear, so all typography roles below default to
  system sans-serif with monospace reserved for technical/spec content —
  fitting for a pedal brand that publishes parameter tables. Rounded
  values of 37.5px and 29.5px on fixed-size circular buttons are observed
  and generalized here to a `full` token. Header structure (50px height,
  1024–1600px width constraints) is observed; all other layout, spacing,
  and mobile behavior below is proposed and clearly marked as inferred.

colors:
  primary: "#ff5a00"
  primary-pressed: "#ff3c00"
  secondary: "#0064ff"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  subtle: "#999999"
  hairline: "#e0e0e0"
  surface-soft: "#e5e5e5"
  surface-card: "#f2f2f2"
  surface-dark: "#141414"
  on-primary: "#ffffff"
  border-light: "#cccccc"
typography:
  display-xl: {fontFamily: "sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  caption: {fontFamily: "sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
  mono-spec: {fontFamily: "monospace", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
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
    borderColor: "{colors.border-light}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-circular:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-light}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.none} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-light}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.mono-spec}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** uses the orange accent (`{colors.primary}`) observed on hover states throughout base.css, applied here as a solid fill for primary calls to action (e.g. "Shop Now," "Explore"). White text on orange satisfies contrast. Hover/active state darkening to `{colors.primary-pressed}` is proposed, not observed.

**button-secondary** is an outline treatment using the neutral border gray, appropriate for secondary actions like "Learn More." Its states (hover, disabled) are proposed conventions, not measured.

**button-circular** generalizes the observed `.button-play` and `.button-up` patterns: fixed square boxes with a border and near-100% border-radius, producing a true circle. The site uses this for a hero play button (75px, white 5px border, glyphicon play icon) and a scroll-up/home button (60px, 1px border) whose icon color shifts to orange or, within `.boss-global` scope, to blue (`{colors.secondary}`) on hover. This is one of the few genuinely observed interaction states in the evidence.

**text-input** is a proposed standard form field for newsletter or dealer-locator forms; no input styling beyond global resets (`border-radius: 0`, `-webkit-appearance: none`) was observed, so field chrome here is inferred from base.css normalization intent.

**nav-bar** reflects the observed `#productheader`/`#contentheader`: 50px fixed height, white background, 1px `{colors.hairline}` bottom border, constrained between 1024px and 1600px wide — a desktop-first, fixed-width header pattern rather than a fluid one. Link color defaults to `{colors.muted}` (#666) and shifts to orange (or blue in BOSS-scoped contexts) on hover, per the `:hover:before` rules on `#ph-home`/`#ch-home`.

**product-card** is proposed for pedal listings, using the light gray card surface (`{colors.surface-card}`) against the page's `{colors.surface-soft}` background to create subtle layering, consistent with the grayscale surface stack observed in the palette.

**hero** proposes a dark, near-black banner (`{colors.surface-dark}`) behind white headline text, matching the `.billboard-headline` rule that sets `color: #fff` for `h1/h2/p`, alongside a `.billboard-headline-black` variant for light-background heroes (mapped to `{colors.ink}` text, not separately tokenized here).

**footer** is a proposed low-contrast band using the same `#e5e5e5` body background observed sitewide, keeping it visually distinct from card surfaces while staying inside the grayscale system.

**badge** and **search** are proposed, filling common e-commerce patterns (new/featured tags, product search) using tokens already grounded in the palette; neither pattern was directly observed in the supplied CSS.

**spec-table** is a category-appropriate addition for a guitar-pedal brand: technical specification blocks (I/O, power draw, dimensions) rendered in `{typography.mono-spec}`, justified by `monospace` appearing in the site's observed `font_families` list even though no selector target was captured.

## Responsive Behavior

This is a recommendation, not measured site behavior — no breakpoints, media queries, or mobile markup were present in the supplied evidence. The observed header explicitly enforces `min-width: 1024px`, implying a desktop-oriented layout at minimum; behavior below that width is unknown.

| Breakpoint | Width      | Notes (proposed) |
|-----------|------------|-------------------|
| compact   | < 768px    | Single-column stacking, nav collapses to menu icon |
| tablet    | 768–1023px | Two-column product grids; header may need a fluid override of the observed 1024px min-width |
| desktop   | 1024–1600px | Matches observed header constraint; standard multi-column layout |
| wide      | > 1600px   | Content max-width caps per observed `max-width: 1600px` |

Touch targets should be at least 44×44px; the observed circular buttons (60–75px) already satisfy this at desktop scale. Collapse the nav-bar into a hamburger pattern below tablet width; this interaction was not observed and is a standard proposal only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS from one shared stylesheet (`base.css`); no rendered page, JavaScript-driven states, or mobile stylesheet was captured.
- No proprietary/brand font was found — only generic `sans-serif`, `serif`, `monospace`, and the `glyphicon` icon font. All typography sizes beyond the icon-font rules (25px, 28px, 33px, 19px) are proposed, not measured.
- Semantic color mapping (e.g., `body`, `surface-card`) is inferred from grayscale frequency in the palette, not from confirmed selector usage for those exact roles.
- The blue (#0064ff) vs. orange (#ff5a00) hover split between `.boss-global` and default Roland scope is observed but its full intent (sub-brand differentiation) is an interpretation, not confirmed documentation.
- Spacing scale, rounded scale (aside from the two observed circular buttons), component states (focus, disabled, error), and all mobile/responsive layout are proposed conventions, not extracted from evidence.
- Font licensing/availability for any fallback stack was not verified; only generic CSS fallback keywords are used.
