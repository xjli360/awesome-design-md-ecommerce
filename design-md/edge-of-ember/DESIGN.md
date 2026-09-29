---
version: alpha
name: "Edge of Ember"
source_url: "https://www.edgeofember.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Ember glow belongs to the gold accents — the muted #c9c26b of aged vermeil and the searing #fbcd0a of polished gold-fill campaign ribbons — but the brand's commanding voltage is a deep teal (#108474) that runs every primary CTA, active filter state, and sustainability icon. For a fine jewelry label living on delicate 14k pieces and recycled silver, that choice is a declaration: Edge of Ember leads with ethics before it leads with luxury. The canvas holds near-white (#f9f9f9, #fafafa) with editorial economy; dark charcoal (#252525) handles body copy while warm near-black #282622 — a brown-tinged shadow rather than pure ink — grounds the footer and dark hero overlays. Deep forest greens (#0b331f, #163120) surface in collection banners and section fills, giving the brand a verdant botanical register beneath its clean Shopify scaffold.

  Typography divides along a precise axis. Albra, a contemporary serif with humanist terminals and generous thick-to-thin contrast, carries the editorial display register — campaign headlines, collection category titles, hero sublines — at sizes from 28 to 48px with slightly tight tracking that suits its narrow shoulders. Lausanne, a Swiss grotesque with even color and wide language support, handles every UI surface: navigation, product metadata, filter labels, body copy — at weights 300 to 500. The pairing enacts the brand name's duality: Albra is the ember warmth, Lausanne the edge precision. Nunito Sans appears within Judge.me review blocks and as a system fallback, its roundness reading as deliberately customer-facing against the stiffer brand stack.

  Product cards sit with hairline-soft borders ({colors.hairline-soft}) on pale canvas, never shadowed — keeping every gram of visual weight inside the photography. Buttons land at {rounded.sm} rather than pill-shaped, signaling contemporary conviction without softening into lifestyle-brand approachability. Lavender (#a89cc8) and pale teal (#c1e6e6) chips tag gemstone collections — Amethyst and Aquamarine lines — extending the palette into the product's actual material vocabulary. A trust-badge strip anchored in primary teal above the footer makes the brand's ethical positioning legible at every scroll depth, and the gold-vivid (#fbcd0a) announcement bar delivers promotional urgency without cheapening the overall register.

colors:
  primary: "#108474"
  primary-active: "#0b331f"
  primary-disabled: "#c1e6e6"
  primary-light: "#edf5f5"
  gold: "#c9c26b"
  gold-vivid: "#fbcd0a"
  forest-deep: "#163120"
  lavender: "#a89cc8"
  teal-pale: "#c1e6e6"
  ink: "#252525"
  ink-warm: "#282622"
  body: "#555555"
  muted: "#7b7b7b"
  muted-light: "#888888"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  hairline-strong: "#bbbbbb"
  canvas: "#f9f9f9"
  canvas-white: "#fafafa"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Albra', Baskerville, Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Albra', Baskerville, Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Albra', Baskerville, Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Albra', Baskerville, Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Lausanne', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lausanne', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.01em
  body-md:
    fontFamily: "'Lausanne', 'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lausanne', 'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Lausanne', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.03em
  label-tag:
    fontFamily: "'Lausanne', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.08em
    textTransform: uppercase
  price-display:
    fontFamily: "'Lausanne', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  price-compare:
    fontFamily: "'Lausanne', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Lausanne', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Lausanne', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Lausanne', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0.04em
  announcement:
    fontFamily: "'Lausanne', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0.02em

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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
    hoverBackgroundColor: "{colors.ink}"
    hoverTextColor: "{colors.on-dark}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    textDecoration: underline
    letterSpacing: 0.04em
  button-gold:
    backgroundColor: "{colors.gold-vivid}"
    textColor: "{colors.ink-warm}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoMaxHeight: 36px
    iconColor: "{colors.ink}"
    cartIndicatorColor: "{colors.primary}"
  announcement-bar:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.on-dark}"
    typography: "{typography.announcement}"
    height: 40px
    accentColor: "{colors.gold-vivid}"
    linkColor: "{colors.gold}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    comparePriceTypography: "{typography.price-compare}"
    comparePriceColor: "{colors.muted}"
    comparePriceTextDecoration: line-through
    padding: "{spacing.md}"
    gap: "{spacing.sm}"
    hoverImageScale: 1.04
    hoverBorderColor: "{colors.hairline}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-tag}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-badge-sale:
    backgroundColor: "{colors.gold-vivid}"
    textColor: "{colors.ink-warm}"
    typography: "{typography.label-tag}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.ink-warm}"
    textColor: "{colors.on-dark}"
    overlayColor: "rgba(40,38,34,0.40)"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    sublineColor: "{colors.hairline-soft}"
    ctaGap: "{spacing.md}"
    minHeight: 620px
    contentAlignment: center
  collection-banner:
    backgroundColor: "{colors.forest-deep}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-sm}"
    accentColor: "{colors.gold}"
    minHeight: 360px
    contentPadding: "{spacing.xxl}"
  gemstone-chip:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    gap: "{spacing.xs}"
  gemstone-chip-active:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "6px 14px"
  trust-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    iconColor: "{colors.primary}"
    iconSize: 24px
    padding: "{spacing.lg} {spacing.xl}"
    gap: "{spacing.xxl}"
    borderTop: "1px solid {colors.hairline-soft}"
    borderBottom: "1px solid {colors.hairline-soft}"
  sustainability-badge:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-active}"
    typography: "{typography.label-tag}"
    iconColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    height: 44px
    iconColor: "{colors.muted}"
    placeholderColor: "{colors.muted}"
  size-swatch:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    size: 40px
    typography: "{typography.caption}"
  size-swatch-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    size: 40px
    typography: "{typography.caption}"
  metal-swatch:
    size: 28px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.primary}"
    borderInactive: "2px solid transparent"
  review-stars:
    activeColor: "{colors.gold-vivid}"
    inactiveColor: "{colors.hairline}"
    size: 16px
    typography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.ink-warm}"
    textColor: "{colors.hairline-soft}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.on-dark}"
    headingTypography: "{typography.label-tag}"
    bodyTypography: "{typography.body-sm}"
    accentColor: "{colors.gold}"
    dividerColor: "{colors.muted}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Teal (#108474) fill with white uppercase Lausanne tracked at 0.08em, 48px tall, 8px radius. Hover darkens to forest green ({colors.primary-active}); disabled drains to pale teal fill with muted text. This is the sole CTA that carries the brand's sustainability signal — use it for Add to Cart, Shop Now, and email subscription confirms.

**`button-secondary`** — Transparent with a 1px ink border and identical uppercase Lausanne. On hover the button fully inverts to ink fill with white text — a confident reversal that reads clearly on both pale canvas and dark editorial sections. Use for Wishlist, View All, and Compare.

**`button-ghost`** — Text-only in teal with underline, tracking softened to 0.04em. Suited to inline narrative prompts ("Learn about our materials", "See how we source") and footer utility links where a bordered button would overweight the column.

**`button-gold`** — Gold-vivid (#fbcd0a) fill with warm ink text, reserved for promotional urgency: flash-sale overlays, gift-with-purchase callouts, limited-edition launch panels. Delivers high visibility against both dark and pale grounds without competing with the primary teal hierarchy.

### Navigation

**`nav-bar`** — A 64px near-white bar with hairline-soft bottom border anchors the document top. Logo sits left at max 36px height; nav links (Lausanne 13px, tracking 0.04em) center with category dropdown reveals on hover; search, wishlist, and bag icons right-align at 44px touch targets with a small teal dot on cart count. Mobile collapses to hamburger with a full-height slide-in drawer.

**`announcement-bar`** — Near-black (#121212) band above the nav, 40px tall. White body copy carries shipping thresholds or event windows; promotional copy bolds in gold-vivid (#fbcd0a). Dismissible on desktop; persistent on mobile.

### Product Card

**`product-card`** — Portrait 3:4 image fills the card width with a 1.04x scale on hover. Title in Lausanne 14px weight 500; price in Lausanne 18px weight 400; compare-at price strikes through in muted gray. A zero-radius badge in the image's top-left corner uses teal for "New" or "Bestseller", gold-vivid for "Sale". The card border steps from hairline-soft at rest to hairline on hover — enough shift to register interaction without adding shadow weight.

### Hero Section

**`hero-section`** — Full-bleed editorial photography with a warm dark overlay (rgba 40,38,34 at 40%) for headline legibility. Albra display-xl (48px, weight 400) in white centers the headline; Lausanne body-md in hairline-soft carries the subline. Two CTAs row-stack beneath: button-primary for the primary collection link, button-secondary for secondary navigation. Minimum 620px height on desktop; 480px on mobile.

### Collection Banner

**`collection-banner`** — Deep forest green (#163120) panels introduce category pages — Gold, Silver, Gemstones, Gifts. Headline in Albra display-md (28px) in white; muted gold (#c9c26b) accents category subtitles or short editorial sublines. Minimum 360px height, content left-aligned or centered depending on editorial layout.

### Gemstone Chips

**`gemstone-chip`** / **`gemstone-chip-active`** — Pill-shaped filter tokens in Lausanne caption (12px) with hairline borders at rest and transparent fill. On selection the background shifts to pale teal ({colors.primary-light}), border to primary teal. Lavender (#a89cc8) color dots (10px circle) accompany Amethyst filters; pale teal (#c1e6e6) dots accompany Aquamarine and Topaz — the dot sits left of the label text and provides instant visual association between chip and gemstone.

### Trust Strip

**`trust-strip`** — A horizontal row of icon-plus-label pairs: "Sustainably Made", "Recycled Metals", "Carbon Neutral Shipping", "Certified Packaging", "12-Month Warranty". Icons in primary teal at 24px; background surface-soft; Lausanne caption text in body gray. Full-bleed between page sections with top and bottom hairline borders. On mobile the row wraps to two columns or scrolls horizontally.

### Product Options

**`size-swatch`** / **`size-swatch-active`** — Square 40px tokens in Lausanne caption represent ring sizes and chain lengths. Inactive: white fill, hairline border. Active: full ink fill, white text. The binary inversion avoids confusion with the teal active color used in filter chips — sizing is a selection, not a category filter.

**`metal-swatch`** — Circular 28px swatches show actual metal fill (yellow gold, rose gold, silver, vermeil). A 2px primary-teal ring appears on the active swatch; inactive swatches hold a 2px transparent ring of equal width to prevent layout shift on selection.

### Reviews

**`review-stars`** — Five stars at 16px; filled in gold-vivid (#fbcd0a), empty in hairline (#dedede). Rating count and review total render in Lausanne caption beside the cluster. Judge.me's JudgemeStar font renders the star glyphs; CSS overrides align fill color to the gold-vivid token.

### Footer

**`footer`** — Warm near-black (#282622) ground, four-column link grid on desktop. Column headings in Lausanne label-tag (11px uppercase, 0.08em tracking) in hairline-soft; links in Lausanne body-sm weight 300 in hairline, brightening to white on hover. A full-width newsletter row holds text-input plus button-gold "Subscribe". Social icons at 20px in muted-light, transitioning to on-dark on hover. Muted divider separates the link grid from the legal strip.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero collapses to 480px min-height; nav becomes hamburger drawer; announcement bar persists; gemstone chips scroll horizontally with scroll-snap; trust strip wraps to two columns; hero CTAs stack vertically; footer collapses to single column with accordions |
| Tablet | 744–1128px | Two-column product grid; hero at 540px; nav shows logo and icon row with hamburger for category links; collection banner left-aligns content; trust strip in three-column wrap |
| Desktop | 1128–1440px | Four-column product grid; full horizontal nav bar; hero at 620px; trust strip in single horizontal row; full four-column footer grid |
| Wide | > 1440px | Content max-width 1440px with auto margins; hero extends to 720px; product grid may open to five columns on ultra-wide viewports |

### Touch Targets

- All buttons and icon actions minimum 44×44px tappable area
- Swatch hit areas padded to 44px with invisible touch extension
- Cart and search icons in nav at 44×44px
- Gemstone chip touch areas extended with 8px padding beyond visible border
- Announcement bar dismiss button minimum 44×44px

### Collapsing Strategy

- Footer: four columns → two columns at tablet → single accordion-expandable column at mobile
- Product grid: 4 → 2 → 1 column, gutter narrows from 24px to 16px to 12px
- Trust strip: horizontal row → two-column wrap → vertical stack with left-aligned icons
- Hero CTAs: row → column stack, secondary button full-width below primary
- Nav: full horizontal → icon-only bar with hamburger drawer, search expands to overlay
- Collection banners: side-by-side → stacked at mobile with reduced min-height (240px)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact Albra font weight options not confirmed from CSS extraction — weight 400 assumed as primary display weight; italic or medium variants unknown
- Script-Single font usage context not identified — likely the logo wordmark or a handwritten signature element on packaging pages; no component mapped
- League Gothic usage context not confirmed — may appear in promotional overlays, countdown timers, or sale banners; no component mapped
- Exact product grid gutter values and column padding not extracted
- Mobile hero content alignment (centered vs. bottom-anchored) not confirmed
- Nav dropdown layout and column structure not verified from extraction
- Hover and active states on nav links (underline, color shift, or indicator dot) not confirmed
- Whether #c9c26b or #fbcd0a is the primary promotional gold not determinable from extraction alone — both mapped as separate tokens
- Exact announcement bar height (40px assumed) and whether it has a close button on desktop not confirmed
- PDP (product detail page) layout — image gallery behavior (thumbnails vs. swiper), sticky add-to-cart bar, and accordion sections for details/materials not verified
