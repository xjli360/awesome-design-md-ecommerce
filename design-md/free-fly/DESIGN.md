---
version: alpha
name: "Free Fly"
source_url: "https://www.freeflyapparel.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A bamboo-fiber outdoor apparel brand that stakes its visual identity on a deep, quiet green (#3e7a5e) and a teal accent (#5ac3b5) that surfaces only on CTAs and sale badges — a restrained palette that reads as grounded rather than outdoorsy-loud. The site runs ABC Diatype Mono for body copy, a monospaced face that would feel cold in finance but here, against a warm off-white canvas (#f4f4f6) and soft gray surfaces (#e5e5e5), it signals precision and intentionality. Product photography does the heavy lifting for texture — bamboo jersey folds, sun-lit fishing scenes — so the UI stays out of the way with generous whitespace and thin hairlines (#dbdde4). Headlines use New Spirit Condensed, a serif with a slight editorial drawl, set in dark ink (#373a36) at sizes that feel like magazine spreads. The marigold accent (#fbc641) appears sparingly — a badge on a bestseller, a dot on a size selector — never competing with the teal. Every button is a pill (`{rounded.full}`), every card corner soft (`{rounded.md}`), and the search bar floats in a full-width teal band that breaks the grid, the one moment the brand raises its voice. The overall mood is calm competence: a brand that knows its fabric is the story, and the interface is just the frame.

colors:
  primary: "#3e7a5e"
  primary-active: "#357974"
  primary-disabled: "#c6e6e4"
  ink: "#373a36"
  body: "#4a4d53"
  muted: "#737572"
  muted-soft: "#9a9db1"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5eb"
  canvas: "#f4f4f6"
  surface-soft: "#ececec"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#5ac3b5"
  accent-teal-light: "#c6e6e4"
  accent-marigold: "#fbc641"
  accent-marigold-soft: "#e2e2da"
  ink-dark: "#1e201e"
  ink-deep: "#272d45"
  border-light: "#d3d4dd"
  border-soft: "#eeeeee"
  star-rating: "#fbc641"

typography:
  display-xl:
    fontFamily: "'New Spirit Condensed', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'New Spirit Condensed', Georgia, serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'New Spirit Condensed', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'New Spirit Condensed', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Basis Grotesque Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Basis Grotesque Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'ABC Diatype Mono', 'Courier New', monospace"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'ABC Diatype Mono', 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'ABC Diatype Mono', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'ABC Diatype Mono', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Basis Grotesque Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Basis Grotesque Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Basis Grotesque Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'ABC Diatype Mono', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Basis Grotesque Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
    textTransform: uppercase

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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  button-accent-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-accent-teal-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid #c13515"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  search-bar-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "0 {spacing.base} {spacing.base}"
  badge-sale:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 40px"
    height: 52px
  footer-section:
    backgroundColor: "{colors.ink-dark}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.badge}"
    color: "{colors.canvas}"
    marginBottom: "{spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    color: "{colors.accent-teal}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  size-selector-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} 0 {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a full pill in the brand green (#3e7a5e) with white uppercase sans-serif text. On hover, it shifts to the darker teal-green (#357974). Disabled state fades to a pale mint (#c6e6e4) with muted text, signaling the action is unavailable without visual noise. Used for "Add to Cart", "Shop Now", and checkout entry points.

**`button-secondary`** — An outlined pill on a white canvas with a thin hairline border (#dbdde4). Active state fills the border to ink (#373a36) and applies a soft surface background (#ececec). Used for "Learn More", "View Details", and secondary checkout paths like PayPal.

**`button-accent-teal`** — The brand's secondary voltage, a bright teal (#5ac3b5) pill used for promotional CTAs, seasonal collections, and "Shop the Sale" moments. Hover state deepens to the primary-active teal (#357974). Never used alongside `button-primary` on the same page to avoid confusion.

**`button-ghost`** — A text-only button with no background or border, using the nav-link typography. Used for "Cancel", "Clear Filters", and inline utility actions. Hover state adds a subtle background tint (not specified in tokens, but typically a 10% opacity of the primary).

### Cards
**`product-card`** — A white card with soft 12px corners and no border, relying on shadow (not captured in tokens, but present on the live site as a subtle drop shadow). The image fills the top with matching corner radius, and title/price sit below in monospaced body type. Hover state typically lifts the card (shadow deepens) and may reveal a quick-add button.

**`badge-sale`** — A marigold (#fbc641) pill with dark ink text, used on product cards and collection pages to flag discounts. The uppercase badge type at 11px sits tight with 2px horizontal padding. Never overlaps the product image — it floats at the top-left corner.

**`badge-new`** — A teal (#5ac3b5) pill with white text, used for new arrivals. Same dimensions as `badge-sale` but distinct color to differentiate messaging at a glance.

### Navigation
**`nav-bar`** — A fixed 72px white bar with a thin bottom hairline (#e5e5eb). Logo sits left, nav links center (uppercase Basis Grotesque Pro at 14px), and utility icons (search, account, cart) right. Active page link gets a 2px bottom border in brand green. On scroll, the bar may gain a subtle shadow.

**`search-bar`** — A full-width teal band (#5ac3b5) that appears on the search page or as a sticky header element. The input field inside is a white pill with monospaced body text. The teal band is the brand's one moment of full-bleed color — it breaks the grid and signals "you are now in search mode."

### Forms
**`text-input`** — A white input with 8px corners and a thin hairline border. On focus, the border doubles to 2px and turns brand green. Error state uses a red border (#c13515) — the only red in the system, reserved exclusively for validation. Inputs use ABC Diatype Mono for a technical, precise feel.

**`size-selector`** — A small pill button group for size options (XS–XXL). Active state fills with brand green and white text. Disabled sizes (out of stock) appear with a line-through and muted color. The selector sits between the product title and the add-to-cart button.

**`quantity-stepper`** — A compact input with minus/plus buttons flanking a numeric display. Uses monospaced type for alignment. The stepper sits inline with the add-to-cart button on desktop, stacked on mobile.

### Footer
**`footer-section`** — A dark ink (#1e201e) full-width band with muted gray text (#9a9db1). Column headings are uppercase badges in white. Links use the monospaced link style and turn teal on hover. The footer includes newsletter signup (a `text-input` with a `button-primary`), legal links, and social icons. No brand green here — the dark canvas lets the content breathe.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column; hero banner reduces to 32px padding; search bar becomes a compact icon; footer stacks to single column |
| Tablet | 744–1128px | Nav shows 3-4 links; product cards in 2-column grid; hero banner at 48px padding; search bar visible as icon+text |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-4 column grid; hero banner at 64px padding; search bar full-width teal band |
| Wide | > 1440px | Max-width container (1440px) centers content; product cards in 4 columns; hero banner may feature full-bleed photography |

### Touch Targets
- All buttons and interactive elements minimum 44px height (48px standard)
- Size selector pills minimum 40px × 40px
- Icon buttons (search, cart, account) minimum 44px × 44px
- Accordion headers minimum 48px tap area
- Quantity stepper buttons minimum 40px × 40px

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1
- Footer columns stack: 4 columns → 2 columns → 1 column
- Search bar collapses from full-width band to icon-only trigger
- Hero banner text reduces from display-xl to display-lg on tablet, display-md on mobile
- Size selector wraps to two rows on mobile (XS–L on top, XL–XXL below)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (text-input focus ring, button hover shadows, card hover lift) could not be reliably extracted from the live site CSS — the extracted colors list is dominated by grays and neutrals, and the brand's true primary (#3e7a5e) was identified by its distinctiveness among the palette rather than by frequency. The accent teal (#5ac3b5) and marigold (#fbc641) appear in the extracted list but their exact usage contexts (badges, CTAs, sale flags) are inferred from common ecommerce patterns.
- Error styling for forms (red border for validation) is assumed from standard Shopify patterns — the exact hex (#c13515) is not in the extracted list.
- Dark mode is not present on the live site and has not been designed.
- Sub-brand or collection-specific color variations (e.g., fishing vs. lifestyle lines) could not be determined.
- Shadow tokens (drop shadows on cards, nav bar on scroll) are absent from the extracted data — the site likely uses layered box-shadows that are not captured in hex extraction.
- Animation and transition durations (button hover, card lift, nav scroll) are not available.
- The font-family list includes "PP Nikkei Maru" and "oke-widget-icons" — the former may be a secondary display face used sparingly (not in primary typography), and the latter is a widget icon font for product reviews (Okendo). Their exact roles are unclear.
- Checkout widget colors (Shopify Pay, Klarna, Afterpay) may be present in the extracted list but are not part of the brand design system — they have been excluded from the palette.
