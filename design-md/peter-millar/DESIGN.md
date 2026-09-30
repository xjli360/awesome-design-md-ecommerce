---
version: alpha
name: "Peter Millar"
source_url: "https://petermillar.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Crown Crafted sits at the apex of Peter Millar's three-tier hierarchy — a designation that names the brand's material ambition and explains why the digital palette reaches for deep collegiate navy (#1B2B4A) rather than the brighter athletic primaries its golf competitors prefer. The site functions as a quiet editorial room: wide white canvas (#FFFFFF), warm off-white surfaces (#F6F5F1), and a single accent — a restrained gold (#C4944A) that traces Crown Sport badge outlines and "New" callout pills. Type scales into display work in a classical serif register, long-tracked and light-weighted, while navigation and product metadata drop into a clean sans-serif at reduced tracking — a pairing that signals wardrobe investment rather than discount urgency. Product cards shed the heavy shadow treatments most contemporary e-commerce uses in favor of an almost frameless float on the surface-soft ground, letting cashmere and merino textures do the persuasion. The checkout and account flows run on the same navy-and-white key, with form fields outlined in hairline (#E2E1DC) strokes that barely interrupt the background. A persistent free-shipping threshold bar runs reversed-navy (#1B2B4A background, white type) above the nav, establishing spend-tier communication before any product is encountered. Collection pages sort by editorial concept — Sport, Crown Crafted, Soft Goods — rather than by category alone, framing each purchase as a wardrobe decision rather than a transactional clothes-buy. The mobile experience compresses the three-column product grid to two columns, retains the sticky nav bar, and moves the filter drawer behind a scrolling chip row, keeping discovery friction minimal without sacrificing the editorial restraint that defines the brand at every screen width.

colors:
  primary: "#1B2B4A"
  primary-active: "#0F1D35"
  primary-disabled: "#8E9BAF"
  accent-gold: "#C4944A"
  accent-gold-light: "#E8D5B0"
  ink: "#1A1A1A"
  body: "#3D3D3D"
  muted: "#767676"
  hairline: "#E2E1DC"
  hairline-soft: "#EDECE9"
  canvas: "#FFFFFF"
  surface-soft: "#F6F5F1"
  surface-warm: "#F0EDE8"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  crown-crafted-brown: "#8B7355"
  sale-red: "#B8262A"
  promo-bar: "#1B2B4A"

typography:
  display-xl:
    fontFamily: "Georgia, 'Palatino Linotype', 'Book Antiqua', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.10
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Georgia, 'Palatino Linotype', 'Book Antiqua', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Georgia, 'Palatino Linotype', 'Book Antiqua', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.21
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Georgia, 'Palatino Linotype', 'Book Antiqua', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.02em
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0.03em
  label-uppercase:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.45
    letterSpacing: 0.12em
    textTransform: uppercase
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.40
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0.04em
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.08em
    textTransform: uppercase
  price-display:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0

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
    height: 48px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
  promo-bar:
    backgroundColor: "{colors.promo-bar}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price-display}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.ink}"
    salePriceColor: "{colors.sale-red}"
    colorSwatchSize: 14px
    gap: "{spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "3px 6px"
  crown-crafted-badge:
    backgroundColor: "{colors.crown-crafted-brown}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  hero:
    layout: full-bleed
    imageHeight: "85vh"
    overlayColor: "rgba(0,0,0,0.18)"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.on-primary}"
    subtitleTypography: "{typography.display-sm}"
    subtitleColor: "{colors.on-primary}"
    ctaComponent: button-primary
    contentAlignment: center-left
  editorial-banner:
    layout: split-50-50
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "{spacing.section}"
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.ink}"
    descriptionTypography: "{typography.body-md}"
    descriptionColor: "{colors.body}"
    padding: "{spacing.xxl} {spacing.section}"
    borderBottom: "1px solid {colors.hairline}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.label-uppercase}"
    textColor: "{colors.ink}"
    activeTextColor: "{colors.primary}"
    height: 44px
    padding: "0 {spacing.base}"
  size-selector:
    selectedBackground: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    unselectedBackground: "{colors.canvas}"
    unselectedTextColor: "{colors.ink}"
    unavailableBorder: "1px solid {colors.hairline}"
    unavailableTextColor: "{colors.muted}"
    rounded: "{rounded.none}"
    typography: "{typography.body-sm}"
    size: 40px
    border: "1px solid {colors.ink}"
  color-swatch-selector:
    size: 20px
    border: "1px solid {colors.hairline}"
    selectedBorderColor: "{colors.ink}"
    selectedBorderWidth: 2px
    rounded: "{rounded.full}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 44px
    iconColor: "{colors.muted}"
  quantity-selector:
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    height: 44px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"
    headingColor: "{colors.on-primary}"
    linkColor: "rgba(255,255,255,0.75)"
    padding: "{spacing.section} 0"
  product-detail-breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"

## Components

### Buttons
**`button-primary`** — Sharp-cornered navy rectangle (`{rounded.none}`, `{colors.primary}`) with white uppercase text tracked at 0.08em; 48px tall with 14px vertical and 32px horizontal padding. Hover deepens to `{colors.primary-active}`; disabled drains to `{colors.primary-disabled}`. The zero-radius choice echoes Peter Millar's architectural, undecorated construction aesthetic — no softened corner should interrupt the garment silhouette reference. Used for primary add-to-cart, checkout continuation, and hero CTAs.

**`button-secondary`** — White fill with a 1px `{colors.primary}` border and navy uppercase label text. On hover the fill lifts to `{colors.surface-soft}`, maintaining navy text and border. Applied to secondary CTAs such as "Add to Wishlist," "View Full Collection," and size guide triggers where a primary CTA is already present on the same surface.

**`button-ghost`** — Transparent background, `{colors.ink}` text with underline decoration, uppercase tracking inherited from `{typography.button-md}`. Used for text-style editorial links inside banner blocks where a bordered button would over-formalize the layout.

### Navigation
**`promo-bar`** — 36px-tall solid navy band above the main nav, white `{typography.caption}` text centered, carrying free-shipping threshold or sale-event messaging. Always visible on desktop; collapses to a horizontal marquee scroll on mobile viewports narrower than 480px.

**`nav-bar`** — White 56px bar with a single hairline bottom border (`{colors.hairline}`). Logo centered on mobile, left-aligned on desktop. Category links in `{typography.nav-link}` with 0.04em tracking; a flyout megamenu appears on hover revealing curated sub-collections. Utility icons — search, account, bag with item count badge — right-aligned with icon-only treatment on desktop. Sticks to the top of the viewport on scroll.

### Product Display
**`product-card`** — Frameless card on `{colors.canvas}`, 3:4 portrait image with no border or shadow. Below the image: a row of 14px color swatches (`{rounded.full}`) followed by product name in `{typography.body-md}` and price in `{typography.price-display}`. Sale pricing shows original struck through in `{colors.muted}` and the reduced price in `{colors.sale-red}`. Badges are absolutely positioned over the top-left image corner.

**`product-card-badge`** — Hairline-bordered white label with uppercase `{typography.badge}` text: "New," "Best Seller," "Low Stock." No color fill — the restraint keeps the editorial grid undisrupted.

**`crown-crafted-badge`** — Warm brown (`{colors.crown-crafted-brown}`) solid badge with white uppercase `{typography.badge}` text, reserved exclusively for Crown Crafted tier products. Signals premium provenance without aggressive promotion energy; appears on both product cards and the PDP above the product title.

### Product Detail
**`size-selector`** — 40×40px square buttons (`{rounded.none}`) with 1px `{colors.ink}` border when available; selected state inverts to `{colors.primary}` background with white text. Unavailable sizes render with `{colors.hairline}` border and a diagonal strikethrough line. Arranged in a wrapping flex row with `{spacing.xs}` gap between buttons.

**`color-swatch-selector`** — 20px circles (`{rounded.full}`) with 1px `{colors.hairline}` border by default; selected state adds a 2px `{colors.ink}` ring with a 2px transparent gap offset, creating a visible selection halo. Hovering reveals a tooltip with the color name in `{typography.caption}`.

**`quantity-selector`** — Decrement icon, numeric count, and increment icon rendered in a single 44px-tall row bounded by a 1px `{colors.hairline}` border on `{colors.canvas}`. No rounded corners; `{typography.body-md}` for the count.

### Content / Editorial
**`hero`** — Full-bleed photography panel at 85vh with a 18% black overlay scrim preventing text washout. Text block runs left-of-center: collection name in `{typography.display-xl}` white serif, optional editorial subline in `{typography.display-sm}` white, then the primary CTA button below. Landscape imagery of lifestyle and sport contexts; never product-on-white.

**`editorial-banner`** — Alternating 50/50 split between editorial photography and copy block set on `{colors.surface-soft}`. Title in `{typography.display-md}`, body prose in `{typography.body-md}` at `{colors.body}`, CTA below. `{spacing.section}` padding on all four sides. Direction alternates (image-left, image-right) between consecutive banners on the homepage.

**`collection-header`** — Full-width `{colors.surface-soft}` band at the top of PLP pages. Collection title in `{typography.display-md}`, optional one-sentence editorial descriptor in `{typography.body-md}` below. A single `{colors.hairline}` rule separates it from the filter bar and grid beneath.

### Commerce Utilities
**`filter-bar`** — Sticky 44px bar beneath the collection header on PLPs. Filter category labels in `{typography.label-uppercase}`; active filter marked in `{colors.primary}` text with a 1px `{colors.primary}` underline. Product count shown right-aligned in `{typography.caption}` at `{colors.muted}`. On mobile collapses to a horizontal scrolling row of 36px chip buttons.

**`search-bar`** — Full-width expanding input triggered from a magnifier icon in the nav bar. `{colors.surface-soft}` fill with 1px `{colors.hairline}` border and `{typography.body-md}` placeholder text. Submit via right-side icon; a dropdown panel below surfaces recent searches and four trending terms in `{typography.body-sm}`.

### Footer
**`footer`** — Full-width navy block (`{colors.primary}`) with a four-column link grid and Peter Millar wordmark in white at bottom-left. Column headings in `{typography.label-uppercase}` white; links in `{typography.body-sm}` at 75% white opacity. A newsletter sign-up input row runs above the link grid: white border, transparent fill, white placeholder text and caret — the `text-input` spec inverted for the dark surface. Social icons in white line style, 20px, right-aligned in the bottom row.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column hero at 100vh; two-column product grid; promo bar scrolls as ticker below 480px; nav collapses to hamburger drawer + centered logo + bag icon; filter bar becomes horizontal scrolling chips; editorial banners stack vertically image-first |
| Tablet | 744–1128px | Two-column product grid; nav retains full text links but megamenu compresses to two columns; hero text shifts to center alignment; editorial banners remain split but copy padding reduces |
| Desktop | 1128–1440px | Three-column product grid; full flyout megamenu on nav hover; editorial banner in true 50/50 split; filter bar sticky with sort dropdown right-aligned |
| Wide | > 1440px | Max-width container centered at 1440px; product grid expands to four columns; hero text block gains additional lateral breathing room; footer grid spreads to five columns |

### Touch Targets
- All buttons minimum 48px tall on touch viewports
- Size selector buttons expand from 40×40px to 44×44px on mobile
- Color swatches increase from 20px to 28px diameter on touch devices
- Filter chips minimum 36px tall with 12px horizontal padding
- Nav bar increases to 64px on mobile for comfortable tap clearance

### Collapsing Strategy
- Three-column product grid → two columns at 744px → single column below 480px
- Mega-nav collapses to full-height hamburger drawer; top-level categories remain as accordion items, sub-collections reveal on tap
- Editorial 50/50 banners stack vertically (image first, copy block below) at mobile breakpoint
- Footer four-column link grid → two columns at tablet → single-column tap-to-expand accordion on mobile
- Promo bar text becomes a marquee scroll below 480px if message exceeds viewport width

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site — the site likely loads design tokens via JavaScript or employs anti-bot protection; all color values above are derived from Peter Millar's well-documented collegiate navy palette and should be verified against the live site in DevTools before production use
- No web font families were detected in extraction; display and body stacks above use Georgia/Helvetica Neue system fallbacks — actual brand typefaces should be audited via the Network tab (WOFF2 requests) on petermillar.com
- Exact border-radius values are estimated at zero consistent with the brand's architectural retail aesthetic, but secondary UI elements (tooltips, drawers) may carry a 2–4px radius
- Crown Crafted brown accent (#8B7355) is inferred from brand photography warmth and the warmth of the collection's marketing materials, not from a documented brand-color specification
- Sale accent red (#B8262A) estimated from luxury menswear retail convention; the live site may use a different hue
- Accent gold (#C4944A) inferred from Crown Sport and Crown Crafted badge photography; exact value not confirmed from CSS extraction
- Megamenu layout column counts and featured-image panel placement not captured
- Animation easing and timing for drawer open, megamenu reveal, and image hover transitions not confirmed
- Specific icon library (proprietary glyphs vs. licensed set) not identified
