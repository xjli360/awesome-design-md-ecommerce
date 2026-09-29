---
version: alpha
name: "California Baby"
source_url: "https://californiababy.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A sun-warmed yellow #f7dc73 — the meta-theme color and the brand’s emotional anchor — floods the California Baby canvas, evoking California poppies, chamomile, and the gentle glow of a nursery at golden hour. Against this honeyed backdrop, a confident red #dd0031 punches through for primary CTAs and sale badges, creating a visual tension that is both playful and urgent — a brand that knows when to soothe and when to act. The palette is deliberately spare: a near-white #dedede for soft surfaces and cards, and deep ink #121212 for body text, ensuring readability across product labels and ingredient lists. There are no hard corners in the interface; every button, input, and card edge is softly rounded at {rounded.sm} or {rounded.md}, mirroring the organic, plant-based formulations the brand is known for. Typography runs clean and approachable — sans-serif, moderate weights, generous line heights — prioritizing clarity for parents scanning ingredient panels and dosage instructions. The overall mood is one of trustworthy warmth: a digital storefront that feels less like a sterile e-commerce engine and more like a sunlit apothecary shelf, where every element — from the pill-shaped search bar to the chamomile-toned footer — reinforces a single promise: gentle, effective, and unmistakably Californian.

colors:
  primary: "#dd0031"
  primary-active: "#b30028"
  primary-disabled: "#f5a3b5"
  ink: "#121212"
  body: "#2a2a2a"
  muted: "#5c5c5c"
  muted-soft: "#8a8a8a"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#f7dc73"
  surface-soft: "#dedede"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-canvas: "#121212"
  badge-sale: "#dd0031"
  badge-new: "#2a8c4a"
  star-rating: "#121212"
  ingredient-tag: "#f7dc73"
  footer-bg: "#f7dc73"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  ingredient-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
    textDecoration: underline

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
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-pill-canvas:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.primary}"
  text-input-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xs}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-canvas}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.lg}"
  nav-bar-sticky:
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-canvas}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.sm}"
  nav-link-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
  nav-link-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-pill-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 1px 4px rgba(0,0,0,0.06)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    fontWeight: 600
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 36px
    marginTop: "{spacing.sm}"
  ingredient-tag:
    backgroundColor: "{colors.ingredient-tag}"
    textColor: "{colors.on-canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
    gap: "{spacing.xxs}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    height: 32px
    width: 32px
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-canvas}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-canvas}"
    padding: "{spacing.xs} 0"
  footer-link-hover:
    textColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-canvas}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.none}"
  hero-banner-image:
    rounded: "{rounded.md}"
  hero-banner-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.md}"
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.lg}"
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    gap: "{spacing.xs}"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    textDecoration: underline
  breadcrumb-current:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
    fontWeight: 600
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    gap: "{spacing.xs}"
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: "1px solid {colors.hairline}"
  cart-item-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  cart-item-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    fontWeight: 600
  cart-item-remove:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    textDecoration: underline
  cart-item-remove-hover:
    textColor: "{colors.primary}"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 52px
  checkout-button-hover:
    backgroundColor: "{colors.primary-active}"
  checkout-button-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  trust-badge-icon:
    height: 20px
    width: 20px
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 40px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand’s signature red #dd0031 with white text and a soft 8px radius. On hover, it deepens to #b30028; when disabled, it fades to a muted pink #f5a3b5. Used for “Add to Cart,” “Checkout,” and “Subscribe” actions across the site. The 48px height and 12px/24px padding provide a generous, easy-to-tap target on mobile.

**`button-secondary`** — An outlined variant with a white fill, red text, and a 2px red border. Maintains the same 48px height and 8px radius as the primary button. On hover, the border and text shift to the deeper active red. Used for “Learn More,” “View Details,” and secondary checkout options.

**`button-tertiary-text`** — A text-only button with no background or border, styled in the primary red. Used for “Cancel,” “Clear,” and inline “Shop Now” links within product descriptions. The 12px vertical padding ensures adequate touch area without visual weight.

**`button-pill-canvas`** — A fully pill-shaped button on the warm yellow canvas background, with dark text. Used for category filters, “Shop by Concern” navigation, and promotional banners. The 10px/20px padding and 9999px radius create a friendly, approachable silhouette.

**`button-pill-primary`** — Same pill shape as the canvas variant but filled with the brand red and white text. Used for high-visibility CTAs within hero banners and promotional sections where the canvas background is already yellow.

### Text Inputs & Forms
**`text-input`** — A standard text input with a white background, 1px hairline border, 8px radius, and 48px height. On focus, the border thickens to 2px and turns red. Error state uses the same 2px red border. Labels sit above the input in muted caption type with 4px bottom margin.

**`select-input`** — Matches the text input styling for visual consistency. Used for quantity selectors, size pickers, and filter dropdowns.

**`textarea`** — A multi-line input with the same border, radius, and padding as the text input. Used for “Special Instructions” on gift orders and contact forms.

**`newsletter-input`** — A pill-shaped email input with a white background and 1px hairline border, designed to pair with the `newsletter-submit` button. The 48px height and 20px horizontal padding create a comfortable field for email entry.

### Navigation
**`nav-bar`** — A fixed-height 72px bar on the warm yellow canvas background, with dark text. The bar spans full width with 24px horizontal padding. When sticky, a subtle 2px shadow drops beneath. Logo sits left-aligned, navigation links center, and utility icons (search, account, cart) right-aligned.

**`nav-link`** — Inline navigation links with 8px/12px padding and an 8px radius hover state that reveals a soft #dedede background. Active links switch to the red primary color with the same background treatment.

**`breadcrumb`** — A horizontal row of muted caption links separated by spacing, with the current page rendered in bold ink. Used on product detail and collection pages for orientation.

### Product Cards
**`product-card`** — A white card with a 12px radius, 16px padding, and a subtle 1px/4px shadow. On hover, the shadow deepens to 4px/12px for a gentle lift effect. The card contains a square image with 8px radius, a title in title-sm, a price in red body-md, and an “Add to Cart” button at the bottom.

**`product-card-badge`** — A small uppercase badge in the brand red with white text and 4px radius, positioned at the top-left of the product image. Used for sale items. A green variant (`product-card-badge-new`) signals new arrivals.

**`ingredient-tag`** — A pill-shaped tag on the yellow canvas background with dark text, used to highlight key ingredients (e.g., “Chamomile,” “Calendula”) on product cards and detail pages.

### Cart & Checkout
**`cart-item`** — A white card with 12px radius, 12px padding, and a 1px hairline border, containing the product image, title, price, quantity selector, and a remove link. The remove link is a muted underline caption that turns red on hover.

**`checkout-button`** — A full-width primary button at 52px height with 14px/32px padding, used as the final CTA in the cart drawer and checkout flow. Hover deepens to the active red; disabled state uses the muted pink.

**`trust-badge`** — A small muted badge on a soft #dedede background, used to display payment icons (Shopify Pay, Klarna, Afterpay) and security assurances near the checkout button.

### Footer
**`footer-section`** — A full-width footer on the warm yellow canvas background with dark text, containing columns of links, a newsletter signup, and brand information. The section uses 64px vertical padding and 24px horizontal padding. Links are underlined on hover and turn red.

### Hero & Content
**`hero-banner`** — A full-width section on the yellow canvas background with 64px vertical padding, containing a large display title, a body subtitle, and optional CTA buttons. The hero image sits within a 12px rounded container.

**`accordion`** — A white card with 12px radius, 12px/16px padding, and a 1px hairline border, used for FAQ sections and product details. The header is a title-sm link that toggles the content body-sm below.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav-bar collapses to hamburger menu; product cards stack in 2-column grid; hero banner reduces padding to 32px; search bar moves to full-width below nav; footer columns stack vertically; accordion becomes default for all content sections |
| Tablet | 744–1128px | Nav-bar shows all links with reduced padding; product cards display in 3-column grid; hero banner maintains 48px padding; search bar remains in nav but collapses to icon; footer shows 2-column layout |
| Desktop | 1128–1440px | Full nav-bar with all links visible; product cards in 4-column grid; hero banner at 64px padding; search bar fully expanded in nav; footer shows 4-column layout |
| Wide | > 1440px | Max-width container at 1440px with centered content; product cards in 4-column grid with increased whitespace; hero banner content centered with max-width 1200px |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card “Add to Cart” buttons are 36px tall but surrounded by 16px padding for a 68px effective touch zone
- Quantity selector buttons are 32px square with 8px padding for a 48px effective touch target
- Nav links have 8px padding creating a 56px touch zone at 72px nav height
- Search bar pill is 48px tall for easy one-handed tapping

### Collapsing Strategy
- Primary navigation collapses to a hamburger icon at 744px breakpoint, revealing a full-screen overlay menu
- Product filters collapse to a “Filter” button that opens a slide-in drawer on mobile
- Product description sections collapse to accordion panels on mobile and tablet
- Footer link columns stack vertically below 744px, with each column preceded by a heading
- Search bar collapses to a magnifying glass icon on tablet and mobile, expanding to full-width on tap
- Cart drawer replaces full cart page on mobile, sliding in from the right

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were found during extraction; the typography block uses a generic sans-serif stack (Helvetica Neue, Helvetica, Arial) as a placeholder. The brand may use a custom typeface (e.g., a rounded sans-serif) that could not be detected.
- Hover states for most components are inferred from common patterns; exact transition durations and easing curves were not extracted.
- Error states for form validation (error messages, iconography, border animations) were not observed.
- Dark mode or high-contrast mode styles are not present in the extracted data.
- Sub-brand or seasonal color palettes (e.g., holiday, limited edition) are not documented.
- The extracted color list (#dedede, #dd0031, #f7dc73, #121212) is sparse and may not represent the full brand palette. The yellow #f7dc73 is used as the canvas color based on its meta-theme-color designation, but it may also function as an accent or background in specific sections. The gray #dedede is used for surface-soft and hairline, but its exact role across components is inferred.
- Shopify Pay, Klarna, and Afterpay button colors were filtered from the extraction but may appear in checkout flows.
- Product swatch colors (for variant selection) were not extracted.
- Loading states, skeleton screens, and spinner animations are not documented.
- Focus-visible styles and keyboard navigation indicators were not observed.
- Print styles and email template styles are not included.
