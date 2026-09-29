---
version: alpha
name: "Russell+Hazel"
source_url: "https://www.russellandhazel.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Russell+Hazel opens with a color bet most office brands won't take — a deep sea-glass teal (#108474) owns every primary action (add-to-cart, active nav states, announcement bars) while a coral-red jolt (#f04f36) handles promotions and urgency marks, logic borrowed from editorial art direction rather than office-supply convention. The canvas holds at white with warm-neutral surfaces at #f6f6f6 and #f4f4f4, and ink sits at near-black #1d1d1d rather than pure black, softening the page without losing contrast. Typography divides along a serif/sans axis: Baskerville and Caslon govern hero headlines and editorial display moments — their curved letterforms signal that a wire-coil notebook or an acrylic tray is an object worth a second look — while Libre Franklin and Montserrat carry the UI and button layer in spaced uppercase labels at weight 700, producing a reading tone closer to a design magazine than a stationery catalog. Color swatches are a first-class UI component: desk accessories in fourteen colorways mean the selected-state ring ({rounded.full} chip, {colors.ink} outline, 2px offset) does as much selling work as the product copy itself. The announcement bar at {colors.primary} with white uppercase Montserrat claims the full viewport width before navigation loads, concentrating attention on shipping thresholds and seasonal promotions. Product cards stay minimal — a soft {colors.surface-card} image field, title in {typography.title-sm}, price in {typography.price}, and a short color-swatch row — letting product photography carry visual weight. Rounded values stay conservative: {rounded.xs} (4px) on buttons, inputs, and cards keeps the grid precise and slightly more editorial than friendly. The footer inverts to {colors.ink} with muted #939393 link text that hovers to white, closing the page with visual weight proportional to the brand's confidence in its product line.

colors:
  primary: "#108474"
  primary-active: "#046e82"
  primary-disabled: "#84c4bb"
  accent: "#f04f36"
  accent-hover: "#f2614a"
  ink: "#1d1d1d"
  body: "#4d4d4d"
  muted: "#7b7b7b"
  muted-soft: "#939393"
  hairline: "#e6e6e6"
  hairline-soft: "#ededed"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#f4f4f4"
  surface-warm: "#f9fafb"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  mint-surface: "#ecfef0"
  success: "#56ad6a"
  error: "#cc1313"
  error-muted: "#ba4444"
  link: "#4a9afc"
  warm-gray: "#a5a8a9"

typography:
  display-xl:
    fontFamily: "Baskerville, Caslon, Garamond, Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Baskerville, Caslon, Garamond, Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Baskerville, Caslon, Garamond, Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Libre Franklin', Montserrat, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Libre Franklin', Montserrat, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Libre Franklin', Montserrat, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Libre Franklin', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Libre Franklin', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  price:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price-lg:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "Montserrat, 'Libre Franklin', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "Montserrat, 'Libre Franklin', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Libre Franklin', Montserrat, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  announcement:
    fontFamily: "Montserrat, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  label-sm:
    fontFamily: "Montserrat, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    border: "1.5px solid {colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.mint-surface}"
    border: "1.5px solid {colors.primary}"
    textColor: "{colors.primary}"
    rounded: "{rounded.xs}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1.5px solid {colors.primary}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 72px
    logoArea: 160px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.announcement}"
    padding: 10px 16px
    height: 40px
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.surface-card}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.caption}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageRounded: "{rounded.xs}"
    padding: 0 0 16px 0
    gap: "{spacing.sm}"
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    selectedOutlineColor: "{colors.ink}"
    selectedOutlineOffset: 2px
    selectedOutlineWidth: 1.5px
    gap: "{spacing.xs}"
  color-swatch-lg:
    size: 32px
    rounded: "{rounded.full}"
    selectedOutlineColor: "{colors.primary}"
    selectedOutlineOffset: 3px
    selectedOutlineWidth: 2px
    gap: "{spacing.sm}"
  promo-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-bestseller:
    backgroundColor: "{colors.mint-surface}"
    textColor: "{colors.primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    titleColor: "{colors.ink}"
    subtitleColor: "{colors.body}"
    padding: 80px 64px
    minHeight: 520px
    textMaxWidth: 560px
  category-tile:
    backgroundColor: "{colors.surface-card}"
    titleTypography: "{typography.title-md}"
    labelTypography: "{typography.label-sm}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageRounded: "{rounded.xs}"
    hoverScale: 1.02
    transitionDuration: 200ms
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    iconColor: "{colors.muted}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    headerTypography: "{typography.title-md}"
    itemTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    textColor: "{colors.ink}"
    borderLeft: "1px solid {colors.hairline}"
    width: 420px
  product-detail-form:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-md}"
    priceTypography: "{typography.price-lg}"
    labelTypography: "{typography.label-sm}"
    textColor: "{colors.ink}"
    gap: "{spacing.lg}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    buttonWidth: 44px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.canvas}"
    padding: 64px 0 40px 0

## Components

### Buttons
**`button-primary`** — Teal-filled (`{colors.primary}`) with white text, all-caps Montserrat 700 at 1px letter-spacing, 4px radius (`{rounded.xs}`), 48px tall. Active state deepens to `{colors.primary-active}` (#046e82); disabled uses `{colors.primary-disabled}` at 60% opacity. This button carries add-to-cart, checkout, and primary form submissions — the coral accent (#f04f36) is never used for primary CTA fill, reserved strictly for badges and promotions.

**`button-secondary`** — 1.5px `{colors.primary}` border on a `{colors.canvas}` background, same uppercase Montserrat type. Hover state fills with `{colors.mint-surface}` (#ecfef0), reinforcing teal brand family. Applied to secondary actions: "Save to Wishlist," "Compare," "View All in Collection."

**`button-text`** — Transparent with underlined `{typography.button-sm}` in `{colors.ink}`. Used for tertiary navigation links where a bordered button would over-weight the hierarchy.

### Text Inputs
**`text-input`** — 48px field, 1px `{colors.hairline}` border thickening to 1.5px `{colors.primary}` on focus, placeholder in `{colors.muted}`, `{rounded.xs}` (4px). Applied to email capture, coupon entry, address fields, and quantity inputs not handled by `quantity-selector`.

### Navigation
**`nav-bar`** — 72px white bar with a 1px `{colors.hairline}` bottom border. Logo lockup in the left 160px; category links in `{typography.nav-link}` (Libre Franklin 13px/500) with a `{colors.primary}` underline on the active state. Cart, search, and account icons sit right-aligned with 48px tap targets. On scroll past the hero, the bar gains a soft box-shadow to lift from content.

**`announcement-bar`** — Full-width `{colors.primary}` strip, 40px tall, sitting above the nav. Copy in `{typography.announcement}` (Montserrat 13px/600, 0.8px tracking, uppercase). Carries free-shipping thresholds, promo codes, and seasonal callouts. A white dismiss icon clears it for the session without page reload.

### Product Cards
**`product-card`** — Minimal card: `{colors.surface-card}` image container with 4px rounding, product name in `{typography.title-sm}` (Libre Franklin 15px/600), price right of name or below in `{typography.price}`, and a `color-swatch` chip row showing available colorways. No card border — background contrast and whitespace create separation. On hover, a translucent quick-add overlay fades in over the image at the bottom edge.

**`color-swatch`** — 20px circular chips (`{rounded.full}`) at 4px gaps. Selected chip shows a 1.5px `{colors.ink}` outline ring with 2px offset. On product detail pages, `color-swatch-lg` (32px chips, `{colors.primary}` selected ring, 3px offset) is used instead. Color name surfaces in a tooltip or adjacent text label — chips carry no visible text.

### Badges
**`promo-badge`** — `{colors.accent}` (#f04f36) background, white `{typography.label-sm}` (10px/700, uppercase, 1.2px tracking), `{rounded.xs}`. Applied to sale prices and clearance. **`badge-new`** uses `{colors.ink}` fill for new arrivals. **`badge-bestseller`** uses `{colors.mint-surface}` background with `{colors.primary}` text — a teal-family signal that reads warm rather than urgent, appropriate for evergreen top-sellers rather than time-limited events.

### Hero
**`hero-banner`** — `{colors.surface-soft}` fill or full-bleed photography background; headline in `{typography.display-xl}` (Baskerville 48px/400), subtitle in `{typography.body-md}` (Libre Franklin 16px/400). Text block is max 560px wide and left-aligned with 80px vertical padding. CTA row below copy typically pairs a `button-primary` and `button-secondary` at 16px gap.

### Category Grid
**`category-tile`** — Square image card on `{colors.surface-card}`, title in `{typography.title-md}` below the image, optional `{typography.label-sm}` category label above. On hover, image scales to 1.02× over 200ms — a gentle lift that invites without aggressive zoom.

### Search
**`search-bar`** — Pill-shaped (`{rounded.full}`) field on `{colors.surface-soft}` with a leading magnifier icon in `{colors.muted}`. On mobile, tapping opens a full-screen overlay with a back button. On desktop, a dropdown appears below showing product thumbnails, collection names, and a "See all results" link at the bottom.

### Cart
**`cart-drawer`** — 420px slide-in panel from the right. "Your Cart" heading in `{typography.title-md}`; each line item in `{typography.body-sm}` with product color and size in `{typography.caption}` below the title, price right-aligned in `{typography.price}`. Quantity controlled by `quantity-selector`. Full-width `button-primary` at the bottom is the checkout CTA.

### Product Detail
**`product-detail-form`** — Product name in `{typography.display-md}` (Baskerville 28px/400), price in `{typography.price-lg}` (Libre Franklin 22px/600). Color label in `{typography.label-sm}` above the `color-swatch-lg` row, then quantity and add-to-cart stacked at `{spacing.lg}` gaps. Description text in `{typography.body-md}`.

### Footer
**`footer`** — Inverted `{colors.ink}` panel with four-column link groups in `{typography.body-sm}` at `{colors.muted-soft}` (#939393), lifting to `{colors.canvas}` on hover. Column headings in `{typography.title-sm}` (Libre Franklin 15px/600) in `{colors.on-dark}`. Bottom strip holds legal copy in `{typography.caption}` at `{colors.muted-soft}` and a social icon row.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart; announcement bar wraps to two lines if needed; hero text centered; cart drawer fills full viewport width |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories inline with sub-navigation in a slide-in mega-menu drawer; hero splits image and text side-by-side |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with hover mega-menu panels; search bar expands inline; hero is full-bleed with text overlay |
| Wide | > 1440px | Grid max-width caps at 1440px with 80px gutters; hero images scale to fill but text block stays at 560px max; no layout changes beyond centering |

### Touch Targets
- All interactive elements maintain a 44px minimum touch target height; icon-only buttons get 48×48px tap areas regardless of visible icon size
- `color-swatch` automatically upgrades to `color-swatch-lg` (32px chips) on mobile to meet touch requirements
- Quantity selector buttons are 44px wide on mobile; the full row is 44px tall

### Collapsing Strategy
- Navigation: top-level categories collapse to a hamburger drawer on mobile; mega-menu sub-categories and featured products move into an accordion inside the drawer
- Product filters: sidebar filter panel collapses to a bottom-sheet modal on mobile, triggered by a "Filter & Sort" button in the grid toolbar
- Footer: four-column layout stacks to a single column on mobile; each column heading becomes an accordion toggle to contain scroll depth
- Announcement bar: always visible; copy wraps naturally on narrow viewports rather than truncating promotional message

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `primary-disabled` (#84c4bb) is derived by lightening `#108474` — not directly observed in the extracted palette; actual disabled teal may differ
- Specific Baskerville/Caslon usage confirmed only from font-family stack presence — precise display sizes, weights, and where serif versus sans-serif is deployed were not extractable from live-site inspection
- No motion or animation tokens observed — hover durations, easing curves, and page-transition behavior in `category-tile` and `cart-drawer` are estimated
- Brand logo lockup treatment (the "+Hazel" script or wordmark style) not confirmed — may be a custom lettered asset rather than a system font from the extracted stack
- Roles for `#ff5268` and `#4a9afc` in the extracted palette are ambiguous — likely a Shopify system color and link color respectively, but could originate from third-party widgets (reviews, loyalty app)
- Whether `#f04f36` or `#f2614a` is the canonical accent fill versus a hover state is not isolatable from extraction alone
- Icon set vendor, stroke weight, and filled-vs-outline style not determinable from extraction
- Mega-menu column layout and hover trigger timing not confirmed — inferred from category depth in page structure
