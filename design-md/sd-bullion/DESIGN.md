---
version: alpha
name: "SD Bullion"
source_url: "https://sdbullion.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Live spot prices scroll in Consolas across a near-black (#222222) ticker band positioned directly above the deep navy (#003665) masthead — announcing immediately that this platform operates on market time, not retail time. The design tension between data-density and precious-metal imagery is the central organizing logic: monospace numerals at 13px carry live gold and silver rates while Roboto Slab headlines anchor campaign copy, serving a buyer who might be simultaneously a chart-watcher and a collector. The gold spectrum — from oxidized #c1a91e through market-floor #e0b20d to vault-gleam #e6cc3d — appears at precisely the moments of commercial intent: buy-now CTAs, price-drop badges, and spot-price highlight borders. Red (#dc1d2c) functions as urgency-only signal, reserved for countdown timers on limited-mintage releases and flash sale callouts, never for navigation or informational labeling. Interactive blues (#4172d5, #2563eb) handle account links and secondary actions, holding the gold palette reserved for metal-specific moments so neither channel bleeds into the other. Cards sit on an #f7f7f7 canvas with #ffffff surfaces and #d7d7d7 hairlines — a neutral temperature matched to product photography of silver rounds and gold bars, where a warmer page background would compete with the metal. Corner radii stay minimal throughout: `{rounded.xs}` on inputs and product cards, `{rounded.none}` on deal badges and category callouts. This flatness signals a commodity marketplace where trust is built from price transparency and data clarity. Open Sans handles body copy and catalog navigation at 14–16px with generous line-height, sustaining readability across dense listing pages and comparison tables. The footer deepens to the same primary navy as the masthead, bookending the page in institutional weight with gold link text completing the two-tone brand circuit.

colors:
  primary: "#003665"
  primary-active: "#002a52"
  primary-hover: "#355dad"
  primary-disabled: "#c2c2c2"
  gold: "#e0b20d"
  gold-bright: "#e6cc3d"
  gold-dark: "#c1a91e"
  accent-red: "#dc1d2c"
  interactive: "#4172d5"
  interactive-hover: "#2563eb"
  ink: "#222222"
  body: "#323232"
  muted: "#575757"
  muted-soft: "#969696"
  hairline: "#d7d7d7"
  hairline-soft: "#e5e7eb"
  canvas: "#f7f7f7"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  ticker-bg: "#222222"
  on-primary: "#ffffff"
  on-gold: "#003665"

typography:
  display-xl:
    fontFamily: "'Roboto Slab', Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Roboto Slab', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Roboto Slab', Georgia, serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-lg:
    fontFamily: "Consolas, 'Courier New', Monaco, 'Liberation Mono', monospace"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -1px
  price-display:
    fontFamily: "Consolas, 'Courier New', Monaco, 'Liberation Mono', monospace"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  price-sm:
    fontFamily: "Consolas, 'Courier New', Monaco, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spot-ticker:
    fontFamily: "Consolas, 'Courier New', Monaco, monospace"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  badge-label:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  category-label:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px

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
    padding: 12px 24px
    height: 44px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-gold:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    border: none
  button-gold-active:
    backgroundColor: "{colors.gold-dark}"
    textColor: "{colors.on-gold}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: 11px 23px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.on-primary}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
    focusBorder: "2px solid {colors.interactive}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    linkHoverColor: "{colors.gold}"
    borderBottom: none
  spot-price-band:
    backgroundColor: "{colors.ticker-bg}"
    textColor: "{colors.gold-bright}"
    typography: "{typography.spot-ticker}"
    height: 36px
    separatorColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    shadow: "0 1px 3px rgba(0,0,0,0.06)"
  spot-price-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderLeft: "4px solid {colors.gold}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    priceTypography: "{typography.price-display}"
    labelTypography: "{typography.caption}"
    changeUpColor: "{colors.gold}"
    changeDownColor: "{colors.accent-red}"
  price-block:
    primaryTypography: "{typography.price-lg}"
    secondaryTypography: "{typography.price-display}"
    smallTypography: "{typography.price-sm}"
    primaryColor: "{colors.ink}"
    accentColor: "{colors.gold}"
    strikeColor: "{colors.muted-soft}"
  badge-deal:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  badge-alert:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
    iconColor: "{colors.muted}"
    focusBorder: "1px solid {colors.interactive}"
  category-filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.category-label}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
    stepButtonColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaColor: "{colors.gold}"
    padding: "{spacing.section} 0"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    bodyTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    linkColor: "{colors.gold}"
    borderTop: "3px solid {colors.gold}"
    padding: "{spacing.xxl} 0"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.hairline}"

## Components

### Buttons

**`button-primary`** — Solid navy (#003665) with white uppercase Open Sans text at 0.5px letter-spacing; this button carries the brand's institutional authority and appears on account actions, checkout progression, and modal confirmations. Hover lightens to #355dad, active deepens to #002a52, and the disabled state drops to #c2c2c2 to signal unavailability without alarming red.

**`button-gold`** — The primary purchase CTA — "Add to Cart", "Buy Now" — rendered in the brand's warmest gold (#e0b20d) with navy (#003665) text, making the financial intent unmistakable against the page canvas. Active state deepens to #c1a91e; the uppercase tracking (0.5px) and 700 weight keep legibility at all sizes.

**`button-secondary`** — White surface with a navy border and navy uppercase text; used for secondary catalog actions like "Learn More", "View Details", and "Compare". Hover fills with #f0f0f0 to acknowledge interaction without displacing the primary CTA hierarchy on pages where both buttons coexist.

**`button-ghost`** — Transparent background with a white border and white text, 36px height, used exclusively on dark (navy or near-black) surfaces such as the hero banner and footer CTA blocks. Keeps the dark panel interactive without introducing a competing fill color.

### Nav Bar & Spot Price Band

**`nav-bar`** — Full-width sticky navy bar at 64px height carrying logo, primary navigation links, and account/cart controls in white Open Sans 600 at 14px. Links hover to gold (#e0b20d), the single warm signal on the bar. The nav sits directly below the spot-price band, so the stacked effect reads as: ticker → brand → content.

**`spot-price-band`** — A 36px near-black (#222222) band pinned to the very top of the viewport, displaying live gold, silver, platinum, and palladium spot prices in Consolas at 13px weight-600 in gold-bright (#e6cc3d). Metal names are muted gray (#575757) separators; price-change arrows run gold (up) or red (#dc1d2c) down. This band is the first element users read and the primary trust signal.

### Product Card

**`product-card`** — White card on #f7f7f7 canvas with a 1px #d7d7d7 hairline border and a subtle 1px shadow. The product name renders in Open Sans 600 at 16px, the spot-basis price in Consolas 700 at 22px with gold (#e0b20d) for premium-tier pricing and ink (#222222) for standard. Badge slots (deal, new, alert) pin to the top-left corner with `{rounded.none}` edges, flush to the card boundary.

### Price Display

**`price-block`** — A three-tier monospace price hierarchy: `price-lg` (28px/700) for the cart/checkout line-item total, `price-display` (22px/700) for the main product page price, and `price-sm` (14px/400) for per-unit or per-ounce secondary callouts. Strike-through prices for discounted items render in #969696. Gold (#e0b20d) accentuates savings labels adjacent to the primary price.

**`spot-price-card`** — A data card with a 4px left border in gold, used in sidebar widgets and the homepage spot-rate dashboard. Price renders in `price-display` monospace; the label (e.g., "Gold Spot") in `caption` at #969696. Positive movement colors the delta in gold; negative in red (#dc1d2c) — matching the ticker band's convention.

### Badges

**`badge-deal`** — Gold (#e0b20d) fill with navy text in 11px uppercase Open Sans 700, zero border-radius, 3px/8px padding. Applied to "On Sale", "Best Price", and discount-percentage callouts. The flat rectangular shape distinguishes it from rounded pill tags and reads as a price sticker.

**`badge-alert`** — Red (#dc1d2c) fill with white text; identical structure to `badge-deal`. Appears exclusively on countdown-adjacent content: "Only 23 Left", "Ending Tonight", limited-mintage run warnings. Never used for informational or navigational elements.

**`badge-new`** — Navy fill with white text; signals newly listed products, recent releases, and 2024/2025 mint-year coins. Maintains the same `{rounded.none}` geometry as the other badge variants for visual consistency across the product grid.

### Search Bar

**`search-bar`** — 44px input field with a magnifier icon in #575757 on the right or left edge, white background, 1px #d7d7d7 border, `{rounded.xs}`. Focus state promotes the border to 1px #4172d5 (interactive blue), not gold — separating search affordance from purchase action. Placeholder text in #575757 at body-md scale.

### Hero Banner

**`hero-banner`** — Full-bleed navy panel with Roboto Slab display-xl headlines in white, body copy in Open Sans body-md, and a `button-gold` CTA. Padding is `{spacing.section}` top and bottom. Secondary action may use `button-ghost`. Background may carry a low-opacity metal texture or photography with a dark overlay to maintain text contrast.

### Footer

**`footer`** — Deep navy matching the masthead, with a 3px gold (#e0b20d) top border as the visual seam between content and footer. Column headings in Open Sans 600 at 16px white; body links in gold (#e0b20d); legal/secondary links in #969696. The navy-gold bookend with the nav creates a closed brand frame around every page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger nav collapses all links into a full-height drawer; spot-price band shows gold only (hides platinum/palladium); product grid is 1-column; `price-lg` drops to 22px; quantity selector and add-to-cart stack vertically |
| Tablet | 744–1128px | Nav shows top-level categories only with overflow "More" dropdown; product grid is 2-column; spot-price band shows gold and silver; hero padding reduces to `{spacing.xl}` |
| Desktop | 1128–1440px | Full nav with all category labels visible; product grid is 3–4 column; spot-price band shows all four metals; sticky sidebar price summary on product detail page |
| Wide | > 1440px | Max-width container (~1280px) centered; side margins fill with canvas color; nav and footer span full width at primary navy |

### Touch Targets

- All buttons and filter chips minimum 44px height on mobile
- Quantity selector increment/decrement controls minimum 44×44px tap zones
- Nav drawer links minimum 48px row height
- Badge tap areas extend 8px beyond visible bounds via padding

### Collapsing Strategy

- Spot-price band: collapses from 4 metals → 2 metals → gold-only ticker at narrowest breakpoints
- Product filters: horizontal scroll chip row on mobile, sidebar panel on desktop
- Nav categories: full label row on desktop, icon+label on tablet, drawer-only on mobile
- Footer columns: 4-column grid on desktop, 2-column on tablet, single-column stacked on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Stock-status green (e.g. "In Stock" indicator) not present in extracted palette; a standard #2d7a2d or similar is likely but unconfirmed
- Exact nav height unconfirmed (64px estimated from visual proportion of extracted color density)
- Meta theme-color not set, so browser chrome color on mobile is undefined
- Animation/transition specs for live spot-price updates (flicker, fade, or slide-in) not extractable from static analysis
- Precise font loading method for Roboto Slab and Open Sans (Google Fonts CDN vs self-hosted) unconfirmed
- Account dashboard, checkout funnel, and order-history page color specifics not captured
- Hover state for product card (border intensification, shadow lift, or gold accent) not confirmed
- Mobile nav drawer background color (likely primary navy, but could be surface-card white) not confirmed
- Exact coin/bar category icon set style (SVG glyphs, photography thumbnails, or illustrated icons) not extractable
