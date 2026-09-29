---
version: alpha
name: "Shashi"
source_url: "https://www.shopshashi.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The spaced lettermark — S H A S H I, each glyph separated by nearly a full em of silence — announces this costume-jewelry brand not through loudness but through geometric ceremony. Every page grounds itself in near-charcoal (#1d1d1d), a deliberate darkness that makes the warm copper and terra cotta product tones read almost as incandescent: the extracted palette describes a complete warm-metal spectrum — #d2815f copper, #c35121 burnt rust, #94553a deep bronze, and a soft blush (#f2d9cf) that introduces femininity without defaulting to predictable dusty rose. The voltage surprise lives in a second register: an electric cobalt (#3d5aff, #0024f0) that surfaces on CTAs and interactive states, cutting a sharp chromatic break against the thermal warmth of the jewelry palette. This oscillation — burnished vs. galvanic, earth-warm vs. spark-cold — is the brand's defining temperature. Pill-shaped filter tags ({rounded.full}) handle collection navigation while product cards and buttons stay strictly square-cornered ({rounded.none}), keeping the precision vocabulary consistent with the jewelry's own hard-set edges and bezel settings. Wide letter-spacing (0.15–0.5em) applied from the logo mark down through section headers, nav links, and button labels gives the interface its fashion pacing — each word spaced for scroll consumption rather than reading speed. Tangerine (#ff763d) and ember (#f04600) appear as flash-heat accents for urgency signals: transient and unmissable against the neutral field. A 36px promo ticker in near-black runs above the navigation, compressing promotional copy into a thin band that never competes with the editorial photography below.

colors:
  primary: "#3d5aff"
  primary-active: "#0024f0"
  primary-disabled: "#a6b4ff"
  ink: "#1d1d1d"
  body: "#4d4d4d"
  muted: "#848484"
  hairline: "#dedede"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  dark-canvas: "#1d1d1d"
  dark-surface: "#0d0d0d"
  on-dark: "#f2f2f2"
  copper: "#d2815f"
  copper-deep: "#c35121"
  copper-dark: "#94553a"
  blush: "#f2d9cf"
  tangerine: "#ff763d"
  ember: "#f04600"
  charcoal: "#424242"

typography:
  logo-display:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.5em
    textTransform: uppercase
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: 0.3em
    textTransform: uppercase
  display-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.25em
    textTransform: uppercase
  display-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.2em
    textTransform: uppercase
  title-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.12em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.15em
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.02em
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.02em
  price-display:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.04em
  caption:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.08em
  button-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.15em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.15em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.12em
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
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-secondary-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 0
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
    logoTypography: "{typography.logo-display}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.logo-display}"
    height: 60px
  promo-ticker:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.ink}"
    gap: "{spacing.sm}"
  product-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  product-badge-sale:
    backgroundColor: "{colors.ember}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  collection-tag:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderActive: "1px solid {colors.ink}"
    textColorActive: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  hero-banner:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.title-md}"
    padding: "{spacing.section} {spacing.xl}"
  editorial-block:
    backgroundColor: "{colors.blush}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  quick-add-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    backgroundSelected: "{colors.ink}"
    textColorSelected: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Solid electric cobalt (#3d5aff) fill on a zero-radius rectangle, uppercase label at 13px with 0.15em tracking ({typography.button-md}). Active state drops to the deeper cobalt (#0024f0); disabled washes to a pale periwinkle. The hard corner is deliberate — it rhymes with the bezel-set geometry of the jewelry and keeps the CTA in the same angular vocabulary as the product itself.

**`button-secondary`** and **`button-secondary-on-dark`** — Transparent fill with a 1px solid border, same dimensions and type as primary. The dark variant swaps ink borders to on-dark (#f2f2f2) for placement directly over hero and editorial modules on charcoal backgrounds. Used frequently on the homepage where photography and dark sections share the CTA row.

**`button-ghost`** — No background, no border, zero padding. Carries the uppercase button type scale but behaves as a text-level affordance. Used for "View all" links in section headers and "Show more" expanders inside filter panels.

### Text Input
**`text-input`** — Square-cornered, 48px tall, 1px hairline border at rest transitioning to 1px ink border on focus. Height deliberately matches button height so newsletter and search form rows stay optically level. No floating label animation — a static uppercase label (title-sm) sits above the field, consistent with the brand's aversion to motion-driven hierarchy.

### Navigation
**`nav-bar`** — 60px tall, white canvas, 1px hairline bottom border. The wordmark renders in logo-display ({typography.logo-display}, 0.5em letter-spacing) to reproduce the "S H A S H I" spaced-character treatment that reads as the brand's primary visual signature. Top-level nav links use nav-link type (0.12em tracking, uppercase, 13px). A `promo-ticker` strip (36px, ink background) sits above the entire nav frame, scrolling promotional text in caption type — this band is always present on desktop and condenses on mobile. `nav-bar-dark` activates on dark-themed campaign pages with identical proportions.

### Product Card
**`product-card`** — No border-radius, 3:4 portrait crop, white canvas beneath. Title renders in title-sm (uppercase, 0.15em tracking) and price in price-display (15px medium) separated by {spacing.sm}. On hover, a quick-add overlay slides in from the image bottom edge containing a `button-primary` spanning the card width. `product-badge` (ink fill, "NEW", "SOLD OUT") and `product-badge-sale` (ember #f04600 fill) float as absolute overlays at image top-left.

### Collection Filter Tags
**`collection-tag`** — Pill-shaped ({rounded.full}) with hairline border at rest; on selection the border switches to ink weight and the text color activates. Uppercase 13px label. The tag row scrolls horizontally at mobile breakpoint below the collection hero. Allows multi-select across metal finish, stone type, and product category dimensions.

### Hero Banner
**`hero-banner`** — Full-bleed dark module on dark-canvas (#1d1d1d). Display type at {typography.display-xl} (48px, 0.3em tracking, weight 300) with a subtitle in title-md and a `button-secondary-on-dark` CTA below. On desktop the image fills the right 55% and copy aligns left in the remaining column; on mobile the image appears above the copy block at full width.

### Editorial Block
**`editorial-block`** — Blush (#f2d9cf) background section that breaks the product grid's neutral rhythm with warmth. Title in display-md (0.25em tracking), body in body-md. Section-level vertical padding ({spacing.section}). Used for campaign stories, material callouts ("Freshwater Pearl", "14k Gold Vermeil"), and brand origin copy.

### Quick-Add Drawer
**`quick-add-drawer`** — Bottom sheet on mobile (slides up from viewport edge), inline side panel on desktop. White canvas, no border-radius, top hairline border on mobile. Contains size-selector tiles in a horizontal row, a quantity stepper, and a `button-primary` spanning full width. Size tiles are 40×40px square ({size-selector}) with an ink fill on selected state.

### Footer
**`footer`** — Near-black (#0d0d0d) background. Four columns on desktop (Shop, About, Help, Newsletter) collapsing to a stacked single column on mobile with the email capture moved to the footer top. Section headings in title-sm (uppercase tracked); links in body-sm. Social icon row centered on mobile, left-aligned on desktop. Legal copy and copyright in caption.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo-display wordmark; hero image above copy block; collection tags scroll horizontally; quick-add becomes bottom sheet |
| Tablet | 744–1128px | Two-column product grid; nav shows primary items only, secondary links in drawer; hero switches to 50/50 split layout |
| Desktop | 1128–1440px | Three-to-four-column product grid; full nav with dropdown panels; hero image occupies right 55%; editorial block goes two-column |
| Wide | > 1440px | Grid holds at four columns with wider gutters; content max-width ~1400px centered; hero gains additional left-margin breathing room |

### Touch Targets
- All tappable elements minimum 44×44px effective area on mobile
- `size-selector` tiles are 40×40px visual — pair with 4px margin to reach 48px effective tap target
- `collection-tag` pills minimum 36px height on mobile with 8px horizontal padding
- Cart, account, and search icons in nav bar padded to 44×44px tap zone regardless of visual icon size
- `promo-ticker` strip excluded from touch interaction; no tap targets inside it

### Collapsing Strategy
- Hamburger activates at < 744px: primary nav, collection dropdowns, and account links collapse into a full-screen overlay drawer sliding from the left
- Hero image moves above text block on mobile (image-first so product photography leads)
- Footer four-column layout stacks to single column; newsletter capture row moves to footer top
- `quick-add-drawer` transitions from inline side panel (desktop) to bottom sheet (mobile)
- `editorial-block` goes single-column on mobile with reduced vertical padding ({spacing.xxl})
- `promo-ticker` condenses to a single static line on mobile, disabling scroll animation

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font families were extracted from the live site — the brand likely loads custom or third-party typefaces via JS or a font CDN. All typography tokens use system Helvetica Neue as a placeholder; actual brand fonts should replace these once identified from the live site or brand kit.
- Primary CTA color assignment is inferred: electric cobalt (#3d5aff, #0024f0) is modeled as the action color based on its distinctiveness against both light and dark surfaces; warm copper (#d2815f) could be the intended primary in a different reading of the hierarchy.
- Dark vs. light canvas balance is uncertain — meta theme-color (#1d1d1d) and the density of near-black hex values suggest significant dark-section usage, but the product grid may be predominantly white canvas.
- Border-radius values for buttons are assumed square ({rounded.none}) based on fashion-jewelry conventions and the spaced-letterform brand register; actual radius may be different.
- Tangerine (#ff763d) and ember (#f04600) use context is unclear — modeled as urgency and sale accents but may correspond to a specific collection colorway or seasonal campaign.
- No icon set, illustration style, hover motion timing, or animation easing data could be extracted.
- `price-display` treatment for sale prices (strikethrough original + colored new price) is unverified; the sale color token is assumed to follow `colors.ember` but may use `colors.primary`.
