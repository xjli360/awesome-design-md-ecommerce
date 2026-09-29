---
version: alpha
name: "Permanent Records"
source_url: "https://www.permanentrecordsla.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A black-and-gray concrete bunker for vinyl obsession, where #222222 ink on #f4f4f4 canvas reads like a photocopied zine pinned to a corkboard — no gradient, no hero image, just raw typographic hierarchy and the occasional #e74c3c alert badge to signal a sold-out pre-order. The brand uses Proxima Nova at 14–16px for nearly everything, trusting weight contrast (400 vs 600) over size jumps to separate body from title; there is no display face, no serif warmth, no decorative flourish. Buttons are hard-cornered rectangles (`{rounded.none}`) with #444444 borders on white canvas, and the only pill shape (`{rounded.full}`) appears on the search input — a lone concession to usability in an otherwise orthogonal grid. The #e74c3c accent (a desaturated stop-sign red) appears on price drops, sold-out badges, and the cart count dot, while #ff9b00 amber signals the "Add to Cart" CTA on product detail pages — a rare splash of heat in a monochrome system. The site feels like the store itself: fluorescent-lit, shelf-dense, built for people who already know what they want.

colors:
  primary: "#e74c3c"
  primary-active: "#c0392b"
  primary-disabled: "#f5b7b1"
  ink: "#222222"
  body: "#444444"
  muted: "#777777"
  muted-soft: "#aaaaaa"
  hairline: "#ced0d2"
  hairline-soft: "#e3e5e7"
  canvas: "#f4f4f4"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-amber: "#ff9b00"
  accent-amber-active: "#e68a00"
  accent-amber-disabled: "#ffe0b3"
  badge-soldout: "#e74c3c"
  badge-preorder: "#5897fb"
  badge-sale: "#ff9b00"
  price-drop: "#e74c3c"
  cart-count: "#e74c3c"
  scrim: "#111111"

typography:
  display-xl:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0
    textTransform: uppercase
  button-md:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  link:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  price:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-sale:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
    color: "{colors.price-drop}"

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
    rounded: "{rounded.none}"
    padding: 10px 20px
    height: 40px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 9px 19px
    height: 40px
    border: 1px solid "{colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: 1px solid "{colors.muted}"
  button-cta-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 10px 20px
    height: 40px
    border: none
  button-cta-amber-active:
    backgroundColor: "{colors.accent-amber-active}"
  button-cta-amber-disabled:
    backgroundColor: "{colors.accent-amber-disabled}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 40px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.muted}"
  search-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: 1px solid "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: 1px solid "{colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.ink}"
    fontWeight: 700
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    border: 1px solid "{colors.hairline-soft}"
  product-card-hover:
    border: 1px solid "{colors.hairline}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: 1/1
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-artist:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
  badge-soldout:
    backgroundColor: "{colors.badge-soldout}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  badge-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.base}"
    borderTop: 1px solid "{colors.hairline}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
    textDecoration: none
  footer-link-hover:
    textColor: "{colors.canvas}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.base}"
  section-header:
    typography: "{typography.title-md}"
    paddingBottom: "{spacing.md}"
    borderBottom: 1px solid "{colors.hairline-soft}"
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 40px
    border: 1px solid "{colors.hairline}"
  cart-count-badge:
    backgroundColor: "{colors.cart-count}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
    padding: 0 4px

## Components

### Buttons
**`button-primary`** — The primary action button, a hard-cornered rectangle in #e74c3c red with white text. Used for "Add to Cart" on product listing pages and primary checkout flows. On hover, shifts to `{colors.primary-active}` (#c0392b). Disabled state uses `{colors.primary-disabled}` (#f5b7b1) with no border.

**`button-secondary`** — A white button with a 1px `{colors.hairline}` border and `{colors.ink}` text. Used for secondary actions like "View Details" or "Cancel". Active state fills `{colors.surface-soft}` background and darkens the border to `{colors.muted}`. No rounded corners — matches the orthogonal system.

**`button-cta-amber`** — The high-contrast amber (#ff9b00) button reserved for the product detail page's primary "Add to Cart" action. Uses `{colors.ink}` text for maximum readability against the warm background. Active state shifts to `{colors.accent-amber-active}` (#e68a00). Disabled state uses `{colors.accent-amber-disabled}` (#ffe0b3).

### Cards
**`product-card`** — A white card on `{colors.surface-card}` background with a 1px `{colors.hairline-soft}` border and no rounded corners. Contains a square aspect-ratio image, the album title in `{typography.title-sm}`, the artist name in `{typography.body-sm}` muted to `{colors.muted}`, and the price in `{typography.price}`. On hover, the border shifts to `{colors.hairline}` for a subtle lift. Sale prices render in `{colors.price-drop}` red.

**`badge-soldout`** — A compact #e74c3c red badge with white uppercase text at 11px/700 weight. No rounded corners. Positioned top-left on product card images. Also used for "Sold Out" labels on product detail pages.

**`badge-preorder`** — A #5897fb blue badge with white uppercase text. Used for upcoming releases available for pre-order. Same dimensions and typography as the soldout badge.

**`badge-sale`** — An amber (#ff9b00) badge with `{colors.ink}` text. Used to flag discounted items. Same dimensions and typography as other badges.

### Navigation
**`nav-bar`** — A white 56px-high bar with a 1px `{colors.hairline-soft}` bottom border. Contains the store logo, category links, and a search icon. Active nav links use `{colors.ink}` at 700 weight; inactive links use `{colors.muted}` at 600 weight. The search icon opens the pill-shaped search input.

**`nav-link-active`** — Bold (700) `{colors.ink}` text for the current section. No underline or indicator — relies on weight contrast alone.

**`nav-link-inactive`** — Medium (600) `{colors.muted}` text for non-active sections. Hover shifts to `{colors.ink}`.

### Forms
**`text-input`** — A white input field with a 1px `{colors.hairline}` border and no rounded corners. Used for email signup, checkout forms, and filter fields. On focus, the border shifts to `{colors.muted}`. Height is 40px with 8px/12px padding.

**`search-input`** — The only pill-shaped element in the system (`{rounded.full}`). A white field with a 1px `{colors.hairline}` border and 16px horizontal padding. Used exclusively for site-wide search. The pill shape is a deliberate departure from the orthogonal system — a usability concession for a frequently used element.

**`filter-dropdown`** — A white dropdown with a 1px `{colors.hairline}` border and no rounded corners. Used for sorting and filtering product listings (by genre, format, price). Same 40px height as text inputs.

### Footer
**`footer`** — A dark footer on `{colors.ink}` (#222222) background with `{colors.muted-soft}` (#aaaaaa) text. Links use `{typography.link}` with no underline by default; hover shifts to `{colors.canvas}` white. Contains store info, social links, and legal text in `{typography.caption}`.

### Hero & Sections
**`hero-section`** — A full-width section on `{colors.surface-soft}` (#eeeeee) background with `{spacing.section}` vertical padding. Used for featured releases, announcements, and seasonal promotions. No image background — relies on typography and product cards for visual interest.

**`section-header`** — A `{typography.title-md}` heading with `{spacing.md}` bottom padding and a 1px `{colors.hairline-soft}` bottom border. Used to label product categories, featured sections, and content blocks.

### Cart
**`cart-count-badge`** — A circular (#e74c3c) badge with white text at 11px. Minimum 18px diameter with 0–4px horizontal padding. Positioned on the cart icon in the nav bar. Displays the number of items in the cart.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1–2 columns). Nav collapses to hamburger menu. Search input hidden behind icon. Footer stacks vertically. |
| Tablet | 744–1128px | Two-column product grid. Nav links visible but condensed. Search input remains pill-shaped but narrower. Footer columns wrap to 2. |
| Desktop | 1128–1440px | Three-column product grid. Full nav with all category links. Search input at full width. Footer displays all columns. |
| Wide | > 1440px | Four-column product grid. Max-width container (1440px) with centered content. Additional whitespace on sides. |

### Touch Targets
- All buttons and interactive elements minimum 40px height (44px on mobile).
- Nav links minimum 44px tap area on mobile.
- Product card tap targets minimum 48px for title/artist links.
- Filter dropdowns minimum 44px height on touch devices.
- Cart count badge minimum 24px diameter on mobile.

### Collapsing Strategy
- Nav links collapse to hamburger menu below 744px. The hamburger icon is 44x44px with a 32px tap target.
- Product grid columns reduce from 4 to 1 as viewport narrows.
- Footer columns collapse from 4 to 1, stacking vertically below 744px.
- Search input collapses to icon-only below 744px, expanding to full-width pill on tap.
- Section padding reduces from `{spacing.section}` (64px) to `{spacing.xxl}` (48px) on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards and buttons are inferred from common patterns; exact CSS transitions and box-shadow values were not extractable from the live site.
- Error styling for form inputs (validation messages, error borders) was not visible in the extracted data.
- The exact font weights for Proxima Nova (400, 600, 700) are inferred from common usage; the site may use additional weights (300, 500, 800) in specific contexts.
- The amber (#ff9b00) CTA button placement is inferred from product detail page patterns; it may also appear in cart and checkout flows.
- Dark mode is not supported; the site uses a light-only palette with `{colors.canvas}` (#f4f4f4) as the primary background.
- The extracted hex list includes several colors (#5897fb, #ff9b00, #995d00, #fde9e9, #f58c8c, #e03939, #9b1818) that may belong to third-party widgets (Shopify Pay, Klarna, Afterpay) rather than the brand itself. The core brand palette is the grayscale (#222222 through #f4f4f4) plus #e74c3c red.
- The site may use a different font for display headings (e.g., a serif or monospace) that was not captured in the extracted font-family declarations. The current typography block assumes Proxima Nova for all text.
- Sub-brand or seasonal color palettes (Record Store Day exclusives, label-specific badges) were not extractable.
- The exact spacing scale is inferred from common e-commerce patterns; the site may use non-standard values for specific components.
