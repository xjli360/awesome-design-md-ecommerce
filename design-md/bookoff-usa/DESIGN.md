---
version: alpha
name: "BookOff USA"
source_url: "https://www.bookoffusa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep-blue #003388 storefront that reads more like a collector’s guild than a discount media bin — that single saturated navy carries the header, footer, and primary CTAs, giving the whole site a uniform, almost archival seriousness. The palette is surprisingly broad for a resale shop: alongside that anchor blue sit a warm amber #ff9900 (used for sale badges and price drops), a crisp lime #02e49b (likely a checkout-widget remnant but visually present), and a magenta #e94c89 that appears in promotional banners. The typography stack is a pragmatic sans-serif mix — Open Sans, Roboto, and system fonts — set at conventional weights with no display-size hero type; the brand lets product imagery and price tags do the talking. Cards use moderate rounding at {rounded.sm} to {rounded.md}, and the search bar sits as a full-width field rather than a pill, suggesting utility over exploration. The overall impression is of a no-nonsense marketplace where the blue #003388 acts as a consistent visual handshake across every page, while accent colors like #ff9900 and #dc3232 (a red for sold-out or clearance markers) provide the only moments of urgency. The site’s design language is functional first — generous whitespace around product grids, a sticky top bar with category dropdowns, and a footer dense with legal and policy links — but the consistent use of that deep blue across chrome elements gives it a cohesion that many secondary-market retailers lack.

colors:
  primary: "#003388"
  primary-active: "#002266"
  primary-disabled: "#8099cc"
  ink: "#1e1f26"
  body: "#444444"
  muted: "#949494"
  muted-soft: "#e8e8eb"
  hairline: "#eeeeee"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-amber: "#ff9900"
  accent-red: "#dc3232"
  accent-magenta: "#e94c89"
  accent-green: "#02e49b"
  badge-sale: "#ff9900"
  badge-soldout: "#dc3232"
  link-blue: "#0757fe"

typography:
  display-xl:
    fontFamily: "'Open Sans', Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Open Sans', Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Open Sans', Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "'Open Sans', Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  link:
    fontFamily: "'Open Sans', Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Open Sans', Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Open Sans', Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
    color: "{colors.accent-amber}"

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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  button-sale:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  top-nav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  top-nav-link-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px {spacing.base}"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    border: "2px solid {colors.primary}"
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 44px
    width: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.body-sm}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
  badge-sale:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-soldout:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    color: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.85
  footer-link-hover:
    opacity: 1
  category-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  category-dropdown-item:
    padding: "{spacing.sm} {spacing.base}"
    color: "{colors.ink}"
  category-dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.xl}"
  hero-banner-accent:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  pagination-disabled:
    color: "{colors.muted}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-link:
    color: "{colors.link-blue}"
  breadcrumb-current:
    color: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the deep blue #003388 and white text. Used for "Add to Cart", "Checkout", and primary form submissions. On hover, shifts to `{colors.primary-active}` (#002266). Disabled state uses a muted blue-grey `{colors.primary-disabled}` (#8099cc).

**`button-secondary`** — An outlined variant with the same blue as text and border on a white background. Used for secondary actions like "View Details" or "Continue Shopping". The 2px border maintains visual weight alongside the primary button.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions within cards or dropdowns. Hover state adds a subtle background tint (not extracted, see Known Gaps).

**`button-sale`** — A compact, high-energy button using the amber #ff9900 on dark text. Used exclusively for sale- or promotion-related CTAs. Smaller padding and font size allow it to sit inside product cards without overwhelming the layout.

### Navigation
**`top-nav`** — A 56px sticky bar filled with `{colors.primary}`. Contains the brand logo (left), category links (center), and utility icons (search, cart, account — right). All text is white. The bar remains fixed at the top during scroll.

**`top-nav-link`** — Navigation links in the top bar. On hover, the background shifts to `{colors.primary-active}` for a subtle darkening effect. Active page may use an underline or bolder weight (not confirmed from extraction).

**`category-dropdown`** — A white dropdown panel with a 1px hairline border. Items are 14px body text. Hovered items get a light grey `{colors.surface-soft}` background. Used for the main product category menu (Books, Movies, Music, Video Games, etc.).

### Cards
**`product-card`** — A white card with `{rounded.sm}` corners and 8px padding. Contains a square product image (1:1 aspect ratio), title, and price. The card has no border or shadow in the extracted styles — relies on the white surface against the soft grey `{colors.surface-soft}` background of the product grid area.

**`product-card-image`** — The product thumbnail inside the card, cropped to a square with `{rounded.xs}` (4px) corners. No border.

**`product-card-price`** — The standard price in bold 18px. When a sale is active, the price uses `{colors.accent-amber}` (#ff9900) instead of the default ink color.

### Badges
**`badge-sale`** — A small uppercase badge with amber background and dark text. Placed at the top-left corner of product card images to indicate discounted items. 2px vertical padding, 6px horizontal.

**`badge-soldout`** — Red background (#dc3232) with white text. Indicates items that are no longer available. Same dimensions as the sale badge.

**`badge-new`** — Green background (#02e49b) with dark text. Used for newly listed inventory. Same dimensions as other badges.

### Search
**`search-bar`** — A full-width text input with a 1px hairline border and `{rounded.sm}` corners. On focus, the border thickens to 2px and turns `{colors.primary}`. The input placeholder text uses `{colors.muted}` (#949494).

**`search-submit`** — A square 44x44 button filled with `{colors.primary}` and a white search icon. Sits to the right of the search input. On hover, shifts to `{colors.primary-active}`.

### Footer
**`footer`** — A deep blue section matching the top nav. Contains columns of links (About, Help, Policies, Social), contact information, and legal text. Links are white with 85% opacity, increasing to full opacity on hover. Padding is generous at 64px top/bottom and 32px sides.

**`footer-link`** — Footer navigation links in white with reduced opacity. Hover state returns to full opacity for a subtle glow effect.

### Hero & Promotional
**`hero-banner`** — A full-width section with `{colors.primary}` background and white text. Used for seasonal promotions, trade-in offers, or featured categories. May include an amber accent bar or button for the CTA.

**`hero-banner-accent`** — An amber (#ff9900) sub-section or accent element within the hero, used for highlighting sale percentages or limited-time offers.

### Pagination
**`pagination`** — Numbered page links at the bottom of search results and category listings. Inactive pages use blue text on transparent background. The active page uses `{colors.primary}` fill with white text. Disabled pages (e.g., "Previous" on page 1) use `{colors.muted}`.

### Breadcrumbs
**`breadcrumb`** — A secondary navigation row above product listings and detail pages. Current page is in `{colors.ink}` (#1e1f26), parent links use `{colors.link-blue}` (#0757fe), and separators (">") use `{colors.muted}`. Font is 12px caption size.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu; product grid goes single-column (1 card per row); search bar becomes full-width below nav; footer links stack vertically; hero banner text reduces to 18px; badges remain but may overlap on smaller images |
| Tablet | 744–1128px | Top nav shows abbreviated category labels (e.g., "Books" only, no subcategories); product grid shows 2-3 cards per row; search bar remains full-width; footer columns reduce to 2 columns |
| Desktop | 1128–1440px | Full top nav with all category links; product grid shows 4-5 cards per row; search bar is centered with max-width; footer shows 4 columns; hero banner at full height |
| Wide | > 1440px | Max-width container (1440px) centered; product grid may show 5-6 cards per row; extra whitespace on sides; top nav remains same layout |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target on mobile
- Product cards are tappable as a whole unit (not just the title link)
- Category dropdown items have 44px minimum height on touch devices
- Pagination buttons are 44x44px minimum on mobile

### Collapsing Strategy
- Top nav collapses to a hamburger icon on mobile (< 744px), revealing a full-screen overlay menu
- Category dropdowns become accordion-style sections in the mobile nav
- Footer columns stack vertically on mobile, with each section becoming a collapsible accordion
- Product filters (if present) collapse into a slide-out drawer or bottom sheet on mobile
- Hero banner reduces height and may hide secondary text on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components (buttons, links, cards) could not be reliably extracted from the static CSS — `primary-active` (#002266) is an assumption based on darkening the primary color by 15%, not a confirmed value
- Error states for form inputs (validation colors, error messages) are not present in the extracted data
- Focus ring styles (outline color, width, offset) are not available
- Active/selected states for navigation items (underline, bold, or background change) are not confirmed
- The extracted color list includes many checkout-widget colors (Klarna pink #f00075, Afterpay green #02e49b, PayPal blue #0866ff, etc.) that are not part of the BookOff brand — these have been excluded from the palette where possible, but `accent-green` (#02e49b) and `accent-magenta` (#e94c89) may still be widget remnants rather than intentional brand colors
- Dark mode or high-contrast mode styles are not present
- Animation and transition timing values (durations, easing functions) are not available
- Shadow values (box-shadow for cards, dropdowns, modals) could not be extracted
- The font stack includes many fallbacks but the primary brand font is assumed to be Open Sans based on its position in the stack — this is not confirmed from any explicit brand guideline
- Loading states (skeleton screens, spinners) are not documented
- Modal/dialog overlay styles (scrim color, opacity) are not available
- The extracted "meta theme-color" was `(none)`, meaning no browser chrome color is set — this may be intentional or an oversight
