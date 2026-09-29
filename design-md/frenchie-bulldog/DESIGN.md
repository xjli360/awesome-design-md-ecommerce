---
version: alpha
name: "Frenchie Bulldog"
source_url: "https://frenchiebulldog.com"
captured_at: "2026-09-28T09:35:33.203416+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Frenchie Bulldog is a Shopify-based pet-apparel storefront selling harnesses,
  leashes, collars, hoodies, and print-matched accessories (Chalk Art, Gummies,
  Veggies) for French Bulldogs and other small breeds. The observed CSS custom
  properties define a two-tier type system: a display face, "CooperBlackProRegular"
  (34px/700/1.2 line-height), used for headers, and a workhorse sans, Montserrat
  (16px/300/1.6), for body copy. Both fall back to generic sans-serif, so the
  distinctive rounded-slab display letterform is not guaranteed to render for
  visitors without the licensed font.
  The palette is dominated by neutral grayscale (#ffffff canvas, #1c1d1d ink,
  #444444 body text, #999999 muted, #f0f1f3 hairline — this last taken directly
  from the observed .site-header border-bottom). A single teal, #20b2bb, appears
  explicitly on .sizing-chart h1 and is proposed here, by inference, as the
  brand's primary interactive/heading accent color since no button-fill hex was
  resolvable from the CSS variables (--colorBtnPrimary is indirected). Supporting
  accents — #d02e2e (sale/alert), #56ad6a (charity/eco messaging, matching the
  site's "giving back" copy), and #f4af29 (gold highlight) — are drawn from the
  supplied swatch list and assigned semantic roles by inference only, not by
  confirmed selector usage. Card and soft-surface tones use #f4f4f4 and #f6f6f6,
  both present in the palette.

colors:
  primary: "#20b2bb"
  ink: "#1c1d1d"
  canvas: "#ffffff"
  body: "#444444"
  muted: "#999999"
  hairline: "#f0f1f3"
  surface-soft: "#f6f6f6"
  surface-card: "#f4f4f4"
  on-primary: "#ffffff"
  accent-alert: "#d02e2e"
  accent-charity: "#56ad6a"
  accent-gold: "#f4af29"
  accent-deep: "#8b0000"
  surface-success-soft: "#ecfef0"
typography:
  display-xl: {fontFamily: "CooperBlackProRegular, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.0em}
  display-md: {fontFamily: "CooperBlackProRegular, sans-serif", fontSize: 34px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.0em}
  title-md: {fontFamily: "CooperBlackProRegular, sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0.0em}
  body-md: {fontFamily: "Montserrat, sans-serif", fontSize: 16px, fontWeight: 300, lineHeight: 1.6, letterSpacing: 0.0em}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 300, lineHeight: 1.5, letterSpacing: 0.0em}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.02em}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.04em}
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    border-bottom: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    ctaBackgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge-sale:
    backgroundColor: "{colors.accent-alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.base}"
  pattern-swatch:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.primary}"
    rounded: "{rounded.full}"
    size: "{spacing.xl}"

## Components

**button-primary** uses the inferred teal accent (`{colors.primary}`) as fill with white text, intended for the header "Shop Now" CTA and add-to-cart actions; the exact fill hex is not directly observable since `--colorBtnPrimary` is a Shopify theme variable not resolved in the supplied CSS, so this mapping is proposed.

**button-secondary** is an outlined, white-fill variant for lower-emphasis actions (e.g., "View all"), proposed to reuse the primary teal as a border/text color for visual consistency without competing with primary CTAs.

**text-input** covers newsletter and search fields, using the observed hairline gray (`#f0f1f3`) for borders and Montserrat body type; padding and radius are proposed defaults, not measured.

**nav-bar** reflects the one confirmed structural rule in evidence — `.site-header { border-bottom-color: #f0f1f3 }` — establishing a light, low-contrast divider beneath a white header bar; the collapsed hamburger/search/cart icon cluster referenced in page text (icon-hamburger, icon-search, icon-cart) is proposed as a right-aligned icon group.

**product-card** is proposed for the Chalk Art / Veggies / Gummies print carousels described in the page text, using the light card surface and title/price type pairing; card boundaries and shadow are not confirmed in the CSS evidence.

**hero** models the observed slideshow pattern (`.slideshow__slide--image_* .btn-custom-cta { background-color:#ffffff }`), showing a white CTA button overlaid on a full-bleed image slide; the surrounding soft background is proposed.

**footer** is proposed as a dark ink-on-white inversion, consistent with typical Shopify footer patterns and the observed presence of newsletter, social, and legal-link content in page text; no footer background hex was directly observed.

**badge-sale** maps to the repeated "Sale" navigation entries (Sale Harnesses, Sale Leashes, Sale Collars) using the observed red `#d02e2e`; pill shape and placement are proposed, not measured.

**search** is proposed using the observed soft surface tone and hairline border, standing in for the theme's `icon-search` trigger and expandable search field.

**pattern-swatch** is a category-specific component addressing the site's signature pattern/print system (Chalk Art, Gummies, Veggies) referenced repeatedly across product variants; circular swatches with a primary-colored selected ring are proposed to let shoppers pick a print across harness, leash, collar, and bandana SKUs.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior (no media queries were present in the supplied CSS evidence):

| Breakpoint | Width      | Layout guidance                                  |
|-----------|-----------|---------------------------------------------------|
| mobile    | <600px    | Single-column product grid, collapsed hamburger nav, sticky cart icon |
| tablet    | 600–959px | 2-column product grid, inline search icon expands to full-width field |
| desktop   | ≥960px    | 3–4 column product grid, persistent horizontal nav with dropdown categories |

Touch targets for nav icons, swatches, and buttons should be at least 44×44px regardless of breakpoint. Below tablet width, the primary nav is expected to collapse into the `icon-hamburger` menu referenced in page text; cart and search likely remain as persistent icon triggers. None of this collapse/expand behavior was directly observed in a rendered viewport.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS custom properties, a limited selector sample, and page text, not a rendered or interactive audit. The primary brand accent (`#20b2bb`) is inferred from a single confirmed usage (`.sizing-chart h1`) and may not represent the actual global button/link color, since `--colorBtnPrimary` and `--colorBody` theme variables were referenced but never resolved to hex in the supplied evidence. Semantic assignments for sale, charity, and gold accent colors are inferred from page copy (sale collections, "giving back to charities") rather than confirmed CSS selector usage. All component paddings, radii, and breakpoints beyond the two explicit `--typeHeaderSize`/`--typeBaseSize` values are proposed, not measured. The display font "CooperBlackProRegular" is a custom/proprietary-looking face; its licensing, hosting, and actual browser availability were not verified, and it falls back to generic sans-serif. No mobile menu, cart drawer, or hover/focus interaction states were observed in a live browser session — all such states are proposed conventions only.
