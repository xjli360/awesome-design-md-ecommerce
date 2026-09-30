---
version: alpha
name: "Prodigy Games"
source_url: "https://www.prodigygames.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A competitive TCG marketplace that wears its red #ee2c2f like a tournament judge's armband — a single, urgent accent that snaps attention to "BUY NOW" buttons, sold-out badges, and the cart icon against a near-black #232424 canvas. The site reads as a dimly lit game shop after hours: deep charcoal surfaces (#151616, #121212) absorb light, while the silver-gray #dedede of card rarities and price tags provides the only relief. Navigation is dense and utilitarian — a top bar packed with franchise logos (Pokémon, Yu-Gi-Oh!, Magic: The Gathering) and a search field that doubles as a set-code lookup, suggesting a user base that knows exactly what it wants and types in shorthand. Product cards stack in tight grids with minimal whitespace, each one a thumbnail of the card art, a bolded name, and a price in the accent red. There is no hero imagery, no lifestyle photography — the inventory is the hero. The checkout flow, powered by Shopify, introduces a brief moment of white (#ffffff) and rounded corners ({rounded.sm}) that feel almost out of place against the otherwise hard-edged, monochrome layout. This is a system built for speed and scanability: high information density, low decoration, and a single color used sparingly but precisely.

colors:
  primary: "#ee2c2f"
  primary-active: "#c41e21"
  primary-disabled: "#f5a3a4"
  ink: "#232424"
  body: "#dedede"
  muted: "#9e9e9e"
  muted-soft: "#6b6b6b"
  hairline: "#3a3a3a"
  hairline-soft: "#2a2a2a"
  canvas: "#232424"
  surface-soft: "#151616"
  surface-card: "#1e1f1f"
  on-primary: "#ffffff"
  on-dark: "#dedede"
  badge-sold-out: "#121212"
  badge-new: "#ee2c2f"
  price: "#ee2c2f"
  star-rating: "#dedede"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-price:
    textColor: "{colors.price}"
    typography: "{typography.title-sm}"
  product-card-badge:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  cart-icon:
    textColor: "{colors.primary}"
    height: 24px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.body}"
    typography: "{typography.link}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
  filter-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 36px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Buy Now", and "Checkout". Rendered in the brand's signature red {colors.primary} with white text and a slight {rounded.sm} corner. On hover, it shifts to a deeper crimson {colors.primary-active}. The disabled state uses a washed-out pink {colors.primary-disabled} to signal inactivity without losing brand recognition.

**`button-secondary`** — A dark-surface alternative for secondary actions like "View Details" or "Save for Later". Uses the card background {colors.surface-card} with body text {colors.body} and a subtle border implied by the contrast. Maintains the same height and padding as the primary button for alignment in forms.

**`button-tertiary-text`** — A text-only button for less prominent actions like "Clear Filters" or "Cancel". Rendered in the accent red {colors.primary} on a transparent background, relying on the dark canvas for contrast.

### Cards
**`product-card`** — The core inventory unit, a compact rectangle on {colors.surface-card} with {rounded.sm} corners. Each card contains a thumbnail of the card art (typically a cropped 1:1 or 3:4 ratio), the card name in {typography.title-sm}, and the price in {colors.price}. A sold-out overlay uses {colors.badge-sold-out} with white text. Cards are densely packed in a grid with minimal {spacing.sm} gaps, maximizing scanability.

**`product-card-badge`** — A small, uppercase label affixed to the top-left corner of a product card. Uses {colors.badge-sold-out} for "SOLD OUT" or {colors.badge-new} for "NEW". The {rounded.xs} and tight padding keep it unobtrusive but legible.

### Navigation
**`nav-bar`** — A fixed top bar at 56px height, rendered in the darkest ink {colors.ink}. Contains the brand logo (typically white text), franchise-specific navigation links (Pokémon, Yu-Gi-Oh!, Magic: The Gathering), a search icon, and a cart icon. The active link or current section uses {colors.primary} for the text color.

**`nav-link-active`** — The active state for navigation items, distinguished by the accent red {colors.primary} against the dark bar. No underline or background change — the color shift alone signals the current page.

### Forms
**`text-input`** — A standard input field for search, filters, and checkout forms. Uses the card surface {colors.surface-card} as the background with {colors.body} text. The {rounded.sm} and {spacing.sm} padding keep it consistent with button styling. Focus state adds a {colors.primary} border (not extracted but assumed).

**`search-bar`** — The primary search input, identical in styling to `text-input` but with a search icon inset on the left. Used for set-code lookups (e.g., "SWSH12") and card name searches. The placeholder text uses {colors.muted}.

### Footer
**`footer`** — A full-width section at the bottom of the page, using the darkest {colors.ink} background. Contains links to "About Us", "Shipping", "Returns", "Contact", and social media icons. Text is in {colors.muted} for secondary information, with links in {colors.body} for readability.

**`footer-link`** — Standard link within the footer, using {colors.body} text on the dark background. Hover state likely shifts to {colors.primary} (assumed, not extracted).

### Filters & Pagination
**`filter-chip`** — A pill-shaped chip for filtering products by set, rarity, or condition. Uses the card surface {colors.surface-card} with body text. The {rounded.full} shape differentiates it from buttons. Active state uses {colors.primary} background with white text.

**`filter-chip-active`** — The active state of a filter chip, using the brand red {colors.primary} to indicate the applied filter. The pill shape remains consistent.

**`pagination-button`** — A square button for page navigation at the bottom of product listings. Uses the card surface {colors.surface-card} with body text. The active page uses {colors.primary} background.

**`pagination-button-active`** — The active page indicator, using the brand red {colors.primary} to distinguish the current page from available pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger menu; search bar moves to a full-width overlay; filter chips stack vertically; pagination becomes "Load More" button |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows franchise links as icons; search bar remains visible but condensed; filter chips wrap in a horizontal strip |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with text links; search bar at full width; filter chips in a horizontal row; pagination shows page numbers |
| Wide | > 1440px | Four-column product grid; nav-bar remains unchanged; search bar expands to accommodate longer queries; additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements maintain a minimum height of 40px for comfortable tapping on mobile.
- Filter chips are at least 36px tall with 14px horizontal padding.
- Nav-bar links on mobile are at least 44px tall to meet accessibility guidelines.
- Product card images are tappable, with the entire card area acting as a link.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu, revealing a full-screen overlay with franchise links, search, and cart.
- The product grid collapses from 4 columns on wide screens to 1 column on mobile, with images scaling proportionally.
- The footer collapses from a multi-column layout to a single column, with links stacked vertically.
- Filter chips collapse from a horizontal row to a vertical list, with a "Filters" button to toggle visibility.
- Pagination collapses from numbered pages to a "Load More" button on mobile to reduce UI clutter.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Font family**: No font-family declarations were found on the live site. The typography block assumes "Inter" as a common modern sans-serif, but this is a guess. The actual brand font may differ.
- **Hover states**: Hover colors for buttons, links, and cards are inferred from the primary-active color but were not extracted from the live site. The actual hover behavior may include underlines, opacity changes, or border shifts.
- **Error styling**: No error states for form inputs (e.g., invalid card number, empty search) were observed. The system likely uses a red border or text, but the exact hex is unknown.
- **Focus states**: Focus rings for accessibility were not extracted. The brand may use a custom focus style (e.g., a white or red outline) or rely on browser defaults.
- **Dark mode**: The site already uses a dark canvas, so a separate dark mode may not exist. However, if the brand plans a light mode, the palette would need significant adjustment.
- **Sub-brand palettes**: The site features multiple TCG franchises (Pokémon, Yu-Gi-Oh!, Magic: The Gathering), each with its own color identity. The extracted palette reflects the overall brand, not franchise-specific accents (e.g., Pokémon yellow, Magic's brown/gold).
- **Checkout flow**: The Shopify checkout was not fully analyzed. It likely introduces a white background and different button styles, which may conflict with the brand's dark theme.
- **Animation and transitions**: No CSS transitions or animations were extracted. The brand may use subtle fades, slides, or hover effects that are not captured.
- **Iconography**: The nav-bar and cart icons were not extracted. The brand likely uses a custom icon set or a library like Font Awesome, but the specific style (outline, filled, monochrome) is unknown.
- **Spacing and grid**: The spacing tokens are estimates based on common e-commerce patterns. The actual grid gaps, padding, and margins may vary.
