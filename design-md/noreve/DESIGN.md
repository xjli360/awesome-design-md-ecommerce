---
version: alpha
name: "Noreve"
source_url: "https://www.noreve.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A leather-goods house that happens to sell phone cases, Noreve stakes its identity on a deep oxblood #81191f — a color that reads as saddle patina rather than corporate red, appearing on every primary CTA, add-to-cart button, and checkout trigger. The palette is otherwise restrained: a warm off-white canvas #fbfbfb, soft stone surfaces #f7f7f7, and a charcoal ink #555555 that keeps body text legible without the harshness of pure black. The extracted hex list reveals a brand that leans heavily on earthy neutrals (#d6d4d4, #ededed, #d0d0d0) punctuated by two accent voltages — a copper #e4752b for sale badges and a deep navy #428bca for informational links. Typography runs Roboto across the system, set at modest weights (400 for body, 500 for buttons, 600 for headings), with display sizes hovering around 20-24px rather than the oversized hero type common in fashion e-commerce. The brand trusts its material photography — close-ups of grain, stitching, and edge paint — over typographic drama. Cards use soft {rounded.sm} corners, buttons are pill-shaped at {rounded.full}, and the navigation bar sits at a compact 64px height, letting product imagery dominate the viewport. The overall effect is that of a small atelier: the oxblood anchor, the warm greys, and the copper accents create a palette that feels burnished rather than polished, as if the interface itself were made of the same leather as the products it sells.

colors:
  primary: "#81191f"
  primary-active: "#6a1419"
  primary-disabled: "#c48a8e"
  ink: "#555555"
  body: "#777777"
  muted: "#999999"
  muted-soft: "#b0b0b0"
  hairline: "#d4d4d4"
  hairline-soft: "#e6e6e6"
  canvas: "#fbfbfb"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-copper: "#e4752b"
  accent-copper-active: "#c8651f"
  accent-navy: "#428bca"
  accent-navy-active: "#357ebd"
  sale-badge: "#e4752b"
  sale-badge-text: "#ffffff"
  rating-star: "#fdaa02"
  error: "#d9534f"
  success: "#46a74e"
  scrim: "#090909"

typography:
  display-xl:
    fontFamily: "'Roboto', Verdana, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "'Roboto', Verdana, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  title-lg:
    fontFamily: "'Roboto', Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', Verdana, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  button-md:
    fontFamily: "'Roboto', Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Roboto', Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
  link:
    fontFamily: "'Roboto', Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto', Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Roboto', Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Roboto', Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0

rounded:
  none: 0px
  xs: 3px
  sm: 6px
  md: 10px
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
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  button-copper:
    backgroundColor: "{colors.accent-copper}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-copper-active:
    backgroundColor: "{colors.accent-copper-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.accent-navy}"
    typography: "{typography.link}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
    padding: "8px 0"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.price}"
    textColor: "{colors.accent-copper}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  rating-stars:
    color: "{colors.rating-star}"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature oxblood #81191f on a pill-shaped body. Text is white Roboto Medium at 14px with 0.5px letter-spacing. On hover, the background deepens to #6a1419. The disabled state fades to a muted rose #c48a8e, signaling unavailability without visual noise.

**`button-secondary`** — A white canvas button with a thin #d4d4d4 hairline border, used for "Add to Wishlist" and "Continue Shopping" actions. On active state, the border tightens to {colors.ink} and the background shifts to {colors.surface-soft}. Height and padding match the primary button for alignment in form layouts.

**`button-copper`** — Reserved for sale-related actions and limited-edition drops, this button uses the copper accent #e4752b. It follows the same pill shape and typography as the primary button but signals urgency or exclusivity. Active state darkens to #c8651f.

**`button-text-link`** — A plain text button styled as a link in navy #428bca, used for "View Details" and "Read More" actions within product cards. No background or border; relies on underline on hover for affordance.

### Cards
**`product-card`** — A white card with soft {rounded.sm} corners containing a product image, title, and price. The image area uses rounded top corners only, creating a subtle distinction between photography and text. The title sits in {typography.title-sm} at 14px weight 600, the price in {typography.price} at 16px weight 600. Sale prices render in {colors.accent-copper}. Cards stack in a responsive grid with {spacing.lg} gaps.

**`sale-badge`** — A small copper pill badge overlaid on product images, using {typography.badge} (11px uppercase weight 600). Padding is tight at 2px 8px with {rounded.xs} corners, ensuring it doesn't obscure the product photography.

### Navigation
**`top-nav`** — A compact 64px white bar with a bottom hairline border in {colors.hairline-soft}. Navigation links use Roboto Medium at 14px with 0.3px letter-spacing. The brand logo sits left-aligned, category links center, and utility icons (search, account, cart) right-aligned. On mobile, the nav collapses to a hamburger menu with a full-height overlay.

**`nav-dropdown`** — A white dropdown panel with {rounded.sm} corners, triggered by hover on top-nav category links. Items are padded at 8px 0 with the same typography as the parent nav. A subtle shadow separates the dropdown from the page content.

### Forms
**`text-input`** — A standard 44px input field with white background, {rounded.sm} corners, and a #d4d4d4 border. Focus state swaps the border to {colors.primary} (#81191f). Error state uses #d9534f. Typography is {typography.body-md} at 15px for readability.

**`search-bar`** — A pill-shaped search field at 40px height with a soft grey background {colors.surface-soft} and a lighter border {colors.hairline-soft}. Focus state uses the primary oxblood border. The search icon sits left-aligned inside the pill.

### Footer
**`footer-section`** — A dark footer using {colors.ink} (#555555) as background, with white text for headings and muted #b0b0b0 for links. Links lighten to full white on hover. The section uses {spacing.section} (64px) vertical padding, creating a substantial base for the page.

### Miscellaneous
**`quantity-selector`** — A compact 40px input with border, used on product detail pages for adjusting cart quantities. Matches the text-input styling but with a narrower width and centered text.

**`rating-stars`** — Five 16px star icons rendered in #fdaa02, used on product cards and detail pages. Empty stars render in {colors.hairline} for contrast.

**`divider`** — A 1px line in {colors.hairline} (#d4d4d4) used between sections. A softer variant in {colors.hairline-soft} (#e6e6e6) is used within cards and compact layouts.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked footer, full-width buttons |
| Tablet | 744–1128px | Two-column product grid, visible top-nav with condensed links, side-by-side footer columns |
| Desktop | 1128–1440px | Three-column product grid, full top-nav with dropdowns, multi-column footer |
| Wide | > 1440px | Max-width container at 1440px centered, expanded whitespace, four-column product grid |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons (search, cart, account) use 44x44px tap targets even if the visible icon is smaller
- Product card tap targets extend to the full card area, not just the title link
- Dropdown menus on tablet/desktop use 48px item heights for comfortable hover-to-click

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a full-screen overlay panel
- Product filters collapse to a "Filter" button that opens a slide-in panel on mobile
- Footer columns stack vertically on mobile, with accordion-style expandable sections for each column
- Product image galleries collapse from thumbnail strip to swipeable dots on mobile
- Multi-column layouts (product grids, feature lists) collapse to single column below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components could not be reliably extracted from the live site CSS; the active states documented above are inferred from common patterns in the extracted palette
- Error and success form states are based on the extracted hexes #d9534f and #46a74e, but their exact application (border color, background tint, iconography) is speculative
- The brand's typography scale is inferred from Roboto being the primary font-family; exact font sizes and weights for display, title, and body levels are estimates based on common e-commerce patterns
- Dark mode support was not detected on the live site; all colors assume a light theme
- Sub-brand or collection-specific palettes (e.g., limited-edition leather colors) are not captured
- The extracted hex list contains many generic web colors (blues, greens, oranges) that likely belong to third-party widgets (payment buttons, social icons, stock photography); the true brand palette is distilled to the most distinctive and recurring values
- Animation and transition durations/easings were not extractable from the live site
- Iconography style (filled vs. outlined, stroke weights) could not be determined from the extracted data
- The brand's logo color and treatment are not captured; the primary oxblood is used as the closest approximation for brand-color applications
