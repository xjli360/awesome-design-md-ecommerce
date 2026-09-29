---
version: alpha
name: "12x12 Cardstock Shop"
source_url: "https://www.12x12cardstock.shop"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Scrolling the shop makes the product immediately legible as the palette itself — candy pink (#ffc0cb), signal red (#ff0000), royal purple (#6a0dad), kraft brown (#964b00), buttercup yellow (#ffff00) — the extracted hex list reads less as a brand color system than as a warehouse inventory of paper reams organized by hue. The interface exists to frame that polychromatic catalog without competing with it. A warm sand tone (#d9bb92) — the color of actual unbleached cardstock — runs through promotional surfaces and hero banners; a lighter parchment field (#f1e5b8) provides the softest content backdrop. The single interactive accent is a clear steel blue (#4195b6, confirmed as meta theme-color), anchoring every CTA, cart action, and filter-active state so the product rainbow can dominate without chrome interference. Outfit handles all UI and body weight — its rounded geometric forms feel modern and approachable without tipping into childish, which suits an adult hobbyist community that takes paper crafting seriously. Tenor Sans steps in for editorial display copy: hero headers and promotional banners benefit from its narrower elegant proportions, lending a stationery-shop refinement that separates the brand from bulk-commodity paper suppliers. Product cards use a gentle {rounded.md} radius on a white {colors.surface-card} ground; color-swatch filter chips take full pills ({rounded.full}) because they replicate the physical experience of flipping through paper chip books. Navigation chrome stays deliberately light — {colors.canvas} headers, {colors.surface-soft} sidebars — so that when a 48-count rainbow grid of paper swatches loads, nothing structural competes. Sale and promo callouts use a warm amber (#e2a764) that reads as inviting heat against the cooler blue primary. The shop's real design language lives in its taxonomy: papers organized by color family, weight, finish, and cut size in deep filter trees, so the UI's primary job is information architecture, not spectacle.

colors:
  primary: "#4195b6"
  primary-active: "#2b6bb0"
  primary-disabled: "#939799"
  ink: "#0f0f0f"
  body: "#323232"
  muted: "#676e72"
  hairline: "#d3d3d3"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  brand-sand: "#d9bb92"
  brand-parchment: "#f1e5b8"
  brand-amber: "#e2a764"
  accent-orange: "#f47d32"
  link: "#0192b5"
  dark-text: "#444444"
  border-medium: "#dedede"

typography:
  display-xl:
    fontFamily: "'Tenor Sans', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Tenor Sans', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Tenor Sans', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Outfit', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Outfit', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Outfit', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Outfit', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Outfit', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Outfit', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Outfit', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  label-caps:
    fontFamily: "'Outfit', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Outfit', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "'Outfit', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'Outfit', sans-serif"
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
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 38px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.border-medium}"
    borderHover: "1px solid {colors.primary}"
    padding: "{spacing.md}"
    imagePlaceholder: "{colors.surface-soft}"
  color-swatch-filter:
    rounded: "{rounded.full}"
    size: 28px
    border: "2px solid transparent"
    borderSelected: "2px solid {colors.primary}"
    outlineOffset: 2px
    tapTarget: 44px
  paper-weight-badge:
    backgroundColor: "{colors.brand-parchment}"
    textColor: "{colors.dark-text}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  sale-badge:
    backgroundColor: "{colors.brand-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  hero:
    backgroundColor: "{colors.brand-sand}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
    minHeight: 400px
  promo-banner:
    backgroundColor: "{colors.brand-parchment}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent-orange}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.brand-sand}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    sectionHeaderTypography: "{typography.title-sm}"
    itemTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    overlayColor: "rgba(0,0,0,0.45)"
    width: 380px
    borderLeft: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    linkColor: "{colors.link}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Steel blue (#4195b6) fill with white text at 15px/600-weight Outfit, 44px tall, {rounded.sm} corners, 12px vertical padding. Hover/active darkens to {colors.primary-active} (#2b6bb0); disabled state falls to {colors.primary-disabled} (#939799). Used for "Add to Cart," checkout CTAs, and filter confirmation actions — the only place in the interface where the blue runs at full saturation.

**`button-secondary`** — White fill with a 1.5px {colors.primary} border and {colors.primary} text. Matches primary height and radius. Used for "View Details," wishlist saves, and secondary panel actions where a filled button would pull focus away from product color swatches.

**`button-ghost`** — Transparent background, {colors.body} text, {rounded.xs} radius. No border. Used inside filter panels and dropdowns for low-emphasis actions like "Clear All" or "Reset Filters." Never competes visually with the swatch grid.

### Inputs & Search
**`text-input`** — White canvas, 1px {colors.hairline} border that sharpens to 1.5px {colors.primary} on focus, 44px height, {rounded.sm}. Placeholder in {colors.muted}. Used across checkout forms, account fields, and filter text searches. Error state border uses {colors.primary-active} with a small caption below in {typography.caption}.

**`search-bar`** — Full pill shape ({rounded.full}) on a {colors.surface-soft} tinted background. Lighter visual weight than the CTA buttons draws the eye to it first on page load. Sits center-aligned in the nav bar on desktop; expands to full width below the nav header on mobile.

### Navigation
**`nav-bar`** — White canvas, 64px tall, with a 1px {colors.hairline} bottom separator. Logo flush left, search bar center or right depending on breakpoint, cart icon and account icon at the far right. All nav links in 14px/500 Outfit ({typography.nav-link}). A slim {promo-banner} strip above the nav carries shipping thresholds; it collapses on mobile to preserve vertical space.

**`breadcrumb`** — Rendered in {typography.caption} below the nav on collection and product pages. Separator uses a forward slash in {colors.hairline}; all ancestor nodes in {colors.muted}; the current page in {colors.ink}. Anchors users navigating the brand's deep paper taxonomy (e.g., Shop → Cardstock → Blue → 65 lb).

### Product Card
**`product-card`** — White card, 1px {colors.border-medium} border at rest (shifts to {colors.primary} on hover), {rounded.md} corners, {spacing.md} padding. Product image fills the top ~60% of the card with {colors.surface-soft} as placeholder. Below the fold: paper name in {typography.title-sm}, a {paper-weight-badge} inline, and price in {typography.price-display}. On hover or keyboard focus a full-width {button-primary} "Add to Cart" appears at the card bottom. Compare price (if on sale) renders in {typography.price-compare} with strikethrough and a {sale-badge} overlaid top-left of the image.

### Color Swatch Filter
**`color-swatch-filter`** — The signature UI element. 28px circular chips, each filled with the exact paper hex (e.g., #ff0000 for Red, #6a0dad for Purple). Unselected chips have a transparent outline; selected chips show a 2px {colors.primary} ring with 2px offset so the chip color remains fully visible. Color families label rows: Red, Orange, Pink, Purple, Blue, Teal, Green, Yellow, Gold, Neutral, Brown, Black, White. Chips pad to a 44px tap target on touch. This replicates the physical act of flipping paper chip books — the most direct product-navigation metaphor in the store.

### Badges
**`paper-weight-badge`** — {colors.brand-parchment} background, {colors.dark-text} text, {typography.label-caps} (11px/700 uppercase Outfit), {rounded.xs}. Displays values like "65 LB," "80 LB," "110 LB" inline in product cards and search results. The parchment fill connects visually to the paper product category.

**`sale-badge`** — Warm amber (#e2a764) background, {colors.ink} text, same {typography.label-caps} and {rounded.xs}. Overlaid top-left on product images at grid scale. Amber reads as warm and promotional without the alarm of pure red.

**`new-badge`** — {colors.primary} fill, {colors.on-primary} white text, same label-caps and radius. Applied alongside or instead of {sale-badge} on newly listed SKUs. The consistent badge system (same size, radius, type scale) keeps the product grid visually clean regardless of how many badges are active.

### Category Pills
**`category-pill`** / **`category-pill-active`** — Full-pill filter tags ({rounded.full}) representing paper categories, sizes, cut formats, and finish types. Inactive: {colors.surface-soft} background, {colors.hairline} border, {colors.body} text. Active: {colors.primary} fill, white text. On desktop, pills wrap in a row above the product grid; on mobile they collapse into a single horizontal scroll strip with no wrapping.

### Hero
**`hero`** — Full-width section on {colors.brand-sand}. Heading in {typography.display-xl} Tenor Sans at 40px/400 weight — the brand's only serif moment; subhead or promo copy in {typography.body-md} Outfit. Minimum 400px height. CTA is {button-primary}. The sand background anchors the paper-product identity without requiring lifestyle photography; the brand's color vocabulary IS the product.

### Promo Banner
**`promo-banner`** — Slim strip above the nav on {colors.brand-parchment}. Body-sm Outfit text carries shipping thresholds ("FREE SHIPPING ON ORDERS $49+") and discount codes; emphasis spans in {colors.accent-orange} highlight threshold amounts and code strings. Collapses to hidden at mobile breakpoints where vertical space is constrained.

### Filter Sidebar
**`filter-sidebar`** — White panel, 1px {colors.hairline} border, {rounded.sm} corners, {spacing.base} internal padding. Section headers in {typography.title-sm} 600-weight Outfit; individual filter options in {typography.body-sm}. Color family rows use {color-swatch-filter} chips; weight, size, and finish use standard checkbox rows at 44px tap height. On mobile, the sidebar promotes to a bottom sheet triggered by a sticky "Filters" pill button above the product grid.

### Cart Drawer
**`cart-drawer`** — Right-side slide-in panel at 380px width, white background, left border 1px {colors.hairline}. A 45% dark scrim covers the page behind. Title in {typography.title-md}; line items show a small square product thumbnail, name in {typography.title-sm}, {paper-weight-badge} inline, quantity stepper, and line price in {typography.price-display}. Footer carries order subtotal and a full-width {button-primary} "Proceed to Checkout" CTA.

### Footer
**`footer`** — {colors.surface-soft} background, 1px {colors.hairline} top border, {spacing.xxl} vertical padding. Four-column layout on desktop (Shop, Customer Service, About, Social). Column heads in {typography.title-sm} 600-weight; links in {typography.body-sm} with {colors.link} color (#0192b5). Bottom row carries copyright line, payment method icons, and any trust badges in {typography.caption}.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + search icon + cart icon; filter sidebar becomes full bottom sheet; promo banner hidden; search expands full-width below nav; category pills become horizontal scroll strip |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + search + cart; filter sidebar collapses to left panel toggled by a "Filter" button above grid; hero heading scales to {typography.display-md} |
| Desktop | 1128–1440px | Three-column product grid; full nav with category links visible; persistent filter sidebar left of grid; hero at full {typography.display-xl}; promo banner always visible |
| Wide | > 1440px | Content max-width ~1400px, centered with auto margins; four-column product grid; hero gains additional vertical padding |

### Touch Targets
- Color swatch chips: 28px visual size padded to minimum 44×44px tap target
- All button variants minimum 44px height
- Nav icons (hamburger, search, cart, account) minimum 44×44px
- Filter checkbox rows and pill tags minimum 44px tap height
- Quantity stepper buttons in cart drawer minimum 44×44px

### Collapsing Strategy
- Promo banner collapses first at < 744px to preserve nav height budget
- Filter sidebar converts to bottom sheet at < 744px; triggered by a sticky "Filters" pill above the product grid
- Primary nav condenses to hamburger at < 744px; category link labels hidden
- Category pill row switches from wrapping row to horizontal scroll at < 744px, no wrapping
- Product grid: 4 col (Wide) → 3 col (Desktop) → 2 col (Tablet) → 1 col (Mobile)
- Hero CTA button switches from inline to full-width at < 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No animation or transition timing values captured — easing curves for cart drawer slide-in, filter panel expand, hover state fades, and swatch selection ring are unknown
- Exact mobile nav height not confirmed; 64px is estimated from desktop observation
- No icon system identified — whether the brand uses an SVG sprite, icon font, or inline SVGs is not determinable from extracted data
- Typography above 40px (possible hero-scale Tenor Sans at 48–56px) may exist for wide-viewport hero banners; extraction did not capture responsive CSS at full resolution
- Exact gap and row spacing within the color swatch chip grid not extracted
- Product page layout (image carousel vs. thumbnail strip vs. zoom overlay) not confirmed
- Loyalty program, points badge, or rewards tier styling not detected in extraction
- Dark mode tokens: none detected; assumed light-mode only
- Price formatting edge cases (bundle pricing, per-sheet pricing, bulk tier breaks) not captured in visual extraction
- Cart upsell or cross-sell module styling (commonly "You might also like" in craft stores) not confirmed
