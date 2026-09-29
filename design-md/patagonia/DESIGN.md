---
version: alpha
name: "Patagonia"
source_url: "https://www.patagonia.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A brand built on a single, unapologetic black (#020202) that runs through every headline, every primary button, every footer background — not as an accent but as the foundational voltage. The palette is deliberately austere: pure white canvas, black ink, and the occasional muted gray for secondary text or borders. There is no secondary brand color in the extracted data; the brand trusts its photography of mountains, rivers, and worn-in fleece to supply all the warmth. Typography runs Avenir Next in three weights — Light, Medium, and Bold — with the bold weight reserved for display headlines and primary CTAs, while body copy stays in a clean Arial or Helvetica fallback. The system avoids decorative flourishes: buttons are flat rectangles with tight padding, navigation is a simple left-aligned logo with right-aligned links, and product cards use a thin hairline border and generous whitespace. The checkout page title ("Hang Tight! Routing to checkout...") reveals a casual, human tone that matches the brand's anti-marketing posture — no urgency, no pressure, just a quiet confidence. The design feels like a climbing wall: functional, honest, and built to last.

colors:
  primary: "#020202"
  primary-active: "#333333"
  primary-disabled: "#666666"
  ink: "#020202"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#020202"
  link-hover: "#333333"
  error: "#cc0000"
  success: "#2e7d32"

typography:
  display-xl:
    fontFamily: "'Avenir Next LT W02 Bold', Arial, Helvetica, Verdana, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Avenir Next LT W02 Bold', Arial, Helvetica, Verdana, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Avenir Next LT W02 Bold', Arial, Helvetica, Verdana, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'AvenirNextLTW02-Medium', Arial, Helvetica, Verdana, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'AvenirNextLTW02-Medium', Arial, Helvetica, Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'AvenirNextLTW02-Medium', Arial, Helvetica, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, Helvetica, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Avenir Next LT W02 Bold', Arial, Helvetica, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Avenir Next LT W02 Bold', Arial, Helvetica, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, Helvetica, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Avenir Next LT W02 Bold', Arial, Helvetica, Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Avenir Next LT W02 Bold', Arial, Helvetica, Verdana, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 12px 24px
    height: 44px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.primary}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-overlay:
    backgroundColor: "{colors.primary}"
    opacity: 0.3
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.muted-soft}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    padding: "0 {spacing.lg} {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. Flat black rectangle with white uppercase Avenir Next Bold text. No rounded corners, no shadows — just a confident block of color. On hover, shifts to a dark gray (#333333). Disabled state fades to medium gray (#666666) with the same flat treatment.

**`button-secondary`** — An outlined variant for secondary actions. White background with a 2px black border and black uppercase text. On hover, the background fills with a soft gray (#f5f5f5). Used for "Learn More" or "Add to Wishlist" actions where the primary button is reserved for "Add to Cart" or "Checkout."

**`button-tertiary`** — A text-only button for the least prominent actions. No background, no border — just black uppercase Avenir Next Bold text. Used for links like "View Details" within product cards or "Cancel" in forms.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height. White background with left-aligned logo and right-aligned navigation links. Links use 13px uppercase Avenir Next Bold with 0.5px letter spacing. Active link is black, inactive links are also black but with a subtle hover state that underlines or darkens slightly.

**`nav-link`** — Individual navigation items with 8px vertical and 12px horizontal padding. Active state uses the primary black color. Hover state may add an underline or slight opacity change.

### Cards
**`product-card`** — A clean product display card with no rounded corners. White background with a thin, soft gray border (#e5e5e5). Contains a product image (with a soft gray placeholder background), title in 16px Avenir Next Medium, and price in 16px Arial body. A small black badge may appear for "New" or "Sale" indicators.

**`product-card-badge`** — A small, flat black rectangle with white uppercase 10px text. Used to flag new arrivals, sale items, or limited editions. Padding is tight at 2px top/bottom and 8px left/right.

### Forms
**`text-input`** — Standard text input fields with a white background, 1px light gray border (#cccccc), and 16px Arial body text. On focus, the border thickens to 2px black. Error state uses a 2px red border (#cc0000). Height is 48px with 12px vertical and 16px horizontal padding.

**`select-input`** — Dropdown selectors matching the text input style. Same dimensions, border, and typography. The dropdown arrow is typically a simple black chevron.

### Hero
**`hero-banner`** — Full-width hero section with a soft gray background (#f5f5f5). Large 36px Avenir Next Bold headline with -0.5px letter spacing. Content is centered with generous padding (64px top/bottom, 24px sides). An optional overlay at 30% opacity black can be used over background images.

### Footer
**`footer`** — A full-width black (#020202) footer with white text. Links are 14px Arial with a hover state that lightens to a medium gray (#999999). Padding is generous at 48px top/bottom and 24px sides. The footer typically contains columns for customer service, company info, and social links.

### Accordion
**`accordion`** — Collapsible sections used for FAQs or product details. White background with a thin soft gray border (#e5e5e5). Headers use 16px Avenir Next Medium with 16px vertical and 24px horizontal padding. Content area has 24px horizontal padding and 16px bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger menu replaces top nav, product cards stack vertically, hero text reduces to 24px, footer collapses to single column |
| Tablet | 744–1128px | Two-column product grid, top nav remains but may collapse secondary links, hero maintains 28px headline, footer uses two columns |
| Desktop | 1128–1440px | Three-column product grid, full top nav visible, hero at 36px headline, footer uses four columns |
| Wide | > 1440px | Max-width container at 1440px, content centered, product grid may expand to four columns, hero remains full-width |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Navigation links have 8px vertical padding to ensure comfortable tap targets
- Product card images are tappable with no minimum size requirement (image fills card width)
- Accordion headers are full-width with 16px vertical padding for easy tapping

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px
- Product grid reduces from 3 columns to 2 at tablet, then 1 at mobile
- Footer columns collapse from 4 to 2 at tablet, then 1 at mobile
- Hero banner text reduces in size at each breakpoint, with optional image cropping on mobile
- Search bar may collapse to an icon on mobile, expanding on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one extracted hex color (#020202) was available from the live site analysis. All other color tokens (grays, whites, reds, greens) are inferred from common Patagonia design patterns and standard accessibility best practices — they may not match the exact live site values.
- No meta theme-color was detected, so the browser chrome color is unknown.
- The site does not appear to be Shopify-based, so checkout-specific colors (Shopify Pay buttons, etc.) are not included.
- Hover, focus, and active states for all components are inferred from common patterns — exact transition durations, opacity values, and animation curves are unknown.
- Error and success colors (#cc0000 and #2e7d32) are standard web defaults, not confirmed Patagonia-specific values.
- Dark mode preferences and associated color tokens are not available.
- Sub-brand or collection-specific color palettes (e.g., for "Patagonia Provisions" or "Worn Wear") are not captured.
- Font sizes and line heights for typography tokens are estimated based on common e-commerce patterns and the extracted font families — exact values from the live site are not available.
- The brand's secondary color (often a green or blue in some Patagonia materials) is not present in the extracted data and is intentionally omitted to avoid fabrication.
