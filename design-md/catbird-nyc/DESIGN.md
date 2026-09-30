---
version: alpha
name: "Catbird NYC"
source_url: "https://catbirdnyc.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Stacked in velvet trays thinner than a fingernail and photographed against bare skin, Catbird's pieces read smaller than most brands' close-up shots — and the site design follows this logic of miniaturization without apology. The primary signal is a pale lavender wash (#ffd1fa), applied to the announcement bar and select badge surfaces rather than to CTAs; it lands as a whisper against the warm off-white canvas (#f9f7f3) that replaces clinical pure-white throughout. Adobe Garamond Pro carries all editorial weight at the display scale — the long ascenders and optical warmth of traditional book typography give collection headers the unhurried feeling of a printed lookbook rather than a landing page — while TT Fors handles navigation, body copy, and UI labels in a clean, low-contrast sans that refuses to compete with the product photography. Near-black (#2a2a2a) is the true workhorse: CTA button fills, body text, footer background, and ring-size tile active states all share the same near-black rather than splitting into multiple dark tones, a unifying restraint that keeps the palette coherent across surfaces. Gold tones (#c07600 and its darker sibling #6f4400) appear in accent roles and the warm cream surface (#fdf0d5) — material references to the actual metal in the trays. Prices render in Overpass Mono, giving the transactional layer a quietly archival register, like a jeweler's receipt typed on a vintage Olivetti. Border radius is set to zero on image containers, inputs, and buttons alike — {rounded.none} everywhere that matters — signaling editorial codes over e-commerce smoothness. Hairlines at #ebebeb are so light they barely register; structure arrives through spacing and type hierarchy, not drawn borders. Sale states reach for #cc0300 as the single moment of real voltage on the page, making a markdown feel like an event.

colors:
  primary: "#2a2a2a"
  primary-active: "#111111"
  primary-disabled: "#b3b3b3"
  brand-lavender: "#ffd1fa"
  brand-blush: "#f9eeee"
  brand-gold: "#c07600"
  brand-gold-dark: "#6f4400"
  brand-cream: "#fdf0d5"
  brand-olive: "#6f7637"
  sale: "#cc0300"
  ink: "#1b1b1b"
  body: "#2a2a2a"
  muted: "#8c8c8c"
  muted-strong: "#545454"
  hairline: "#ebebeb"
  hairline-strong: "#d5d6df"
  canvas: "#f9f7f3"
  surface-soft: "#f9eeee"
  surface-warm: "#fdf0d5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Adobe Garamond Pro', 'Times New Roman', Times, Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Adobe Garamond Pro', 'Times New Roman', Times, Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Adobe Garamond Pro', 'Times New Roman', Times, Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  editorial-pullquote:
    fontFamily: "'Adobe Garamond Pro', 'Times New Roman', Times, Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.5
    letterSpacing: 0
  title-lg:
    fontFamily: "'TT Fors', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.15px
  title-md:
    fontFamily: "'TT Fors', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  title-sm:
    fontFamily: "'TT Fors', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.8px
    textTransform: uppercase
  body-md:
    fontFamily: "'TT Fors', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'TT Fors', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'TT Fors', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'TT Fors', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.2px
    textTransform: uppercase
  button-sm:
    fontFamily: "'TT Fors', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'TT Fors', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  price:
    fontFamily: "'Overpass Mono', 'Courier New', Courier, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-lg:
    fontFamily: "'Overpass Mono', 'Courier New', Courier, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0

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
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: none
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline-strong}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
    height: 44px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "1px solid {colors.ink}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.brand-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageRounded: "{rounded.none}"
    gap: "{spacing.sm}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    padding: 0
    columnGap: "{spacing.lg}"
  product-card-badge:
    backgroundColor: "{colors.brand-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "3px {spacing.xs}"
    position: "absolute top-left on image"
  product-card-sale-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "3px {spacing.xs}"
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
    textAlign: center
    ctaMarginTop: "{spacing.xl}"
  hero-split:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    layout: "50/50 image-left text-right"
    textPadding: "{spacing.xxl}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xl} 0"
    textAlign: center
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.price}"
  price-sale:
    salePriceColor: "{colors.sale}"
    originalPriceColor: "{colors.muted}"
    saleTypography: "{typography.price}"
    originalDecoration: line-through
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    suggestionTypography: "{typography.body-sm}"
    inputBorder: "1px solid {colors.hairline-strong}"
    inputRounded: "{rounded.none}"
    inputHeight: 44px
    entryAnimation: "slide-down fade-in"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} {spacing.xl}"
    columns: 4
    inputBorder: "1px solid {colors.on-primary}"
    inputRounded: "{rounded.none}"
  wishlist-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    activeTextColor: "{colors.sale}"
    rounded: "{rounded.full}"
    size: 32px
    position: "absolute top-right on product-card hover"
  ring-size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline-strong}"
    rounded: "{rounded.none}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    size: 40px
    layout: "horizontal row"
  material-swatch:
    size: 20px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.ink}"
    border: "1px solid {colors.hairline-strong}"
    activeOffset: 3px
    tooltip: "metal name on hover"
  editorial-band:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.editorial-pullquote}"
    padding: "{spacing.section} {spacing.xxl}"
    textAlign: center

## Components

### Buttons
**`button-primary`** — Sharp-cornered ({rounded.none}), 48px tall, near-black (#2a2a2a) fill with white text in uppercase TT Fors at 13px/1.2px tracking. The absence of border radius is a deliberate editorial signal — this is not the pill-shaped urgency of fast fashion. Active state deepens to #111111; disabled state uses muted gray (#b3b3b3) maintaining the flat aesthetic. Used for Add to Cart, Complete Purchase, and primary navigation CTAs.

**`button-secondary`** — Hollow variant with 1px near-black border and matching text, transparent fill. Identical height (48px) and typography to primary, maintaining visual alignment when both appear together. Used for secondary flows: add to wishlist, view full collection, continue shopping.

**`button-ghost`** — Text-only, no border, no fill. Uppercase 11px TT Fors at 1.5px tracking. Used for inline contextual links — "learn more," "view details" — where adding a border would clutter the layout.

### Text Input
**`text-input`** — Sharp-cornered, 44px tall, warm-canvas background (#f9f7f3) with 1px hairline border (#d5d6df) that sharpens to #1b1b1b on focus. No inner shadow, no background shift — the border weight change is the only state signal. Placeholder text in muted (#8c8c8c). Used across email capture, checkout fields, account forms, and search.

### Navigation
**`nav-bar`** — 60px tall on a warm white canvas (#f9f7f3) with a 1px hairline border-bottom (#ebebeb). Category links in uppercase TT Fors 13px at 0.8px letter-spacing; hover state adds a 1px border-bottom beneath the individual link rather than filling the background. Wordmark centered on desktop; hamburger left-aligned on mobile. Cart icon at far right carries a lavender (#ffd1fa) bubble count overlay. No logo animation, no sticky scroll effects — the nav stays static.

**`announcement-bar`** — A 36px strip in brand-lavender (#ffd1fa) above the nav bar. Used for free shipping thresholds, flash sales, and limited drops. Body-sm text centered; a small dismiss X anchors the right edge. The lavender is the only surface-level application of this color — it signals "attention, gently" rather than urgency.

### Product Card
**`product-card`** — Full-bleed image with no border radius, no outer card border, no box shadow. Below the image: product name in body-sm (13px TT Fors regular), then price in Overpass Mono on a separate line. The mono font gives price a receipt-like quietness that refuses to shout. A lavender badge ({colors.brand-lavender}) appears in the image corner for "New" or metal-type labeling. A wishlist heart renders on hover at the top-right of the image. Cards in a 3- or 4-column grid with {spacing.lg} gap; no surrounding surface or shadow.

### Hero
**`hero-editorial`** — Warm canvas (#f9f7f3) background, centered Adobe Garamond Pro headline at 48px weight 400. No video, no parallax, no countdown timers. The quietness is the statement. A single button-primary sits {spacing.xl} below the copy. This block reads like a journal opener rather than a landing page.

**`hero-split`** — On collection pages: 50/50 left image / right text on blush surface (#f9eeee). Text column holds a display-lg Garamond heading and two body-md paragraphs describing material origin or collection narrative. No overlapping text on image. Clean, flat, print-adjacent.

### Collection Header
**`collection-header`** — Centered, canvas background, display-md Garamond heading, optional body-md paragraph. Sits at the top of every category page before the product grid. {spacing.xl} vertical padding keeps it from crowding the first row of products.

### Price Display
**`price-display`** — Overpass Mono at 14px in near-black (#1b1b1b). When a sale is active, the original price renders in muted gray (#8c8c8c) with strikethrough alongside the sale price in red (#cc0300) — the only instance of #cc0300 on the page, giving markdowns real visual weight without using it elsewhere.

### Search
**`search-overlay`** — A full-viewport overlay in warm canvas (#f9f7f3) slides down from the nav on search icon click. Single centered input field, sharp-cornered, 44px tall. Autocomplete suggestions list below in body-sm. No backdrop shadow or blur — the overlay is clean white space with a single task.

### Footer
**`footer`** — Near-black (#2a2a2a) background, white text. Four columns: Shop, About, Customer Care, Newsletter. Column headings in title-sm (uppercase, 0.8px tracking). Links in body-sm. The newsletter input inverts the standard input: white 1px border, white placeholder and text on dark canvas. Same sharp-corner ({rounded.none}) form as the light-mode inputs — consistency across color contexts.

### Ring Size Selector
**`ring-size-selector`** — 40×40px flat tiles ({rounded.none}) in a horizontal row. Unselected: white fill, 1px hairline border (#d5d6df). Selected: near-black fill (#2a2a2a) with white text in body-sm. Out-of-stock: muted text (#b3b3b3) with diagonal rule, still clickable to trigger a waitlist modal. The binary color inversion (white→black) is the entire state system — no gradients, no intermediate colors.

### Material Swatch
**`material-swatch`** — 20px circles ({rounded.full}) representing metal type (yellow gold, rose gold, white gold, sterling silver). Active state gains a 2px solid {colors.ink} ring at 3px offset via box-shadow — creating a visible halo without scaling the circle. No text label beside the swatch; a tooltip reveals the metal name on hover/focus.

### Editorial Band
**`editorial-band`** — A full-width warm-cream (#fdf0d5) block with centered italic Adobe Garamond Pro pullquote at 22px. Used between product grid sections for brand storytelling — material sourcing, the permanent jewelry offering, Brooklyn origin stories. {spacing.section} vertical padding gives the prose room.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger left + wordmark center; display-xl scales to 28px (display-md Garamond); announcement bar wraps to two lines if needed; footer collapses to stacked accordion columns; hero-split stacks vertically (image above, text below) |
| Tablet | 744–1128px | Two-column product grid; nav shows abbreviated category links without dropdown; hero-split renders side-by-side; search overlay maintains full viewport |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with mega-menu dropdowns; hero-editorial and hero-split render at spec proportions; price in Overpass Mono remains 14px |
| Wide | > 1440px | Four-column product grid; max-width container ~1280px centered with symmetric gutters; display-xl may scale to 56px; side whitespace increases rather than stretching content |

### Touch Targets
- All tappable elements minimum 44×44px on mobile
- Ring size tiles expand to 44×44px on mobile (from 40px desktop)
- Material swatches get 32px minimum tap area via padding, despite 20px visual diameter
- Nav icon buttons (cart, search, hamburger) padded to 44px touch area
- Wishlist heart button padded to 44px on mobile product cards

### Collapsing Strategy
- Footer newsletter capture moves above column grid on mobile (highest-priority conversion)
- Collection-header body paragraph hidden on mobile; heading only
- Product card name truncates to one line on mobile with text-overflow ellipsis; price holds on line two
- Announcement bar persists at all breakpoints; dismiss state stored in sessionStorage
- Desktop mega-menu dropdowns become full-screen slide-in panels on mobile
- Editorial band pullquote scales from 22px to 18px on mobile; {spacing.xxl} padding reduces to {spacing.xl}

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color set; mobile browser chrome color cannot be confirmed from extraction
- Platform flagged non-Shopify; custom cart drawer and checkout UI tokens are not observable via static extraction
- Font "Lucia" appears in the extracted stack but its specific usage role is unclear — possibly a legacy fallback or campaign-specific element, not mapped to any component
- Font "Denton Condensed" extracted but context not confirmed — possibly used in seasonal campaign headlines or special edition pages rather than core UI
- Role of #8bc53f (bright green), #ff5501 (orange), #003399 and #006bb4 (blues) is ambiguous — likely third-party widget colors (live chat, review platform, payment badge) rather than brand palette; excluded from tokens
- Exact nav height and wordmark dimensions estimated at 60px — could not be measured from static extraction
- Hover/focus transition timing and easing curves not extractable from static analysis
- Product image aspect ratio (likely 1:1 square or 4:5 portrait for fine jewelry) not confirmed from extraction
- Gold accent application (#c07600, #6f4400, #fdf0d5) on live site may be seasonal or campaign-specific; exact component mapping is inferred rather than observed
