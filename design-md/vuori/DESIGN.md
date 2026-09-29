---
version: alpha
name: "Vuori"
source_url: "https://www.vuoriclothing.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A California-crafted performance apparel brand that runs on a charcoal-and-cream skeleton (#3e3e3e, #ededed, #f8f8f8) with a single electric-blue jolt (#006dff) reserved exclusively for the primary action — the Add to Bag button, the search icon, the checkout entry point. The palette reads like a coastal landscape: warm stone (#727272) for secondary text, a flash of marigold (#faaf43) and lemon (#f8eb30) for sale badges and seasonal accents, and a near-black ink (#17120f) for body copy that carries the weight of the brand's "performance lifestyle" positioning. Typography runs AktivGrotesk across the entire system — a clean, mid-century Swiss grotesk that avoids both the coldness of Helvetica and the warmth of a humanist sans — set at modest weights (400–500 for body, 600 for navigation, 700 for display headlines) with generous line spacing that mirrors the open, breathable fit of the brand's clothing. The interface is deliberately uncluttered: product cards use soft corners ({rounded.md} ~12px), the top nav is a fixed 72px bar with a centered logo and minimal links (Men, Women, Sale), and the search bar is a pill-shaped input ({rounded.full}) with a subtle hairline (#c6c6c6) that only appears on hover. Vuori's design language trusts negative space and product photography over decorative elements — there are no hero carousels, no parallax effects, no brand illustrations. The checkout flow, powered by Shopify, inherits the same charcoal-and-cream palette with the blue CTA as the single color anchor, while Klarna and Afterpay widgets introduce their own brand colors (#a4def9, #29a8e0) that sit alongside but never compete with Vuori's own. The result is a system that feels like the brand's clothing: purposeful, unpretentious, and built for movement.

colors:
  primary: "#006dff"
  primary-active: "#0052cc"
  primary-disabled: "#b3d4ff"
  ink: "#17120f"
  body: "#3e3e3e"
  muted: "#727272"
  muted-soft: "#a0a0a0"
  hairline: "#c6c6c6"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#faaf43"
  accent-sale-light: "#f8eb30"
  accent-sky: "#a4def9"
  accent-ocean: "#29a8e0"
  error: "#d02e2e"
  meta-theme: "#3e3e3e"

typography:
  display-xl:
    fontFamily: "'AktivGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'AktivGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'AktivGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'AktivGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'AktivGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'AktivGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'AktivGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'AktivGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'AktivGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'AktivGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'AktivGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'AktivGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'AktivGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'AktivGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
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
    padding: 14px 32px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-active:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  search-bar-active:
    borderColor: "{colors.hairline}"
    borderWidth: 1px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    textColor: "{colors.body}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.body}"
  product-card-sale-badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-sold-out-badge:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 40px
  size-selector-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.body}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.xl} 0 {spacing.base} 0"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "0 0 {spacing.base} 0"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-active:
    textColor: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The single most important interactive element in the system, rendered in Vuori's signature blue (#006dff) with white text and a subtle 8px corner radius. On hover, it shifts to a deeper navy-blue (#0052cc) to signal activation. The disabled state uses a pale blue (#b3d4ff) with the same white text, maintaining legibility while clearly indicating non-interactivity. Padding is generous (14px top/bottom, 32px left/right) to create a comfortable tap target on mobile.

**`button-secondary`** — An outlined alternative with a white background and dark ink text, used for secondary actions like "View Details" or "Save for Later." The active state fills the background with the soft surface gray (#f8f8f8). Border is 1px solid {colors.hairline} in default state, thickening to 2px solid {colors.ink} on hover.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel" or "Clear Filters." Hover state adds a subtle background tint of {colors.surface-soft}. Uses smaller typography ({typography.button-sm}) to visually subordinate it to primary and secondary buttons.

**`button-pill`** — A fully rounded variant of the primary button, used exclusively for the search bar's submit action and the "Add to Bag" on quick-add product cards. The pill shape ({rounded.full}) creates a friendly, approachable feel that contrasts with the system's otherwise modest corner radii.

### Navigation
**`nav-bar`** — A fixed 72px bar at the top of every page, with a white background and centered logo. Navigation links are uppercase, 14px, weight 600, with 0.5px letter spacing. The active page link has a 2px bottom border in {colors.ink}. On scroll, the nav bar gains a subtle bottom shadow (0 2px 4px rgba(0,0,0,0.08)). Mobile collapses to a hamburger menu with a slide-out drawer.

**`nav-link-active`** — The currently selected navigation item, distinguished by a 2px solid underline in {colors.ink}. The text color remains {colors.ink} for maximum contrast.

**`nav-link-inactive`** — Non-selected navigation items use {colors.body} (#3e3e3e) to visually recede while remaining legible. Hover state shifts to {colors.ink}.

### Product Cards
**`product-card`** — The core content unit for the product grid, featuring a full-bleed product image with {rounded.md} corners, the product name in {typography.title-sm}, and the price in {typography.price}. The card has no background color (transparent) — it relies entirely on the product photography and whitespace for visual structure. On hover, the image scales up 2% with a smooth transition (0.3s ease), and a quick-add button appears at the bottom.

**`product-card-sale-badge`** — A small marigold (#faaf43) badge with uppercase "SALE" text in {typography.badge}. Positioned at the top-left of the product image with 8px padding from the edge. Uses 4px corner radius for a subtle but noticeable shape.

**`product-card-new-badge`** — A blue (#006dff) badge with uppercase "NEW" text, used for newly launched products. Same dimensions and positioning as the sale badge.

**`product-card-sold-out-badge`** — A muted gray (#727272) badge with uppercase "SOLD OUT" text, overlaid on the product image with a semi-transparent white scrim behind it.

### Forms & Inputs
**`text-input`** — Standard form input with a white background, 48px height, and 8px corner radius. Default state has a 1px solid {colors.hairline} border. On focus, the border switches to 2px solid {colors.primary} with a subtle blue box-shadow (0 0 0 3px rgba(0,109,255,0.1)). Placeholder text uses {colors.muted-soft}.

**`search-bar`** — A pill-shaped input ({rounded.full}) with a soft gray background (#f8f8f8) and 44px height. On focus, it gains a 1px solid {colors.hairline} border and expands to full width on mobile. The search icon is positioned at the left with 12px padding.

**`size-selector`** — A grid of pill-shaped buttons for size selection. Default state is a white background with 1px solid {colors.hairline} border. Active state fills with {colors.ink} and inverts text to white. Hover state adds a 1px solid {colors.ink} border.

**`quantity-selector`** — A compact horizontal control with minus/plus buttons flanking a central number display. Uses {colors.surface-soft} background with 8px corner radius. Buttons are 40px square with centered icons.

### Footer
**`footer-link`** — Standard text links in the footer, using {typography.link} with {colors.body}. On hover, the color shifts to {colors.ink}. Links are stacked vertically in columns with 8px spacing between items.

**`footer-heading`** — Column headings in the footer, using {typography.title-sm} with {colors.ink}. No hover state — these are non-interactive labels.

### Layout & Structure
**`hero-section`** — Full-width section at the top of landing pages, using {colors.surface-soft} background with {typography.display-xl} for the headline. Padding is {spacing.section} (64px) top and bottom. Content is centered with max-width 1200px.

**`section-heading`** — Section titles throughout the site, using {typography.display-md} with {colors.ink}. Includes 32px top padding and 16px bottom padding to create visual separation from adjacent content.

**`accordion-trigger`** — Clickable headers for collapsible sections (product details, shipping info, size guide). Uses {typography.title-sm} with a right-aligned chevron icon that rotates 180 degrees on open. No background, no border — just text and icon.

**`accordion-content`** — The expanded content panel below an accordion trigger. Uses {typography.body-sm} with {colors.body} for readability. Padding is 16px bottom only, with content flowing naturally from the trigger.

**`divider`** — A 1px horizontal line using {colors.hairline-soft}, used to separate sections within a page (e.g., between product description and reviews). Full width with no margin by default.

**`icon-button`** — A circular 40px button with no background and a centered icon. Used for utility actions like wishlist, share, and cart. Hover state adds a subtle background tint of {colors.surface-soft}. Active state uses {colors.ink} for the icon color.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item), hamburger nav, stacked footer, full-width hero, search bar expands to full width, size selector becomes horizontal scroll |
| Tablet | 744–1024px | Two-column product grid (2 items), hamburger nav persists, footer in 2 columns, hero has 48px padding, search bar is 60% width |
| Desktop | 1024–1440px | Three-column product grid (3 items), full top nav visible, footer in 4 columns, hero has 64px padding, search bar is 360px fixed width |
| Wide | > 1440px | Four-column product grid (4 items), max-width 1440px container, hero has 80px padding, search bar is 400px fixed width |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px and minimum width of 44px to meet WCAG touch target guidelines
- Product card quick-add buttons are 48px × 48px for easy tapping
- Size selector pills are 44px × 44px minimum
- Icon buttons are 40px × 40px with 44px tap area via padding
- Nav bar hamburger icon is 44px × 44px

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 1024px
- Product grid reduces columns from 4 to 3 to 2 to 1 as viewport shrinks
- Footer columns collapse from 4 to 2 to 1
- Size selector switches from grid to horizontal scroll below 744px
- Search bar expands from fixed width to full width below 744px
- Product images switch from landscape to square crop below 744px
- Accordion sections are always collapsed by default on mobile, with first section open on desktop

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors include several checkout-widget colors (Klarna's #a4def9 and #29a8e0, Shopify Pay's blue) that are not part of Vuori's own brand palette — these are noted in the colors block as `accent-sky` and `accent-ocean` but should not be used for primary brand elements
- The extracted font list includes "Klarna Headline" which is a checkout-widget font, not Vuori's own — AktivGrotesk is the brand's primary typeface
- Hover and active states for most components are inferred from common patterns rather than extracted from the live site
- Error state styling (form validation, error messages) could not be reliably extracted
- Dark mode is not supported by the current site
- Sub-brand or seasonal palette variations (e.g., holiday, collaboration) are not captured
- Animation durations and easing curves are not extracted — standard 0.3s ease is assumed
- Box shadow values for nav bar, cards, and modals are not extracted
- The exact font weights available in AktivGrotesk on the site (400, 500, 600, 700) are confirmed, but variable font axes are unknown
- Product image aspect ratios and grid gap sizes are estimated based on common e-commerce patterns
- The meta theme-color (#3e3e3e) is used as the body text color and nav bar background on mobile, but its exact application context is unclear
