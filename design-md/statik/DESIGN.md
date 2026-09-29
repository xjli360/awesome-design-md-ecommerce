---
version: alpha
name: "Statik"
source_url: "https://www.statikco.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep teal #108474 — the color of a charging indicator glowing in a dark room — serves as Statik's primary voltage, appearing on every CTA, power-bank casing, and cable tag across the site. That teal is paired with a sharp marigold #ffc900 that acts as a secondary accent on badges, sale markers, and highlight labels, creating a high-contrast, industrial-electronic palette. The canvas is a clean #ffffff with a soft surface layer at #f9fafb and card surfaces at #fafafa, while the ink sits at #121212 for maximum readability against the bright backgrounds. Typography runs on Neue Haas Grotesk (Display and Text variants) — a Swiss sans-serif that brings precision and neutrality, letting the product photography and color do the emotional work. Buttons are pill-shaped at {rounded.full} with generous padding, and product cards use a subtle {rounded.sm} radius that keeps the interface feeling modern without being playful. The brand's category navigation, product grids, and footer all sit on a hairline of #dedede, a soft gray that structures content without competing with the teal-marigold energy. A secondary purple accent #be408e appears on audio-product badges and limited-edition drops, adding a surprising warmth to an otherwise cool, tech-forward system. The overall feel is that of a premium accessory brand that knows its audience wants reliability first, style second — the teal says "charged and ready," the marigold says "deal alert," and the clean white says "trust us."

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#a3d5cc"
  ink: "#121212"
  body: "#3f3f3f"
  muted: "#7b7b7b"
  muted-soft: "#aeaeae"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-marigold: "#ffc900"
  accent-purple: "#be408e"
  accent-purple-dark: "#953bbd"
  accent-purple-deep: "#3f1b74"
  accent-audio: "#a01deb"
  surface-gray: "#f4f4f4"
  surface-gray-medium: "#eeeeee"
  border-light: "#dadada"
  border-medium: "#c3c3c4"

typography:
  display-xl:
    fontFamily: "'neue-haas-grotesk-display', 'Neue Haas Grotesk Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -1.2px
  display-lg:
    fontFamily: "'neue-haas-grotesk-display', 'Neue Haas Grotesk Display', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.11
    letterSpacing: -0.72px
  display-md:
    fontFamily: "'neue-haas-grotesk-display', 'Neue Haas Grotesk Display', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.14
    letterSpacing: -0.56px
  display-sm:
    fontFamily: "'neue-haas-grotesk-display', 'Neue Haas Grotesk Display', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.18
    letterSpacing: -0.22px
  title-md:
    fontFamily: "'neue-haas-grotesk-text', 'Neue Haas Grotesk Text', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.22
    letterSpacing: 0
  title-sm:
    fontFamily: "'neue-haas-grotesk-text', 'Neue Haas Grotesk Text', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'neue-haas-grotesk-text', 'Neue Haas Grotesk Text', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'neue-haas-grotesk-text', 'Neue Haas Grotesk Text', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'neue-haas-grotesk-text', 'Neue Haas Grotesk Text', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "'neue-haas-grotesk-text', 'Neue Haas Grotesk Text', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'neue-haas-grotesk-text', 'Neue Haas Grotesk Text', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.33px
    textTransform: uppercase
  button-md:
    fontFamily: "'neue-haas-grotesk-text', 'Neue Haas Grotesk Text', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'neue-haas-grotesk-text', 'Neue Haas Grotesk Text', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.26px
  link:
    fontFamily: "'neue-haas-grotesk-text', 'Neue Haas Grotesk Text', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'neue-haas-grotesk-text', 'Neue Haas Grotesk Text', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.14px
  price-display:
    fontFamily: "'neue-haas-grotesk-display', 'Neue Haas Grotesk Display', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px

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
    rounded: "{rounded.full}"
    padding: 14px 28px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
  button-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-marigold-active:
    backgroundColor: "#e6b500"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  text-input-error:
    border: "2px solid #d32f2f"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.price-display}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-audio:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-sale:
    backgroundColor: "#d32f2f"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.full}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
  category-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  category-tile-active:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a pill-shaped button with a deep teal fill and white text. On hover, the background shifts to `{colors.primary-active}` (#0d6b5d) with no border change. The disabled state uses `{colors.primary-disabled}` (#a3d5cc) with white text, signaling reduced affordance. Used for "Add to Cart," "Checkout," and primary form submissions.

**`button-secondary`** — An outlined variant with a white fill, teal text, and a 2px teal border. Active state inverts the border to `{colors.primary-active}` and adds a soft surface background. Used for "Learn More," "View Details," and secondary actions alongside primary buttons.

**`button-tertiary`** — A text-only button with no background or border, using teal text. Used for less prominent actions like "Cancel," "Clear Filters," or inline links styled as buttons.

**`button-marigold`** — A high-energy variant using the marigold accent as background with dark ink text. Active state darkens to #e6b500. Used for sale promotions, limited-time offers, and high-visibility CTAs in banners or hero sections.

### Cards
**`product-card`** — A clean white card with an 8px radius, no padding on the container itself. The product image occupies the top with `{rounded.sm}` applied to the top corners only. Title uses `{typography.title-sm}` with 8px top padding and 16px horizontal padding, while the price sits below with 4px top padding and 16px bottom padding. Cards are typically arranged in a responsive grid with 16px gaps.

**`category-tile`** — A bordered tile (1px `{colors.hairline}`) with 16px padding and an 8px radius. Active state gains a 2px teal border. Used for category navigation on collection pages and the homepage.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height with a white background and a soft bottom border. Links use `{typography.nav-link}` at 14px with 0.14px letter spacing. Active links render in teal, inactive in muted gray. The bar contains the brand logo, category links, search icon, and cart icon on desktop, collapsing to a hamburger menu on mobile.

**`search-bar`** — A pill-shaped search input with a soft surface background and 1px hairline border. On focus, the border switches to a 2px teal stroke. Used in the nav bar and on search result pages.

### Forms
**`text-input`** — Standard text input with white background, 8px radius, 12px vertical and 16px horizontal padding, and a 1px hairline border. Focus state uses a 2px teal border. Error state uses a 2px red (#d32f2f) border. Used for email signups, shipping addresses, and search queries.

**`quantity-selector`** — A compact input for adjusting product quantities, with 8px padding, 40px height, and an 8px radius. Used on product detail pages and cart line items.

### Badges
**`product-badge`** — A small marigold badge with uppercase 11px bold text, 4px vertical and 8px horizontal padding, and a 4px radius. Used for "New," "Best Seller," and feature highlights on product cards.

**`product-badge-audio`** — A purple variant using `{colors.accent-purple}` for audio-specific products like headphones and speakers. Same sizing and typography as the standard badge.

**`product-badge-sale`** — A red badge (#d32f2f) for sale and discount indicators. Same sizing and typography as the standard badge.

### Footer
**`footer-section`** — A dark footer with `{colors.ink}` background and white text. Links render in muted-soft gray and shift to white on hover. The footer contains multi-column link groups, social icons, and legal text, with 48px vertical padding and 32px horizontal padding.

### Hero
**`hero-banner`** — A full-width hero section with a soft surface background, large display typography, and 64px vertical padding. The CTA button uses `{colors.primary}` with full pill rounding. Used on the homepage and campaign landing pages.

### Accordion
**`accordion-header`** — A clickable header with 16px padding and a soft bottom border. Content area collapses/expands below with body-sm typography and 16px bottom padding. Used for FAQ sections, product descriptions, and filter panels.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger navigation, stacked footer columns, hero padding reduces to 32px, buttons go full-width, product cards stack vertically |
| Tablet | 744–1128px | Two-column product grid, visible top nav with condensed links, footer splits into two rows, hero padding at 48px |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all category links, footer in single row with four columns, hero at full 64px padding |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, same nav and footer layout as desktop |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card tap targets include the entire card surface, not just text
- Quantity selector buttons are at least 40px × 40px
- Accordion headers have full-width tap targets at 48px minimum height
- Mobile hamburger menu icon is 44px × 44px
- Cart icon and search icon in nav are 44px × 44px

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-in drawer for category links
- Product filters collapse into an accordion panel on mobile, with a "Filters" button that opens a modal overlay
- Footer columns stack vertically on mobile, with each column becoming an accordion
- Product image galleries collapse from thumbnail strips to swipeable carousels on mobile
- Multi-column text sections (features, specs) collapse to single-column on mobile
- Hero content stacks vertically on mobile (text above CTA) instead of side-by-side

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow depth, scale transforms) could not be reliably extracted from static CSS
- Error state styling for forms beyond the red border (error message typography, icon placement) is inferred but not confirmed
- Dark mode or high-contrast mode variants are not present in the extracted data
- Sub-brand or collection-specific color palettes (e.g., limited edition drops) may exist beyond the extracted teal-purple-marigold system
- Animation timing and easing curves for transitions (hover, focus, page load) are not available
- Dropdown menu styling (mega menu, sub-navigation) was not captured in the extraction
- Modal/overlay styling (background scrim opacity, close button placement) is inferred from common patterns
- The extracted color list includes several grays (#eeeeee, #f4f4f4, #fafafa, #dedede, #c3c3c4, #ebebeb) that may represent different surface layers or borders — the mapping to specific components is based on frequency analysis and may not perfectly match the design intent
- The purple accent family (#be408e, #953bbd, #3f1b74, #a01deb) appears in the extraction but the exact usage rules (which purple for which context) are inferred from common audio-branding patterns
- Shopify checkout widget colors (Shopify Pay, Klarna, Afterpay) may be present in the extracted palette but have been excluded from the design system tokens
