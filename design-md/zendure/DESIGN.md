---
version: alpha
name: "Zendure"
source_url: "https://www.zendure.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Two voltages power Zendure's visual system: the sustained charge of #009f7f teal on a near-black #1c1d1d canvas that dominates hero sections and product pages, and the high-frequency pulse of #fa4500 orange reserved exclusively for purchase decisions and critical CTAs. This deliberate pairing — cool renewable-energy teal against urgent combustion orange — mirrors the hardware itself: battery systems holding energy in reserve, then releasing it on demand. Type runs Nunito Sans throughout, a rounded geometric sans that softens technical specifications without losing precision; display headlines sit at 40–56px in weight 700–800 on dark backgrounds, while body copy drops to Open Sans at 14–16px for data-dense spec sheets and comparison tables. Radius language is minimal but consistent: buttons round to `{rounded.sm}` at 8px, cards carry `{rounded.md}` at 12px, and pill badges on product categories use `{rounded.full}`. The fourth color in the hierarchy, #fbcd0a yellow-gold, appears sparingly as an energy indicator — capacity meters, star ratings, and promotional banners — borrowing the visual language of charging LEDs on the physical product. A fifth token, #a89cc8 lavender-purple, surfaces in the SolarFlow product line to differentiate solar integration products from the core portable power range. The surface language moves between #f9fafb for default page backgrounds, #edf5f5 for teal-tinted feature blocks, and deep #121212 for immersive product showcases. Spacing is generous by hardware-brand standards: section breaks at 80–96px, product grid gutters at 24px, and hero copy padded 40px from the navigation — a cadence that gives expensive hardware room to breathe before specification tables begin.

colors:
  primary: "#009f7f"
  primary-dark: "#108474"
  primary-mid: "#179e80"
  primary-light: "#c1e6e6"
  primary-tint: "#edf5f5"
  primary-active: "#108474"
  primary-disabled: "#c1e6e6"
  accent: "#fa4500"
  accent-hover: "#e03c00"
  accent-alt: "#ff4f33"
  energy-gold: "#fbcd0a"
  solar-purple: "#a89cc8"
  teal-mid: "#339999"
  on-primary: "#ffffff"
  ink: "#1c1d1d"
  ink-deep: "#121212"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#afafaf"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  hairline-faint: "#eeeeee"
  canvas: "#f9fafb"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-teal: "#edf5f5"
  surface-dark: "#1c1d1d"
  surface-deepdark: "#121212"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  spec-value:
    fontFamily: "'Nunito Sans', 'Open Sans', monospace, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  spec-label:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: -0.25px
  button-lg:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.25px
  badge:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0

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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 50px
  button-primary-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-teal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 50px
  button-teal-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.on-dark}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
    shadow: "0 2px 12px rgba(0,0,0,0.07)"
  product-card-price:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    paddingTop: "{spacing.section-lg}"
    paddingBottom: "{spacing.section-lg}"
  hero-teal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.section}"
  feature-block:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl} {spacing.lg}"
  spec-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  spec-card-value:
    textColor: "{colors.primary}"
    typography: "{typography.spec-value}"
  spec-card-label:
    textColor: "{colors.muted}"
    typography: "{typography.spec-label}"
  energy-badge:
    backgroundColor: "{colors.energy-gold}"
    textColor: "{colors.ink-deep}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-line-badge:
    backgroundColor: "{colors.primary-tint}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  solar-badge:
    backgroundColor: "{colors.solar-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  capacity-indicator:
    backgroundColor: "{colors.hairline-soft}"
    fillColor: "{colors.primary}"
    height: 8px
    rounded: "{rounded.full}"
  capacity-indicator-full:
    fillColor: "{colors.energy-gold}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  compare-table:
    headerBackground: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    rowEvenBackground: "{colors.canvas}"
    rowOddBackground: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
  app-download-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    mutedTextColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"

## Components

### Buttons
**`button-primary`** — The primary purchase trigger renders as a #fa4500 orange block on {rounded.sm} corners, 50px tall with 14px vertical padding. The high-chroma orange creates intentional contrast against both the teal brand palette and dark hero backgrounds, communicating urgency without competing with informational content. Hover darkens to #e03c00; a disabled state drops opacity to 40%. On dark hero sections, the orange CTA is the sole fully-saturated element — everything else defers to it.

**`button-teal`** — Secondary CTAs in brand-positive contexts (newsletter signup, feature exploration, learn-more flows) use the #009f7f primary teal. Shares the same {rounded.sm} geometry and 50px height as button-primary, but signals lower commercial urgency — used when the action deepens engagement rather than closes a transaction.

**`button-secondary`** — A ghost variant with a 2px teal border and transparent fill. Appears alongside button-primary in two-button CTA groups and on light card surfaces where a filled button would visually compete with product photography. The dark variant (`button-secondary-dark`) swaps the teal border for white on hero or dark sections.

### Navigation
**`nav-bar`** — On light-background pages the nav renders white with a 1px #e9e9e9 hairline bottom. On immersive hero sections it switches to `nav-bar-dark` with a #1c1d1d background that merges into the hero. Height is 64px with Nunito Sans 14px/600 links. The Zendure wordmark anchors left; product category links (Home Energy, Portable Power, Solar, Accessories) span center; cart, search, and account icons cluster right. Sub-menus expand as full-width mega panels on hover with teal section headings.

### Product Card
**`product-card`** — Cards carry a white surface with 1px #e9e9e9 border and a subtle 0 2px 12px shadow at 7% opacity, sitting on {rounded.md} 12px corners. Product image fills the top portion on a #f7f7f7 background; title renders in title-sm (18px/600); price in price-display (24px/800 ink). Capacity and wattage specs appear in a compact row of `spec-card` chips below the title — the {colors.primary} teal on the spec value numerals makes kilowatt-hour numbers immediately scannable against the card's neutral field.

### Spec Cards
**`spec-card`** — A repeating grid component for hardware specifications: battery capacity (kWh), output power (W), charging time, and weight. The numeric value renders in spec-value (28px/700) in {colors.primary} teal; the label renders in spec-label (12px/uppercase/0.5px tracking) in {colors.muted}. The {colors.surface-soft} #f7f7f7 background differentiates the spec zone from the page canvas without a border line.

### Energy Badges
**`energy-badge`** — A #fbcd0a yellow-gold chip with {rounded.xs} corners marking watt-hour ratings, "Best Seller" status, and limited-time bundle flags. The yellow borrows from the visual language of battery-status LEDs on the physical hardware, so repeat customers read it immediately as a capacity signal. Text is badge-scale (11px/700/uppercase).

**`product-line-badge`** — A teal-tinted pill ({rounded.full}) labels product categories — "Portable Power," "Home Energy," "Smart Home" — using {colors.primary-tint} background with {colors.primary} text. Appears at the top of product cards and in collection headers.

**`solar-badge`** — The #a89cc8 lavender-purple pill distinguishes SolarFlow product variants, creating a visible sub-brand signal without a separate logo system. Consistent placement top-left on product cards keeps the product family legible across the catalog grid.

### Hero
**`hero-dark`** — Full-width dark hero ({colors.surface-dark} #1c1d1d) with headline in display-xl (56px/800) in white. The teal primary acts as a highlight color on key words or subheadline accent lines rather than a background fill. Product lifestyle photography renders on the right half on desktop with a hard-cut or soft-gradient blend into the dark field; on mobile the image stacks below the headline and CTA row.

**`hero-teal`** — An alternate hero configuration for seasonal promotions fills the full background with {colors.primary}, white type, and a single `button-primary` orange CTA. Used sparingly to signal a campaign break — launch events, flash sales, regional promotions — where the entire viewport commits to brand voltage rather than product photography.

### Capacity Indicator
**`capacity-indicator`** — An 8px-tall horizontal progress bar with {rounded.full} ends used on product detail pages to visualize battery percentage or power output ceiling relative to product maximum. The track renders in #e9e9e9; fill defaults to {colors.primary} teal for standard charge states, shifting to `capacity-indicator-full` ({colors.energy-gold} #fbcd0a) in marketing contexts celebrating full capacity. A text label above carries the exact value in spec-value scale.

### Search
**`search-bar`** — A pill-shaped input ({rounded.full}, 44px height) on a {colors.surface-soft} background with a magnifying-glass icon inset left and a teal search button inset right. Appears in the nav dropdown overlay and a standalone search results page. Focus state upgrades the border from 1px {colors.hairline} to 1px {colors.primary} teal.

### Compare Table
**`compare-table`** — A sticky-column table for side-by-side product comparison, critical to Zendure's high-consideration purchase flow where customers weigh a 3.84 kWh vs 7.68 kWh system. The header row uses {colors.primary} as background with white text. Alternating rows use {colors.canvas} and {colors.surface-soft}. The first column (specification labels) is sticky-left at 160px; product columns are 200px minimum. On mobile and tablet, the table enables horizontal scroll with the label column pinned.

### Announcement Bar
**`announcement-bar`** — A 36px pinned strip above the nav in {colors.primary} teal with white caption-scale text for shipping thresholds, flash sale countdowns, and regional availability messages. On mobile, text truncates to the single highest-priority phrase with a right-aligned close control at minimum 44px tap area.

### Footer
**`footer`** — Deep {colors.ink-deep} #121212 background with a four-column link grid. Category headings render in caption (13px/500) in {colors.muted-soft} #afafaf; links in body-sm (14px/400) in white at 80% opacity. A newsletter input with teal submit button anchors the third column. The bottom bar holds social icons, a region/language selector, and legal links in caption-sm scale.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to display-md (32px); spec chip row scrolls horizontally; nav collapses to hamburger + logo + cart icon; announcement bar truncates to one phrase; footer stacks to single column |
| Tablet | 744–1128px | Two-column product grid; hero shifts to 60/40 text/image split; nav shows top-level categories with sub-menus in a slide-in drawer; spec cards wrap to 2×2 grid |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with hover mega-menus; hero at 50/50 or 40/60 text/image; spec cards in a 4-column row; compare table fully expanded |
| Wide | > 1440px | Max content width capped at 1440px centered; hero image scale increases; product grid may expand to 4 columns; outer margins widen to {spacing.section} |

### Touch Targets
- All nav links and icon buttons minimum 44×44px hit area
- Entire product card surface is tappable, not just the title or CTA
- Spec chip rows swipeable on mobile with momentum scrolling and visible overflow hint
- CTA buttons minimum 50px height across all viewports
- Announcement bar close/dismiss control minimum 44px tap area

### Collapsing Strategy
- Navigation: full mega-menu → top-level tabs only → hamburger drawer with accordion sub-menus
- Hero: side-by-side text + image → image-above-text stack on mobile, headline scales down two type steps
- Spec card grid: 4-column row → 2×2 grid → horizontal scroll strip with partial fourth card visible
- Compare table: full expanded → sticky first column + horizontal scroll on tablet/mobile
- Footer: 4-column link grid → 2-column → 1-column stacked on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No proprietary typeface detected; Nunito Sans and Open Sans are confirmed loaded but per-heading weight assignments were inferred from visual hierarchy rather than extracted CSS custom properties
- Exact button border-radius not confirmed via CSS extraction; {rounded.sm} 8px is an informed estimate based on observed visual rounding
- The #a89cc8 purple appears in the extracted palette but its assignment to the SolarFlow product line is inferred from brand context — exact usage rules unconfirmed
- Dark-mode support is unconfirmed; the dark hero (#1c1d1d) and deep footer (#121212) may be section-level surface choices rather than a full system dark theme
- Font sizes for mega-menu sub-item links not extractable from static scan
- Animation and transition timing values (hover durations, carousel intervals, scroll-reveal delays) not captured
- Exact box-shadow token values for product cards not confirmed — the 0 2px 12px rgba(0,0,0,0.07) estimate is based on observed card lift
- Social icon colors (#3b5998 Facebook, #1da1f2 Twitter) appear in the extracted palette as external brand colors, not Zendure design tokens
- Baskerville appears in the extracted font stack but its role (editorial pull-quotes, fallback only) could not be determined from extraction alone
