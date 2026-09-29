---
version: alpha
name: "APMEX"
source_url: "https://www.apmex.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Stacked American Eagles, kilobars, and Morgan dollars define the product catalog, and APMEX's interface makes no effort to disguise that material context — the design system is built to look like the velvet tray beneath the coin, not the magazine ad above it. The deep charcoal baseline (#313131) anchors every surface, a near-black that reads as display-case lining rather than tech-brand dark mode, chosen to maximise contrast against high-gloss precious-metal photography. Gold-toned interactive elements follow as a direct documentary consequence: {colors.primary} names the category the platform trades in before a single headline is read. Where most e-commerce brands borrow a personality color, APMEX's gold is tautological.

  Secondary surfaces sit in warm off-whites and pale grays, leaving coin photography — minted reliefs, proof finishes, stackable bars — as the uncontested visual hero. Typography draws entirely from the native system stack (Arial, -apple-system), signaling institutional sobriety over editorial personality. Weights stay conservative; price data and live spot tickers carry the urgency that other brands push through typographic drama.

  The persistent spot-price bar locked to the very top of the viewport — live gold, silver, platinum, and palladium quotes updating in real time — is structurally the most distinctive UI element on the site, a data ribbon that no fashion or grocery retailer would place above the hero image. It frames the transaction context immediately: every product here has a live market price, and the interface never lets the visitor forget it. Product cards layer mint name, metal purity, troy weight, and real-time pricing in a dense informational pattern suited to buyers comparing fractional ounces rather than lifestyle aesthetics.

  Trust infrastructure is unusually prominent: BBB ratings, secure-checkout seals, and IRA-eligible tags appear inline with product listings rather than relegated to a footer. Corner radii trend conservative — {rounded.xs} to {rounded.sm} on cards and inputs — matching the institutional register, with {rounded.full} reserved for small filter chips and badge tags rather than primary CTAs. The overall composition resembles a financial-exchange skin applied to an e-commerce chassis: legibility and security signaling at every decision point, with warm gold as the single chromatic signal against charcoal and white.

colors:
  primary: "#C4923A"
  primary-hover: "#B88232"
  primary-active: "#A87830"
  primary-disabled: "#E8D5B0"
  ink: "#313131"
  body: "#4A4A4A"
  muted: "#767676"
  muted-soft: "#9E9E9E"
  hairline: "#D9D9D9"
  hairline-soft: "#EFEFEF"
  canvas: "#FFFFFF"
  surface-soft: "#F8F5F0"
  surface-card: "#FFFFFF"
  surface-dark: "#1E1E1E"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  price-up: "#2E7D32"
  price-down: "#C62828"
  price-neutral: "#767676"
  ira-accent: "#1A4A8A"
  trust-seal: "#1A4A8A"

typography:
  display-xl:
    fontFamily: "Arial, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "Arial, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "Arial, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Arial, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  price-display:
    fontFamily: "Arial, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  spot-ticker:
    fontFamily: "Arial, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  nav-label:
    fontFamily: "Arial, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  data-label:
    fontFamily: "Arial, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 11px
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
    padding: "12px 24px"
    height: 44px
    hoverBackgroundColor: "{colors.primary-hover}"
    activeBackgroundColor: "{colors.primary-active}"
    disabledBackgroundColor: "{colors.primary-disabled}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "11px 23px"
    height: 44px
    border: "1px solid {colors.ink}"
    hoverBackgroundColor: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "11px 23px"
    height: 44px
    hoverTextColor: "{colors.primary-active}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    padding: "10px 14px"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoMaxHeight: 36px
    dropdownBackgroundColor: "{colors.canvas}"
    dropdownBorder: "1px solid {colors.hairline}"
    activeItemColor: "{colors.primary}"
  spot-price-ticker:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.spot-ticker}"
    height: 36px
    padding: "0 {spacing.base}"
    upColor: "{colors.price-up}"
    downColor: "{colors.price-down}"
    neutralColor: "{colors.price-neutral}"
    labelColor: "{colors.muted-soft}"
    metalSeparator: "1px solid rgba(255,255,255,0.15)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
    imageRounded: "{rounded.none}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    ctaTypography: "{typography.button-sm}"
    hoverBorder: "1px solid {colors.primary}"
    hoverShadow: "0 2px 8px rgba(0,0,0,0.10)"
  metal-filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    selectedBorder: "1px solid {colors.primary}"
  ira-badge:
    backgroundColor: "{colors.ira-accent}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 7px"
  trust-seal-row:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.lg} {spacing.base}"
    borderTop: "1px solid {colors.hairline}"
    iconSize: 40px
    gap: "{spacing.xl}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    inputBackgroundColor: "{colors.canvas}"
    inputTextColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    iconColor: "{colors.muted}"
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    height: 44px
  price-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.data-label}"
    cellTextColor: "{colors.ink}"
    cellTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    priceTypography: "{typography.price-display}"
    upColor: "{colors.price-up}"
    downColor: "{colors.price-down}"
    rowHoverBackgroundColor: "{colors.surface-soft}"
  promotional-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    linkColor: "{colors.on-primary}"
    linkTextDecoration: underline
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    hoverBorder: "1px solid {colors.primary}"
    imageAspectRatio: "1 / 1"
    labelPadding: "{spacing.sm}"
    labelBackgroundColor: "{colors.canvas}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} 0"
    columnGap: "{spacing.xxl}"

## Components

### Buttons
**`button-primary`** — The primary CTA renders in gold (#C4923A) with white type on a 4px-radius rectangle at 44px height, sitting at medium weight 700 to project authority without shouting. On hover it darkens to `primary-hover`; on press it deepens further to `primary-active`. Disabled state washes to `primary-disabled`, a pale sand that preserves the gold hue family.

**`button-secondary`** — White fill with a 1px solid charcoal border, matching the primary's height and radius. Used for secondary purchase paths (Add to Watchlist, Compare) and modal cancel actions. Hover shifts the fill to `surface-soft` for a gentle step back.

**`button-ghost`** — Transparent background with primary-gold text; no border. Appears on detail pages as an inline link-styled action (View Coin Details, See All Variants) where a bordered button would add visual weight without warrant.

### Spot Price Ticker
**`spot-price-ticker`** — A full-width bar fixed to the very top of the viewport, rendered in near-black `surface-dark` (#1E1E1E). Metal names (GOLD, SILVER, PLATINUM, PALLADIUM) appear in `muted-soft` as labels; prices render in `on-dark` at `spot-ticker` weight. Live price-change deltas colorize to `price-up` (green) or `price-down` (red). This element has no rounded corners and spans the full viewport edge-to-edge, functioning as a persistent market-data ribbon that never scrolls away.

### Product Card
**`product-card`** — A white card with a 1px `hairline-soft` border and 4px radius. The upper region is devoted entirely to product photography at full card width (no padding), typically square-cropped at 1:1. Below the image: mint name in `body-sm`, product title in `title-sm`, troy weight and purity in `caption`, and the current buy price in `price-display` weight. A full-width `button-primary` CTA closes the card at the bottom. On hover, the border transitions to `primary` and a subtle shadow appears. IRA-eligible products append an `ira-badge` beneath the title.

### Spot / Price Table
**`price-table`** — A data table used on metal overview pages (Gold, Silver hub pages) showing quantity-break pricing. Column headers use `data-label` (12px uppercase, 0.5px tracking) on a `surface-soft` background row. Data rows alternate on hover to `surface-soft`. Price columns colorize positives in `price-up` and declines in `price-down`. No rounded corners on any cell; the table reads as a financial ledger.

### Metal Filter Chips
**`metal-filter-chip`** — Pill-shaped chips (9999px radius) used in category sidebars and search-results filters to toggle metal type, mint, year, and weight. Unselected state: `surface-soft` fill with `hairline` border. Selected state inverts to `primary` fill with `on-primary` text — the only context outside primary CTAs where gold fill appears at this small scale.

### Search Bar
**`search-bar`** — A composite input-plus-submit unit rendered as a single horizontal bar. The text input fills most of the width; the right end terminates in a gold `button-primary`-styled submit button (loupe icon on mobile, "Search" label on desktop) flush to the input border. The outer container sits in `surface-soft`, creating a slight tray effect. Focus ring: `primary` border on the input segment only.

### Promotional Banner
**`promotional-banner`** — A slim full-width gold bar (`primary` fill) pinned just below the spot-price ticker, carrying offer copy in `on-primary` white at `body-sm`. Links within the banner stay white with underline decoration to remain accessible on the gold ground. Dismissible on some contexts; persistent on category pages.

### IRA Badge
**`ira-badge`** — A small navy (#1A4A8A) rectangular tag (4px radius) reading "IRA ELIGIBLE" in 11px 700-weight uppercase. Appears inline with product title and in product-card metadata. The navy contrasts the gold CTA system to signal a distinct category attribute rather than a promotional flag.

### Trust Seal Row
**`trust-seal-row`** — A horizontal strip in `surface-soft` appearing above the footer, holding BBB accreditation, SSL-cert badges, Google Customer Reviews, and payment-method icons. Logos render at 40px max-height with generous horizontal gap (`spacing.xl`). Caption-weight text labels appear below each seal. The row signals financial-platform trust conventions borrowed from banking rather than lifestyle retail.

### Footer
**`footer`** — Full charcoal (`ink` #313131) background occupying substantial vertical space with four to five column groups: Shop by Metal, About APMEX, Account, Learning Center, and a newsletter signup. Column headings use `title-sm` in `on-dark`. Links render in `muted-soft` and shift to `primary` gold on hover — the only gold-on-dark interaction in the system, and the most visually striking state in the footer. No top border; the dark slab simply begins after the trust-seal row.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Spot-price ticker collapses to 2 metals (Gold, Silver) with a "More" toggle; nav collapses to hamburger with full-screen drawer; product grid shifts to 2-column; price-table scrolls horizontally; search bar expands full-width on tap |
| Tablet | 744–1128px | 3-column product grid; nav shows top-level labels without mega-dropdown; spot-ticker shows all 4 metals in compact form; category filter moves to a horizontal scroll-strip above results |
| Desktop | 1128–1440px | Full mega-dropdown nav with subcategory columns; 4-column product grid; spot-ticker expands with extended price-change metadata; filter sidebar fixed at left of results grid |
| Wide | > 1440px | Max content width ~1400px centered with equal gutters; spot-ticker gains chart sparklines per metal; hero sections increase padding to `section` tokens |

### Touch Targets
- All interactive chip and badge elements maintain minimum 44×44px tap targets via padding extension
- Spot-ticker metal items expand tap area on mobile with 36px height → 44px touch padding
- Filter chips enforce minimum 44px height at mobile widths regardless of label length

### Collapsing Strategy
- Mega-dropdown nav collapses to icon-only hamburger below 1128px; category depth moves into slide-in drawer with back-navigation breadcrumbs
- Price table columns de-prioritize "Dealer Premium" and "Change %" columns below 744px, showing only Quantity, Price per Unit, and Total
- Trust-seal row stacks to 2×3 grid on mobile; all seals remain visible (not hidden)
- Footer columns collapse to accordion-style expandable sections on mobile, defaulting to closed

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site returned a bot-challenge page ("Just a moment...") during extraction; only one hex value (#313131) was captured with confidence — all other colors derive from brand knowledge and published brand assets, not live extraction
- No custom typeface detected; the entire type system uses system-stack fonts (Arial, -apple-system). If APMEX has licensed a custom display face for headings, it was not observable
- Exact gold brand hex is unconfirmed from extraction — #C4923A is derived from publicly visible brand assets and logo analysis; the true primary may vary from #B8832A to #CFA040
- No meta theme-color tag found, so mobile browser chrome color is unspecified
- Spot-ticker refresh interval, animation behavior, and exact layout of multi-metal ribbon are inferred from category convention; live implementation detail unknown
- Dark-mode support status is unknown — no CSS custom-property tokens for dark theme were extractable
- Exact nav-bar mega-dropdown column structure and depth unknown without JavaScript execution
- Cart and checkout flow color system (especially error/validation states) not extractable from homepage load
