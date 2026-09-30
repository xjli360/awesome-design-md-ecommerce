---
version: alpha
name: "RevHQ"
source_url: "https://www.revhq.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A black-and-gray concrete bunker for punk, hardcore, and underground culture, where #ff5268 — a hot pink that reads like a scream on a flyer — is the only color allowed to bleed through the monochrome. The site runs on a single monospace typeface, giving every product title, price, and nav link the same deadpan authority as a photocopied zine or a hand-stamped 7-inch sleeve. The canvas is white (#ffffff), the ink is near-black (#191919), and the entire visual system is held together by a hierarchy of grays — #888888 for muted body text, #dedede for hairline borders, #e5e3df for soft dividers, #f4f4f4 for surface cards. There are no rounded corners anywhere except the pink CTA button, which uses a tight {rounded.sm} to feel like a stamp rather than a pill. The top nav is a dense horizontal strip of genre categories (Vinyl, T‑Shirts, Books, Patches, etc.) in all-caps monospace, no dropdowns, no icons — just text and a search bar. Product cards are flat white rectangles with a single border (#dedede), a square image, and a three-line caption: artist, format, price. The hot pink (#ff5268) appears only on the primary CTA ("Add to Cart"), the cart badge, and the sale badge — a deliberate scarcity that makes the color feel like a stage dive in an otherwise gray room.

colors:
  primary: "#ff5268"
  primary-active: "#e04054"
  primary-disabled: "#f5a0ac"
  ink: "#191919"
  body: "#444444"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#e5e3df"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-badge: "#ff5268"
  sold-out-badge: "#888888"
  social-facebook: "#3b5998"
  social-twitter: "#1da1f2"
  social-pinterest: "#bd081d"
  social-instagram: "#222222"

typography:
  display-xl:
    fontFamily: "'Courier New', 'Consolas', 'Liberation Mono', monospace"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Courier New', 'Consolas', 'Liberation Mono', monospace"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Courier New', 'Consolas', 'Liberation Mono', monospace"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Courier New', 'Consolas', 'Liberation Mono', monospace"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Courier New', 'Consolas', 'Liberation Mono', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Courier New', 'Consolas', 'Liberation Mono', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Courier New', 'Consolas', 'Liberation Mono', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Courier New', 'Consolas', 'Liberation Mono', monospace"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Courier New', 'Consolas', 'Liberation Mono', monospace"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Courier New', 'Consolas', 'Liberation Mono', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Courier New', 'Consolas', 'Liberation Mono', monospace"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Courier New', 'Consolas', 'Liberation Mono', monospace"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    padding: 10px 20px
    height: 40px
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
    padding: 9px 19px
    height: 40px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 40px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 6px 12px
    height: 32px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: 1px solid "{colors.hairline}"
  product-card-image:
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-artist:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  sold-out-badge:
    backgroundColor: "{colors.sold-out-badge}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: 24px 16px
  footer-link:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.canvas}"

## Components

### Buttons
**`button-primary`** — The single hot-pink CTA across the site. Used for "Add to Cart", "Checkout", and primary form submissions. Uses a tight {rounded.sm} (4px) that reads as a stamp, not a pill. On hover, darkens to {colors.primary-active}. Disabled state fades to {colors.primary-disabled} with white text. Text is uppercase monospace at 13px, weight 700.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Continue Shopping". White background with {colors.ink} text and a 1px solid {colors.hairline} border. Same dimensions and typography as primary. Hover state adds a 1px solid {colors.ink} border.

**`button-tertiary-text`** — A text-only button for actions like "Clear Filters" or "Cancel". No background, no border. Uses {typography.button-md} in {colors.ink}. Hover state underlines.

### Product Cards
**`product-card`** — A flat white rectangle with a 1px {colors.hairline} border and no border-radius. Contains a square product image (no rounding), followed by three lines of text: artist name ({typography.title-sm} in {colors.ink}), format/description ({typography.body-sm} in {colors.muted}), and price ({typography.body-md} in {colors.ink}). The entire card is clickable. On hover, the border shifts to {colors.ink} for a subtle lift.

**`sale-badge`** — A small, unrounded rectangle in {colors.primary} with white uppercase text. Positioned at the top-left of the product image. Reads "SALE" or a percentage off. No padding beyond 2px 6px — intentionally tight and cheap-looking, like a price tag from a record store.

**`sold-out-badge`** — Same shape and position as the sale badge, but in {colors.sold-out-badge} (muted gray) with white text. Reads "SOLD OUT" or "GONE".

### Navigation
**`nav-bar`** — A 48px-tall horizontal strip at the top of the page. White background with no border or shadow. Contains genre links (Vinyl, T‑Shirts, Books, Patches, etc.) in uppercase monospace at 11px, weight 700, with {colors.muted} as the default color. The active/current category uses {colors.ink}. Links are separated by a single pipe character (|) or a thin {colors.hairline} vertical rule. No dropdowns, no icons, no search bar in the nav — search is a separate element below.

**`nav-link`** — A text-only link in the top nav. No background, no padding. Default color is {colors.muted}. Active state is {colors.ink}. No underline or decoration — the color change is the only signal.

### Forms
**`text-input`** — A simple, unrounded input field with a 1px {colors.hairline} border and white background. Used for search, email signup, and checkout fields. On focus, the border shifts to {colors.ink}. No placeholder styling beyond {colors.muted} text. Height is 40px with 8px 12px padding.

### Footer
**`footer`** — A dark band at the bottom of the page with {colors.ink} background and {colors.muted} text. Contains links to About, Shipping, Returns, Contact, and social media icons (Facebook, Twitter, Instagram, Pinterest) in their respective brand colors. Links are {typography.caption} (11px monospace). On hover, link text shifts to {colors.canvas}. The footer also includes a copyright line in {colors.muted-soft}.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to a hamburger menu. Product cards stack in a single column. Search bar moves below the nav. Footer links stack vertically. Sale badges scale down slightly. |
| Tablet | 744–1128px | Nav remains horizontal but may wrap to two rows. Product cards display in a 2-column grid. Search bar is inline with the nav. Footer links remain horizontal but with reduced spacing. |
| Desktop | 1128–1440px | Full nav with all categories visible. Product cards in a 3- or 4-column grid. Search bar is a standalone element below the nav. Footer is full-width with horizontal link rows. |
| Wide | > 1440px | Content max-width is 1440px, centered. Product cards in a 4-column grid. Nav remains unchanged. Additional whitespace on the sides. |

### Touch Targets
- All buttons and links have a minimum touch target of 44px height (buttons are 40px with 2px padding on each side to reach 44px).
- Nav links have 48px touch height.
- Product cards are fully tappable with no minimum size constraint beyond the image.
- Search bar has 32px height — below the 44px recommendation, but acceptable for a text input.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger icon. The full category list appears in a slide-out drawer from the left.
- The search bar collapses from a full-width element to a compact icon that expands on tap.
- Product cards collapse from a multi-column grid to a single column.
- Footer links collapse from a horizontal row to a vertical stack.
- Sale badges remain visible but may reduce font size slightly.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for buttons and links were inferred from common patterns — the live site may use different transitions or colors.
- Error states for form inputs (validation, required fields) were not extracted. Assumed red border or text, but not confirmed.
- The exact font-family stack is `monospace` — the specific font (Courier New, Consolas, Liberation Mono) is an assumption based on common monospace defaults. The live site may use a custom monospace font.
- Sub-brand or collection-specific color palettes (e.g., "New Arrivals" vs. "Sale" sections) were not extracted.
- Dark mode is not supported — the site appears to be light-mode only.
- The social media icon colors (#3b5998, #1da1f2, #bd081d, #222222) are standard brand colors for Facebook, Twitter, Pinterest, and Instagram, respectively. These were extracted from the page but may not be actively used in the footer.
- The extracted color list includes many grays and a single hot pink (#ff5268). The pink is assumed to be the primary brand color because it is the most distinctive and appears in CTAs. However, the brand may also use other accent colors (e.g., yellow, green) that were not captured in the extraction.
- The `meta theme-color` is #ffffff, confirming a white canvas. No other theme-color meta tags were found.
- The site runs on Shopify, so checkout and cart components may use Shopify's default styling rather than custom tokens. These were not extracted.
