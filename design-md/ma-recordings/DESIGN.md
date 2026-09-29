---
version: alpha
name: "MA Recordings"
source_url: "https://www.marecordings.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep navy (#006699) anchors a site that sells silence — or rather, the absence of digital noise. MA Recordings, a purist audiophile label, presents its catalog on a near-blank white canvas where the only persistent color is that single blue, used for links, hover states, and the faint underlines that separate album titles from track times. The second extracted blue (#114499) appears in secondary accents — perhaps the shopping-cart icon or the footer dividers — but the design is so spartan that even these two colors feel like abundance. There are no hero images, no carousels, no category-strip animations; each album page is a typographic grid of metadata — artist, title, recording date, microphone type — set in what appears to be a system serif or a neutral sans-serif (no font-family declarations were extractable from the live CSS). The product card is a text block with a small thumbnail, the CTA is a text link in {colors.primary} rather than a pill or button, and the checkout flow likely inherits the same minimalism. This is a site that treats the browser as a liner-note booklet: the brand voltage comes from the recording quality, not the interface. The {rounded.full} tokens that dominate consumer DTC are absent here — corners are sharp, spacing is generous but not decorative, and the only "component" with any visual weight is the album cover thumbnail, which sits at a modest 200px square. MA Recordings does not sell a lifestyle; it sells a listening experience, and the design steps aside to let the music breathe.

colors:
  primary: "#006699"
  primary-active: "#114499"
  primary-disabled: "#b0c4de"
  ink: "#111111"
  body: "#222222"
  muted: "#555555"
  muted-soft: "#888888"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
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
    rounded: "{rounded.none}"
    padding: 8px 16px
    height: 36px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 7px 15px
    height: 36px
  text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    textDecoration: underline
  text-link-hover:
    textColor: "{colors.primary-active}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-hover:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 16px
  product-card-thumbnail:
    width: 200px
    height: 200px
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-artist:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: 24px 16px
  footer-link:
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  album-detail-grid:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 24px
  album-detail-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    textTransform: uppercase
  album-detail-value:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  cart-icon:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    height: 24px
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px

## Components

### Buttons
**`button-primary`** — A flat, rectangular button with no border radius, using the brand's deep navy (#006699) as background and white text. The hover state shifts to the darker accent blue (#114499). This button appears only in checkout and account actions — the primary "add to cart" action on album pages is a text link, not a button, preserving the site's editorial feel.

**`button-secondary`** — An outlined variant with a white background and navy text, sharing the same sharp corners and compact padding. Used for secondary actions like "View Cart" or "Continue Shopping." The 1px border is implied by the background contrast rather than an explicit stroke.

**`text-link`** — The dominant CTA pattern across the site. A simple underlined text link in the brand blue, with no background or padding. Used for "Add to Cart," "More Info," and navigation items. The hover state darkens the blue to #114499. This component is the site's primary interaction affordance — there are no pill buttons, no filled CTAs on product pages.

### Navigation
**`nav-bar`** — A minimal top bar, 48px tall, with white background and black text. Links are spaced with 12px padding and use the same sans-serif as body text. The hover state turns the link text to the brand blue. No logo is present in the extracted data — the site likely uses a text-based "MA Recordings" title in the header.

**`nav-link`** — A text-only link with no background or border, matching the site's overall restraint. Active state is indicated by the brand blue color, not an underline or background change.

### Product Cards
**`product-card`** — A text-heavy card with a small thumbnail (200px square), no border radius, and generous 16px padding. The card contains the album title (serif, 18px), the artist name (sans-serif, 14px, muted gray), and the price (sans-serif, 16px). There is no shadow, no border, no hover lift — the card is a typographic block that trusts the album art and metadata to sell the product.

**`product-card-thumbnail`** — A fixed 200px square image with no rounding. The thumbnail is small relative to the text block, reinforcing the site's focus on information over imagery.

### Forms
**`text-input`** — A simple rectangular input field with no border radius, white background, and 8px padding. The border is a 1px solid hairline (#cccccc). Focus state likely uses the brand blue as a border color, though this could not be extracted.

### Footer
**`footer`** — A light gray (#f5f5f5) background section with muted text and brand-blue links. Padding is 24px top/bottom and 16px sides. The footer contains copyright text, links to the label's social media (likely icons in brand blue), and possibly a newsletter signup.

### Album Detail Grid
**`album-detail-grid`** — The core layout for individual album pages. A two-column or stacked grid of metadata labels (uppercase, muted, 12px) and values (regular weight, 16px, black). Fields include: Artist, Title, Recording Date, Location, Microphone, Format, and Price. The grid has 24px padding and no visual dividers — spacing alone separates the fields.

**`cart-icon`** — A simple icon in brand blue, 24px tall, with no background or badge. The cart icon is likely a shopping bag or basket outline, matching the site's minimal aesthetic.

**`checkout-button`** — The only filled button on the site, using the brand navy background with white text. It appears only on the cart/checkout page, not on product cards. The button is rectangular with no border radius and 12px/24px padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; album detail grid stacks vertically; product card thumbnail reduces to 150px; nav bar collapses to hamburger menu; footer links stack |
| Tablet | 744–1128px | Two-column product grid; album detail grid uses two columns; nav bar shows all links; footer uses two columns |
| Desktop | 1128–1440px | Three-column product grid; album detail grid uses two columns with wider spacing; nav bar centered; footer uses three columns |
| Wide | > 1440px | Max-width container (1200px) centered; product grid may expand to four columns; album detail grid uses two columns with generous whitespace |

### Touch Targets
- All interactive elements (links, buttons, inputs) are at least 44px tall on mobile
- Text links have 8px minimum padding on all sides to ensure tappable area
- Cart icon is 24px with 10px invisible padding for touch targets
- Checkout button is 44px tall, exceeding the 44px minimum

### Collapsing Strategy
- Navigation collapses to a hamburger menu below 744px
- Product grid collapses from 3 columns to 2 at 744px, then to 1 at mobile
- Album detail metadata grid collapses from 2 columns to 1 below 744px
- Footer columns collapse from 3 to 2 at 744px, then to 1 at mobile
- Product card thumbnail reduces from 200px to 150px on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font-family declarations could not be extracted from the live site CSS. The typography block uses Georgia (serif) for display and Arial (sans-serif) for body text as reasonable defaults for a text-heavy audiophile site, but the actual fonts may differ.
- Hover states for text inputs (border color, shadow) could not be extracted.
- Error styling for forms (invalid email, missing fields) is unknown.
- The checkout flow's visual design (payment form, order summary) could not be extracted.
- Mobile navigation behavior (hamburger menu animation, overlay style) is inferred.
- The site's logo or wordmark treatment is unknown — assumed to be text-based.
- Social media icon colors and hover states are unknown.
- The product card's hover state (if any) is unknown — assumed to be none based on the site's minimalism.
- Dark mode or high-contrast mode styles are not present in the extracted data.
- The site's use of images (album covers, artist photos) beyond the 200px thumbnail is unknown.
- The extracted color palette is limited to two blues and white — the brand may use additional accent colors for badges, sale indicators, or genre tags that were not captured.
