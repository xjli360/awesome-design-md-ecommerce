---
version: alpha
name: "Greenwich Letterpress"
source_url: "https://greenwichletterpress.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Instrument Serif and Instrument Sans arrive as a matched type pair — siblings from the same family, sharing proportions and stroke rhythm — which is an uncommon choice for a stationery brand. Most letterpress shops reach for unrelated historical pairings (a grotesque with a slab, a transitional with a geometric) to signal hand-craft credibility; Greenwich instead trusts the internal tension between the serif's editorial weight and the sans's clean utility to do that work. The extracted palette cleaves into three distinct registers: a near-black field of #191919 and #121212 forming the ink layer; a gray infrastructure of #dedede, #c8c8c8, #777777, and #555555 building the card skeleton and divider system; and two deep chromatic anchors — #8b0000, a Venetian-press crimson, and #006400, the green of a British wax-seal die — that share primary-signal duties across CTAs and collection callouts. Against this composed palette, #3ed660 reads as a deliberate override: too saturated for the shop's base register but immediately legible as a promotional signal against dark backgrounds. The amber #ee9441 appears on price badges and sale callout elements, warm enough to hold against both canvas and card surfaces without a border. CTAs sit in the crimson ({colors.primary}) with near-zero border radius ({rounded.xs}), recalling the squared impression of a letterpress block pressed against dampened cotton stock. Pill shapes and soft corners are absent from primary actions; they appear only in filter chips and tag labels where information density demands compact containment. Jost occupies the functional type layer — paper grades, quantity selectors, order reference codes — running at 11–12px with generous tracking, staying optically separate from the Instrument hierarchy above. The overall effect is a shop that reads like a paper goods catalog: dense with product, restrained in decoration, and anchored by chromatic sobriety that makes the two brand colors feel like printed inks rather than interface conventions.

colors:
  primary: "#8b0000"
  primary-active: "#6b0000"
  primary-disabled: "#c4a0a0"
  secondary: "#006400"
  accent-amber: "#ee9441"
  promo: "#3ed660"
  ink: "#191919"
  deep-ink: "#121212"
  body: "#555555"
  muted: "#777777"
  hairline: "#dedede"
  hairline-soft: "#c8c8c8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.01em
  body-md:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  label:
    fontFamily: "'Jost', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.04em
  price-display:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  mono:
    fontFamily: "monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 44px
    textTransform: uppercase
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
    textTransform: uppercase
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    logoTypography: "{typography.display-sm}"
    borderBottom: "1px solid {colors.hairline}"
    height: 56px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    hoverBorder: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    imageAspectRatio: "3/4"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  sale-badge:
    backgroundColor: "{colors.promo}"
    textColor: "{colors.deep-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  amber-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.canvas}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  price-display:
    currentPriceColor: "{colors.ink}"
    originalPriceColor: "{colors.muted}"
    salePriceColor: "{colors.primary}"
    currentTypography: "{typography.price-display}"
    originalTypography: "{typography.body-sm}"
    originalTextDecoration: line-through
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.hairline}"
  paper-swatch-selector:
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.ink}"
    rounded: "{rounded.none}"
    size: 32px
    gap: "{spacing.xs}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    activeBg: "{colors.ink}"
    activeText: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  footer:
    backgroundColor: "{colors.deep-ink}"
    textColor: "{colors.hairline}"
    linkColor: "{colors.canvas}"
    headingTypography: "{typography.label}"
    bodyTypography: "{typography.caption}"
    paddingVertical: "{spacing.section}"
  order-reference:
    textColor: "{colors.muted}"
    typography: "{typography.mono}"
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    padding: 2px 6px

## Components

### Buttons

**`button-primary`** — The primary CTA — Add to Cart, Checkout, Submit — runs in #8b0000 crimson with {rounded.xs} (2px) corners, echoing the squared impression of a letterpress die against cotton stock. Text runs in {typography.button-md} with 0.04em tracking and uppercase transform, giving the label the structural density of a monogram stamp. On hover it steps to {colors.primary-active} (#6b0000) with no shadow or elevation shift; the brand treats depth as a printing term, not a UI cue. Disabled state uses {colors.primary-disabled}, a desaturated rose that holds layout space without drawing attention.

**`button-secondary`** — An outlined variant carrying {colors.primary} text on a {colors.canvas} ground, bordered with a 1px crimson stroke. Used for secondary purchase flows — Save to Wishlist, View Details, Add to Registry — and for paired-button layouts where hierarchy needs to be visible at a glance. Maintains the same 44px height and uppercase label treatment as the primary so vertical rhythm is unbroken across CTA pairs.

**`button-ghost`** — A {colors.ink} label on transparent ground with a 1px {colors.hairline} border. Used for low-hierarchy actions: Continue Shopping, Clear Filters, Cancel. Sits in the gray register and recedes visually when placed beside a primary or secondary CTA, drawing the eye to the action with actual priority.

### Form Elements

**`text-input`** — Fully squared ({rounded.none}), 44px tall, with a 1px {colors.hairline} border that steps to {colors.ink} on focus — no glow, no shadow, just a border weight shift. Placeholder text runs in {typography.body-md} at {colors.muted}, clearing on first keystroke. The shop's preference for clean press-ready rectangles extends to all form elements; no floating labels, no inner icons except the search field.

**`filter-chip`** — Small selectable chips for collection filtering by paper weight, size, format, or occasion. Inactive chips sit in {colors.surface-soft} with a {colors.hairline} border; active chips invert to {colors.ink} ground with {colors.canvas} text. Rounded to {rounded.sm} (4px) — the only component class that relaxes the near-zero radius rule, since filter tags appear at density where modest softening aids visual parsing.

**`paper-swatch-selector`** — 32×32px flat squares representing paper stock or envelope color options. No border radius; the selected state uses a 2px {colors.ink} inset border that mimics the registration marks used in letterpress makeready. Swatches are arranged in a tight row with {spacing.xs} gaps, scannable at a glance without needing labels unless a color name is ambiguous.

### Navigation

**`nav-bar`** — 56px tall on desktop, {colors.canvas} background, separated from page content by a 1px {colors.hairline} bottom border. The wordmark or logo runs in {typography.display-sm} (Instrument Serif, 22px, weight 400), positioned left. Primary category links run in {typography.caption} (Jost, 12px, 0.04em tracking), center or right-aligned depending on layout. Cart count appears as a plain {colors.ink} digit beside a bag icon with no colored bubble. No mega-menu; category fly-downs use a {colors.surface-soft} panel that slides below the nav rail.

**`breadcrumb`** — Runs in {typography.caption} at {colors.muted}, with a plain "/" separator at the same color. The current page segment steps to {colors.ink}. No chevron or arrow glyphs — the separator matches the type register of the surrounding label text, avoiding any illustrative elements that would break the catalog-page reading mode.

### Product Elements

**`product-card`** — Image fills a 3:4 portrait frame with {rounded.none}, placing photography in proportions that mirror a standard greeting card or notecard. Below the image: product name in {typography.title-sm}, paper spec or subtitle in {typography.caption} at {colors.muted}, price in {typography.price-display}. No rounded corners, no drop shadow — a flat tile that reads as a catalog entry. Hover does not lift the card; instead a thin 1px {colors.hairline} border appears around the tile, signaling interactivity through containment rather than elevation.

**`sale-badge`** — A flat rectangle in {colors.promo} (#3ed660) with {colors.deep-ink} text at {typography.label} (uppercase Jost, 11px). Positioned at the top-left corner of the product image with {rounded.none}. The saturated green is deliberately incongruous with the shop's muted palette — it functions as a spot color, the digital equivalent of a neon sale sticker on a printed catalog page. It should appear only on genuinely reduced items, not as a permanent promotional fixture.

**`amber-badge`** — Same flat rectangle structure as `sale-badge` but in {colors.accent-amber} (#ee9441), used for new arrivals, seasonal collection flags, or editor's pick callouts. The warm amber holds against both the dark hero ground and the light card surface without a border, making it usable across contexts where {colors.promo} would read as sale-specific.

**`price-display`** — Current price in {typography.price-display} at {colors.ink}. When an item is discounted, the original price appears inline in {typography.body-sm} with line-through decoration at {colors.muted}, and the active price shifts to {colors.primary} (crimson) — making the discount legible through color and weight alone, without requiring a badge duplicate.

**`order-reference`** — SKU, order number, and reference codes render in {typography.mono} inside a {colors.surface-soft} capsule with {rounded.xs} corners. This keeps machine-readable strings visually distinct from editorial copy without introducing a special badge component; the monospace face and light background do all the separating work.

### Layout Components

**`hero-banner`** — A full-bleed panel in {colors.ink} (#191919) carrying the Instrument Serif display headline at {typography.display-xl} (48px, weight 400) in {colors.canvas}. The light weight on a dark ground replicates the visual sensation of letterpress where ink barely bites into the stock — present enough to read, light enough to feel precise. A one-line subhead runs in {typography.body-md} below the headline, followed by a single primary CTA. On desktop, editorial photography is inset at 50% width beside the text block; on mobile the image drops and the text block fills full width on the dark ground.

**`category-tag`** — Small uppercase chip labels in {colors.surface-soft}, used in collection header rows and product metadata lines to indicate paper type, occasion, or collection membership. Run in {typography.label} with 0.08em tracking. Used sparingly — no more than two or three per product record — so the Jost uppercase reads as annotation rather than noise.

**`footer`** — {colors.deep-ink} (#121212) background with a four-column link grid. Column headings in {typography.label} (uppercase Jost) at {colors.canvas}; body links in {typography.caption} at {colors.hairline} (#dedede), which reads as a soft warm gray against near-black without appearing disabled. A sub-row at the bottom carries social icons and legal links at reduced opacity. No border separates the footer from the page body — the jump to near-black is the separator.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark + cart; hero headline steps down to {typography.display-md} (32px); filter chips move into a slide-up bottom drawer; paper-swatch-selector rows wrap to two columns |
| Tablet | 744–1128px | Two-column product grid; nav shows wordmark and cart only, categories in hamburger panel; hero retains dark ground but subhead is hidden; breadcrumb visible above grid |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with category links visible; hero splits text left / image right at 50/50; filter sidebar is a persistent left panel |
| Wide | > 1440px | Four-column product grid; hero and content max-width 1440px centered; content gutters expand to {spacing.xxl} on each side |

### Touch Targets

- All interactive elements maintain 44px minimum height on mobile (buttons, inputs, nav links, swatch selectors)
- Filter chips increase padding to 10px 16px on mobile to reach the 44px touch target
- Product card tap region is the full tile including the whitespace below the image
- Paper swatch selectors increase from 32×32px to 40×40px on touch viewports
- Breadcrumb links maintain a minimum 44px tap height via vertical padding extension

### Collapsing Strategy

- Filter sidebar converts to a bottom-sheet drawer on mobile, triggered by a "Filter & Sort" bar pinned above the product grid
- Product grids collapse 4→3→2→1 column as viewport narrows through breakpoints
- Nav categories collapse into a slide-in side panel at tablet and below; the hamburger icon appears at {spacing.base} from the left edge with the wordmark centered
- Footer four-column link grid stacks to two columns at tablet and one column at mobile
- Hero image panel is hidden on mobile; the dark ground and text fill the full viewport width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Pure white canvas (#ffffff) was not present in the extracted color list; it is inferred as the Shopify theme page background and is almost certainly correct, but the computed value was not confirmed from the live site
- Light surface-soft (#f5f5f5) is inferred — extraction surfaced only mid and dark neutrals; the actual value may be a slightly warmer or cooler light gray
- No meta theme-color was set, so the mobile browser chrome accent color is undefined and will default to the OS system color
- Exact border-radius values for Shopify theme components could not be confirmed from extraction; the near-zero-radius approach is inferred from the brand's letterpress aesthetic and the absence of rounded values in the color extraction
- Hover and focus transition durations and easing curves are not confirmed; 150ms ease is assumed as a Shopify theme default
- Font weights for Instrument Serif in active use could not be confirmed; italic variants for product callouts or pull quotes may be in use on the live site but were not captured
- Any custom icon set, illustrated spot art, or hand-drawn ornamental elements could not be extracted from the live site snapshot
- Secondary green (#006400) is present in the extracted palette but its specific UI application (CTA variant, collection color coding, or seasonal theming only) could not be determined without deeper inspection of the live collection pages
