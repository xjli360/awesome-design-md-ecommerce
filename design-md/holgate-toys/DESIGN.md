---
version: alpha
name: "Holgate Toys"
source_url: "https://www.holgatetoy.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A wooden toy brand that uses #ff0000 as its primary voltage — a pure, unapologetic red that reads as both childhood primary and mid-century toy-store signage, not the muted clay or ochre that "natural" brands reach for. The palette is built on a stark black-and-white skeleton (#121212 ink, #ffffff canvas) with red as the only color that gets to be loud; every other chromatic hue in the extracted palette (#0071e3 blue, #334fb4 navy, #62bbfa sky) appears to belong to Shopify checkout widgets or social-icon footers rather than the brand itself. Assistant serves as the primary typeface, a clean geometric sans that pairs with the wood-grain photography and blocky toy silhouettes without competing for attention. The site runs on Shopify, so the product-grid layout follows the platform's standard 2-3-4 column breakpoints, but the brand asserts itself through red-on-white CTAs, red price badges, and red "ADD TO CART" buttons that create a consistent pulse across every product page. There is no gradient, no drop shadow, no decorative flourish — the design trusts the physical product photography (wooden trains, blocks, puzzles) to supply all the warmth, while the UI stays in a crisp, almost industrial register. The red (#ff0000) appears in three states: full saturation for primary actions, a slightly darker #cc0000 for hover, and a washed-out #ff4444 for disabled or secondary indicators. The overall feeling is less "cozy toy store" and more "design-conscious maker's catalog" — the red is the exclamation point, the white is the silence, and the wood is the substance.

colors:
  primary: "#ff0000"
  primary-active: "#cc0000"
  primary-disabled: "#ff4444"
  ink: "#121212"
  body: "#1d1d1f"
  muted: "#677279"
  muted-soft: "#7d7d7d"
  hairline: "#d0d0d0"
  hairline-soft: "#e1e3e4"
  canvas: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-badge: "#ff0000"
  sale-badge-text: "#ffffff"
  error: "#cc0000"
  error-soft: "#ff4444"
  social-blue: "#0071e3"
  social-navy: "#334fb4"

typography:
  display-xl:
    fontFamily: "'Assistant', 'SF Pro Text', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Assistant', 'SF Pro Text', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Assistant', 'SF Pro Text', -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Assistant', 'SF Pro Text', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Assistant', 'SF Pro Text', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', 'SF Pro Text', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', 'SF Pro Text', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', 'SF Pro Text', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Assistant', 'SF Pro Text', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Assistant', 'SF Pro Text', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Assistant', 'SF Pro Text', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Assistant', 'SF Pro Text', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Assistant', 'SF Pro Text', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Assistant', 'SF Pro Text', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
    rounded: "{rounded.none}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
    rounded: "{rounded.none}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-sale-price:
    typography: "{typography.price}"
    textColor: "{colors.primary}"
    marginTop: "{spacing.xs}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    height: 24px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  add-to-cart-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: "{spacing.md} {spacing.lg}"
    borderTop: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The brand's single strongest action signal. A solid red rectangle (`{rounded.sm}`) with white text in 15px/600 weight Assistant, 0.5px letter-spacing for a slightly authoritative read. On hover it darkens to `#cc0000`; disabled state uses `#ff4444` — still red but visibly washed, signaling the action is unavailable without breaking the red-as-primary rule. The 44px height meets touch-target minimums while keeping the button compact enough for product-grid add-to-cart rows.

**`button-secondary`** — An outlined alternative for secondary actions like "View Details" or "Learn More". Uses a 2px solid `{colors.ink}` border on a white canvas, same 44px height and `{rounded.sm}` corners. Active state fills the background with `{colors.surface-soft}` (`#f3f3f3`) for a subtle press effect. No red — the brand reserves its primary color for primary actions only.

**`button-ghost`** — Text-only button for tertiary actions like "Cancel" or "Clear Filters". Transparent background, `{colors.ink}` text, no border. Padding is reduced to 12px 16px to keep the footprint minimal. Hover state would add a light `{colors.surface-soft}` background (not extracted, noted in gaps).

### Cards
**`product-card`** — The core shopping unit. A white canvas with zero rounding — the brand does not soften its product images with rounded corners, letting the physical toy shapes (trains, blocks, puzzles) provide all the organic form. The image container is a perfect 1:1 square with `{colors.surface-soft}` background for loading states. Title sits in 16px/600 weight, price in 18px/700 weight. Sale prices flip to `{colors.primary}` red, paired with a `{rounded.none}` red badge reading "SALE" in 11px uppercase bold.

### Navigation
**`nav-bar`** — A 64px white bar with a single `{colors.hairline-soft}` bottom border. Navigation links use 15px/600 weight Assistant with 0.3px letter-spacing. The active state underlines with a 2px `{colors.primary}` red border — the only color in the top chrome. The bar stays fixed on scroll for product browsing, collapsing to a hamburger on mobile.

### Forms
**`text-input`** — Standard 44px input with `{colors.hairline}` border and `{rounded.sm}` corners. Focus state swaps to a 2px `{colors.primary}` red border — the red appears only when the user engages, keeping the resting state clean. Used for search, newsletter signup, and checkout fields.

**`search-bar`** — A pill-shaped (`{rounded.full}`) input with `{colors.hairline}` border and `{colors.muted}` placeholder text. The full rounding contrasts with the rest of the system's `{rounded.sm}` corners, making the search action feel distinct and inviting. 44px height matches button sizing for visual alignment in the header.

### Badges
**`sale-badge`** — A sharp red rectangle (no rounding) with white uppercase text. The zero-radius corner is intentional — it reads as a price tag or inventory sticker rather than a UI pill. Placed at the top-left of product-card images, overlapping the edge.

### Footer
**`footer`** — A dark `{colors.ink}` band with white body text and `{colors.muted-soft}` links. Social icons use the same muted gray, with `{colors.social-blue}` and `{colors.social-navy}` reserved for the actual icon fills (these come from Font Awesome brand glyphs, not the brand's own palette). The footer stacks links in columns on desktop and collapses to a single column on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero section reduces padding to 32px; sale-badge font shrinks to 10px; search-bar moves into collapsible drawer |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses 28px display text; footer links in two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses 36px display text; footer links in four columns |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero text scales to 40px; increased whitespace around product cards |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height (exceeds Apple HIG 44pt recommendation)
- Product card tap targets include the full card area, not just the title/price text
- Nav links have 12px horizontal padding for comfortable finger targeting
- Quantity selector buttons are 40px × 40px minimum tap area
- Search-bar height is 44px for easy one-handed tapping

### Collapsing Strategy
- Top navigation collapses to a hamburger icon at < 744px, with a slide-out drawer for links
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport shrinks
- Footer link columns collapse from 4 → 2 → 1
- Hero section reduces vertical padding from 64px to 32px on mobile
- Search bar moves from inline in the header to a full-width collapsible drawer on mobile
- Sale badges remain visible but reduce font size to prevent overflow on small cards

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted font list includes "Font Awesome 6 Brands" and "Font Awesome 6 Free" — these are icon fonts, not body type. The primary brand font is assumed to be Assistant based on its presence in the extracted declarations, but the exact hierarchy (weights, sizes for all typography tokens) is inferred from common Shopify patterns rather than extracted CSS.
- Hover and focus states for most components (ghost buttons, text inputs, nav links) are inferred from common patterns, not extracted from the live site.
- Error state styling (form validation, out-of-stock messaging) is not present in the extracted data — `#cc0000` and `#ff4444` are used as error colors based on their presence in the palette, but exact usage is speculative.
- The extracted color list is heavily polluted with Shopify default colors (#008060 Shopify green, #0071e3 Apple-style blue, #334fb4 social navy) and stock-image dominant tones. The brand's true primary (#ff0000) is the most distinctive color in the list and is used as such, but secondary brand colors (if any exist beyond red, black, and white) could not be reliably isolated.
- Dark mode styling is not present in the extracted data — the brand likely does not support it.
- The `object-fit: contain` declaration in the extracted hints suggests product images use contain rather than cover, but this is a guess based on a single CSS property.
- No animation or transition timing data was extracted (hover fade durations, card lift effects, etc.).
- The brand's logo color and usage (whether it uses the red, or sits in black/white) could not be determined from the extracted data.
