---
version: alpha
name: "Autonomous"
source_url: "https://www.autonomous.ai"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A black-and-blue industrial precision that frames itself as "The AI Hardware Company" — #111111 ink against #f2f2f2 canvas, with #1965e0 as the single electric accent that pulls every CTA, badge, and interactive edge into focus. The palette is deliberately restrained: #555555 muted for secondary text, #171717 for near-black surfaces, and a sharp #c10015 red that appears only in sale badges or error states, never competing with the primary blue. No rounded corners above {rounded.sm} — buttons, cards, and inputs sit at 8px or 4px, giving the interface a machined, tool-like feel that matches the motorized standing desks and ergonomic chairs the brand sells. The typography runs a clean sans-serif stack at moderate weights (500–600 for display, 400 for body), with no decorative flourishes; the brand trusts its product photography and spec tables to carry the story. Navigation is a fixed top bar with a bold logo lockup, dropdown menus for product categories, and a cart icon that stays pinned to the right — utility over discovery. The checkout flow, powered by Shopify, inherits the same blue primary but introduces Klarna and Afterpay badge colors that sit outside the brand palette. Every interaction — hover underlines on nav links, blue border on focused inputs, subtle shadow on product cards — reinforces the message: this is hardware, engineered, and ready to ship.

colors:
  primary: "#1965e0"
  primary-active: "#144bb5"
  primary-disabled: "#8ab0f0"
  ink: "#111111"
  body: "#333333"
  muted: "#555555"
  muted-soft: "#777777"
  hairline: "#d4d4d4"
  hairline-soft: "#e5e5e5"
  canvas: "#f2f2f2"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-dark: "#171717"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-red: "#c10015"
  accent-red-soft: "#f44e4e"
  accent-blue-light: "#2299dd"
  success: "#1a8a1a"
  warning: "#f5a623"
  error: "#c10015"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-danger:
    backgroundColor: "{colors.accent-red}"
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
    padding: 12px 16px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px rgba(25,101,224,0.2)"
  text-input-error:
    borderColor: "{colors.error}"
    boxShadow: "0 0 0 2px rgba(193,0,21,0.2)"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    color: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.price}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.on-dark}"
  cart-icon:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 24px
  cart-count-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 18px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.md}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.md}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Buy Now", and "Shop" actions. On hover, shifts to `{colors.primary-active}` (#144bb5) with a subtle darkening. Disabled state uses `{colors.primary-disabled}` (#8ab0f0) and reduces opacity to 0.5. **`button-secondary`** — A white button with black text for secondary actions like "Learn More" or "View Details". On hover, adds a 1px `{colors.hairline}` border. **`button-secondary-outline`** — A transparent button with a blue border and blue text, used for "Compare" or "Customize" actions. On hover, fills with a 10% opacity blue background. **`button-danger`** — Red button for destructive actions like "Remove from Cart" or "Cancel Order". Uses `{colors.accent-red}` (#c10015) and darkens on hover.

### Text Inputs
**`text-input`** — Standard form input for checkout, search, and account forms. White background with a 1px `{colors.hairline}` border. On focus, the border switches to `{colors.primary}` with a 2px blue box-shadow ring. Error state uses `{colors.error}` (#c10015) with a red ring. **`select-input`** — Same styling as text input but with a custom dropdown arrow icon in `{colors.muted}`.

### Navigation
**`nav-bar`** — Fixed top navigation bar at 72px height with white background and a subtle bottom border (`{colors.hairline-soft}`). The logo sits on the left (typically black on white), product category links in the center, and utility icons (search, account, cart) on the right. **`nav-link-active`** — Active nav link underlined with a 2px `{colors.primary}` bar. **`nav-link-hover`** — Hover state shifts text color to `{colors.primary}`.

### Product Cards
**`product-card`** — The core product display component used on collection pages and search results. A white card with a subtle drop shadow (`0 1px 3px rgba(0,0,0,0.08)`) and `{rounded.sm}` corners. The product image fills the top with rounded top corners. Below the image, the title uses `{typography.title-md}` and the price uses `{typography.price}`. On hover, the shadow deepens to `0 4px 12px rgba(0,0,0,0.12)`. **`badge-sale`** — A small red badge overlaid on the product image corner, using `{colors.accent-red}` with uppercase white text. **`badge-new`** — Blue badge for new arrivals. **`badge-sold-out`** — Gray badge for out-of-stock items.

### Hero Section
**`hero-section`** — Full-width hero banner with a near-black background (`{colors.surface-dark}` #171717) and white text. Used for major campaigns and product launches. The headline uses `{typography.display-xl}` and a primary CTA button (`{hero-cta}`) sits below the copy. Background images or videos are full-bleed with a dark overlay.

### Footer
**`footer`** — Dark background footer (`{colors.surface-dark}`) with white text. Links use `{colors.muted-soft}` (#777777) and shift to white on hover. Organized into columns for product categories, support, company info, and social links.

### Accordion
**`accordion-header`** — Used on product detail pages for specs, shipping info, and reviews. A clickable header with a gray background (`{colors.canvas}`) and a chevron icon that rotates on open. **`accordion-content`** — The expandable content area with white background and body text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product cards stack in single column; hero text reduces to `{typography.display-md}`; footer stacks vertically; search bar moves to mobile drawer |
| Tablet | 744–1128px | Nav shows 4-5 category links; product cards in 2-3 column grid; hero maintains full-width but reduces padding; footer uses 2-column layout |
| Desktop | 1128–1440px | Full nav with all category links; product cards in 3-4 column grid; hero with max-width content container; footer uses 4-column layout |
| Wide | > 1440px | Content max-width at 1440px; hero content centered with 1200px max-width; product cards maintain 4-column grid with larger images |

### Touch Targets
- All buttons and interactive elements minimum 44px height (matches `{button-primary}` height)
- Nav links have 48px touch area (padding + height)
- Cart icon has 44x44px touch target
- Accordion headers have 48px touch height
- Product card CTAs maintain 44px minimum

### Collapsing Strategy
- Top nav collapses to hamburger menu at < 744px
- Product filters collapse to a slide-out drawer on mobile
- Multi-column footer collapses to single column on mobile
- Product image gallery collapses to single-image carousel on mobile
- Search bar collapses to icon-only on mobile, expanding to full input on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extractable from the live site; the typography block uses a common sans-serif stack (Inter, system fonts) as a reasonable default — actual brand font may differ
- Hover and focus states for most components were inferred from common patterns, not extracted from live CSS
- Error styling for forms (validation messages, error icons) was not observed
- Dark mode styling is not present on the live site and was not implemented
- Sub-brand or collection-specific palettes (e.g., for ErgoChair vs. SmartDesk lines) were not extracted
- Checkout flow uses Shopify's default styling with Klarna/Afterpay badges — those colors (#f44e4e, #2299dd) are not part of the brand palette
- Animation durations and easing curves were not extracted
- The extracted hex list (#111111, #f2f2f2, #1965e0, #2299dd, #c10015, #f44e4e, #555555, #171717) appears to be a generic web palette dominated by blues and grays; #1965e0 was selected as the most distinctive primary, but the brand may have a more unique accent that wasn't captured in the extraction
