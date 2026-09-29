---
version: alpha
name: "Carved"
source_url: "https://www.carved.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The brand's visual identity is anchored on a deep, warm brown #582012 — the meta theme-color that spills from the browser chrome into the site's own navigation bar, creating a seamless, almost leather-bound frame for the product photography. This brown, alongside its lighter companion #653c28, reads as wood stain and patina, not corporate neutral; it's the color of a well-worn knife handle or a guitar fretboard. Against a canvas of #eeeeee and #f2f1ee, the product shots — wooden phone cases with live-edge contours and resin inlays — become the sole source of visual texture. The typography runs Assistant and Harman-Sans, a pairing that feels utilitarian and workshop-adjacent: clean enough for e-commerce but with enough character to nod at the handcrafted. Buttons and badges lean into a restrained use of #ff0000 and #ff3939 for sale markers and cart indicators, a sharp, almost automotive-red accent that cuts through the earth tones. The overall mood is that of a maker's studio translated into a storefront: generous whitespace, soft card radii ({rounded.md}), and a navigation that lets the grain of the wood — not the chrome of the interface — do the selling.

colors:
  primary: "#582012"
  primary-active: "#4a1a0f"
  primary-disabled: "#d4c5bc"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#676767"
  muted-soft: "#9a9a9a"
  hairline: "#dedede"
  hairline-soft: "#eae7e3"
  canvas: "#f2f1ee"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#ff0000"
  accent-red-soft: "#ff3939"
  wood-light: "#653c28"
  wood-dark: "#593b26"
  star-rating: "#121212"

typography:
  display-xl:
    fontFamily: "'Assistant', 'Harman-Sans', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Assistant', 'Harman-Sans', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Assistant', 'Harman-Sans', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Assistant', 'Harman-Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', 'Harman-Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', 'Harman-Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', 'Harman-Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Assistant', 'Harman-Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Assistant', 'Harman-Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Assistant', 'Harman-Sans', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Assistant', 'Harman-Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Assistant', 'Harman-Sans', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "'Assistant', 'Harman-Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-new:
    backgroundColor: "{colors.wood-light}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
  star-rating:
    color: "{colors.star-rating}"
    size: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the deep brown `{colors.primary}` with white text. Used for "Add to Cart" and "Checkout" actions. On hover, it shifts to `{colors.primary-active}`. Disabled state uses `{colors.primary-disabled}`. The `{rounded.sm}` corner feels deliberate without being severe.
**`button-secondary`** — An outlined or ghost variant on `{colors.canvas}` with `{colors.ink}` text. Used for secondary actions like "View Details" or "Continue Shopping." Maintains the same height and padding as primary for alignment.
**`button-accent-red`** — A smaller, urgent button using `{colors.accent-red}`. Reserved for sale-related CTAs, clearance banners, or limited-time offers. Uses `{typography.button-sm}` to fit tighter spaces.

### Navigation
**`nav-bar`** — The top navigation bar is a solid band of `{colors.primary}` at 64px height. Links use `{typography.nav-link}` in white. The bar includes the brand logo (typically text or a logomark in white), a search icon, and a cart icon. On mobile, the nav collapses into a hamburger menu.
**`icon-button`** — Circular icon buttons for search, cart, and account. Transparent background with white icon color, `{rounded.full}`. Hover state adds a subtle white background at 10% opacity.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with `{rounded.md}` corners. Contains a product image (with `{rounded.md}` applied to the image itself), the product title in `{typography.title-md}`, the price in `{typography.price}`, and a star rating. The card has no border; it relies on the contrast between the white card and the `{colors.surface-soft}` or `{colors.canvas}` background.
**`badge-sale`** — A small, red badge (`{colors.accent-red}`) with white uppercase text. Positioned at the top-left of product images. Uses `{rounded.xs}` for a subtle pill shape.
**`badge-new`** — A brown badge (`{colors.wood-light}`) for new arrivals. Same shape and typography as the sale badge but in a wood-toned accent.

### Forms
**`text-input`** — Standard text input fields for search, email signup, and address forms. White background, `{colors.ink}` text, `{rounded.sm}` corners. Focus state adds a 2px `{colors.primary}` border.
**`search-bar`** — A pill-shaped search bar (`{rounded.full}`) with a white background and `{colors.muted}` placeholder text. Used in the header and on the search page. Includes a search icon on the left.

### Footer
**`footer`** — A full-width footer in `{colors.primary}` with white text. Contains links, social icons, and legal text in `{typography.body-sm}`. The footer uses generous vertical padding (`{spacing.section}`) to create breathing room.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; search bar moves below nav; cards stack vertically |
| Tablet | 744–1128px | Two-column product grid; nav remains expanded but with reduced link spacing; search bar is inline |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; search bar in header; cards show hover zoom effect |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; increased whitespace around cards |

### Touch Targets
- All interactive elements (buttons, links, icons) have a minimum touch target of 44x44px.
- Product card tap areas extend to the full card boundary.
- Nav links have 48px tap height on mobile.
- Icon buttons are 40x40px minimum.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger menu. The search bar moves to a dedicated row below the nav.
- The product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Footer links collapse into a single-column accordion on mobile.
- Badges remain visible at all breakpoints but may shrink in font size on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only `button-primary` and `button-secondary` hover states could be reliably inferred. Other interactive elements (links, icon buttons) may have custom hover effects not captured.
- **Error styling**: Form validation error colors and states (e.g., red border, error message typography) were not observed.
- **Focus states**: Keyboard focus indicators (outline, ring) were not extracted. Likely uses a `{colors.primary}` outline or box-shadow.
- **Dark mode**: No dark mode variant was detected. The brand may not support it.
- **Sub-brand palettes**: Carved may have seasonal or collection-specific color accents (e.g., for resin or stone inlays) that were not captured.
- **Typography scale**: The exact font sizes for `display-xl` and `title-lg` are estimated based on common e-commerce patterns. The extracted fonts (Assistant, Harman-Sans) are confirmed, but precise weights and sizes may vary.
- **Spacing scale**: The `section` value (64px) is an estimate. Actual section padding may be larger or smaller.
- **Checkout colors**: The extracted list includes Shopify Pay (#142688), Klarna (#ff5f00), and Afterpay (#eb001b, #f79e1b) colors. These are not part of the Carved brand palette and should be ignored for design system tokens.
- **Social icon colors**: The presence of Google colors (#4285f4, #34a853, #fbbc04, #ea4335) suggests social login buttons or icons. These are not brand colors.
