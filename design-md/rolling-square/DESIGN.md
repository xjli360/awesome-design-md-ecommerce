---
version: alpha
name: "Rolling Square"
source_url: "https://www.rollingsquare.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A black-and-neon utility brand for lifehackers, where #000000 is the canvas and #17e260 is the voltage — a lime-green that appears on primary CTAs, badge dots, and product highlights like a soldering iron tip. The site runs on Shopify but rejects the typical soft-commerce look: hard black backgrounds, monospace type in `Basier Square Mono` for technical specs, and a palette that borrows from electronics — #ff7f7f for error states, #ffc100 for warning accents, #004d8b for deep informational links. Product cards sit on #f9fafb with {rounded.sm} corners, but the hero section uses full-bleed black with green glowing buttons at {rounded.full}, suggesting a brand that sells cables and chargers as if they were tactical gear. The nav bar is fixed, black (#1a1a1a), with white text and a search icon that triggers a full-screen overlay — no hamburger, no dropdowns. Badges appear in #17e260 for "in stock" and #ff7f7f for "low stock", both set in Montserrat uppercase at 10px. The checkout flow uses Shopify defaults (Klarna, Afterpay badges visible), but the brand's own cart drawer is black with green accent buttons. Typography splits personality: Montserrat for headings (bold, condensed, all-caps on section titles) and Inter for body copy (light weight, generous line-height). The overall feel is less "lifestyle gadget" and more "electronics lab manual" — every pixel feels engineered, not curated.

colors:
  primary: "#17e260"
  primary-active: "#14c954"
  primary-disabled: "#a3f0b8"
  ink: "#1a1a1a"
  body: "#555555"
  muted: "#888888"
  muted-soft: "#bbbbbb"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#000000"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  on-primary: "#000000"
  on-dark: "#ffffff"
  error: "#ff7f7f"
  error-strong: "#8b0000"
  warning: "#ffc100"
  info: "#004d8b"
  accent-blue: "#7fd7ff"
  accent-teal: "#108474"
  accent-purple: "#a89cc8"
  stock-green: "#17e260"
  stock-red: "#ff7f7f"
  star-rating: "#fbcd0a"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  mono:
    fontFamily: "'Basier Square Mono', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
    textTransform: uppercase
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.on-dark}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.on-dark}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-green:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    border: "1px solid {colors.on-dark}"
  icon-button-circle:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-circle-green:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
  search-input:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  badge-stock:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-low-stock:
    backgroundColor: "{colors.stock-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "16px 40px"
    height: 56px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    textTransform: uppercase
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
  cart-item:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  quantity-selector:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline}"
  accordion-faq:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in #17e260 lime green on a black background. Uses Montserrat uppercase at 14px with full pill rounding. On hover, shifts to `primary-active` (#14c954). Disabled state uses `primary-disabled` (#a3f0b8) with reduced opacity. Found on add-to-cart, checkout, and hero CTAs.
**`button-secondary`** — An outlined button for dark backgrounds: transparent fill with a 2px white border. Hover fills with #1a1a1a. Used for secondary actions like "Learn More" on hero sections or "View Details" on product pages.
**`button-tertiary-text`** — A text-only button in #17e260 green, no background or border. Used for inline actions like "Apply Coupon" or "See All" in category strips.
**`button-pill-green`** — A smaller pill button (8px vertical padding, 20px horizontal) used for inline badges or quick-add actions. Same green fill as primary but with `button-sm` typography.
**`button-pill-outline`** — A small outlined pill for dark backgrounds, used for filter tags or "Compare" actions. White border, transparent fill.

### Cards
**`product-card`** — A white card on #f9fafb surface with {rounded.sm} corners. Contains a product image (top corners rounded, bottom flush), title in Montserrat 16px semibold, and price in Inter 16px semibold. No shadow — relies on hairline border (#dedede) for separation. Hover state adds a subtle green border (#17e260, 2px).
**`cart-item`** — A dark card (#1a1a1a) inside the black cart drawer. Displays product thumbnail, title, quantity selector, and price. Uses {rounded.sm} corners and 16px padding.

### Navigation
**`top-nav`** — Fixed black bar (#1a1a1a) at 64px height. Contains logo (left), nav links (center, uppercase Montserrat 13px), and search icon (right). No dropdowns — all navigation is flat. On mobile, nav links collapse into a full-screen overlay triggered by a hamburger icon.
**`search-overlay`** — A full-screen black overlay (#000000) triggered by the search icon. Contains a search input field with dark background (#1a1a1a) and green accent cursor. Results appear below in a scrollable list with product cards.

### Forms
**`search-input`** — A dark input field (#1a1a1a) with white text and a 1px hairline border. Uses {rounded.sm} corners and 48px height. Placeholder text in #888888. Focus state adds a #17e260 border.
**`quantity-selector`** — A compact input group for cart quantities. Dark background with hairline border, centered text, and +/- buttons. Uses {rounded.sm} corners.

### Badges
**`badge-stock`** — Green (#17e260) badge with black text, uppercase Montserrat 10px. Used for "In Stock" labels on product cards. {rounded.xs} corners, 2px vertical padding.
**`badge-low-stock`** — Red (#ff7f7f) badge with white text. Used for "Low Stock" warnings.
**`badge-sale`** — Yellow (#ffc100) badge with black text. Used for "Sale" or "Discount" labels.
**`badge-new`** — Blue (#7fd7ff) badge with black text. Used for "New Arrival" labels.

### Footer
**`footer`** — Dark section (#1a1a1a) with muted gray text (#888888). Column layout with headings in uppercase Montserrat. Links in Inter 14px with hover color #ffffff. Includes social icons, newsletter signup, and legal text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-up), nav links hidden behind hamburger, hero text reduces to 24px, buttons become full-width, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, nav links visible as text (no icons), hero uses 28px display, side-by-side footer columns |
| Desktop | 1128–1440px | Three-column product grid, full nav with search icon, hero uses 36px display, four-column footer |
| Wide | > 1440px | Max-width container at 1440px, centered content, product grid can show 4 columns, hero remains full-bleed |

### Touch Targets
- All buttons and links: minimum 44px height, 44px width for icon-only targets
- Quantity selector +/- buttons: 40px x 40px tap area
- Product card tap targets: entire card is clickable (minimum 120px height)
- Nav links: 44px minimum tap height
- Search icon: 48px x 48px tap area

### Collapsing Strategy
- Top nav links collapse to hamburger menu at < 744px
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport shrinks
- Footer columns collapse from 4 → 2 → 1 at tablet breakpoints
- Hero section reduces padding from 64px to 32px on mobile
- Search overlay replaces inline search on all breakpoints (no persistent search bar)
- Product card images maintain 1:1 aspect ratio on mobile, 4:3 on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from static HTML/CSS — only primary button hover was confirmed
- Error state styling for form inputs (validation messages, error borders) not observed
- Dark mode / high-contrast mode not present on the live site
- Sub-brand or collection-specific color variations not detected (e.g., "Edge" vs "inCharge" product lines may have distinct palettes)
- Animation durations and easing curves not extracted (transition timing for hover states, drawer slide-in, search overlay fade)
- Typography scale for mobile (responsive font sizes) not confirmed — desktop values used as baseline
- Spacing scale for mobile (reduced padding/margins) not extracted — desktop values used
- The extracted hex list contains many generic grays and blues likely from Shopify framework defaults, social icons, and payment badges — the true brand palette is narrower: #000000, #17e260, #1a1a1a, #ff7f7f, #ffc100, #004d8b, #7fd7ff, #f9fafb
- Font stack order for `Basier Square Mono` and `Baskerville` unclear — `Basier Square Mono` used for technical specs, `Baskerville` may appear in editorial content but not confirmed
- `JudgemeIcons` and `JudgemeStar` fonts are from the Judge.me review app, not brand typography
- `Montserrat` with `!important` suggests aggressive override — likely the primary heading font
