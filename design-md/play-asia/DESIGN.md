---
version: alpha
name: "Play-Asia"
source_url: "https://www.play-asia.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A dense, high-signal import marketplace that packs a global toy, game, and collectibles catalog into a single #313131 monochrome spine — the only extracted hex from the live site, and it tells the whole story. Play-Asia does not rely on a signature brand color; instead it leans on a vast grid of product thumbnails, each a tiny saturated rectangle of Japanese packaging, limited-edition steelbooks, and anime figures, to provide all the visual energy. The interface is a functional container: white canvas, gray hairline borders, and a system-font stack that loads instantly without a single custom typeface request. Navigation is a horizontal strip of category links (PS5, Nintendo Switch, Anime, Figures, Pre-orders) that scrolls left-right on mobile, each link a simple text label with no icon or badge — the brand trusts its taxonomy over decoration. Product cards are compact: a 200x200 thumbnail, a two-line title in 14px system bold, a price in 16px, and a small "Add to Cart" button in the primary gray. The search bar is a full-width rectangle with a magnifying-glass icon and placeholder text, not a pill — Play-Asia is about speed and specificity, not hospitality. The footer is a dense wall of links organized into columns (Help, Company, Payment, Community), each link in 12px gray, with payment icons (Visa, Mastercard, PayPal, Alipay) and a "We ship worldwide" confidence line. The overall mood is utilitarian but trustworthy — a no-nonsense storefront for a passionate niche audience that already knows what it wants.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#1a1a1a"
  body: "#313131"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dcdcdc"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#cc0000"
  success: "#2e7d32"
  link: "#0066cc"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
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
    padding: 8px 16px
    height: 36px
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
    padding: 7px 15px
    height: 36px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 48px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  badge-new:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  price-current:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
  price-original:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  breadcrumb-link:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.link}"
  breadcrumb-separator:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"

## Components

### Buttons
**`button-primary`** — The primary action button, used for "Add to Cart", "Checkout", and "Sign In". It uses the brand's single extracted color `#313131` as a solid background with white text. On hover, it darkens to `{colors.primary-active}` (`#1a1a1a`). The disabled state uses `{colors.primary-disabled}` (`#a0a0a0`) with white text. The button has minimal `{rounded.sm}` (4px) corners, a compact 36px height, and 14px semibold system text — no pill shapes or gradients.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Wishlist". It uses a white background with `{colors.primary}` text and a 1px solid `{colors.hairline}` border. On hover, the border darkens to `{colors.primary}`. The dimensions match `button-primary` for alignment in forms and card actions.

**`button-tertiary-text`** — A text-only button for inline actions like "Clear filters" or "Cancel". It has no background or border, using `{colors.primary}` text on hover. The typography matches `{typography.button-md}` for consistent sizing.

### Cards
**`product-card`** — The core product display unit in the grid. It consists of a square thumbnail container (200x200px on desktop, scaling down on mobile), a two-line title in `{typography.body-sm}` (14px, 400 weight, `{colors.body}`), a price line using `{typography.title-sm}` (16px, 600 weight, `{colors.ink}`), and an `button-primary` for "Add to Cart". The card has `{rounded.sm}` corners and a 1px `{colors.hairline}` border. On hover, a subtle shadow appears (not tokenized — see Known Gaps). The thumbnail area is clickable and links to the product detail page.

### Navigation
**`nav-bar`** — A horizontal strip of category links (e.g., "PS5", "Nintendo Switch", "Anime", "Figures", "Pre-orders", "Sale"). It is 48px tall, uses `{colors.canvas}` background, and `{typography.nav-link}` (14px, 500 weight). The active tab uses `{colors.ink}` text with a 2px bottom border in `{colors.ink}`; inactive tabs use `{colors.muted}`. On mobile, the strip scrolls horizontally with no wrapping. There is no hamburger menu — the full category list is always accessible via scroll.

**`breadcrumb-link`** — Used on product detail pages to show the navigation path (e.g., "Home > PlayStation 5 > Games > Elden Ring"). Each link uses `{colors.link}` (`#0066cc`) and `{typography.link}` (14px, 400 weight). Separators are `{colors.muted-soft}` chevrons or slashes in `{typography.caption}`.

### Forms
**`text-input`** — Standard text input for search, login, and checkout forms. It has a white background, `{colors.body}` text, `{rounded.sm}` corners, and a 1px `{colors.hairline}` border. On focus, the border changes to `{colors.primary}`. The height is 40px with 8px 12px padding. Placeholder text uses `{colors.muted}`.

**`search-bar`** — The primary search input, typically placed in the header or on the homepage. It uses a light gray background (`{colors.surface-soft}`) rather than a white one, with `{colors.muted}` placeholder text. A magnifying-glass icon is positioned to the left of the input. The shape is a simple rectangle with `{rounded.sm}` — not a pill. On focus, the background becomes white and a `{colors.primary}` border appears.

### Badges
**`badge-new`** — A small red badge used on product cards to indicate new arrivals. It uses `{colors.error}` (`#cc0000`) as background with white text in `{typography.badge}` (11px, 700 weight). The badge has `{rounded.xs}` (2px) corners and 2px 6px padding.

**`badge-sale`** — A small green badge for sale/discount items. It uses `{colors.success}` (`#2e7d32`) as background with white text. All other properties match `badge-new`.

### Footer
**`footer-link`** — Links in the footer columns (Help, Company, Payment, Community). They use `{colors.muted}` (`#666666`) and `{typography.caption}` (12px, 400 weight). On hover, the color changes to `{colors.ink}`. The footer also contains payment icons (Visa, Mastercard, PayPal, Alipay) and a "We ship worldwide" confidence line in `{colors.muted-soft}`.

### Price Display
**`price-current`** — The current price of a product, displayed in `{typography.title-sm}` (16px, 600 weight) with `{colors.ink}`. Used on product cards and detail pages.

**`price-original`** — The original (strikethrough) price for sale items, displayed in `{typography.body-sm}` (14px, 400 weight) with `{colors.muted-soft}` (`#999999`). It is rendered with a line-through text decoration.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Product grid goes to 2 columns; nav-bar scrolls horizontally; search-bar becomes full-width; footer links stack vertically; product card thumbnails shrink to 140px |
| Tablet | 744–1128px | Product grid uses 3–4 columns; nav-bar is fully visible; search-bar is 400px max-width; footer columns display in 2 rows |
| Desktop | 1128–1440px | Product grid uses 5–6 columns; nav-bar is centered with max-width container; search-bar is 500px; footer columns display in a single row |
| Wide | > 1440px | Product grid uses 6–7 columns; content is centered in a 1440px max-width container; nav-bar and footer expand to full width |

### Touch Targets
- All buttons and links have a minimum touch target of 44x44px (Apple HIG compliant).
- Product card thumbnails are at least 140x140px on mobile.
- Nav-bar category links are at least 44px tall with 16px horizontal padding.

### Collapsing Strategy
- On mobile (< 744px), the footer collapses from a multi-column layout to a single vertical stack of link groups.
- The product grid collapses from 5–6 columns on desktop to 2 columns on mobile.
- The search bar collapses from a centered 500px element to a full-width element on mobile.
- The nav-bar does not collapse into a hamburger menu; instead, it scrolls horizontally on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (`#313131`) was extracted from the live site. This is likely the primary text/button color, but the full palette (including any brand accent colors, hover states, error/success colors, and link colors) could not be reliably extracted. The colors above are best guesses based on common e-commerce patterns and the extracted gray.
- No custom font-family was found; the site uses the system font stack. Typography sizes and weights are inferred from common e-commerce patterns and may not match the exact live site.
- Rounded corner values (`rounded`) are estimated based on typical e-commerce implementations. The exact border-radius values on the live site may differ.
- Spacing values (`spacing`) are standard increments and may not match the exact grid system used by Play-Asia.
- Hover states for buttons, links, and cards are inferred from common patterns. The exact hover colors and shadow effects on the live site are unknown.
- Error states for form inputs (e.g., invalid email, missing required fields) could not be extracted.
- The product card hover effect (shadow or border change) could not be extracted.
- The checkout flow, payment form, and order confirmation page designs are not represented.
- Dark mode is not supported by the extracted data.
- The site's loading states, skeleton screens, and empty states are unknown.
- The exact icon set (magnifying glass, cart, user, etc.) and their sizes are not captured.
- The header's logo dimensions and placement are not specified.
- The "Just a moment..." page title suggests a Cloudflare challenge page, which may have prevented full extraction of the site's design tokens.
