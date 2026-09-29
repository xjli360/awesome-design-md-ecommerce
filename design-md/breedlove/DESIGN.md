---
version: alpha
name: "Breedlove"
source_url: "https://www.breedlovemusic.com"
captured_at: "2026-09-28T09:14:26.629924+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Breedlove's Shopify-based storefront (breedloveguitars.com / breedlovemusic.com) uses a restrained,
  craft-forward palette anchored by a near-black foreground (#121212) on white (#ffffff), with a muted
  teal (#246c6c) as the primary interactive accent — observed directly as both the default and hover
  fill on the "Load More" product-grid button. A sage/mint family (#5a957d, #a7d0c0, #dde9e6) and a
  slate-blue family (#205c7c, #242833, #2c2e35) appear in the wider extracted palette but without a
  captured UI role; they are treated here as inferred supporting accents for surfaces, badges, or
  seasonal callouts. A warm gold (#e0a43f) and an indigo (#334fb4) are likewise present but unassigned,
  kept as optional highlight colors. Shopify's native accelerated-checkout blue (#1990c6, hover #136f99)
  is a platform-level color rather than brand-authored, and is isolated to payment components only.
  Typography pairs a bold condensed display face, Anton, for large uppercase headings (60px observed on
  the homepage h1) with a humanist sans, Assistant (Helvetica/sans-serif fallback, from the observed
  font-family list), for body copy, and a heavy Inter 18pt for buttons (19px, weight 900, observed). The
  interpretation favors a workshop-honest, high-contrast, USA-made aesthetic: minimal rounding, confident
  uppercase labels with generous tracking, and generous whitespace suited to a premium handmade
  instrument brand. Layout, spacing rhythm, and mobile behavior are proposed, not observed.

colors:
  primary: "#246c6c"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#595b61"
  hairline: "#dedede"
  surface-soft: "#f3f3f3"
  surface-card: "#dde9e6"
  on-primary: "#ffffff"
  accent-gold: "#e0a43f"
  accent-indigo: "#334fb4"
  accent-blue: "#1990c6"
  accent-blue-hover: "#136f99"
  sage: "#5a957d"
  mint: "#a7d0c0"
  deep-navy: "#205c7c"
  charcoal: "#2c2e35"
  near-black: "#000000"
typography:
  display-xl: {fontFamily: "Anton, sans-serif", fontSize: 60px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Anton, sans-serif", fontSize: 40px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Anton, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0.5px}
  body-md: {fontFamily: "Assistant, Helvetica, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.96px}
  body-sm: {fontFamily: "Assistant, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.5px}
  caption: {fontFamily: "Assistant, Helvetica, sans-serif", fontSize: 13px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Inter 18pt, sans-serif", fontSize: 19px, fontWeight: 900, lineHeight: 1, letterSpacing: 1.8px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    borderColor: "{colors.hairline}"
  hero:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  spec-panel:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    borderColor: "{colors.hairline}"

## Components
**button-primary** uses the one directly observed interaction pair on the site: the "Load More" button's teal fill (#246c6c) with white text, styled here as the default state for primary calls-to-action like "Add to Cart." Hover/focus darkening (e.g., toward `{colors.ink}`) is proposed, echoing the button's own hover swap to black seen in the CSS.

**button-secondary** is an outlined, white-fill variant proposed for lower-emphasis actions ("Learn more," "View cart") to preserve one dominant accent per screen, using the same teal for border and label text.

**text-input** is a proposed minimal-border field for search, newsletter, and account forms; no live input styling was captured, so radius and padding follow the general square, low-rounding system inferred from the button's 0px radius fallback.

**nav-bar** is inferred from the page's header text content (Store, Guitars, About, Artists, Blog, Log in, Cart) rather than any captured layout CSS; a plain white bar with dark-ink text keeps focus on product photography.

**product-card** reflects the featured-products grid pattern (title, series/category tag, price, Add to Cart) seen in the page text; the soft teal-tinted card surface (`{colors.surface-card}`) is proposed to differentiate cards from the white page background without introducing a new hue.

**hero** is proposed for the "Bringing It Back Home" homepage banner, using a dark charcoal ground with the Anton display face to match the confident, uppercase brand voice implied by the copy and the observed h1 styling.

**footer** is proposed as a dark, high-contrast band (ink background, white text) consistent with the near-black `--color-foreground` token, used for social/legal links; exact footer markup was not present in the evidence.

**badge** is proposed for series labels ("Roots," "Artisan," "Collector") seen repeatedly beside product names, styled as a pill outline rather than a filled shape to keep secondary information quiet.

**search** is proposed as a lightweight, borderless field on a soft-gray surface, matching the "Search Search" control referenced in the page text; no dedicated search CSS was extracted.

**spec-panel** is a category-appropriate proposed component for guitar tonewood/build specifications (referenced by copy like "proven tonewood pairings"), using the muted teal-tinted card surface and hairline border to present structured spec data distinctly from marketing copy.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <600px | Single-column product grid, collapsed hamburger nav, stacked hero text over full-bleed image |
| Tablet | 600–1024px | 2-column product grid, nav may remain collapsed |
| Desktop | >1024px | 3–4 column product grid, full horizontal nav |

Touch targets should be at least 44×44px, matching Shopify's own accelerated-checkout button sizing (`clamp(25px, ..., 55px)`) seen in the evidence. Navigation should collapse to a hamburger/drawer pattern below tablet width; this is a standard proposal, not confirmed from captured markup.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from static CSS/text extraction only; no live rendering, computed layout, or interaction states (hover, focus, active, disabled) were directly observed beyond the single documented button hover swap. Several palette colors (sage, mint, indigo, gold, slate-blue family) have no confirmed UI role and are assigned here as inferred/optional accents. Exact `--font-body-family` and `--font-heading-family` variable values were not resolved in the evidence; Assistant and Anton assignments are inferred from the supplied `font_families` list and the one explicit `font-family: Anton` rule. All font sizes outside the two directly observed values (60px heading, 19px button) are proposed. Mobile/responsive layout, breakpoints, and grid column counts are proposed conventions, not measured. Custom font licensing and self-hosting/availability for Anton, Assistant, and Inter 18pt were not verified.
