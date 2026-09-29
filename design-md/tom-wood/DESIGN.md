---
version: alpha
name: "Tom Wood"
source_url: "https://www.tomwoodproject.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Hammered silver catches light differently than polished gold — and Tom Wood has built an entire visual language around that principle of deliberate surface. The Norwegian jewelry house runs on two extracted tones: near-void ink (#121212) and cool-silver mist (#dedede), a palette so compressed it reads more like a metallurgical study than a brand color system. Primary actions fire in #121212 — the darkest button on the whitest canvas — and the {rounded.none} geometry that runs through every UI edge echoes the brand's preference for hard-set sterling forms over softened consumer shapes. Typography is not extractable from the live site (tokens load via JavaScript), so the spec below adopts a clean grotesque stack as the closest documented analogue to Tom Wood's editorial cadence; the actual production typeface should be verified against the live stylesheet. Navigation is sparse and hierarchical: collection names set in small-caps letter-spacing, no badge clutter, no promotional interruptions. Product cards suppress ornament entirely — image, name, price, and nothing else — treating each object as the specimen it is. The checkout and account flows share the same monochromatic restraint: no accent color relieves the tension, no hover gradient softens the edge. At mobile widths the single-column grid tightens to near-full-bleed imagery, keeping the jewelry large and the chrome invisible. The overall spatial logic favors generous vertical rhythm ({spacing.section} gaps between editorial rows) against tight horizontal gutters, a proportion that mirrors how the pieces themselves are photographed: close, lit from one side, against a neutral ground.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#999999"
  ink: "#121212"
  body: "#2d2d2d"
  muted: "#666666"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  silver-mid: "#dedede"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.04em
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.03em
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.02em
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1em
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01em
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.01em
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  price-display:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.03em
  label-micro:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1em
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
    border: "1px solid {colors.ink}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    textDecoration: underline
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.xl}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.lg} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    nameTypography: "{typography.body-md}"
    priceTypography: "{typography.price-display}"
    gap: "{spacing.sm}"
    hoverBehavior: second-image-crossfade
  product-card-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-micro}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  hero-full-bleed:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    imagePosition: center
    overlayOpacity: 0.2
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.display-sm}"
    ctaComponent: button-primary
    minHeight: 90vh
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
    height: 48px
  filter-tag-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-micro}"
    rounded: "{rounded.none}"
    padding: "6px 12px"
  filter-tag-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label-micro}"
    rounded: "{rounded.none}"
    padding: "6px 12px"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: "12px 16px"
    height: 48px
    focusBorder: "1px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.ink}"
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 48px
    selectedBorder: "1px solid {colors.ink}"
    soldOutStyle: strikethrough
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 48px
    width: 120px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    activeColor: "{colors.ink}"
  editorial-strip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaComponent: button-secondary
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.silver-mid}"
    headingTypography: "{typography.title-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Full-width or fixed 48px-height blocks set in small-caps uppercase with 0.12em letter-spacing, background #121212, no border radius. The hover state darkens to absolute #000000; disabled collapses to #999999 with identical geometry. All corners are square (`{rounded.none}`), a deliberate choice that refuses the softness of consumer pill buttons.

**`button-secondary`** — Canvas white fill with a 1px #121212 border, same uppercase typographic cadence as primary. Used on product pages alongside add-to-cart to surface secondary actions (add to wishlist, share) without competing brightness.

**`button-text-link`** — Transparent background, body-weight underline, no uppercase treatment. Reserved for inline editorial links within long-form copy, size guide modals, and return policy references.

### Navigation

**`nav-bar`** — 64px fixed bar on a white canvas, separated from content by a 1px #dedede hairline. Links are set in `{typography.nav-link}` — 12px uppercase at 0.12em tracking, no weight boost. Logo sits centered or left-aligned. A hamburger appears at mobile widths; no mega-menu flyout at desktop — category lists drop in a clean flat panel below the bar using `{typography.nav-link}` with generous padding.

**`nav-dropdown`** — Flat white panel anchored below the hairline, spanning full viewport width. Column layout with category headings in `{typography.title-md}` and subcategories in `{typography.nav-link}`. No imagery in the dropdown — text only.

### Product Card

**`product-card`** — Hard-edged rectangle, 4:5 aspect ratio image, zero radius. On hover a second hero image crossfades in (no zoom, no overlay). Below the image: product name in `{typography.body-md}`, price in `{typography.price-display}`, both left-aligned with `{spacing.sm}` gap. Color variants shown as small solid swatches beneath the price. No "Add to Cart" visible on the card — conversion happens on the PDP.

**`product-card-badge`** — Flush black rectangle (`{rounded.none}`) positioned top-left of the image, content "NEW" or "SOLD OUT" in `{typography.label-micro}`. No color variation in the badge; the system uses ink-on-black for all states.

### Filters and Size Selector

**`filter-bar`** — Sticky strip below the collection header, height 48px, with horizontal scroll at mobile. Active filters fill to `{colors.ink}` with white label; inactive tags carry a `{colors.hairline}` border. Filter count shown as a parenthetical in `{typography.caption}`.

**`size-selector`** — Square tiles in a horizontal row, each 48px tall, `{rounded.none}`. Selected tile gets a full 1px #121212 border upgrade from the hairline default. Sold-out sizes render with a diagonal strikethrough line over the tile rather than being removed.

### Editorial Strip

**`editorial-strip`** — Full-bleed #121212 section used to break grid monotony between collection rows. White headline in `{typography.display-md}`, body copy in `{typography.body-md}`, and a `button-secondary` (white border, white text on dark) as CTA. Padding follows `{spacing.section}` vertically.

### Footer

**`footer`** — Dark #121212 background with column layout: newsletter signup left, link columns center, social and legal right. Link labels in `{colors.silver-mid}` (#dedede) distinguish them from body copy. Headings use `{typography.title-sm}` uppercase; links use `{typography.body-sm}`.

### Hero

**`hero-full-bleed`** — Viewport-height (90vh) image with a 20% dark scrim. Title in `{typography.display-xl}` (light weight, wide tracking), subtitle in `{typography.display-sm}`. CTA uses `button-primary` in white-on-black variant. No carousel — single static or slow-loop video.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, full-bleed images, hamburger nav, filter drawer slides from bottom, hero shrinks to 70vh |
| Tablet | 744–1128px | Two-column product grid, nav remains horizontal with condensed labels, filter bar scrolls horizontally |
| Desktop | 1128–1440px | Three-column product grid, full nav dropdown, filter sidebar option alongside filter bar |
| Wide | > 1440px | Four-column grid, max-width container centered at 1440px, hero image extends edge-to-edge behind centered text block |

### Touch Targets

- All buttons and interactive tiles maintain minimum 48px height
- Size selector tiles are minimum 44×44px even at smallest ring sizes
- Nav links spaced at minimum 44px tap height in the mobile drawer
- Swatch targets padded to 32×32px minimum with 4px gap between

### Collapsing Strategy

- Desktop filter sidebar collapses to a bottom-sheet drawer on mobile
- Nav dropdown collapses to a full-screen slide-in panel on mobile with back-navigation
- Editorial strips stack vertically; image appears above copy on mobile (reversed from desktop)
- Collection description truncates to three lines with "Read more" expansion on mobile
- Footer columns stack to single column on mobile; newsletter form moves to top of footer

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No fonts extracted** — the live site loads typography via JavaScript, preventing static extraction. The spec uses a Helvetica Neue grotesque stack as a structural proxy; the actual brand typeface (possibly a licensed geometric or custom sans) must be verified by inspecting the live network requests or Shopify theme assets.
- **Only two hex values extracted** (#dedede, #121212) — the full palette including any accent color, error states, or promotional tones could not be confirmed. All intermediate grays (#2d2d2d, #666666, #f4f4f4, #ffffff) are inferred from standard monochromatic e-commerce conventions, not scraped data.
- **No meta theme-color** — iOS Safari tab tint and PWA manifest color are undefined; likely defaults to white.
- **Accent or campaign color unknown** — seasonal collections may introduce a limited accent (warm gold, oxidized copper) not visible in the base site palette. Verify against current editorial campaign assets.
- **Exact letter-spacing values** — without extracted CSS, tracking values for nav and button type are approximated from visual inspection of brand reference imagery rather than computed stylesheet values.
- **Icon system not documented** — Tom Wood may use a custom SVG glyph set; no icon font or sprite was detectable from the extracted hints.
