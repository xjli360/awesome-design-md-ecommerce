---
version: alpha
name: "Still Life Ceramics"
source_url: "https://stilllifeceramics.com"
captured_at: "2026-09-28T09:50:29.441511+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Still Life Ceramics is an LA-based storefront for handmade pottery, functional art,
  and community classes, built on a Shopify theme exposing CSS custom properties for
  color, spacing, and type rather than fixed literal values. The observed palette is
  warm and craft-forward: a terracotta/clay red (#b6534c) reads as the most brand-specific
  accent among the supplied hexes and is proposed here as primary, evoking fired clay
  and glaze work. A muted sage (#747f6b) and dusty mauve (#97798c) appear alongside
  soft taupe (#cbc5bc) and thistle (#d8bfd8), suggesting a secondary earth-and-botanical
  accent set fitting for handmade homewares; their exact UI roles are not confirmed by
  the CSS and are treated as inferred. Neutrals dominate: near-black text tones (#212121,
  #363636), warm-white surfaces (#fafafa, #f5f5f5), and light hairlines (#e2e2e2, #cccccc)
  support a gallery-like, product-forward layout typical of the theme's card and grid
  patterns. Font stacks reference Avenir, Avenir Next, Helvetica Neue, Montserrat, and
  Quicksand as available families, but the CSS only exposes var(--font-body)/
  var(--font-heading) without resolved values; Montserrat/Quicksand are proposed for
  display and heading roles, with Avenir/Helvetica Neue/Arial proposed for body copy,
  both labeled inferred pending confirmation.

colors:
  primary: "#b6534c"
  secondary: "#747f6b"
  ink: "#212121"
  canvas: "#ffffff"
  body: "#363636"
  muted: "#757575"
  hairline: "#e2e2e2"
  surface-soft: "#f5f5f5"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-mauve: "#97798c"
  border-strong: "#cccccc"
  link: "#1773b0"
typography:
  display-xl: {fontFamily: "Montserrat, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Quicksand, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Avenir, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Avenir, 'Helvetica Neue', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Avenir, 'Helvetica Neue', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    borderColor: "{colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    height: "64px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlayColor: "#00000033"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  class-listing-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    accentColor: "{colors.accent-mauve}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the terracotta accent as a solid call-to-action fill (e.g. "Add to Cart," "Book a Class"), with white text for contrast; this mapping is inferred since the CSS shows only a rgba/white icon color, not a resolved button fill.

**button-secondary** is a lower-emphasis outlined variant for actions like "View Details" or filter toggles, using the observed hairline gray as its border and ink text; hover/active states are proposed, not observed.

**text-input** covers newsletter, search, and checkout fields with a white background and thin hairline border consistent with the theme's light, minimal aesthetic; focus outline should follow the CSS's observed `outline-color:Highlight` accessibility rule.

**nav-bar** models the header, which the CSS confirms has a transparent variant (`.header--transparent`) with white text and a translucent white/20% border, likely for hero-overlay states; a solid canvas-background variant is proposed for scrolled/inner pages.

**product-card** represents shop grid tiles (mugs, bowls, platters) with a soft off-white card surface and a thin hairline border to separate product photography from the page background, per the theme's `--radius-2` token informing a subtle corner radius.

**hero** proposes a full-bleed banner using dark ink as an overlay backdrop for imagery, matching the transparent-header pattern where light text sits over photography; exact hero copy/layout was not present in the supplied evidence.

**footer** uses the lighter surface-soft tone with muted gray text for secondary links (Wholesale, FAQs, Clay for a Cause), consistent with the theme's understated neutral palette.

**badge** is proposed for tags like "Local Artist" or "Handmade," using the sage secondary color as a small pill accent — an inferred use of a palette color not otherwise assigned a confirmed UI role.

**search** models the site's search/currency-selector overlay implied by the large country/currency list in the page text, styled as a soft-background input consistent with text-input.

**class-listing-card** is a category-specific component for the site's pottery Classes offering, using the mauve accent as a distinguishing highlight against standard product cards, with generous internal padding for schedule/description text.

## Responsive Behavior

Recommended breakpoints (not measured from live site):

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | < 480px | Single-column product grid, collapsed nav to hamburger menu |
| tablet | 480–860px | Matches theme's `--max-width-small: 860px`; 2-column grid |
| desktop | 860–1260px | Matches theme's `--max-width: 1260px`; 3–4 column grid |
| wide | > 1260px | Content capped at max-width, centered |

Touch targets should meet a minimum 44px height, aligning with the theme's `--height-button: 44px` token. Navigation is expected to collapse into a slide-out or overlay menu below tablet width (the theme defines `--z-index-flyouts` and `--z-index-header` tokens consistent with an off-canvas pattern), though this interaction was not directly observed. All breakpoint values and collapse behavior are proposed recommendations, not confirmed measurements.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS/text extraction only; no live rendering, screenshots, or DOM interaction was performed. Several limitations apply: (1) the theme's `var(--font-body)` and `var(--font-heading)` custom properties were never resolved to concrete font names in the supplied CSS, so Montserrat/Quicksand/Avenir role assignments are inferred from the available font-family list, not confirmed; (2) hex-to-role mapping (e.g. primary = #b6534c, secondary = #747f6b) is a stylistic proposal based on visual plausibility for a ceramics brand, not a captured computed style; (3) component states such as hover, focus, disabled, and active were not present in the evidence beyond a generic `:focus` outline rule; (4) mobile/responsive layout, breakpoint pixel values, and navigation collapse behavior are proposed conventions, not measured; (5) spacing and radius scales follow a standard proposed system rather than the theme's actual `--spacing-*` custom properties, which use a different scale (5/10/20/40px and rem-based large values); (6) font licensing and self-hosting availability for Montserrat, Quicksand, and Avenir were not verified and should be confirmed before implementation.
