---
version: alpha
name: "Greats"
source_url: "https://greats.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The electric violet (#6849e3) that pulses through Greats' primary actions sits in deliberate tension with the near-black (#141415) it presses against — a pairing that reads more like a downtown gallery than a sneaker boutique. Greats built its reputation on the Royale, a direct-to-consumer white leather Oxford that arrived before the DTC playbook was a cliché, and the digital environment mirrors that origin story: a stark, minimal shell where photography does the selling and the brand's purple surfaces only where it must — CTAs, active size cells, focus rings. Tenor Sans carries the editorial register, pulling double duty as a display face with enough geometric restraint to keep the site from drifting into fashion-magazine territory; Helvetica Neue handles the workday copy, body text, and nav labels, its studied neutrality letting product imagery breathe. The palette runs lean — two near-blacks (#141415, #121212) that behave as canvas-dark and ink depending on context, a pair of near-identical grays (#dedede, #d7d7d7) managing hairlines and surface softs, and the white canvas that any leather-sneaker brand's photography demands. Radius is used sparingly: buttons carry a subtle 4px curve rather than a pill, product cards read closer to square than round, and the overall geometry stays in the rectilinear tradition of NYC streetwear rather than the soft arcs of athleisure. Size selectors — the critical interaction for footwear — render as tight bordered grids where the active state floods the cell with violet and flips the label white, one color doing the work of communicating availability, selection, and brand identity in a single toggle. The checkout drawer closes the loop in the same dark-to-light rhythm: near-black header bar yielding to a white panel, violet CTA anchoring the bottom.

colors:
  primary: "#6849e3"
  primary-active: "#5338c2"
  primary-disabled: "#c4b8f5"
  ink: "#141415"
  body: "#121212"
  muted: "#6b6b6b"
  hairline: "#dedede"
  hairline-soft: "#d7d7d7"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  canvas-dark: "#141415"
  error: "#c0392b"

typography:
  display-xl:
    fontFamily: "'Tenor Sans', 'Helvetica Neue', sans-serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Tenor Sans', 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Tenor Sans', 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  label-upper:
    fontFamily: "'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price:
    fontFamily: "'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.75px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.75px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
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
  section: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
    cartIconColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageRatio: "1 / 1"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    padding: "{spacing.sm}"
    gap: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 600px
    padding: "{spacing.xxl} {spacing.lg}"
  size-selector:
    gridColumns: 5
    cellSize: 48px
    cellRounded: "{rounded.sm}"
    defaultBorder: "1px solid {colors.hairline}"
    defaultBackground: "{colors.canvas}"
    defaultTextColor: "{colors.ink}"
    defaultTypography: "{typography.body-sm}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
    disabledBackground: "{colors.surface-soft}"
    disabledTextColor: "{colors.muted}"
    disabledDecoration: line-through
    gap: "{spacing.xs}"
  color-swatch:
    size: 28px
    rounded: "{rounded.full}"
    selectedRingColor: "{colors.ink}"
    selectedRingOffset: 2px
    selectedRingWidth: 2px
    gap: "{spacing.sm}"
  product-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  pdp-image-gallery:
    thumbnailSize: 64px
    thumbnailRounded: "{rounded.none}"
    thumbnailBorder: "1px solid {colors.hairline}"
    thumbnailActiveBorder: "1px solid {colors.ink}"
    mainImageRatio: "1 / 1"
    backgroundColor: "{colors.surface-soft}"
    gap: "{spacing.sm}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    headerTypography: "{typography.display-sm}"
    itemNameTypography: "{typography.title-sm}"
    itemPriceTypography: "{typography.price}"
    dividerColor: "{colors.hairline}"
    padding: "{spacing.lg}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    resultNameTypography: "{typography.title-sm}"
    resultPriceTypography: "{typography.body-sm}"
    backdropColor: "rgba(20, 20, 21, 0.6)"
    inputHeight: 48px
    inputBorder: "1px solid {colors.hairline}"
    inputRounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-upper}"
    dividerColor: "rgba(255,255,255,0.12)"
    padding: "{spacing.xxl} {spacing.lg}"

## Components

### Buttons

**`button-primary`** — Greats' violet (#6849e3) fill with white all-caps type at 14px, 0.75px letter-spaced, on a 48px-tall container with a 4px radius (`{rounded.sm}`). The radius is deliberate restraint — just enough curve to soften, not enough to signal casual. Hover darkens to #5338c2; disabled washes to #c4b8f5, which goes visually quiet without disappearing entirely.

**`button-secondary`** — White fill, 1px `{colors.ink}` border, identical height and radius to primary. Appears beside the primary on PDPs for secondary actions like wishlist adds. On hover, the background shifts to `{colors.surface-soft}`, providing feedback without color drama.

**`button-ghost`** — Text-only with underline, used for low-stakes actions — "View All," drawer dismissals, secondary navigation links — where ink commitment would add too much visual weight to the page.

### Navigation

**`nav-bar`** — 64px, white, separated from page content by a 1px `{colors.hairline}` bottom border. The Greats wordmark sits left in near-black; nav links run in 14px Helvetica Neue regular at even horizontal spacing. Cart and search icons anchor the right. On mobile the entire link set collapses behind a hamburger; the drawer inverts to near-black with white type.

### Product Cards

**`product-card`** — Strictly rectilinear: no border radius, square image crop on a `{colors.surface-soft}` tile. Product name in `{typography.title-sm}` above price in `{typography.price}`, with color and size range in `{typography.caption}` below. On hover, a quick-add affordance or alternate colorway image may surface — the grid reads flat at rest, interactive on engagement.

### Size Selector

**`size-selector`** — A 5-column grid of 48×48px cells, each bordered in `{colors.hairline}` at rest. Tapping or clicking a size floods the cell with `{colors.primary}` and flips the numeral to `{colors.on-primary}` — the only moment the violet appears mid-interaction outside of CTAs. Sold-out sizes retain their cell geometry but render in `{colors.surface-soft}` with a strikethrough numeral, keeping the grid intact rather than punching holes.

### Hero Banner

**`hero-banner`** — Near-black canvas (`{colors.canvas-dark}`) that ensures white leather product photography pops cleanly. Headline in Tenor Sans at 56px/400 weight — the font's elegance handles the display scale without needing heavier weight. Subhead in `{typography.body-md}` in `{colors.on-dark}`. The CTA renders as `button-primary`, violet against dark, maximum contrast ratio.

### Badges

**`product-badge`** — Hard-cornered (`{rounded.none}`) ink-black chip with all-caps white label, pinned to the upper-left of product imagery. The hard corner reads deliberate in a design system that uses `{rounded.sm}` elsewhere — the badge is a stamp, not a tag. Sale variant swaps fill to `{colors.primary}` for immediate hierarchy signaling.

### PDP Image Gallery

**`pdp-image-gallery`** — Vertical thumbnail strip left of the main image on desktop; each thumbnail is a 64px square with a hairline border at rest and an ink border when active. Main image fills a square viewport in `{colors.surface-soft}`. On mobile, thumbnails collapse into a horizontally swipeable carousel beneath the main view.

### Cart Drawer

**`cart-drawer`** — 400px right-aligned panel, white background, with line items separated by `{colors.hairline}` dividers. Header in Tenor Sans 24px (`{typography.display-sm}`) gives the drawer a branded moment inside a functional shell. Checkout CTA spans the full panel width as `button-primary`, bottom-anchored.

### Search Overlay

**`search-overlay`** — A full-width input drops from beneath the nav bar, backed by a 60% near-black scrim over page content. Results appear as product rows with thumbnail, name, and price — no editorial decoration, strict utility. Input field uses the same height and border treatment as `text-input`.

### Footer

**`footer`** — Inverted palette: `{colors.canvas-dark}` background with `{colors.on-dark}` links and all-caps `{typography.label-upper}` section headings. Mirrors the hero's dark register, bookending the page in the brand's secondary ground color. Link columns stack 4-across on desktop, accordion on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with full-height dark drawer; size selector at 4 columns; hero min-height 400px; cart drawer expands to full viewport width; footer collapses to accordion columns |
| Tablet | 744–1128px | Two-column product grid; primary nav links visible; hero may split 50/50 image-text; cart drawer stays at 400px |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav with hover dropdowns; PDP splits to gallery-left / details-right; size selector 5 columns |
| Wide | > 1440px | Max content width ~1440px, centered with canvas gutters; grid stays at 4 columns; hero constrains headline width to ~60% |

### Touch Targets

- Size-selector cells are 48×48px minimum — no reduction on mobile
- Nav icons (cart, search, hamburger) padded to 44×44px tap area
- Color swatches expand from 28px to 36px effective touch area via invisible padding on mobile
- Primary CTA buttons run full-width (100%) below 744px breakpoint

### Collapsing Strategy

- Primary nav collapses to hamburger at < 744px; links stack vertically in a full-height near-black overlay drawer
- Product filters (if present) slide in from the left as a drawer on mobile, appear as a fixed left-rail sidebar on desktop
- PDP image gallery converts from a vertical thumbnail strip to a swipe carousel on mobile
- Footer link columns stack to a single column with accordion-expand behavior on mobile
- Hero text block moves from overlay-on-image to stacked text-above-image on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font files confirmed — Tenor Sans likely loads from Google Fonts; exact weights served (400 only, or 400/700) not determinable from extraction
- Helvetica Neue is a paid system font on non-Apple devices; web fallback stack behavior on Windows/Android not confirmed
- #007aff present in extraction but is iOS system blue (autofill, form controls) — not a Greats brand color and excluded from palette
- Exact button border-radius values not confirmed; `{rounded.sm}` (4px) inferred from aesthetic category conventions
- Hover/active state treatments for nav links not extractable; underline or subtle opacity shift assumed
- No motion/transition tokens recoverable — 200ms ease assumed for interactive states
- Sale price color treatment (red, primary violet, or muted) not confirmed
- Dark-mode variant unknown; site appears to be light-mode-only with selective dark sections (hero, footer)
- Precise grid gutter widths and max content column counts not extracted
