---
version: alpha
name: "Bessey"
source_url: "https://besseytools.com"
captured_at: "2026-09-28T10:13:40.916116+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from BESSEY Tools North America's supplied CSS and page text. The observed palette centers on a strong red (#e3000f, with a close variant #e3000b and hover/darker state #b6000c) paired with near-black ink (#000000, #1f2426) and a white canvas (#ffffff). Bootstrap-derived utility colors (#dc3545, #198754, #ffc107, #6c757d, #f8f9fa, #dee2e6) appear throughout, indicating a Bootstrap-based front end with default state colors (danger, success, warning, muted) layered over a custom brand red. Headings use Roboto with Arial/Helvetica/sans-serif fallbacks per the observed h1–h6 rule; body text is assumed to inherit the same Bootstrap body-font stack, as no distinct body font-family rule was supplied, so Roboto is reused there as an inferred choice. Roboto Slab was observed in the font list but no selector confirming its role was supplied, so it is treated as a possible display accent only, not assigned to a component. Buttons show bold weight, zero border-radius by default, and a light inset/shadow treatment (#ffffff26, #00000013). This design system proposes an industrial, high-contrast, utilitarian language: sharp corners on buttons, red as the sole accent for actions and emphasis, and generous use of neutral grays for structure, reflecting a B2B tools manufacturer site rather than a decorative retail brand.

colors:
  primary: "#e3000f"
  primary-hover: "#b6000c"
  ink: "#000000"
  ink-soft: "#1f2426"
  canvas: "#ffffff"
  body: "#212529"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#f9f9f9"
  on-primary: "#ffffff"
  border-subtle: "#ced4da"
  danger: "#dc3545"
  success: "#198754"
  warning: "#ffc107"
  info: "#00bcd4"
  overlay-dark: "#000000cc"
  overlay-light: "#ffffff26"
typography:
  display-xl: {fontFamily: "Roboto, Arial, Helvetica, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Roboto, Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Roboto, Arial, Helvetica, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Roboto, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Roboto, Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Roboto, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.5, letterSpacing: 0.2px}
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
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.border-subtle}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-subtle}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border-subtle}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    stripedBackgroundColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components
**button-primary** is the sole high-emphasis action style, using the observed brand red with white text and bold weight; sharp corners follow the observed `--bs-btn-border-radius:0` default. Hover/darker state (#b6000c) is proposed by analogy to the palette's red variants, not confirmed as a measured hover rule.

**button-secondary** is a proposed outline treatment for lower-emphasis actions (e.g., "Learn more," filters), using neutral border/ink colors since no secondary-button-specific selector was supplied.

**text-input** follows Bootstrap form-control conventions implied by the `.form-control` selectors in evidence (file-selector-button styling, border/background tokens), with padding and radius proposed at a small, utilitarian scale consistent with the zero-radius button default.

**nav-bar** is inferred as a white/light header bar given the canvas and hairline colors present; no header-specific selector was supplied, so structure (logo left, links right, language switcher) is proposed based on the page text listing "EN FR" and "Products / Company / Support" navigation groups.

**product-card** proposes a bordered, light-surface card for clamping tools, vises, and cutting-tool listings, using `surface-card` (#f9f9f9) and hairline borders; no card selector was present in evidence, so padding and radius are proposed defaults suited to an industrial catalog grid.

**hero** proposes a dark ink-soft background for the homepage banner referencing the "new one-handed clamp EHK360" feature described in page text, with white display type; actual hero background/image was not observed in CSS.

**footer** is inferred dark to balance the hero, grouping the many footer link categories visible in page text (Products, Company, Support, Newsletter); color choice reuses `ink-soft` since no footer-specific background rule was supplied.

**badge** proposes a small red label for "New Products & Offers" or category tags referenced in navigation text; no badge selector was present in evidence.

**search** models the site's visible "Search" function using neutral surface and border tokens consistent with Bootstrap form defaults.

**spec-table** proposes a striped data table (per the observed `.table-striped` rules) for technical/clamping-tool specifications, using the striped background token drawn directly from Bootstrap CSS variables in evidence.

## Responsive Behavior
This is a recommended, unmeasured breakpoint scheme following the Bootstrap variables found in evidence (`--bs-breakpoint-sm:576px; md:768px; lg:992px; xl:1200px; xxl:1400px`):

| Breakpoint | Width | Layout guidance (proposed) |
|---|---|---|
| xs | 0–575px | Single-column stack; nav collapses to hamburger/off-canvas menu |
| sm | 576–767px | Two-column product grids begin; search remains full-width |
| md | 768–991px | Nav bar expands inline; product-card grids move to 2–3 columns |
| lg | 992–1199px | Full desktop nav; product grids at 3–4 columns; hero at full display-xl scale |
| xl/xxl | 1200px+ | Max-width container centers content; spacing scales to section/xxl tokens |

Touch targets on buttons and nav items should be at least 44px tall in mobile contexts; this is a proposed accessibility guidance, not a site-measured value. Collapse behavior for the primary navigation and language switcher (EN/FR) is assumed conventional (hamburger toggle) but was not observed in the supplied CSS or markup.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built entirely from static CSS variable dumps, a page-text excerpt, and a flat color/font-family list; no rendered layout, computed styles, or DOM structure were observed. Component boundaries (nav-bar, hero, product-card, footer, search) are inferred from page-text content and generic Bootstrap conventions, not from selectors tied to those regions. Font-size, line-height, letter-spacing, and weight values in `typography` beyond the base `body`/heading rules are proposed defaults scaled for an industrial B2B site, not measured from the source. The role of Roboto Slab (present in the font-family list but with no confirming selector) is left unassigned. Hover, focus, active, and disabled states beyond the generic `.btn:hover`/`:focus-visible` variable references are proposed, not verified interactions. Mobile/tablet navigation collapse behavior was not observed. Availability, licensing, and web-font loading configuration for Roboto were not verified from this evidence set.
