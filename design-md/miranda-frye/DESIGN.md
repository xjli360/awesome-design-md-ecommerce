---
version: alpha
name: "Miranda Frye"
source_url: "https://www.mirandafrye.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The lightbox is mint — a pale seafoam wash (#e6f7f4) that Miranda Frye uses as hero backgrounds and editorial card surfaces, giving gold and silver pieces a coolly luminous ground that reads like a clean jeweler's tray rather than a lifestyle aspirational shot. Against that signature surface, a near-black charcoal (#272727) carries headlines set in a Baskerville–Caslon–Garamond cascade: three closely related bracketed-serif typefaces stacked in explicit fallback order, a typographic specificity unusual on Shopify and one that signals the brand's editorial self-awareness. The primary navigation and CTA structure sits in deep navy (#121f36), anchoring the hierarchy without competing with the jewelry itself; button fills darken on interaction while the canvas stays bright and airy. A warm cream (#fef3e2) surfaces in banner sections and promotional callouts, giving the palette a second neutral that reads like aged linen beside the cooler mint. The spacing system is generous — sections breathe at 64px gaps, product grids give each piece room to read as an object rather than merchandise in a tile. Sans-serif body copy in Inter or Muli keeps navigation and utility text legible and modern against the more classical display faces; the contrast between editorial serif headlines and functional sans body is one of the brand's defining voice moves. Price points are treated as metadata, set in small muted type so they don't crowd the product name. The steel-blue-gray mid-tone (#b1b7c3, #999ea8) appears in secondary text and disabled states, softening transitions without reaching for a high-contrast error palette. The amber gold (#f59e0b) surfaces sparingly — likely in promotional badge fills or low-stock indicators — and the teal (#338fb1) appears in link accents or informational banners. Form corners sit at a modest 4px radius: enough to avoid hard brutalism but far from the pill-shaped softness of lifestyle wellness brands. This is a brand that sells wearable precision, and the UI language mirrors it.

colors:
  primary: "#121f36"
  primary-active: "#0b1322"
  primary-disabled: "#b1b7c3"
  ink: "#272727"
  body: "#4c4c4c"
  muted: "#888888"
  muted-soft: "#9b9b9b"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-mint: "#e6f7f4"
  surface-cream: "#fef3e2"
  surface-light-blue: "#f4f8fe"
  on-primary: "#ffffff"
  accent-gold: "#f59e0b"
  accent-teal: "#338fb1"
  steel-mid: "#999ea8"
  error: "#ea0202"
  error-bg: "#f8d7da"
  error-text: "#721c24"
  success-bg: "#d4edda"
  success-text: "#155724"
  warning-bg: "#fff3cd"
  warning-text: "#856404"
  scrim: "#1c1c1c"

typography:
  display-xl:
    fontFamily: "Baskerville, 'Baskerville Old Face', Caslon, Garamond, Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Baskerville, 'Baskerville Old Face', Caslon, Garamond, Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Baskerville, Caslon, Garamond, Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Baskerville, Caslon, Garamond, Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.1px
  title-sm:
    fontFamily: "Inter, Muli, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  body-md:
    fontFamily: "Inter, Muli, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, Muli, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, Muli, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  price:
    fontFamily: "Inter, Muli, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Inter, Muli, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Inter, Muli, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "Inter, Muli, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
  badge:
    fontFamily: "Inter, Muli, -apple-system, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.muted}"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-mint}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.primary}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cream:
    backgroundColor: "{colors.surface-cream}"
    headlineTypography: "{typography.display-md}"
    headlineColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "{spacing.xxl} {spacing.xl}"
  section-header:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.body}"
    marginBottom: "{spacing.xl}"
  collection-label:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  badge-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  price-display:
    regularColor: "{colors.muted}"
    saleColor: "{colors.error}"
    typography: "{typography.price}"
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    borderActive: "1px solid {colors.primary}"
    backgroundActive: "{colors.primary}"
    textColorActive: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  pdp-gallery:
    backgroundColor: "{colors.surface-mint}"
    thumbnailBorder: "1px solid {colors.hairline}"
    thumbnailBorderActive: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
  swatch-button:
    size: 24px
    borderActive: "2px solid {colors.primary}"
    borderInactive: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.steel-mid}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Deep navy (#121f36) fill with white type set in uppercase tracked {typography.button-md}. The {rounded.xs} radius (4px) keeps edges precise and jeweler-clean; this is not a pill brand. Active state darkens to #0b1322; disabled washes to the steel-gray {colors.primary-disabled} without losing the rectangular form. The 1.5px letter-spacing signals restraint rather than aggression — the same register as a hallmark stamped into metal.

**`button-secondary`** — White fill with a 1px deep navy border and navy type via {typography.button-md}, a mirror to `button-primary`. Used on secondary CTAs like "Explore the Collection" where competing fills on the same viewport would crowd the hierarchy.

**`button-ghost`** — Transparent with underline and {typography.button-sm}. Appears in editorial contexts and footer navigation where the button affordance is optional and the text itself carries the weight.

### Inputs
**`text-input`** — Single-pixel hairline border (#dedede) at rest, sharpens to primary navy on focus. Lowercase {typography.body-md}, 48px height aligned to button height for form-row harmony. No fill color shift on focus — border change is the sole feedback signal, keeping the form surface visually calm.

### Navigation
**`nav-bar`** — White canvas, 64px height, hairline-soft bottom border. Nav links in {typography.nav-link} (Inter 500, 13px, +0.5px tracking) feel editorial without being heavy. On scroll, a subtle drop shadow likely replaces color change. Logo positioned center or left in display serif.

**`announcement-bar`** — Deep navy strip above the nav, 36px tall, caption-weight white type. Creates a visual bookend with the navy footer, sealing the page in brand color at both ends. Used for free-shipping thresholds, sale announcements, and new-drop messaging.

### Product Card
**`product-card`** — No card border or shadow; image bleeds to the grid gutter. Product name in {typography.title-md} (Baskerville 18px, 400 weight) sits directly below the image with {spacing.sm} gap; price in small muted Inter below that. The serif product title gives each piece a proper-noun feeling — named rather than catalogued. Hover states likely reveal a secondary lifestyle image via crossfade rather than a button overlay, consistent with the non-intrusive surface language.

### Hero
**`hero-banner`** — The signature mint surface (#e6f7f4) is the primary hero ground. Display headline in {typography.display-xl} (Baskerville 48px) over the color wash; no photographic background on editorial hero moments, letting the mint read cleanly as a jeweler's display context. {spacing.section} vertical padding gives the headline room to exist as an object. CTA in `button-primary` below.

**`hero-cream`** — Warm cream variant (#fef3e2) for seasonal or promotional sections. Suggests warmth and gold-adjacent richness without using literal gold fills. Headline at {typography.display-md}.

### Badges
**`badge-new`** — Zero-radius rectangle in deep navy, 10px uppercase white type in {typography.badge}. Sits upper-corner on new arrival imagery. The flat rectangle against soft jewelry contexts creates deliberate punctuation.

**`badge-gold`** — Amber fill (#f59e0b) for "Bestseller" or material-callout labels. The only warm accent tone in an otherwise cool palette — used with restraint so it retains signal value.

**`badge-sale`** — Error red (#ea0202) for sale-price labeling, consistent with the `price-display` sale color so the signal is unified across the card.

### Filter Pills
**`filter-pill`** — {rounded.full} pills for collection filtering by metal type, stone, or category. Default white with hairline border; active inverts to navy fill and white type. The pill shape provides deliberate contrast to the otherwise sharp-edged button and input system, marking sorting affordances as categorically distinct from transactional CTAs.

### PDP Gallery
**`pdp-gallery`** — Mint surface (#e6f7f4) as image-well background, carrying the hero color into the product detail page so pieces feel continuous with the editorial brand environment. Active thumbnail framed with 1px primary navy border; no rounded corners on image frames to keep focus on the object itself.

### Footer
**`footer`** — Deep navy fill (#121f36) mirrors the announcement bar, sealing the page in brand color. White body copy, steel-gray links ({colors.steel-mid}) for secondary nav columns. Section headings in uppercase-spaced {typography.title-sm}. Newsletter input embedded inline with white border against the dark field.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero headline scales to {typography.display-sm}; PDP gallery becomes horizontal scroll strip |
| Tablet | 744–1128px | Two-column product grid; nav shows primary categories inline, secondary in dropdown; hero headline and image may stack vertically |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav visible; hero runs full viewport width at {spacing.section} vertical padding |
| Wide | > 1440px | Content max-width ~1400px centered; hero crops to maintain aspect ratio; grid holds at four columns |

### Touch Targets
- All buttons, nav links, and swatch controls minimum 44×44px touch area
- Swatch buttons at 24px visual size padded to 44px tap zone
- Filter pills minimum 36px height on mobile, 44px if stacked in a filter drawer
- Announcement bar dismiss or scroll controls minimum 44px tap area

### Collapsing Strategy
- Mega-nav collapses to full-screen side drawer on mobile with flat category list and close button
- PDP sticky add-to-cart bar pins at viewport bottom on mobile below the fold
- Collection filters migrate from inline sidebar to a bottom-sheet modal on mobile
- Announcement bar may scroll-marquee on narrow widths rather than truncate with ellipsis

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.
- Exact logo typeface and custom lettering not confirmed; Baskerville is the inferred display face but the wordmark may be set in a proprietary cut
- Whether mint (#e6f7f4) is used as a full hero background or only as product-image tray background requires visual confirmation
- Several near-black values (#141414, #171722, #1c1c1c) suggest possible dark-section treatments or alternate surface modes, but a full dark mode is unconfirmed
- Hover and focus animation easing/timing values not extractable from static hints
- Exact product grid gutter width and column breakpoints not confirmed
- Custom icon set (jewelry category glyphs, ring/necklace/earring pictograms) presence unconfirmed
- Whether #338fb1 (teal) is a link accent, informational banner color, or legacy/unused value not confirmed
- Loyalty or gift-note badge color treatment not confirmed
