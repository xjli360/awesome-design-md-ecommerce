---
version: alpha
name: "Washed Ashore"
source_url: "https://www.washedashore.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The name performs the first design decision — jewelry that arrives already carrying a history of water, pressure, and slow polish, so the pieces themselves don't need to shout. Washed Ashore places demi-fine work against a warm off-white canvas ({colors.canvas}), a ground that reads less like a blank page and more like bleached linen laid out in afternoon light, slightly warm at the weave. The palette inferred from the coastal-jewelry archetype the brand occupies leans on sandy neutrals and burnished gold as the primary signal color ({colors.primary}, a warm #B89A72), with a muted seafoam accent ({colors.seafoam}) that stops well short of cliché turquoise — it's the green of sea glass ground dull by years of tumbling, not the electric aqua of a tourism poster. Type, inferred from the demi-fine category norm, likely runs an elegant editorial serif — something in the Cormorant or Garamond family for display moments — paired with a restrained geometric or humanist sans for body and navigation, keeping the prose editorial and the UI clinical enough to let photography lead. Rounded values are conservative: small radii on buttons and input fields ({rounded.xs} to {rounded.sm}), product cards with barely-perceptible corners ({rounded.sm}), and the occasional {rounded.full} pill reserved for material or collection badges. Spacing is generous, consistent with a brand that trusts negative space as much as it trusts the pieces themselves — wide section padding ({spacing.section}), breathing room between grid items, and a product card that gives the image the overwhelming majority of the visual real estate. Interaction states use darkened and desaturated primary variants rather than dramatic color shifts, keeping the mood even across hover, focus, and press. Gold foil or warm-toned CTA buttons contrast cleanly against the off-white canvas, directing the eye without the urgency of a red CTA system. The overall register is slow, unhurried, and coastal — designed to feel like browsing a very small, very well-lit shop near water, where the proprietor is not watching you.

colors:
  primary: "#B89A72"
  primary-active: "#9A7D58"
  primary-disabled: "#DDD0BB"
  ink: "#1C1A17"
  body: "#3D3830"
  muted: "#7A7268"
  hairline: "#DDD6CE"
  canvas: "#FAFAF7"
  surface-soft: "#F4EFE8"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  seafoam: "#8AABA5"
  seafoam-soft: "#C5D6D3"
  gold-accent: "#C9A85C"
  sand: "#E8DDD0"
  pebble: "#B4A99D"

typography:
  display-xl:
    fontFamily: "'Cormorant Garamond', 'Garamond', 'Georgia', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Cormorant Garamond', 'Garamond', 'Georgia', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Cormorant Garamond', 'Garamond', 'Georgia', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Cormorant Garamond', 'Garamond', 'Georgia', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.04em
  body-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  label-uppercase:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.04em
  price:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  price-lg:
    fontFamily: "'Cormorant Garamond', 'Garamond', 'Georgia', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.08em
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
    padding: 14px 32px
    height: 48px
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
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
    padding: 0
  button-pill-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.display-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    placeholderColor: "{colors.pebble}"
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    gap: "{spacing.sm}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    hoverOverlay: "opacity 0.3s ease"
    badgePosition: "top-left"
  hero-editorial:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    layout: "split-50/50 or full-bleed image with text overlay"
    ctaVariant: "button-primary"
    paddingVertical: "{spacing.section}"
  collection-banner:
    backgroundColor: "{colors.sand}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    captionTypography: "{typography.label-uppercase}"
    captionColor: "{colors.muted}"
    paddingVertical: "{spacing.xxl}"
    textAlign: "center"
  material-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 4px 12px
  product-grid:
    columns: "2 mobile / 3 tablet / 4 desktop"
    gap: "{spacing.base}"
    paddingHorizontal: "{spacing.xl}"
  product-detail-image:
    layout: "sticky scroll — image grid left, info panel right"
    imageRounded: "{rounded.none}"
    thumbnailGap: "{spacing.xs}"
  product-info-panel:
    paddingLeft: "{spacing.xl}"
    titleTypography: "{typography.display-sm}"
    priceTypography: "{typography.price-lg}"
    priceColor: "{colors.body}"
    descriptionTypography: "{typography.body-md}"
    descriptionColor: "{colors.muted}"
    ctaStack: "vertical — button-primary full-width, then button-secondary"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-uppercase}"
    height: 36px
    textAlign: "center"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    width: 420px
    borderLeft: "1px solid {colors.hairline}"
    headerTypography: "{typography.title-md}"
    itemTitleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    totalTypography: "{typography.title-md}"
    ctaVariant: "button-primary"
    rounded: "{rounded.none}"
  swatch-selector:
    size: 24px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.ink}"
    borderInactive: "1px solid {colors.hairline}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"
    headingColor: "{colors.pebble}"
    columns: 4
    paddingVertical: "{spacing.section}"
    borderTop: "none"
  newsletter-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    inputVariant: "text-input"
    ctaVariant: "button-primary"
    layout: "centered column, max-width 480px"
    paddingVertical: "{spacing.xxl}"
  lookbook-tile:
    imageAspectRatio: "3/4"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    hoverOverlay: "rgba(0,0,0,0.08)"
    shopLinkTypography: "{typography.button-sm}"
    shopLinkColor: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — A flat rectangular button with no border radius, warm sand-gold fill ({colors.primary}), white label set in spaced uppercase ({typography.button-md}). On hover the fill shifts to {colors.primary-active}, a deeper warm brown; no box-shadow or lift effect. Disabled state uses {colors.primary-disabled}, a pale desaturated version of the primary, keeping the layout intact without visual noise.

**`button-secondary`** — Same geometry as the primary but transparent-fill with a 1px {colors.ink} border. Used for secondary actions on product detail pages (e.g., "Add to Wishlist" alongside the primary "Add to Cart"). On dark backgrounds, border and label shift to {colors.canvas}.

**`button-ghost`** — No border, no background; {colors.muted} label in {typography.button-sm} uppercase. Used for low-priority links within content areas — "Read more", "See all", navigation-adjacent actions where a full button would be too heavy.

**`button-pill-badge`** — Small {rounded.full} pill in {colors.surface-soft} with {colors.body} text; used for material callouts (e.g., "14K Gold Fill", "Sterling Silver") beneath product titles or in filter bars. Not interactive in all contexts; when tappable, transitions border to {colors.ink} on focus.

### Navigation
**`nav-bar`** — 64px fixed bar on {colors.canvas} with a 1px {colors.hairline} bottom border. The wordmark sits left in {typography.display-sm}, keeping the serif brand voice present at the topmost UI layer. Center nav links use {typography.nav-link} (13px, 0.04em tracking) to maintain the unhurried editorial pace. Right cluster holds search icon, wishlist icon, and bag icon — all 20px strokes, {colors.ink}. Cart count renders as a small {colors.primary} dot with white number, not a bubble badge. The announcement bar ({colors.ink} ground, white {typography.label-uppercase}) sits above the nav, dismissable via a right-aligned X.

### Product Card
**`product-card`** — No border radius, no drop shadow. Image fills a 4:5 frame; on hover a secondary image fades in with `opacity 0.3s ease` rather than a slide — the stillness is intentional. Below the image: product name in {typography.body-sm} {colors.ink}, price in {typography.price} {colors.body}, and any material badges as `button-pill-badge` elements in a horizontal flex row. "SOLD OUT" or "LOW STOCK" labels overlay the image at the bottom-left in {typography.badge} on a semi-opaque {colors.ink} strip.

### Product Detail
**`product-detail-image`** — Sticky scroll: left column holds a vertical thumbnail strip (4 images, 64px wide, {spacing.xs} gap) beside a large primary image; right column holds the info panel. No lightbox by default — click opens a clean full-screen modal with left/right arrow navigation. Image corners are square throughout ({rounded.none}), keeping the coastal-minimal register clean.

**`product-info-panel`** — Title in {typography.display-sm}, price in {typography.price-lg}, both {colors.ink}. Below the price: the `swatch-selector` row for metal/stone variants, a size or length selector (same swatch treatment), then the full-width `button-primary` ("Add to Cart"), then `button-secondary` ("Add to Wishlist"). Product description in {typography.body-md} {colors.muted} beneath a thin {colors.hairline} rule. Material and care details in a collapsible accordion using `title-sm` headers.

### Collection & Editorial
**`collection-banner`** — Full-width {colors.sand} band with centered layout. Collection name in {typography.display-md}, preceded by a category label in {typography.label-uppercase} {colors.muted}. Restrained; no hero image here — the product grid below carries the visual weight.

**`hero-editorial`** — Either a 50/50 split (image left, text right on {colors.surface-soft}) or a full-bleed image with a semi-transparent overlay panel. Headline in {typography.display-xl}, subtext in {typography.body-md}, CTA as `button-primary`. The editorial split layout is preferred for seasonal campaigns; full-bleed for single-product launches.

**`lookbook-tile`** — 3:4 image with a subtle `hoverOverlay` of rgba(0,0,0,0.08). Below: a caption in {typography.caption} {colors.muted} and a "Shop the look" ghost link in {typography.button-sm} {colors.ink}. Tiles appear in a 2-col or 3-col masonry-adjacent grid with consistent {spacing.base} gutters.

### Utility
**`cart-drawer`** — Slides in from the right at 420px on {colors.canvas}, 1px {colors.hairline} left border. Header in {typography.title-md} "Your Bag". Each line item shows a 72px product thumbnail (square crop), title in {typography.body-sm}, variant label in {typography.caption} {colors.muted}, and price in {typography.price} right-aligned. Below the item list: a subtotal row in {typography.title-md}, then the `button-primary` ("Checkout") full-width, then a {typography.body-sm} {colors.muted} note about shipping or free returns.

**`newsletter-strip`** — Centered column on {colors.surface-soft} with headline in {typography.display-sm}, a `text-input` (full-width up to 480px), and `button-primary` below. No decorative elements — the coastal restraint carries through to this utility strip.

**`announcement-bar`** — 36px {colors.ink} strip above the nav, rotating promotional messages in {typography.label-uppercase} {colors.canvas}. Dismissable; once dismissed, the nav slides up to fill the viewport top.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark + bag icon; hero-editorial becomes full-bleed stack (image top, text bottom); cart drawer full-width; product detail layout stacks (images above info panel) |
| Tablet | 744–1128px | 2-column product grid; nav shows partial links or still collapsed; hero-editorial uses 50/50 split; product detail image grid switches to 2-wide with no thumbnail strip |
| Desktop | 1128–1440px | 3–4 column product grid; full nav bar; product detail image uses sticky scroll with thumbnail strip; announcement bar visible |
| Wide | > 1440px | Max content width ~1400px centered; product grid stays at 4 columns; hero-editorial image side gets a subtle parallax offset; generous gutter padding prevents content from touching viewport edges |

### Touch Targets
- All interactive icons (nav icons, swatches, close buttons) minimum 44×44px hit area
- Swatch selectors 24px visual, padded to 40px touch target
- Cart and wishlist icon buttons padded to 44px height in mobile nav
- Accordion headers minimum 48px tall on mobile

### Collapsing Strategy
- Desktop horizontal nav collapses to off-canvas drawer at < 1024px
- Product detail 50/50 layout stacks vertically at < 744px, image always above info
- Collection banner maintains centered text at all widths; font-size scales down one step (display-md → display-sm) at mobile
- Cart drawer goes full-width (100vw) on mobile
- Footer 4-column grid collapses to 2 columns at tablet, single accordion-style columns at mobile
- Lookbook 3-col grid → 2-col at tablet → 1-col at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No color data extracted**: washedashore.co returned no hex values via automated extraction (likely JS-loaded tokens or anti-bot protection). All color values above are inferred from the coastal demi-fine jewelry archetype and the brand name's strong coastal signal. Verified brand palette documentation would supersede all color choices.
- **No font data extracted**: Font stacks above (Cormorant Garamond + Inter) are archetypal for the demi-fine jewelry category. The actual typefaces may differ — custom fonts loaded via @font-face or a hosted foundry (Klim, Grilli Type, Dinamo) would not surface in automated extraction.
- **Platform unconfirmed**: Shopify flag returned False, but platform could not be confirmed. Component assumptions (cart drawer, product detail layout) follow conventions common to headless or custom DTC storefronts rather than a specific Shopify theme.
- **No page title extracted**: Brand's official wordmark casing, subtitle, or SEO descriptor is unknown.
- **Primary brand color confidence is low**: Without verified hex data, the warm sand-gold (#B89A72) is an inference from name and category. If the brand uses a contrasting accent (e.g., deep navy, terracotta, dusty rose) as primary CTA color, the entire button and highlight system would need revision.
- **Interaction patterns unverified**: Hover behaviors (secondary-image swap on product cards, drawer vs. page navigation for cart) are inferred from category norms and not confirmed against live site behavior.
