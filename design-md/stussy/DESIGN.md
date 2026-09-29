---
version: alpha
name: "Stüssy"
source_url: "https://stussy.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Two colors and a hand-drawn signature — Stüssy's digital presence distills four decades of streetwear credibility into a near-binary palette of #121212 and #dedede, leaving campaign photography and the iconic cursive logo to carry all the visual weight. The site runs on Arial, the most utilitarian of system font stacks, a choice that reads less like an oversight and more like a declaration: the brand has nothing to prove through custom type. Navigation is skeletal — a horizontal strip of category links across a white canvas with no hero animation, no countdown timers, no upsell banners — just a tight product grid and editorial campaign images that run edge to edge at full bleed. Drop culture lives here, but quietly; limited releases surface as ordinary product listings rather than hyped pre-sale pages, trusting the International Stüssy Tribe to already know what matters. The {rounded.none} discipline extends to every container — product cards, text inputs, modal overlays, and size swatches all run with zero border-radius, a hard-edge geometry rooted in the brand's early-1980s Laguna Beach surf-skate origins without sentimentalizing them. On-primary text flips to {colors.on-primary} against the {colors.primary} fill, and the system never reaches for a third hue — every interactive state, hover, and disabled condition resolves through opacity or the #dedede mid-tone, keeping the monochrome discipline intact across every surface. Spacing is generous at wide breakpoints and compresses cleanly on mobile, maintaining the editorial cadence without collapsing into a cluttered layout. The footer runs dense with navigation links at small type scale — an index-pragmatism that respects the community's ability to self-navigate. Product photography does the heavy lifting: large images at high contrast against the near-white canvas, no overlaid badge color beyond a plain text label, no star-rating hero — just garment, light, and the invisible grid that holds everything in place.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#767676"
  ink: "#121212"
  body: "#333333"
  muted: "#767676"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-muted: "#f0f0f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  mid-gray: "#dedede"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.02em
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.04em
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.05em
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.05em
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
  price-display:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  price-struck:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
    textDecoration: line-through

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
    padding: 14px 24px
    height: 48px
    width: 100%
  button-primary-hover:
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
    padding: 13px 23px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
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
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
  product-card-name:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-struck}"
    textColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    imageLayout: full-bleed
    textOverlay: false
    minHeight: 80vh
  hero-caption:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} 0"
  drop-label:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: "2px 6px"
  sale-label:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    backdropColor: "rgba(18,18,18,0.4)"
  size-swatch:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 40px
    minWidth: 40px
  size-swatch-selected:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  size-swatch-unavailable:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary-disabled}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    textDecoration: line-through
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    borderBottom: none
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    paddingTop: "{spacing.xl}"
  footer-link:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    hoverUnderline: true
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"

## Components

### Buttons
**`button-primary`** — Full-width #121212 fill with white uppercase Arial type at 0.05em tracking, zero border-radius, 48px height. Hover state deepens to #000000; disabled state drops to {colors.primary-disabled} fill while keeping {colors.on-primary} label. The sharp rectangle is the singular house shape — no pill, no softened corner, no drop shadow — applied consistently from add-to-bag to newsletter subscribe.

**`button-secondary`** — White canvas with a 1px {colors.ink} border and identical uppercase type scale. Hover shifts fill to {colors.surface-soft}. Used on PDPs alongside `button-primary` — typically "Notify Me" or an out-of-stock fallback — and preserves the same hard-edge geometry so the two buttons stack without visual friction.

### Text Input
**`text-input`** — Zero radius, 1px {colors.hairline} border at rest, upgrading to 1px {colors.ink} on focus. 48px height with 12px vertical padding. Deployed in the search overlay, newsletter footer signup, and checkout address fields. No floating label animation — placeholder text vanishes on type, maintaining the brand's no-ceremony approach to form UI.

### Nav Bar
**`nav-bar`** — 60px tall, white canvas, 1px {colors.hairline} bottom border. Logo left-aligned on mobile, centered on desktop; category links run as a flat horizontal list in 13px Arial with no weight differentiation. Cart and search icons sit right-aligned. There is no mega-menu animation — the `nav-dropdown` panel appears flush below the bar with a 1px {colors.hairline} top border and disappears without easing, consistent with the brand's instantaneous, no-flourish interaction style.

### Product Card
**`product-card`** — 3:4 aspect ratio imagery with zero corner treatment, a tight gap below the image to the product name in {typography.title-sm} and price in {typography.price-display}. Secondary image swaps in on hover with no transition. Color swatches, when present, render as small flat squares with no radius. Sale pricing shows the original amount struck through in {colors.muted} via `product-card-price-sale`, with the sale figure in standard {colors.ink}. No hover elevation, no shadow — tiles stay flat within the grid.

### Hero
**`hero`** — Full-bleed campaign imagery at a minimum of 80vh, no text overlay by default. Campaign copy, when present, appears below the image as a `hero-caption` block in {typography.body-sm} and {colors.muted}, maintaining strict editorial separation between image and word. No autoplay carousel; if multiple frames exist, manual arrow controls appear flush with the image edge.

### Drop / Sale Labels
**`drop-label`** — A 1px {colors.ink}-bordered rectangle in {typography.caption-bold} uppercase, white background. Applied top-left on product cards for new arrivals and collaborations. No accent color for "new" — the brand keeps the monochrome constraint even at the label level.

**`sale-label`** — Inverse of the drop label: #121212 fill with {colors.on-primary} caption text. Indicates discounted product on the grid tile and the PDP image area.

### Search Overlay
**`search-overlay`** — A full-width input bar that expands from the nav on icon tap, 1px {colors.hairline} border, no corner radius. A 40%-opacity ink scrim drops behind it to signal modal state without obscuring page context. Results populate below as a flat link list in {typography.body-sm}, sorted by relevance with no category grouping chrome.

### Size Swatches
**`size-swatch`** — Square-corner 40px-tall tiles, 1px {colors.hairline} border at rest, {typography.caption-bold} label. Selected state fills with {colors.ink} and inverts to {colors.on-primary} text with a matching solid border. Unavailable sizes render in {colors.primary-disabled} with a strikethrough; the border remains to preserve grid alignment.

### Category Tab
**`category-tab`** — {typography.nav-link} in {colors.muted}; active state switches to {colors.ink} with a 2px bottom-border underline, no fill change. Used in product listing filter rows and collection sub-navigation. The underline is the only active indicator — there is no pill background or highlight.

### Footer
**`footer`** — White canvas, 1px {colors.hairline} top border, dense 12px {typography.caption} links organized in columnar groups. No bold section headers — all footer text sits at the same weight, using only spacing to delineate columns. Newsletter input uses the standard `text-input` component. Region selector and legal links sit in a bottom strip, also in {typography.caption}, maintaining the flat typographic hierarchy to the last line.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero clamped at 60vh; size swatch row wraps; footer collapses to accordion sections |
| Tablet | 744–1128px | Two-column product grid; nav shows partial category list or remains hamburger; hero stays full-bleed |
| Desktop | 1128–1440px | Three- to four-column product grid; full horizontal nav with instant dropdown flyouts; hero at 80vh |
| Wide | > 1440px | Grid caps at four columns with wider gutters; content container centered at max-width; hero fills viewport width without cropping key subjects |

### Touch Targets
- All buttons minimum 48px height on mobile
- Size swatches 44×44px minimum touch target on mobile even when visually rendered at 40px
- Nav icon buttons (cart, search, hamburger) 44×44px minimum
- Footer accordion triggers 48px minimum height per row

### Collapsing Strategy
- Nav: full horizontal list → hamburger drawer. Drawer opens as a full-height white overlay from the left, {colors.hairline} separators between items, no animation easing.
- Product grid: 4 col → 3 col → 2 col → 1 col across breakpoints.
- Footer: multi-column link grid → single-column accordion. Newsletter row remains visible at all breakpoints.
- Hero: aspect ratio maintained, height clamped at 60vh on mobile to preserve above-fold product access.
- Filters / sort: side panel on desktop → bottom sheet drawer on mobile with 48px trigger row.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only two hex values were extracted (#dedede, #121212); canvas white (#ffffff), body text grays, muted tones, and surface variants are inferred from brand convention — not confirmed from live DOM extraction.
- Font stack reports "Arial, inherit, serif !important" — the site may load a licensed or custom display face for editorial headers that was not captured in CSS font-family declarations; all typography defaults to Arial here.
- No accent, link, error, or success colors were extracted; error red, link color, and validation states are omitted rather than fabricated.
- No explicit border-radius values were confirmed from the live site; {rounded.none} as the dominant shape is inferred from the brand's documented hard-edge aesthetic, not measured from the DOM.
- No spacing scale or column count was captured; grid and spacing values follow streetwear-retail convention and should be validated against live layout measurements.
- Interactive state tokens (focus ring color, hover opacity values) are derived from palette extension, not live extraction.
- No motion, animation, or transition tokens were captured; all interaction timing should be treated as unspecified.
