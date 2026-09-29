---
version: alpha
name: "Ozzie Collectables"
source_url: "https://www.ozziecollectables.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Gold as a primary action color is an act of confidence — most e-commerce operators treat #ffd700 as a warning tone, yet Ozzie Collectables stakes its entire CTA system on it, treating chrome-yellow as the store's single voltage rather than a cautionary accent. The decision suits the audience: Funko Pops and trading cards are objects people collect for their visual intensity, and a store that mirrors that energy in gold and deep orange (#ff7d00) signals authenticity before a single product is inspected. On-primary text runs #121212 against the gold field — a reversal of the usual white-on-dark convention that holds contrast cleanly because Cabin, the brand's humanist geometric sans-serif, carries enough stroke weight to remain legible in near-black on chrome-yellow. The cream surface token (#fff8d6) is the quieter half of this palette — it replaces clinical white in announcement bars, filter panels, and checkout sidebars, giving every page the warmth of a collector's display case bathed in late-afternoon light rather than fluorescent overhead. Near-black (#121212) handles all structural anchors and body text, while the light gray (#dedede) draws hairlines and disabled states without the coldness of pure silver. Product cards sit on `{rounded.sm}` corners — subtle enough to read as modern grid items but present enough to soften the inevitable image-heavy density of a pop culture catalog. New-arrival and hot-pick badges use `{rounded.full}` pill shapes in orange (#ff7d00) against near-black, a pairing that reads as energetic without becoming garish. The overall register is a collector's market stall translated into digital: warm, gold-lit, stocked to the edges, and confident that its audience knows exactly what it's here for.

colors:
  primary: "#ffd700"
  primary-active: "#e6c200"
  primary-disabled: "#fff0a0"
  secondary: "#ff7d00"
  secondary-active: "#e06d00"
  ink: "#121212"
  body: "#333333"
  muted: "#6b6b6b"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#fff8d6"
  surface-card: "#ffffff"
  on-primary: "#121212"
  on-secondary: "#ffffff"
  on-dark: "#ffffff"
  badge-new: "#ff7d00"
  badge-sale: "#e63946"
  star: "#ffd700"

typography:
  display-xl:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.1px
  badge-label:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-original:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 46px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 46px
    border: "2px solid {colors.ink}"
  button-orange:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 46px
  button-sm-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    logoColor: "{colors.primary}"
    borderBottom: "3px solid {colors.primary}"
  announcement-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    height: 36px
    padding: 0 {spacing.base}
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    height: 42px
    padding: 0 {spacing.base}
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    imageAspectRatio: "1:1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    hoverBorderColor: "{colors.primary}"
    hoverShadow: "0 4px 16px rgba(255,215,0,0.25)"
  badge-new:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 3px 9px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 3px 9px
  badge-hot:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 3px 9px
  price-tag:
    currentPriceColor: "{colors.ink}"
    currentPriceTypography: "{typography.price-display}"
    originalPriceColor: "{colors.muted}"
    originalPriceTypography: "{typography.price-original}"
    originalPriceDecoration: line-through
    salePriceColor: "{colors.badge-sale}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.display-sm}"
    ctaButton: "{components.button-primary}"
    padding: "{spacing.xxl} {spacing.section}"
    minHeight: 480px
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    itemPadding: "{spacing.md} {spacing.base}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    gap: "{spacing.sm}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.ink}"
    headerTextColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    totalTypography: "{typography.title-md}"
    checkoutButton: "{components.button-primary}"
    borderLeft: "3px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.primary}"
    linkHoverColor: "{colors.secondary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "4px solid {colors.primary}"
    padding: "{spacing.xxl} {spacing.section}"
  star-rating:
    filledColor: "{colors.star}"
    emptyColor: "{colors.hairline}"
    typography: "{typography.caption}"

## Components

### Buttons
**`button-primary`** — Gold (#ffd700) fill with near-black text and 8px rounded corners; 46px tall with `font-weight: 700` Cabin ensuring the label reads in near-black on chrome-yellow at all viewport sizes. Active state darkens to #e6c200; disabled washes out to #fff0a0 with muted text and a `not-allowed` cursor.

**`button-secondary`** — White fill with a 2px solid #121212 border mirrors the primary dimensions exactly; used for secondary actions like "Add to Wishlist" or filter toggles where the gold primary would compete with CTA hierarchy.

**`button-orange`** — Orange (#ff7d00) fill with white text; used for urgency-adjacent CTAs like "Buy Now" or flash-sale banners where gold already saturates the page and a hue shift signals escalation.

**`button-sm-ghost`** — Transparent background with near-black label text; 4px radius; used for inline actions inside product cards (quick-view, compare) that should not compete with the main add-to-cart button.

### Search Bar
**`search-bar`** — Full-radius pill (`{rounded.full}`) that contrasts with the square grid of product tiles, signaling a different interaction mode. The border thickens from 2px gray to 2px gold on focus, grounding the active state in brand color without background change.

### Product Card
**`product-card`** — 1:1 image ratio over a white surface with 1px #dedede border and 8px corners. On hover, the border transitions to gold and a warm gold-tinted drop shadow (`rgba(255,215,0,0.25)`) lifts the card without heavy shadow drama. Badges — New, Sale, Hot — pin to the top-left of the image in pill shapes; gold for Hot Pick, orange for New Arrival, red for Sale.

### Price Tag
**`price-tag`** — Current price in #121212 at 20px/700 for visual weight; struck-through original price in #6b6b6b at 14px/400 sits inline to its right; sale price overrides the current color with #e63946. The proximity and contrast ratio of the three states communicates markdown clearly without extra labeling.

### Navigation Bar
**`nav-bar`** — Near-black (#121212) background with a 3px gold bottom border that acts as a brand underline at page top. Logo renders in #ffd700 on dark, maintaining the gold-on-black collector's aesthetic. Nav links run Cabin 14px/600 in white, shifting to gold on hover.

### Announcement Bar
**`announcement-bar`** — The cream surface (#fff8d6) separates it visually from the black nav without a hard rule, using warmth contrast rather than border contrast. Caption-weight Cabin in near-black handles shipping offers and promo codes legibly at 36px height.

### Hero Banner
**`hero-banner`** — Near-black canvas with the headline in gold (#ffd700) at 48px/700 and subline in white at 24px/600. The primary CTA button sits gold-on-gold territory only when the background panel is truly dark; a secondary white-border ghost button offers contrast pairing. Minimum 480px height allows full product photography.

### Category Strip
**`category-strip`** — Cream (#fff8d6) background row of pill-adjacent rounded tiles (8px corners); active category fills gold with near-black text, inactive tiles are white with gray hairline border. This component doubles as a mobile horizontal scroll filter and a desktop tab row.

### Badges
**`badge-hot`** — Gold fill, near-black uppercase label at 11px/700 with 0.5px tracking; `{rounded.full}` pill. **`badge-new`** — Orange fill with white text, same geometry. **`badge-sale`** — Red (#e63946) fill with white text. All three pin to image corners via absolute positioning in the product card, stacking vertically when multiple apply.

### Cart Drawer
**`cart-drawer`** — Slides in from the right with a white body and a near-black header strip matching the nav, unified by a 3px left-side gold border that frames the panel. Checkout button is full-width gold primary.

### Footer
**`footer`** — Near-black with a 4px gold top border marking the transition from page content. Links render in gold (#ffd700), shifting to orange (#ff7d00) on hover — a warm within-palette hover rather than a color-change surprise. Section headings in Cabin 15px/600 white separate columns.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger + logo + cart icon; search bar moves inside drawer; category strip becomes horizontal scroll row; hero shrinks to 320px min-height |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows top-level categories inline with hamburger for sub-menus; search bar visible in header; hero banner at 400px min-height |
| Desktop | 1128–1440px | Three–four column product grid; full nav-bar with all category links visible; mega-menu on category hover; hero at full 480px |
| Wide | > 1440px | Max content width capped at 1440px with symmetric margin; product grid stays at four columns; hero image scales without stretching layout |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Product card tap target covers full card surface, not just title text
- Badge chips sized to minimum 32px height for reliable tap even when stacked
- Cart icon and hamburger icon padded to 48×48px hit areas in mobile nav

### Collapsing Strategy
- Category navigation: mega-menu on desktop collapses to nested accordion inside hamburger drawer on mobile
- Filters sidebar: fixed left column on desktop becomes bottom sheet modal on mobile, toggled by a gold "Filter" pill button
- Product grid: four → three → two → one column breakpoints using CSS Grid auto-fill with `minmax(200px, 1fr)`
- Footer columns: four-column grid collapses to two on tablet, single accordion-expandable list on mobile
- Announcement bar: full text on desktop, truncated with marquee scroll on mobile when content exceeds viewport width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; mobile browser chrome color assumed to match nav-bar near-black (#121212)
- Font weight availability for Cabin not confirmed beyond standard 400/600/700; intermediate weights (500) may render as nearest available
- Exact nav-bar height on mobile not extracted; 60px assumed from Shopify theme conventions
- Hover/focus animation durations not extractable from static analysis; standard 150–200ms ease assumed
- No confirmed icon library or icon style (outline vs filled); system/generic icons assumed
- Secondary typeface for display or decorative use (if any) not confirmed — Cabin appears to be the sole font family
- Exact product grid gutter width not extracted; 16px assumed from Shopify Dawn/Impulse defaults
- Sale badge color (#e63946) is inferred from convention, not extracted from the live site palette
