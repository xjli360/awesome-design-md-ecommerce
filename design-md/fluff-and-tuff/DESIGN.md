---
version: alpha
name: "Fluff & Tuff"
source_url: "https://fluffandtuff.com"
captured_at: "2026-09-29T04:11:20.739403+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Fluff & Tuff is a BigCommerce-powered storefront for a plush dog-toy brand, evidenced by Stencil theme CSS, product cards with size/price variants (Small/Medium/Large+), and retailer/wholesale flows typical of a wholesale-plus-DTC pet brand. The confirmed typographic system pairs "Clarendon LT Std" for headings and buttons with "Gotham Rounded" for body copy, both falling back to Arial/Helvetica/sans-serif — a serif-slab-meets-rounded-sans combination that reads as friendly but established, fitting a legacy pet-product brand. The dominant heading color is a deep brick-red (#640707), while the primary interactive color is a brighter red (#c2191e) used for primary buttons; these two reds are related but distinct and are preserved as separate roles rather than merged. Neutrals (#555, #757575, #999, #ccc, #e5e5e5) drive body text, borders, and secondary buttons. A warm off-white (#f0edea) appears as a panel/section tone distinct from pure white, and is used here as a soft surface. Additional palette colors (orange, green, blue, tan) are present in the evidence but their exact UI role is not confirmed by the supplied selectors, so they are mapped only to plausible, clearly-labeled inferred roles (status/badge accents). All spacing, radii beyond the confirmed 4px button radius, and most sizing are proposed conventions, not measured values.

colors:
  primary: "#c2191e"
  primary-deep: "#640707"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#555555"
  muted: "#757575"
  hairline: "#cccccc"
  surface-soft: "#f0edea"
  surface-card: "#ffffff"
  panel: "#e5e5e5"
  on-primary: "#ffffff"
  border-strong: "#999999"
  accent-amber: "#f1a500"
  accent-green: "#008a06"
  accent-blue: "#0a6aa1"
  disabled: "#cccccc"
typography:
  display-xl: {fontFamily: "'Clarendon LT Std', Arial, Helvetica, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: 0.25px}
  display-md: {fontFamily: "'Clarendon LT Std', Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0.25px}
  title-md: {fontFamily: "'Clarendon LT Std', Arial, Helvetica, sans-serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.25px}
  body-md: {fontFamily: "'Gotham Rounded', Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Gotham Rounded', Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Gotham Rounded', Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "'Clarendon LT Std', Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.25px}
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
    border: "1px solid {colors.primary}"
    hover: {backgroundColor: "#666666", borderColor: "#666666"}
  button-secondary:
    backgroundColor: "transparent"
    textColor: "#666666"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
    hover: {borderColor: "{colors.border-strong}", textColor: "{colors.ink}"}
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.border-strong}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
    focusBorder: "{colors.accent-blue}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: "72px"
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    overlayButtonBackground: "rgba(255,255,255,0.9)"
    overlayButtonColor: "{colors.ink}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.primary-deep}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.muted}"
    linkColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.muted}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "{colors.primary}"
    selectedTextColor: "{colors.primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.md}"

## Components
**button-primary** renders the confirmed `.button--primary` pattern: brick-red fill (#c2191e), white text, 4px radius (the one directly observed radius value), and a darker-gray hover state matching the theme's `:hover` rule — used for Add to Cart and primary CTAs.

**button-secondary** mirrors the theme's default `.button` (transparent background, #ccc border, #666 text) for lower-priority actions like "Compare" or "Sign in"; hover/active states are proposed extrapolations of the observed pattern scaled to secondary emphasis.

**text-input** is a proposed pattern for search and account forms; border color and padding are inferred from general form-body/panel spacing conventions in the CSS, not a directly observed input rule.

**nav-bar** is a proposed header treatment using canvas background and a hairline bottom border consistent with the theme's neutral palette; exact height and collapse behavior are not measured.

**product-card** reflects observed card-related selectors (`.card-figcaption-body .card-text` in muted gray, `.card-figcaption-button` as a semi-transparent white overlay button) applied to the toy grid (name, size, price, Add to Cart).

**hero** proposes a warm off-white (#f0edea) section background beneath a brick-red display headline, intended for the homepage banner area; no hero-specific selector was supplied, so structure is inferred from brand tone.

**footer** uses the observed `.panel-header` gray (#e5e5e5) as a plausible footer/section background with muted link text, matching the site's link/account footer content (Help, Retailers, Wholesale).

**badge** is a proposed status chip (e.g., "Sold Out", "No Squeak") using an amber accent from the palette; no badge selector was directly observed, so color choice is an inferred, clearly-flagged extrapolation.

**search** and **size-selector** are proposed, category-appropriate patterns: the latter reflects the product data's Small/Medium/Large+ sizing observed in page text, styled as a pill selector using the primary red for the active state.

## Responsive Behavior
This is a proposed responsive recommendation, not measured site behavior; the CSS evidence includes generic BigCommerce breakpoint comments (e.g., 551px, 801px, 1261px, 1681px) suggesting a mobile/tablet/desktop/wide structure.

| Breakpoint | Range | Layout guidance |
|---|---|---|
| mobile | <551px | Single-column product grid, stacked nav, full-width buttons |
| tablet | 551–800px | 2-column product grid, condensed nav |
| desktop | 801–1260px | 3–4 column product grid, full nav bar |
| wide | 1261px+ | 4+ column grid, max-width content container |

Touch targets should be at least 44px tall for buttons and size-selector chips. Navigation should collapse into a hamburger/menu toggle below 801px, consistent with the "Toggle menu" label present in page text, though the exact collapse mechanism was not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Extraction is static (CSS + text only); no live rendering, computed styles, or DOM screenshots were captured, so actual layout, spacing rhythm, and grid structure are not observed.
- Only "Gotham Rounded" and "Clarendon LT Std" are confirmed brand fonts tied to explicit selectors; other font names in the evidence (Montserrat, Open Sans, Source Sans Pro) may belong to third-party widgets and are excluded from tokens.
- Font licensing/availability for "Gotham Rounded" and "Clarendon LT Std" as web fonts is not verified; fallback stacks are required in production.
- Several palette colors (amber, green, blue, tan tones) have no directly observed selector role; their use in `badge`, `search`, and focus states is inferred and should be validated against real components.
- All spacing scale values and most typography sizes beyond the base body/heading rules are proposed conventions, not measured pixel values.
- No interaction states (focus rings, transitions beyond the documented button hover/active), mobile menu behavior, or cart/drawer UI were observed in the supplied evidence.
- Component definitions (hero, footer, nav-bar, text-input, search, size-selector) are structurally plausible proposals based on brand tone and page text, not confirmed markup/CSS selectors.
