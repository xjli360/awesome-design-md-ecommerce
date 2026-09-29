---
version: alpha
name: "Reference Recordings"
source_url: "https://www.referencerecordings.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep navy #3c65a6 anchors a catalog that has been promising "The Best Seat in the House" since 1976, a phrase that is not marketing fluff but a literal contract with the listener. The brand's visual system operates like a high-end recording session: a clean white canvas (#f5f5f5) for the body, near-white surface cards (#ebebeb) for product thumbnails, and a near-black ink (#171a21) for editorial copy that carries the weight of liner notes. The primary blue (#3c65a6) appears on the top nav bar, the primary CTA buttons, and the site's header — a cool, authoritative signal that this is a label, not a streaming service. Secondary accents surface as muted grays (#777777, #545b62) for secondary text and borders, while a suite of utility colors (#d39e00 for warnings, #1e7e34 for success, #bd2130 for errors) suggests a checkout and account system that prioritizes clarity over charm. Typography runs system-native — Arial, Helvetica Neue, and their fallbacks — in a pragmatic, no-nonsense stack that prioritizes legibility over personality. Buttons use a modest {rounded.sm} radius, product cards a slightly softer {rounded.md}, and the overall spacing rhythm is generous ({spacing.base} gutters, {spacing.lg} between sections) to let the album art breathe. The brand does not chase trends; it builds a quiet, trustworthy container for the music.

colors:
  primary: "#3c65a6"
  primary-active: "#004085"
  primary-disabled: "#b3d7ff"
  ink: "#171a21"
  body: "#383d41"
  muted: "#777777"
  muted-soft: "#818182"
  hairline: "#dae0e5"
  hairline-soft: "#ebebeb"
  canvas: "#f5f5f5"
  surface-soft: "#ebebeb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#1e7e34"
  warning: "#d39e00"
  error: "#bd2130"
  info: "#117a8b"
  error-bg: "#f1b0b7"
  success-bg: "#b1dfbb"
  warning-bg: "#ffe8a1"
  info-bg: "#abdde5"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-danger:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    boxShadow: "0 0 0 3px {colors.primary-disabled}"
  text-input-error:
    border: "2px solid {colors.error}"
    boxShadow: "0 0 0 3px {colors.error-bg}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
  nav-link-active:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "3px solid {colors.on-primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 2px 4px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.15)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-subtitle:
    typography: "{typography.body-lg}"
    marginTop: "{spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  alert-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.success}"
  alert-error:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.error}"
  alert-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.warning}"
  alert-info:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.info}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.info}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  pagination-disabled:
    textColor: "{colors.muted}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    textColor: "{colors.primary}"
  breadcrumb-separator:
    textColor: "{colors.muted}"
    margin: "0 {spacing.xs}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.lg} 0"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's deep navy (#3c65a6) and white text. Uses a modest {rounded.sm} radius and 44px height for comfortable tapping. On hover/active, shifts to a darker navy (#004085). Disabled state uses a light blue (#b3d7ff) to signal inactivity without visual noise.
**`button-secondary`** — An outlined variant with a white fill and navy border, used for secondary actions like "View Details" alongside a primary CTA. Active state darkens the border and adds a light gray background (#ebebeb). Maintains the same 44px height and {rounded.sm} radius as the primary.
**`button-tertiary-text`** — A text-only button with no background or border, used for low-emphasis actions like "Cancel" or "Learn More." Hover state adds a subtle underline.
**`button-success`** — A green (#1e7e34) filled button for confirmatory actions like "Add to Cart" or "Checkout." Shares the same dimensions and radius as the primary button.
**`button-danger`** — A red (#bd2130) filled button for destructive actions like "Remove from Cart." Uses the same structural tokens as the primary button.

### Cards
**`product-card`** — A white card with a subtle shadow (0 2px 4px rgba(0,0,0,0.08)) and {rounded.md} corners. Contains a square album art image with {rounded.sm} corners, the album title in title-sm, and the price in a bold 18px weight. On hover, the shadow deepens to 0 4px 12px rgba(0,0,0,0.15) for a subtle lift effect. A badge variant overlays a small yellow (#d39e00) pill in the top-left corner for "New Release" or "Sale" labels.
**`product-card-image`** — The album art container, maintaining a 1:1 aspect ratio with {rounded.sm} corners. Designed to showcase the label's high-resolution cover art without distortion.

### Navigation
**`nav-bar`** — A fixed-height (64px) top bar filled with the primary navy (#3c65a6). Contains the brand logo on the left and navigation links on the right, all in white text. The bar spans the full viewport width with {spacing.lg} horizontal padding.
**`nav-link`** — White text links with {spacing.sm} vertical and {spacing.md} horizontal padding. The active state adds a 3px white bottom border for clear indication of the current section.
**`breadcrumb`** — A secondary navigation pattern using muted gray (#777777) text for the current page and navy (#3c65a6) for clickable parent pages. Separators are simple slashes with {spacing.xs} margins.

### Forms
**`text-input`** — A standard input field with a white background, 1px hairline border (#dae0e5), and {rounded.sm} corners. On focus, the border thickens to 2px navy with a 3px light blue (#b3d7ff) box-shadow ring. Error state swaps to a 2px red (#bd2130) border with a pink (#f1b0b7) shadow ring.
**`select-input`** — A dropdown selector sharing the same dimensions and styling as the text input, with a custom chevron indicator in the muted gray.

### Alerts
**`alert-success`** — A green-tinted banner (#b1dfbb background, #1e7e34 text) with a solid green border, used for success confirmations like "Item added to cart." Uses {rounded.sm} and {spacing.md} internal padding.
**`alert-error`** — A pink-tinted banner (#f1b0b7 background, #bd2130 text) with a red border, used for error messages like "Invalid coupon code."
**`alert-warning`** — A yellow-tinted banner (#ffe8a1 background, #d39e00 text) with a gold border, used for warnings like "Limited stock."
**`alert-info`** — A teal-tinted banner (#abdde5 background, #117a8b text) with a teal border, used for informational messages like "Free shipping on orders over $50."

### Other Components
**`hero-section`** — A full-width navy (#3c65a6) banner at the top of key pages, containing the page title in display-xl (32px) and a subtitle in body-lg (18px). Minimum height of 400px to create a strong visual anchor.
**`search-bar`** — A pill-shaped ({rounded.full}) search input with a white background and 1px hairline border. On focus, the border switches to 2px navy. Designed to sit within the hero section or as a standalone element.
**`footer`** — A dark (#171a21) footer spanning the full viewport width, with muted gray (#818182) text links that lighten to white on hover. Contains copyright, legal links, and social media icons.
**`pagination`** — A row of numbered page links in navy, with the active page filled in navy with white text. Disabled pages (e.g., "Previous" on page 1) appear in muted gray.
**`divider`** — A 1px horizontal rule in hairline gray (#dae0e5), used to separate sections within a page. Margin of {spacing.lg} on both sides.
**`section-header`** — A display-md (24px) heading in the ink color (#171a21) with {spacing.lg} bottom margin, used to introduce content sections like "New Releases" or "Best Sellers."

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row); nav-bar collapses to hamburger menu; hero-section reduces to 300px min-height with 24px font; search-bar moves below hero; footer stacks links vertically |
| Tablet | 744–1128px | Two-column product grid (2 cards per row); nav-bar shows all links with reduced padding; hero-section maintains 400px height; search-bar sits inline in hero |
| Desktop | 1128–1440px | Three-column product grid (3 cards per row); full nav-bar with standard padding; hero-section at full height; search-bar centered in hero |
| Wide | > 1440px | Four-column product grid (4 cards per row); max-width container (1440px) centered; hero-section may include parallax background; search-bar expands to 600px max-width |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height (Apple HIG guideline).
- Nav links have at least 44px tap area via padding.
- Product cards have a minimum 120px width on mobile to ensure tap targets are large enough.
- Search bar maintains 48px height for comfortable tapping.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer.
- Product grid collapses from 4 columns (wide) to 1 column (mobile).
- Footer link columns collapse from a horizontal row to a vertical stack on mobile.
- Hero section reduces padding and font size on mobile to avoid excessive scrolling.
- Breadcrumbs may truncate on mobile, showing only the current page and a "Back" link.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for most components were inferred from common patterns; the live site's actual hover colors (e.g., for nav links, product cards, secondary buttons) could not be reliably extracted.
- Error, warning, success, and info colors were derived from Bootstrap-like utility classes present in the extracted hex list; the brand may use custom variants for these states.
- Typography weights and sizes are estimated based on common system font usage; the actual font stack may include additional weights (e.g., 300, 500) not captured in the extracted font-family declarations.
- The brand's logo and icon system (SVG, custom icons, social media icons) could not be extracted; colors for these elements are not included.
- Dark mode or high-contrast mode variants are not documented.
- The extracted hex list is heavily polluted with Bootstrap defaults and checkout-widget colors (e.g., #0062cc, #1e7e34, #bd2130). The primary (#3c65a6) was chosen as the most distinctive non-framework color, but the brand may have a secondary accent or a different primary in production that was not captured.
- Spacing values (padding, margin, section gaps) are estimated based on common e-commerce patterns; the actual design may use different values.
- The brand's "Since 1976" tagline and "The Best Seat in the House" slogan are present in the page title but their visual treatment (typography, placement) could not be extracted.
- Album art and product photography styling (borders, shadows, hover effects) are inferred; the actual implementation may differ.
- Checkout flow components (cart, payment forms, order summary) are not documented as their styling could not be reliably separated from Shopify/third-party widget defaults.
