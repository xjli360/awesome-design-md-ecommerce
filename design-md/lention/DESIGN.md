---
version: alpha
name: "Lention"
source_url: "https://www.lention.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A workspace-ergonomics brand that lives in the tension between industrial utility and consumer approachability, anchored on a near-black ink (#222222) and a signature orange (#fd4014) that fires across every primary CTA, badge, and category highlight. The brand uses a restrained palette of warm grays (#f7f7f7, #696969, #878787) and crisp whites (#fff) to create a clean, almost clinical backdrop for product photography, while the orange acts as a single voltage — never competing, always directing. Typography runs Poppins at moderate weights (400-600) with generous line heights, avoiding the heavy 700+ that characterizes pure tech hardware brands; the system trusts product imagery and whitespace over typographic muscle. Navigation is a fixed top bar with a centered logo and dropdown menus, while product cards use soft corners ({rounded.sm}) and hairline borders to frame items without visual clutter. The brand's secondary accent set — a cool blue (#0048ff), a muted teal (#56cfe1), and a safety green (#19bf24) — appears in badges, shipping indicators, and trust signals, suggesting a multi-category marketplace (cables, stands, chargers, monitors) rather than a single-product play. The overall feel is "premium but not precious": a workspace brand that wants you to buy confidently without the Apple-store reverence.

colors:
  primary: "#fd4014"
  primary-active: "#e03500"
  primary-disabled: "#fec0a8"
  ink: "#222222"
  body: "#383838"
  muted: "#696969"
  muted-soft: "#878787"
  hairline: "#d9d9d9"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#0048ff"
  accent-teal: "#56cfe1"
  accent-green: "#19bf24"
  accent-pink: "#e81e63"
  badge-sale: "#ec0101"
  badge-new: "#ad9725"
  star-rating: "#e0b252"
  error: "#eb001b"
  success: "#428445"
  dark-surface: "#111827"

typography:
  display-xl:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Segoe UI', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Segoe UI', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.1px
  link:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 500
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  text-input-placeholder:
    textColor: "{colors.muted-soft}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  nav-dropdown-item:
    padding: 8px 16px
    hoverBackgroundColor: "{colors.surface-soft}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 500
  product-card-price-sale:
    textColor: "{colors.badge-sale}"
  product-card-rating:
    typography: "{typography.caption-sm}"
    textColor: "{colors.star-rating}"
  badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
  badge-shipping:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
  badge-category:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    padding: "{spacing.md} 0 {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.canvas}"
    fontWeight: 600
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.xl} 0 {spacing.md}"
  section-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 36px
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  add-to-cart-button-active:
    backgroundColor: "{colors.primary-active}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
    padding: "0 {spacing.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, filled with the signature orange (#fd4014) and white text. On hover, shifts to a deeper burnt orange (`{colors.primary-active}`). Disabled state uses a pale peach (`{colors.primary-disabled}`) to signal non-interactivity while maintaining brand recognition. Used for "Add to Cart", "Buy Now", and primary checkout flows.

**`button-secondary`** — A white button with a single-pixel hairline border, used for secondary actions like "View Details" or "Learn More". On hover, the border darkens to ink and the background picks up a soft gray tint (`{colors.surface-soft}`). Maintains the same 44px height as primary for visual alignment in forms.

**`button-ghost`** — A text-only button with no border or background, used for tertiary actions like "Cancel" or "Remove". On hover, a soft gray background appears. The text color sits at body gray rather than full ink to visually demote the action.

**`button-pill`** — A fully rounded variant of the primary button, used for promotional badges, category filters, and quick-add actions in product grids. Smaller padding and font size than the standard primary, but retains the orange fill and white text.

### Forms & Inputs
**`text-input`** — Standard single-line text input with a white background, hairline border, and 8px corner radius. On focus, the border doubles in weight and switches to the primary orange. Error state swaps the border to red (`{colors.error}`). Placeholder text uses a muted gray (`{colors.muted-soft}`) at body-md weight.

**`select-input`** — Matches the text-input structure but includes a dropdown arrow (not defined in tokens). Same height, padding, and border treatment. Used for product sorting, quantity selection, and address forms.

**`quantity-selector`** — A compact three-part component: decrement button, numeric display, increment button. The outer container has a hairline border and 8px radius; the +/- buttons sit inside with a soft gray background and 4px radius. Used exclusively on product detail pages and cart line items.

### Navigation
**`nav-bar`** — A fixed top bar at 64px height with a white background and a subtle bottom border (`{colors.hairline-soft}`). Contains the brand logo (centered or left-aligned), dropdown category menus, and a search icon. The nav-link typography runs at 15px weight 500 — slightly smaller than typical e-commerce navs to keep the bar compact.

**`nav-dropdown`** — Appears on hover over top-level nav items. A white panel with 8px radius, containing a vertical list of links. Each item has 8px vertical padding and 16px horizontal padding; hover adds a soft gray background. No icons or images — purely text-driven.

### Cards
**`product-card`** — A white card with a soft border (`{colors.hairline-soft}`) and 8px radius. The image occupies the top with matching corner radius (top-left and top-right only). Below the image: title, rating stars, and price. On hover, the border strengthens to `{colors.hairline}` and a subtle shadow lifts the card. Used in collection grids, search results, and related-product carousels.

**`product-card-price-sale`** — When a product is on sale, the price switches to red (`{colors.badge-sale}`). The original price is shown as a strikethrough in muted-soft gray (not defined as a separate token but implied by the component).

### Badges
**`badge`** — Small uppercase labels at 11px weight 600 with 4px radius and 2px/8px padding. Four color variants map to different signals: sale (red), new (gold), shipping (green), and category (orange). Applied as overlays on product images or inline next to product titles.

### Hero
**`hero-section`** — The full-width banner at the top of the homepage and category pages. Uses a soft gray background (`{colors.surface-soft}`) with 64px vertical padding. The heading runs at 32px weight 600, with a body-gray subheading below. The hero typically contains a single primary button and a product image or lifestyle photo.

### Footer
**`footer`** — A dark section with an ink background and white text. Contains column headings at 16px weight 600, followed by link lists at 14px weight 400 in muted-soft gray. Links lighten to full white on hover. The footer includes payment icons, social links, and legal text at caption size.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 items); nav collapses to hamburger menu; hero padding reduces to 32px; font sizes drop one step (display-xl → display-lg); search bar moves to full-width below nav; footer columns stack vertically |
| Tablet | 744–1128px | Two-column product grid; nav remains horizontal but dropdowns become full-width overlays; hero uses 48px padding; font sizes at display-lg/display-md; search bar sits inline in nav |
| Desktop | 1128–1440px | Three-to-four-column product grid; full horizontal nav with dropdowns; hero at 64px padding; all typography at defined sizes; search bar in nav with expanded width |
| Wide | > 1440px | Max-width container at 1440px with auto margins; product grid can show 5 columns; hero background extends edge-to-edge; all content centered within container |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height (Apple HIG compliance)
- Nav dropdown items have 44px minimum tap target (8px padding + 28px text height)
- Quantity selector buttons are 36px — slightly below ideal but constrained by layout
- Search bar tap target is 40px height — acceptable for mobile
- Product card links use the full card as tap target (not just text)

### Collapsing Strategy
- Top nav collapses to hamburger icon at < 744px; dropdown menus become slide-in panels
- Product filters collapse to a "Filter" button that opens a modal overlay on mobile
- Footer columns stack vertically on mobile, with accordion-style expand/collapse for each section
- Product image galleries collapse from thumbnail strip to swipeable dots on mobile
- Multi-column category grids collapse to single-column carousels on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for all components could not be fully extracted; the above are best estimates based on common patterns and the brand's visual language
- Error states for forms (validation messages, error icons) were not observed on the live site
- Dark mode is not supported; no dark-mode tokens were found in the extracted CSS
- Sub-brand or seasonal color palettes (e.g., holiday, clearance) are not documented
- Typography scale for mobile (reduced sizes) was not extracted; the above assumes desktop-first scaling
- The exact font stack may include additional fallbacks not captured in the extraction (e.g., local system fonts)
- Animation and transition durations/easings were not extracted; the brand likely uses 200-300ms ease-in-out
- Icon set (shopping cart, user account, search, etc.) was not analyzed; the brand appears to use SVG icons in the nav
- Checkout flow styling (Shopify default vs. custom) could not be determined from the extracted data
- The extracted hex list contains several colors that appear to be Shopify widget defaults (e.g., #0048ff, #19bf24) — the primary orange (#fd4014) was selected as the most distinctive brand color, but secondary accents may vary by page or campaign
