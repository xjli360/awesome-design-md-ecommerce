---
version: alpha
name: "Keychron"
source_url: "https://www.keychron.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A mechanical keyboard brand that uses a distinctive teal-green (#108474) as its primary voltage — an unusual choice for a tech-hardware company that signals precision without the cold blue of gaming peripherals or the black of enterprise IT. The site runs on a warm off-white canvas (#f9f9f9) with generous use of soft grays (#eeeeee, #e5e5e5, #dadada) for card backgrounds and section dividers, creating a calm, workshop-like atmosphere. A marigold accent (#fade20) appears sparingly — on sale badges, highlight tags, and the occasional CTA — adding a pop of energy that reads as "deal alert" rather than brand identity. The typography stack is DM Sans at display sizes (clean, geometric, approachable) with Montserrat and Roboto as fallbacks, set at moderate weights (400-600) that let the product photography of aluminum cases and RGB keycaps do the heavy lifting. Product cards use soft corners ({rounded.md} ~12px) with thin hairline borders (#e1e1e1), while buttons and badges are more rounded ({rounded.lg} ~20px) to feel tactile and inviting. The nav bar is a fixed white strip with a subtle bottom hairline, and the search bar sits as a pill-shaped input with a green accent border. The overall mood is "enthusiast workshop" — clean enough for productivity, warm enough for hobbyists, with the green acting as a constant visual anchor across category pages, product detail, and cart.

colors:
  primary: "#108474"
  primary-active: "#0d6b5e"
  primary-disabled: "#a3d5cc"
  ink: "#353535"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#808085"
  hairline: "#e1e1e1"
  hairline-soft: "#eeeeee"
  canvas: "#f9f9f9"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#fade20"
  accent-marigold-active: "#f1e10d"
  badge-sale: "#fade20"
  badge-new: "#899df1"
  star-rating: "#fade20"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'DM Sans', 'Montserrat', 'Roboto', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'DM Sans', 'Montserrat', 'Roboto', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'DM Sans', 'Montserrat', 'Roboto', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'DM Sans', 'Montserrat', 'Roboto', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', 'Montserrat', 'Roboto', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', 'Montserrat', 'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', 'Montserrat', 'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', 'Montserrat', 'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', 'Montserrat', 'Roboto', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'DM Sans', 'Montserrat', 'Roboto', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'DM Sans', 'Montserrat', 'Roboto', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.2px
  micro-label:
    fontFamily: "'DM Sans', 'Montserrat', 'Roboto', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'DM Sans', 'Montserrat', 'Roboto', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'DM Sans', 'Montserrat', 'Roboto', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.15px
  link:
    fontFamily: "'DM Sans', 'Montserrat', 'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', 'Montserrat', 'Roboto', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
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
    rounded: "{rounded.lg}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: 11px 27px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-pill-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-marigold-active:
    backgroundColor: "{colors.accent-marigold-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid #c13515"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-pill-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 8px 0
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.06)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-price-sale:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.surface-card}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.md}"
    padding: "10px 20px"
    height: 44px
  category-filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  category-filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
    border: "1px solid {colors.hairline}"
    height: 36px
  add-to-cart-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "12px 24px"
    height: 56px
    boxShadow: "0 -2px 8px rgba(0,0,0,0.06)"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Buy Now", and primary form submissions. Rendered in the brand teal (#108474) with white text and generous 20px corner radius ({rounded.lg}), giving it a friendly, approachable feel. On hover, shifts to a darker shade ({colors.primary-active}) with no scale or shadow change — the brand prefers color-depth over motion. Disabled state uses a muted pastel teal ({colors.primary-disabled}) with white text, maintaining readability.

**`button-secondary`** — Used for secondary actions like "View Details", "Compare", and "Cancel". A white button with a thin hairline border and ink text. On hover, the border deepens to ink and the background shifts to soft surface. The 20px corner radius matches the primary button for visual consistency across action pairs.

**`button-tertiary-text`** — A text-only link styled as a button, used for "Learn More" and "Read Reviews". Uses the primary teal for text color, no background or border, and inherits button typography. On hover, text color darkens to primary-active.

**`button-pill-marigold`** — A special accent button reserved for sale promotions, limited-time offers, and "Deal of the Day" CTAs. Uses the marigold yellow (#fade20) with dark ink text and a fully pill-shaped radius. On hover, shifts to the darker marigold shade (#f1e10d). This button is intentionally distinct from the primary teal system to signal urgency and value.

### Text Inputs & Search
**`text-input`** — Standard form input for checkout fields, address forms, and account settings. White background with a thin hairline border and 12px corner radius. On focus, the border thickens to 2px and turns primary teal. Error state uses a red border (#c13515) with no background tint change — the brand keeps error states minimal.

**`search-bar-pill`** — The site-wide search input, styled as a pill-shaped field with a white background and hairline border. On focus, the border becomes 2px primary teal. The pill shape ({rounded.full}) distinguishes search from other form inputs and gives it a more discoverable, friendly appearance.

### Navigation
**`nav-bar`** — Fixed top navigation bar at 64px height with a white background and a soft hairline bottom border. Navigation links use 15px DM Sans at weight 500. Active nav items show a 2px primary teal bottom border and teal text color. Inactive items use body gray (#555555). The nav includes a dropdown component for category menus, rendered as a white card with 12px corner radius and a subtle drop shadow.

**`nav-dropdown`** — Dropdown menu panels that appear on hover over nav items. White background with 12px corner radius and a soft box shadow (0 4px 12px rgba(0,0,0,0.08)). Contains links styled as body-sm with 8px vertical padding per item.

### Product Cards
**`product-card`** — The primary content container for product listings on category pages and search results. White background with a soft hairline border and 12px corner radius. On hover, gains a subtle box shadow and the border becomes slightly more visible. The card image has rounded top corners matching the card radius, while the bottom is flat. Title uses title-sm typography, price uses body-md in body color, and sale prices switch to primary teal.

**`badge-sale`**, **`badge-new`**, **`badge-out-of-stock`** — Small rectangular badges overlaid on product card images. Sale badges use the marigold yellow with dark ink text. New badges use a soft blue (#899df1) with white text. Out-of-stock badges use muted-soft gray (#808085) with white text. All badges use 4px corner radius and 11px bold typography.

### Footer
**`footer-section`** — The site footer uses a dark ink background (#353535) with white text for headings and muted gray for links. The newsletter signup combines a standard text input with a primary teal submit button. Footer links use muted-soft gray (#808085) and shift to white on hover.

### Category Filters
**`category-filter-chip`** — Pill-shaped filter chips used on collection pages for keyboard size, switch type, and connectivity. Soft gray background with a hairline border and body text. Active state fills with primary teal and white text. The pill shape ({rounded.full}) makes filters feel interactive and scannable.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 columns), nav collapses to hamburger menu, search bar becomes full-width below nav, product cards stack vertically, filter chips wrap to multiple rows, footer stacks in single column |
| Tablet | 744–1128px | Two-column product grid, nav items remain visible but condensed (no dropdowns), search bar is 50% width, filter chips show in a horizontal scrollable strip |
| Desktop | 1128–1440px | Three-column product grid, full nav with dropdowns, search bar is 33% width centered in nav, filter chips in a single row, footer has 3-4 columns |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, nav and search maintain desktop layout, additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px on mobile
- Filter chips and badge elements maintain 36px minimum height for tap targets
- Nav hamburger icon is 48x48px with 8px padding
- Quantity selector buttons are 36x36px minimum
- Add-to-cart bar is fixed at 56px height on mobile with safe-area padding

### Collapsing Strategy
- Top nav collapses to a hamburger menu on mobile (< 744px), revealing a full-screen overlay with category links, search, and account links
- Product filters collapse to a "Filter" button that opens a bottom sheet on mobile
- Product description sections (specs, reviews, shipping) collapse to accordion panels on mobile and tablet
- Footer columns collapse to a single column on mobile with expandable section headers
- Image galleries collapse from thumbnail strip to swipeable dots on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components are inferred from common patterns; exact transition durations and easing curves were not extracted
- Error state styling for forms (validation messages, error icons) was not visible in the extracted data
- Dark mode or high-contrast mode variants are not present in the extracted palette
- The exact font stack order is inferred; DM Sans appears most frequently but Montserrat and Roboto may have different fallback priorities
- Sub-brand or collection-specific color variations (e.g., "K Pro" vs "Q Series") could not be extracted
- The extracted color list includes many near-identical grays (#eeeeee, #f9f9f9, #f7f7f7, #f0f0f0, #fafafa, #f2f2f2) — the exact surface and hairline tokens were chosen based on frequency and context, but the brand may use more or fewer distinct gray values
- The marigold accent (#fade20) and blue badge (#899df1) are present in the extraction but their exact usage contexts (which badges, which CTAs) are inferred from common ecommerce patterns
- Shopify checkout widget colors (Klarna, Afterpay, etc.) may have been partially included in the extraction; the primary teal (#108474) is distinctive enough to be confidently the brand color
- Star rating color is assumed to match the marigold accent based on common ecommerce patterns, but could not be confirmed from extracted data
- The "phones" mention in the page title suggests mobile compatibility but no mobile-specific design tokens were extracted
