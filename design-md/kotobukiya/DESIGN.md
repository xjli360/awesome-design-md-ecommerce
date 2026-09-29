---
version: alpha
name: "Kotobukiya"
source_url: "https://www.kotous.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A precision-engineered collectible marketplace where deep navy (#3c4662) and a single cyan accent (#00d7e1) provide the voltage, while a vast gray spectrum — from #fcfcfc canvas to #111111 ink — creates the quiet, museum-grade backdrop that lets sculpted plastic figures command attention. The brand's visual system is built on deliberate restraint: a primary blue (#006bb4) that reads as institutional rather than playful, supported by warm amber (#ffca30) and safety-orange (#ff5501) for limited-use badges and sale flags. Every corner is soft but not pillowy — cards and buttons land at {rounded.sm} (8px) rather than the full-radius approach of consumer marketplaces, suggesting a catalog of precision objects rather than casual goods. Typography runs Open Sans across all weights, with display sizes staying lean at 500–600 weight rather than heavy 700+, letting product photography and sculpt detail do the heavy lifting. The checkout and utility chrome leans heavily on a secondary blue (#1979c3) and a warm error red (#e02b27), while the persistent top bar uses a dark navy (#3c4662) with white text — a framing device that says "gallery" more than "store." The extracted palette is notably gray-dominant (over a dozen grays from #f0f0f0 to #8f8f8f), suggesting a system that uses value contrast rather than color to create hierarchy, with the cyan (#00d7e1) and amber (#ffca30) acting as rare, deliberate surprises — the equivalent of a single bright decal on an otherwise monochrome mecha kit.

colors:
  primary: "#006bb4"
  primary-active: "#1979c3"
  primary-disabled: "#bbbbbb"
  ink: "#111111"
  body: "#303030"
  muted: "#757575"
  muted-soft: "#8f8f8f"
  hairline: "#d1d1d1"
  hairline-soft: "#e5e5e5"
  canvas: "#fcfcfc"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  navy: "#3c4662"
  navy-active: "#4a5678"
  cyan: "#00d7e1"
  amber: "#ffca30"
  orange: "#ff5501"
  error: "#e02b27"
  warm-bg: "#fdf0d5"
  warm-text: "#6f4400"
  warm-accent: "#c07600"

typography:
  display-xl:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  price:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-sale:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
    color: "{colors.error}"

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
    padding: 10px 20px
    height: 40px
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
    padding: 10px 20px
    height: 40px
  button-navy:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-amber:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  text-input-focus:
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.price}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
  badge-new:
    backgroundColor: "{colors.cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-preorder:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-exclusive:
    backgroundColor: "{colors.orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    height: 40px
  add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  category-tab:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  hero-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
  hero-banner-cta:
    backgroundColor: "{colors.cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  filter-panel:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
  filter-checkbox:
    rounded: "{rounded.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the store, used for "Add to Cart," "Checkout," and primary form submissions. Rendered as a solid blue (#006bb4) rectangle with 8px rounded corners and white text in 14px/600 Open Sans. On hover, shifts to #1979c3; disabled state drops to #bbbbbb with white text. Height is 40px for standard use, 48px for the prominent add-to-cart variant.

**`button-secondary`** — An outlined or ghost alternative for less prominent actions like "View Details" or "Cancel." Uses a white background with #111111 text and a 1px #d1d1d1 border. Same 8px rounding and 40px height as primary. Hover adds a subtle #e5e5e5 background fill.

**`button-navy`** — Used exclusively within the dark navy (#3c4662) header and footer areas where a primary blue button would clash. White text on navy background, same 8px rounding and 40px height. Hover shifts to #4a5678.

**`button-amber`** — A warm accent button reserved for promotional CTAs, limited-time offers, or pre-order actions. Uses #ffca30 background with #111111 text. Same dimensions as other buttons. The amber provides deliberate contrast against the otherwise cool palette.

### Cards
**`product-card`** — The primary content container for the product grid. A white (#ffffff) card with 8px rounded corners, subtle shadow, and 1px #e5e5e5 border. Contains a product image (also 8px rounded at the top), title in 14px/600 Open Sans, and price in 16px/700. Sale prices render in #e02b27. Cards sit on a #f6f6f6 surface-soft background in the grid, creating a clean gallery-like separation.

**`product-card-image`** — The image area within a product card, cropped to a consistent aspect ratio (typically 1:1 or 4:3 for model kits). Uses `object-fit: cover` as found in the extracted CSS. The 8px rounding matches the parent card, with images filling the top portion.

### Navigation
**`nav-bar`** — A persistent 48px top bar using the brand's dark navy (#3c4662) with white navigation links in 14px/600 Open Sans. Contains the brand logo (left), category links (center), and utility icons (search, cart, account — right). On scroll, the bar transitions to a white (#ffffff) background with #111111 text for contrast against page content.

**`category-tab`** — Pill-shaped filter tabs used in category navigation strips. Default state is #f6f6f6 background with #757575 text in 12px/600 Open Sans. Active state fills with #006bb4 and white text. Both states use full rounding (9999px) and 6px vertical / 16px horizontal padding.

**`breadcrumb`** — Secondary navigation rendered in 12px/400 Open Sans with #757575 text. Active/current page uses #111111. Separators are simple ">" glyphs in #d1d1d1.

### Forms
**`text-input`** — Standard form input for search, checkout fields, and account forms. White background, 8px rounded corners, 40px height, 8px/12px padding. Default border is #d1d1d1; focus state gains a #006bb4 border. Text renders in 15px/400 Open Sans.

**`quantity-selector`** — A compact input group for adjusting item quantities in the cart. Uses a white background with 8px rounding and 40px height. Contains minus/plus buttons flanking a centered numeric value. All text in 14px/600 Open Sans.

### Badges
**`badge-new`** — A small cyan (#00d7e1) label with #111111 text, used to flag newly released products. 4px rounding, 2px/6px padding, 11px/700 Open Sans uppercase.

**`badge-sale`** — A red (#e02b27) label with white text for discounted items. Same dimensions and typography as the new badge.

**`badge-preorder`** — An amber (#ffca30) label with #111111 text for upcoming releases available for pre-order.

**`badge-exclusive`** — An orange (#ff5501) label with white text for store-exclusive or limited-edition items.

### Footer
**`footer`** — A full-width dark navy (#3c4662) section containing link columns, social icons, and legal text. Links render in 14px/400 white Open Sans. The footer uses generous vertical padding (48px+ section spacing) and maintains the gallery-like framing established by the top nav.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 columns), hamburger nav replaces full category strip, search bar collapses to icon, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, category strip scrolls horizontally, nav bar shows limited links with "More" dropdown |
| Desktop | 1128–1440px | Three-to-four-column product grid, full nav bar visible, search bar expanded, footer in multi-column layout |
| Wide | > 1440px | Max-width container (typically 1280px) centered, four-column product grid, additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 40px height for touch accessibility
- Category tabs and badge labels are minimum 32px tall with adequate tap spacing
- Quantity selector buttons are 40px × 40px for easy tap targeting
- Mobile nav hamburger icon is 44px × 44px

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Category filter strip becomes horizontally scrollable on tablet and mobile
- Product grid reduces columns progressively (4 → 3 → 2 → 1)
- Footer link columns stack vertically on mobile
- Search bar collapses to icon-only on mobile, expanding to full-width overlay on tap
- Breadcrumb truncates on mobile, showing only current page and "Home"

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted color palette is heavily gray-dominant (over 15 grays) with a few distinctive accents — the true brand primary may be more nuanced than #006bb4, but this was the most distinctive non-gray, non-blue color in the extracted set
- Font-family extraction returned mixed results including framework defaults (Luma icons, pagebuilder-font) and cookie-consent text — Open Sans appears to be the primary brand face but exact weight/scale mapping is inferred from common e-commerce patterns
- Hover states for most components are inferred from common patterns rather than extracted from live CSS
- Error states, validation styling, and form feedback colors are not present in the extracted data
- Dark mode is not supported based on available extraction
- Sub-brand or franchise-specific color palettes (e.g., specific anime/manga series) are not captured
- The warm-bg (#fdf0d5) and warm-text (#6f4400) colors suggest a secondary promotional palette but its usage context is unclear
- Checkout flow styling (Shopify Pay, Klarna, etc.) colors may be present in the extracted list but are not brand-controlled
- Animation timing, transition curves, and shadow values are not extracted
- The extracted cyan (#00d7e1) and amber (#ffca30) are highly distinctive but may be used sparingly — exact usage frequency is unknown
