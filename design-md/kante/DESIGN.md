---
version: alpha
name: "Kante"
source_url: "https://kanteplanters.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The design trick is borrowed from the product itself — a planter engineered to read like poured concrete but weighing a fraction of real masonry. Kante's visual language mirrors that sleight of hand: a palette stripped to cool whites, warm grays, and near-blacks that evoke cast stone without ever feeling industrial or harsh. CTAs and interactive elements anchor in a deep charcoal (#2d2d2d) that doubles as the brand's ink color, collapsing the usual contrast between brand-voltage and text into a single unified tone. There is no electric accent, no lifestyle-brand coral, no botanical green — the restraint is total and intentional. Type runs in a neutral geometric sans at weights that hover between 300 and 600; headings earn their scale through generous leading and wide letter-spacing rather than heavy weight. Product cards sit on a barely-warm off-white surface (#f6f5f3), giving the planters — all neutrals themselves — just enough separation from the canvas to read as objects on a shelf rather than images on a screen. Buttons are mildly rounded (`{rounded.sm}`) rather than pill-shaped, keeping the experience in architectural territory. The grid is sparse, with wide gutters and section padding that would feel excessive in a crowded DTC context but reads correctly when the product is a large-format outdoor object meant to be studied rather than impulse-purchased. Search and filtering stay subordinate — this is a considered-purchase brand where the full catalog is small enough to browse visually. Navigation is horizontal and flat, anchored by the wordmark left and a minimal utility cluster right. No mega-menus. No badge inflation. Kante trusts that a customer who would spend on a concrete-look planter does not need urgency mechanics.

colors:
  primary: "#2d2d2d"
  primary-active: "#111111"
  primary-disabled: "#a8a8a6"
  ink: "#1a1a1a"
  body: "#3c3c3a"
  muted: "#787874"
  hairline: "#e3e2de"
  hairline-soft: "#eeede9"
  canvas: "#ffffff"
  surface-soft: "#f6f5f3"
  surface-warm: "#efede9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-stone: "#c4bfb8"
  accent-terracotta: "#b07060"
  scrim: "#1a1a1a"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 38px
    fontWeight: 300
    lineHeight: 1.18
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.04em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.06em
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  caption-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.04em
  price-display:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.5
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
  section: 80px
  section-lg: 120px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    border: none
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
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    borderBottom: "1px solid {colors.ink}"
    padding: 2px 0px
  add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 40px
    height: 56px
    width: 100%
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    position: sticky
    paddingX: "{spacing.xl}"
  nav-wordmark:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    letterSpacing: 0.15em
    textTransform: uppercase
  nav-utility-cluster:
    gap: "{spacing.lg}"
    iconSize: 20px
    textColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageBg: "{colors.surface-soft}"
    gap: "{spacing.md}"
    padding: 0
    imageAspect: "4/5"
  product-card-title:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
    fontWeight: 400
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.body}"
  product-card-hover:
    imageScale: 1.03
    transition: transform 600ms ease
  hero-full:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    layout: split-50-50
    paddingX: "{spacing.section}"
    paddingY: "{spacing.section-lg}"
    imagePosition: right
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 540px
  hero-subhead:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    maxWidth: 420px
    marginTop: "{spacing.xl}"
  hero-cta-group:
    display: flex
    gap: "{spacing.md}"
    marginTop: "{spacing.xxl}"
  collection-grid:
    columns: 3
    gap: "{spacing.xl}"
    paddingX: "{spacing.section}"
    paddingY: "{spacing.section}"
  collection-grid-mobile:
    columns: 2
    gap: "{spacing.base}"
  section-label:
    typography: "{typography.title-sm}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.lg}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.sm}"
  product-detail-layout:
    columns: "60% 40%"
    gap: "{spacing.xxl}"
    paddingX: "{spacing.section}"
    paddingY: "{spacing.section}"
  product-gallery:
    mainImageAspect: "1/1"
    thumbnailSize: 72px
    thumbnailGap: "{spacing.sm}"
    thumbnailBorder: "2px solid transparent"
    thumbnailBorderActive: "2px solid {colors.ink}"
  product-info-panel:
    paddingLeft: "{spacing.xxl}"
    gap: "{spacing.xl}"
  product-title:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    fontWeight: 300
  product-price-block:
    typography: "{typography.price-display}"
    textColor: "{colors.body}"
    marginTop: "{spacing.sm}"
  size-selector:
    display: flex
    flexWrap: wrap
    gap: "{spacing.sm}"
    marginTop: "{spacing.base}"
  size-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-label}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "8px 16px"
    height: 40px
  size-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
  specs-table:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    borderColor: "{colors.hairline-soft}"
    rowPadding: "12px 0"
    gap: "{spacing.base}"
  material-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.none}"
    padding: "6px 12px"
    display: inline-flex
  color-swatch:
    width: 28px
    height: 28px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderActive: "2px solid {colors.ink}"
    outline: "1px solid {colors.hairline}"
    gap: "{spacing.sm}"
  accordion:
    borderTop: "1px solid {colors.hairline}"
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} 0"
    iconSize: 16px
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.muted}"
    bodyPadding: "0 0 16px 0"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-label}"
    height: 40px
    textAlign: center
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: "11px 16px"
    height: 44px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    paddingX: "{spacing.section}"
    paddingY: "{spacing.xxl}"
    columns: 4
    columnGap: "{spacing.xxl}"
  footer-heading:
    typography: "{typography.caption-label}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.base}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hoverColor: "{colors.ink}"
  editorial-band:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    paddingX: "{spacing.section}"
    paddingY: "{spacing.section}"
    layout: centered
    maxWidth: 720px
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.muted}"
    gap: "{spacing.xl}"

## Components

### Buttons

**`button-primary`** — Full charcoal fill (#2d2d2d) with no border radius, uppercase tracked lettering at 13px. The square corner is a deliberate architectural choice that reads alongside a product photographed with 90-degree angles; it never rounds. Hover darkens to `primary-active` (#111111). Disabled state uses `primary-disabled` (#a8a8a6), reducing contrast without changing shape. Height is 48px across all breakpoints; the label letter-spacing widens to 0.08em, giving the uppercase tracking room to breathe.

**`button-secondary`** — White fill with a 1px charcoal border, same square geometry as the primary. Hover introduces a `surface-soft` (#f6f5f3) fill wash rather than border-color change, keeping the contrast shift subtle. Used for secondary PDPs actions (e.g. "Save to Wishlist", size guide links) and paired alongside `button-primary` in the hero CTA group with a `{spacing.md}` gap.

**`button-ghost`** — Transparent background, no border, only a 1px bottom border acting as an underline. Used for contextual inline actions — "Learn More," "View all sizes" — where a full button would overpower the editorial copy. Label runs at 11px uppercase with `button-sm` tracking.

**`add-to-cart`** — Full-width variant of `button-primary` pinned to the bottom of the product info panel on mobile. Height increases to 56px for touch comfort. The increased height is the only mobile adaptation; color and typography are identical.

### Navigation

**`nav-bar`** — Sticky, 64px tall, white background with a hairline bottom border (#e3e2de). Three-zone layout: wordmark left, category links centered, utility cluster (search icon, account, cart) right. The wordmark uses `{typography.nav-link}` uppercase with exaggerated letter-spacing (0.15em) — it functions as a logotype rather than a brand mark image. No logo SVG observed on the extracted page, suggesting the wordmark IS the logo.

**`promo-banner`** — 40px charcoal ribbon above the nav, white uppercase caption-label text centered. Used for shipping thresholds and seasonal promotions. Sits above the sticky nav layer so it scrolls away while the nav bar stays fixed.

### Product Cards

**`product-card`** — No border, no shadow, no border-radius. A 4:5 image container fills the top over a `surface-soft` background; the planter photograph sits against the warm off-white, eliminating the need for any drop shadow or card frame. On hover, the image scales to 1.03× over 600ms ease — slow enough to feel physical rather than reactive. Below the image, title in `body-sm` weight 400 and price in `price-sm` weight 400 sit on a flush-left baseline with `{spacing.md}` gap. No "Add to Cart" visible in the grid — the card is a navigation unit, not a purchase trigger.

**`collection-grid`** — Three-column at desktop with `{spacing.xl}` gutter and `{spacing.section}` horizontal padding. The wide page padding narrows the live grid considerably, which suits large planters that need visual breathing room. Each column shows one product without competing copy or badge overlays.

### Product Detail

**`product-gallery`** — Square main image (1:1) with a vertical thumbnail strip left on desktop. Thumbnails are 72px squares with a 2px transparent border switching to 2px charcoal on active — minimal but readable. On mobile the thumbnail strip collapses to a horizontal swipe row below the main image.

**`size-selector`** and **`color-swatch`** — Sizes render as flat rectangular chips (`size-chip`) with a 1px hairline border; active state inverts to full charcoal fill. Color finishes use `color-swatch` circles (28px, `{rounded.full}`) ringed by a 1px hairline outline, with a 2px charcoal active border offset from the fill circle. Both controls sit flush-left under the price block, separated by `{spacing.base}` margins.

**`specs-table`** — Two-column definition table: left column in `spec-label` uppercase muted gray, right column in `body-sm` charcoal. Rows separated by `hairline-soft` lines. Covers dimensions (H × D), weight, material composition, and drainage. This is among the highest-priority components for planters — a customer comparing pots by weight and size reads this table before the description.

**`accordion`** — Used for collapsible product information sections: Care Instructions, Shipping, Returns. Top border only, no bottom border on closed state (the next item provides the visual separator). Chevron icon 16px, rotates on open. Body text in `body-sm` muted.

### Editorial

**`editorial-band`** — Centered column, max 720px wide, over `surface-warm` (#efede9). Headline in `display-md` weight 300, body in `body-md` muted, with `{spacing.section}` vertical padding. Used mid-page to break product grids with brand narrative — typically a sentence about the manufacturing process or material sourcing. No imagery; the warmth of the background color carries the tonal weight.

**`material-badge`** — Small inline tag in `surface-warm` background, uppercase `caption-label` text. Appears in product cards occasionally to flag material variant ("MGO", "Lightweight Concrete-Look"). Not used as urgency or promotional signaling.

### Footer

**`footer`** — Four-column layout over `surface-soft` (#f6f5f3) with a top hairline. Column headings in `caption-label` uppercase; links in `body-sm` muted gray hovering to ink. The soft background creates continuity with the product card image area — the page fades to the same warm off-white it entered from.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; `add-to-cart` pinned as sticky bottom bar; gallery switches to swipe with dot indicators; footer collapses to single-column stacked accordion; nav utility cluster reduces to icon-only |
| Tablet | 744–1128px | Two-column product grid; product detail switches to stacked (gallery above, info below) rather than side-by-side; footer two columns; hero switches to full-bleed stacked with copy overlaid |
| Desktop | 1128–1440px | Three-column grid; split 60/40 PDP layout active; sticky nav full three-zone; footer four columns |
| Wide | > 1440px | Max-width container (~1440px) centered with extended side margins; section padding increases to `section-lg` (120px); product grid gains optional fourth column |

### Touch Targets

- Minimum 44px height on all interactive elements (enforced by `add-to-cart` 56px, buttons 48px, `text-input` 44px)
- Size chips minimum 40px height × 48px minimum width for thumb comfort
- Color swatches 28px with 8px transparent tap-area padding to reach 44px effective target
- Accordion headers full-width tap, min 48px height
- Nav utility icons minimum 44×44px touch zone despite 20px visual icon size

### Collapsing Strategy

- Promo banner scrolls off on mobile; nav bar remains sticky
- Product specs table maintains two-column layout on all breakpoints — do not linearize into a list
- Editorial band reduces max-width to full-bleed on mobile with increased horizontal padding (`{spacing.xl}`)
- Color swatch row wraps naturally; do not introduce horizontal scroll
- Thumbnail strip becomes horizontal swipe row below main image on mobile; vertical strip is desktop-only
- Footer navigation columns collapse to accordion on mobile, revealing links on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site — the palette above is inferred from Kante's widely observable concrete-aesthetic and neutral positioning, not pixel-sampled values. All color tokens should be validated against the live site before production use.
- No font families were detected in extraction — the typography stack defaults to Helvetica Neue. Kante may use a licensed geometric sans (e.g. Aktiv Grotesk, Neue Haas Grotesk, or similar) loaded via a JS font loader or CDN that evaded extraction.
- Platform is not confirmed as Shopify — component patterns (size selectors, cart drawer, variant pickers) follow Shopify conventions as a reasonable default but may differ.
- No theme-color meta tag present — brand accent color for browser chrome / PWA cannot be confirmed.
- Product badge / tag system (if any) not confirmed — `material-badge` component is inferred from planter-category conventions, not observed directly.
- Exact border-radius values not confirmed — square corners (`{rounded.none}`) are inferred from the architectural/concrete aesthetic; site may use minimal (`{rounded.xs}` 2px) rather than true zero.
- Animation durations and easing curves for hover and page transitions not extracted.
- Whether a cart drawer or cart page is used is unknown; cart interaction pattern is assumed drawer-based but not confirmed.
