---
version: alpha
name: "Le Gramme"
source_url: "https://www.legramme.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Electric #f5f500 yellow — pure voltage against an otherwise near-monochromatic grayscale field — is the sole color that breaks the Le Gramme system. The collection is organized by gram measurement: 1g, 2g, 3g cord bracelets, 5g cable rings, 7g and 9g chains — each weight is a product variant rather than a size, and the digital storefront encodes the same precision logic. Where other fine jewelry brands build atmosphere through warm gold tones and serif romanticism, Le Gramme operates on a technical register: the custom 'legramme' typeface carries headings with grotesque geometry, weight numerals render in monospace to reinforce the metrology theme, and GT-America-LG-Regular handles body copy with the clean neutrality of a product specification sheet. The near-white canvas (#fafafa) gives material photography — polished and brushed silver against spare natural backdrops — room to breathe without the clinical bite of pure white. Near-black (#111111) dominates primary actions and navigation; yellow (#f5f500) surfaces for sale indicators and active-state highlights, functioning more like a warning lamp than a decorative element. Hairlines land at #dedede — the most-extracted mid-gray — while surface cards sit at #f7f7f7, barely-perceptible elevation shifts in a system that treats contrast as a finite, metered resource. Corners are flat or essentially so: {rounded.none} for cards and imagery, {rounded.xs} at most for interactive chips, mirroring the precise geometry of the physical pieces' brushed facets and clean chamfers. Product detail pages build structured grids where weight variants stack as monospace-labelled selection chips, each one a specification entry rather than a stylistic gesture. The footer repeats this restraint — dense, small-text columns on a near-black (#121212) surface, referencing French industrial precision without nostalgia.

colors:
  primary: "#f5f500"
  primary-active: "#cccc00"
  primary-disabled: "#f5f5b3"
  accent-error: "#cc0000"
  accent-success: "#10cc00"
  ink: "#111111"
  body: "#282828"
  muted: "#767676"
  muted-light: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#fafafa"
  surface-soft: "#f2f2f2"
  surface-card: "#f7f7f7"
  surface-mid: "#e0e0e0"
  on-primary: "#111111"
  on-dark: "#ffffff"
  dark-surface: "#121212"
  dark-surface-mid: "#282828"
  mid-gray: "#808080"

typography:
  display-xl:
    fontFamily: "'legramme-bold', 'GT-America-LG-Regular', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1px
  display-md:
    fontFamily: "'legramme-bold', 'GT-America-LG-Regular', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'legramme-bold', 'GT-America-LG-Regular', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'GT-America-LG-Regular', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  title-sm:
    fontFamily: "'GT-America-LG-Regular', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1em
    textTransform: uppercase
  body-md:
    fontFamily: "'GT-America-LG-Regular', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'GT-America-LG-Regular', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'GT-America-LG-Regular', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.05em
  weight-display:
    fontFamily: "monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  weight-hero:
    fontFamily: "monospace"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0
  price:
    fontFamily: "monospace"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'GT-America-LG-Regular', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'GT-America-LG-Regular', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "'GT-America-LG-Regular', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase

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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.muted-light}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  button-cta-yellow:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-cta-yellow-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "none"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imagePaddingBottom: 100%
    titleTypography: "{typography.title-sm}"
    weightTypography: "{typography.weight-display}"
    priceTypography: "{typography.price}"
  weight-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.weight-display}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 8px 14px
    selectedBorder: "1px solid {colors.ink}"
    selectedBackgroundColor: "{colors.ink}"
    selectedTextColor: "{colors.on-dark}"
  weight-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.weight-display}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 8px 14px
  material-tag:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "none"
    textTransform: uppercase
    letterSpacing: 0.1em
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  hero:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.title-md}"
    minHeight: 80vh
    contentMaxWidth: 640px
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "48px 0 32px"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.caption}"
    headingTypography: "{typography.title-sm}"
    borderTop: "none"
    padding: "48px 0"

## Components

### Buttons
**`button-primary`** — A flat-cornered ({rounded.none}) near-black ({colors.ink}) block button, uppercase text at 0.12em tracking, height 48px. On hover, background shifts to {colors.body} (#282828). Disabled state drops to {colors.muted-light} with {colors.on-dark} text. This is the primary purchase action — "Add to Cart", "Proceed to Checkout" — carrying the weight of the entire transaction flow in its absolute flatness.

**`button-cta-yellow`** — The electric {colors.primary} (#f5f500) variant deployed for sale CTAs and urgency-framed moments. Text color is {colors.on-primary} (black) to maintain legibility on the bright ground. Active state darkens to {colors.primary-active} (#cccc00). Appears sparingly — one per page at most — to preserve the signal value of yellow in a system that otherwise deploys no color.

**`button-secondary`** — Transparent fill with a 1px {colors.ink} border and matching text. Shares the zero-radius geometry and uppercase tracking of `button-primary`. Used for secondary paths: wishlist, "View Collection", explore-more — wherever the filled dark CTA is reserved for the primary purchase action.

**`button-ghost`** — Borderless, transparent, {colors.muted} text in {typography.button-sm}. Used for low-priority actions like filter resets and modal dismissals. No visible affordance at rest; the text itself is the target.

### Weight Chips
**`weight-chip`** — Monospace-labelled selection chips for product weight variants (1g, 2g, 3g, 5g, 7g, 9g). Default: {colors.canvas} background, 1px {colors.hairline} border. Selected state inverts to {colors.ink} fill with {colors.on-dark} text. Active-focus state uses `weight-chip-active` with {colors.primary} fill — the one moment yellow enters the product-detail page. No radius anywhere; flat geometry reinforces the measurement logic.

### Text Input
**`text-input`** — Zero-radius, 1px {colors.hairline} border at rest. On focus, border upgrades to 1px {colors.ink} — minimal but unambiguous state change. Text in {typography.body-md}, placeholder in {colors.muted}. Height 48px matches button height for aligned form rows.

### Navigation
**`nav-bar`** — 56px tall, {colors.canvas} background, 1px {colors.hairline} bottom border. Links in {typography.nav-link} (12px, uppercase, 0.1em tracking). Logo typically centered or left-aligned at compact scale. Cart count and language/currency selector at right. On dark hero sections, the nav may invert to {colors.on-dark} text against a transparent or {colors.dark-surface} background.

### Product Card
**`product-card`** — Full-width square image (aspect-ratio 1/1, zero radius), product title below in {typography.title-sm} uppercase, gram weight directly beneath in {typography.weight-display} monospace, price at bottom in {typography.price} monospace. {colors.surface-card} background. Hover state scales image subtly (transform: scale(1.02)) without card shadow or elevation change — no decorative embellishment.

### Hero
**`hero`** — Full-width dark panel ({colors.dark-surface} / #121212) with centered or left-aligned content. Title in {typography.display-xl}, subtitle category label in {typography.title-md} uppercase. Primary CTA rendered as `button-cta-yellow` on dark; secondary as `button-secondary` with {colors.on-dark} border. Min-height 80vh on desktop to give material photography full presence.

### Material Tag
**`material-tag`** — Uppercase annotation labels for material specification: ARGENT 925, OR 18K, VERMEIL, PALLADIÉ. Text in {typography.caption} with {colors.muted} color. No background, no border — reads as metadata gloss rather than a badge. Appears below weight and price in product cards.

### Sale Badge
**`sale-badge`** — Flat {colors.primary} yellow label, {colors.on-primary} black text, zero radius. Applied to product card images at top-left corner. Deliberately compact (3px / 8px padding, {typography.button-sm}) to preserve photography.

### Collection Header
**`collection-header`** — {colors.canvas} band, {typography.display-md} title, {colors.hairline} bottom border. Category descriptor in {typography.title-sm}. 48px padding top, 32px bottom. On mobile, title scale reduces to {typography.display-sm}.

### Footer
**`footer`** — {colors.dark-surface} (#121212) surface, column-grid layout. Section headings in {typography.title-sm} ({colors.on-dark}). Link text in {typography.caption} ({colors.muted-light}). Social icons via Font Awesome 6 Brands. No decorative dividers — column spacing carries all hierarchy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, nav collapses to hamburger + logo, hero min-height 60vh, weight chips scroll horizontally |
| Tablet | 744–1128px | Two-column product grid, hero 70vh, nav shows partial top-level links |
| Desktop | 1128–1440px | Three or four-column grid, full nav, hero 80vh with text left-aligned over photography |
| Wide | > 1440px | Grid max-width capped at 1440px, gutters expand symmetrically, no further layout change |

### Touch Targets
- Weight chips maintain minimum 44px height even at compact monospace text size
- Primary buttons are 48px tall and expand to full-width on mobile
- Nav links padded to 44px tap area on mobile vs. condensed desktop header
- Sale badges are excluded from touch targets — decorative overlay only

### Collapsing Strategy
- Navigation: hamburger below 744px with full-height slide-in drawer on {colors.dark-surface}
- Product grid: 1-col (mobile) → 2-col (tablet) → 3–4-col (desktop/wide)
- Weight chip row: horizontal scroll with visible overflow on mobile rather than multi-row wrap
- Hero text: {typography.display-xl} drops to {typography.display-sm} on mobile; subtitle may collapse
- Footer columns: single stack on mobile → 2-col on tablet → 4-col on desktop

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Custom 'legramme' and 'legramme-bold' typeface metrics (exact x-height, full weight range, fallback rendering) not publicly documented
- GT-America-LG-Regular: whether 'LG' suffix denotes a modified/licensed variant or a specific optical cut is unconfirmed
- Whether #f5f500 / #ffff00 yellow functions as primary CTA background or exclusively as sale/discount indicator — extraction shows presence but context is ambiguous
- #cc0000 and #10cc00 precise roles (error/success system states vs. promotional coloring) unconfirmed from extraction
- Exact border-radius values from live CSS — all radii in this spec are inferred from brand aesthetic; live site may use 0px throughout
- Animation and transition timing values (hover, chip selection, cart slide-in) not extractable
- Whether site deploys a sticky/fixed nav or transparent-on-hero nav pattern
- Dark mode or theme-toggle behavior not confirmed
- Price display locale rules (EUR primary, USD switching behavior, sale price strikethrough color)
- Exact monospace font used for weight/price numerals — 'monospace' is the stack fallback; a specific face (e.g. Courier, Roboto Mono) may be specified in JS-loaded CSS
