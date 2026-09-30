---
version: alpha
name: "Mondo"
source_url: "https://mondoshop.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A collector's fever dream rendered in a red-and-blue voltage that feels like a movie poster come to life. The primary red `#d63021` — a stop-sign, blood-drop, candy-apple red — is the brand's nervous system, appearing on every add-to-cart button, every badge, every sale flag. It's paired with a deep, almost cobalt blue `#0073ce` that reads as the cool counterpoint: think midnight sky behind a neon sign. The canvas is a clean `#ffffff` with hairline strokes in `#dedede` and `#dadada` that carve out product cards and grid sections with surgical precision. Type runs Poppins at modest weights — 400 for body, 600 for titles — giving the whole system a geometric, slightly retro-futuristic feel that matches the action-figure and poster art. There is no softness here: corners are either razor-sharp (`{rounded.none}`) or fully pill-shaped (`{rounded.full}`), with nothing in between. The `#121212` ink anchors text and icons, while `#4d4d4d` muted handles secondary copy. The brand trusts its product photography — high-contrast, saturated, often against black or gradient backdrops — to do the heavy lifting, letting the UI stay out of the way. Buttons are chunky and confident, with 48px heights and 16px horizontal padding that invite the click. The nav bar is a simple white strip with the Mondo logotype centered, flanked by dropdown menus and a cart icon — no search bar visible until you click the magnifying glass. This is a system built for the scroll-and-scan behavior of collectors hunting for limited drops: fast, visual, and unapologetically loud.

colors:
  primary: "#d63021"
  primary-active: "#b0261a"
  primary-disabled: "#f5b3ad"
  ink: "#121212"
  body: "#4d4d4d"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#dedede"
  hairline-soft: "#dadada"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#0073ce"
  accent-blue-active: "#005ba3"
  star-rating: "#121212"
  badge-sold-out: "#4d4d4d"
  badge-new: "#d63021"
  badge-sale: "#d63021"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  link:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
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
    rounded: "{rounded.none}"
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 23px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 32px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 15px
    height: 32px
    border: "1px solid {colors.hairline}"
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-dropdown-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  search-icon-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: 24px
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-grid:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
    gap: "{spacing.lg}"
  product-detail-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.xl} {spacing.lg}"
  product-detail-title:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
  product-detail-price:
    typography: "{typography.display-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.sm}"
  product-detail-description:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.base}"
    lineHeight: 1.6
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 56px
    width: "100%"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.canvas}"
    hoverTextColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.canvas}"
    textTransform: uppercase
    letterSpacing: "0.5px"
    marginBottom: "{spacing.base}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 48px
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: "400px"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.canvas}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
    marginTop: "{spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    marginTop: "{spacing.lg}"
  category-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "{spacing.base} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline}"
  category-link:
    typography: "{typography.nav-link}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} {spacing.base}"
    hoverTextColor: "{colors.primary}"
  category-link-active:
    typography: "{typography.nav-link}"
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.base} {spacing.lg}"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.body}"
    hoverTextColor: "{colors.primary}"
  breadcrumb-current:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
  pagination-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  loading-spinner:
    borderColor: "{colors.hairline}"
    borderTopColor: "{colors.primary}"
    height: 32px
    width: 32px
  error-message:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  success-message:
    backgroundColor: "#e8f5e9"
    textColor: "#2e7d32"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call to action, rendered in the brand's signature red `#d63021` with white text and zero border radius. This is the workhorse of the system, used for "Add to Cart", "Pre-order", and "Shop Now" actions. On hover, it shifts to `#b0261a` for a subtle but confident darkening. The disabled state uses `#f5b3ad` to signal unavailability without competing with the active red.

**`button-secondary`** — An outlined button with a 2px solid black border on a white background. Used for secondary actions like "View Details" or "Learn More". On hover, the background fills with black and text inverts to white, creating a satisfying flip effect. The border keeps the button grounded even when adjacent to the primary red.

**`button-tertiary-text`** — A text-only button in the brand red, used for inline actions like "Clear filters" or "See all". No background, no border — just the red text on white, relying on the color's natural visual weight to signal clickability.

**`button-pill-primary`** — A compact, fully pill-shaped button in the brand red, used for filter chips, tag badges, and small-scale CTAs within product cards. The `{rounded.full}` shape creates a friendly, badge-like appearance that contrasts with the system's otherwise sharp corners.

**`button-pill-outline`** — The outlined counterpart to the pill button, used for inactive filter states or "Sold Out" tags. The 1px hairline border keeps it present without competing with the active pill.

### Navigation
**`top-nav`** — A 72px white bar with a 1px bottom hairline. The Mondo logotype sits centered, flanked by uppercase nav links in Poppins 500 at 13px with 0.5px letter spacing. Dropdown menus appear on hover for categories like "Art Prints", "Action Figures", and "Vinyl". The cart icon and search trigger sit on the right edge.

**`nav-dropdown-trigger`** — The clickable/hoverable element that opens a dropdown menu. Styled as a simple text link with 8px vertical padding for a generous hit area.

**`nav-dropdown-menu`** — A white dropdown panel with a subtle box shadow, containing category sub-links. No border radius — the sharp corners match the system's aesthetic.

**`search-icon-trigger`** — A 40px circular icon button that toggles the search overlay. No background by default, but gains a soft gray fill on hover.

**`search-overlay`** — A full-width white panel that drops down from the nav bar when search is activated. Contains the search input and suggested results.

**`search-input`** — A 48px tall input with a soft gray background and 1px hairline border. The sharp corners keep it consistent with the system, while the generous height makes it easy to type on mobile.

**`category-nav`** — A horizontal strip of category links below the hero, with a bottom hairline. Active categories get a 2px red underline, while inactive ones use the body gray with a red hover state.

### Cards
**`product-card`** — A white card with no border radius, containing a product image, title, price, and optional badge. The card relies on the product photography and generous whitespace for visual separation rather than shadows or borders.

**`product-card-image`** — The image area of the card, with a soft gray background that serves as a placeholder before the image loads. No border radius — the image fills the card edge to edge.

**`product-card-badge`** — An absolute-positioned badge in the brand red, placed at the top-left of the card. Uses uppercase Poppins 600 at 11px with 0.5px letter spacing. Used for "New", "Sale", or "Pre-order" labels.

**`product-card-badge-sold-out`** — A gray version of the badge for sold-out items. The muted color signals unavailability without the emotional weight of the red.

### Product Detail
**`product-detail-section`** — The main content area for a product detail page, with generous padding on all sides.

**`add-to-cart-button`** — A full-width, 56px tall button in the brand red. The increased height and width make it the most prominent element on the page, designed to capture the impulse purchase moment.

**`quantity-selector`** — A 48px tall input with a soft gray background and hairline border, used for adjusting item quantities. The sharp corners and simple styling keep it from competing with the primary CTA.

### Footer
**`footer`** — A black (`#121212`) footer section with white text. The dark background creates a strong visual anchor at the bottom of the page, with the brand red used sparingly for link hover states.

**`footer-heading`** — Uppercase headings in the footer, using Poppins 600 at 14px with 0.5px letter spacing. The uppercase treatment adds a sense of structure and hierarchy.

**`newsletter-input`** — A white input on the dark footer background, with a hairline border. The contrast makes it easy to find and use.

**`newsletter-submit`** — A red submit button paired with the newsletter input, using the smaller button typography to match the input's scale.

### Hero
**`hero-section`** — A full-width section with a black background and white text, used for featured collections and major announcements. The dark backdrop makes the product imagery pop, especially for brightly colored action figures and posters.

**`hero-cta`** — The primary call to action within the hero, using the standard button-primary styling with additional horizontal padding for visual weight.

### States & Feedback
**`loading-spinner`** — A 32px circular spinner with a gray track and red top border. The red accent keeps the loading state on-brand.

**`error-message`** — A light red background with the brand red text, used for form validation errors and API failures.

**`success-message`** — A light green background with dark green text, used for success confirmations like "Added to cart" or "Order placed".

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 items), hamburger menu replaces top nav, search becomes full-screen overlay, product cards stack vertically, hero section reduces to 300px min-height, footer links stack in single column |
| Tablet | 744–1128px | Two-column product grid, top nav remains visible but dropdowns become tap-to-open, search overlay is full-width but not full-screen, hero section maintains 400px height |
| Desktop | 1128–1440px | Three-column product grid, full top nav with hover dropdowns, search is a compact overlay, hero section at 400px with wider content padding |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero section at 500px with larger typography, additional whitespace around product cards |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px for mobile touch compliance
- Icon buttons are 40px × 40px minimum
- Nav links have 8px vertical padding for comfortable tapping
- Product card images are tappable with no minimum size requirement (image fills card width)
- Quantity selector has 48px height for easy stepper interaction

### Collapsing Strategy
- Top nav collapses to a hamburger menu on mobile (< 744px), with a slide-out drawer for category navigation
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer link columns collapse from 4 columns to 2 at tablet, to 1 at mobile
- Hero section collapses from side-by-side layout to stacked on mobile
- Category nav collapses from horizontal scroll to a dropdown selector on mobile
- Search overlay transitions from a compact panel on desktop to a full-screen modal on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components were inferred from common patterns; actual Mondo hover behaviors may differ (e.g., subtle scale transforms, color transitions)
- Error and success message styling is assumed based on common e-commerce patterns; actual Mondo implementations may use different colors or icons
- Dropdown menu animation and timing (fade, slide, duration) could not be extracted
- Mobile hamburger menu animation and drawer behavior (slide from left vs. right, overlay vs. push) is unknown
- Product card hover effects (zoom on image, shadow elevation, border highlight) are not confirmed
- Add-to-cart animation (micro-interaction, confirmation toast, cart badge update) is not documented
- Font weights beyond 400 and 600 are assumed; actual Mondo usage may include 300 or 700 weights
- Line heights and letter spacing values are estimated based on standard Poppins typography; actual values may vary
- Dark mode is not present on the live site and is not documented
- Sub-brand or collection-specific color palettes (e.g., for Marvel, DC, or Disney licensed products) are not captured
- Checkout flow styling (Shopify checkout, payment method buttons) uses default Shopify theme colors and is not part of Mondo's design system
- Social media icon colors (Facebook blue, Twitter blue, Instagram gradient) are platform defaults and not brand colors
- The extracted color list includes `#0073ce` which appears as an accent blue on the site; its exact usage (links, badges, secondary CTAs) is inferred from context
