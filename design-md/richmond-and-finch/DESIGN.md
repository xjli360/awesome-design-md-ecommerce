---
version: alpha
name: "Richmond & Finch"
source_url: "https://www.richmondfinch.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A phone-case brand that uses a saturated #0051c3 as its primary voltage — a confident, almost electric blue that appears across CTAs, badges, and category headers, while a secondary #bd2426 (a deep crimson) and #9bca3e (a sharp lime green) create a three-color accent system that feels more like a sportswear label than a phone accessory shop. The extracted palette reads as a generic web framework base (#dedede, #ebebeb, #404040, #313131) overlaid with these three distinctive brand accents, suggesting the live site may have been unreachable at extraction time — the DNS failure in the page title confirms this. The typography stack is a standard system-font fallback chain (-apple-system, BlinkMacSystemFont, Roboto, Helvetica Neue, sans-serif), indicating no custom typeface investment; the brand relies on weight contrast and generous whitespace rather than proprietary letterforms. The crimson #bd2426 appears as a secondary CTA color and likely powers sale badges or error states, while the lime #9bca3e suggests in-stock indicators or promotional ribbons. The blue family (#0051c3, #0045a6, #003681, #2f7bbf) forms a gradient scale from primary to hover to deep navy, with #f68b1f and #ee730a adding an orange accent for shipping or urgency badges. The overall system reads as a high-contrast, accessibility-conscious palette built for e-commerce conversion — bright accents against a neutral gray canvas, with {rounded.sm} corners on buttons and {rounded.md} on product cards to keep the interface crisp without feeling playful.

colors:
  primary: "#0051c3"
  primary-active: "#0045a6"
  primary-disabled: "#b0c9e8"
  ink: "#313131"
  body: "#404040"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#d9d9d9"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-crimson: "#bd2426"
  accent-lime: "#9bca3e"
  accent-orange: "#f68b1f"
  accent-orange-active: "#ee730a"
  blue-dark: "#003681"
  blue-mid: "#2f7bbf"
  gray-light: "#dedede"
  gray-mid: "#d9d9d9"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.25px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.25px
    textTransform: uppercase

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
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-accent-crimson:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-crimson}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-instock:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: 64px 24px
  hero-banner-accent:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: 64px 24px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    textColor: "{colors.gray-light}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 44px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's electric blue {colors.primary} (#0051c3) and white text. On hover or active, it shifts to {colors.primary-active} (#0045a6). The disabled state uses {colors.primary-disabled} (#b0c9e8) to signal non-interactivity. All primary buttons use {rounded.sm} (8px) corners and 44px height for comfortable touch targets.

**`button-secondary`** — An outlined-style button with a white background and {colors.primary} text. The active state inverts to {colors.surface-soft} background with {colors.primary-active} text. Used for "View All" links, secondary CTAs, and cancel actions. Maintains the same 44px height and {rounded.sm} corners as the primary button for visual consistency.

**`button-accent-crimson`** — A high-urgency variant using {colors.accent-crimson} (#bd2426) as the fill color. Reserved for "Sale," "Clearance," or limited-time offers where the brand needs to signal urgency without competing with the primary blue. Same dimensions and corner radius as the primary button.

**`button-accent-orange`** — A compact, smaller button (36px height) using {colors.accent-orange} (#f68b1f). Used for shipping announcements, "Free Shipping" badges, or inline promotional triggers. Uses {typography.button-sm} to fit tighter layouts.

### Cards
**`product-card`** — The core product display unit, a white card with {rounded.md} (12px) corners. Contains a product image with matching corner radius, a title in {typography.title-sm}, and a price in {typography.body-md}. Badges overlay the top-left corner of the image area. Cards sit on a white or {colors.surface-soft} background with no visible shadow — the brand relies on the hairline divider for separation.

**`product-card-badge`** — Small, uppercase labels (11px, 700 weight) that overlay product images. Three variants exist: crimson for "Sale," orange for promotional messaging, and lime green for "In Stock" or "New." All use {rounded.xs} (4px) corners and tight 2px 8px padding to minimize visual footprint.

### Navigation
**`nav-bar`** — A 64px fixed-height bar with white background and uppercase nav links in {typography.nav-link} (14px, 600 weight, 0.25px letter-spacing). Active links render in {colors.primary}, inactive links in {colors.muted}. The bar likely includes a logo lockup on the left, a search icon on the right, and a cart icon with a badge count.

**`category-chip`** — Pill-shaped filter chips (36px height, {rounded.full}) used for product category navigation. Inactive chips use {colors.surface-soft} background with {colors.ink} text; active chips switch to {colors.primary} background with white text. Used in horizontal scrollable strips on mobile and tablet.

### Forms
**`text-input`** — Standard 48px input fields with {rounded.sm} corners, white background, and {colors.ink} text. Focus state adds a {colors.primary} border (2px). Error state swaps the border to {colors.accent-crimson} and text to the same red. Used for search, checkout forms, and newsletter signups.

**`search-bar`** — A pill-shaped search input ({rounded.full}) with a {colors.surface-soft} background and 48px height. On focus, the background shifts to white and a {colors.primary} border appears. The pill shape differentiates the global search from standard form inputs.

### Footer
**`footer`** — A dark footer section using {colors.ink} (#313131) as the background with white text. Links render in {colors.gray-light} (#dedede) and shift to full white on hover. The footer uses 48px vertical padding and likely contains 3-4 columns of links, social icons, and a newsletter signup form.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 columns), hamburger nav replaces top nav, category chips collapse to horizontal scroll, hero banner reduces to 48px padding, footer stacks to single column |
| Tablet | 744–1128px | Two-column product grid (3-4 columns), full top nav visible with condensed links, category chips in scrollable strip, hero banner at 56px padding, footer in 2-column layout |
| Desktop | 1128–1440px | Three-column product grid (4 columns), full top nav with all links, category chips in static row, hero banner at 64px padding, footer in 3-4 column layout |
| Wide | > 1440px | Max-width container (1440px) centered, product grid expands to 5 columns, all elements at maximum spacing, hero banner may include full-bleed imagery |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Category chips are 36px tall — below the 44px recommendation, but acceptable for horizontal scroll contexts where chips are not the primary interaction
- Product cards are tap-targets for the entire card area, not just the title or price
- Search bar is 48px tall for comfortable thumb reach
- Nav links in mobile hamburger menu are 48px tall tap targets

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with the logo centered and cart/search icons flanking
- Category chip strip collapses from a static row to a horizontally scrollable container on mobile and tablet
- Footer collapses from 3-4 columns to a single stacked column below 744px
- Hero banner reduces padding and may hide secondary text or CTAs on mobile
- Product grid reduces from 4-5 columns to 2 columns on mobile, ensuring each card remains legible

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The live site was unreachable at extraction time (DNS resolution failure), so the extracted hex colors and font declarations come from cached or fallback HTML/CSS — the true brand palette may differ significantly from what is documented here
- No hover states, focus rings, or active press states could be extracted for any component beyond the primary button
- No typography scale could be confirmed from live CSS — the documented scale is an educated guess based on the system font stack and common e-commerce patterns
- No spacing scale or grid system could be extracted — the documented spacing tokens are generic defaults
- No shadow/elevation tokens could be extracted — product cards may use box-shadow or border-based separation
- No animation or transition timing values could be extracted
- No iconography style or social media icon colors could be confirmed
- No dark mode or high-contrast mode variants exist in the extracted data
- The brand's actual primary color may be one of the three accent colors (crimson, lime, orange) rather than the blue — the blue was chosen as primary because it appears most frequently in the extracted list, but this is an assumption
- No checkout flow styling (Shopify Pay, Klarna, Afterpay) could be extracted despite their likely presence on a phone-case e-commerce site
