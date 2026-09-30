---
version: alpha
name: "Phaidon"
source_url: "https://www.phaidon.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A scholarly yet sensual art-book publisher whose identity is built on a near-black ink (#231f20) and a sharp, acidic yellow (#ffc800) — the kind of yellow that reads as a highlighter stroke across a monograph page, not a friendly accent. The brand trusts its typography above all else: Akzidenz Grotesk Next in its condensed and extended cuts runs across the entire surface, from 12px captions that sit tight against plate edges to 48px display heads that stretch across full-bleed spreads. The yellow appears sparingly — a single CTA button, a price badge, a category tag — and never competes with the art itself. The canvas is a warm off-white (#f0f0f0) rather than pure white, giving the site the feel of uncoated paper stock. Secondary blues (#bad2df) and teals (#088f87) surface only in editorial callouts and footer links, never in primary actions. The grid is generous: 64px sections, 48px xxl spacing, and cards with soft 12px radii (`{rounded.md}`) that suggest a gallery wall rather than a product shelf. There is no hero video, no auto-playing carousel — just a clean, typographic hierarchy that lets the book covers breathe. The checkout path, powered by Shopify, introduces a secondary yellow (#f6e70f) and a cooler gray (#dedede) for form fields, but the editorial pages remain resolutely monochrome with yellow as the sole voltage.

colors:
  primary: "#ffc800"
  primary-active: "#e6b400"
  primary-disabled: "#ffe680"
  ink: "#231f20"
  body: "#121212"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#cfcfcf"
  hairline-soft: "#dedede"
  canvas: "#f0f0f0"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#231f20"
  editorial-blue: "#bad2df"
  editorial-teal: "#088f87"
  checkout-accent: "#f6e70f"
  star-rating: "#ffc800"
  error: "#c13515"

typography:
  display-xl:
    fontFamily: "'akzidenz-grotesk-next-extend', 'akzidenz-grotesk-next', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'akzidenz-grotesk-next-extend', 'akzidenz-grotesk-next', Helvetica, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'akzidenz-grotesk-next', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'akzidenz-grotesk-next', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'akzidenz-grotesk-next', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'akzidenz-grotesk-next', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'akzidenz-grotesk-next', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'akzidenz-grotesk-next', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'akzidenz-grotesk-next', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'akzidenz-grotesk-next-conden', 'akzidenz-grotesk-next', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  caption-sm:
    fontFamily: "'akzidenz-grotesk-next-conden', 'akzidenz-grotesk-next', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'akzidenz-grotesk-next', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'akzidenz-grotesk-next', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'akzidenz-grotesk-next', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'akzidenz-grotesk-next', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'akzidenz-grotesk-next', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'akzidenz-grotesk-next', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0

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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
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
    padding: 12px 24px
    height: 44px
    border: 1px solid "{colors.hairline}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 0
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.ink}"
  text-input-error:
    border: 1px solid "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid "{colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: 12px 16px 4px
  product-card-price:
    typography: "{typography.price}"
    padding: 0 16px 12px
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.caption}"
    textColor: "{colors.primary}"
  category-tag:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 12px
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: 64px 24px
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  breadcrumb:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    textColor: "{colors.ink}"
    fontWeight: 600
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 44px
    border: 1px solid "{colors.hairline}"
  add-to-cart-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 24px
    height: 56px

## Components

### Buttons
**`button-primary`** — A flat, sharp-cornered yellow rectangle that reads as a deliberate editorial mark rather than a friendly tap target. The uppercase Akzidenz Grotesk Next at 14px sits centered on a 44px-tall block of #ffc800. On hover, the yellow deepens to #e6b400 (`{colors.primary-active}`); the disabled state fades to a pale #ffe680 (`{colors.primary-disabled}`). There is no border, no shadow, no pill radius — the button is a pure typographic gesture.

**`button-secondary`** — An outlined variant on the same 44px frame, using the canvas background color with a 1px hairline border (#cfcfcf). The text remains #231f20. This button sits alongside the primary in checkout flows and secondary CTAs, always subordinate to the yellow block.

**`button-tertiary`** — A text-only link styled as a button, with no background, no border, and no padding beyond 12px vertical. Used for "View all" links and filter resets. The uppercase 14px weight-600 text sits flush against the content edge.

### Cards
**`product-card`** — A white card on the warm #f0f0f0 canvas, with a 12px radius (`{rounded.md}`) that softens the otherwise sharp-cornered system. The card contains a full-bleed image with rounded top corners, followed by the book title in 16px weight-600 and the price in 16px weight-600. A yellow badge (`{product-card-badge}`) may appear in the top-left corner for "New" or "Sale" flags, set in 11px uppercase weight-600 on the #ffc800 background. Cards sit on a generous 24px grid gutter.

**`category-tag`** — A small, sharp-cornered yellow pill used to label book categories (Architecture, Art, Design, etc.). The 11px uppercase badge text sits on #ffc800 with 4px vertical and 12px horizontal padding. These tags appear above product titles and in filter strips.

### Navigation
**`nav-bar`** — A 72px-tall bar on the #f0f0f0 canvas, separated from the content by a 1px #dedede hairline. The Phaidon logotype sits left, navigation links (Books, Categories, Gifts, Sale) run center, and a search icon plus cart icon sit right. Links are 14px uppercase weight-500 with 8px vertical and 16px horizontal padding. The active link switches text color to #ffc800.

**`breadcrumb`** — A condensed 11px uppercase secondary navigation used on product and category pages. Items are separated by a "/" in #cfcfcf, with the current page in #231f20 weight-600.

### Forms
**`text-input`** — A 44px-tall white input with a 1px #cfcfcf border and no border-radius. The 16px Akzidenz Grotesk Next text sits with 12px vertical and 16px horizontal padding. On focus, the border switches to #231f20. Error states use a #c13515 border.

**`quantity-selector`** — A compact 44px-tall input with minus/plus buttons flanking a centered numeric value. Used on the product page and cart. The border is 1px #cfcfcf, and the buttons are text-only with no background.

### Footer
**`footer`** — A dark band at #231f20 (`{colors.ink}`) with white text and yellow headings. Links are 14px weight-400 in white, and section headings use the 12px uppercase condensed cut in #ffc800. The footer is padded 48px vertically and 24px horizontally, with a 64px section gap above it.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to hamburger; product cards stack; hero padding reduces to 32px; display-xl drops to 32px; search bar moves to full-width below nav |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses 40px display-lg; section padding at 48px |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at 48px display-xl; 64px section padding |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px centered; hero may use 56px display with wider letter-spacing |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height
- Nav links have 8px vertical padding on a 72px bar, ensuring 44px+ tap targets
- Quantity selector buttons are 44px × 44px
- Search bar and text inputs are 44px tall
- Product card tap targets (title, price, badge) are at least 44px tall

### Collapsing Strategy
- Primary nav collapses to a hamburger menu below 744px
- Category filter strip collapses to a horizontal scrollable row below 744px
- Product grid collapses from 4 columns to 3 to 2 to 1 as viewport shrinks
- Footer columns stack to single column below 744px
- Hero section reduces vertical padding from 64px to 32px on mobile
- Search bar moves from inline nav position to full-width below nav on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for secondary buttons, text inputs, and nav links were not fully extractable from the live site CSS; the active states provided are best-guess based on common patterns
- Error state styling for forms (error messages, iconography, color) could not be confirmed — #c13515 is an assumption based on common e-commerce patterns
- The editorial blue (#bad2df) and teal (#088f87) appear in the extracted colors but their exact usage context (backgrounds, borders, text) is inferred from visual inspection of a limited page set
- Dark mode is not supported and no dark-mode tokens were found in the extracted CSS
- Sub-brand or collection-specific color palettes (e.g., Phaidon Architecture, Phaidon Kids) were not extracted
- The Shopify checkout flow may introduce additional colors (Klarna pink, Afterpay black) that are not part of the Phaidon brand system
- Font weight values for Akzidenz Grotesk Next variants are estimates based on common weights (400, 500, 600); the exact weight mapping for each cut could not be confirmed
- The `textTransform: uppercase` on nav-link and button styles is inferred from the brand's typographic treatment but not explicitly confirmed in extracted CSS
- Spacing values for section padding and grid gutters are estimates based on visual analysis of a single page viewport
