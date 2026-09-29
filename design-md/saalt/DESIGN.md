---
version: alpha
name: "Saalt"
source_url: "https://saalt.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A period-care brand that uses a restrained palette of near-black (#141414) and soft warm white (#fefefe) to signal clinical seriousness, then breaks the tension with a single unexpected accent: a muted lavender-purple (#a45cec) that appears on the homepage hero CTA button, the "Shop" navigation link hover state, and the brand's "Saalt" wordmark in the footer. The extracted hex list reads like a generic Shopify storefront until that #a45cec appears — it's the brand's only deliberate chromatic move, and it lands like a quiet counterpoint to the category's pink-and-pastel conventions. Body text runs Inter at 16px on a #f6f6f6 canvas, with Montserrat reserved for display headlines and the logo lockup. Cards and buttons use soft 8px rounding ({rounded.sm}), while the primary CTA button sits at 48px tall with 14px horizontal padding and a purple fill that shifts to a darker hover state. The checkout flow uses a standard Shopify pill shape ({rounded.full}) for the "Add to Cart" button. The site leans on generous whitespace and a single-column product grid on mobile, with a two-column layout on desktop. The overall mood is calm, direct, and unapologetically functional — the design trusts the product's utility over decorative flourishes.

colors:
  primary: "#a45cec"
  primary-active: "#8b3fd6"
  primary-disabled: "#d4b3f5"
  ink: "#141414"
  body: "#545454"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#e2e2e2"
  hairline-soft: "#dedede"
  canvas: "#fefefe"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#f7d6c5"
  accent-cool: "#3f4759"
  link-blue: "#007aff"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
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
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    padding: 14px 24px
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
    padding: 13px 23px
    height: 48px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  hero-headline:
    typography: "{typography.display-xl}"
  hero-subheadline:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: 0 0 16px 0
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with Saalt's signature purple (#a45cec) and white text. Used for "Add to Cart", "Subscribe", and primary checkout flows. On hover, the background shifts to a darker purple (#8b3fd6). The disabled state uses a lighter purple (#d4b3f5) to indicate inactivity.

**`button-secondary`** — A white button with dark text, used for secondary actions like "Learn More" or "View Details". The outline variant (`button-secondary-outline`) uses a transparent background with a dark text color and a 1px solid border (hairline) for structure.

**`button-pill`** — A fully rounded variant of the primary button, used sparingly for promotional banners or sticky mobile CTAs. It shares the same purple fill and white text but uses a smaller font size and tighter padding.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, white background, with navigation links in Inter 14px/500. The active link (or hover state) shifts to the brand purple (#a45cec). The nav collapses to a hamburger menu on mobile.

**`nav-link-active`** — The active or hover state for navigation links, using the brand purple to indicate the current page or section.

### Cards
**`product-card`** — A white card with soft 8px rounding, used to display product thumbnails, titles, and prices. The image area shares the same rounding. The title uses `title-sm` (Inter 16px/600) and the price uses `body-md` (Inter 16px/400) in the body gray (#545454).

**`product-card-image`** — The image container within a product card, rounded at 8px to match the card itself.

### Forms
**`text-input`** — A standard text input field with white background, 8px rounding, and 48px height. On focus, the border color changes to the brand purple (#a45cec) to indicate active state.

**`quantity-selector`** — A compact input for selecting product quantities, using a soft gray background (#f6f6f6) and 40px height. Used on product detail pages and cart.

### Badges
**`badge-new`** — A small purple badge with white text, used to flag new products or collections. Uses uppercase 11px/700 type with 0.5px letter spacing.

**`badge-sale`** — A warm peach-toned badge (#f7d6c5) with dark text, used to indicate sale or promotional items. Same typography as the new badge.

### Footer
**`footer`** — A dark footer (#141414) with white text, containing links, legal information, and brand messaging. Links use the muted gray (#aaaaaa) to reduce visual weight. The footer stacks on mobile and expands to a multi-column layout on desktop.

### Accordion
**`accordion-header`** — Used for FAQ sections and product details, with a white background and dark text. The header is clickable and expands to reveal content below.

**`accordion-content`** — The expandable content area within an accordion, using body gray text and standard body typography.

### Hero
**`hero-section`** — The homepage hero area, using a soft gray background (#f6f6f6) with a large headline in Montserrat 36px/700 and a subheadline in Inter 16px/400 in body gray.

### Search
**`search-bar`** — A fully rounded search input used in the navigation or on search pages. White background with 48px height and 20px horizontal padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to 28px; footer stacks vertically; accordion expands by default for first item |
| Tablet | 744–1128px | Two-column product grid; nav links visible; hero uses 32px headline; footer uses two-column layout |
| Desktop | 1128–1440px | Two-column product grid with larger thumbnails; full nav bar; hero uses 36px headline; footer uses four-column layout |
| Wide | > 1440px | Max-width container at 1440px; content centered; product grid may expand to three columns |

### Touch Targets
- All buttons and interactive elements maintain a minimum height of 44px for touch accessibility.
- Navigation links have a minimum tap area of 44x44px, even when text is smaller.
- Quantity selector buttons are at least 40x40px.
- Accordion headers have a minimum touch area of 48px height.

### Collapsing Strategy
- The top navigation collapses to a hamburger menu below 744px.
- The footer collapses from four columns to two at tablet, and to a single column on mobile.
- Product grids collapse from two columns to one on mobile.
- Accordion sections collapse by default, with the first item expanded on mobile for immediate content visibility.
- Search bars may collapse to an icon on mobile, expanding to full width on tap.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list is dominated by grays (#141414, #e2e2e2, #dedede, #f6f6f6, #545454, #f3f3f3, #fefefe, #888888, #aaaaaa, #121212) and a single distinctive purple (#a45cec). The brand's true primary is assumed to be #a45cec based on its uniqueness and usage on the homepage CTA, but this is an inference — the extraction may have missed other brand colors (e.g., a secondary green or blue) that appear less frequently in the DOM.
- Hover states for buttons and links are inferred from common patterns; exact hover colors for secondary and tertiary buttons were not extracted.
- Error states for form inputs (e.g., red border, error message styling) were not observed.
- Typography sizes and weights are estimated based on common Inter/Montserrat usage at 16px body and 36px display; exact values from the live site's CSS were not extracted.
- Dark mode styling is not present on the live site.
- Sub-brand or collection-specific color palettes (e.g., for "Saalt Teen" or "Saalt Wear") were not observed.
- The extracted font list includes "swiper-icons" (a slider library), which is not a brand font and has been excluded.
- The meta theme-color tag is absent, so the browser chrome color is unknown.
- Checkout widget colors (Shopify Pay, Klarna, Afterpay) may be present in the extracted list but have been filtered out; the brand's true palette may be slightly different in the checkout flow.
