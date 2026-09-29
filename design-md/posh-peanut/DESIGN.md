---
version: alpha
name: "Posh Peanut"
source_url: "https://poshpeanut.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A soft, playful baby-and-family brand built on a distinctive teal-mint palette anchored by #087780 and #54bdb6, where rounded corners and generous white space create a gentle, trustworthy shopping experience. The brand's signature move is pairing deep charcoal ink (#343132) with these vibrant aqua tones, using the teal as both primary action color and decorative accent across buttons, badges, and product-card highlights. The canvas (#f4f4f6) stays light and airy, while muted tones (#676986, #9a9db1) provide subtle structure without competing with the colorful product photography. Buttons use a pill-like shape with {rounded.full} corners, and the search bar follows the same friendly radius — there are no sharp edges in the interface. The typography system relies on a clean sans-serif stack (inherit declarations suggest system fonts or a Shopify theme default), with display sizes kept moderate to let the product images lead. Product cards feature a soft {rounded.sm} corner, a clean white surface, and the teal accent appearing in sale badges, size-selector highlights, and add-to-cart buttons. The brand's secondary palette includes a warm blush (#d9f5f6), a deeper navy (#272d45), and a bright accent green (#00caaa) used sparingly for promotional elements. The overall feeling is one of calm, trustworthy playfulness — the digital equivalent of a well-designed nursery where every edge has been softened and every color chosen to feel both cheerful and safe.

colors:
  primary: "#087780"
  primary-active: "#0e7a82"
  primary-disabled: "#b2f9e9"
  ink: "#343132"
  body: "#676986"
  muted: "#9a9db1"
  muted-soft: "#d3d4dd"
  hairline: "#e5e5e5"
  hairline-soft: "#e9e7e4"
  canvas: "#f4f4f6"
  surface-soft: "#f7f7f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal-light: "#54bdb6"
  accent-teal-bright: "#00caaa"
  accent-navy: "#272d45"
  accent-blush: "#d9f5f6"
  error: "#c60606"
  sale-badge: "#07818b"

typography:
  display-xl:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  button-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-sale:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
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
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.accent-blush}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-small:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    boxShadow: "0 2px 8px rgba(52, 49, 50, 0.08)"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
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
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    textColor: "{colors.error}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  size-selector-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.accent-teal-light}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "none"
  newsletter-button:
    backgroundColor: "{colors.accent-teal-bright}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "10px 24px"
    height: 44px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-active:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Checkout," and key conversion points. Rendered as a pill shape with {rounded.full} corners, filled with the brand teal {colors.primary} and white text. On hover, shifts to {colors.primary-active} with a subtle darkening. The disabled state uses {colors.primary-disabled} with muted text, signaling unavailability without visual noise. Text is uppercase, 14px, weight 600, with 0.5px letter spacing for a clean, intentional look.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Continue Shopping." Uses a white fill with a 2px teal border and teal text. On hover, the background fills with the blush accent {colors.accent-blush} and the border deepens to {colors.primary-active}. Maintains the same pill shape and typography as the primary button for visual consistency.

**`button-tertiary-text`** — A text-only button used for less prominent actions like "Clear Filters" or "Cancel." Transparent background with teal text, no border. Relies on the uppercase button typography to maintain hierarchy without competing with primary and secondary buttons.

**`button-pill-small`** — A compact pill button used for filter chips, category tags, and quick-add actions. Same teal fill and white text as the primary button, but with smaller padding (8px 20px) and smaller uppercase typography (12px). Uses {rounded.full} to maintain the brand's signature pill language at a smaller scale.

### Cards
**`product-card`** — The core product display unit across collection pages and search results. A white card with {rounded.sm} corners and no padding at the container level. The product image sits flush to the top corners (rounded only at the top), followed by the product title in {typography.title-sm} and the price in {typography.price}. Sale prices render in {colors.error} using {typography.price-sale}. Cards stack in a responsive grid with generous gap spacing.

**`product-card-image`** — The image container within a product card, using {rounded.sm} on the top corners only. Images are typically 1:1 or 4:5 aspect ratio, with object-fit: cover to maintain consistency across the grid.

### Navigation
**`nav-bar`** — The persistent top navigation bar, 72px tall with a white background and the brand's deep charcoal ink for text. At rest, no shadow; on scroll, a subtle 2px shadow at 8% opacity of {colors.ink} appears. Navigation links use uppercase 14px text at weight 500 with 0.3px letter spacing. The active state underlines with a 2px teal border and shifts text color to {colors.primary}.

**`nav-link`** — Standard navigation link using uppercase 14px text at weight 500. Inactive state uses {colors.ink}; active state uses {colors.primary} with a 2px bottom border in the same teal.

### Forms
**`text-input`** — Standard text input for forms, search, and checkout fields. White background with a 1px hairline border, {rounded.sm} corners, and 16px body text. On focus, the border thickens to 2px and shifts to {colors.primary}. Error state uses a 2px red border ({colors.error}). Padding is 12px vertical, 16px horizontal, with a 48px height for comfortable touch targets.

**`search-bar`** — The site search input, styled as a pill with {rounded.full} corners. Uses a soft gray background ({colors.surface-soft}) with a 1px hairline border. On focus, the border thickens to 2px teal. Padding is 10px vertical, 20px horizontal, with a 44px height — slightly shorter than the text input to feel more like a search affordance than a form field.

**`newsletter-input`** — Email input for the newsletter signup in the footer. White background, pill shape ({rounded.full}), 44px height. Paired with a bright teal ({colors.accent-teal-bright}) submit button using the same pill shape and height for a seamless, unified appearance.

### Badges & Labels
**`sale-badge`** — A small, high-contrast badge for sale items. Uses the deeper teal ({colors.sale-badge}) background with white uppercase 10px text at weight 700. {rounded.xs} corners keep it compact and unobtrusive, with 4px/8px padding.

**`size-selector`** — Size picker for product detail pages. A small square or rectangular button with {rounded.sm} corners, 1px hairline border, and 36px height. The active state fills with {colors.primary} and white text, clearly indicating the selected size.

### Footer
**`footer-section`** — The site footer, using the deep charcoal ink ({colors.ink}) as background with white text. Links use the muted soft gray ({colors.muted-soft}) and shift to the light teal accent ({colors.accent-teal-light}) on hover. The newsletter signup area sits prominently within the footer, using the white card input and bright teal button for visual contrast against the dark background.

**`footer-link`** — Footer navigation links in {colors.muted-soft} at 14px regular weight. On hover, transitions to {colors.accent-teal-light} for a subtle interactive cue against the dark footer background.

### Accordion
**`accordion-header`** — Used for product descriptions, shipping details, and FAQ sections. A transparent header with {colors.ink} text in {typography.title-sm}, separated from the next section by a 1px hairline border. Padding is 16px vertical, no horizontal padding at the container level.

**`accordion-content`** — The expandable content area below each accordion header. Uses {colors.body} for text color and {typography.body-sm} for readability. Padding is 8px top, 16px bottom, with no horizontal padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; search bar moves to expandable icon; product cards stack vertically; footer links stack in single column; size selectors become full-width |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links with dropdown for secondary items; search bar remains visible but compact; product cards show 2 per row; footer uses 2-column layout |
| Desktop | 1128–1440px | Three or four-column product grid; full nav bar visible; search bar at full width in header; product cards show 3-4 per row; footer uses 4-column layout with newsletter |
| Wide | > 1440px | Max-width container at 1440px; product grid can show 4-5 columns; all elements centered within max-width; whitespace increases proportionally |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Size selectors and quantity selectors are 36-40px tall, meeting the 44px touch target when including padding and spacing
- Nav links have 72px touch area (full nav-bar height) even if text is smaller
- Search bar and text inputs are 44-48px tall for comfortable touch interaction
- Accordion headers have 16px padding top and bottom, creating a minimum 48px touch target

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a slide-out drawer
- Secondary navigation (categories, filters) collapses to dropdowns or accordion panels on mobile
- Product filters move to a slide-out panel on mobile, accessible via a "Filter" button
- Footer link columns collapse to a single column on mobile, with accordion-style expandable sections
- Product image galleries collapse from thumbnails to dot indicators on mobile
- Multi-column layouts (product grids, feature sections) collapse to single column below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font family declarations were not explicitly extractable from the live site (only "inherit" and widget-specific fonts found). The typography block uses a system font stack as a reasonable default — the actual brand font (likely a Google Font or Shopify theme font) should be identified from design files or CSS source maps.
- Hover and active states for many components (footer links, accordion headers, breadcrumbs) are inferred from common e-commerce patterns rather than extracted from the live site.
- Error state styling for forms (validation messages, error icons) was not observed and should be defined from design files.
- Dark mode or high-contrast mode variants are not present in the extracted data and may not be supported.
- The extracted hex list includes several colors that may be Shopify widget defaults (#2c3e50, #121212) or third-party payment badges — these have been deprioritized in favor of the distinctive teal-mint palette.
- Specific spacing values for product grid gaps, section padding, and container max-width were not extractable and should be confirmed from design files.
- The brand's secondary palette (blush, navy, bright green) usage frequency and specific component assignments are inferred from common patterns rather than extracted rules.
- Animation and transition durations/easings were not extractable — a standard 200-300ms ease-in-out is recommended as default.
- Checkout flow styling (Shopify checkout overrides) was not observed and may use platform defaults.
