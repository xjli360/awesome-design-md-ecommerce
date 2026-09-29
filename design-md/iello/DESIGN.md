---
version: alpha
name: "IELLO"
source_url: "https://iello.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A board game publisher that uses a primary red #f0263c with the punch of a game timer's final beep — it appears on every product badge, price tag, and add-to-cart button against a clean canvas #f3f4f5. The brand's secondary blue #003388 anchors the header and footer, creating a confident two-color system that reads as both playful and trustworthy. Product cards sit on white with soft rounded corners {rounded.sm}, while category badges use the full-radius pill shape {rounded.full} in either red or blue to signal game type. The typography system leans on a single sans-serif stack at moderate weights — body copy at 14px with 1.5 line-height keeps rules text readable, while game titles use a bolder 18px weight 700 to stand out in grid layouts. The checkout flow and account pages shift to a lighter palette with muted backgrounds #f0f0f0 and hairline borders #e7f5fe, maintaining the brand's approachable feel without visual fatigue. The overall impression is of a toy store that takes its games seriously but not itself — bright accents, generous whitespace, and a clear hierarchy that lets the product photography do the heavy lifting.

colors:
  primary: "#f0263c"
  primary-active: "#d41e32"
  primary-disabled: "#fca5af"
  ink: "#090909"
  body: "#32373c"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#e5e7eb"
  hairline-soft: "#f0f0f0"
  canvas: "#f3f4f5"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  secondary: "#003388"
  secondary-active: "#002266"
  secondary-light: "#e7f5fe"
  accent-green: "#e9fbe5"
  accent-red-soft: "#fcf0ef"
  badge-red: "#f0263c"
  badge-blue: "#003388"
  badge-text: "#ffffff"
  star-rating: "#231d9a"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0

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
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.secondary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.hairline}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  top-nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  top-nav-link-active:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "0 {spacing.base} {spacing.base}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-badge-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
  footer:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  hero-banner:
    backgroundColor: "{colors.secondary-light}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 36px
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  checkout-summary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, using the brand red #f0263c on white. On hover it darkens to #d41e32, and in disabled state it fades to a soft pink #fca5af. Used for "Add to Cart", "Buy Now", and primary form submissions. Height is 44px with 12px vertical padding and 24px horizontal.

**`button-secondary`** — Uses the deep blue #003388 for secondary actions like "View Details" or "Learn More". Same dimensions and hover behavior as primary, but with the blue active state #002266. Appears in the header and on product detail pages.

**`button-outline`** — A bordered variant with transparent background, 2px hairline border, and dark ink text. Used for "Cancel" actions, secondary navigation, and when multiple equal-weight CTAs appear together. On hover, the border thickens to 2px of the primary red.

**`button-pill-primary`** — A compact, fully rounded pill button in brand red, used for category filters, tag badges, and small inline actions. Height is 36px with 8px vertical padding and 20px horizontal. The pill shape signals a filter or tag rather than a primary action.

### Cards
**`product-card`** — A white card with 8px rounded corners and no padding at the container level — the image fills the top with matching top radius, while title, price, and badge content sit below with 16px side padding. Cards sit on the light gray canvas #f3f4f5 with a subtle shadow or border. The aspect ratio for product images is 1:1 square.

**`product-badge`** — A small uppercase pill badge in brand red or blue, used to indicate "New", "Sale", "Best Seller", or game category. Text is 11px weight 600 with 0.3px letter spacing, padded 4px vertically and 10px horizontally. The badge sits absolutely positioned over the product image's top-left corner.

### Navigation
**`top-nav`** — A 64px tall bar with deep blue #003388 background and white text. Navigation links use 15px weight 500 with 8px vertical and 16px horizontal padding. The active link is underlined with a 2px red border. The nav contains the logo, main category links, search, and cart icon.

**`search-bar`** — A full-radius pill input with white background and 1px hairline border. On focus, the border becomes 2px of brand red. Height is 40px with 8px vertical and 16px horizontal padding. The search icon sits inside the pill on the left.

### Forms
**`text-input`** — Standard text input with white background, 1px hairline border, 8px rounded corners, and 42px height. On focus, the border switches to 2px brand red. Placeholder text uses the muted color #6b7280. Used for email, search queries, and checkout fields.

**`select-input`** — Same dimensions and styling as text-input but with a dropdown arrow. Used for quantity selection, country/region pickers, and game category filters.

### Footer
**`footer`** — A deep blue #003388 footer section with white text at 14px weight 400. Links have 0.8 opacity by default and become fully opaque on hover. Padding is 48px vertical and 24px horizontal. The footer contains columns for support, about, legal, and social links.

### Hero
**`hero-banner`** — A full-width section with light blue #e7f5fe background, used for featured games, seasonal promotions, and new releases. The hero uses 26px bold display text with a single primary CTA button. Padding is 64px vertical and 24px horizontal.

### Cart & Checkout
**`cart-item`** — A white card with 8px rounded corners and 16px padding, separated from other items by a 1px hairline bottom border. Contains the product thumbnail, title, quantity selector, price, and remove button.

**`checkout-summary`** — A light gray #f0f0f0 card with 12px rounded corners and 24px padding. Displays subtotal, shipping, tax, and total. The "Place Order" button uses the primary red style.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid, hamburger menu replaces top nav, product cards stack vertically, hero banner reduces to 32px padding, search bar collapses to icon-only |
| Tablet | 744–1128px | Two-column product grid, top nav shows limited links with "More" dropdown, search bar remains full but narrower, hero uses 22px display text |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links visible, search bar at 400px max-width, hero at full width with 26px display text |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero banner constrained to container width |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target
- Category pills are 36px tall with 16px horizontal padding — touch target exceeds 44px width
- Product card CTAs are 44px tall with generous padding
- Mobile hamburger icon is 44x44px
- Quantity selector buttons are 36x36px with 12px padding

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Category filter strip collapses to a horizontal scrollable row on mobile
- Footer columns stack vertically below 744px
- Product grid reduces columns: 4→3→2→1 as viewport shrinks
- Hero banner text reduces from 26px to 22px to 18px
- Search bar collapses to icon-only on mobile, expanding on tap
- Cart page shifts from side-by-side to stacked layout below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations could be extracted from the live site — the typography block uses a common sans-serif stack (Inter) as a reasonable default, but the actual brand font is unknown
- Hover and active states for most components are inferred from common patterns rather than extracted from live CSS
- Error states for form inputs (validation, error messages) were not observed
- Dark mode styling is not present on the live site
- Sub-brand or seasonal color palettes could not be identified
- The exact border radius values for cards and buttons are estimated from visual inspection of extracted colors — the actual CSS may differ
- Dropdown menu styling (mega menu, sub-navigation) was not captured
- Modal and overlay styling (lightbox, cart drawer) is absent
- The star rating color #231d9a appears in the extracted colors but its exact usage context is unclear — it may be a social icon color rather than a rating color
- Loading states, skeleton screens, and animation timing were not extracted
- Print styles and accessibility-focused styling (focus rings, skip links) are undocumented
