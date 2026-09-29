---
version: alpha
name: "Plastic Empire"
source_url: "https://www.plasticempire.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Bright #118811 green set against a near-black (#121212) field is an unusual call for a collectibles superstore — most shops in the Funko space default to corporate blue or shadowy charcoal, but Plastic Empire stakes its territory with a vivid mid-green that reads across vinyl-packed shelves and thumbnail grids alike. The palette is deliberately primary: green for action (every CTA, every in-stock signal), #e32402 red for urgency (sale, low-stock, clearance), #ffbd00 yellow for celebration and featured drops, and #dedede silver-gray for structure and dividers. Nothing in the stack is subtle — these are the colors of box art, not luxury goods. Type runs in Muli, a geometric sans that sits at moderate weights for body copy and jumps to bold 700–800 for price tags and product titles, matching the energy of a store where the headline is always the figure in the box. Navigation is dense — categories span action figures, comics, trading cards, exclusives, pre-orders, and clearance — so the nav bar must handle horizontal scroll on mobile without collapsing into a hamburger wilderness. Product cards are the dominant UI unit: square-cropped art, a title in `{typography.title-md}`, a price in `{typography.price-display}`, and badge slots for Exclusive, Pre-Order, Sale, and New Arrival — all drawn from the same four-color signal palette. The `{rounded.xs}` to `{rounded.sm}` range keeps corners firm and geometric, fitting the hard plastic aesthetic of the product category. Checkout urgency is amplified through red countdown badges and yellow "only X left" callouts. The overall register is a high-density comic shop translated into an always-on digital grid — loud, legible, and genuinely fun to browse.

colors:
  primary: "#118811"
  primary-active: "#0d6e0d"
  primary-disabled: "#8cc98c"
  accent-red: "#e32402"
  accent-red-muted: "#f9ded9"
  accent-yellow: "#ffbd00"
  accent-yellow-muted: "#fff4cc"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  hairline: "#dedede"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-accent-red: "#ffffff"
  on-accent-yellow: "#121212"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 18px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 18px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0
    color: "#e32402"
  price-original:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
    textDecoration: line-through
  badge-label:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 10px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 14px
    fontWeight: 800
    lineHeight: 1.25
    letterSpacing: 0.4px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  category-label:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.1px

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
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 44px
  button-danger:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-accent-red}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-sm-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 50px
    borderBottom: "none"
  nav-top-utility:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 36px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 42px
    searchIconColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm}"
    imageAspectRatio: "1 / 1"
    imageObjectFit: contain
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    hoverShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-sale:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.accent-red-muted}"
    priceTypography: "{typography.price-sale}"
    originalPriceTypography: "{typography.price-original}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-accent-red}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-exclusive:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-accent-yellow}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-preorder:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-low-stock:
    backgroundColor: "{colors.accent-yellow-muted}"
    textColor: "{colors.on-accent-yellow}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.display-sm}"
    ctaButton: "{components.button-primary}"
    minHeight: 360px
    padding: "{spacing.xxl} {spacing.xl}"
    overlayScrim: "linear-gradient(90deg, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0) 60%)"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.category-label}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
    hoverBorder: "1px solid {colors.primary}"
    hoverTextColor: "{colors.primary}"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.category-label}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    separator: "/"
    separatorColor: "{colors.hairline}"
  promo-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 36px
    textAlign: center
  section-header:
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    borderBottom: "3px solid {colors.primary}"
    paddingBottom: "{spacing.sm}"
    marginBottom: "{spacing.lg}"
  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackgroundColor: "{colors.canvas}"
    inactiveTextColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    itemSize: 36px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.title-md}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.primary}"
    dividerColor: "#333333"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The primary CTA runs #118811 green fill with white uppercase Muli 800 lettering, 4px corners, and 44px height. It handles Add to Cart, Checkout, and search submit; on hover it deepens to `{colors.primary-active}` (#0d6e0d) with no transform. The disabled state fades to `{colors.primary-disabled}` (a washed sage green) and sets pointer-events: none.

**`button-secondary`** — White fill with a 2px green border and green text; used for wishlist, secondary filters, and view-all links. Shares the same uppercase Muli 800 treatment to keep hierarchy clear even at equal visual size.

**`button-danger`** — #e32402 red, used sparingly for remove-from-cart, cancel pre-order, and clearance triggers. White text with the same uppercase badge energy as the primary.

### Badges

**`badge-new`** — Green fill, white uppercase Muli 800 at 10px/0.6px tracking. Pinned top-left on product card image. Signifies recent inventory additions.

**`badge-sale`** — Red (#e32402) fill, white text. Appears in tandem with a strikethrough original price in `{typography.price-original}` below the sale price.

**`badge-exclusive`** — Yellow (#ffbd00) fill, near-black text. Used for Funko Exclusive and store-exclusive variants; the gold immediately signals collectible status.

**`badge-preorder`** — Near-black (#121212) fill, white text. Reserved for items not yet shipping; appears in place of or alongside the add-to-cart button.

**`badge-low-stock`** — Pale yellow `{colors.accent-yellow-muted}` fill with dark text; softer than the sale badge, signals "only N left" without full alarm color.

### Navigation

**`nav-top-utility`** — A slim 36px green bar at the very top of the viewport carrying shipping thresholds ("Free shipping over $X") and login/account links in small white Muli. It sits above the main dark nav and uses green to maintain brand continuity.

**`nav-bar`** — Near-black (#121212) background, white `{typography.nav-link}` links at 13px/700. The horizontal list covers Funko Pop, Marvel, DC, Disney, Anime, Sports, Pre-Order, Sale, and more. On desktop, categories scroll horizontally if they overflow. A search bar with a green magnifier icon is inset at the right side.

### Search

**`search-bar`** — White input with `{rounded.xs}` corners, 1px `{colors.hairline}` border. On focus, border upgrades to 2px green. The submit icon button sits inside the trailing edge, colored `{colors.primary}`. Suggestions dropdown has `{colors.surface-soft}` background and `{rounded.sm}` shadow.

### Hero

**`hero-banner`** — Full-bleed image behind a left-anchored dark scrim gradient that fades from 70% black to transparent at 60% width. Headline in `{typography.display-xl}` white, subline in `{typography.display-sm}`, and a green `button-primary` CTA below. Minimum 360px tall on desktop; reduced to 220px on mobile with centered text layout.

### Product Card

**`product-card`** — White card with 1px `{colors.hairline}` border and 4px corners. The top half is a square 1:1 image container with `{colors.surface-soft}` background and contain-fit for box-art imagery. Badge chips (new/sale/exclusive/preorder) stack in the top-left corner of the image zone. Below the image: title in `{typography.title-sm}`, price in `{typography.price-display}`, and a compact green Add to Cart button. On hover, the card lifts with a subtle box-shadow; the image does not zoom (preserves artwork integrity).

### Category Chips

**`category-chip`** — Pill-shaped filter tokens using `{rounded.full}` that appear as horizontal scroll row beneath the hero or at the top of collection pages. Idle state is `{colors.surface-soft}` with a `{colors.hairline}` border. Active/selected state flips to green fill. On hover, border and text color turn green without fill change.

### Section Header

**`section-header`** — Section titles (New Arrivals, Trending Funko, Pre-Orders) use `{typography.display-md}` in near-black with a 3px green left or bottom border as the brand underline treatment — no decorative dividers, just the color stripe.

### Promo Bar

**`promo-bar`** — A full-width 36px green bar above `nav-top-utility`, cycling shipping offers and discount codes in small white Muli. Uses the same green as the primary CTA so the top-of-page block reads as one branded header stack.

### Footer

**`footer`** — Near-black (#121212) background with white column headings in `{typography.title-md}`, links in `{typography.body-sm}` light gray (`{colors.hairline}`), and hover links turning green. Payment icon row and social icons sit at the bottom. Column grid is 4-up on desktop, 2-up on tablet, single-column accordion on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero drops to 220px, text centered; nav collapses to hamburger + search icon; category chips scroll horizontally; badges reduce font to 9px |
| Tablet | 744–1128px | 2–3 column product grid; nav shows top categories inline, overflow hidden behind "More" dropdown; hero 280px; promo bar wraps to 2 lines if needed |
| Desktop | 1128–1440px | 4-column product grid; full horizontal nav with all categories visible; hero 360px; category chip row shows 8–10 chips before scroll |
| Wide | > 1440px | Grid expands to 5 columns; max-width container centered at 1440px; hero scales to 420px with larger display-xl headline |

### Touch Targets

- All add-to-cart buttons maintain a minimum 44px hit area even in compact card views
- Category chips set minimum height 36px to be thumb-friendly in horizontal scroll
- Nav links in mobile hamburger menu expand to 48px row height with full-width tap zone
- Badge overlays are display-only; they do not need touch targets

### Collapsing Strategy

- Primary nav collapses to hamburger at < 744px; the top utility bar remains visible (shrinks to 30px)
- Category chip row becomes a single horizontal scrollable row at all breakpoints — never wraps to grid
- Product card image container maintains 1:1 aspect ratio at all breakpoints via padding-top trick or aspect-ratio CSS
- Price and title remain visible at all sizes; description text (if present) is truncated to 2 lines on card

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; the #118811 green is inferred as primary from extracted palette distinctiveness
- Muli is listed in font stacks but exact weight variants loaded (400/600/700/800) could not be confirmed from extraction — using logical weight assignments based on Muli's published weight range
- No specific border-radius values could be extracted from CSS; `{rounded.xs}` (4px) is inferred from Shopify theme conventions and the hard-edge product photography aesthetic
- Icon system (product category icons, cart, wishlist, social icons) not observable from extraction — assume SVG icon font or inline SVGs in brand green
- Exact nav bar height and mobile breakpoints not confirmed; values above match common Shopify theme defaults
- No dark-mode variant detected; site appears light-only with dark nav strip
- Animation/transition timing (hover states, cart drawer slide-in) not extractable from static scan
