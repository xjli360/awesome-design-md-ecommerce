---
version: alpha
name: "Yacht Club Games Store"
source_url: "https://yachtclubgames.com/store"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A pixel-perfect merch storefront that channels the NES-era warmth of Shovel Knight through a burnt-orange (#da532c) and sky-blue (#5bbad5) palette that reads more like a retro cartridge label than a modern e-commerce site. The primary #da532c is the voltage of every "Add to Cart" button, the top-nav underline, and the hover state on product thumbnails — it's the same orange that glows on the Shovel Knight logo, pulled straight from the pixel art's fire palette. The canvas is a soft #f5f5f5, not pure white, giving the store a worn-in feel like a well-loved game manual, while #d3d3d3 hairline borders keep product cards and dividers from feeling too sharp. The accent #ff4500 (a deeper, more aggressive orange-red) appears on sale badges and limited-edition callouts, creating a secondary voltage that signals urgency without clashing. The store's typography leans on system fonts (no custom web font found), which is a deliberate choice — it keeps the page loading fast and the vibe utilitarian, like a 90s game catalog printed on a dot-matrix. Product cards use `{rounded.sm}` corners, just enough to soften the pixel grid without betraying the 8-bit ethos, while the main CTA buttons go `{rounded.md}` for a slightly friendlier tap target. The nav bar is a simple horizontal strip with the logo left-aligned and cart right-aligned, no hamburger until mobile — a no-nonsense layout that prioritizes browsability. The overall mood is nostalgic but not kitschy: the orange and blue are complementary without being loud, the gray canvas keeps the focus on the product photography (plush toys, vinyl soundtracks, enamel pins), and the absence of heavy shadows or gradients keeps everything flat and honest, like a sprite on a CRT.

colors:
  primary: "#da532c"
  primary-active: "#c44a26"
  primary-disabled: "#f0b09a"
  ink: "#222222"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d3d3d3"
  hairline-soft: "#e0e0e0"
  canvas: "#f5f5f5"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#ff4500"
  accent-blue: "#5bbad5"
  accent-blue-hover: "#4aa8c4"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  button-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.md}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    padding: "0 {spacing.base} {spacing.base}"
  badge-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.lg} 0 {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart" and "Checkout" flows. Rendered in `{colors.primary}` (#da532c) with white text and `{rounded.md}` corners. On hover, shifts to `{colors.primary-active}` (#c44a26) for a subtle darkening. Disabled state uses `{colors.primary-disabled}` (#f0b09a) to indicate non-interactivity while maintaining brand color presence.

**`button-secondary`** — An outlined or ghost alternative for secondary actions like "View Details" or "Continue Shopping". Uses a white background with `{colors.ink}` text and a `{colors.hairline}` border. Hover fills the background with `{colors.surface-soft}` (#eeeeee) for a light press effect.

**`button-sale`** — A compact, high-urgency button for limited-time offers or clearance items. Uses the deeper `{colors.accent-sale}` (#ff4500) background with white text and tighter padding. Typically paired with a `badge-sale` component on product cards.

### Navigation
**`nav-bar`** — A fixed or sticky top bar at 64px height with a `{colors.canvas}` background. Contains the Yacht Club Games logo on the left, a horizontal list of nav links (Store, Games, About, etc.) in the center, and a cart icon on the right. Active nav links are underlined with a 2px `{colors.primary}` border.

**`nav-link-active`** — The currently selected navigation item. Uses `{colors.primary}` text color and a bottom border in the same orange to create a clear active indicator without a background pill.

**`nav-link-inactive`** — Default navigation items in `{colors.muted}` (#666666). On hover, they shift to `{colors.ink}` for better readability.

### Cards
**`product-card`** — A clean, white card (`{colors.surface-card}`) with `{rounded.sm}` corners and no border — the card sits on the `{colors.canvas}` background, relying on the contrast between #ffffff and #f5f5f5 for separation. The product image fills the top with `{rounded.sm}` top corners, followed by the title and price stacked below. On hover, a subtle `boxShadow` lifts the card slightly.

**`product-card-title`** — The product name set in `{typography.title-sm}` (16px, 600 weight) with `{spacing.sm}` padding above and `{spacing.base}` on the sides.

**`product-card-price`** — The price displayed in `{typography.body-sm}` with `{colors.muted}` color, positioned below the title with side padding.

### Badges
**`badge-sale`** — A small, uppercase badge for sale items. Uses `{colors.accent-sale}` (#ff4500) background with white text, `{rounded.xs}` corners, and tight 2px/6px padding. Positioned at the top-left corner of product card images.

**`badge-new`** — A similar badge for new arrivals or pre-orders. Uses `{colors.accent-blue}` (#5bbad5) background to differentiate from sale badges while maintaining the same structural pattern.

### Forms
**`text-input`** — Standard text input for search, newsletter signup, or checkout fields. White background, `{colors.body}` text, `{rounded.sm}` corners, and a `{colors.hairline}` border. Focus state would add a `{colors.primary}` border (not extracted, noted in gaps).

### Footer
**`footer`** — A dark footer with `{colors.ink}` background and white text. Contains links to support, privacy policy, and social media. Footer links start in `{colors.muted-soft}` and brighten to `{colors.canvas}` on hover.

### Dividers
**`divider`** — A 1px horizontal line in `{colors.hairline}` (#d3d3d3) used to separate sections or product rows.

### Section Headings
**`section-heading`** — Used for category titles like "New Arrivals" or "Best Sellers". Set in `{typography.display-md}` (24px, 700 weight) with generous top padding and bottom spacing.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product cards stack in single column; `button-primary` becomes full-width; search bar moves below nav; footer links stack vertically |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards in 2-column grid; search bar remains in nav; footer links in 2 columns |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; search bar prominently positioned; footer links in 4 columns |
| Wide | > 1440px | Max-width container (1200px) centers content; product cards may expand to 4 columns; whitespace increases around sections |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav links have 48px tap area (padding + height)
- Product cards are fully tappable, with the entire card linking to the product page
- Cart icon button is 48px × 48px minimum
- Search bar has 40px height with comfortable padding

### Collapsing Strategy
- On mobile (< 744px), the nav bar collapses to a hamburger menu icon on the left, with the logo centered and cart icon on the right
- Product grid collapses from 3 columns to 2 (tablet) to 1 (mobile)
- Footer links collapse from 4 columns to 2 (tablet) to stacked (mobile)
- Search bar moves from inline in the nav to a full-width element below the nav on mobile
- Section headings reduce from 24px to 20px on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom web font declarations were found on the live site; the store uses system font stack. If a custom font (e.g., a pixel or retro typeface) is used in the actual brand, it was not extracted and should be added.
- Hover, focus, and active states for text inputs and links were not reliably extracted — focus ring color and style are assumed to follow `{colors.primary}` but are unconfirmed.
- Error and validation styling for forms (e.g., red borders, error messages) was not observed.
- The extracted hex list included only 5 colors, which may be incomplete. The brand's true palette may include additional colors (e.g., a darker blue for headers, a yellow for accents) that were not present in the extracted data.
- The `meta theme-color` was not set, so the browser chrome/tab color is undefined.
- Dark mode is not supported — no `prefers-color-scheme` media queries or dark palette tokens were found.
- The store does not appear to be Shopify-based (platform-shopify: False), so checkout flow components (payment buttons, cart drawer) may use a different system entirely.
- Typography line-heights and letter-spacing values are estimated based on standard system font behavior; exact values may vary slightly on different operating systems.
- The `button-secondary` border color is assumed to be `{colors.hairline}` but was not explicitly extracted.
- Product card shadow on hover is inferred from common patterns; exact shadow values were not extracted.
