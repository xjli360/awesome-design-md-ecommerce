---
version: alpha
name: "Buck Mason"
source_url: "https://buckmason.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Rust and sand — Buck Mason's visual identity rests on the contrast between #b73e25, a terracotta pulled from the American Southwest, and the warm putty tones (#dddad0, #fafaf8) that replace clinical white on every surface. The primary activates sparingly: buy buttons, sold-out markers, sale callouts, nothing else. Everything between those red moments is a studied sequence of near-neutrals that makes product photography do the work a brand with more insecurity would hand to graphic pattern or color block. BigCaslon FB anchors the editorial layer — full-width hero headlines at 56px, weight 400, bracketed serifs that recall mid-century American catalog lettering. Acumin Pro Condensed takes the operational layer: all caps, tight tracking, at 11–14px it labels navigation, filters, category headers, and product name lines without competing with the image. Proxima Nova Wide handles CTAs and overlines, its wide stance lending quiet authority to 13px uppercase button text. Overpass Mono surfaces only at micro-scale for SKU codes and size-chart reference numbers, a typographic register that signals manufacturing traceability rather than affectation. Corner radius is effectively zero ({rounded.none}) on every interactive component — buttons, inputs, filter chips, size selectors — a hard edge that reads as functional rather than decorative, the UI equivalent of a raw seam. The announcement bar alternates between near-black (#111111) for evergreen messaging and neon #4bff40 for sale events, a shock-contrast move that makes the brand's usual restraint read as deliberate economy. An olive (#7c7d5f) bridges the warm neutrals and the earthy product range — field fatigue colors, washed indigo — appearing in category navigation highlights and editorial background blocks. The product grid uses a strict 3/4 portrait ratio with no hover overlays beyond a discreet secondary colorway swatch; the image alone closes the sale, trusting the product to speak first.

colors:
  primary: "#b73e25"
  primary-active: "#82311f"
  primary-disabled: "#d4a090"
  primary-light: "#e57043"
  ink: "#111111"
  body: "#252525"
  muted: "#767676"
  muted-soft: "#aaaaaa"
  hairline: "#dddad0"
  hairline-soft: "#eeeeee"
  canvas: "#fafaf8"
  surface-soft: "#f4f2ec"
  surface-card: "#f3f1ef"
  surface-warm: "#dddad0"
  on-primary: "#fafaf8"
  on-dark: "#fafaf8"
  olive: "#7c7d5f"
  olive-muted: "#97b43b"
  promo-flash: "#4bff40"
  scrim: "#111111"

typography:
  display-xl:
    fontFamily: "'big-caslon-fb', 'Big Caslon', Georgia, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'big-caslon-fb', 'Big Caslon', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'big-caslon-fb', 'Big Caslon', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'big-caslon-fb', 'Big Caslon', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'acumin-pro-condensed', 'Acumin Pro Condensed', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  title-sm:
    fontFamily: "'acumin-pro-condensed', 'Acumin Pro Condensed', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'acumin-pro', 'Acumin Pro', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'acumin-pro', 'Acumin Pro', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'acumin-pro', 'Acumin Pro', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'proxima-nova-wide', 'Proxima Nova Wide', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'proxima-nova-wide', 'Proxima Nova Wide', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'acumin-pro-condensed', 'Acumin Pro Condensed', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'acumin-pro', 'Acumin Pro', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
  mono-sm:
    fontFamily: "'Overpass Mono', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  overline:
    fontFamily: "'proxima-nova-wide', 'Proxima Nova Wide', Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 2px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: none
    textDecoration: underline
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
    logoTypography: "{typography.display-sm}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    iconColor: "{colors.ink}"
    cartBadgeBackgroundColor: "{colors.primary}"
    cartBadgeTextColor: "{colors.on-primary}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    height: 36px
    padding: 0 16px
  promo-announcement-bar:
    backgroundColor: "{colors.promo-flash}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    height: 36px
    padding: 0 16px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    productNameTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    colorwayLabelTypography: "{typography.caption}"
    colorwayLabelColor: "{colors.muted}"
    swatchSize: 16px
    swatchGap: 4px
    padding: 8px 0
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    selectedBackgroundColor: "{colors.ink}"
    selectedTextColor: "{colors.on-dark}"
    selectedBorder: "1px solid {colors.ink}"
    unavailableBorder: "1px solid {colors.hairline-soft}"
    unavailableTextColor: "{colors.muted-soft}"
    unavailableDecoration: line-through
    size: 40px
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    selectedRingColor: "{colors.ink}"
    selectedRingWidth: 2px
    selectedRingOffset: 2px
  hero-full-bleed:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.title-md}"
    overlineTypography: "{typography.overline}"
    overlayScrim: "linear-gradient(to bottom, transparent 40%, rgba(17,17,17,0.6) 100%)"
    ctaVariant: button-primary
  editorial-split:
    imageColumnWidth: "55%"
    textColumnWidth: "45%"
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    overlineTypography: "{typography.overline}"
    overlineColor: "{colors.muted}"
    padding: 48px
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-lg}"
    descriptionTypography: "{typography.body-md}"
    padding: 64px 48px
  category-nav-pill:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: 6px 14px
    activeTextColor: "{colors.ink}"
    activeBorderBottom: "2px solid {colors.ink}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline}"
    height: 48px
    padding: 0 24px
  sku-label:
    typography: "{typography.mono-sm}"
    textColor: "{colors.muted}"
  product-detail-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
    salePriceColor: "{colors.primary}"
    strikethroughColor: "{colors.muted-soft}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    inputBorder: none
    inputBorderBottom: "1px solid {colors.hairline}"
    backdropColor: "rgba(17,17,17,0.4)"
    suggestionTypography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-md}"
    headingColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    borderTop: "1px solid #333333"
    padding: 48px 64px

## Components

### Buttons

**`button-primary`** — Sharp-cornered ({rounded.none}), terracotta (#b73e25) fill with Proxima Nova Wide uppercase text at 13px/+1.5px tracking. The 48px height and 32px horizontal padding give a generous click target without excess visual mass. Hover darkens to #82311f (`button-primary-active`); disabled washes to the dusty #d4a090 (`button-primary-disabled`), never graying out in a way that suggests system failure.

**`button-secondary`** — Transparent fill with a 1px `{colors.ink}` stroke, same type spec as primary. Inverts to black fill on active state, which avoids a separate outline-hover that might read as a hover flash. Used heavily on product pages alongside primary for "Add to Wishlist" and "Find In Store" parity CTAs.

**`button-ghost`** — Text-only with underline, 11px Proxima Nova Wide uppercase, no border or fill. Appears for secondary links inside modals, size-guide openers, and policy disclaimers at the base of the cart drawer.

### Navigation

**`nav-bar`** — 60px tall, warm white (#fafaf8) background with a 1px `{colors.hairline}` bottom border. "BUCK MASON" wordmark in BigCaslon FB at 20px carries the brand weight without a logomark; Acumin Pro Condensed at 13px uppercase handles all nav links. Icon-button targets (search, cart, account) are 40px touch targets. The cart badge uses the terracotta primary (#b73e25) to match the site's CTA register, ensuring the count reads as urgent.

**`announcement-bar`** — 36px near-black strip in `{colors.ink}` for evergreen rotating messages (free shipping thresholds, store locations). Toggled to `promo-announcement-bar` during sale events: the neon #4bff40 fill against `{colors.ink}` text is a deliberate polarity flip that the otherwise austere palette makes visible across the room.

### Product Grid & Cards

**`product-card`** — Zero-radius, 3/4 portrait image container. Product name in Acumin Pro 14px, price in Acumin Pro 16px weight 400 below it, colorway label in 12px muted caption. Swatch row sits between name and price: 16px circles at `{rounded.full}`, gap 4px, selected swatch ringed with 2px `{colors.ink}` at 2px offset. No card shadow, no hover zoom animation — only the secondary colorway image fades in on desktop hover, keeping interaction feedback in the image layer rather than the card chrome.

**`product-card-badge`** — Flush rectangle in `{colors.primary}`, `{typography.title-sm}` (11px condensed uppercase), 3px 8px padding. Absolute-positioned top-left of the product image. Used for "NEW", "SALE", "ALMOST GONE" — never stacked; only the highest priority badge appears.

### Product Detail

**`size-selector`** — 40×40px flat tiles, `{rounded.none}`, 1px `{colors.hairline}` border at rest. Active tile inverts to `{colors.ink}` fill with `{colors.on-dark}` text; unavailable tiles take a lighter hairline border, strikethrough text in `{colors.muted-soft}`, and a cursor-not-allowed state. Sizing runs in `{typography.title-sm}` uppercase, consistent with filter and nav chrome. No carousel or dropdown — all sizes display in a wrapping flex grid.

**`color-swatch`** — 20px diameter circles at `{rounded.full}`. Selected state uses a 2px ring in `{colors.ink}` at 2px offset rather than a checkmark overlay, preserving color readability. Tooltips on hover show the colorway name in `{typography.caption}`.

**`product-detail-price`** — Acumin Pro 16px weight 400 in `{colors.ink}`. Sale price shifts to `{colors.primary}` (terracotta), original price renders in `{colors.muted-soft}` with text-decoration line-through to its right.

**`sku-label`** — Overpass Mono 11px in `{colors.muted}`, displayed below the product title block. Anchors the product in a manufacturing register without drawing visual attention.

### Editorial & Hero

**`hero-full-bleed`** — Edge-to-edge image with a bottom-biased gradient scrim (transparent → rgba(17,17,17,0.6)). Headline in BigCaslon FB 56px/400 weight, subhead in Acumin Pro Condensed 14px uppercase with +1.5px tracking. CTA uses `button-primary`. Mobile collapses headline to `{typography.display-lg}` at 40px.

**`editorial-split`** — 55/45 image-to-text column split on a `{colors.surface-soft}` (#f4f2ec) field. Overline in `{typography.overline}` (10px Proxima Nova Wide, 2px tracking, muted color) precedes the BigCaslon headline. Body copy in Acumin Pro 16px/1.6 line-height. Columns stack vertically on mobile, image first.

**`collection-header`** — Full-width banner on `{colors.surface-soft}` background, 64px top-bottom padding. BigCaslon FB at 40px titles the collection; description body at 16px Acumin Pro beneath. No hero image — the header block is typographic only, letting the product grid carry visual weight.

### Navigation & Filtering

**`category-nav-pill`** — Inline text links in `{typography.title-sm}` uppercase; inactive state in `{colors.muted}`, active in `{colors.ink}` with a 2px `{colors.ink}` underline border rather than a background fill. No border-box or pill shape — flat underline emphasis only.

**`filter-bar`** — 48px sticky strip in `{colors.canvas}` with 1px `{colors.hairline}` bottom border. Sort and filter triggers in `{typography.title-sm}` uppercase. Active filter count appears as a numeric suffix in `{colors.primary}`.

### Search

**`search-overlay`** — Full-width panel slides down from nav at 100% viewport width. Input field: no outer border, only a 1px `{colors.hairline}` bottom border on the text field itself. Input text in Acumin Pro 16px. Suggestions list in 14px Acumin Pro with matching term bolded. Backdrop scrim at rgba(17,17,17,0.4) covers the rest of the viewport.

### Footer

**`footer`** — Near-black (#111111) field with `{colors.on-dark}` (#fafaf8) text. Column headings in `{typography.title-md}` (14px Acumin Pro Condensed uppercase), links in `{typography.body-sm}` (14px Acumin Pro) at `{colors.muted-soft}`. A 1px #333333 top border separates it from the page body. Social icons are minimal SVG outlines at 20px. Newsletter input uses a dark-field variant: transparent background, 1px muted-soft border, on-dark text, primary-color subscribe button.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to `{typography.display-lg}` (40px); nav collapses to hamburger menu with slide-in drawer; filter bar becomes a bottom sheet; editorial-split stacks image over text |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; editorial-split holds side-by-side at reduced padding; hero headline at `{typography.display-xl}` (56px) |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with all primary links visible; collection-header at full 64px padding; editorial-split at 55/45 ratio |
| Wide | > 1440px | Content locked to max-width ~1440px with symmetric side margins; product grid stays four columns; hero image scales to fill but text block is centered within the max-width container |

### Touch Targets

- All nav icon buttons (search, cart, account) minimum 40×40px tap target
- Size selector tiles 40×40px minimum — do not reduce below this on mobile
- Color swatches expand to 28px on mobile with 4px gap maintained
- Filter/sort triggers in the filter bar: minimum 44px height on mobile
- Announcement bar links: 36px full-height tap zone

### Collapsing Strategy

- Primary nav collapses at 744px to hamburger; drawer slides in from left over a scrim
- Category sub-nav (category-nav-pill row) becomes a horizontally scrollable strip on mobile with no scroll indicator arrows
- Editorial-split reflows image above text block; image goes 100% width, text block gets 24px horizontal padding
- Filter bar becomes a fixed bottom sheet on mobile with "Filters" and "Sort" as two equal tap targets that open modal panels
- Footer four-column layout collapses to single-column accordion on mobile; each heading is a tap-to-expand disclosure

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed line-height or letter-spacing values for navigation — estimated from visual inspection of common Acumin Pro Condensed usage patterns
- BigCaslon FB weight variants not confirmed beyond 400; site may use 500 or 600 for certain editorial contexts
- Exact nav bar height not extracted — 60px is an estimate; could be 56px or 64px
- Hover states for product-card image crossfade (primary → secondary colorway) not confirmed — behavior inferred from common Shopify apparel pattern
- Mobile menu drawer animation (slide vs. fade) not extracted
- Cart drawer behavior (sidebar fly-in vs. page overlay) not confirmed from extraction
- bio-sans font stack detected but no clear usage mapping identified — may be a fallback or legacy stack
- Exact grid column gaps (product grid gutter width) not extracted; 16px or 24px gutter likely
