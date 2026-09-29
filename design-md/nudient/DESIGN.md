---
version: alpha
name: "Nudient"
source_url: "https://www.nudient.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A monochrome canvas of #f8f8f8 and #232323 where phone cases become architectural objects rather than accessories — the brand treats its product photography with the same deadpan precision as a Scandinavian furniture catalog, letting matte black polycarbonate and microfiber lining speak through negative space. The extracted palette is overwhelmingly achromatic: #232323 anchors the system as the ink for every headline and primary CTA, while #f8f8f8 provides a warm, almost paper-like canvas that softens what could be a cold minimalism. The single chromatic voltage comes from #0e2cc7, a saturated royal blue that appears on sale badges, delivery-promise highlights, and the occasional accent link — it’s used so sparingly that when it appears it feels like a deliberate interruption. Futura PT runs across the system in two weights (book and medium), a geometric sans that echoes the brand’s mid-century modern sensibility; there are no rounded corners on the product itself, but the UI uses {rounded.sm} for buttons and {rounded.md} for cards, creating a subtle distinction between the hard-edged product and the soft interface that frames it. The checkout flow introduces #31862d (a muted green for “in stock” indicators) and #dd4242 (error states), but these feel inherited from Shopify’s defaults rather than brand decisions. The overall effect is a storefront that trusts its product photography to carry the emotional weight — the UI is deliberately recessive, a gallery wall painted #f8f8f8 where the phone cases are the art.

colors:
  primary: "#232323"
  primary-active: "#111111"
  primary-disabled: "#bfbfbf"
  ink: "#232323"
  body: "#444444"
  muted: "#636363"
  muted-soft: "#bfbfbf"
  hairline: "#dedede"
  hairline-soft: "#dcdcdc"
  canvas: "#f8f8f8"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#0e2cc7"
  accent-yellow: "#ffcc00"
  accent-green: "#31862d"
  error-red: "#dd4242"
  error-dark: "#c72d00"
  sale-badge: "#0e2cc7"
  stock-green: "#31862d"
  star-rating: "#fcc13c"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Futura PT', futura-pt_book, Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.5px
  display-lg:
    fontFamily: "'Futura PT', futura-pt_book, Georgia, serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: 0.3px
  display-md:
    fontFamily: "'Futura PT', futura-pt_medium, Georgia, serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.25px
  title-lg:
    fontFamily: "'Futura PT', futura-pt_medium, Georgia, serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.2px
  title-md:
    fontFamily: "'Futura PT', futura-pt_medium, Georgia, serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.15px
  body-md:
    fontFamily: "'Futura PT', futura-pt_book, Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0
  body-sm:
    fontFamily: "'Futura PT', futura-pt_book, Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Futura PT', futura-pt_book, Georgia, serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Futura PT', futura-pt_book, Georgia, serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'Futura PT', futura-pt_medium, Georgia, serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Futura PT', futura-pt_medium, Georgia, serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Futura PT', futura-pt_book, Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  nav-link:
    fontFamily: "'Futura PT', futura-pt_medium, Georgia, serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Futura PT', futura-pt_medium, Georgia, serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "'Futura PT', futura-pt_medium, Georgia, serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.40
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
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.error-red}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-sale-badge:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-stock-badge:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-rating:
    textColor: "{colors.star-rating}"
    typography: "{typography.caption-sm}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 32px
    height: 44px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-dark:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: 16px 0
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 0 0 16px 0
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  notification-bar:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: 8px 16px
    height: 36px
  error-message:
    backgroundColor: "{colors.error-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  success-message:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 8px 12px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a solid #232323 rectangle with uppercase Futura PT Medium at 14px. On hover, the background shifts to #111111 with no scale or shadow animation — the brand prefers a flat, no-fuss interaction. The disabled state uses #bfbfbf for background, maintaining the same dimensions and typography but removing all interactivity cues. **`button-secondary`** — An inverted variant with #f8f8f8 background and #232323 text, used on dark hero sections or footer areas where the primary button would blend into the canvas. **`button-secondary-outline`** — A transparent background with a 1px #232323 border, used for “Add to Cart” on product detail pages and secondary actions in modals. **`button-accent-blue`** — Reserved for promotional CTAs and limited-edition drops, using #0e2cc7 as the background to create visual urgency against the otherwise monochrome palette.

### Cards
**`product-card`** — A clean, borderless card on #f8f8f8 canvas with {rounded.md} corners applied only to the image container. The card contains a product image on #f4f4f4 background, a title in {typography.title-md}, and a price in {typography.price}. Sale items display a **`product-card-sale-badge`** — a small #0e2cc7 rectangle with white uppercase text, positioned at the top-left of the image. In-stock indicators use **`product-card-stock-badge`** with #31862d background. The rating component uses #fcc13c for star icons, rendered at 12px.

### Navigation
**`nav-bar`** — A fixed top bar at 64px height on #f8f8f8, containing the brand logo (left), navigation links in uppercase 13px Futura PT Medium with 0.5px letter-spacing (center), and utility icons (search, cart, account) on the right. On scroll, the bar compresses to 56px. The mobile hamburger menu icon uses a 40px {rounded.full} touch target. **`nav-link`** — Uppercase 13px Futura PT Medium with no underline decoration; the active page is indicated by a 2px #232323 underline bar beneath the text.

### Forms
**`text-input`** — A 48px tall input on #f8f8f8 canvas with 1px #dedede border and {rounded.sm} corners. Focus state shifts the border to #232323. Error state uses #dd4242 border and text color for the error message below the field. The placeholder text is #bfbfbf. **`quantity-selector`** — A compact 40px tall component with minus/plus buttons flanking a centered numeric value, used on cart and product detail pages.

### Footer
**`footer-section`** — A full-width #232323 block with white text, containing column headings in {typography.title-md} and links in {typography.link}. The footer uses no background image or pattern — the brand maintains its minimal ethos even in the deepest part of the page. Social media icons render in white at 20px with 40px {rounded.full} touch targets. **`footer-link`** — White 14px Futura PT Book with no underline; hover adds a subtle opacity shift to 0.8.

### Notifications & Messages
**`notification-bar`** — A 36px tall banner across the top of the page (below the nav) using #0e2cc7 background, used for shipping promotions, sale announcements, and cookie consent. The text is white 13px Futura PT Book. **`error-message`** — A #dd4242 background pill with white text, used for form validation and checkout errors. **`success-message`** — A #31862d background pill with white text, used for “Added to Cart” confirmations and successful form submissions.

### Dividers
**`divider`** — A 1px #dedede horizontal rule used between sections and product rows. **`divider-soft`** — A 1px #dcdcdc variant used within cards and accordion panels for a subtler separation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to {typography.display-lg}; product cards stack vertically; footer links collapse into accordion; search bar becomes full-width below nav |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but reduce letter-spacing; hero maintains {typography.display-xl} with reduced padding; footer shows two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses maximum padding; footer shows four columns; product cards show hover state with subtle shadow |
| Wide | > 1440px | Four-column product grid; content max-width at 1440px with centered layout; hero uses larger typography scale; product cards gain additional whitespace |

### Touch Targets
- All interactive elements (buttons, links, icons) maintain minimum 44px height
- Icon buttons use 40px {rounded.full} circles for finger-friendly taps
- Quantity selector buttons are 40px × 40px minimum
- Mobile nav hamburger icon is 44px × 44px
- Product card tap targets extend to full card width

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Footer link columns collapse to single accordion below 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Hero section reduces padding from 64px to 32px on mobile
- Search bar transitions from inline to full-width below 744px
- Product image galleries switch from row to single-image swipe on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the static HTML; the above assumes minimal opacity/border changes based on common patterns
- Error state styling for select dropdowns and checkboxes was not observed
- The brand may use additional Futura PT weights (light, bold) that were not present in the extracted font declarations
- Dark mode styling is not present on the live site and was not documented
- Sub-brand or collection-specific color palettes (e.g., limited edition drops) were not captured
- Animation durations and easing curves for transitions (button hover, card hover, nav scroll) were not extractable
- The exact border width for `button-secondary-outline` is assumed at 1px based on visual inspection
- Checkout-specific styling (Shopify checkout override colors) was not extracted and may differ from the main site palette
- The extracted #fcc13c (star-rating) and #ffcc00 (accent-yellow) may be Shopify default colors rather than intentional brand choices
- Product card shadow on hover was not extractable and is assumed to be a subtle box-shadow based on common e-commerce patterns
