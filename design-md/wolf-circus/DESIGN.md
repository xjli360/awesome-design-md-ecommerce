---
version: alpha
name: "Wolf Circus"
source_url: "https://www.wolfcircus.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Gellix — a geometric grotesque with warmth in its terminals — runs the entire Wolf Circus type system at weights that never climb above Bold, leaving the recycled gold vermeil and sterling silver in product photography to deliver all the color the page requires. The ink tone (#121212) reads softer than pure black, giving typography a matte, almost-printed quality; #dedede mirrors polished sterling silver in dividers and placeholder strokes, turning a structural element into a quiet material reference. Buttons hold a near-square profile with letter-spacing nudged open to 0.10em, signaling that the brand operates at an editorial cadence rather than a conversion-anxious one. The entire canvas is white (#ffffff), uninterrupted by brand-color washes or gradient overlays — the site's color arrives exclusively through product: warm yellow golds, cool silver, the occasional oxidized black finish.

  On the grid, product cards carry no visible border at rest; hover states surface a 1px hairline in #dedede rather than a color shift, keeping the neutral palette intact. Collection headers alternate between Gellix-Bold display at generous tracking and smaller Gellix-Regular body runs, establishing a rhythm borrowed more from print lookbooks than from Shopify's default templates. Navigation collapses to a hamburger on mobile without visible indicator count badges — the expectation is that the catalog is browsed, not searched.

  Ring and necklace category pages use metal-choice swatches (gold vermeil, recycled silver, rose gold vermeil) rendered as small circular chips with a {rounded.full} shape and a 1px border that upgrades to #121212 on selection — the only moment the near-black primary functions as an accent rather than a background. Announcement bars run full-width in #121212 with on-primary (#ffffff) type at caption scale and wide letter-spacing, replacing color urgency with typographic authority.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#aaaaaa"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#888888"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  silver-echo: "#dedede"
  scrim: "rgba(18,18,18,0.45)"

typography:
  display-xl:
    fontFamily: "'Gellix-Bold', 'Gellix', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: 0.02em
  display-md:
    fontFamily: "'Gellix-Bold', 'Gellix', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0.01em
  title-lg:
    fontFamily: "'Gellix-Bold', 'Gellix', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.01em
  title-md:
    fontFamily: "'Gellix-Regular', 'Gellix', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  body-md:
    fontFamily: "'Gellix-Regular', 'Gellix', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0.01em
  body-sm:
    fontFamily: "'Gellix-Regular', 'Gellix', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.01em
  caption:
    fontFamily: "'Gellix-Regular', 'Gellix', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.08em
    textTransform: uppercase
  price:
    fontFamily: "'Gellix-Regular', 'Gellix', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  button-md:
    fontFamily: "'Gellix-Regular', 'Gellix', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.10em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Gellix-Regular', 'Gellix', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.06em
  announcement:
    fontFamily: "'Gellix-Regular', 'Gellix', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.10em
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 44px
    border: none
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
    padding: 13px 31px
    height: 44px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    padding: 0
    textDecoration: underline
    textUnderlineOffset: 3px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.announcement}"
    height: 36px
    paddingHorizontal: "{spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageBorderRest: none
    imageBorderHover: "1px solid {colors.hairline}"
    gap: "{spacing.sm}"
  product-card-title:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.body}"
  metal-swatch:
    width: 18px
    height: 18px
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    gap: "{spacing.xs}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    padding: 8px 16px
    height: 40px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    paddingVertical: "{spacing.section}"
    imageObjectFit: cover
  collection-header:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-md}"
    descTypography: "{typography.body-md}"
    titleColor: "{colors.ink}"
    paddingVertical: "{spacing.xl}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  badge-sold-out:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  accordion-item:
    borderBottom: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-md}"
    titleColor: "{colors.ink}"
    bodyColor: "{colors.body}"
    paddingVertical: "{spacing.base}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.on-primary}"
    headingTypography: "{typography.caption}"
    paddingVertical: "{spacing.xxl}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    overlayColor: "{colors.scrim}"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 36px
    width: 100px

## Components

### Buttons
**`button-primary`** — Full-bleed #121212 fill with white Gellix uppercase label at 0.10em letter-spacing and zero border-radius. Hover darkens to pure #000000. The sharp corners and wide tracking position "Add to Cart" and "Shop Now" actions as deliberate commands; disabled state uses #aaaaaa fill so unavailable options read immediately without a tooltip.

**`button-secondary`** — White fill with a 1px #121212 border and matching Gellix uppercase label. On hover the fill shifts to surface-soft (#f7f7f7), maintaining the outline without introducing a new tone. Used for secondary CTAs such as "View All" and "Learn More."

**`button-ghost`** — No background, no border; a simple underline with 3px offset carries the affordance. Reserved for inline text links within editorial body copy, product description disclaimers, and navigation breadcrumb paths.

### Text Input
**`text-input`** — White canvas with a 1px #dedede hairline border that upgrades to a 1px #121212 stroke on focus; zero radius. Placeholder runs in #888888 muted; typed text in #121212. Used for email capture in footer newsletter blocks, search overlays, and checkout address fields.

### Navigation
**`nav-bar`** — 56px-tall white bar with a bottom 1px #dedede hairline. The brand wordmark sits left-aligned in Gellix-Bold; category links run center or right in nav-link scale (13px, 0.06em tracking); the right cluster holds search, wishlist, and cart icon buttons at 20×20px each with 44×44px touch targets. On scroll the bar gains a `box-shadow: 0 1px 8px rgba(18,18,18,0.06)` to maintain legibility without changing the background color.

**`announcement-bar`** — 36px strip in #121212 above the nav, Gellix uppercase caption at 0.10em tracking in white. Shipping thresholds and promotional copy rotate here via Shopify announcement settings.

### Product Card
**`product-card`** — Square-crop image with no rounding and no shadow at rest. Hover surfaces a 1px #dedede border around the image tile without scaling or lifting the card. Below the image: product name in body-sm (13px), metal variant label in muted caption, price in price scale (14px, #3a3a3a). Metal swatch chips render as 18px filled circles in {rounded.full} with a 1px hairline border; selection upgrades the border to 1px #121212 with a 1px white inset gap creating a halo ring.

### Hero
**`hero-section`** — Full-viewport-width image with editorial copy either overlaid at bottom-left or stacked in a block below the image on mobile. Display type at display-xl (52px Gellix-Bold, 0.02em tracking); supporting text in body-md; primary CTA in button-primary. Vertical padding contracts from section (80px) to xl (32px) at the mobile breakpoint.

### Metal Swatch Selector
**`metal-swatch`** — 18px circular chips in {rounded.full} used on both product cards (passive, no label) and PDP option selectors (text label beneath each chip). Gold vermeil renders at approximately #c6973f fill; recycled sterling silver at #b8b8b8; rose gold vermeil at #d4a090. These fill values are product-photography-derived approximations — the selection interaction (1px #121212 outer border, 1px white gap) is the definitive visual signal regardless of fill.

### Collection Header
**`collection-header`** — White canvas section above the product grid. Collection name in display-md (32px Gellix-Bold); optional editorial description in body-md below. Padding at xl (32px) top and bottom. No background color variation between collections — category identity is carried by the heading text, not color banding.

### Accordion
**`accordion-item`** — Used on PDP for product details, materials, care instructions, and shipping policy. A 1px #dedede hairline separates rows. Title runs in title-md (13px uppercase, 0.08em tracking); expanded body in body-md (15px). A minimal "+" / "−" character right-aligns in #888888 muted; no animated chevron icons.

### Badges
**`badge-new`** — #121212 fill, white Gellix caption uppercase, zero radius, 3×8px padding. Positioned top-left over product card images for new arrivals. **`badge-sold-out`** — #dedede fill with #888888 muted text, same geometry; overlays the image tile so product photography remains visible beneath.

### Footer
**`footer`** — #121212 background, all text in #ffffff. Column headings in caption scale (11px uppercase, 0.08em tracking); links at body-sm (13px). Newsletter form embeds a text-input variant with 1px white border on the dark ground and an inverted button-secondary (white border, white text, transparent fill). Social icons render as simple SVG line icons at 20×20px in white.

### Cart Drawer
**`cart-drawer`** — Slides in from the right at 400px on desktop; full-width bottom sheet on mobile. White canvas with 1px #dedede left-border and a `rgba(18,18,18,0.45)` scrim over the page. Line items show product thumbnail, name in body-sm, metal variant in caption, and price in price scale. Quantity stepper is a 36px-tall 100px-wide box in #dedede border with "−" count "+" centered in body-sm. Checkout CTA inherits button-primary at full drawer width.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark only; hero image full-width with text stacked below; cart drawer expands to full-width bottom sheet; section padding contracts to {spacing.xl} (32px); swatch labels hidden, chips only |
| Tablet | 744–1128px | 2-column product grid; nav shows wordmark and icon cluster, categories in hamburger; hero can adopt side-by-side text layout; announcement bar remains single-line |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with visible category links; collection filter panel as left-rail; cart drawer at 400px fixed width |
| Wide | > 1440px | Max content width 1440px centered with auto side margins; product grid caps at 4 columns; hero imagery scales via object-fit cover; editorial text blocks max-width ~680px |

### Touch Targets
- All icon buttons (search, wishlist, cart) maintain a 44×44px minimum touch target even when the visual icon is 20×20px
- Metal swatch chips expand their hit area to 32×32px on mobile despite rendering at 18×18px
- Accordion row tap area spans the full row width at a minimum of 44px height
- Quantity stepper "−" and "+" buttons are each at least 36×36px on mobile

### Collapsing Strategy
- Primary nav links collapse into a full-screen slide-in drawer at < 744px, preserving category hierarchy as an accordion within the drawer
- Collection filter panel shifts from a persistent left-rail on desktop to a bottom-sheet overlay on mobile, triggered by a "Filter" pill button
- Product image gallery transitions from a multi-thumbnail horizontal strip on desktop to a swipeable full-width carousel with dot indicators on mobile
- Footer columns stack vertically on mobile with each heading acting as a disclosure toggle for its link list

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only two hex colors were extracted (#121212, #dedede); all surface-soft, body, muted, and error tones are inferred from category convention — not confirmed from live site inspection
- Gold vermeil, rose gold, and recycled silver swatch fill colors are approximated from product photography norms; actual rendered values for interactive chips are unconfirmed
- Exact nav height, announcement bar height, and cart drawer width are estimated; Shopify theme stylesheet inspection would confirm precise values
- No accent or highlight color was extracted; Wolf Circus appears to use no supplementary brand color beyond the two confirmed tones — any sale or promotional accent color is unknown
- Gellix font licensing is not publicly documented in detail; fallback stack assumes -apple-system / Helvetica Neue when Gellix fails to load in non-licensed environments
- Button border-radius preference (none vs. xs: 2px) could not be confirmed from extraction; square corners are assumed based on minimalist fine jewelry DTC norms
- Hover and focus animation durations (transition timing) are not extractable from static analysis; 150–200ms ease-in-out is assumed as a standard Shopify default
