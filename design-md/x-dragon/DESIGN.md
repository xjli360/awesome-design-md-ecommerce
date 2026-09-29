---
version: alpha
name: "X-Dragon"
source_url: "https://www.x-dragon.net"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Solar panels stitched directly into nylon clamshell cases — X-Dragon's flagship products harvest sunlight and route it into phone batteries, and the brand's visual identity operates on the same output-first logic: extract maximum signal from minimum surface. The name carries a mythology of raw power, and the design language earns it through high-contrast staging — near-black canvases, white ink at full opacity, and a charging-LED orange (#f47c20) that functions as the single brand voltage across every primary CTA, spec badge, and UI accent. The palette is not warm or inviting; it is alert. Every product photograph implies darkness interrupted by illumination — the glow of a charging indicator in a tent, on a trail, at the bottom of a bag — which explains why the brand reaches for orange rather than the cool blues that dominate consumer electronics. Type almost certainly runs in a grotesque or geometric sans: the category demands legibility at small sizes when communicating wattage, panel count, and capacity in mAh within tight product card real estate. Display sizes run heavy at 700–800 weight, reinforcing an engineering-first posture, while body copy sits at regular weight with slightly open tracking to keep dense spec language readable on mobile screens. No serifs anywhere; this is a tools brand, not a lifestyle brand. Component shapes lean industrial-modern: rounded corners exist at {rounded.sm} to {rounded.md} — enough to read as contemporary consumer product, not enough to feel precious. The primary CTA button carries orange against a dark surface, creating a focal-point hierarchy that routes the eye to "Add to Cart" or "Buy Now" before the user has finished scanning. Product cards are vertically stacked and photography-first, with a spec strip below the image in {typography.spec-label} — wattage, port count, panel size — before price in {typography.price-display} at 800 weight. Navigation is shallow and categorical: Solar Chargers, Power Banks, Phone Cases, Cables, with a persistent cart icon and search trigger. No editorial content competes with the product grid. The buyer is typically researching on a phone while traveling, which drives every mobile-first density decision: sticky add-to-cart bars on PDPs, single-column grids at 375px, and horizontally scrolling category tabs that keep the entire product taxonomy within one thumb reach. Spec tables use {colors.hairline} rows on {colors.surface-soft} backgrounds, keeping dense technical grids legible without visual noise. The footer anchors brand legitimacy through warranty terms, FCC/CE compliance badges, and certification marks — buyers at this price point are vetting the brand as much as the product.

colors:
  primary: "#f47c20"
  primary-active: "#d4620e"
  primary-disabled: "#7a4010"
  ink: "#ffffff"
  body: "#e0e0e0"
  muted: "#8a8a8a"
  hairline: "#2a2a2a"
  hairline-soft: "#1f1f1f"
  canvas: "#0f0f0f"
  surface-soft: "#1a1a1a"
  surface-card: "#222222"
  surface-raised: "#2c2c2c"
  on-primary: "#ffffff"
  spec-highlight: "#f47c20"
  error: "#e53e3e"
  success: "#38a169"

typography:
  display-xl:
    fontFamily: "'Inter', 'DIN Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 40px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', 'DIN Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Inter', 'DIN Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', 'DIN Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'DIN Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'DIN Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01px
  body-sm:
    fontFamily: "'Inter', 'DIN Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.01px
  spec-label:
    fontFamily: "'Inter', 'DIN Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  caption:
    fontFamily: "'Inter', 'DIN Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', 'DIN Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', 'DIN Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Inter', 'DIN Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  price-display:
    fontFamily: "'Inter', 'DIN Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.3px

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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-buy-now:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 56px
    width: "100%"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoAccentColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    iconColor: "{colors.muted}"
    iconFocusColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    padding: 10px 14px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    imageAspect: "1/1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    specTypography: "{typography.spec-label}"
    specColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderHover: "1px solid {colors.primary}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    accentColor: "{colors.primary}"
    padding: "{spacing.section} {spacing.xl}"
    imagePosition: "right"
    ctaVariant: "button-primary"
  category-tab:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    activeTextColor: "{colors.primary}"
    activeBorderBottom: "2px solid {colors.primary}"
    padding: "{spacing.md} {spacing.base}"
    rounded: "{rounded.none}"
    height: 44px
  spec-badge:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.spec-highlight}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    border: "1px solid {colors.primary}"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  spec-table-row:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.base}"
  sticky-cart-bar:
    backgroundColor: "{colors.surface-card}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.base}"
    position: "fixed"
    bottom: 0
    width: "100%"
    ctaVariant: "button-buy-now"
  trust-badge-row:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    iconColor: "{colors.primary}"
    typography: "{typography.caption}"
    gap: "{spacing.xl}"
    padding: "{spacing.lg} 0"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkColor: "{colors.body}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The brand's primary voltage: #f47c20 orange fill on the near-black canvas, 48px tall with {rounded.sm} corners and 28px horizontal padding. It is the highest-contrast element in any viewport and should appear exactly once per screen as the dominant action. The active state darkens to #d4620e on press; the disabled state collapses to #7a4010 fill with {colors.muted} text, preserving the dark-field relationship without introducing an anomalous light surface.

**`button-buy-now`** — A full-width, 56px-tall variant of the primary button reserved for product detail page CTAs and the mobile sticky cart bar. The extra 8px of height is a deliberate touch-target investment at the moment of purchase commitment — the single highest-stakes tap in the entire funnel.

**`button-secondary`** — Transparent background with a 1px {colors.hairline} border and {colors.ink} white label text, matching button-primary in height and padding. Deployed for secondary actions like "Add to Wishlist" or "Compare," always adjacent to a primary CTA so the hierarchy is unambiguous.

### Navigation

**`nav-bar`** — 64px tall, {colors.canvas} background with a 1px {colors.hairline} bottom border separating it from the product grid below. The X-Dragon wordmark or logomark anchors the left edge in {colors.primary} orange, functioning as both brand identifier and homepage return. Category links run in {typography.nav-link} — 14px, uppercase, 600 weight, tracked — in {colors.body} gray that brightens to {colors.ink} white on hover. A cart icon with an orange item-count dot sits at the far right.

**`category-tab`** — A horizontally scrollable strip rendered below the nav-bar, encoding the four to five top-level product categories. Inactive tabs read in {colors.muted}; the active tab acquires {colors.primary} text and a solid 2px {colors.primary} bottom border that visually roots the selected state without additional chrome. Minimum tap height is 44px.

### Product Card

**`product-card`** — Dark {colors.surface-card} fill with a 1px {colors.hairline} border that upgrades to a 1px {colors.primary} border on hover, turning the grid into a browsable field of orange-lit selections. The image occupies a square 1:1 aspect ratio at the top of the card; below it a spec strip in {typography.spec-label} uppercase {colors.muted} surfaces key attributes (wattage, mAh, port count), then the product name in {typography.title-sm}, then price in {typography.price-display} at 800 weight. Rounded at {rounded.md}. Spec badges float in the top-left corner of the image, new-badges in the top-right.

### Search

**`search-bar`** — Inline in the nav-bar on desktop; on mobile it collapses to a search icon that triggers a full-width overlay input. The field is {colors.surface-card} fill with a 1px {colors.hairline} border that activates to 1px {colors.primary} on focus. Placeholder in {colors.muted}; the magnifier icon also shifts to {colors.primary} on focus, giving a two-point visual confirmation of the active state.

### Hero

**`hero-banner`** — Full-bleed {colors.canvas} section with the product headline in {typography.display-xl} at 800 weight; subheadline in {typography.body-md} at {colors.body}. On desktop the product image sits right-aligned, often a hard-lit shot of the charger against a gradient or environmental backdrop; on mobile, image stacks above copy. The `button-primary` CTA sits below the subheadline. Optional graphic accents — lightning arc, charge-level indicator — render in {colors.primary} orange, reinforcing the energy system.

### Badges

**`spec-badge`** — A small, high-information label in {colors.surface-raised} with {colors.spec-highlight} text and a 1px {colors.primary} border, applied inline on product cards and PDPs to foreground the most decision-relevant specs: "20W Fast Charge," "26800mAh," "4 Solar Panels." Typography is {typography.spec-label} — 12px, uppercase, 700 weight, 0.5px tracked — ensuring legibility at badge scale.

**`new-badge`** — Solid {colors.primary} fill with {colors.on-primary} white text in {typography.spec-label}, applied to the top-right corner of product card images for recent releases. The fill is deliberately identical to the primary button, linking newness with urgency in the same brand token.

### Spec Table

**`spec-table-row`** — Hairline-separated rows on {colors.surface-soft}, each row carrying a {colors.muted} spec label in {typography.spec-label} on the left and a {colors.body} value in {typography.body-sm} on the right. The dark-surface alternating treatment keeps dense technical grids scannable without introducing color complexity. This component is the primary trust-building mechanism on product detail pages, where wattage, dimensions, weight, and certifications convert skeptical buyers.

### Sticky Cart Bar

**`sticky-cart-bar`** — Fixed to the viewport bottom on mobile PDPs, with {colors.surface-card} background and a 1px {colors.hairline} top border. Contains price at {typography.price-display} on the left and the full-width `button-buy-now` CTA filling the right portion. It disappears on desktop where the sidebar layout keeps the add-to-cart zone in the viewport without assistance.

### Trust Badges

**`trust-badge-row`** — A horizontal row of 3–4 icon-and-label pairs (Solar Certified, 18-Month Warranty, FCC/CE, Free Returns) in {colors.muted} text with {colors.primary} icons at {typography.caption} scale. Appears below the add-to-cart zone on PDPs and above the footer on the homepage. The orange icons are the only decorative use of the brand color outside of interactive elements — a deliberate signal that these guarantees are as load-bearing as a CTA.

### Footer

**`footer`** — {colors.surface-soft} background with a 1px {colors.hairline} top border and {spacing.section} vertical padding. Link text in {colors.body}, ambient copy and legal text in {colors.muted}, all at {typography.caption} scale. Desktop renders a four-column grid (Shop, Support, Legal, Social); compliance badges (CE, FCC, RoHS) sit in a bottom strip, reinforcing the legitimacy signal that the trust-badge-row began.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer + persistent cart icon; category-tabs horizontally scroll below nav; sticky-cart-bar activates on PDP; hero image stacks above copy; footer becomes accordion |
| Tablet | 744–1128px | Two-column product grid; nav shows primary categories inline with overflow; hero runs side-by-side layout; footer two-column; sticky-cart-bar hidden |
| Desktop | 1128–1440px | Three-to-four-column product grid; full horizontal nav with inline search-bar; spec-table full width; PDP uses two-column layout with sticky sidebar CTA; footer four-column |
| Wide | > 1440px | Content max-width ~1400px centered; four-column grid maintained; hero gains extra horizontal padding; nav-bar gains additional breathing room on both edges |

### Touch Targets
- All buttons minimum 48px height; `button-buy-now` at 56px for the primary conversion moment
- Category tabs minimum 44px tap height with {spacing.base} horizontal padding regardless of visual label height
- Nav icons (search, cart, hamburger) minimum 44×44px touch area via padding
- Spec badges and trust-badge icons minimum 32px touch target enforced with padding expansion

### Collapsing Strategy
- Nav: full horizontal with search on desktop → primary categories inline, hamburger for overflow on tablet → full hamburger drawer on mobile; cart icon always persistent
- Product grid: 4-col at wide → 3-col desktop → 2-col tablet → 1-col mobile
- Hero: image-right side-by-side on desktop/tablet → image-above stacked on mobile below 744px
- Spec table: full-width table on desktop → horizontally scrollable at mobile below 480px
- Footer: 4-column grid → 2-column at tablet → per-section accordion at mobile
- Search: inline in nav-bar on desktop/tablet → icon-triggered full-screen overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site — all palette values are inferred from publicly observable brand positioning and tech-accessories category conventions, not confirmed extraction; actual brand colors may differ substantially
- No font stacks were detected — typography spec uses Inter/DIN Next/system-sans as the most probable choice for a tech-accessories DTC brand; actual typeface may be licensed or custom
- No meta theme-color was present, suggesting either a dark-mode preference or absent PWA configuration
- Exact border-radius values unconfirmed — all {rounded.*} assignments are category-conventional estimates
- Brand may operate a light-canvas variant for informational pages (warranty, about, returns); this spec assumes dark canvas as the primary product-facing surface
- No logo SVG or wordmark extracted; logo color ({colors.primary} orange) is inferred from naming convention and product photography tendencies
- Promotional palette (sale red, clearance orange vs. standard orange) not confirmed; error/success tokens are generic web defaults
- No animation, transition timing, or hover-state duration data available
- Rating or review UI patterns not confirmed; brand may source reviews from Amazon or third-party widgets with their own design language
