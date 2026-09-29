---
version: alpha
name: "Winc"
source_url: "https://winc.com"
captured_at: "2026-09-28T05:01:55.386228+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Winc's observed CSS centers on a near-black "obsidian" (#060F0C) used for borders, select controls, slider thumbs, and body copy, paired with a clean white (#ffffff) header background and a warmer off-white "crystal" (#fdfcfa) used behind form controls. Pure black (#000000) and a mid-gray body tone (#333333) also appear directly in typed color declarations, alongside a muted gray (#888888) used for strikethrough sale pricing. A small set of saturated accents — gold (#ffc700), berry red (#e9152e), deep green (#065831), rust (#b74737), and a soft mauve (#c0a6c7) — sit in the palette and are treated here as flavor/varietal accent colors (inferred role, not confirmed usage) for badges and collection tags. Headline type uses NoeDisplay, a serif-leaning display face confirmed at 38px/44px and a smaller 26px/32px variant, suggesting a two-tier heading scale. All interface and body text observed in CSS uses BrownStd at 14–16px with either a light (300) or bold (700) weight, so this interpretation infers an intermediate regular weight for standard paragraph copy. Rounding, spacing, and most component states below are proposed conventions grounded in the pill-shaped select control (border-radius: 40px) and slider track/thumb radii actually present in the CSS.

colors:
  primary: "#060f0c"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#888888"
  hairline: "#dedede"
  surface-soft: "#f3f3f3"
  surface-card: "#fdfcfa"
  on-primary: "#ffffff"
  accent-gold: "#ffc700"
  accent-berry: "#e9152e"
  accent-green: "#065831"
  accent-mauve: "#c0a6c7"
  accent-rust: "#b74737"
  accent-lime: "#ebf5a9"
typography:
  display-xl: {fontFamily: "NoeDisplay, serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "NoeDisplay, serif", fontSize: 38px, fontWeight: 700, lineHeight: 1.16, letterSpacing: 0.015em}
  title-md: {fontFamily: "BrownStd, sans-serif", fontSize: 20px, fontWeight: 300, lineHeight: 1.4, letterSpacing: 0}
  body-md: {fontFamily: "BrownStd, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0}
  body-sm: {fontFamily: "BrownStd, sans-serif", fontSize: 14px, fontWeight: 300, lineHeight: 1.6, letterSpacing: 0}
  caption: {fontFamily: "BrownStd, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.02em}
  button-md: {fontFamily: "BrownStd, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.6, letterSpacing: 0}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "4px solid {colors.primary}"
    padding: "{spacing.md} {spacing.xl}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    height: "71px"
    hairline: "{colors.hairline}"
  hero:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-md}"
    subTypography: "{typography.title-md}"
    padding: "{spacing.section} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    priceColor: "{colors.ink}"
    salePriceColor: "{colors.muted}"
    padding: "{spacing.base}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "4px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.lg}"
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    padding: "{spacing.xs} {spacing.base}"

## Components
**button-primary** uses the obsidian (#060f0c) fill confirmed as the CSS root primary variable, paired with white text; a fully rounded pill shape is proposed by analogy with the observed 40px-radius state select control. **button-secondary** inverts this to an outlined obsidian border on white, mirroring the exact `border: 4px solid var(--primary-obsidian)` rule found on the mobile state selector. **nav-bar** reflects the confirmed white header background and the fixed `--menu-height: 71px` custom property, with BrownStd bold nav-link text colored obsidian as directly declared. **hero** is a proposed composite pattern (not observed as a discrete block) that pairs NoeDisplay display type with the lighter BrownStd subtitle style seen in `.subtitle--decorated`, set against the warm crystal off-white background. **product-card** is inferred from the presence of `.product-grid-rating-price` and sale-price strikethrough styling (#888888 on `s` elements); card chrome, radius, and border are proposed conventions. **footer** is a proposed dark-obsidian band for contrast and closure, since no footer-specific rules were supplied; typography reuses the confirmed BrownStd family. **badge** is proposed for varietal/collection tags (e.g. "No Sulfites," "Certified Vegan") using the pale lime accent already present in the palette. **search** and **text-input** both extrapolate the pill-and-border language of the one fully specified control (the ship-to state select), reusing its 4px obsidian border and rounded silhouette. **filter-pill** is a category-appropriate proposed component for the extensive varietal/region/winemaking filter taxonomy visible in the page text, using an active/inactive state pattern that is not confirmed by any supplied CSS.

## Responsive Behavior
| Breakpoint | Approx width | Notes (proposed) |
|---|---|---|
| Mobile | <480px | Single-column product grid; hamburger nav drawer (`.header__mobile` confirmed present); state-select pill full-width |
| Tablet | 480–1024px | Two-column product grid; filter menu collapses into `Show menu` accordions as page text suggests |
| Desktop | >1024px | Multi-column grid; full horizontal nav (`.header__desktop`) with dropdown mega-menus |

Touch targets are recommended at a minimum 44px height for buttons and select controls, consistent with the pill-shaped, heavily-padded select observed in CSS. Menu collapse behavior (accordion "Show menu" panels) is referenced in the supplied text content but no interaction, animation, or breakpoint values were directly measured — this table is a design recommendation only, not observed site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, JavaScript-driven interaction, hover/focus states, or true responsive breakpoints were observed. Several color-to-role assignments (e.g. accent-gold, accent-berry, accent-mauve, accent-rust, accent-green as badge/varietal accents) are inferred placements of palette colors whose actual UI usage was not confirmed in the supplied rules. Font weights for body-md and caption, all font sizes for display-xl and caption, and all rounded/spacing scale values beyond the two explicitly observed radii (40px pill, 5–10px slider) are proposed conventions, not measurements. Availability and licensing of BrownStd and NoeDisplay as web fonts were not verified; fallback stacks are supplied defensively. Component definitions for hero, footer, product-card, badge, search, text-input, and filter-pill are inferred design patterns appropriate to a wine-subscription DTC storefront, not confirmed observed markup structures.
