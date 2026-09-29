---
version: alpha
name: "InStockTrades"
source_url: "https://www.instocktrades.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A discount comic book marketplace that wears its deal-hunting DNA on its sleeve, anchored on a deep-ink canvas (#222222) rather than the white expanse typical of retail. The brand's primary voltage is a hot-orange (#fe8300) that appears on every price tag, add-to-cart button, and sale banner — a color that reads as "clearance aisle urgency" rather than luxury warmth. The site uses a dense, information-rich layout where product thumbnails sit in tight grids against dark surfaces (#383838, #3f3f3f, #2b2b2b), with price callouts in bright red (#ff0000) and yellow-gold (#ffba0c, #dad55e) that signal percentage-off savings. Typography runs system-level sans-serif (Arial, Helvetica, Open Sans) at modest sizes — the design trusts raw discount percentages and stock photography over refined typographic hierarchy. Navigation is a horizontal strip of category links against the dark header, with a prominent search bar and account/login utilities. Buttons use the orange primary with white text and sharp corners ({rounded.sm}), while sale badges and price tags adopt pill shapes ({rounded.full}) in yellow and red. The overall mood is that of a warehouse aisle: functional, high-contrast, and unapologetically promotional, with every design decision optimized for conversion rather than aesthetic calm.

colors:
  primary: "#fe8300"
  primary-active: "#e34e03"
  primary-disabled: "#ffba0c"
  ink: "#222222"
  body: "#383838"
  muted: "#444444"
  muted-soft: "#aaaaaa"
  hairline: "#454545"
  hairline-soft: "#5f3f3f"
  canvas: "#111111"
  surface-soft: "#2b2b2b"
  surface-card: "#3f3f3f"
  on-primary: "#ffffff"
  sale-red: "#ff0000"
  sale-gold: "#ffba0c"
  sale-yellow: "#dad55e"
  sale-yellow-bg: "#fffa90"
  success-green: "#47801a"
  link-blue: "#003eff"
  error-red: "#ff4500"
  badge-text: "#777620"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-lg:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    backgroundColor: "{colors.muted}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  button-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
    borderColor: "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    height: 200px
  product-price:
    typography: "{typography.price-lg}"
    textColor: "{colors.sale-red}"
  product-price-original:
    typography: "{typography.price-sm}"
    textColor: "{colors.muted-soft}"
    textDecoration: line-through
  sale-badge:
    backgroundColor: "{colors.sale-yellow-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  sale-badge-red:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
    borderColor: "{colors.hairline}"
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 40px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: 24px 16px
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 0
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
    padding: 4px 12px
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
    padding: 4px 12px
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    padding: 32px 16px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 32px
  pagination-link:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  pagination-link-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  account-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  cart-count-badge:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 1px 6px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and primary form submissions. It uses the brand's hot orange (#fe8300) background with white text, sharp 4px corners, and bold 14px Open Sans. On hover, it shifts to a deeper burnt orange (#e34e03). The disabled state drops to a muted gray (#444444) with lighter gray text (#aaaaaa), signaling the button is non-interactive.

**`button-secondary`** — An outlined variant used for secondary actions like "View Details" or "Cancel". It uses the dark canvas (#111111) background with orange (#fe8300) text, maintaining the same 4px radius and bold typography. This button sits alongside primary buttons in forms and product listings.

**`button-sale`** — A compact, pill-shaped badge-button used to highlight discount percentages on product cards. It uses bright red (#ff0000) background with white text, 11px bold type, and full rounding. This button is purely decorative and informational — it does not trigger navigation.

**`button-cart`** — A taller, more prominent version of the primary button specifically for cart-related actions. It uses the same orange background and white text but with increased padding (12px 24px) and height (44px) to accommodate touch targets and emphasize the purchase action.

### Cards
**`product-card`** — The core product display unit, a dark gray (#3f3f3f) card with 4px rounding and 12px padding. Each card contains a product image, title, price (in red), and optional sale badges. The card background provides contrast against the darker page canvas (#111111) while keeping the focus on the product thumbnail and pricing information.

**`product-card-image`** — The image container within a product card, set to a slightly lighter dark (#2b2b2b) background with minimal 2px rounding. It maintains a fixed height of 200px to ensure consistent card sizing across grid layouts.

### Navigation
**`nav-bar`** — The primary site navigation, a 48px horizontal bar with the darkest ink (#222222) background and white text. It contains category links, search, and account utilities. The bar is fixed at the top of the viewport for persistent access.

**`nav-link`** — Standard navigation link with transparent background and white text on the dark nav bar. Active links use the orange primary (#fe8300) background with 4px rounding to indicate the current section.

**`category-strip`** — A secondary navigation strip below the main nav, using the darkest canvas (#111111) background. It contains genre and category tabs for browsing the catalog. Active tabs use the orange primary background.

### Forms
**`text-input`** — Standard text input field used for search, login, and checkout forms. It uses a dark gray (#3f3f3f) background with white text, 4px rounding, and a subtle border (#454545). The input height (36px) is compact for dense layouts.

**`search-bar`** — The primary search input, slightly taller (40px) than standard inputs, with the same dark gray background and white text. It sits prominently in the nav bar and on search results pages, with an adjacent orange submit button.

### Badges
**`sale-badge`** — A pill-shaped badge with pale yellow background (#fffa90) and dark olive text (#777620), used to display "Save X%" or "Sale" labels on product cards. The full rounding and compact padding make it sit neatly on product thumbnails.

**`sale-badge-red`** — An alternative sale badge using bright red (#ff0000) background with white text, used for more urgent or higher-discount promotions. Same pill shape and typography as the yellow variant.

### Footer
**`footer`** — The site footer, using the darkest ink (#222222) background with muted gray (#aaaaaa) text. It contains links to policies, account pages, and company information. Links use the same muted gray with hover states likely shifting to orange.

### Pagination
**`pagination-link`** — Page number links in product listing pagination, using dark gray (#3f3f3f) backgrounds with white text and 4px rounding. The active page uses the orange primary background for clear visual distinction.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, collapsed nav into hamburger menu, reduced font sizes, stacked footer links, search bar moves to top |
| Tablet | 744–1128px | Two-column product grid, expanded nav with dropdowns, standard font sizes, side-by-side footer columns |
| Desktop | 1128–1440px | Three-to-four-column product grid, full horizontal nav, larger hero banners, multi-column footer |
| Wide | > 1440px | Four-to-five-column product grid, max-width container (1440px), expanded whitespace, larger product cards |

### Touch Targets
- All buttons and links maintain minimum 44px height for touch accessibility
- Search bar and text inputs have 40px minimum height
- Navigation links have 36px minimum tap area
- Product card images are tappable with minimum 200px height
- Sale badges are 24px+ in height for easy tapping

### Collapsing Strategy
- Main navigation collapses to hamburger menu below 744px
- Category strip collapses to a scrollable horizontal row on mobile
- Product grid reduces from 4 columns to 1 column on mobile
- Footer links stack vertically on mobile
- Hero banners reduce height and font size on mobile
- Search bar moves from nav bar to a dedicated top section on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components could not be reliably extracted — only button-primary hover (#e34e03) was confirmed
- Error styling for form inputs (red borders, error messages) not observed in extracted data
- Focus states and keyboard navigation styling not captured
- Dark mode — the site already uses dark backgrounds extensively, but no explicit dark mode toggle or alternate palette was found
- Loading states (spinners, skeleton screens) not observed
- Dropdown menu styling for navigation categories not fully captured
- Mobile hamburger menu animation and overlay styling not extracted
- Checkout flow styling (multi-step form, payment fields) not observed
- Sub-brand or promotional campaign palettes (e.g., holiday sales, special events) not captured
- The extracted color list includes several colors (#00ff00, #add8e6, #e9e9e9, #f6f6f6, #ededed) that may be from third-party widgets, stock images, or unused CSS — these were excluded from the primary palette
- Font sizes and weights are estimated based on common patterns for the declared font families — exact values may vary on the live site
- Spacing values are inferred from typical e-commerce layouts and may not match the site's exact grid system
