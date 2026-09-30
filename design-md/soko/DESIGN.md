---
version: alpha
name: "Soko"
source_url: "https://shopsoko.com"
captured_at: "2026-09-28T10:08:58.137811+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  SOKO's storefront CSS exposes a neutral black-and-white foundation (#000000, #ffffff, #111111) layered with warm accent tones drawn from its jewelry materials: a brass/gold badge color (#7e6b45) used for "best seller" labeling, a wood-brown pairing (#603021, #452318) evocative of the brand's wood-and-metal pieces, and a muted gold (#bf9b30) that reads as a plausible accent for gold-plated product lines. Reds (#d02f2e, #a70100, #db4827) and a green (#478947) appear alongside badge and status selectors and are treated here as sale/eco-badge accents, inferred rather than confirmed as primary brand color. Several blues (#007aff, #142fbd, #0071ce, #eb001b, #f79e1b) originate from Swiper carousel defaults and payment-icon SVGs bundled in the CSS and are excluded from the brand palette as non-semantic library artifacts.
  Typography uses two observed families — Outfit and Cabin — with no serif or script face present. Outfit is assigned to display/heading roles for its geometric, modern character fitting "modern jewelry" positioning; Cabin is assigned to body copy as a warmer humanist workhorse. Root CSS confirms a 4px spacing unit and a 16px chat-widget border-radius, both reused directly below. All exact heading pixel sizes are inferred approximations from the site's rem-based custom properties, since the true root font-size was not confirmed in the supplied evidence.

colors:
  primary: "#000000"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#aaaaaa"
  hairline: "#e8e8e8"
  surface-soft: "#f5f5f5"
  surface-card: "#fcfcfc"
  on-primary: "#ffffff"
  accent-gold: "#bf9b30"
  accent-brass: "#7e6b45"
  accent-wood: "#603021"
  accent-wood-dark: "#452318"
  accent-green: "#478947"
  accent-sale: "#d02f2e"
typography:
  display-xl: {fontFamily: "Outfit, sans-serif", fontSize: "56px", fontWeight: 600, lineHeight: 1.05, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Outfit, sans-serif", fontSize: "40px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Outfit, sans-serif", fontSize: "24px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "Cabin, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0px"}
  body-sm: {fontFamily: "Cabin, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Cabin, sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.5px"}
  button-md: {fontFamily: "Outfit, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1, letterSpacing: "0.5px"}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
  material-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent-brass}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-sale}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.xs}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary**: Solid black fill with white text, used for primary calls to action such as "Add to Cart" and "Checkout." Rounded corners follow the small 4px radius consistent with the theme's compact input controls. Hover/pressed states are not observed and are proposed as a modest opacity or invert shift.

**button-secondary**: An outlined variant using the same ink color for border and text on a white background, intended for secondary actions like "View Details" or filter toggles. Proposed only; no CSS-confirmed outline style was present in the evidence.

**text-input**: A bordered field using the near-white hairline color for its border and white background, matching the theme's `--height-input: 48px` custom property. Focus-state color is inferred to reuse the site's link-focus outline variable referenced in the CSS (`--color-text-link`), though the token's resolved hex was not supplied.

**nav-bar**: A white, hairline-bordered bar housing the mega-menu categories (Earrings, Rings, Bracelets, Necklaces, etc.) visible in the page text. Typography uses the smaller Cabin body size for density across the many category links; layout wrapping behavior is not observed.

**product-card**: A neutral card surface for grid listings, pairing a body-weight product title with a smaller price line. Card background uses a near-white "fcfcfc" tone versus pure white canvas to imply subtle separation, though no shadow or border value was directly confirmed for cards.

**material-badge**: A pill-shaped label proposed for surfacing material metadata (Gold-Plated, Silver, Wood, Mixed Materials) seen in the site's filter taxonomy. Uses the brass accent color sourced from the observed `best-seller` badge rule, repurposed here for material tagging since no distinct material-badge color was separately evidenced.

**hero**: A large display banner using the largest inferred type scale, intended for homepage messaging such as the brand's Nairobi-based, sustainable-materials story. Background uses the light gray surface tone; no hero-specific background color was directly observed, so this is an inferred proposal.

**footer**: An inverted black footer block with white text, holding informational links (About, Our Impact, Our Materials, FAQ, Press, Contact). Ink/canvas inversion is proposed for visual weight at page end, not confirmed from footer-specific CSS in the evidence.

**badge**: A compact sale/status marker reusing one of the observed red tones (#d02f2e) for "On Sale" or similar states, since the CSS confirms product-badge selectors exist for handles like `responsible`, `best-seller`, and `new`, though only the latter two had explicit color declarations captured.

**search**: A bordered search field styled consistently with text-input, supporting the "Shop All" and quick-search flyout referenced by the `--z-index-quick-search` custom property. Icon and placeholder styling are not observed.

## Responsive Behavior

The theme's custom properties expose explicit breakpoints, reused here as a proposed layout guide rather than measured rendering:

| Range | Media Query | Proposed Behavior |
|---|---|---|
| ≤479px | `--media-below-480` | Single-column product grid, stacked nav collapses to hamburger + flyout |
| 480–719px | `--media-above-480` | Two-column product grid, condensed header |
| 720–959px | `--media-above-720` | Category mega-menu begins showing inline |
| 960–1199px | `--media-above-960` | Three-to-four column grid, full desktop nav |
| ≥1200px | `--media-above-1200` | Max content width caps at `--max-width: 1400px` |

Touch targets should meet a minimum 44px hit area consistent with the Swiper navigation button sizing (`--swiper-navigation-size: 44px`) observed in the CSS. Flyout/drawer width is confirmed at `460px` on larger viewports via `--flyout-width`, collapsing to `375px + gap` on mobile per the same variable. This table is a recommendation derived from theme tokens, not an observation of actual rendered breakpoint behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is generated from static CSS custom properties, selector fragments, and page text only; no rendered layout, hover/focus states, animation timing, or real breakpoint screenshots were observed. Several palette values (blues, payment-brand reds/oranges) were identified as third-party library or payment-icon artifacts and deliberately excluded from brand role assignment; remaining color-to-role mapping (e.g., accent-gold, accent-wood) is inferred from thematic fit with jewelry materials, not confirmed via direct component screenshots. Font pixel sizes for the type scale are approximated from rem-based custom properties without a confirmed root font-size, so all `typography` values above should be treated as proposed, not measured. Component states (hover, active, disabled, error) are entirely proposed and unverified. Font licensing/availability for Outfit and Cabin as used specifically by SOKO was not verified beyond their presence in the CSS `font-family` declarations.
