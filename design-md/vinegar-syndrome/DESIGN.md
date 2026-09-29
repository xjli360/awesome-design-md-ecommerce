---
version: alpha
name: "Vinegar Syndrome"
source_url: "https://vinegarsyndrome.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A cult film preservation label that wears its archive’s patina on the surface — the palette is anchored on a weathered gold #edc236 that reads like an old video-store sign, not a brand mark. That gold carries across primary buttons, sale badges, and the site’s header strip, while a secondary gold #ffbe00 and a deep red #c62828 handle urgency and membership tiers. The canvas is a warm off-white #eeeeee, not pure white, and the body copy sits in #444444 — a softened black that avoids the clinical contrast of a standard e‑commerce site. Typography runs Archivo Narrow at condensed widths, giving product titles and navigation a dense, almost newspaper-classified feel that matches the label’s exhaustive catalog of forgotten genre films. Search bars and filter dropdowns use tight {rounded.sm} corners, while product cards and membership badges use {rounded.md} — nothing is pill-shaped; the system avoids the friendly roundness of modern DTC in favor of a slightly industrial, archival precision. The checkout flow and account pages shift to a cooler gray #f7f7f7 canvas, suggesting a functional zone separate from the browsing experience. Red badges #ff2626 on sold-out items and #4fc3f7 accent links provide the only high-saturation moments outside the gold family, creating a restrained but unmistakable visual language: this is a shop that treats every out-of-print VHS and 4K restoration as a museum artifact.

colors:
  primary: "#edc236"
  primary-active: "#d4a92e"
  primary-disabled: "#f5e0a0"
  ink: "#111111"
  body: "#444444"
  muted: "#aaaaaa"
  muted-soft: "#bbbbbb"
  hairline: "#d5d5d5"
  hairline-soft: "#e6e6e6"
  canvas: "#eeeeee"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  surface-checkout: "#f7f7f7"
  on-primary: "#111111"
  on-dark: "#ffffff"
  accent-red: "#c62828"
  accent-red-bright: "#ff2626"
  accent-red-soft: "#ffdede"
  accent-blue-link: "#4fc3f7"
  accent-blue-active: "#1199ff"
  accent-purple: "#9333ea"
  membership-gold: "#ffbe00"
  membership-bg: "#eedd22"
  sold-out: "#ff0000"
  sold-out-soft: "#ff6d6d"
  warm-gray: "#b79e8c"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
    textTransform: uppercase
  price:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    padding: 8px 16px
  button-sold-out:
    backgroundColor: "{colors.sold-out-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  button-membership:
    backgroundColor: "{colors.membership-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.hairline}"
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  top-nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    border-bottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.accent-red-bright}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-membership:
    backgroundColor: "{colors.membership-bg}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  filter-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 14px
    height: 40px
    border: "1px solid {colors.hairline}"
  filter-dropdown-active:
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 32px
  pagination:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
    border-bottom: "1px solid {colors.hairline-soft}"
  cart-total:
    typography: "{typography.price}"
    padding: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Subscribe", and "Checkout" flows. Rendered in the brand gold #edc236 with dark text for high contrast. On hover, shifts to `{colors.primary-active}` (#d4a92e). Disabled state uses `{colors.primary-disabled}` (#f5e0a0) with muted text.

**`button-secondary`** — Used for "View Details", "Cancel", and secondary checkout actions. White background with a thin hairline border. Active state fills with `{colors.surface-soft}` and darkens the border to `{colors.muted}`.

**`button-ghost`** — Text-only button for filter resets, "Clear All", and inline actions. No background, no border — relies on `{typography.button-sm}` weight for distinction.

**`button-sold-out`** — A soft red button for items that are out of stock, using `{colors.sold-out-soft}` (#ff6d6d) background. Prevents further interaction while signaling availability status.

**`button-membership`** — Exclusive to the subscription/membership flow, using the secondary gold `{colors.membership-gold}` (#ffbe00) to visually separate the membership tier from standard purchases.

### Navigation
**`top-nav`** — Fixed header bar at 64px height on a warm off-white `{colors.canvas}` (#eeeeee). Contains the brand logo, category links, search icon, and cart. Bottom border uses `{colors.hairline}` (#d5d5d5). Links are set in uppercase `{typography.nav-link}`.

**`top-nav-link`** — Individual navigation items with 8px horizontal padding. Active state shows a 2px gold underline from `{colors.primary}`. Hover state darkens text to `{colors.ink}`.

### Forms & Inputs
**`text-input`** — Standard text field for email, name, and address forms. White background, 44px height, thin hairline border. Focus state swaps border to `{colors.primary}` gold.

**`select-input`** — Dropdown selectors for sorting, filtering, and quantity. Same dimensions and styling as `text-input` for visual consistency.

**`search-bar`** — Site search input matching the form field pattern but with 16px horizontal padding for comfort. Focus state uses gold border to match the brand's accent.

### Cards
**`product-card`** — The primary product display unit. White background with `{rounded.md}` (8px) corners. Image area uses top-rounded corners only. Title uses `{typography.title-sm}` at 14px/600 weight, price uses `{typography.price}` at 18px/700 weight. No shadow — relies on the card's white surface against `{colors.canvas}` for separation.

**`product-card-badge`** — Small gold badge overlaid on product images for "New Release", "Sale", or "Exclusive" labels. Uses `{typography.badge}` at 11px uppercase with tight 2px/8px padding.

**`badge-sold-out`** — Bright red (#ff2626) badge for out-of-stock items. Uses white text for maximum contrast against the red.

**`badge-membership`** — Gold (#eedd22) badge for subscriber-only items. Dark text maintains readability on the lighter gold.

### Filters & Search
**`filter-dropdown`** — Category and sorting dropdowns at 40px height. Matches the input styling pattern with hairline border. Active state highlights with gold border.

**`search-bar`** — See Forms & Inputs section above.

### Footer
**`footer`** — Dark section using `{colors.ink}` (#111111) background with light text. Links use `{colors.muted-soft}` (#bbbbbb) and shift to gold on hover. Padding uses `{spacing.xxl}` (48px) vertical and `{spacing.section}` (64px) horizontal on desktop.

### Hero & Layout
**`hero-banner`** — Full-width promotional banner using `{colors.canvas}` background. Large headline in `{typography.display-xl}` (32px/700 weight). CTA button uses `{colors.primary}` gold with generous 32px horizontal padding.

**`pagination`** — Page number links with transparent background. Active page fills with gold `{colors.primary}`. Inactive pages show `{colors.body}` text on hover.

### Cart
**`cart-item`** — Individual line items in the cart drawer or page. White background with soft hairline bottom border. Each item shows thumbnail, title, quantity selector, and price.

**`cart-total`** — Order total line using `{typography.price}` weight for emphasis. Positioned at the bottom of the cart summary.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu. Product cards stack in single column. Filter dropdowns become full-width accordions. Hero banner reduces padding to 32px. Footer stacks links vertically. |
| Tablet | 744–1128px | Top nav shows limited links (logo, search, cart, hamburger). Product cards display in 2-column grid. Filter dropdowns remain visible but compact. Hero banner uses 48px padding. |
| Desktop | 1128–1440px | Full top nav with all category links visible. Product cards in 3-column grid. Filter sidebar or top bar with dropdowns. Hero banner uses 64px padding. |
| Wide | > 1440px | Max-width container at 1440px centered. Product cards in 4-column grid. Additional whitespace around hero and footer sections. |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility.
- Filter dropdowns and search inputs use 40px+ height.
- Product card tap targets (title, image, price) are independently tappable with minimum 44x44px hit areas.
- Cart quantity selectors use 36px+ buttons with adequate spacing.

### Collapsing Strategy
- Top nav: On mobile, all category links collapse into a slide-out drawer. Search icon remains visible in the header bar.
- Product filters: On mobile, filter options collapse into a single "Filter" button that opens a modal or drawer.
- Footer: On mobile, link columns stack vertically with expandable sections for "Customer Service", "About", and "Connect".
- Product grid: Columns reduce from 4 → 3 → 2 → 1 as viewport shrinks.
- Hero banner: On mobile, reduces to single-column layout with stacked text and CTA.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the live site CSS. The active states defined above are inferred from common patterns.
- Error styling for form validation (red borders, error messages) was not observed in the extracted data. A standard red (#c62828) is available in the palette but not assigned.
- Dark mode is not present on the live site. All components assume light mode only.
- Sub-brand or collection-specific color variations (e.g., "VSU", "VSA", "Partner Label" badges) were not captured. The `membership-gold` and `membership-bg` tokens are best guesses from extracted yellows.
- The exact font sizes for `display-xl` through `caption` are inferred from common Archivo Narrow usage patterns on the site. The extracted font-family list only included "Archivo Narrow" without size/weight data.
- Checkout-specific components (payment form, shipping selector, order summary) were not analyzed due to cart access limitations.
- Animation and transition durations (hover fades, dropdown animations, modal transitions) were not extracted.
- The `rounded` values are inferred from common e-commerce patterns on the site. The exact pixel values for card corners and button radii could not be precisely determined from the extracted CSS.
