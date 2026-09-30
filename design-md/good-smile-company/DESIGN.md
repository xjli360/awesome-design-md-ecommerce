---
version: alpha
name: "Good Smile Company"
source_url: "https://www.goodsmileus.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A collector's marketplace where the #ff860d voltage of an unboxing moment — that first flash of orange against a near-black stage — becomes the brand's entire emotional signature. Good Smile Company wraps its anime and pop-culture figures in a palette that reads like a convention hall at dusk: deep charcoals (#36363b, #444349, #202025) and a true black (#121212) form the display case, while two oranges — a bright #ff860d and a slightly warmer #f47920 — act as the accent lights that pick out price tags, add-to-cart buttons, and pre-order badges. The canvas is a warm off-white (#fffaf4) that avoids the sterile hospital feel of pure white, and the secondary gray (#939598) and light gray (#dedede) handle borders, dividers, and secondary text. The site runs on Shopify, so the checkout flow inherits that platform's conventions, but the storefront itself is a dark, dramatic gallery: product images float on black backgrounds, typography is clean and unobtrusive, and every interactive element — from the pill-shaped search bar to the orange CTA buttons — is designed to get out of the way of the merchandise. The brand trusts its IP above all else; the design system is a neutral, high-contrast frame for Nendoroids, Figmas, and scale figures.

colors:
  primary: "#ff860d"
  primary-active: "#f47920"
  primary-disabled: "#dedede"
  ink: "#121212"
  body: "#36363b"
  muted: "#939598"
  muted-soft: "#dedede"
  hairline: "#dedede"
  hairline-soft: "#f0f0f0"
  canvas: "#fffaf4"
  surface-soft: "#f5f0eb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  pre-order-badge: "#ff860d"
  sold-out-badge: "#939598"
  figure-card-bg: "#121212"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
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
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.figure-card-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-title:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
  product-card-price:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.price}"
  pre-order-badge:
    backgroundColor: "{colors.pre-order-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  sold-out-badge:
    backgroundColor: "{colors.sold-out-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
  category-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.link}"
    rounded: "{rounded.none}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 40px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature orange (#ff860d) against white text. Used for "Add to Cart", "Pre-Order", and "Checkout" actions. On hover, shifts to the deeper #f47920. Disabled state fades to #dedede with muted text, signaling unavailability. Padding is 12px 24px with a subtle 8px border radius.

**`button-secondary`** — An outlined variant on a white background with ink text and a 1px hairline border. Used for "View Details", "Continue Shopping", and secondary checkout actions. On hover, the background shifts to the soft surface tone and the border turns to ink.

**`button-tertiary-text`** — A text-only button in the primary orange, used for "Learn More" or "See All" links within content sections. No background or border — relies entirely on the orange color for affordance.

### Navigation
**`nav-bar`** — A fixed-height 64px bar in deep ink (#121212) with uppercase, letter-spaced nav links in white. The active link or current section uses the primary orange. The bar is full-width and contains the brand logo, category links, and a search icon.

**`nav-link-active`** — The active state for navigation items, switching text color to the primary orange to indicate the current page or section.

### Search
**`search-bar`** — A pill-shaped input field on the warm canvas background with a 1px hairline border. Used in the header for product search. The full border radius and generous padding make it feel approachable and quick to use.

### Cards
**`product-card`** — The primary product display component. A dark card (#121212) that acts as a stage for the product image. The dark background makes the figure photography pop, especially for brightly colored anime characters. Text on the card is white for readability.

**`product-card-title`** — The product name, rendered in the standard title typography on a white background below the dark card area. This creates a clear separation between the visual hero and the product metadata.

**`product-card-price`** — The price, always shown in the primary orange to draw the eye. Uses a bold weight to stand out against the product title.

### Badges
**`pre-order-badge`** — A small orange badge with uppercase text, used to flag items available for pre-order. The 4px border radius and tight padding keep it compact and unobtrusive.

**`sold-out-badge`** — A gray badge indicating an item is sold out. Uses the same styling as the pre-order badge but in a muted tone to de-emphasize unavailable items.

### Footer
**`footer`** — A full-width dark section (#121212) with muted gray text for secondary information and white links for navigation. The footer contains links to support, about, and legal pages.

**`footer-link`** — Footer navigation links in white against the dark background. Uses the standard link typography.

### Hero
**`hero-banner`** — A full-width banner section on a dark background with large white display text. Used for promotional campaigns, new arrivals, and seasonal events. The dark background ensures the hero image or video is the focal point.

### Category Links
**`category-link`** — Text links used in category navigation strips. They have no border radius and rely on the body text color for a clean, minimal appearance.

### Icon Buttons
**`icon-button`** — Circular icon buttons (e.g., cart, account, search) in the navigation bar. Transparent background with white icons on the dark nav bar. The full border radius creates a clean circle.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Navigation collapses to hamburger menu. Product cards stack in a single column. Search bar moves to a full-width row below the nav. Hero banner text reduces to display-md size. Footer links stack vertically. |
| Tablet | 744–1128px | Navigation shows limited links (logo, search, cart, menu). Product cards display in a 2-column grid. Hero banner maintains full-width but with reduced padding. |
| Desktop | 1128–1440px | Full navigation with all category links visible. Product cards in a 3- or 4-column grid. Hero banner at full height with large display text. |
| Wide | > 1440px | Maximum content width constraint (1440px) with centered layout. Product cards in a 4-column grid. Hero banner may include parallax or full-bleed imagery. |

### Touch Targets
- All interactive elements (buttons, links, icons) maintain a minimum 44px height for touch accessibility.
- Icon buttons in the nav bar are 40px circles, exceeding the 44px target when including padding.
- Product card tap targets (title, price, image) are at least 48px tall.
- Search bar is 40px tall with 10px internal padding, providing a comfortable touch area.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses to a hamburger menu with a slide-out drawer.
- Category links in the navigation strip collapse to a horizontal scrollable list on tablet and mobile.
- Footer links collapse from a multi-column layout to a single vertical stack on mobile.
- Hero banner text reduces in size and padding on mobile to avoid overflow.
- Product card grids reduce columns: 4 → 3 → 2 → 1 as viewport narrows.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extracted from the live site. The typography block uses Inter as a reasonable system-adjacent sans-serif, but the actual brand font may differ. A review of the site's CSS or design assets is needed.
- Hover and focus states for most components are inferred from common patterns (darkening primary, adding borders) but were not extracted from the live site.
- Error states for form inputs (e.g., invalid email, missing required fields) were not observed.
- Dark mode is not implemented; the site uses a consistent light/dark contrast approach (dark nav, light content areas).
- The Shopify checkout flow uses its own design system, which may differ from the storefront's palette and typography.
- Sub-brand or collection-specific color variations (e.g., Nendoroid vs. Figma vs. scale figures) were not observed.
- Loading states, skeleton screens, and empty states were not extracted.
- The exact border radius for product cards (rounded.md) is an estimate based on the general design language; the actual value may vary.
- The primary-active color (#f47920) is inferred from the extracted palette as the warmer orange, but the exact hover state may be a different shade or include an opacity change.
