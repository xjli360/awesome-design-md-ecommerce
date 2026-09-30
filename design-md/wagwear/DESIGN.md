---
version: alpha
name: "Wagwear"
source_url: "https://wagwear.com"
captured_at: "2026-09-28T10:12:16.479190+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Wagwear's storefront CSS shows a warm, editorial-leaning palette built on true black (#000000/#111111) text and CTAs against a soft off-white canvas (#ffffff, with a warm cream #f4f1ec used for product-media backgrounds). Supporting neutrals (#777777, #666666, #e4e1db) carry secondary copy and hairlines, while a small set of saturated accents — orange (#f67e3f, used as the observed review-star color), forest green (#3c9342) and ochre-brown (#7e6b45) — are reserved for product badges (responsible, best-seller) and rating UI. Typography draws on "Jost" for display-weight headings and an Avenir/Avenir Next/Helvetica Neue stack for body and UI copy, matching the site's mix of a geometric display face with a humanist workhorse sans; exact rendered pixel sizes are inferred from CSS custom-property names (heading-display-1 through heading-6, body-400 through body-200) whose root em-scale was not confirmed, so sizes below are proposed approximations, not measured. The interpretation favors a clean, gallery-like product grid (cream media tiles, black text, generous whitespace) with small saturated badge/rating accents to keep focus on the dog-boot and apparel photography, consistent with the "design-minded dog" positioning in the copy.

colors:
  primary: "#000000"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#3a3a3a"
  muted: "#777777"
  hairline: "#e4e1db"
  surface-soft: "#f4f1ec"
  surface-card: "#f5f3f0"
  on-primary: "#ffffff"
  accent: "#f67e3f"
  accent-success: "#3c9342"
  accent-gold: "#7e6b45"
  border-subtle: "#e6e3dd"
typography:
  display-xl: {fontFamily: "Jost, sans-serif", fontSize: 56px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Jost, sans-serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Jost, sans-serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Avenir, 'Avenir Next', 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Avenir, 'Avenir Next', 'Helvetica Neue', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Avenir, 'Avenir Next', 'Helvetica Neue', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.02em}
  button-md: {fontFamily: "Avenir, 'Avenir Next', 'Helvetica Neue', Arial, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.04em}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "transparent"
    variants:
      responsible: "{colors.accent-success}"
      best-seller: "{colors.accent-gold}"
      new: "{colors.ink}"
      save: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
  rating-stars:
    iconColor: "{colors.accent}"
    labelColor: "{colors.muted}"
    typography: "{typography.caption}"
  variant-swatch:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.ink}"
    rounded: "{rounded.full}"

## Components

**button-primary** mirrors the observed `.ambcta__button` rule directly: black background, white text, 700-weight 14px letter-spaced label, and a 4px radius with hover darkening toward `#1a1a1a` (proposed as a near-`{colors.ink}` hover state, not separately tokenized here).

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Shop all →" links), inverting to filled ink-on-white on hover; this hover behavior is not confirmed from the supplied CSS.

**text-input** is a proposed form pattern for the newsletter/search fields, using the light hairline border color (`#e4e1db`) against the white canvas, since no explicit input styling was present in the evidence.

**nav-bar** reflects the multi-category header (WAGWELLIES, WALK, WEAR, CARRY, PLAY, SLEEP) implied by the mega-menu class names (`.wag-mega__product`); background/text colors are drawn from those rules, but overall nav layout and sticky behavior are inferred, not measured.

**product-card** is grounded in `.befp__item .product-item__media` (cream `#f4f1ec` tile background) and `.wag-mega__product-price` (`#777777` muted price text), giving the grid its gallery-like, warm-neutral feel.

**hero** is a proposed large-format banner pattern (matching the "NEW FOR FALL / The SPORT Collection" hero copy) using the display typography scale; exact hero sizing/imagery treatment was not present in the CSS evidence.

**footer** is inferred as a dark ink block for the multi-column link footer (Shop, About, Resources, Customer Care) seen in the page text; no explicit footer background color was found in the supplied rules, so `{colors.ink}` is a proposed substitute.

**badge** directly reuses the four observed `.product-badge[data-handle]` colors (responsible green, best-seller gold, new/save black variants), which is the most concretely evidenced component in this set.

**search** and **rating-stars** are proposed/observed-hybrid: rating icon color (`#f67e3f`) is directly from `--lxs-rating-icon-color`, while search field chrome is proposed to match the text-input pattern.

**variant-swatch** is a category-appropriate addition for WagWellies' many named colorways (Hot Pink, Lavender, Cobalt Blue, Golden, Mojave, Retro Blue); styling is proposed using the card surface and hairline tokens, as no swatch-specific CSS was supplied.

## Responsive Behavior

Proposed breakpoints (not measured from live site behavior):

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | 0–599px | single-column product grid, collapsed hamburger nav, stacked hero text |
| tablet | 600–1023px | 2-column product grid, mega-menu likely collapses to accordion |
| desktop | 1024–1439px | full mega-nav, 3–4 column grid |
| wide | 1440px+ | max-width content container, larger hero display type |

Touch targets should be at minimum 44×44px for nav links, badges, and swatch controls. Mega-menu category flyouts should collapse to an accordion pattern below tablet width. This table is a recommendation based on typical Shopify-theme conventions, not an observation of Wagwear's actual responsive markup or breakpoints.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, JavaScript-driven interaction, or mobile viewport was observed. Font-size custom properties (`--font-size-heading-*`, `--font-size-body-*`) were present as rem values but the root font-size multiplier was not confirmed, so all typographic pixel sizes above are proposed approximations rather than measured renders. Hover/focus/active states beyond the one explicitly observed (`.ambcta__button:hover`) are proposed, not verified. Footer, hero, nav-bar, search, and variant-swatch background/behavior mappings are inferred from partial class-name evidence and general e-commerce conventions, not confirmed layout screenshots. "Jost" and the Avenir/Helvetica Neue stack are used only because they appear in the supplied font-family list; no licensing or actual font-loading/availability was verified. Color-to-role assignments (e.g., ink vs. body vs. muted) are best-effort semantic groupings of the observed hex values and may not match the site's internal naming.
