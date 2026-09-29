---
version: alpha
name: "Solaris Japan"
source_url: "https://solarisjapan.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The brand’s identity is anchored on a deep teal #108474 — a color that reads as both oceanic and electronic, appearing in the primary navigation bar, cart totals, and checkout buttons, while the warm accent #f5af19 (a marigold yellow) punctuates sale badges, discount labels, and limited-edition callouts. The canvas is a near-white #f9fafb, with product cards surfaced on pure white #ffffff and separated by hairline borders in #e9e9e9. The typography relies on Nunito Sans for body and display text — a rounded, approachable sans-serif that softens the high-density grid of product thumbnails, price tags, and filter bars. Buttons use {rounded.sm} corners, while search bars and category pills adopt {rounded.full} for a friendly, tactile feel. The overall mood is that of a bustling marketplace — generous whitespace around hero banners, tight stacking in product grids, and a persistent yellow accent that signals urgency without aggression. Social icons and payment badges (Visa, PayPal, Klarna) sit in the footer in their native brand colors (#3b5998, #1da1f2, #dd4b39), kept separate from the core palette. The brand trusts its teal-and-marigold voltage to carry the user from browse to cart, with the checkout flow rendered in a clean, monochrome surface.

colors:
  primary: "#108474"
  primary-active: "#0d6b5c"
  primary-disabled: "#a3d4c8"
  ink: "#222222"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#aaaaaa"
  hairline: "#e9e9e9"
  hairline-soft: "#f2f2f2"
  canvas: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#f5af19"
  accent-marigold-active: "#d2920f"
  accent-marigold-soft: "#fffb00"
  badge-red: "#c8102e"
  badge-red-soft: "#fafafa"
  star-rating: "#fbcd0a"
  social-facebook: "#3b5998"
  social-twitter: "#1da1f2"
  social-google: "#dd4b39"
  social-pinterest: "#e60023"
  social-linkedin: "#0073b1"
  social-youtube: "#ff0000"
  payment-klarna: "#ffb3c7"
  payment-paypal: "#003087"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.15px
  link:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-marigold-active:
    backgroundColor: "{colors.accent-marigold-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-pill-teal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.badge-red}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-bar-link:
    color: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.md}"
  nav-bar-link-active:
    color: "{colors.accent-marigold-soft}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-pill-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    margin-top: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    font-weight: 600
  product-card-sale-badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-stock-badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.lg}"
    rounded: "{rounded.md}"
  hero-banner-accent:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xl} {spacing.lg}"
    rounded: "{rounded.md}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  filter-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  filter-dropdown-active:
    border: "2px solid {colors.primary}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  pagination-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.body}"
    typography: "{typography.link}"
  footer-social-icon:
    width: 24px
    height: 24px
    rounded: "{rounded.full}"
  cart-icon:
    color: "{colors.on-primary}"
    fontSize: 20px
  cart-badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.full}"
    width: 20px
    height: 20px
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  checkout-button-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  checkout-summary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  loading-spinner:
    color: "{colors.primary}"
    width: 32px
    height: 32px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in teal #108474 with white text and {rounded.sm} corners. On hover, it shifts to `{colors.primary-active}` (#0d6b5c); the disabled state uses `{colors.primary-disabled}` (#a3d4c8) with reduced opacity. Used for "Add to Cart", "Checkout", and "Sign Up" actions. **`button-secondary`** — An outlined variant with a white background and teal border, used for "View Details" and "Cancel" actions. Hover fills the background with `{colors.surface-soft}`. **`button-accent-marigold`** — The urgency variant in #f5af19 with dark ink text, reserved for "Sale", "Limited Stock", and "Pre-Order" CTAs. Active state deepens to #d2920f. **`button-pill-teal`** — A fully rounded pill in teal, used for category filters and "Shop Now" hero links. **`button-pill-outline`** — A transparent pill with a 2px teal border, used for secondary filter toggles and "Learn More" links.

### Navigation
**`nav-bar`** — A fixed top bar at 64px height, filled with `{colors.primary}` (#108474). Navigation links are white, uppercase, set in `{typography.nav-link}` (14px/600). The active link is highlighted with `{colors.accent-marigold-soft}` (#fffb00). The cart icon sits on the right, with a marigold badge showing item count. **`nav-bar-link`** — Individual links with 16px horizontal padding. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

### Cards
**`product-card`** — A white card with {rounded.md} (12px) corners and 8px padding, containing an image, title, price, and optional badges. The image uses {rounded.sm} (8px) corners. The title is set in `{typography.title-sm}` (16px/600) in ink, while the price uses `{typography.body-md}` (16px/400) in teal. **`product-card-sale-badge`** — A small marigold badge with uppercase text, pinned to the top-left corner of the image. **`product-card-stock-badge`** — A red (#c8102e) badge for "Sold Out" or "Low Stock" labels.

### Forms
**`text-input`** — A 44px-tall input with a 1px hairline border, {rounded.sm} corners, and 16px horizontal padding. On focus, the border thickens to 2px teal. Error state uses a 2px red border. **`filter-dropdown`** — A 40px-tall select element with a hairline border, used for sorting and category filtering. Active state mirrors the input focus style.

### Hero & Banners
**`hero-banner`** — A teal (#108474) banner with white text, set in `{typography.display-lg}` (28px/700). Used for seasonal promotions and new arrivals. **`hero-banner-accent`** — A marigold (#f5af19) variant with dark ink text, used for clearance sales and limited-time offers.

### Footer
**`footer-section`** — A light gray (#f2f2f2) footer with muted text, containing links, social icons, and payment badges. Social icons are rendered as 24px circles with their respective brand colors. Payment badges (Visa, PayPal, Klarna) are displayed in their native colors.

### Miscellaneous
**`star-rating`** — Gold (#fbcd0a) stars at 16px, used on product cards and review sections. **`pagination-button`** — A 36px-tall button in `{colors.surface-soft}` for page navigation; the active page uses teal. **`loading-spinner`** — A teal (#108474) spinner at 32px, used during product list loading and checkout processing.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product grid goes single-column (1 card); hero banners stack vertically; search bar moves below nav; footer links stack |
| Tablet | 744–1128px | Nav remains horizontal but compresses; product grid shows 2-3 columns; hero banners use 50% width; filter bar collapses into a single dropdown |
| Desktop | 1128–1440px | Full nav with all links; product grid shows 4 columns; hero banners span full width; filter bar expands to horizontal row |
| Wide | > 1440px | Max-width container at 1440px; product grid shows 5 columns; extra whitespace around hero and footer; category pills wrap in a single row |

### Touch Targets
- All buttons and links: minimum 44px height (WCAG AAA for mobile)
- Product card tap targets: minimum 48px for price, title, and badge areas
- Filter dropdowns and text inputs: 44px height for comfortable tapping
- Nav bar links: 48px tap area (padding ensures hit target)
- Cart icon and hamburger menu: 48px x 48px touch zone

### Collapsing Strategy
- Top nav: collapses to hamburger menu on mobile (< 744px)
- Category pill strip: wraps to multiple rows on tablet, collapses to a single dropdown on mobile
- Filter bar: horizontal row on desktop, collapses to a single "Filter" button on mobile
- Footer: 4-column layout on desktop, stacks to single column on mobile
- Hero banners: side-by-side on desktop, stack vertically on mobile
- Product grid: 4-5 columns on desktop, 2-3 on tablet, 1 on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links were inferred from the primary color; exact hover hex values were not extracted from the live site.
- Error styling for forms (red border, error message typography) is assumed based on common e-commerce patterns; no error state CSS was found.
- Dark mode is not supported; no dark-mode CSS variables were detected.
- Sub-brand palettes (e.g., for "Pre-Order" vs "Sale" vs "Limited Edition") were not extracted; the marigold accent is used for all urgency badges.
- The font stack includes "JudgemeIcons" and "JudgemeStar" for review widgets, but their exact usage and sizing were not captured.
- Payment gateway colors (Klarna, PayPal) are assumed from their brand guidelines; the site may use different shades.
- The meta theme-color (#4C576A) is a slate gray that does not match the primary teal; it may be a fallback or legacy value.
- No animation or transition durations were extracted; all motion is assumed at 200ms ease-in-out.
- The extracted hex list includes many grays and social-icon colors; the true brand palette (teal + marigold) was identified by frequency and distinctiveness, but secondary accents (e.g., for "New" badges) may exist.
