---
version: alpha
name: "Desenio"
source_url: "https://desenio.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Desenio proves that a poster retailer's interface competes directly with its own inventory — every pixel spent on nav chrome is a pixel stolen from art. The result is one of the sparest storefronts in Nordic e-commerce: a gallery-white (#ffffff) field, hairlines at #e5e5e5, and body copy so understated it barely registers above the prints. Category navigation is stripped to a single horizontal strip; the mega-menu drops with the opacity of a museum plaque rather than a commerce takeover. Art fills the grid at a consistent image-to-frame ratio, and the UI's only real visual claim is the frame selector — a ring of lacquered swatches (black, white, natural, walnut) that lets shoppers configure their print into the physical object it will become. CTAs run in near-black (#1a1a1a) with all-caps tracked letter-spacing, a typographic choice that reads as gallery label rather than shop button. Uppercase is Desenio's tone-of-voice carrier: category names, size pickers, and badge text all run at 1–1.5px tracking with tight caps, holding editorial formality without weight. The frame-selector swatches, size radios, and paper-type toggles form a product configurator that is the functional centrepiece of every PDP — minimal chrome, maximum decision support. The room-visualizer mockup (placing your print in a photographed interior) appears as a secondary tab, deferring to the flat product scan as the canonical image. Sale badges come in a discreet pill at {rounded.full}, claret-tinted (#c0392b) against white, so they flag without screaming. Spacing is generous — the grid breathes at {spacing.lg} gutters on desktop — sustaining the gallery register throughout. Responsive layout compresses to a two-column grid on mobile, collapsing the nav into a hamburger sheet that slides in from the left; the frame and size selectors stack vertically below the hero image rather than sitting beside it.

colors:
  primary: "#1a1a1a"
  primary-active: "#333333"
  primary-disabled: "#b0b0b0"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#767676"
  hairline: "#e5e5e5"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f6f4"
  surface-card: "#ffffff"
  surface-warm: "#faf9f7"
  on-primary: "#ffffff"
  sale: "#c0392b"
  sale-soft: "#fdf0ef"
  badge-new: "#1a1a1a"
  badge-new-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-uppercase:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  price-original:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
    textDecoration: line-through
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.3px
  category-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: none
    rounded: "{rounded.none}"
    padding: 8px 0px
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.none}"
    hoverImageScale: 1.03
    hoverTransition: 300ms ease
    gap: "{spacing.sm}"
  product-grid:
    columns: 4
    gap: "{spacing.lg}"
    backgroundColor: "{colors.canvas}"
  hero-editorial:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
    layout: split-image-text
  badge-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.full}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.badge-new-text}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.full}"
    padding: 3px 8px
  frame-selector:
    swatchSize: 24px
    swatchBorderSelected: "2px solid {colors.ink}"
    swatchBorderDefault: "1px solid {colors.hairline}"
    swatchBorderRadius: "{rounded.full}"
    labelTypography: "{typography.caption-uppercase}"
    gap: "{spacing.sm}"
  size-selector:
    optionStyle: radio-pill
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackground: "{colors.canvas}"
    inactiveTextColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: none
    rounded: "{rounded.none}"
    padding: 10px 16px
    height: 44px
    iconColor: "{colors.muted}"
  category-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.category-label}"
    border: "1px solid {colors.hairline}"
    borderHover: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 6px 14px
  room-visualizer-tab:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-uppercase}"
    borderBottom: "2px solid transparent"
    activeTextColor: "{colors.ink}"
    activeBorderBottom: "2px solid {colors.ink}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.ink}"
    headingTypography: "{typography.caption-uppercase}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons
**`button-primary`** — Flat rectangle at zero radius, near-black (#1a1a1a) fill, white type set in 13px/600 uppercase with 1.2px tracking. Active state steps fill to #333333; disabled drops to #b0b0b0 with white label unchanged. Height locks at 48px, horizontal padding 32px. The hard geometry and tracked caps read as gallery edition rather than commerce-round, anchoring the purchase CTA in editorial register.

**`button-secondary`** — White fill, 1px #1a1a1a border, same uppercase type. On hover, fill inverts to black / white text. Appears beside the primary CTA on PDPs ("Add to wishlist" adjacent to "Add to cart") and in modal confirmation flows.

**`button-ghost`** — Transparent, no border, underlined body text at button-sm scale. Used for "View all" links in editorial carousels, room-visualizer toggle text, and nav utility links that should read as inline prose rather than controls.

### Text Input
**`text-input`** — Zero-radius rectangle, 1px #e5e5e5 border that steps sharply to 1px #1a1a1a on focus with no box-shadow. Placeholder in #767676, active text in #1a1a1a. Height 48px with 16px horizontal padding. Mirrors the flat button geometry — no softening anywhere in the form language.

### Navigation
**`nav-bar`** — 64px tall, white canvas, 1px hairline bottom border. Desenio wordmark left-anchored in clean sans; main category links centered in 14px/400 with light tracking; utility icons (search, wishlist, cart) right-anchored. Cart carries a numeric badge overlay. On hover, a full-width mega-menu slides below the hairline — 3–4 column editorial grid of sub-category tiles with art imagery and category-label headings. On mobile, collapses to hamburger left / logo center / cart right, with the hamburger sheet sliding from the left edge.

### Product Card
**`product-card`** — Zero-radius image container at 3:4 portrait aspect ratio (matching actual poster proportions). Title in 13px/400 sits below; price in 18px/400. Sale price renders in #c0392b alongside a strikethrough original. On hover, image scales 1.03× over 300ms ease — enough to confirm interactivity without disrupting the grid rhythm. Badge pills overlay image top-left corner.

### Product Grid
**`product-grid`** — 4-column on desktop with 24px gutters, no card borders, white canvas ground. The repeating portrait-frame grid is the dominant visual rhythm of the site; gutter width is calibrated to read as white mat rather than layout gap.

### Hero
**`hero-editorial`** — Split layout: editorial headline at 48px/300 weight left, curated art selection right. Background in warm off-white (#faf9f7). Vertical padding at section scale (64px). The featherlight display weight defers visual authority to the imagery.

### Badges
**`badge-sale`** — Claret (#c0392b) pill at full radius, white 11px/600 uppercase at 1.5px tracking. Overlays product card top-left. **`badge-new`** — Same geometry, black fill. Both kept small to avoid competing with the print image; they signal without asserting.

### Frame Selector
**`frame-selector`** — Row of 24px circular swatches representing finish options (black lacquer, white, natural wood, dark walnut). Selected: 2px solid #1a1a1a ring. Default: 1px #e5e5e5 ring. Label in 11px tracked uppercase above the row names the active selection. This is the primary tactile interaction on the PDP — the moment the poster becomes a physical object.

### Size Selector
**`size-selector`** — Flat rectangular radio pills at zero radius. Active: #1a1a1a fill / white text. Inactive: white fill / #1a1a1a text / 1px #e5e5e5 border. Format labels (30×40, 50×70, 70×100 cm) in 13px/400. Flat pill language matches primary button geometry.

### Search Bar
**`search-bar`** — Appears in mega-menu and full-screen search overlay. No border, #f7f6f4 surface background, 44px tall. Search icon left; clear icon appears right when populated. Type in body-md scale. Zero radius maintains flat language consistency.

### Category Chips
**`category-chip`** — Flat rectangle (zero radius), 1px #e5e5e5 border, 11px uppercase tracked at 1.5px. Used in filter strips on collection pages. Hover steps border to #1a1a1a. Active inverts to black fill / white text.

### Room Visualizer Tab
**`room-visualizer-tab`** — Tab switcher pair (PRODUCT IMAGE / ROOM VIEW) in 11px tracked uppercase. Inactive: #767676 text, no underline. Active: #1a1a1a text, 2px solid bottom border. Thin and space-efficient — does not interrupt vertical scroll momentum on the PDP.

### Footer
**`footer`** — Warm soft surface (#f7f6f4), 1px top border. Column headers in 11px tracked uppercase. Body links in 13px/400. Social icon strip and newsletter input using the standard text-input spec. Padding 48px vertical.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | 2-column product grid; nav collapses to hamburger sheet sliding from left; frame and size selectors stack below hero image; hero becomes single-column stacked |
| Tablet | 744–1128px | 3-column product grid; mega-menu accessible; PDP shifts to image-top / configurator-bottom |
| Desktop | 1128–1440px | 4-column product grid; full horizontal nav with mega-menu drop; PDP is image-left / configurator-right split |
| Wide | > 1440px | Grid constrained to ~1440px max-width; side margins expand; product grid holds at 4 columns with proportionally larger gutters |

### Touch Targets
- All buttons minimum 48px height
- Frame swatches 24px visual diameter, 44px tap target
- Size selector pills minimum 44px height on mobile
- Nav hamburger icon minimum 44×44px tap zone
- Wishlist and cart icons in nav: 44×44px touch area

### Collapsing Strategy
- Primary nav collapses to hamburger sheet at < 744px; sheet overlays full screen with 16px padding, main categories as top-level rows
- Mega-menu sub-categories become accordion rows inside the hamburger sheet
- Product grid steps 4 → 3 → 2 columns at Desktop → Tablet → Mobile breakpoints
- PDP frame, size, and paper-type configurator stacks vertically below main image on mobile
- Room visualizer tab pair becomes full-width tap targets on mobile
- Footer 4-column layout stacks to single column on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Extraction blocked by Vercel security checkpoint**: all extracted colors (#0070f3, #3291ff) and font stacks belong to Vercel's own checkpoint UI, not Desenio. This entire spec is built from brand knowledge, not live extraction.
- **Exact brand typeface unconfirmed**: Desenio may use a licensed geometric sans or a custom cut not identifiable without live site access; Helvetica Neue is used here as the closest documented match.
- **Secondary accent color unconfirmed**: a warm sand or muted sage may appear in seasonal editorial campaigns but could not be verified.
- **Precise border-radius values unconfirmed**: buttons and selectors appear flat (zero radius) from brand imagery, but actual pixel values were not extractable.
- **Animation timing curves**: hover scale on product cards and mega-menu slide duration are estimated from visual convention.
- **Paper-type selector**: a matte/satin/premium paper toggle reportedly exists on PDPs; its exact visual treatment is unconfirmed.
- **Wordmark font**: the Desenio logotype appears to use a custom or licensed condensed sans — cannot be confirmed without live access.
- **Promotional banner**: a top-of-page offer strip (free shipping threshold, discount codes) likely exists but styling details are unknown.
