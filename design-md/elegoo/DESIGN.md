---
version: alpha
name: "Elegoo"
source_url: "https://www.elegoo.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Electric blue #0035ff arrives at Elegoo with the bluntness of an extruder temperature readout — not a warm lifestyle hue but a binary signal that marks every primary CTA, active filter, and link hover state across the storefront. Below it, the palette is deliberately industrial: near-black #121212 and charcoal #2c2d2e carry most of the above-fold real estate on product pages, aligning the experience closer to machine firmware UI than consumer lifestyle retail. Off-white #f5f5f5 and graduated grays (#dedede, #e2e2e2, #ededed) compose a neutral field for spec sheets and comparison tables, each register one step lighter per layer of depth. Two accent voltages punctuate that neutral field: chrome-yellow #ffd100 claims promotional badges and sale callouts with an almost physical urgency, while violet #a75bff surfaces on specific product-tier labeling — likely marking a resin-printer line where resolution specifications become the differentiator worth color-coding. Neither appears in interactive chrome, which keeps #0035ff disciplined as the sole action color. Plus Jakarta Sans drives all display weight at tight negative letter-spacing, its geometric construction reading like tolerance specifications stamped into alloy rather than editorial headings. Poppins handles body copy and microlabels where monolinear strokes hold legibility on dark card surfaces at 12–14px without anti-aliasing artifacts. The pairing creates productive tension: Jakarta's confident geometry at display scale versus Poppins' neutral utility at text scale. Corner radii stay deliberately modest throughout — {rounded.sm} at 4px for input chrome and tight UI elements, {rounded.md} at 8px for product cards, {rounded.lg} at 12px for modal overlays and hero containers. Nothing rounds to a pill except promotional deal labels, which use {rounded.full} to signal limited-time offers rather than navigation. The geometry is flat and Cartesian — no organic softness — which suits a brand whose products physically translate digital mesh files into layered physical objects one 0.05mm slice at a time.

colors:
  primary: "#0035ff"
  primary-active: "#002edb"
  primary-hover: "#1b49ff"
  primary-disabled: "#8099ff"
  accent-yellow: "#ffd100"
  accent-purple: "#a75bff"
  accent-amber: "#f5c076"
  error: "#c62a32"
  ink: "#121212"
  body: "#272727"
  dark-surface: "#2c2d2e"
  muted: "#6d6b6b"
  muted-soft: "#b2b2b2"
  hairline: "#dedede"
  hairline-soft: "#dadce0"
  surface-mid: "#e2e2e2"
  surface-card: "#ededed"
  surface-soft: "#f5f5f5"
  canvas: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Plus Jakarta Sans', Poppins, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Plus Jakarta Sans', Poppins, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Plus Jakarta Sans', Poppins, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Plus Jakarta Sans', Poppins, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.1px
  title-sm:
    fontFamily: "'Plus Jakarta Sans', Poppins, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Poppins, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Poppins, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Poppins, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  label-uppercase:
    fontFamily: "Poppins, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "Poppins, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  price:
    fontFamily: "'Plus Jakarta Sans', Poppins, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.2px
  button-md:
    fontFamily: "'Plus Jakarta Sans', Poppins, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'Plus Jakarta Sans', Poppins, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Plus Jakarta Sans', Poppins, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
  full: 9999px

spacing:
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
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.6
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1.5px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
    activeIndicatorColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    imageRounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    shadowResting: "0 1px 4px rgba(0,0,0,0.08)"
    shadowHover: "0 4px 16px rgba(0,53,255,0.12)"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    minHeight: 560px
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
  badge-sale:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  badge-bestseller:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  product-tier-badge:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  spec-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  category-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  promo-banner:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.section}"
    textAlign: center
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    height: 42px
    iconColor: "{colors.muted}"
  price-display:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    salePriceColor: "{colors.error}"
    originalPriceDecoration: line-through
    originalPriceColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The electric-blue (#0035ff) primary button is Elegoo's most direct visual element: 44px tall with {rounded.sm} 4px corners and 600-weight Plus Jakarta Sans at 15px, it reads like a status indicator on industrial equipment rather than a soft consumer CTA. Hover lightens fractionally to #1b49ff, active compresses to #002edb; disabled fades to #8099ff at 60% opacity. A `button-dark` variant using {colors.ink} fill appears on light-canvas pages where the blue CTA would compete with product imagery.

**`button-secondary`** — Outlined variant matching primary dimensions at 1.5px #0035ff border and transparent fill. Border and label both shift to {colors.primary-active} on activation; the background picks up {colors.surface-soft} to provide tactile feedback without flooding the button with color.

**`button-ghost`** — Transparent background with {colors.body} text at {typography.button-sm}; used for low-priority actions in spec-comparison sidebars and filter panels where adding color would saturate an already-dense layout.

### Text Input

**`text-input`** — Flat-topped with {rounded.sm} 4px corners, inputs default to a {colors.hairline} (#dedede) border that swaps to {colors.primary} blue on focus — the same voltage as the primary button, ensuring form fields feel connected to the action system. Height holds at 42px, 2px shorter than the 44px button, which subtly groups form and submit without merging them visually.

### Navigation

**`nav-bar`** — 72px tall on white canvas with a 1px {colors.hairline} underline. Navigation links use {typography.nav-link} at 14px/500 weight — understated next to the brand logo — and the active category receives a {colors.primary} underline indicator rather than a filled chip. Search and cart icons sit in the right cluster at 24px glyph size, padded to 44px touch targets. On scroll, the bar does not collapse: Elegoo's category depth requires persistent access to printer-line navigation.

### Product Card

**`product-card`** — White canvas with {rounded.md} 8px corners on both the card frame and the product image swatch. On hover, the drop shadow deepens with a #0035ff-tinted value (0 4px 16px rgba(0,53,255,0.12)) — a blue halo spills from the card edge, reinforcing primary voltage at the point of selection rather than at a button. Price in {typography.price} and title in {typography.title-md} occupy the lower third; spec tags ({spec-tag}) tile horizontally above the title for build volume, layer height, and connectivity callouts.

### Hero Banner

**`hero-banner`** — Full-bleed dark (#121212) hero with the display headline in {typography.display-xl} Plus Jakarta Sans at 48px and {colors.primary} blue used for emphasis spans or CTA button fill. A secondary ghost/outline button in white stroke sits beside the primary CTA on comparison and category landing pages. Minimum 560px height gives the hero enough mass to frame large product-render photography without the image feeling cropped.

### Badges

**`badge-sale`** — Pill-shaped ({rounded.full}) in chrome-yellow #ffd100 with near-black {colors.ink} text; the contrast is intentionally loud, functioning at the scale of a clearance sticker rather than a UI label. **`badge-new`** — Same pill geometry in {colors.primary} blue with white text, reserved for recently launched SKUs. **`badge-bestseller`** — Charcoal {colors.dark-surface} pill with white text signals a permanent catalog-tier designation rather than a promotional state. **`product-tier-badge`** — Violet #a75bff pill marks product-line differentiation (resolution tier, flagship feature set) without the sale or urgency signal of the yellow.

### Promo Banner

**`promo-banner`** — Full-width sitewide bar in chrome-yellow #ffd100 with {typography.body-sm} Poppins text in near-black ink. The yellow is used nowhere else at this horizontal scale, giving the banner immediate recognition at page load. Collapses to {spacing.base} horizontal padding on mobile and may wrap to two lines; the yellow background makes the line-break graceful rather than broken.

### Search Bar

**`search-bar`** — Inset into the nav right cluster with {colors.surface-soft} fill rather than pure white, distinguishing it from page body content at a glance. Focus ring switches border to {colors.primary} blue; the magnifier icon renders at {colors.muted} (#6d6b6b) at rest and deepens to {colors.ink} on focus. On mobile, the search bar expands to a full-width overlay drawer on tap rather than reusing the inline input.

### Price Display

**`price-display`** — Sale price renders in {colors.error} #c62a32 at {typography.price} 22px/700, while the struck-through original price holds {colors.muted} #6d6b6b — the red/gray contrast makes discounts immediately scannable in a product grid of 20+ cards without requiring an additional badge.

### Footer

**`footer`** — Charcoal {colors.dark-surface} (#2c2d2e) spans full bleed below the product grid. Link columns use {typography.body-sm} Poppins at {colors.muted-soft} (#b2b2b2) at rest, brightening to {colors.canvas} white on hover. Column headings use {typography.title-sm} Plus Jakarta Sans at full white. The dark footer against the light-canvas product content creates a deliberate page-end boundary that reads as intentional punctuation rather than a default template footer.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + search icon + cart; hero min-height drops to 320px; promo banner wraps to two lines with {spacing.base} horizontal padding; category chips scroll horizontally in a no-wrap row |
| Tablet | 744–1128px | 2-column product grid; nav shows primary printer-line links with overflow menu; hero holds two-column layout with headline left, product render right |
| Desktop | 1128–1440px | 3–4 column product grid; full nav bar with all category links visible; hero spans full width with left-aligned CTA cluster |
| Wide | > 1440px | Content centered in max-width 1440px container; product grid can expand to 5 columns; hero image scales within the container without stretching |

### Touch Targets
- All interactive elements maintain minimum 44×44px touch area
- Nav icon buttons (search, cart, account) use transparent padding to reach 44px without visual bulk
- Category chips enforce min-width 48px to prevent tap errors on dense horizontal filter rows
- Badge pills include 8px invisible hit-area expansion on mobile to avoid tap misses near card edges
- Promo banner link text padded to 44px vertical tap height even when typographic line is shorter

### Collapsing Strategy
- Primary nav: utility links (Account, Cart, Search) remain visible at all widths; category nav folds into a slide-out drawer behind a hamburger at < 744px
- Spec tags on product cards: show first 3 on mobile with a "+N" overflow chip; all tags visible on tablet and above
- Hero headline: collapses from {typography.display-xl} (48px) → {typography.display-md} (32px) on tablet → {typography.display-sm} (24px) on mobile
- Footer: 4-column link grid → 2-column on tablet → single-column accordion on mobile with expand/collapse per section
- Search: full-width overlay drawer on mobile tap; inline input in nav on tablet and above

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Pure white `#ffffff` was not present in the extracted hex list; `canvas` white is assumed as the standard Shopify default background and was not directly confirmed from live extraction
- `primary-disabled` (#8099ff) is derived by desaturation from the extracted blue range — not directly sampled from the live site
- Exact border-radius values were not measured from the live DOM; {rounded.sm} (4px) and {rounded.md} (8px) are inferred from the engineering-product aesthetic and common Shopify theme patterns
- Button and input heights (44px, 42px) are inferred from visual proportion patterns, not extracted from computed styles
- Whether the site operates a dark-mode default or uses dark surfaces only in hero/footer sections is unclear from extraction; both #121212 and #f5f5f5 appear prominently in the palette
- The exact product-line assignment for violet #a75bff (SATURN, MARS, NEPTUNE, or another sub-brand) could not be confirmed without deeper navigation-state traversal
- Variable font axis availability for Plus Jakarta Sans (weights 500, 600 beyond the standard 400/700) is assumed but not confirmed from the extracted font stack
- Hover and focus transition durations and easing curves were not extractable from the live site
