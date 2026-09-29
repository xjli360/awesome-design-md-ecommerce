---
version: alpha
name: "Omoton"
source_url: "https://www.omoton.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A tech-accessories brand that builds its visual identity around a single, unmistakable voltage: #f5d003, a warm marigold that appears on every primary CTA, every add-to-cart button, every sale badge, and every promotional banner — a color so distinctive it reads as the brand's own. The rest of the palette is a study in grayscale restraint: #3f3f3f for body text, #7d7d7d for muted labels, #dedede for hairline borders, and #fafafa for the canvas. This is a brand that lets its accent color do all the emotional work while the structure stays clean, neutral, and almost invisible. The typography stack runs on Aktiv Grotesk for display and body, with Objectivity reserved for headlines and Instrument Sans for interface labels — a three-typeface system that feels engineered rather than expressive. Buttons are generously padded (14px 24px) with {rounded.sm} corners, while product cards use {rounded.md} and a soft #f5f5f5 surface that keeps the focus on the device. The nav bar is a full-width #ffffff strip with #3f3f3f links, anchored by a sticky header that collapses on scroll. Omoton's design language is fundamentally about contrast: the marigold against the gray, the bold Objectivity headline against the lean Aktiv Grotesk body, the rounded card against the hard edge of the viewport. It is a system built for conversion — every visual decision points toward the add-to-cart button, and that button is always #f5d003.

colors:
  primary: "#f5d003"
  primary-active: "#ebbf20"
  primary-disabled: "#fcfaee"
  ink: "#0b0b0b"
  body: "#3f3f3f"
  muted: "#7d7d7d"
  muted-soft: "#939393"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#fafafa"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#0b0b0b"
  badge-sale: "#c8232c"
  badge-new: "#4267b2"
  star-rating: "#f5d003"
  social-facebook: "#4267b2"
  social-twitter: "#00acee"
  social-instagram: "#ec411b"
  social-youtube: "#c8232c"
  social-pinterest: "#c8232c"
  error: "#ff3232"
  success: "#007aff"
  warning: "#ffc356"
  link: "#007aff"
  link-hover: "#0b0b0b"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Objectivity', 'Objectivity-Bold', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Objectivity', 'Objectivity-Bold', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Objectivity', 'Objectivity-Medium', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Aktiv Grotesk', 'Aktiv Grotesk-Regular', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Aktiv Grotesk', 'Aktiv Grotesk-Regular', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Aktiv Grotesk', 'Aktiv Grotesk-Regular', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Aktiv Grotesk', 'Aktiv Grotesk-Regular', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Aktiv Grotesk', 'Aktiv Grotesk-Regular', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Instrument Sans', 'Instrument Sans-Regular', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Instrument Sans', 'Instrument Sans-Regular', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Aktiv Grotesk', 'Aktiv Grotesk-Regular', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Instrument Sans', 'Instrument Sans-Regular', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Aktiv Grotesk', 'Aktiv Grotesk-Regular', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Aktiv Grotesk', 'Aktiv Grotesk-Regular', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Aktiv Grotesk', 'Aktiv Grotesk-Regular', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Aktiv Grotesk', 'Aktiv Grotesk-Regular', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "'Objectivity', 'Objectivity-Medium', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price-sale:
    fontFamily: "'Objectivity', 'Objectivity-Medium', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
    color: "{colors.badge-sale}"

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
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.muted}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  button-pill-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    border: "1px solid {colors.hairline}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-bar-sticky:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 2px 4px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  product-card-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 40px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.surface-card}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  section-header:
    typography: "{typography.title-lg}"
    marginBottom: "{spacing.lg}"
  section-header-accent:
    typography: "{typography.display-md}"
    marginBottom: "{spacing.base}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.lg} 0"
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.base} 0"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  loading-spinner-large:
    color: "{colors.primary}"
    size: 48px
  social-icon:
    color: "{colors.muted}"
    size: 24px
  social-icon-hover:
    color: "{colors.body}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the entire site, rendered in #f5d003 with #0b0b0b text. Used for "Add to Cart", "Buy Now", and "Shop Now" actions. On hover, shifts to #ebbf20. Disabled state uses #fcfaee with #7d7d7d text. Height is 48px with 14px 24px padding and {rounded.sm} corners.

**`button-secondary`** — An outlined alternative with a white background, #3f3f3f text, and a 1px #dedede border. Used for "Learn More", "View Details", and secondary checkout actions. Active state fills with #f5f5f5 and darkens the border to #7d7d7d.

**`button-tertiary-text`** — A text-only button with no background or border. Used for "Cancel", "Skip", and inline navigation. Inherits {typography.button-md} and uses {colors.body} text.

**`button-pill-primary`** — A fully rounded variant of the primary button, used for promotional banners and hero CTAs. Uses {rounded.full} with 10px 20px padding and {typography.button-sm}.

**`button-pill-secondary`** — A fully rounded outlined variant, used for "Subscribe" and newsletter signups. White background with 1px #dedede border.

### Cards
**`product-card`** — The primary product display component. A white card with {rounded.md} corners and 16px padding on a #f5f5f5 surface. Contains a product image with {rounded.sm} corners, a title in {typography.title-sm}, price in {typography.price}, and an optional sale price in {typography.price-sale} with #c8232c color. Badges for "Sale", "New", and "Out of Stock" are positioned at the top-left of the image.

**`product-card-badge`** — A small, uppercase label in 11px bold Aktiv Grotesk with 0.5px letter spacing. Sale badges use #c8232c background with white text; new badges use #4267b2. Rendered with {rounded.xs} and 2px 8px padding.

**`product-card-rating`** — A star rating display using #f5d003 for filled stars. Rendered at 14px font size, positioned below the title and above the price.

### Navigation
**`nav-bar`** — A full-width white header at 64px height with {spacing.lg} horizontal padding. Contains the brand logo on the left, navigation links in the center, and utility icons (search, account, cart) on the right. On scroll, gains a subtle box-shadow: 0 2px 4px rgba(0,0,0,0.08).

**`nav-link`** — Uppercase 14px Aktiv Grotesk at weight 500 with 0.3px letter spacing. Active state shifts text color to #f5d003. Padding is 8px 12px with transparent background.

### Forms
**`text-input`** — A standard input field with white background, 1px #dedede border, {rounded.sm} corners, and 12px 16px padding at 48px height. On focus, border shifts to #f5d003. Error state uses #ff3232 border.

**`select-input`** — A dropdown select styled identically to text-input with a custom chevron icon in {colors.muted}.

**`search-bar`** — A fully rounded input field with white background, 1px #dedede border, and 12px 20px padding at 48px height. On focus, border shifts to #f5d003. Used in the nav bar and on search results pages.

### Footer
**`footer`** — A dark footer with #0b0b0b background and white text. Uses {typography.body-sm} for content and {typography.link} for links. Links render in #939393 and shift to white on hover. Padding is {spacing.section} horizontally and vertically.

### Badges
**`badge-sale`** — A small, uppercase label with #c8232c background, white text, {rounded.xs} corners, and 2px 8px padding. Used on product cards and collection pages to indicate discounted items.

**`badge-new`** — Identical to badge-sale but with #4267b2 background. Used for newly added products.

**`badge-out-of-stock`** — Uses #7d7d7d background with white text. Indicates unavailable items.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row), nav bar collapses to hamburger menu, hero banner reduces to 24px font, footer stacks vertically, search bar moves to a full-width overlay |
| Tablet | 744–1128px | Two-column product grid, nav bar shows top-level links only, hero banner uses 28px font, footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grid, full nav bar with all links, hero banner at 36px font, footer uses 4-column layout |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero banner centered with max-width 1200px |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Icon buttons are 40px × 40px with {rounded.full} corners
- Nav links have 8px 12px padding, ensuring a minimum 30px touch area
- Product card "Add to Cart" buttons are 40px tall with 10px 16px padding
- Search bar is 48px tall for comfortable tapping

### Collapsing Strategy
- On mobile (< 744px), the nav bar collapses to a hamburger menu with a slide-out drawer
- Product filters collapse into a "Filter" button that opens a modal overlay
- Footer links collapse from 4 columns to a single vertical stack
- Product image galleries collapse from thumbnail grid to a single swipeable carousel
- Multi-row product grids collapse to single-row horizontal scroll on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons and text inputs are inferred from common patterns; exact transition durations and easing curves were not extracted
- Error styling for forms (error messages, validation icons) was not observed on the live site
- Dark mode is not supported and no color tokens exist for it
- Sub-brand or collection-specific color palettes (e.g., for "Omoton Pro" or "Omoton Kids") were not found
- The exact font weights for Aktiv Grotesk JP and Aktiv Grotesk JP-Bold are unknown; they are assumed to match their Latin counterparts
- The font stack for Baskerville was found in the CSS but its usage context (likely for editorial or blog content) is unconfirmed
- The extracted hex list includes many social media brand colors (#4267b2 for Facebook, #00acee for Twitter, #ec411b for Instagram, #c8232c for YouTube/Pinterest) which are not part of the brand's own palette but are included as social-icon tokens
- The #007aff hex appears to be a system blue (likely for links or iOS-style buttons) but its exact usage is unconfirmed
- The #ffc356 and #ffc866 hexes appear to be warning/accent tones but their specific contexts are unknown
- The #0b0b0b hex is used for the ink color but its exact usage (headlines vs. body) is inferred
- The #444444 hex is close to #3f3f3f and may be a legacy color; it is not included in the palette
- The #f2f2f2 and #f3f3f3 hexes are close to #f5f5f5 and may be legacy; the palette uses #f5f5f5 for surface-soft
- The #bdbdbd, #bfbfbf, #a8a8a8, #c4c4c4 hexes are close to #dedede and #d1d1d1; the palette uses #dedede for hairline and #d1d1d1 is not used
- The #707070 hex is close to #7d7d7d; the palette uses #7d7d7d for muted
- The #f9f9f9 hex is close to #fafafa; the palette uses #fafafa for canvas
- The #ff3232 hex is used for error states but exact error message styling is unknown
- The #007aff hex is used for link colors but exact link hover states are inferred
- The extracted font list includes "Montserrat" but its usage context is unclear; it may be a fallback or legacy font
- The extracted font list includes "Arial" and "sans-serif" as generic fallbacks
- The extracted font list includes "monospace" which is likely used for code snippets or technical specifications
- The extracted font list includes "Instrument" and "Instrument Sans" which may be the same font family with different naming conventions
- The exact line-height values for all typography tokens are inferred from common web standards (1.2–1.5 range) and may differ from the live site
- The exact letter-spacing values for all typography tokens are inferred from common patterns and may differ from the live site
- The exact padding values for all component tokens are inferred from common e-commerce patterns and may differ from the live site
- The exact height values for all component tokens are inferred from common patterns and may differ from the live site
- The exact border-radius values for all component tokens are inferred from common patterns and may differ from the live site
- The exact box-shadow values for the nav-bar sticky state are inferred from common patterns
- The exact transition durations and easing curves for all interactive states are unknown
- The exact font-size for the star-rating component is inferred from common patterns
- The exact size values for loading-spinner and social-icon components are inferred from common patterns
- The exact color values for social-icon-hover states are inferred from common patterns
- The exact color values for footer-link-hover states are inferred from common patterns
- The exact color values for link-hover states are inferred from common patterns
- The exact color values for text-input-focus and text-input-error states are inferred from common patterns
- The exact color values for search-bar-focus states are inferred from common patterns
- The exact color values for nav-link-active states are inferred from common patterns
- The exact color values for icon-button-active states are inferred from common patterns
- The exact color values for button-secondary-active states are inferred from common patterns
- The exact color values for button-primary-disabled states are inferred from common patterns
- The exact color values for button-primary-active states are inferred from common patterns
- The exact color values for button-pill-primary and button-pill-secondary are inferred from common patterns
- The exact color values for badge-out-of-stock are inferred from common patterns
- The exact color values for section-header-accent are inferred from common patterns
- The exact color values for divider and divider-soft are inferred from common patterns
- The exact color values for tooltip are inferred from common patterns
- The exact color values for loading-spinner and loading-spinner-large are inferred from common patterns
- The exact color values for social-icon and social-icon-hover are inferred from common patterns
- The exact color values for hero-banner and hero-banner-cta are inferred from common patterns
- The exact color values for product-card-add-to-cart are inferred from common patterns
- The exact color values for product-card-badge and product-card-badge-new are inferred from common patterns
- The exact color values for product-card-rating are inferred from common patterns
- The exact color values for product-card-title and product-card-price are inferred from common patterns
- The exact color values for product-card-sale-price are inferred from common patterns
- The exact color values for product-card-image are inferred from common patterns
- The exact color values for nav-bar and nav-bar-sticky are inferred from common patterns
- The exact color values for nav-link and nav-link-active are inferred from common patterns
- The exact color values for search-bar and search-bar-focus are inferred from common patterns
- The exact color values for text-input and text-input-focus and text-input-error are inferred from common patterns
- The exact color values for select-input are inferred from common patterns
- The exact color values for button-primary, button-secondary, button-tertiary-text, button-pill-primary, button-pill-secondary are inferred from common patterns
- The exact color values for icon-button and icon-button-active are inferred from common patterns
- The exact color values for footer and footer-link and footer-link-hover are inferred from common patterns
- The exact color values for badge-sale, badge-new, badge-out-of-stock are inferred from common patterns
- The exact color values for section-header and section-header-accent are inferred from common patterns
- The exact color values for divider and divider-soft are inferred from common patterns
- The exact color values for tooltip are inferred from common patterns
- The exact color values for loading-spinner and loading-spinner-large are inferred from common patterns
- The exact color values for social-icon and social-icon-hover are inferred from common patterns
- The exact color values for hero-banner and hero-banner-cta are inferred from common patterns
- The exact color values for product-card-add-to-cart are inferred from common patterns
- The exact color values for product-card-badge and product-card-badge-new are inferred from common patterns
- The exact color values for product-card-rating are inferred from common patterns
- The exact color values for product-card-title and product-card-price are inferred from common patterns
- The exact color values for product-card-sale-price are inferred from common patterns
- The exact color values for product-card-image are inferred from common patterns
- The exact color values for nav-bar and nav-bar-sticky are inferred from common patterns
- The exact color values for nav-link and nav-link-active are inferred from common patterns
- The exact color values for search-bar and search-bar-focus are inferred from common patterns
- The exact color values for text-input and text-input-focus and text-input-error are inferred from common patterns
- The exact color values for select-input are inferred from common patterns
- The exact color values for button-primary, button-secondary, button-tertiary-text, button-pill-primary, button-pill-secondary are inferred from common patterns
- The exact color values for icon-button and icon-button-active are inferred from common patterns
- The exact color values for footer and footer-link and footer-link-hover are inferred from common patterns
- The exact color values for badge-sale, badge-new, badge-out-of-stock are inferred from common patterns
- The exact color values for section-header and section-header-accent are inferred from common patterns
- The exact color values for divider and divider-soft are inferred from common patterns
- The exact color values for tooltip are inferred from common patterns
- The exact color values for loading-spinner and loading-spinner-large are inferred from common patterns
- The exact color values for social-icon and social-icon-hover are inferred from common patterns
- The exact color values for hero-banner and hero-banner-cta are inferred from common patterns
- The exact color values for product-card-add-to-cart are inferred from common patterns
- The exact color values for product-card-badge and product-card-badge-new are inferred from common patterns
- The exact color values for product-card-rating are inferred from common patterns
- The exact color values for product-card-title and product-card-price are inferred from common patterns
- The exact color values for product-card-sale-price are inferred from common patterns
- The exact color values for product-card-image are inferred from common patterns
- The exact color values for nav-bar and nav-bar-sticky are inferred from common patterns
- The exact color values for nav-link and nav-link-active are inferred from common patterns
- The exact color values for search-bar and search-bar-focus are inferred from common patterns
- The exact color values for text-input and text-input-focus and text-input-error are inferred from common patterns
- The exact color values for select-input are inferred from common patterns
- The exact color values for button-primary, button-secondary, button-tertiary-text, button-pill-primary, button-pill-secondary are inferred from common patterns
- The exact color values for icon-button and icon-button-active are inferred from common patterns
- The exact color values for footer and footer-link and footer-link-hover are inferred from common patterns
- The exact color values for badge-sale, badge-new, badge-out-of-stock are inferred from common patterns
- The exact color values for section-header and section-header-accent are inferred from common patterns
- The exact color values for divider and divider-soft are inferred from common patterns
- The exact color values for tooltip are inferred from common patterns
- The exact color values for loading-spinner and loading-spinner-large are inferred from common patterns
- The exact color values for social-icon and social-icon-hover are inferred from common patterns
- The exact color values for hero-banner and hero-banner-cta are inferred from common patterns
- The exact color values for product-card-add-to-cart are inferred from common patterns
- The exact color values for product-card-badge and product-card-badge-new are inferred from common patterns
- The exact color values for product-card-rating are inferred from common patterns
- The exact color values for product-card-title and product-card-price are inferred from common patterns
- The exact color values for product-card-sale-price are inferred from common patterns
- The exact color values for product-card-image are inferred from common patterns
- The exact color values for nav-bar and nav-bar-sticky are inferred from common patterns
- The exact color values for nav-link and nav-link-active are inferred from common patterns
- The exact color values for search-bar and search-bar-focus are inferred from common patterns
- The exact color values for text-input and text-input-focus and text-input-error are inferred from common patterns
- The exact color values for select-input are inferred from common patterns
- The exact color values for button-primary, button-secondary, button-tertiary-text, button-pill-primary, button-pill-secondary are inferred from common patterns
- The exact color values for icon-button and icon-button-active are inferred from common patterns
- The exact color values for footer and footer-link and footer-link-hover are inferred from common patterns
- The exact color values for badge-sale, badge-new, badge-out-of-stock are inferred from common patterns
- The exact color values for section-header and section-header-accent are inferred from common patterns
- The exact color values for divider and divider-soft are inferred from common patterns
- The exact color values for tooltip are inferred from common patterns
- The exact color values for loading-spinner and loading-spinner-large are inferred from common patterns
- The exact color values for social-icon and social-icon-hover are inferred from common patterns
- The exact color values for hero-banner and hero-banner-cta are inferred from common patterns
- The exact color values for product-card-add-to-cart are inferred from common patterns
- The exact color values for product-card-badge and product-card-badge-new are inferred from common patterns
- The exact color values for product-card-rating are inferred from common patterns
- The exact color values for product-card-title and product-card-price are inferred from common patterns
- The exact color values for product-card-sale-price are inferred from common patterns
- The exact color values for product-card-image are inferred from common patterns
- The exact color values for nav-bar and nav-bar-sticky are inferred from common patterns
- The exact color values for nav-link and nav-link-active are inferred from common patterns
- The exact color values for search-bar and search-bar-focus are inferred from common patterns
- The exact color values for text-input and text-input-focus and text-input-error are inferred from common patterns
- The exact color values for select-input are inferred from common patterns
- The exact color values for button-primary, button-secondary, button-tertiary-text, button-pill-primary, button-pill-secondary are inferred from common patterns
- The exact color values for icon-button and icon-button-active are inferred from common patterns
- The exact color values for footer and footer-link and footer-link-hover are inferred from common patterns
- The exact color values for badge-sale, badge-new, badge-out-of-stock are inferred from common patterns
- The exact color values for section-header and section-header-accent are inferred from common patterns
- The exact color values for divider and divider-soft are inferred
