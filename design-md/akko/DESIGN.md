---
version: alpha
name: "Akko"
source_url: "https://en.akkogear.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep violet current (#6f5cae) runs through Akko's mechanical-keyboard universe, a brand that treats switches and keycaps the way a paint company treats pigment swatches. The primary purple sits across from a navy anchor (#003366) and a near-black ink (#212121), creating a palette that reads as nocturnal and precision-oriented rather than playful or pastel. Typography splits between Poppins for English headers — a geometric sans with open, friendly counters — and Microsoft Yahei for Chinese, reflecting the brand's dual-market identity. Product photography dominates: keyboard builds shown in exploded views, switch stems exposed, keycap profiles rendered in cross-section. The search bar uses a full-pill radius ({rounded.full}) against a dark canvas, and category navigation runs as a horizontal strip of illustrated icons — each switch type (linear, tactile, clicky) gets its own glyph. Badges appear in a secondary purple (#8071b3) for "NEW" flags and in a warm pink (#f78da7) for limited-edition collaborations. The checkout flow swaps the dark theme for a clean white surface-card, suggesting the brand knows when to step back and let the product's own color — a gradient PBT keycap set, a translucent polycarbonate case — do the selling. There is no hero video; instead, the hero is a static 3D render of the latest keyboard, lit from above, with the model number set in Poppins-Medium at 28px. The footer collapses into a single column of small, gray links (#8f9196) — no social icons, no newsletter signup, just support, about, and distributor pages. The entire experience feels like a tool catalog that happens to be beautiful, not a lifestyle brand that happens to sell keyboards.

colors:
  primary: "#6f5cae"
  primary-active: "#5a4a8f"
  primary-disabled: "#b3a8d6"
  ink: "#212121"
  body: "#32373c"
  muted: "#8f9196"
  muted-soft: "#a7a7a7"
  hairline: "#d8d8d8"
  hairline-soft: "#e9e9e9"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  navy: "#003366"
  deep-navy: "#000370"
  accent-purple: "#8071b3"
  accent-pink: "#f78da7"
  accent-orange: "#ff6900"
  accent-green: "#17ac4d"
  badge-new: "#8071b3"
  badge-limited: "#f78da7"
  star-rating: "#ff6900"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Microsoft Yahei', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', 'Microsoft Yahei', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', 'Microsoft Yahei', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Microsoft Yahei', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Microsoft Yahei', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', 'Microsoft Yahei', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', 'Microsoft Yahei', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', 'Microsoft Yahei', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Poppins', 'Microsoft Yahei', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', 'Microsoft Yahei', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', 'Microsoft Yahei', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', 'Microsoft Yahei', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Poppins', 'Microsoft Yahei', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'Microsoft Yahei', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  price:
    fontFamily: "'Poppins', 'Microsoft Yahei', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  price-sale:
    fontFamily: "'Poppins', 'Microsoft Yahei', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
    color: "{colors.accent-orange}"

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: 1px solid "{colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: 1px solid "{colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    border: 1px solid "{colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.accent-orange}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: 1px solid "{colors.hairline}"
  search-bar-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid "{colors.hairline-soft}"
  top-nav-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
    borderBottom: 2px solid "{colors.primary}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: 12px 0
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    borderBottom: 2px solid "{colors.primary}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: 1:1
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    padding: 0 "{spacing.base}" "{spacing.base}" "{spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-hover:
    boxShadow: 0 4px 12px rgba(0,0,0,0.08)
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.xl}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.canvas}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted-soft}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 32px
  badge:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-limited:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.link}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    color: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
  footer-heading:
    color: "{colors.canvas}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.base}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  switch-spec-table:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  switch-spec-label:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  switch-spec-value:
    typography: "{typography.body-sm}"
    color: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Buy Now", and "Pre-order". Renders as a solid purple rectangle with 8px corners, white Poppins-Medium text at 14px. On hover, shifts to `primary-active` (#5a4a8f). Disabled state uses `primary-disabled` (#b3a8d6) with no shadow. **`button-secondary`** — Outlined variant for secondary actions like "View Details" or "Compare". White background with a 1px hairline border, ink text. Active state gains a purple border. **`button-ghost`** — Text-only purple link for "Learn More" or "Read Reviews". No background, no border. **`button-pill-primary`** — Fully rounded pill used for filter tags and "Shop Now" in the category strip. Smaller padding (8px 20px) and smaller type. **`button-pill-outline`** — Outlined pill for "Clear Filters" or deselected filter states.

### Text Inputs & Forms
**`text-input`** — Standard form field with 8px corners, 1px hairline border, 44px height. On focus, the border switches to primary purple. Error state uses orange (#ff6900) border. **`select-input`** — Dropdown selector matching the text-input dimensions and border treatment. Used for switch type filters, sorting, and quantity selectors. **`search-bar`** — Full-pill search input on light backgrounds. White with hairline border. **`search-bar-dark`** — Full-pill search input on dark backgrounds (hero section). Ink background with white text.

### Navigation
**`top-nav`** — Fixed 64px header with white background and soft bottom border. Contains logo (left), nav links (center), and cart/search icons (right). **`top-nav-dark`** — Dark variant used on product pages with dark hero sections. Ink background, white text. **`nav-link`** — Inline navigation items with 8px vertical padding. Active state shows a 2px purple bottom border. **`category-strip`** — Horizontal scrollable strip of category tabs (Keycaps, Switches, Keyboards, Accessories). Each tab is a `category-tab` with muted text; active tab uses ink text and a purple underline.

### Product Cards
**`product-card`** — Square-aspect-ratio card with 12px rounded corners, white background, no border. Contains a 1:1 product image at the top (rounded top corners), title in title-sm, and price in price typography. On hover, a subtle box-shadow lifts the card. **`product-card-badge`** — Small uppercase badge overlaid on the image corner. Purple for "NEW", pink for "Limited", orange for "SALE". **`product-card-badge-limited`** — Pink variant for limited-edition collaborations.

### Hero Section
**`hero-section`** — Full-width dark section (ink background) with white text. Contains a `hero-title` (display-xl), `hero-subtitle` (body-md in muted-soft), and a `hero-cta` button (primary purple). No background image — uses a 3D product render as the visual anchor.

### Badges & Labels
**`badge`** — Small uppercase label with 4px corners. Used for "NEW", "BEST SELLER", "AWARD WINNER". Purple background. **`badge-limited`** — Pink background for "LIMITED EDITION". **`badge-sale`** — Orange background for "SALE" or "% OFF".

### Footer
**`footer`** — Dark section (ink background) with muted gray links. Columns for Support, About, Distributors, and Legal. No social icons. No newsletter signup. Links turn white on hover. **`footer-heading`** — White title-sm labels for each column.

### Dividers
**`divider`** — Full-width 1px hairline line. **`divider-soft`** — Lighter version for subtle separation within cards or sections.

### Switch Spec Table
**`switch-spec-table`** — Light gray surface with 8px corners, used on product detail pages to display switch specifications (actuation force, travel distance, lifespan). Labels in caption/muted, values in body-sm/ink.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Top nav collapses to hamburger menu. Category strip becomes a horizontal scroll. Product cards stack vertically. Footer collapses to single column. Hero section reduces padding to 32px. Search bar moves to a full-width overlay. |
| Tablet | 744–1128px | Two-column product grid. Top nav shows limited links (Shop, Support). Category strip remains scrollable. Footer shows 2 columns. Hero section uses 48px padding. |
| Desktop | 1128–1440px | Three-column product grid. Full top nav with all links visible. Category strip shows all tabs without scroll. Footer shows 4 columns. Hero section uses 64px padding. |
| Wide | > 1440px | Four-column product grid. Max-width container at 1440px. Hero section centers content with larger type. |

### Touch Targets
- All buttons and links: minimum 44px height, 44px width for icon-only targets.
- Search bar: 48px height for easy tapping.
- Category strip tabs: minimum 48px height, 16px horizontal padding.
- Product card: entire card is tappable, minimum 120px height.
- Hamburger menu icon: 44x44px tap area.

### Collapsing Strategy
- Top nav links collapse into a hamburger menu below 744px.
- Category strip collapses from visible tabs to a horizontal scroll on mobile.
- Product grid collapses from 4 columns to 3 to 2 to 1 as viewport shrinks.
- Footer columns collapse from 4 to 2 to 1.
- Hero section reduces vertical padding from 64px to 32px on mobile.
- Search bar moves from inline to full-width overlay on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list contains 30+ colors, many of which appear to be generic web palette colors (blues, grays, and one bright accent per category). The true brand palette likely centers on #6f5cae (purple) and #003366 (navy), but hover states, error states, and disabled states for these colors are inferred from common accessibility patterns — not extracted from the live site.
- Font-family declarations found: Cardo, FontAwesome, Inter, Microsoft Yahei, Poppins, Quicksand. Poppins and Microsoft Yahei are used for the primary typography; Cardo, Inter, and Quicksand may appear in specific contexts (e.g., product descriptions, technical specs) but their usage could not be confirmed.
- No meta theme-color was found — the browser chrome/taskbar color is unknown.
- Dark mode styling is not confirmed. The site appears to use a dark hero section and dark footer, but a full dark-mode toggle or system-preference-based dark theme is not documented.
- Switch spec table styling (background, rounded corners) is inferred from common patterns on similar keyboard brand sites — not extracted from Akko's live CSS.
- Star rating color (#ff6900) is inferred from the extracted orange hex, but the exact component styling (size, spacing, half-star rendering) is unknown.
- Product card hover shadow values (0 4px 12px rgba(0,0,0,0.08)) are estimated — the exact shadow could not be extracted.
- Checkout flow styling (Shopify Pay, Klarna, Afterpay buttons) is not included — these are typically provided by third-party widgets and not part of the brand's design system.
- Animation and transition durations (button hover, card hover, nav dropdown) are not documented.
- Focus-visible ring styles for keyboard navigation are not confirmed.
- The brand may use a secondary typeface (Cardo, Inter, or Quicksand) for specific contexts (e.g., technical documentation, blog posts) but this could not be reliably extracted.
