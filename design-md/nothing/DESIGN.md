---
version: alpha
name: "Nothing"
source_url: "https://nothing.tech"
captured_at: "2026-09-28T09:07:53.103012+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Nothing's storefront is built on a strict monochrome foundation — pure black (#000000) and white (#ffffff) — accented by a small, deliberate set of signal colors defined as CSS custom properties: accent-red (#c6102e), accent-yellow (#ffc700), and accent-blue (#002f6c), plus supplementary brights (#27d4e0, #ff42ad, #ffee00, #f4e300) likely reserved for Glyph Interface or campaign call-outs. A neutral greyscale ramp (#f4f4f4, #f5f5f5, #e5e7eb, #b1b3b3, #999999) supports card surfaces, dividers, and muted text without competing with the black/white core.
  Typography is distinctive and brand-owned: Ndot-Regular renders product names in a lowercase, dot-matrix style (observed at 20px/55 weight), NType82-Regular serves body copy (observed at 16px/1.4 line-height), and NType82-Headline is inferred for larger display type though its size/weight were not directly observed. Geist Mono Variable and system monospace stacks are treated as inferred candidates for technical captions or spec labels, consistent with the brand's engineering-forward tone.
  This interpretation proposes a minimal, high-contrast component system — black/white primary surfaces, a single red or yellow accent for primary actions, and monospace micro-labels for specs — extrapolated from the token evidence rather than directly observed page layout.

colors:
  primary: "#c6102e"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#999999"
  hairline: "#e5e7eb"
  surface-soft: "#f4f4f4"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  accent-yellow: "#ffc700"
  accent-blue: "#002f6c"
  accent-cyan: "#27d4e0"
  accent-pink: "#ff42ad"
  accent-yellow-bright: "#ffee00"
  greyscale-default: "#b1b3b3"
typography:
  display-xl: {fontFamily: "NType82-Headline, sans-serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "NType82-Headline, sans-serif", fontSize: 36px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.25px}
  title-md: {fontFamily: "Ndot-Regular, sans-serif", fontSize: 20px, fontWeight: 55, lineHeight: 1.25}
  body-md: {fontFamily: "NType82-Regular, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4}
  body-sm: {fontFamily: "NType82-Regular, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4}
  caption: {fontFamily: "Geist Mono Variable, ui-monospace, monospace", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "NType82-Regular, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.2px}
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
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: "64px"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    gap: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  spec-strip:
    backgroundColor: "{colors.surface-card}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-sm}"
    accentColor: "{colors.accent-cyan}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    gap: "{spacing.lg}"

## Components
**button-primary** — A solid, high-contrast call-to-action using the accent-red token as an inferred primary action color; no live button color was directly observed, so this pairs the defined `--accent-red` variable with white text as a proposed convention.

**button-secondary** — An outlined, transparent-background variant for secondary actions (e.g., "Learn More"), keeping the monochrome ink-on-white identity dominant; hover/focus states are proposed, not observed.

**text-input** — A soft-grey field (surface-soft) with a light hairline border, intended for newsletter or search-adjacent forms referenced in the footer text; focus-ring styling is proposed.

**nav-bar** — A fixed 64px-tall bar matching the observed `--header-height` CSS variable, white background with black text/logo; sticky/scroll-collapse behavior is proposed, not measured.

**product-card** — Used for headphone/earbud tiles (e.g., "ear (a)", "CMF Clip Pro"), combining the Ndot-Regular product-name style with NType82-Regular descriptive copy on a light card surface; imagery treatment is proposed.

**hero** — A full-bleed black section for flagship messaging ("we're building a world where tech is fun again"), using display-xl headline type in white; exact hero height/media behavior was not observed and is proposed.

**footer** — A black footer band housing utility links (Support, Newsletter, Legal, social icons) in small body type, consistent with the dark-mode greyscale variables (`--greyscale-dm-*`) found in the CSS.

**badge** — A small pill using accent-yellow, suited to labeling promotional or "new" tags (e.g., "Open Beta"); this role is inferred from the presence of the yellow accent token rather than direct badge markup evidence.

**search** — A pill-shaped input for site/product search, using the full-radius token and muted placeholder color; not directly observed in the supplied evidence, proposed for e-commerce completeness.

**spec-strip** — A category-specific component for headphone technical specs (battery life, ANC, driver tuning credits like "tuning by KEF"), using monospace caption type for numeric/spec labels and a cyan accent to echo the Glyph-related bright color found in the palette; this is a proposed pattern, not an observed module.

## Responsive Behavior
This is a recommended breakpoint structure, not measured site behavior, since no responsive CSS or viewport-specific rules were supplied.

| Breakpoint | Width      | Notes (proposed) |
|-----------|-----------|-------------------|
| mobile    | <640px    | Single-column product cards, collapsed nav into a hamburger menu, touch targets ≥44px |
| tablet    | 640–1024px| Two-column card grid, nav-bar remains visible at 64px height |
| desktop   | >1024px   | Multi-column grid, full horizontal nav, hero at full section spacing |

Touch targets for buttons and nav items should maintain a minimum 44×44px hit area; the nav-bar is expected to collapse into a drawer or overlay below the tablet breakpoint, though this collapse pattern was not observed in the supplied CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/token extraction only; no rendered page, computed layout, or interaction states were observed. The mapping of `--accent-red`, `--accent-yellow`, and `--accent-blue` to specific UI roles (e.g., primary button vs. badge vs. warning) is inferred from variable naming, not confirmed usage. Font sizes/weights for `display-xl`, `display-md`, `body-sm`, `caption`, and `button-md` are proposed scale extrapolations beyond the two directly observed rules (`.type-product-name`, `.type-body`). Ndot-Regular, Ndot-Bold, NType82-Regular, and NType82-Headline appear to be proprietary Nothing typefaces; their licensing and availability outside the brand's own assets were not verified. Mobile navigation collapse, hover/focus states, scroll behavior, and actual grid layouts were not observed and are marked proposed throughout. Additional palette colors (e.g., translucent blacks/whites, dark-mode overlay tints) exist in the evidence but were omitted from role assignment due to insufficient context on their applied usage.
