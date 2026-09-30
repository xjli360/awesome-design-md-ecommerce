---
version: alpha
name: "Petit Moments"
source_url: "https://www.petitmoments.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Cherry-red punctuation — sale badges, add-to-cart pills, and wishlist hearts in #e8144b — interrupt a near-white blush palette of #fae2e0 and #fff4fa, giving the storefront the feel of a bijouterie window where one bold piece catches the light against tissue paper. FoundersGrotesk runs the transactional layer: navigation labels in small uppercase with open tracking, price strings at a compact 14–18px, and button copy at 12px/0.12em — a vernacular that reads fashion-forward without the self-seriousness of luxury type hierarchies. Baskerville surfaces in campaign headlines and editorial moments, its old-style serifs contrasting the grotesque grid and recalling a fashion lookbook rather than a jeweler's certificate. Product cards sit on clean white against the #fafafa body, images square-cropped at full card width with piece names in {typography.body-sm} and prices stacked directly below; four across on desktop, the grid prioritizes discovery over drama — at costume-jewelry price points shoppers buy from abundance, not singularity. Blush tones cascade from #fae2e0 through #e0b5b2 and #fff4fa as hero backgrounds, collection headers, and review-star fills, keeping the brand consistently warm without committing to a single defining hue. Accent gold (#fbcd0a) surfaces narrowly at promotional callouts; muted teal (#108474) and sage (#13a165) handle success and trust signals in form states. Lavender (#a89cc8) and pale teal (#c1e6e6) hint at seasonal collection palettes. Buttons take {rounded.full} — the pill shape is approachable and gift-store warm — against hairline-bordered card frames and flat-edged inputs that keep the layout structured. The ink (#191919) reads as charcoal rather than absolute black, ensuring blush warmth is never undercut by harsh contrast.

colors:
  primary: "#e8144b"
  primary-active: "#c50d3c"
  primary-disabled: "#f2a0b8"
  sale-red: "#d72c0d"
  ink: "#191919"
  body: "#262626"
  muted: "#5e5e5e"
  muted-soft: "#7b7b7b"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  canvas-warm: "#fafafa"
  surface-soft: "#f1f1f1"
  surface-card: "#ffffff"
  surface-warm: "#f7f7f7"
  on-primary: "#ffffff"
  blush-soft: "#fae2e0"
  blush-pale: "#fff4fa"
  blush-mid: "#e0b5b2"
  accent-gold: "#fbcd0a"
  accent-teal: "#108474"
  accent-teal-soft: "#c1e6e6"
  accent-green: "#13a165"
  accent-lavender: "#a89cc8"

typography:
  display-xl:
    fontFamily: "Baskerville, 'Times New Roman', Georgia, serif"
    fontSize: 42px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Baskerville, 'Times New Roman', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Baskerville, 'Times New Roman', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "FoundersGrotesk, Karla, 'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "FoundersGrotesk, Karla, 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.03em
  body-md:
    fontFamily: "FoundersGrotesk, Karla, 'Nunito Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "FoundersGrotesk, Karla, 'Nunito Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "FoundersGrotesk, Karla, 'Nunito Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  button-md:
    fontFamily: "FoundersGrotesk, Karla, 'Nunito Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "FoundersGrotesk, Karla, 'Nunito Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  price-lg:
    fontFamily: "FoundersGrotesk, Karla, 'Nunito Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: 0
  price-sm:
    fontFamily: "FoundersGrotesk, Karla, 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0
  nav-link:
    fontFamily: "FoundersGrotesk, Karla, 'Nunito Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  badge:
    fontFamily: "FoundersGrotesk, Karla, 'Nunito Sans', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1
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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    padding: 10px 0
  quick-add:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 8px 16px
    opacity: 0
    hoverOpacity: 1
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    placeholder: "{colors.muted-soft}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.canvas-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageRatio: "1:1"
    imageRounded: "{rounded.none}"
    titleTypography: "{typography.body-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.ink}"
    salePriceColor: "{colors.sale-red}"
    originalPriceColor: "{colors.muted}"
    gap: "{spacing.sm}"
    paddingBottom: "{spacing.base}"
  hero:
    backgroundColor: "{colors.blush-pale}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-md}"
    paddingVertical: "{spacing.section}"
    textAlign: center
  collection-header:
    backgroundColor: "{colors.blush-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    paddingVertical: "{spacing.xxl}"
    textAlign: center
  badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 6px
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 6px
  badge-promo:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 6px
  price-block:
    regularColor: "{colors.ink}"
    saleColor: "{colors.sale-red}"
    originalColor: "{colors.muted}"
    regularTypography: "{typography.price-lg}"
    saleTypography: "{typography.price-lg}"
    originalTypography: "{typography.price-sm}"
    originalDecoration: line-through
  review-stars:
    starFillColor: "{colors.blush-mid}"
    starEmptyColor: "{colors.hairline}"
    countTypography: "{typography.caption}"
    countColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: none
    padding: 10px 16px
    height: 38px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    headerTypography: "{typography.title-md}"
    headerBorderBottom: "1px solid {colors.hairline}"
    itemTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-sm}"
    width: 400px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.hairline}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.caption}"
    paddingVertical: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — A full-pill (#e8144b, {rounded.full}) CTA at 44px tall with small-uppercase FoundersGrotesk at 12px/0.12em tracking. Active state deepens to `{colors.primary-active}` (#c50d3c); disabled washes out to a pastel blush `{colors.primary-disabled}`. The pill form is the brand's warmth signal — it appears on every primary action from "Add to Cart" to "Shop Now."

**`button-secondary`** — Matching pill geometry, white fill with a 1px `{colors.ink}` border; effectively a ghost pill. Used for secondary CTAs like "View Details" and "Learn More" alongside the primary cherry. Maintains the same 44px height for pairing in horizontal button groups.

**`button-ghost`** — Transparent background, ink text, no border; used for tertiary actions (dismiss, "continue shopping") where a border would add visual noise. Label inherits `{typography.button-md}` tracking.

**`quick-add`** — A small pill button that floats invisibly over product card thumbnails (opacity 0) and reveals on hover. Smaller padding (8px 16px), `{typography.button-sm}`, with a light `{colors.hairline}` border. Standard for Shopify themes serving discovery-mode shoppers.

### Inputs & Search

**`text-input`** — Slightly rounded rectangle ({rounded.xs}) with a 1px `{colors.hairline}` border that sharpens to `{colors.ink}` on focus. No floating label — placeholder text in `{colors.muted-soft}` disappears on entry. Height 42px keeps mobile tappability while matching the compact scale of the FoundersGrotesk type stack.

**`search-bar`** — Full-pill search field on a `{colors.surface-soft}` background with no border, typically placed inline in the nav or in a full-width overlay. The pill echo of the primary button creates visual consistency across the interactive layer.

### Navigation

**`nav-bar`** — 60px tall, `{colors.canvas-warm}` fill with a 1px `{colors.hairline-soft}` bottom border. Navigation links render in `{typography.nav-link}` (12px uppercase, 0.08em tracking) creating the small-label density typical of multi-category jewelry stores. Logo centered on mobile, left-aligned on desktop.

**`promo-banner`** — A 36px cherry-red (`{colors.primary}`) strip pinned above the nav, white caption text, single promotional string centered. Collapses or hides on scroll in most Shopify themes; re-appears on scroll-up.

### Product Grid & Cards

**`product-card`** — Zero rounding on card and image — the grid reads as a flat editorial spread rather than a softened app layout. Square-cropped imagery fills the card width. Title in `{typography.body-sm}` ink, price in `{typography.price-sm}` immediately below, with no separating line. `quick-add` overlays the image on hover. Sale and New badges (`badge-sale`, `badge-new`) sit at the top-left corner of the image frame.

**`price-block`** — On sale: the sale price prints in `{colors.sale-red}` at `{typography.price-lg}`, with the original struck through in `{colors.muted}` at `{typography.price-sm}`. Regular price renders in `{colors.ink}`. Inline horizontal layout on product page, stacked on card.

**`review-stars`** — Five-star row with fills in `{colors.blush-mid}` (#e0b5b2) — a dusty rose that references the brand palette without the aggression of a primary color. Empty stars use `{colors.hairline}`. Count label in `{typography.caption}` `{colors.muted}`.

### Badges

**`badge-sale`** — Tomato red (#d72c0d, distinct from the cherry primary) for discount callouts. `{rounded.xs}`, 10px uppercase FoundersGrotesk. The hue difference between sale red and primary cherry prevents sale context from bleeding into CTA context.

**`badge-new`** — Same geometry as `badge-sale`, ink fill. A secondary signal sitting on new arrivals or restocks.

**`badge-promo`** — Accent gold (#fbcd0a) fill with `{colors.ink}` text for seasonal promotions. Appears narrowly — gift-with-purchase, holiday campaign labels.

### Content & Layout

**`hero`** — Pale blush canvas (`{colors.blush-pale}` #fff4fa), centered Baskerville headline in `{typography.display-xl}`, supporting copy in `{typography.body-md}`, primary pill CTA. Full-width image heroes alternate with this text-forward layout for editorial campaign pages.

**`collection-header`** — Slightly warmer blush (`{colors.blush-soft}` #fae2e0) with a centered `{typography.display-md}` Baskerville title. Padding at `{spacing.xxl}` top and bottom gives breathing room between the header and the four-column grid below.

### Utility

**`cart-drawer`** — 400px side panel, white canvas, header with title in `{typography.title-md}` separated from line items by a `{colors.hairline}` bottom border. Line items use `{typography.body-sm}` for name and `{typography.price-sm}` for subtotals. Checkout CTA is a full-width `button-primary`.

**`footer`** — Dark ink (`{colors.ink}`) reversal with `{colors.surface-soft}` body text and `{colors.hairline}` links — the brand's only dark-mode zone. Column headings in `{typography.title-sm}`, links in `{typography.caption}`. Newsletter input uses a transparent field with a white underline border rather than the boxed input form.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo; hero text scales to `{typography.display-sm}`; cart drawer goes full-width |
| Tablet | 744–1128px | Two-column product grid; nav links visible if count ≤ 6; hero remains centered; cart drawer at 360px |
| Desktop | 1128–1440px | Four-column product grid; full nav with dropdowns; hero max-width 1200px centered; promo banner visible |
| Wide | > 1440px | Grid max-width 1440px centered with `{spacing.section}` lateral padding; no additional columns added |

### Touch Targets

- All primary buttons minimum 44px tall, full-pill to maximize tap width
- `quick-add` hidden on touch devices; replaced by direct tap-to-PDP navigation
- Nav items minimum 44px hit area on mobile via padding
- Review star row minimum 32px tall for tap-friendly rating browsing

### Collapsing Strategy

- Navigation: links collapse to hamburger at < 744px; search moves to drawer overlay
- Product filters: sidebar on desktop, bottom sheet drawer on mobile
- Collection header: Baskerville headline scales from 42px → 28px → 22px across breakpoints using display-xl → display-md → display-sm
- Footer: four columns stack to single-column accordion on mobile
- Promo banner: 36px on desktop → 44px on mobile (larger touch target for dismissal)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button border-radius not confirmed from extraction; {rounded.full} inferred from pill-button convention common to this Shopify theme tier
- FoundersGrotesk weight usage (400 vs 500 vs 600) not directly observable from color extraction; weights assigned by fashion-jewelry category convention
- No confirmed custom icon set beyond JudgemeIcons (review widget) and JudgemeStar — product and navigation icons likely Shopify theme defaults (SVG, stroke-based)
- Hover and animation timing values (transition duration, easing) not extractable from static color pass
- Exact grid gap and gutter widths not confirmed; `{spacing.sm}` and `{spacing.base}` assigned by Shopify Dawn/Sense theme defaults
- Dark-mode or alternate theme support not determined from extraction
- Lavender (#a89cc8) and light teal (#c1e6e6) usage context unclear — may be seasonal collection-specific or third-party widget colors
