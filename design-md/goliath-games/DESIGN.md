---
version: alpha
name: "Goliath Games"
source_url: "https://www.goliathgames.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Compressed military lettering and a board-game color riot coexist under one roof — Goliath runs exclusively on D-DIN, an industrial sans-serif that originated in German engineering manuals and arrived at game-night headlines via its legibility at distance. D-DIN Condensed handles the loudest display work, stacking uppercase titles at 48–64px in a way that fills the viewport the same way box art fills a retail shelf. The deep navy ground (#0d1e63) anchors the header, footer, and hero zones in a single gravitational field, giving every product grid a dark sky to erupt against. Red (#e11b22) drives every primary CTA, sale callout, and active-state indicator — one signal color doing all the commercial lifting. Below it, electric yellow (#ffdd00), arcade green (#75c32c), citrus orange (#ff6900), and pale pink (#f78da7) rotate through category badges and product chips, functioning as a visual taxonomy where different age groups and game types carry different accent hues without requiring additional iconography. A pale mint-cream surface (#f2fbe4, {colors.surface-soft}) appears behind category landing grids, dropping the chroma just enough for comfortable browsing without abandoning the brand's saturated ground. Geometry leans utilitarian — cards and inputs carry {rounded.sm} at 8px, just enough softness to read as contemporary without dissolving the industrial frame that D-DIN's letterforms set up. Primary buttons go harder at {rounded.xs} (4px), a nearly rectangular shape that communicates action over invitation. Product metadata — age ratings in navy-filled chips, player counts in pale-surface pills at {rounded.full} — arrives in D-DIN Condensed at badge-label weight, tiny specs that carry real decision-making information without pulling the eye from product photography. What holds the visual system together across a catalog spanning toddler games and adult party titles is that #0d1e63 navy, which operates the way a game box's dark background operates: every other color reads more decisively against it than it would on white.

colors:
  primary: "#0d1e63"
  primary-active: "#003388"
  primary-disabled: "#ebf1ff"
  cta: "#e11b22"
  cta-active: "#cf2e2e"
  cta-disabled: "#f78da7"
  ink: "#0f0a0a"
  body: "#3c3a46"
  muted: "#55595c"
  muted-soft: "#818a91"
  hairline: "#a6b0b4"
  hairline-soft: "#abb8c3"
  canvas: "#feffff"
  surface-soft: "#f2fbe4"
  surface-card: "#ffffff"
  surface-strong: "#ebf1ff"
  on-primary: "#feffff"
  on-cta: "#feffff"
  on-dark: "#feffff"
  accent-yellow: "#ffdd00"
  accent-green: "#75c32c"
  accent-orange: "#ff6900"
  accent-gold: "#fcb900"
  accent-pink: "#f78da7"
  accent-teal: "#7bdcb5"
  dark-surface: "#2f4153"
  charcoal: "#32373c"
  near-black: "#4d4848"

typography:
  display-xl:
    fontFamily: "'D-DIN Condensed', 'D-DINCondensed', 'D-DIN', sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "'D-DIN Condensed', 'D-DINCondensed', 'D-DIN', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
    textTransform: uppercase
  display-md:
    fontFamily: "'D-DIN', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'D-DIN', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'D-DIN', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'D-DIN', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'D-DIN Exp', 'D-DINExp', 'D-DIN exp', 'D-DIN', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'D-DIN Exp', 'D-DINExp', 'D-DIN exp', 'D-DIN', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'D-DIN', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'D-DIN', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'D-DIN', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'D-DIN', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  badge-label:
    fontFamily: "'D-DIN Condensed', 'D-DINCondensed', 'D-DIN', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  age-rating:
    fontFamily: "'D-DIN Condensed', 'D-DINCondensed', 'D-DIN', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0
  price-display:
    fontFamily: "'D-DIN', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.2px
  price-sale:
    fontFamily: "'D-DIN', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0
    textDecoration: line-through

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
    backgroundColor: "{colors.cta}"
    textColor: "{colors.on-cta}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "12px 28px"
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.cta-active}"
    textColor: "{colors.on-cta}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.cta-disabled}"
    textColor: "{colors.on-cta}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "10px 26px"
    height: 48px
  button-navy:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "12px 28px"
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    border: "2px solid {colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "10px 26px"
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    activeIndicatorColor: "{colors.cta}"
    logoHeight: 40px
  nav-announcement-strip:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    salePriceTypography: "{typography.price-sale}"
    imageBgColor: "{colors.canvas}"
    padding: "{spacing.base}"
    hoverShadow: "0 4px 16px rgba(13,30,99,0.12)"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.display-sm}"
    minHeight: 480px
    paddingX: "{spacing.xl}"
    paddingY: "{spacing.section}"
  hero-category-landing:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    paddingY: "{spacing.xxl}"
  sale-badge:
    backgroundColor: "{colors.cta}"
    textColor: "{colors.on-cta}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  new-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  age-rating-chip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.age-rating}"
    rounded: "{rounded.xs}"
    width: 40px
    height: 40px
  player-count-chip:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  category-tab-active:
    backgroundColor: "{colors.cta}"
    textColor: "{colors.on-cta}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 16px"
  category-tab-inactive:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 16px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
  promotional-ribbon:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    height: 40px
    paddingX: "{spacing.base}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    paddingY: "{spacing.xxl}"

---

## Components

### Buttons

**`button-primary`** — Red (#e11b22) fill on a near-square {rounded.xs} (4px) corner, uppercase D-DIN at 16px/700 with 0.5px tracking. The near-rectangular shape reads as a buzzer rather than a cloud tap — pressing it should feel decisive. Active state darkens to `cta-active` (#cf2e2e); hover lifts 2px with a soft red-tinted drop shadow. Disabled state uses the pale pink `cta-disabled` (#f78da7).

**`button-navy`** — Identical geometry to `button-primary` but filled with the primary navy (#0d1e63). Used in hero zones and dark-ground contexts where red would read as alarm rather than invitation. On-primary white text keeps the same uppercase D-DIN spec. Pair with `button-primary` when two actions share a hero zone.

**`button-secondary`** — Canvas fill, 2px navy border, navy text. Matches `button-primary` at 48px height so the two sit level in side-by-side button pairs. Uppercase D-DIN preserves visual parity; hover fills the border color inward to a light `surface-strong` tint.

**`button-ghost`** — Transparent fill, 2px white border, white text. Appears exclusively on navy and charcoal backgrounds — hero panels, footer CTAs — where a colored button would break the dark-ground composition. Not for use on light surfaces.

### Navigation

**`nav-bar`** — 64px navy (#0d1e63) bar with the Goliath logo at 40px height on the left, uppercase D-DIN 700 category links at center, and utility icons (search, cart, account) at right in white. Active items carry a `cta` red underline indicator. Mobile below 744px collapses to a hamburger that opens a full-screen navy drawer, retaining the `category-tab-active` / `category-tab-inactive` chip row as a horizontal scroll rail.

**`nav-announcement-strip`** — 36px charcoal (#32373c) band above the main nav for sitewide promotions. White or `accent-yellow` text on the dark ground maintains contrast without borrowing the red signal reserved for CTAs.

### Product Cards

**`product-card`** — White `surface-card` tile with {rounded.sm} (8px) corners and a `hairline` border. Product image occupies the top ~60% on a white image field; title renders in `title-sm` (16px/700); price in `price-display` (22px/700). If a sale price exists, the original price renders in `price-sale` with strikethrough alongside the discounted price in `price-display`. Badges (`sale-badge`, `new-badge`, `age-rating-chip`) stack in the image's top-left corner. Hover lifts with `hoverShadow` — a 4px navy-tinted shadow that avoids the warm glow typical of lifestyle brands.

### Badges and Chips

**`sale-badge`** — Red (#e11b22) fill, white `badge-label` text, {rounded.xs}. Hard-edged and high-contrast; functions as a stop-sign interrupt in the product grid. Never stack two colored badges — `sale-badge` and `new-badge` should be mutually exclusive.

**`new-badge`** — Electric yellow (#ffdd00) fill, near-black `badge-label` text, {rounded.xs}. Lower urgency temperature than the sale badge — announces novelty without demanding action. Yellow on near-black achieves 7:1+ contrast.

**`age-rating-chip`** — 40×40px navy square, white D-DIN Condensed numerals ("8+", "12+"). Fixed dimensions keep rating information scannable across the grid at a glance, matching how physical PEGI icons work on box art. Render at {rounded.xs} to match the board geometry of the card.

**`player-count-chip`** — Pale-navy `surface-strong` (#ebf1ff) pill at {rounded.full} carrying "2–4 players" copy in `badge-label`. Softer than the age chip; reads as informational rather than regulatory. Place below the title, not in the image zone.

**`category-tab-active`** / **`category-tab-inactive`** — Active tab fills `cta` red with white `button-sm` text; inactive sits on `surface-strong` with primary navy text. Together they form the category filter row above product grids. Gap between tabs: {spacing.xs}. On mobile, the row becomes a horizontal scrollable strip.

### Hero

**`hero-banner`** — Full-width navy zone at minimum 480px, carrying a D-DIN Condensed `display-xl` headline in white and a `display-sm` subheadline. CTA renders as `button-primary` (red). Right half of the hero may carry a product or lifestyle image at natural opacity; the navy left half ensures text legibility without a scrim.

**`hero-category-landing`** — Softer entry for category browse pages: `surface-soft` (#f2fbe4) background, `ink` text, `display-md` headline at 36px. Used when the full navy-and-red hero voltage would overwhelm a browsing context. No minimum height constraint — content-driven.

### Search and Forms

**`search-bar`** — 44px tall, {rounded.sm}, `canvas` fill with a left-aligned magnifying-glass icon in `muted` gray. Placeholder copy in `muted`. Border shifts from `hairline` to `primary` navy on focus. On desktop the search bar sits in the nav-bar icon area as an expand-in-place field; on mobile it becomes a full-width row below the hamburger trigger.

**`text-input`** — Shares `search-bar` geometry. Focus ring: 2px `primary` navy border. Used in checkout, account registration, and contact forms. Error state swaps border to `cta` red with an inline error message in `body-sm`.

### Promotional

**`promotional-ribbon`** — Full-width yellow (#ffdd00) strip at 40px carrying uppercase `button-sm` copy in near-black. Appears above the nav-bar or inlined within hero zones for seasonal events. Never stacks with the `nav-announcement-strip` — one announcement surface is active at a time.

### Footer

**`footer`** — Navy (#0d1e63) ground with four-column link grid. Column headings in white `title-sm`; body links in `hairline` gray `body-sm`; link hover brightens to canvas white. Social icons via Font Awesome 5 Free at 20px in `hairline` color. Goliath logo renders at reduced size in the leftmost column above the legal copy in `caption`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero headline drops to `display-lg` (48px); age-rating and player-count chips stack below product title rather than overlaying the image; category tab row becomes horizontal scroll strip |
| Tablet | 744–1128px | Two-column product grid; nav shows primary category links, hides secondary utility links; hero retains two-column layout at `display-xl` with reduced padding |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav with all category links and utility icons; hero at full 480px minimum height with `display-xl` at 64px |
| Wide | > 1440px | Max-width container centered at 1440px; product grid may expand to five columns; hero background image scales without stretching; footer columns stay at four |

### Touch Targets

- All buttons minimum 48px height; icon buttons and nav icons minimum 44px touch zone
- Age-rating chips are 40×40px visual but carry a 48×48px invisible touch target on mobile
- Category tab chips use {rounded.full} pill shape on player-count chips to maximize perceived tap area relative to small physical size
- Footer links minimum 44px vertical tap zone via padding compensation

### Collapsing Strategy

- Navigation collapses in priority order: secondary utility links (Help, Track Order) first, then full nav becomes hamburger below 744px; category tabs move to horizontal scroll row at tablet
- Promotional ribbon shortens copy to a single line on mobile; overflow text is hidden with ellipsis rather than reflowing to two lines
- Hero switches from side-by-side (text left, image right) to stacked (image below text) below 744px; min-height drops to 320px
- Footer columns collapse from four across to two at tablet and a single accordion-expand list on mobile
- Product card badge stack collapses to a maximum of two overlapping chips on mobile with a "+N" overflow indicator if more exist

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact logo dimensions, clearspace rules, and wordmark color variants (white vs. navy lockup) were not extractable from metadata alone
- The full category-to-accent-color mapping (which hex maps to which game category or age tier) could not be confirmed from extraction
- Hover and focus transition timing values (easing curves, duration in ms) were not captured
- Whether D-DIN is self-hosted, loaded via a font CDN, or licensed per-seat, and the associated fallback rendering behavior on Windows, was not confirmed
- Exact mobile nav height in open-drawer state and whether a sticky-on-scroll nav variant exists were not captured
- Product image aspect ratio standards (1:1 square, 4:3, or freeform) could not be determined from metadata
- The search experience pattern (modal overlay, inline expand, or dedicated search results page) was not extractable
- Whether the multicolor accent palette ({colors.accent-green}, {colors.accent-orange}, {colors.accent-teal}) maps to specific branded product lines or is applied contextually was not determinable
