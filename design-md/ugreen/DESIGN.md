---
version: alpha
name: "Ugreen"
source_url: "https://www.ugreen.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A matte-black-and-green electronics ecosystem built for the charging-drawer crowd — the brand that makes the cables, hubs, and power banks you never think about until you need one, and then you reach for the one with the #007934 leaf. That green, a deep chlorophyll, is the single brand voltage: it appears on the primary CTA, the logo mark, the LED ring on a GaN charger, and the silicone tie on a braided USB-C cable. The canvas is a cool #f8f8f8, not pure white — a deliberate off-white that reads as technical rather than retail, closer to a tool manufacturer than a phone-case brand. Typography runs Metropolis at moderate weights (500–600 for display, 400 for body), never heavy; the brand trusts product photography — glossy black plastic, brushed aluminum, glowing green ports — over typographic muscle. Cards and buttons use soft {rounded.sm} corners, while the hero search bar and category pills go {rounded.full}, creating a friendly, approachable feel for what is fundamentally industrial hardware. The nav bar is a dark band at #121212 with white text, a rare inversion that signals "pro" or "premium" without shouting. Badges for "New," "Sale," and "Best Seller" appear in #8b0000 and #ee9441 — a red and an orange that break the green/gray scheme intentionally, like warning lights on a control panel. The footer collapses into a dense, link-heavy grid on mobile, but the product grid stays generous, with 16px gutters and 12px card padding that keep the browsing experience airy despite the technical subject matter.

colors:
  primary: "#007934"
  primary-active: "#006400"
  primary-disabled: "#a3d8b0"
  ink: "#121212"
  body: "#404040"
  muted: "#a3a3a3"
  muted-soft: "#c8c8c8"
  hairline: "#dedede"
  hairline-soft: "#e9eaeb"
  canvas: "#f8f8f8"
  surface-soft: "#f0f1f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#8b0000"
  accent-orange: "#ee9441"
  accent-green-bright: "#3ed660"
  link-blue: "#1975b7"
  badge-sale: "#c30000"
  badge-new: "#ee901d"
  badge-best: "#7b1ec7"
  dark-nav: "#121212"
  dark-nav-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Metropolis', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Metropolis', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Metropolis', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Metropolis', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Metropolis', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "'Metropolis', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Metropolis', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Metropolis', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "'Metropolis', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Metropolis', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.2px
  link:
    fontFamily: "'Metropolis', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Metropolis', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Metropolis', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-green:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.dark-nav}"
    textColor: "{colors.dark-nav-text}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.dark-nav-text}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
    boxShadow: "0 1px 2px rgba(0,0,0,0.04)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  hero-search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 52px
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  hero-search-icon:
    color: "{colors.muted}"
    size: 20px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "12px 0"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginBottom: "{spacing.md}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
    marginBottom: "{spacing.sm}"
  footer-link-hover:
    color: "{colors.primary}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-best-seller:
    backgroundColor: "{colors.badge-best}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    padding: "0 12px"
  add-to-cart-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
    boxShadow: "0 -2px 8px rgba(0,0,0,0.06)"

## Components

### Buttons
**`button-primary`** — The workhorse CTA, a solid #007934 green rectangle with {rounded.sm} corners and white Metropolis 600 at 15px. On hover it deepens to #006400; disabled it fades to a muted green (#a3d8b0). Used for "Add to Cart," "Buy Now," and primary form submissions. **`button-secondary`** — An outlined variant on a white or light gray background, with a 1px #dedede border and #121212 text. Active state fills the background with #f0f1f2. **`button-tertiary-text`** — A text-only link styled as a button, using the primary green for the text color, no background or border. Used for "Learn More" and "View Details" links. **`button-pill-green`** — A fully rounded pill in the primary green, used for filter tags and quick-action chips. **`button-pill-outline`** — The inverse pill, transparent with a hairline border, used for inactive filter states.

### Cards
**`product-card`** — A white card with {rounded.sm} corners, 12px padding, and a subtle 1px shadow. On hover the shadow deepens to 4px. The card contains a square image with {rounded.xs} corners, a title in {typography.title-sm}, and a price in {typography.body-sm}. Badges (New, Sale, Best Seller) overlay the top-left of the image. **`product-card-badge`** — A small, uppercase, 11px label with 0.5px letter spacing, set on a red (#8b0000), orange (#ee901d), or purple (#7b1ec7) background depending on the badge type.

### Navigation
**`nav-bar`** — A dark (#121212) 60px bar with white, uppercase nav links in Metropolis 500 at 14px with 0.5px letter spacing. On scroll, the bar transitions to white with a subtle shadow. The logo sits left, the nav links center, and the cart/search icons right. **`nav-link`** — Uppercase, 14px, 0.5px letter spacing, white on dark nav, green on active state. **`category-strip`** — A horizontal scrollable strip of pill-shaped category filters below the hero. Inactive pills are gray (#f0f1f2 background, #404040 text); active pills flip to the primary green.

### Forms
**`text-input`** — A 44px tall input with {rounded.sm} corners, a 1px #dedede border, and 12px/16px padding. On focus the border turns #007934; on error it turns #8b0000. **`quantity-selector`** — A bordered box with a minus button, the quantity number, and a plus button. Used on product detail pages for cart quantity adjustment.

### Footer
**`footer-section`** — A light gray (#f0f1f2) section with columns of links. Each column has a bold heading in {typography.title-sm} and links in {typography.link} at #a3a3a3 that turn green on hover. The footer collapses to a single column on mobile with accordion-style expandable sections.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item per row), nav collapses to hamburger menu, category strip scrolls horizontally, footer becomes accordion, hero search bar reduces to icon-only, product card padding drops to 8px |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed (icons only for cart/search), category strip fully visible, hero search bar shows placeholder text, product card padding at 12px |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, category strip with 8+ pills visible, hero search bar with full input and search button, product card padding at 12px |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, nav bar centered, category strip centered, hero section with wider search bar |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px
- Category pills are 36px tall with 8px padding, meeting the 44px effective touch area
- Quantity selector buttons are 44px tall with 12px horizontal padding
- Nav links have 8px vertical padding, making the effective touch area 60px (full nav bar height)
- Product card links (title, image) have implicit touch targets through the card's 12px padding

### Collapsing Strategy
- Top nav: On mobile (<744px), the full nav link list collapses into a hamburger menu. Cart and search icons remain visible.
- Category strip: On mobile, the strip becomes horizontally scrollable with a "fade" gradient at the edges to indicate overflow.
- Product grid: Collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Footer: On mobile, link columns collapse into accordion sections with expand/collapse toggles. The newsletter signup remains visible at the top.
- Hero section: On mobile, the hero image reduces height by 40%, and the search bar becomes an icon-only button that opens a full-screen search overlay.
- Product detail page: On mobile, the image gallery becomes a single-column swipeable carousel, and the "Add to Cart" bar sticks to the bottom of the viewport.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted from the static site; only primary button and product card hover states were observed.
- Error states for forms (validation messages, error icons) were not visible in the extracted data.
- Dark mode is not implemented on the live site; no dark theme tokens are available.
- Sub-brand or product-line-specific color palettes (e.g., for "Ugreen Pro" or "Ugreen Nexode") could not be distinguished from the main brand palette.
- The exact font weight for Metropolis in display sizes is inferred from common usage; the extracted CSS only showed "Metropolis" without specific weight declarations.
- Animation and transition durations (e.g., button hover, nav scroll, card hover) were not extractable; a default of 200ms ease-in-out is assumed.
- The hero search bar's internal layout (icon position, placeholder text style, button vs. icon) is inferred from common e-commerce patterns.
- The footer's accordion behavior on mobile is inferred from common responsive patterns; the exact breakpoint and animation are not confirmed.
- The nav bar's scroll behavior (transition from dark to white) is inferred from the presence of both a dark nav and a white scrolled state in the extracted CSS.
- The product card's aspect ratio is assumed to be 1:1 based on common product photography; the actual ratio may vary by product type.
