---
version: alpha
name: "Oeuf"
source_url: "https://oeufnyc.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A nursery furniture brand that wraps its eco-conscious mission in a palette of warm grays and a single jolt of safety red (#ea0202) — the only color that breaks the hushed, natural-toned surface of the site. The extracted palette reads like a Scandinavian nursery at dusk: charcoal ink (#272727) for headlines, soft stone (#b1b7c3) for secondary text, and a pale mint wash (#e6f7f4) that surfaces in backgrounds and product photography, suggesting the brand's commitment to non-toxic finishes and sustainable materials. The typography pairs Libre Baskerville — a serif with the quiet authority of a children's book — with Poppins, a geometric sans-serif that handles navigation and product labels with clean, unpretentious clarity. Product cards sit on a canvas of near-white (#f5f5f5) with hairline borders (#e5e5e5) that define space without shouting, while the checkout flow introduces a secondary blue (#121f36) that reads as trustworthy and calm. The red appears sparingly — sale badges, error states, the occasional CTA — and carries the weight of a warning light in an otherwise serene room. Every corner is softly rounded ({rounded.sm} to {rounded.md}), every spacing generous ({spacing.xl} between product rows), and the overall impression is one of deliberate restraint: a brand that trusts its materials, its craftsmanship, and the quiet confidence of a well-made crib.

colors:
  primary: "#272727"
  primary-active: "#1c1c1c"
  primary-disabled: "#9b9b9b"
  ink: "#272727"
  body: "#4c4c4c"
  muted: "#6b6b6b"
  muted-soft: "#888888"
  hairline: "#e5e5e5"
  hairline-soft: "#eaeaea"
  canvas: "#f5f5f5"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#ea0202"
  accent-blue: "#121f36"
  accent-mint: "#e6f7f4"
  badge-sale: "#ea0202"
  badge-new: "#121f36"
  star-rating: "#272727"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Libre Baskerville', Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Libre Baskerville', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Libre Baskerville', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase

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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-red-active:
    backgroundColor: "#c00101"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.link}"
    padding: 0
  button-text-link-hover:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
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
    outline: none
  text-input-error:
    border: "2px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 1px 3px rgba(0,0,0,0.06)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
    objectFit: cover
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-banner-alt:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
  footer-link-hover:
    color: "{colors.muted-soft}"
  footer-heading:
    typography: "{typography.caption}"
    color: "{colors.on-primary}"
    textTransform: uppercase
    letterSpacing: "1px"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-trigger-active:
    textColor: "{colors.primary}"
  accordion-panel:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  quantity-selector-button-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
  breadcrumb:
    typography: "{typography.caption-sm}"
    color: "{colors.muted-soft}"
  breadcrumb-active:
    color: "{colors.ink}"
  breadcrumb-separator:
    color: "{colors.hairline}"
    padding: "0 {spacing.xs}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  rating-stars-empty:
    color: "{colors.hairline}"
    size: 16px
  loading-spinner:
    color: "{colors.primary}"
    size: 32px
  error-message:
    backgroundColor: "#f8d7da"
    textColor: "#721c24"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid #f5c6cb"
  success-message:
    backgroundColor: "#d4edda"
    textColor: "#155724"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid #c3e6cb"
  warning-message:
    backgroundColor: "#fff3cd"
    textColor: "#856404"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid #ffeeba"
  info-message:
    backgroundColor: "#f4f8fe"
    textColor: "{colors.accent-blue}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid #d1d5db"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in charcoal ink (#272727) with white text and a soft 8px radius. Used for "Add to Cart", "Checkout", and primary form submissions. On hover, the background deepens to near-black (#1c1c1c). The disabled state fades to a muted gray (#9b9b9b) with white text, signaling unavailability without visual noise.

**`button-secondary`** — An outlined alternative for secondary actions like "View Details" or "Save for Later". Uses a white background with charcoal text and a 1px hairline border. On hover, the background shifts to a soft off-white (#f9fafb). Height and padding match the primary button for consistent alignment in forms and product grids.

**`button-accent-red`** — Reserved for high-urgency actions: clearance sales, limited-time offers, and final markdowns. Uses the brand's safety red (#ea0202) as background with white text. On hover, the red deepens to a darker crimson (#c00101). This button carries visual weight and should be used sparingly — no more than one per page.

**`button-text-link`** — A text-only button for inline actions like "Learn More" or "Read Reviews". No background, no border — just the link typography in charcoal ink. On hover, the text fades to muted gray, providing a subtle but clear interactive cue.

### Cards
**`product-card`** — The primary product display unit, a white card with a 12px radius and a subtle box shadow. The card contains a square-ratio product image (top corners rounded to match the card), a title in Poppins medium, and a price in muted gray. On hover, the shadow deepens to create a gentle lift effect. Badges (sale, new) are positioned absolutely at the top-left of the image area.

**`product-card-badge`** — A small, uppercase label pinned to the top-left of product images. Sale badges use the accent red background; new-arrival badges use the accent blue (#121f36). Both use white text and a tight 4px radius, ensuring they read as tags rather than design elements.

### Navigation
**`nav-bar`** — A fixed-position top navigation bar, 72px tall, with a white background and a soft bottom hairline. The nav contains the brand logo (left), product category links (center), and utility icons (search, account, cart) on the right. On scroll, a subtle box shadow replaces the hairline for visual depth. Active nav links are underlined with a 2px charcoal border.

**`nav-link-active`** — Uppercase Poppins semibold in charcoal with a 2px bottom border. The active state is reserved for the current page or section, providing a clear location indicator.

**`nav-link-inactive`** — Same typography but in muted gray, with no underline. On hover, the text color shifts toward charcoal to indicate interactivity.

### Forms
**`text-input`** — Standard text input fields for checkout forms, search, and account pages. White background, charcoal text, 48px height, and a 1px hairline border with 8px radius. On focus, the border doubles to 2px charcoal with no outline. Error states swap the border to 2px accent red.

**`quantity-selector`** — A compact input for adjusting product quantities, typically found on the cart page or product detail. Contains a decrement button, a read-only number display, and an increment button. The buttons have a subtle hover state that reveals a light gray background.

**`search-bar`** — A pill-shaped search input with full 9999px radius, used in the navigation and on search-focused pages. White background with a 1px hairline border. On focus, the border becomes 2px charcoal. The pill shape is a deliberate departure from the standard 8px radius, creating a distinct search affordance.

### Footer
**`footer-section`** — A dark footer section with charcoal background and white text. Contains columns for brand information, customer service links, and social media icons. Headings are uppercase Poppins caption with 1px letter spacing. Links are white Poppins body-sm that fade to muted gray on hover.

### Messaging
**`error-message`** — A light red background (#f8d7da) with dark red text (#721c24) and a matching border. Used for form validation errors, payment failures, and system alerts. The 8px radius and 12px padding keep it contained and readable.

**`success-message`** — A light green background (#d4edda) with dark green text (#155724). Used for successful add-to-cart confirmations, order placements, and account updates.

**`warning-message`** — A light yellow background (#fff3cd) with dark yellow text (#856404). Used for low-stock warnings, shipping delays, and policy reminders.

**`info-message`** — A light blue background (#f4f8fe) with dark blue text (#121f36). Used for informational banners about promotions, new collections, or site features.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger navigation, stacked footer, 16px page padding, reduced hero height to 300px |
| Tablet | 744–1128px | Two-column product grid, expanded nav with dropdowns, 24px page padding, hero at 400px |
| Desktop | 1128–1440px | Three-column product grid, full nav bar, 32px page padding, hero at 450px |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, centered layout, hero at 500px |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px on mobile
- Product card tap targets extend to full card width for easy selection
- Quantity selector buttons are 40x40px minimum
- Accordion triggers have 48px minimum height for finger-friendly tapping

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px
- Product filters collapse into a slide-out drawer on mobile
- Footer columns stack vertically below 744px, with accordion-style expandable sections for each column
- Product image galleries switch from grid to single-image swipe on mobile
- Multi-column text layouts (features, specifications) collapse to single column below 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for many components (product card, nav links, footer links) are inferred from common patterns rather than extracted from the live site
- Active/focus states for text inputs and buttons are based on accessibility best practices, not extracted CSS
- The exact font weights for Libre Baskerville and Poppins are inferred from common web usage; the site may use different weights
- The hero banner background color (accent-mint #e6f7f4) is extracted from the color list but its exact usage context is inferred
- Dark mode is not present on the live site and is not defined
- The extracted color list includes many checkout-widget colors (Shopify Pay, Klarna, Afterpay) that are not part of the brand palette — these have been excluded from the design system
- The brand's true primary color (#272727) is a dark charcoal, which is unusual for a nursery brand — this is confirmed by the extracted data but may surprise designers familiar with pastel-heavy competitors
- Sub-brand or collection-specific color variations are not captured
- Animation durations, easing functions, and transition properties are not extracted
- The exact border-radius values for product cards and buttons are inferred from common patterns; the extracted CSS may use different values
- Form validation error states use colors (#f8d7da, #721c24) that are likely Shopify defaults rather than brand-specific choices
- The accent red (#ea0202) may be used more or less frequently than documented; its exact distribution across the site is unknown
