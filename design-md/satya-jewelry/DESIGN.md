---
version: alpha
name: "Satya Jewelry"
source_url: "https://www.satyajewelry.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Gold at #c9a557 — a warm saffron-amber that sits halfway between a marigold and a wedding band — is not an accent in Satya's visual language but the ceremonial axis around which an entire column of fired-earth tones rotates. Every primary call-to-action, price emphasis, and hover state draws from this single hue, with #ab8229 deepening it under press and #f5e6c4 dissolving it into near-transparency on disabled states. The canvas family runs warm rather than white: #fcfbf9 carries the base, #f9f3ef softens product-image backgrounds, and #f1ede6 lends depth to nested surface blocks — three near-whites that never feel clinical or medical. Against these, the ink hierarchy descends through a column of fired-clay tones: near-black #3c322a for primary copy, #554438 for body text, and #605953 for muted annotations, with the meta theme color #9d806c functioning as navigational chrome and secondary label fill.

  The spiritual and symbolic positioning is encoded in the palette before a single glyph renders. Warm tans like #bea58e and #907360 surface in hover borders and decorative dividers, evoking incense-darkened wood and ritual objects rather than the polished chrome of luxury accessory retail. Cards carry warm, low-contrast surfaces rather than drop shadows, and depth is achieved through nested warm tones — #f9f3ef inside #fcfbf9 inside #f1ede6 — rather than elevation. Buttons read flat and square-shouldered (`{rounded.none}`) as a deliberate counterpoint to the soft spiritual imagery; the brand trusts photography and symbolic iconography to carry warmth, reserving geometry for structure.

  Badge and filter treatments for chakra categories and spiritual themes use pill forms (`{rounded.full}`) in muted gold, translating the product vocabulary — mantras, symbols, intentions — into a scannable filterable taxonomy without losing the brand's ceremonial register. No font families were captured from the live site extraction, suggesting they load via deferred JS; the typography specifications below use best-fit system stacks for a spiritual-jewelry brand and should be validated against live computed styles before production use. Spacing is generous throughout: wide collection margins and open whitespace between section blocks let individual pieces read as symbolic objects rather than inventory.

colors:
  primary: "#c9a557"
  primary-active: "#ab8229"
  primary-disabled: "#f5e6c4"
  primary-gold-light: "#f5e6c4"
  gold-amber: "#c39b44"
  ink: "#3c322a"
  body: "#554438"
  muted: "#605953"
  muted-soft: "#9d806c"
  warm-gray: "#706a64"
  hairline: "#d9d9d9"
  hairline-soft: "#f2f2f2"
  canvas: "#fcfbf9"
  surface-soft: "#f9f3ef"
  surface-card: "#f1ede6"
  surface-warm: "#f5ebe4"
  on-primary: "#3c322a"
  warm-tan: "#bea58e"
  medium-brown: "#907360"
  deep-brown: "#46382e"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.4px
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1.5px
    textTransform: uppercase
  price-display:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  eyebrow:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 2.5px
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
    rounded: "{rounded.none}"
    padding: "14px 36px"
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "13px 35px"
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost-gold:
    backgroundColor: "transparent"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "13px 35px"
    height: 48px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-promo-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    priceColor: "{colors.ink}"
    salePriceColor: "{colors.primary-active}"
    nameTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.none}"
    imagePadding: "{spacing.sm}"
  symbol-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    border: "1px solid {colors.hairline}"
  collection-eyebrow:
    textColor: "{colors.primary-active}"
    typography: "{typography.eyebrow}"
    marginBottom: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    minHeight: 580px
    padding: "{spacing.section} {spacing.xl}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    iconColor: "{colors.muted}"
    height: 44px
  chakra-filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    quoteTypography: "{typography.body-md}"
    authorTypography: "{typography.caption}"
    starColor: "{colors.primary}"
    accentBorder: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  newsletter-strip:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    inputBorderColor: "{colors.hairline}"
    inputBackgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.xl}"
  swatch-selector:
    size: 24px
    borderRadius: "{rounded.full}"
    defaultBorderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    selectedBorderWidth: 2px
    gap: "{spacing.xs}"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    height: 44px
    width: 44px
  footer:
    backgroundColor: "{colors.deep-brown}"
    textColor: "{colors.warm-tan}"
    linkColor: "{colors.primary-gold-light}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    borderTop: "2px solid {colors.medium-brown}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Square-shouldered (`{rounded.none}`) with a warm gold #c9a557 fill and dark #3c322a ink for text. The flat geometry reads as an intentional brand statement against the soft photographic imagery; on hover it deepens to #ab8229 without animation delay. The disabled state washes to #f5e6c4 with muted text, preserving the gold family even in inactive states.

**`button-secondary`** — Outline variant in transparent fill with a 1px #3c322a border, matching the primary's square radius and height. Functions as an equal-weight alternative for two-CTA layouts (e.g., "Add to Bag" / "Add to Wishlist") without introducing a competing color.

**`button-ghost-gold`** — Gold-tinted outline with `{colors.primary-active}` text and a 1px `{colors.primary}` border. Used for secondary actions in editorial contexts — "Shop the Collection", "Explore the Symbol" — where a dark outline would overpower the adjacent photography.

**`nav-promo-strip`** — A 36px strip above the main nav using the full primary gold #c9a557 as background with dark on-primary text. Carries shipping thresholds, sale notices, and intention-of-the-day copy — the first gold element a visitor encounters.

### Navigation

**`nav-bar`** — 64px tall on a warm near-white #fcfbf9 canvas, separated from page content by a hairline-soft #f2f2f2 border. Links use `{typography.nav-link}` at weight 500 with moderate letter-spacing. The logo centers or left-aligns depending on breakpoint; icon row (search, account, cart) clusters right.

**`search-bar`** — Pill-shaped (`{rounded.full}`) in contrast to the square buttons, creating a deliberate tension between interaction types. Background is `{colors.surface-soft}` (#f9f3ef) when inactive, sharpening to a `{colors.primary}` border on focus. Icon tinted `{colors.muted}` (#605953).

### Product Listing

**`product-card`** — No border, no shadow — cards are differentiated by the warm #f9f3ef image-container background against the #fcfbf9 page canvas. Product name in `{typography.body-sm}`, price in `{typography.price-display}` (serif, 18px), sale price in `{colors.primary-active}` to maintain the gold vocabulary even at markdown.

**`chakra-filter-chip`** — Pill filter chips for spiritual categories (Chakras, Intentions, Symbols). Resting state is warm surface with hairline border; selected state fills with `{colors.primary}` and `{colors.on-primary}` text. The typography (`{typography.badge-label}`, 10px uppercase, 1.5px tracking) keeps labels compact enough for a dense filter row.

**`symbol-badge`** — Small pill label applied to product cards to indicate spiritual affiliation (e.g., "Lotus", "Hamsa", "Om"). Uses muted warm-surface fill and `{typography.badge-label}` — distinct from the interactive chakra chip by being non-clickable, rendering as category metadata rather than a filter action.

### Product Detail

**`swatch-selector`** — 24px circular swatches with a `{colors.primary}` 2px selected-state ring and `{colors.hairline}` resting border. The gold ring reads as premium within the warm palette without needing a checkmark or other overlay indicator.

**`quantity-stepper`** — Square-edged stepper (matching button geometry) in `{colors.canvas}` with `{colors.hairline}` border. Three cells: decrement / count / increment, each 44×44px for accessible touch targets.

### Editorial & Conversion

**`hero-banner`** — Warm `{colors.surface-soft}` background (used when no full-bleed photography is present), headline in `{typography.display-xl}` (serif, 42px, weight 400) and subhead in `{typography.body-md}`. Minimum 580px height leaves room for model photography on left or right column.

**`collection-eyebrow`** — Small uppercase gold label (`{typography.eyebrow}`, 11px, 2.5px tracking) in `{colors.primary-active}` sitting above collection or editorial headings. Serves as the brand's primary wayfinding label — "New Arrivals", "Best Sellers", "The Lotus Collection" — at a size that doesn't compete with the serif display below.

**`testimonial-card`** — Warm `{colors.surface-card}` (#f1ede6) tile with a 2px `{colors.primary}` left accent border and gold star rating. Author attribution in `{typography.caption}`. Arranged in a horizontal scroll or grid below product descriptions to carry social proof within the brand's earth register.

**`newsletter-strip`** — Full-width warm `{colors.surface-warm}` (#f5ebe4) band with centered serif headline (`{typography.display-sm}`) and inline email input / primary CTA pairing. No dark backgrounds — the brand maintains the warm register throughout the funnel rather than switching to high-contrast for conversion moments.

### Footer

**`footer`** — Sole dark surface in the brand: deep espresso #46382e with `{colors.warm-tan}` (#bea58e) body text and `{colors.primary-gold-light}` (#f5e6c4) links. The warm-dark footer reads as grounding rather than stark, consistent with the ritual-object sensibility. Link hover lifts to full primary gold #c9a557.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero stacks copy above image; chakra filter chips scroll horizontally in a snap container; promo strip text truncates to one line |
| Tablet | 744–1128px | Two-column product grid; nav shows primary categories inline with overflow in hamburger; hero moves to 50/50 split; newsletter strip stacks headline above input |
| Desktop | 1128–1440px | Three-to-four column product grid; full horizontal nav with all categories; hero reaches 580px minimum height; testimonial cards in three-column grid |
| Wide | > 1440px | Max content width caps at ~1440px with centered layout; hero can extend to full viewport width with constrained text column; product grid stays at four columns |

### Touch Targets

- All interactive elements (buttons, chips, swatches, nav items) meet 44×44px minimum touch target
- Quantity stepper cells are explicitly 44×44px
- Swatch selectors at 24px visual size are wrapped in a 44px tap area
- Chakra filter chips use 6px vertical padding + line height to reach minimum tap height naturally

### Collapsing Strategy

- Primary nav collapses at < 744px into a drawer from left edge, revealing full category hierarchy
- Chakra filter row becomes a horizontal-scroll snap container below 744px; no wrapping
- Hero copy-image split stacks vertically at mobile, copy first, image below
- Footer columns collapse from four-column to two-column at tablet and single-column at mobile
- Product card image-to-text ratio stays consistent across breakpoints; grid column count drives card width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font families captured from live extraction — the site likely loads custom typefaces via deferred JS or a web font CDN that bypassed the extractor. Display and body font stacks above are best-fit inferences (serif display + system sans body) based on the spiritual-jewelry aesthetic. Inspect `document.fonts` or computed CSS on the live site to confirm actual families.
- Letter-spacing and line-height values in typography tokens are inferred from category conventions, not measured from rendered page output — validate with a design token audit or Figma source if available.
- No motion or animation tokens extracted; transition durations, easing curves, and hover animation behavior are not specified here.
- Icon system details (glyph library, stroke weight, size variants for spiritual/chakra symbols) not captured.
- Sale badge and "New" badge exact dimensions, colors, and positioning within product card not confirmed from extraction.
- Mobile nav drawer background color, overlay scrim opacity, and animation direction not confirmed.
- Exact product image aspect ratio (square, portrait, or mixed) not determinable from color extraction alone.
