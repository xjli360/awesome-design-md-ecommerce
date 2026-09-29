---
version: alpha
name: "Goumi Kids"
source_url: "https://goumikids.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A baby-clothing brand that turns the nursery-warmth of #eae0d2 into a full digital ecosystem — the color reads like unbleached muslin, like the inside of a well-loved swaddle, and it appears everywhere from the site background to product-card fills to the footer canvas. Against this soft, sandy base, #c4936f (a warm caramel) and #d43747 (a restrained berry-red) provide the only real color voltage: the red appears on sale badges, add-to-cart buttons, and the tiny hearts that mark wishlist items, while the caramel surfaces in secondary CTAs, size-selector borders, and the horizontal rules that separate product details. Montserrat runs across the entire site at moderate weights — display headlines sit at 500/600 rather than heavy 700+, trusting the generous spacing and the product photography (babies in convertible gowns, mitts that actually stay on) to carry emotional weight rather than typographic muscle. The navigation is unusually sparse for a Shopify store: a single row with logo-left, a compact cart icon, and a hamburger that reveals a full-width overlay menu — no mega-nav, no category dropdowns. Product cards use soft, even radii ({rounded.md}) and the add-to-cart button is a full-width pill ({rounded.full}) in the berry-red, creating a single clear action per product page. The checkout flow inherits Shopify's default button styling, but the brand's own interface maintains a consistent warmth through the #eae6df surface and #dac8af hairline — the whole site feels like a nursery that happens to sell things, not a store that happens to be soft.

colors:
  primary: "#d43747"
  primary-active: "#b32e3c"
  primary-disabled: "#f3cbcb"
  ink: "#151414"
  body: "#484747"
  muted: "#7b7a7a"
  muted-soft: "#9a9a9a"
  hairline: "#dac8af"
  hairline-soft: "#e6e6e6"
  canvas: "#eae0d2"
  surface-soft: "#eae6df"
  surface-card: "#f7f7f7"
  on-primary: "#ffffff"
  accent-caramel: "#c4936f"
  accent-green: "#56ad6a"
  accent-green-soft: "#ecfef0"
  accent-gold: "#ecbd5e"
  badge-red: "#d02e2e"
  star-rating: "#c4936f"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.25px
  price:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  price-sale:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
    color: "{colors.primary}"

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
    rounded: "{rounded.full}"
    padding: 14px 32px
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.accent-caramel}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: 1px solid "{colors.accent-caramel}"
  button-secondary-active:
    backgroundColor: "{colors.accent-caramel}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  button-pill-caramel:
    backgroundColor: "{colors.accent-caramel}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    border: 1px solid "{colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  hamburger-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
  search-bar-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 44px
    border: 1px solid "{colors.accent-caramel}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
    textColor: "{colors.primary}"
  product-card-wishlist:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 36px
  product-card-badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-sold-out:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: 1px solid "{colors.hairline}"
  size-selector-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: 2px solid "{colors.accent-caramel}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 44px
  footer-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.accent-caramel}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.accent-caramel}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 0 0 16px 0
  review-stars:
    color: "{colors.star-rating}"
    fontSize: 16px
  review-stars-empty:
    color: "{colors.muted-soft}"
    fontSize: 16px
  breadcrumb-link:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"
  breadcrumb-current:
    typography: "{typography.caption-sm}"
    textColor: "{colors.ink}"
  loading-spinner:
    color: "{colors.accent-caramel}"
    size: 24px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a full-width pill in the brand's berry-red (#d43747). Used for "Add to Cart", "Checkout", and primary form submissions. On hover, shifts to `primary-active` (#b32e3c). Disabled state uses `primary-disabled` (#f3cbcb) with white text — low contrast by design, signaling non-interactivity. Text is uppercase Montserrat 600 at 14px with 0.5px letter-spacing.

**`button-secondary`** — An outlined pill in caramel (#c4936f) on a white card background. Used for "Size Guide", "View Details", and secondary product actions. Active state fills with caramel and flips text to white. Border is 1px solid caramel; padding is 13px 31px to account for the border offset.

**`button-tertiary-text`** — A text-only button with no background or border. Used for "Cancel", "Clear Filters", and dismissible actions. Inherits ink color and button-md typography. Hover state adds underline.

**`button-pill-primary`** — A compact pill variant of the primary button, used in cart summaries, promo-code fields, and mobile sticky CTAs. Same berry-red fill but smaller padding (10px 20px) and button-sm typography (12px uppercase).

**`button-pill-caramel`** — A compact pill in the caramel accent, used for "Subscribe" in the newsletter form and for "Apply" on promo codes. Same dimensions as `button-pill-primary` but with caramel fill.

### Cards
**`product-card`** — A white card (`surface-card`, #f7f7f7) with 12px rounded corners (`rounded.md`). Contains the product image (also rounded at 12px), title in body-sm, price in price typography (18px/600), and a wishlist heart icon in the top-right corner colored berry-red. Sale items show the sale price in `price-sale` (same weight, red color) with a `badge-red` badge (#d02e2e) reading "SALE" in 11px uppercase. Sold-out items get a gray badge. Cards sit on the `canvas` background (#eae0d2) with generous spacing between them (24px gap on desktop).

### Navigation
**`top-nav`** — A single-row bar at 64px height on the `canvas` background. Logo sits left-aligned; a compact cart icon with item count badge sits right-aligned. On mobile, a hamburger icon replaces any nav links. The hamburger opens a full-screen overlay menu with nav links in 14px/500 Montserrat, a search bar, and secondary links (Account, Orders, Help). No mega-nav or dropdowns — the brand keeps navigation intentionally minimal.

**`hamburger-menu`** — The mobile navigation trigger, rendered as three stacked lines in ink color on the canvas background. Opens a full-width overlay with a close button (X icon) in the top-right. The overlay menu lists primary categories, a search bar, and utility links. Background is `canvas` with no scrim — the overlay feels like a drawer, not a modal.

### Forms
**`text-input`** — A standard input field with 12px rounded corners, 1px `hairline` border (#dac8af), and 12px horizontal padding. Height is 44px. On focus, the border switches to 2px `accent-caramel` (#c4936f). Placeholder text uses `muted` (#7b7a7a). Error state uses a 1px `primary` border with error message in `primary` text.

**`size-selector`** — A chip-style selector for baby clothing sizes (NB, 0-3M, 3-6M, etc.). Each chip is 40px tall with 8px horizontal padding, 8px rounded corners, and a 1px `hairline` border. Active chip gets a 2px `accent-caramel` border. Chips are arranged in a horizontal row with 8px gaps.

**`quantity-selector`** — A compact stepper with minus/plus buttons flanking the current quantity. Background is `surface-soft` (#eae6df), 44px tall, with 12px rounded corners. Buttons are icon-only with no border; the quantity display is centered in body-md weight.

**`newsletter-input`** — A full-width pill input at 48px height with 12px horizontal padding, 1px `hairline` border, and `rounded.full`. The adjacent submit button is a `button-pill-caramel` at the same height, creating a seamless combined control.

### Footer
**`footer-section`** — A multi-column footer on the `canvas` background. Each column has a `footer-heading` (title-sm, 16px/500, ink) and a list of `footer-link` items (14px/400, muted). Links hover to `accent-caramel`. The bottom bar contains copyright text in caption-sm and payment icons. A newsletter signup form sits in the first column with `newsletter-input` and `newsletter-submit` components.

### Badges
**`product-card-badge`** — A small rectangular badge (4px rounded) in `badge-red` (#d02e2e) with white text in 11px/700 uppercase. Used for "SALE", "NEW", and "BESTSELLER" labels. Positioned absolutely in the top-left corner of product images. Padding is 2px 8px.

**`product-card-badge-sold-out`** — Same dimensions but with `muted-soft` (#9a9a9a) background. Used for "SOLD OUT" labels.

### Dividers
**`divider`** — A full-width 1px line in `hairline` (#dac8af). Used between product details sections and in the footer.

**`divider-soft`** — A full-width 1px line in `hairline-soft` (#e6e6e6). Used between accordion items and in the cart summary for lighter visual separation.

### Accordion
**`accordion-header`** — A clickable row in `canvas` background with `title-sm` typography (16px/500) and 16px vertical padding. Includes a chevron icon that rotates on open. No border — the divider between items is `divider-soft`.

**`accordion-content`** — The expandable panel below each header, with `body-sm` typography (14px/400) and 16px bottom padding. Used for product descriptions, care instructions, and shipping details.

### Review Stars
**`review-stars`** — Five star icons rendered in `star-rating` color (#c4936f, matching the caramel accent). Each star is 16px. Empty stars use `muted-soft` (#9a9a9a). The numeric rating (e.g., "4.5") sits beside the stars in caption typography.

### Breadcrumbs
**`breadcrumb-link`** — A 12px/400 link in `muted` color, separated by a "/" character in the same style. The current page (`breadcrumb-current`) uses `ink` color. Used on product detail pages and collection pages.

### Loading
**`loading-spinner`** — A 24px spinning circle in `accent-caramel` (#c4936f). Used for async operations (adding to cart, loading more products). On dark backgrounds, the spinner inverts to white.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top-nav collapses to logo + hamburger + cart. Product cards go single-column with full-width images. Size-selector chips stack to two rows. Footer collapses to single column. Accordion becomes the primary layout for product details. Search bar moves to overlay menu. |
| Tablet | 744–1128px | Top-nav shows logo + cart + hamburger (no inline links). Product cards in 2-column grid. Footer shows 2 columns. Size-selector chips remain in a single row. |
| Desktop | 1128–1440px | Full top-nav with logo + cart + hamburger (still no inline links — the brand keeps it minimal). Product cards in 3-column grid. Footer shows 3-4 columns. Search bar visible in the top section. |
| Wide | > 1440px | Max-width container at 1440px centered. Product cards in 4-column grid. Footer shows 4 columns with additional whitespace. |

### Touch Targets
- All interactive elements (buttons, links, chips) maintain a minimum 44px height per WCAG 2.1 touch-target guidelines.
- Wishlist hearts are 36px with 4px padding — slightly below guideline but acceptable for a secondary action.
- Quantity stepper buttons are 44px × 44px hit areas.
- Accordion headers are 48px minimum height (16px padding top and bottom + 16px line height).
- Hamburger icon is 44px × 44px.

### Collapsing Strategy
- Top-nav links collapse into the hamburger overlay at all breakpoints — the brand never shows inline nav links.
- Product description, care instructions, and shipping details collapse into accordion panels on mobile and tablet; on desktop they remain visible as stacked sections.
- Footer columns collapse from 4 to 2 to 1 as viewport shrinks.
- Size-selector chips collapse from a single row to two rows on mobile.
- Product image galleries collapse from thumbnail strip to dot indicators on mobile.
- Cart summary collapses from side-by-side (items + totals) to stacked on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list is long (27 colors) but heavily weighted toward grays and neutrals — the brand's true primary (#d43747, berry-red) and secondary (#c4936f, caramel) were identified as the most distinctive non-gray colors. The remaining grays (#e6e6e6, #b3b3b3, #dedede, #cdcdcd, #9a9a9a, #808080, #d3d3d3, #f2f2f2, #1a1a1a, #121212) were mapped to utility tokens (hairline-soft, muted-soft, etc.) but their exact roles on the live site couldn't be verified.
- Hover states for buttons and links were inferred from common patterns — the extracted data didn't include :hover CSS.
- Error states for form inputs (border color, error message styling) were not extractable from the live site HTML.
- The font-family declaration found was "Montserrat" — no fallback stack was visible. The stack shown in typography is a reasonable guess based on common Shopify practices.
- Dark mode was not detected on the live site.
- Sub-brand or seasonal color palettes (if any) could not be extracted.
- The checkout flow uses Shopify's default styling, which may differ from the brand's design system — the extracted colors may include Shopify Pay, Klarna, and Afterpay widget colors that aren't part of the brand's own palette.
- Social media icon colors (Facebook blue, Instagram pink, Pinterest red) may be present in the extracted list but were not distinguishable from brand colors.
- Stock photography dominant tones (e.g., skin tones, fabric colors) may have influenced the extracted hex list — the warm neutrals (#eae0d2, #eae6df, #dac8af) could be partially driven by product photos rather than intentional design tokens.
- Animation durations, easing curves, and transition properties were not extractable.
- The exact font weights used for headings vs. body text were inferred from common Montserrat usage patterns — the live site may use different weights.
