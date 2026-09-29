---
version: alpha
name: "M.Gemi"
source_url: "https://mgemi.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  M.Gemi operates on a Tuesday rhythm — new Italian-made styles arrive once a week, sell in limited quantities, and never restock. That scarcity logic, more than any color choice, shapes every interaction surface: urgency without vulgarity, exclusivity without the velvet-rope aesthetic. The crimson (#bb2832) surfaces at exactly the moments the cadence demands — "NEW THIS WEEK" drop badges, low-stock alerts, primary add-to-cart buttons — and nowhere else. Everything else holds back deliberately: a warm off-white canvas (#f7f6f3), a deep charcoal ink (#161d25) anchoring nav and footer, and the cool slate (#c4cdd5) that the site meta-color declares as its ambient atmosphere, visible in product-image backgrounds and quiet accent placements. The orange (#ff7216) and the steel blues (#849bb6, #4f7a9c) read as promotional moments and interactive depth — not brand pillars.

  Type is the clearest signal of M.Gemi's positioning. 205TF Louize — a French editorial serif designed for publishing houses rather than storefronts — carries every headline and display scale at light-to-regular weights (300–400), set with generous tracking in lowercase. This is unhurried typography that expects the reader to slow down, closer to Vogue Italia than to any Shopify template default. Body and interface copy runs in Helvetica: workaday, invisible, letting Louize carry the brand voice without contest. Courier surfaces at price display — a receipt-from-the-factory conceit that reinforces the direct-from-Italy narrative without spelling it out.

  Buttons are square-cornered (`{rounded.none}`) everywhere in the primary interaction layer. There is no pill shape on a CTA, no rounded softness at the purchase moment — the hard edge signals decisiveness. CTAs sit at 48px with uppercase letter-spacing at 1.2px, enough air to feel engraved rather than printed. Inputs strip to a single bottom border on white — the minimal form treatment that removes anything that might distract from the weekly buying decision. The product grid runs four-up portrait (3:4 ratio) with a cross-fade to an alternate angle on hover, the standard luxury e-com gesture performed with no embellishment. Filter pills break the square rule intentionally: `{rounded.full}` on facet selectors signals that browsing is exploratory while adding to cart is final. The promo banner and footer close in the deep ink (#161d25), framing the warm canvas in dark bookends.

colors:
  primary: "#bb2832"
  primary-active: "#8b0000"
  primary-disabled: "#e8b0b3"
  ink: "#161d25"
  body: "#191919"
  muted: "#767676"
  muted-soft: "#b1b1b1"
  hairline: "#d8d8d8"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f7f6f3"
  surface-warm: "#f9f6f2"
  surface-card: "#f7f5f4"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-blue: "#146ff8"
  accent-slate: "#c4cdd5"
  accent-orange: "#ff7216"
  steel-mid: "#849bb6"
  size-available: "#447b17"
  size-scarce: "#bb2832"
  dark-crimson: "#32070e"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'205TF Louize', Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'205TF Louize', Georgia, serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'205TF Louize', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'205TF Louize', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.4px
  title-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.4px
  body-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  price-display:
    fontFamily: "Courier, 'Courier New', monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  price-sale:
    fontFamily: "Courier, 'Courier New', monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 1.2px
    textTransform: uppercase
  button-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  label-caps:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.6px

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 20px
  xl: 32px
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    width: "100% (full-width in product context)"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    textDecoration: underline
    underlineOffset: 3px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: none
    borderBottom: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} 0"
    placeholderColor: "{colors.muted}"
    focusBorderBottom: "1px solid {colors.ink}"
    labelTypography: "{typography.label-caps}"
    labelColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoFamily: "'205TF Louize', Georgia, serif"
    logoSize: 20px
    logoWeight: 400
    logoTracking: 2px
    logoTransform: uppercase
    iconColor: "{colors.ink}"
    cartBadgeBackground: "{colors.primary}"
    cartBadgeText: "{colors.on-primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    nameTypography: "{typography.body-sm}"
    nameColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    salePriceColor: "{colors.primary}"
    originalPriceDecoration: line-through
    originalPriceColor: "{colors.muted}"
    hoverEffect: "cross-fade to alternate product angle"
    badgePosition: "top-left, absolute"
  hero-editorial:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    layout: "full-bleed image with bottom-anchored text overlay, or 50/50 split on desktop"
    ctaButton: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  drop-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
    position: "absolute top-left over product image"
  made-in-italy-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.md}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    size: 44px
    selectedBorder: "2px solid {colors.ink}"
    selectedBackground: "{colors.ink}"
    selectedTextColor: "{colors.on-primary}"
    unavailableBackground: "{colors.surface-soft}"
    unavailableTextColor: "{colors.muted-soft}"
    unavailableCross: true
    lowStockLabelColor: "{colors.primary}"
    lowStockLabelTypography: "{typography.label-caps}"
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    selectedRing: "2px solid {colors.ink}"
    selectedRingOffset: 2px
    gap: "{spacing.xs}"
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xs} {spacing.md}"
    selectedBackground: "{colors.ink}"
    selectedTextColor: "{colors.on-dark}"
    selectedBorder: "1px solid {colors.ink}"
  promo-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-caps}"
    padding: "{spacing.sm} {spacing.base}"
    height: 40px
    textAlign: center
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.ink}"
    gap: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.label-caps}"
    headingColor: "{colors.muted-soft}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderTop: none

## Components

### Buttons

**`button-primary`** — A square-cornered, 48px-tall crimson block (#bb2832) that reads as a printing stamp rather than a digital affordance. Letter-spacing of 1.2px on uppercase Helvetica gives the text weight without adding font-weight, so "ADD TO CART" and "SHOP NOW" read more like an edition label than a call to action. On active/press, shifts to the dark crimson (#8b0000); disabled state bleaches to a pale pink (#e8b0b3). Spans full width in the product detail context.

**`button-secondary`** — Identical dimensions to primary (48px height, same uppercase tracking) with canvas background and an ink-bordered outline. Used for "FIND MY SIZE", "NOTIFY ME", and wishlist-adjacent actions where the choice is secondary but the weight should feel equivalent. No rounding.

**`button-ghost`** — Text-only with underline, no background or border. Used for navigation-adjacent links — "VIEW ALL", "LEARN MORE" — where adding a bordered box would over-structure the layout. Underline offset at 3px keeps it from feeling cramped against the Helvetica baseline.

### Product Card

**`product-card`** — Portrait images at 3:4 ratio with no border, no rounding, and minimal padding. On hover the primary image cross-fades to a second angle — typically a sole view or wear shot — at 300ms ease. Product name sits beneath in body-sm Helvetica; price renders in Courier (price-display) to distinguish it typographically from descriptive text. Sale pricing stacks the new figure in crimson (#bb2832) above the struck-through original in muted gray (#767676). Drop badges appear absolute top-left over the image in solid crimson.

### Size Selector

**`size-selector`** — 44×44px squares arranged in a tight grid. Selected sizes invert to ink-on-canvas (dark background, white text); unavailable sizes display with a diagonal strike rendered as a CSS pseudo-element in muted-soft (#b1b1b1). When a size reaches low stock, a label-caps line below the grid appears in the primary crimson: "ONLY 2 LEFT" — the one editorial intrusion of urgency into what is otherwise a calm, non-pressure UI.

### Drop Badge

**`drop-badge`** — A small, hard-edged crimson rectangle placed absolute top-left over the product image. Typography is label-caps at 11px / 1.5px tracking, white text on primary red. Text reads "NEW THIS WEEK" or "JUST DROPPED". No rounding, no shadow — the badge reads as a physical tag applied to the product rather than a UI overlay.

### Navigation

**`nav-bar`** — 64px-tall white bar with a 1px hairline bottom border. The M.GEMI wordmark renders in 205TF Louize at ~20px, uppercase, with exaggerated letter-spacing — more logotype than simply the brand name set in the brand font. Category links run in 13px Helvetica with 0.6px tracking, centered or left-aligned cluster. Cart icon carries a crimson badge dot when items are present. On mobile, the nav collapses to a hamburger with a full-screen drawer.

### Hero Editorial

**`hero-editorial`** — Full-bleed photography (shot in Italian workshops or coastal locations) with either bottom-anchored text overlay or a 50/50 split on wider viewports. Headlines use display-xl 205TF Louize at 56px / weight 300 — the ultra-light cut of the serif creates a magazine-cover tension against the sharp product photography. The primary CTA button sits below the headline, full-width on mobile, fixed-width on desktop. Background tone on text-only sections pulls surface-soft (#f7f6f3).

### Filter Pills

**`filter-pill`** — The one place `{rounded.full}` appears in the UI. Pill-shaped facets for Category, Color, Width, Heel Height — unselected in surface-soft with a hairline border; selected state inverts to ink background with white caption text. The rounding contrast against the square buttons is intentional: browsing affordances are soft, purchasing affordances are hard.

### Promo Banner

**`promo-banner`** — A 40px-tall ink-dark (#161d25) full-width strip at the very top of the page. label-caps typography in white, centered. Used for free-shipping thresholds, weekly-drop announcements, and site-wide promotions. Color is the darkest in the palette, creating a deliberate frame before the white-canvas page begins.

### Text Input

**`text-input`** — Single bottom-border on white, no box, no rounded corners. The floating label animates to a small label-caps treatment above the field on focus. Matches the M.Gemi visual philosophy of removing any chrome that doesn't carry meaning — even the form field doesn't get a box.

### Made in Italy Badge

**`made-in-italy-badge`** — A small rectangular tag in surface-warm (#f9f6f2) with a hairline border, label-caps typography. Appears on PDP near the product name or in the details accordion, confirming provenance without a flag icon or illustration. Intentionally understated — the claim is made quietly, not celebrated.

### Footer

**`footer`** — Full-width ink-dark (#161d25) section. Column headings in label-caps with muted-soft (#b1b1b1) color; links in hairline-gray (#d8d8d8) that lighten to white on hover. Newsletter signup uses the text-input style transposed onto the dark background — bottom border in muted-soft, white input text. The dark footer closes the page against the off-white canvas the way a book cover closes against the pages inside.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen drawer; hero goes full-bleed portrait; size selector scrolls horizontally; promo banner wraps to two lines if needed; filter pills scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; hero switches to 50/50 split layout; nav shows abbreviated link set; size selector stays grid |
| Desktop | 1128–1440px | Four-column product grid; full nav link set visible; hero at full-bleed landscape; PDP switches to two-column (image left, details right) |
| Wide | > 1440px | Max-width container (~1400px) centered; side gutters grow; product grid stays four columns with wider card padding; hero image gains parallax margin |

### Touch Targets

- Size selector squares expand from 44px to 48px on mobile
- Color swatches increase to 32px diameter with 8px gap on touch
- Nav hamburger target area: 44×44px minimum
- Filter pills maintain 36px height minimum on mobile for thumb accessibility
- Add to cart button always full-width on mobile (100% container)

### Collapsing Strategy

- Desktop mega-nav with category columns collapses to hamburger at < 1128px
- Four-column product grid → two-column at tablet → single-column at mobile
- PDP two-column layout (images + form) stacks vertically at < 744px with images first
- Filter bar with horizontal pill row collapses behind a "FILTER" button on mobile; pills appear in a slide-up drawer
- Hero text overlay moves from absolute-positioned center/bottom to below-image stacked block on mobile
- Footer multi-column layout stacks to single column on mobile; accordions replace open columns

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No design tokens extracted for motion/animation — transition durations for image hover cross-fades, drawer open/close, and filter pill selection are estimated (300ms ease) from convention rather than extracted values
- The accent colors #5665d2 (purple-blue) and #3ed660 (bright green) appear in the extraction but no confirmed UI context could be determined; they may be third-party widget or Shopify admin artifacts
- 205TF Louize weight range is not confirmed — the extracted stack names the family but does not confirm which weights (Thin/Light/Regular/Medium) are loaded; fontWeight 300 and 400 are assumed from the light editorial rendering typical of this face
- Exact letter-spacing values for the M.GEMI wordmark logotype are not confirmed — the 2px uppercase tracking is an estimate
- No confirmed spacing values for the product image gallery (full-bleed vs. padded) on PDP
- Dark-mode or alternate theme presence could not be confirmed from extraction
- The Courier usage in price display is inferred from the font stack presence — exact scoping to price elements vs. broader use is not confirmed
- #ff7216 (orange) and #ee9441 (amber) context is ambiguous — possibly flash-sale pricing or promotional badge variants not observed during extraction
