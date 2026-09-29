---
version: alpha
name: "Keyway"
source_url: "https://www.keywaydesigns.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A forest-and-resin palette anchored on a deep, saturated evergreen (#108474) that reads as grown wood rather than corporate green — the brand’s primary voltage, appearing on every add-to-cart button, navigation highlight, and footer accent. The supporting sage (#717d49) and warm marigold (#ffba00) badges and sale tags introduce a craft-shop warmth that keeps the system from feeling cold or industrial. The canvas is a near-white (#f9fafb) with soft card surfaces (#ffffff) and hairline borders in #dedede, creating a clean, workshop-table atmosphere where the product photography — wood grain, resin swirls, live-edge shapes — does the heavy atmospheric lifting. Typography runs a two-family system: Jost for display and button labels (a geometric sans with humanist quirks in the uppercase R and K), and Nunito Sans for body copy, giving the interface a friendly, slightly handmade rhythm that matches the woodworking positioning. Buttons are softly squared at {rounded.sm}, product cards carry a gentle {rounded.md} shadow, and the marquee hero section uses a full-bleed image with a dark scrim overlay (#222222 at 60%) and white text, a confident move that lets the material texture dominate. The brand’s Shopify checkout layer introduces a secondary palette of social blues (#3b5998, #1da1f2) and payment-widget accents, but the core system stays firmly in the woodshop: green, sage, marigold, and warm charcoal.

colors:
  primary: "#108474"
  primary-active: "#0d6b5c"
  primary-disabled: "#a3d4c9"
  ink: "#222222"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#717d49"
  accent-marigold: "#ffba00"
  accent-marigold-active: "#f7cb07"
  accent-lavender: "#a89cc8"
  accent-teal: "#c1e6e6"
  star-rating: "#ffba00"
  social-facebook: "#3b5998"
  social-twitter: "#1da1f2"
  scrim: "#222222"
  error: "#c13515"
  success: "#108474"

typography:
  display-xl:
    fontFamily: "'Jost', 'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Jost', 'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Jost', 'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Jost', 'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', 'Jost', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Jost', 'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Jost', 'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Jost', 'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Jost', 'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Jost', 'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase

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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-sale:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
  button-sale-active:
    backgroundColor: "{colors.accent-marigold-active}"
    textColor: "{colors.ink}"
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-circle-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.body}"
  nav-cart-icon:
    textColor: "{colors.primary}"
    height: 24px
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    minHeight: 500px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "16px 36px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-sale-badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-sold-out-badge:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.surface-soft}"
    typography: "{typography.link}"
  footer-social-icon:
    textColor: "{colors.surface-soft}"
    height: 20px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  accordion-header:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    borderBottom: "2px solid {colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand’s signature evergreen (#108474) with white text and a soft 8px corner. Used for "Add to Cart", "Shop Now", and primary checkout flows. On hover, the background shifts to a deeper forest tone (#0d6b5c). The disabled state uses a muted sage (#a3d4c9) to signal inactivity while maintaining brand color harmony.
**`button-secondary`** — An outlined variant with a white fill and a 2px solid border in the primary green. Used for secondary actions like "View Details" or "Learn More". Hover state darkens the border and text to the active green.
**`button-tertiary-text`** — A text-only button with no background or border, used for inline actions like "Cancel" or "Clear Filters". The text color matches the primary green, and hover adds a subtle underline.
**`button-sale`** — A high-visibility marigold (#ffba00) button with dark ink text, used exclusively for sale or promotional CTAs. The active state shifts to a slightly deeper gold (#f7cb07). This button introduces the brand’s warm accent into the action system.

### Cards
**`product-card`** — The primary product display container, a white card with a soft 12px corner radius and a subtle drop shadow (0 2px 8px rgba(0,0,0,0.08)). Contains a square-ratio product image with 8px corners, a title in Jost 18px/600, a price in Nunito Sans 16px/400, and an "Add to Cart" button. Badges for "Sale" (marigold background) or "Sold Out" (gray background) overlay the top-left of the image. The card is designed to feel like a small display table for a handcrafted object.

### Navigation
**`nav-bar`** — A fixed 72px white bar with a bottom border in the softest hairline (#e9e9e9). Navigation links are set in Jost 15px/500 with 0.5px letter spacing and uppercase transformation, giving the nav a refined, slightly editorial feel. The active link is underlined with a 2px primary-green bar. The cart icon is rendered in the primary green, serving as a subtle but persistent brand anchor.
**`nav-link-active`** — The active state for a top-level navigation item. The text color shifts to the primary green, and a 2px bottom border in the same green appears below the text.
**`nav-link-inactive`** — The default state for navigation items, using the body gray (#555555). Hover state transitions to the primary green.

### Forms
**`text-input`** — A standard text input field with a white background, 1px hairline border (#dedede), 8px corner radius, and 48px height. On focus, the border thickens to 2px and turns primary green. Error state uses a 2px red (#c13515) border. The placeholder text uses the muted gray (#7b7b7b).
**`select-dropdown`** — Matches the text-input styling but includes a custom dropdown arrow in the primary green. Used for product filtering (e.g., "Sort by", "Material").

### Search
**`search-bar`** — A pill-shaped search input with a full 9999px border radius, white background, and 1px hairline border. The placeholder reads "Search products..." in muted gray. On focus, the border becomes 2px primary green. The search icon sits inside the input on the left, rendered in the body gray.

### Footer
**`footer-section`** — A full-width dark footer with a #222222 background and soft white text (#f2f2f2). Contains columns for "Shop", "Support", "About", and social media links. Social icons (Facebook, Twitter) use their brand colors (#3b5998, #1da1f2) but are rendered at a smaller 20px size. Links are set in Nunito Sans 14px/400 and turn primary green on hover.

### Badges
**`product-card-sale-badge`** — A small uppercase badge with a marigold (#ffba00) background and dark ink text, used to flag discounted items. The 4px corner radius and tight padding (4px 8px) keep it unobtrusive but visible.
**`product-card-sold-out-badge`** — A gray (#aaaaaa) badge with white text, signaling unavailability. Uses the same dimensions and typography as the sale badge.

### Accordion
**`accordion-header`** — Used in product description sections (e.g., "Details", "Shipping", "Returns"). A white background with a bottom hairline border, 16px/600 Jost title, and a chevron icon that rotates on open. The content area uses Nunito Sans 16px/400 with 16px padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row), hamburger menu replaces top nav, hero section reduces to 300px min-height, search bar collapses to icon-only, footer stacks vertically, buttons become full-width |
| Tablet | 744–1128px | Two-column product grid, top nav shows condensed links (Shop, About, Support), hero section at 400px min-height, search bar remains expanded but narrower |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links visible, hero section at 500px min-height, search bar at full width within a constrained container |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero section at 600px min-height with parallax effect, additional whitespace around all sections |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height and 44px width for touch accessibility.
- Icon buttons (cart, search, menu) are 40px x 40px with 8px internal padding.
- Product card "Add to Cart" buttons are 48px tall on mobile to accommodate finger taps.
- Accordion headers have 48px touch height.
- Quantity selector buttons are 40px x 40px.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile (< 744px). The menu drawer slides in from the left, overlaying the content with a 60% opacity scrim.
- Product filters collapse into a bottom sheet or modal on mobile.
- Footer columns stack vertically on mobile, with each section becoming an accordion.
- Search bar collapses to a magnifying glass icon on mobile; tapping it expands the full input field.
- Product image galleries collapse from a row of thumbnails to a swipeable carousel on mobile.
- Multi-column product grids collapse to single column on mobile, two columns on tablet.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components (buttons, links, cards) are inferred from common patterns; exact transition durations and easing curves were not extracted.
- Error styling for forms (validation messages, error icon placement) is assumed based on standard Shopify patterns; the exact error color (#c13515) is from the extracted list but its usage is inferred.
- Dark mode is not present on the live site; no dark mode tokens are defined.
- The exact font weights for Jost and Nunito Sans are inferred from common web usage; the live site may use different weights for specific contexts.
- Sub-brand or collection-specific palettes (e.g., limited edition colors) were not extracted.
- The hero section's exact height and overlay opacity are inferred from common e-commerce patterns; the extracted data did not include precise CSS values.
- Animation and transition specifications (duration, easing, stagger) are not available.
- The checkout flow uses Shopify's default styling; brand-specific checkout overrides were not detected.
- The exact spacing values for the product card's internal padding and the footer's section padding are inferred from common patterns; the extracted data did not include precise measurements.
- The star-rating color (#ffba00) is inferred from the extracted marigold; the actual rating component may use a different shade.
