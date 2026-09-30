---
version: alpha
name: "Wiha"
source_url: "https://wihatools.com"
captured_at: "2026-09-28T09:18:28.779318+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Wiha's storefront evidence shows a utilitarian, high-contrast palette built around near-black text (#282828) on a white (#ffffff) canvas, with a saturated red (#d20024) used consistently across sale and promotional badges and a mid-tone blue (#0e72b5) reserved for "new tool" and "web exclusive" callouts. A mustard yellow (#fabb00) marks Pro-Picks promotions and a deep navy (#1e316a) flags stock-up sales, giving the badge system a clear semantic hierarchy that this interpretation preserves and extends into primary/secondary action colors. Body-copy grays (#333333, #444444, #666666, #5d6971) and light neutrals (#f4f6f8, #f9f9f9, #ebeded, #dddddd) suggest a restrained, catalog-dense UI built for professional tool shopping rather than lifestyle imagery. No proprietary webfont was detected in the supplied evidence; the CSS references system sans-serif stacks (Helvetica Neue, Helvetica, Arial) and monospace stacks (Consolas, Menlo, Courier New), which this spec adopts directly rather than inventing a brand typeface. The heading scale (58/42/38/32/22/16px) and body sizes (22/20/18px) come from the site's own CSS custom properties. Component treatments below (badges, product cards, spec tables) are inferred from label class names and are proposed interaction/layout patterns for a professional tool e-commerce experience, not verified visual or interactive observations.

colors:
  primary: "#d20024"
  ink: "#282828"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f4f6f8"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-blue: "#0e72b5"
  accent-yellow: "#fabb00"
  accent-navy: "#1e316a"
  accent-black: "#000000"
  neutral-200: "#ebeded"
  neutral-300: "#cccccc"
  neutral-400: "#9c9c9c"
typography:
  display-xl: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 58px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 38px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Consolas, Menlo, Monaco, Courier New, monospace", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.0, letterSpacing: 0.5px}
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
  lg: 20px
  xl: 32px
  xxl: 48px
  section: 64px
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.xl}"
    hover:
      backgroundColor: "{colors.canvas}"
      textColor: "{colors.ink}"
      borderColor: "{colors.ink}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: "52px"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    skuTypography: "{typography.caption}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    saleBackgroundColor: "{colors.primary}"
    saleTextColor: "{colors.on-primary}"
    newBackgroundColor: "{colors.accent-blue}"
    newTextColor: "{colors.on-primary}"
    proPicksBackgroundColor: "{colors.accent-yellow}"
    proPicksTextColor: "{colors.ink}"
    stockUpBackgroundColor: "{colors.accent-navy}"
    stockUpTextColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: "52px"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary**: Modeled on the observed `--add2cart-bg-color: #282828` / `--add2cart-text-color: #FFFFFF` pair, with an inverted hover state (`--add2cart-bg-color-hover: #FFFFFF`, `--add2cart-text-color-hover: #282828`) taken directly from the CSS custom properties. Used for Add to Cart and primary checkout actions.

**button-secondary**: An outlined ink-on-white variant proposed for secondary actions (e.g., "Shop All", "Learn More") that appear repeatedly in the navigation and promo text; no explicit CSS was captured for this variant, so its border/fill logic is inferred from the primary button's inversion pattern.

**text-input**: Height of 52px is taken directly from `--form-input-field-height`. Border and text colors are inferred from the neutral/hairline palette since no explicit input-focus styling was supplied.

**nav-bar**: A white, ink-on-white header is inferred from the extensive mega-menu category list (Kits & Systems, Screwdrivers, Pliers & Cutters, etc.) implied by the page text; actual sticky/collapse behavior was not observed.

**product-card**: Reflects the `--wrapper-bg-color`, `--image-bg-color`, and hover-state tokens captured in the CSS (white card, off-white `#F9F9F9` hover background). Title, price, and SKU typography map to title-md, body-md, and a monospace caption respectively, the latter inferred to suit the numeric SKU strings visible in the product listings (e.g., "92405").

**hero**: Uses the largest heading token (`--heading-large-font-size: 58px`) against the soft surface color; promotional banners like "SlimLine System Sale — Up to 35% off" suggest a hero/banner pattern, though exact hero layout was not observed.

**footer**: Inverted ink background with white text is proposed to visually anchor the long Support/Kits link list seen in the page text; no footer-specific CSS was supplied, so this is an inferred convention common to catalog sites of this density.

**badge**: Directly grounded in the supplied `.product-card__label--*` rules — red (#d20024) dominates general sale states, blue (#0e72b5) marks "new tool"/"web exclusive," yellow (#fabb00) marks "Pro-Picks," and navy (#1e316a) marks "stock-up" sales. This is the most evidence-backed component in the spec.

**search**: Proposed as a bordered input consistent with the text-input token, sized to the same 52px field height; no dedicated search-bar CSS was present in the evidence.

**spec-table**: A category-appropriate addition for hand tools, proposed to present torque ranges, drive sizes, and insulation ratings (e.g., "3/8\" Drive 10-50 Nm 7-36 lb-ft") seen in product titles, using the soft surface background and caption/body-sm typography for label/value pairs.

## Responsive Behavior

This is a recommendation, not measured site behavior, since no breakpoint-specific layout was captured beyond two sets of root CSS custom properties (a tighter mobile-scale set and a larger desktop-scale set implied by the differing `--heading-*` and `--vertical-breather` values).

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <640px | Single-column product grid; nav collapses to a hamburger/mega-menu drawer; heading sizes use the smaller root scale (e.g., h1 36px). |
| Tablet | 640–1024px | 2–3 column product grid; category mega-menu may remain collapsed or become a horizontal scroll. |
| Desktop | 1024–1440px | Full mega-menu with category flyouts; heading sizes use the larger root scale (e.g., h1 42px, hero 58px). |
| Wide | >1440px | Container gutter (`20px` observed) and max content width govern extra whitespace; grid may expand to 4+ columns. |

Touch targets should be at least 44–46px tall, aligning with the observed `--button-height: 46px`. Mega-menu collapse into an accordion drawer on mobile is proposed, not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Extraction is static: no rendered layout, breakpoints, hover/focus states, or JS-driven interactions (e.g., cart drawer, mega-menu open/close) were directly observed.
- Color-to-role mapping (primary, ink, muted, surface-soft, etc.) is inferred from usage context (badges, backgrounds) rather than an explicit design-token export; all hexes are reused from the supplied palette.
- No proprietary or licensed webfont was found in the evidence; all typography uses system sans-serif (Helvetica Neue/Helvetica/Arial) and monospace (Consolas/Menlo/Courier New) stacks, so brand-specific type licensing has not been verified.
- The `rounded` scale is entirely proposed; no border-radius values were present in the supplied CSS.
- The `spacing` scale blends the site's real custom properties (20px gutter, 48px vertical breather) with a proposed general-purpose scale; exact spacing at all levels was not captured.
- Component states marked "hover" (e.g., button-primary) are grounded in explicit CSS variables; all other interaction states (focus, active, disabled) are proposed and unverified.
- Mobile/tablet navigation and product-grid layouts are inferred from category-list content only, not from observed responsive CSS or screenshots.
