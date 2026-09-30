---
version: alpha
name: "Sena Cases"
source_url: "https://www.senacases.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A case for a phone is a case for a life — Sena Cases wraps devices in leather that starts at #3a3a3a, a near-black that reads as charcoal rather than void, and accents every primary action in #00b5e2, a cyan that feels more like a signal flare than a brand color. The extracted palette is a scatter of e-commerce defaults — #e5e5e5, #f1f1f1, #dfdfdf, #dedede, #eeeeee, #fafafa — but the brand's true voltage lives in that cyan and a secondary purple #4e008e that appears on sale badges and category highlights. Proxima Nova runs the typography at modest weights; buttons sit at 14–16px with 600 weight, never shouting. Product cards use soft corners ({rounded.sm}) and a white canvas (#ffffff) that lets the leather texture do the selling. The site is a Shopify storefront, so checkout widgets introduce #1abc9c (teal) and #1976d2 (blue) that aren't brand — they're platform. What distinguishes Sena is the material promise: leather cases photographed against neutral backgrounds, with color swatches in #571eae, #33c4e8, and #ff1493 that signal a product range wider than the nav suggests. The search bar is a pill ({rounded.full}) in #f1f1f1, the footer stacks #3a3a3a links on #2b2b2b, and the whole thing reads as a leather goods store that happens to sell phone accessories — not an accessory brand trying to be fashion.

colors:
  primary: "#00b5e2"
  primary-active: "#0099c0"
  primary-disabled: "#b3e8f5"
  ink: "#3a3a3a"
  body: "#3d4246"
  muted: "#707070"
  muted-soft: "#9f9f9f"
  hairline: "#e5e5e5"
  hairline-soft: "#f1f1f1"
  canvas: "#ffffff"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-purple: "#4e008e"
  accent-purple-light: "#571eae"
  accent-cyan-light: "#33c4e8"
  accent-pink: "#ff1493"
  accent-teal: "#1abc9c"
  accent-red: "#ba0c2f"
  accent-red-light: "#c90404"
  badge-sale: "#4e008e"
  badge-new: "#00b5e2"
  footer-bg: "#2b2b2b"
  footer-text: "#707070"
  star-rating: "#ff1493"

typography:
  display-xl:
    fontFamily: "'proxima-nova', Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-lg:
    fontFamily: "'proxima-nova', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'proxima-nova', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'proxima-nova', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'proxima-nova', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'proxima-nova', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'proxima-nova', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'proxima-nova', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'proxima-nova', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'proxima-nova', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'proxima-nova', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'proxima-nova', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'proxima-nova', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'proxima-nova', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'proxima-nova', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  footer-link:
    fontFamily: "'proxima-nova', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
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
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-cyan:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
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
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 4px rgba(0,0,0,0.08)"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-pill-focus:
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
  product-card-compare-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    textDecoration: line-through
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-color-swatch:
    width: 20px
    height: 20px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
  product-card-color-swatch-selected:
    border: "2px solid {colors.ink}"
  product-card-rating:
    color: "{colors.star-rating}"
    typography: "{typography.caption}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.footer-link}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.canvas}"
  footer-link-hover:
    color: "{colors.canvas}"
  newsletter-input:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.muted}"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.ink}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  pagination-disabled:
    color: "{colors.muted-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in #00b5e2 cyan with white text and 8px rounded corners. On hover it darkens to #0099c0; disabled state fades to #b3e8f5. Used for "Add to Cart", "Shop Now", and checkout entry points. **`button-secondary`** — A white button with a 1px #e5e5e5 border and #3a3a3a text, used for "Learn More" and secondary actions. Hover state darkens the border to #3a3a3a. **`button-tertiary-text`** — A text-only button in #00b5e2 cyan, used for "View All" links and inline actions. **`button-pill-cyan`** — A fully rounded pill variant of the primary button, used in promotional banners and hero sections. **`button-pill-outline`** — A white pill with a 1px #e5e5e5 border, used for filter toggles and category navigation.

### Cards
**`product-card`** — The core product display unit: white background, 8px rounded corners, subtle shadow (#0 1px 3px rgba(0,0,0,0.08)). On hover the shadow deepens to #0 4px 12px rgba(0,0,0,0.12). The image area has rounded top corners only. Title uses 16px/600 weight, price uses 16px/400 weight. A compare-at price appears in #9f9f9f with line-through when on sale. **`product-card-badge`** — A small uppercase badge in #4e008e purple for sale items, or #00b5e2 cyan for new arrivals. **`product-card-color-swatch`** — 20px circular swatches with a 2px transparent border; selected state shows a #3a3a3a border. **`product-card-rating`** — Star rating rendered in #ff1493 pink, using 13px caption type.

### Navigation
**`nav-bar`** — A 64px white bar with 15px/600 weight navigation links in #3a3a3a. On scroll it gains a subtle shadow (#0 2px 4px rgba(0,0,0,0.08)). **`nav-dropdown`** — White dropdown panels with 8px rounded corners and a 4px/12px shadow, containing body-type links. **`search-bar-pill`** — A 40px tall fully rounded search input in #fafafa with a 1px #e5e5e5 border. On focus the border switches to #00b5e2 cyan.

### Forms
**`text-input`** — Standard 44px tall input with 8px rounded corners, 1px #e5e5e5 border, and 16px padding. Focus state shows a #00b5e2 cyan border. **`select-input`** — Same dimensions and styling as text input, used for dropdown selectors like sort order and quantity. **`newsletter-input`** — A dark variant for the footer: #2b2b2b background, white text, 1px #707070 border. **`newsletter-button`** — A 40px tall cyan button paired with the newsletter input.

### Footer
**`footer`** — A dark section on #2b2b2b background with #707070 link text. Headings are white at 16px/600 weight. Links hover to white. The newsletter input and button sit in a row, with the input taking available width and the button fixed at its content width.

### Hero & Banner
**`hero-banner`** — A full-width section on #fafafa background with 64px vertical padding and 24px horizontal padding. Uses 28px/600 weight display type. The CTA button matches the primary button style. Used for seasonal promotions and new collection launches.

### Accordion
**`accordion-header`** — A clickable row with 12px vertical padding, 16px horizontal padding, and a 1px #e5e5e5 bottom border. Uses 16px/600 weight type. **`accordion-content`** — The expandable panel below, with 16px padding and 16px/400 weight body type.

### Breadcrumb & Pagination
**`breadcrumb`** — 13px/400 weight links in #707070, with the active (current page) item in #3a3a3a. **`pagination`** — 14px/400 weight page numbers in #3a3a3a. The active page gets a #00b5e2 cyan background with white text and 8px rounded corners. Disabled arrows render in #9f9f9f.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row), hamburger menu replaces full nav, search bar collapses to icon, footer stacks vertically, hero banner reduces to 48px padding |
| Tablet | 744–1128px | Two-column product grid (2 cards per row), nav links show top-level only with dropdowns on tap, search bar remains visible but shorter, footer splits into two columns |
| Desktop | 1128–1440px | Three-column product grid (3 cards per row), full nav with dropdowns on hover, search bar at full width, footer in four columns |
| Wide | > 1440px | Four-column product grid (4 cards per row), max-width container at 1440px, nav and footer remain at desktop layout |

### Touch Targets
- All buttons and links: minimum 44px height
- Color swatches: 20px diameter with 4px touch padding (effective 28px)
- Mobile nav hamburger: 44px x 44px tap area
- Accordion headers: 44px minimum height
- Search bar: 40px height (mobile), 44px (desktop)

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Secondary nav (category links) collapses to a horizontal scroll strip on mobile
- Footer columns collapse to a single column below 744px
- Product filters collapse to a slide-out drawer on mobile
- Search bar collapses to an icon that expands to full-width overlay on tap
- Accordion sections collapse by default on mobile, expand on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is dominated by e-commerce framework defaults (#e5e5e5, #f1f1f1, #dfdfdf, #dedede, #eeeeee, #fafafa) and checkout-widget colors (#1abc9c, #1976d2). The brand's true primary (#00b5e2) and secondary (#4e008e) are distinctive but the palette may be incomplete.
- Font stack extracted as "proxima-nova, Helvetica, sans-serif" — exact font weights and sizes are inferred from typical Shopify implementations; actual values may vary.
- Hover states for buttons and cards are inferred from common patterns; actual extracted hover colors are not available.
- Error states for form inputs (red borders, error messages) are not extracted.
- Dark mode is not supported; the site appears to be light-only.
- Sub-brand or collection-specific palettes (e.g., leather color swatches) are not captured beyond the extracted hexes.
- The "Font Awesome 5 Brands" and "Font Awesome 5 Free" declarations suggest icon usage but icon sizes and colors are not extracted.
- Meta theme-color is absent, meaning the browser chrome color is not set.
- The page title references "Targus" which may indicate a parent company or redirect; the Sena Cases brand identity is assumed from the URL and extracted colors.
