---
version: alpha
name: "Magnetic Me"
source_url: "https://magneticme.com"
captured_at: "2026-09-28T10:15:41.873608+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Magnetic Me's storefront CSS shows a black-and-cream foundation overlaid with a
  wide, saturated accent palette (red, yellow, aqua, violet, orange, pink, green)
  used to color-code the button hover states referenced by CSS custom properties
  such as var(--color-yellow) and var(--color-aqua). This pattern is treated as
  evidence of a playful, category-coded color system typical of a kids'/baby
  apparel brand, though the exact hex-to-name mapping for every variable is
  inferred rather than directly confirmed in the supplied rules. Button
  typography (14px, weight 600, 24px line-height, 0.56px letter-spacing,
  uppercase, font-family Serenity) is directly observed and forms the basis for
  the button-md token. Heading and body typefaces ("SangBleu OG Sans",
  "untitled sans", and the decorative "Magnetic Embroidery Block/Tennessee"
  families) are present in the font list but their specific selectors were not
  supplied, so their assigned roles (display, body) are inferred from naming
  and typical usage, not confirmed layout. The interpretation favors a warm,
  off-white canvas ({colors.surface-soft}) with black ink and white-on-black
  primary actions, reserving the bright accent set for badges, category tags,
  and playful hover states rather than core UI chrome, since only black/white
  fills were evidenced for primary buttons.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#3f3f3f"
  muted: "#777777"
  hairline: "#dedede"
  surface-soft: "#f8f6f5"
  surface-card: "#faf7f3"
  on-primary: "#ffffff"
  accent-red: "#e73c3e"
  accent-yellow: "#e9dc66"
  accent-aqua: "#9ccdd1"
  accent-violet: "#6771d8"
  accent-orange: "#e4893d"
  accent-pink: "#eb5874"
  accent-green: "#53b49c"
  accent-indigo: "#14098b"
typography:
  display-xl: {fontFamily: "'Magnetic Embroidery Block', 'SangBleu OG Sans', serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'SangBleu OG Sans', serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "'SangBleu OG Sans', serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'untitled sans', Roboto, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'untitled sans', Roboto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'untitled sans', Roboto, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Serenity, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 24px, letterSpacing: 0.56px}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  fabric-swatch-selector:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.ink}"
    rounded: "{rounded.full}"
    labelTypography: "{typography.caption}"
    padding: "{spacing.xxs}"

## Components
**button-primary** renders as a solid black fill with white text and square corners, matching the `.btn-negative` rule (`background-color:var(--color-black); color:var(--color-white)`), intended for primary calls to action like "Add to Cart" and "Check Out."

**button-secondary** mirrors the outlined `.btn` rule (white background, black text, 1px black border) that inverts to a solid black fill on hover; proposed hover state is not restyled here since only the base treatment was evidenced.

**text-input** is a proposed field style using the neutral hairline border and off-white canvas seen across the palette; no explicit input CSS was supplied, so padding and radius are proposed defaults.

**nav-bar** reflects the extensive multi-level navigation text content (Baby, Toddler & Kids, Family Matching, Nightwear, Daywear, etc.) implied by the page structure; visual chrome (height, sticky behavior) is proposed, not measured.

**product-card** is inferred from standard Shopify PLP/PDP conventions given this is a Shopify-hosted theme (`theme.mfmDWwQs.min.css`); card background uses the warm off-white surface tone rather than pure white to match the observed cream swatches.

**hero** proposes a soft cream backdrop with a large embroidery-style display headline, referencing the "Magnetic Embroidery" font family names and the brand's promotional copy ("More Time For the Moments That Truly Matter"); no hero layout was directly observed.

**footer** is proposed as a black band with white text for contrast, consistent with the black/white core system; content grouping (link columns, newsletter) is inferred from the large nav/footer taxonomy in the page text, not confirmed footer markup.

**badge** proposes a red pill for sale/new tags, drawing on the vivid `#e73c3e` red present in the palette and the "Sale" and "New Arrivals" navigation items; exact badge styling was not present in the supplied CSS.

**search** proposes a lightweight bordered field consistent with the input treatment; presence of a search UI is inferred from typical ecommerce patterns, not confirmed by evidence.

**fabric-swatch-selector** is a category-appropriate proposed component for choosing between the brand's named fabrics (Modal, RightFit™, CloudStretch™, Pointelle, Organic Cotton, Waffle, Chenille, Velour) listed in the navigation text; a circular swatch with a bold selected-state border is proposed, not observed.

## Responsive Behavior
Recommendation only — no responsive/mobile CSS was supplied for verification.

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | 0–599px | Single-column nav collapses to hamburger; mega-menu categories (Baby, Toddler & Kids, Family Matching) stack as accordions |
| Tablet | 600–959px | 2-column product grid; sticky add-to-cart on PDP |
| Desktop | 960–1279px | 3–4 column product grid; full mega-menu on hover |
| Wide | 1280px+ | 4+ column grid; hero max-width constrained with generous side padding |

Touch targets should be at least 40px (matching the observed `.btn` height of 40px) with `{spacing.sm}`–`{spacing.md}` internal padding. Mobile navigation should collapse the deep category taxonomy into progressive disclosure to avoid overwhelming the user given the breadth of listed subcategories.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from a static snapshot of colors, font-family names, and a handful of CSS rules (chiefly button styles); no rendered layout, computed sizes, or responsive behavior were observed. Font role assignments (e.g., "SangBleu OG Sans" for headings, "untitled sans" for body) are inferred from name and typical convention, not from selector-level evidence, and licensing/availability of the custom "Magnetic Embroidery Block/Tennessee," "Serenity," and "SangBleu OG Sans" families is unverified. The mapping of many accent hexes (yellow, aqua, violet, orange, pink, green) to specific UI roles is inferred from the button hover CSS variable names (`--color-yellow`, `--color-aqua`, etc.) without confirmed hex values for each variable. Component definitions beyond button-primary/secondary (nav-bar, product-card, hero, footer, search, badge, text-input, fabric-swatch-selector) are proposed patterns appropriate to a Shopify baby-apparel storefront and are not confirmed from supplied markup. Spacing and rounded-corner scales follow the required template structure and are not fully derived from measured values, aside from the observed `border-radius:0` on buttons.
