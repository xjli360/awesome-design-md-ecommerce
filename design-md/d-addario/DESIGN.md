---
version: alpha
name: "D'Addario"
source_url: "https://www.daddario.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, resonant #303030 ink anchors D'Addario's digital presence, a near-black that reads as serious and tactile — the color of a guitar fretboard or a piano's polished ebony. Against this, #cf2027 fires as the single brand voltage, a confident red that appears on primary CTAs, sale badges, and the iconic D'Addario logo mark, signaling precision and passion in equal measure. The canvas is a clean #f7f7f7, not a clinical white, lending a warm workshop feel, while #e2e6eb and #dedede provide soft structural hairlines and card borders that keep the layout airy without sacrificing hierarchy. Product cards use a generous {rounded.sm} corner radius, softening the industrial edge of instrument hardware, while the top navigation runs full-width at 80px with a subtle bottom border in #e0e0e0, housing a search bar with {rounded.full} pill ends and a cart icon that pulses the brand red. The typography leans on a clean sans-serif system — likely a variant of Inter or a similar geometric — with display headlines at 28px and 500 weight, body copy at 16px with 1.5 line height, and button labels set in 14px semibold. A secondary green (#1f3521) surfaces in environmental messaging and sustainability badges, while #289551 appears in success states and "in stock" indicators. The overall mood is that of a master luthier's workshop translated into a clean, high-fidelity e-commerce experience: every component feels machined, tested, and ready to perform.

colors:
  primary: "#cf2027"
  primary-active: "#a3191f"
  primary-disabled: "#f0b3b6"
  ink: "#303030"
  body: "#2c2c2c"
  muted: "#707070"
  muted-soft: "#aaaaaa"
  hairline: "#e0e0e0"
  hairline-soft: "#e2e6eb"
  canvas: "#f7f7f7"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#289551"
  success-soft: "#e8f5e9"
  environmental: "#1f3521"
  badge-red: "#d12121"
  badge-orange: "#cc6328"
  footer-bg: "#231f20"
  footer-text: "#eceaea"

typography:
  display-xl:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.28px
  display-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: -0.22px
  title-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.22px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.28px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.24px
    textTransform: uppercase
  link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.14px

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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 16px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    padding: 11px 15px
  text-input-error:
    border: "1px solid {colors.primary}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(48,48,48,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sustainability:
    backgroundColor: "{colors.environmental}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    height: 400px
  hero-banner-overlay:
    backgroundColor: "rgba(48,48,48,0.4)"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    color: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-panel:
    padding: "{spacing.base} {spacing.lg}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    width: 44px
    height: 44px
  cart-icon:
    color: "{colors.ink}"
    height: 24px
  cart-icon-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with D'Addario red (#cf2027) and white uppercase label. On hover, it deepens to #a3191f with no border shift — the color darkens enough to signal action without needing an outline. Disabled state drops to a pale pink (#f0b3b6) that reads as inactive but still legible. Used for "Add to Cart," "Checkout," and primary form submissions.

**`button-secondary`** — A white button with a 1px #e0e0e0 border and ink text, used for "Learn More," "View Details," and secondary checkout actions. Active state fills the background with #f3f3f3 and darkens the border to #707070. The uppercase 14px semibold label matches the primary button's typography, keeping the pair visually balanced.

**`button-tertiary`** — A text-only button in brand red, used for "Cancel," "Clear Filters," and inline "Shop Now" links within content cards. No background or border — just the red text on hover underlines to reinforce clickability.

### Cards
**`product-card`** — A white card with a soft #e2e6eb border and 8px corner radius. The image sits flush to the top edges (rounded top corners only), followed by the product name in 16px semibold and the price in 16px regular. On hover, the border shifts to #e0e0e0 and a subtle 4px shadow lifts the card — no dramatic elevation, just enough to feel selectable. Badges (sale, new, sustainability, out-of-stock) pin to the top-left of the image area with 4px rounded corners and uppercase 11px bold labels.

### Navigation
**`nav-bar`** — A full-width white bar at 80px height with a 1px #e0e0e0 bottom border. The D'Addario logo sits left, primary nav links (Strings, Accessories, Parts, Artists, Support) run center, and the search icon + cart icon sit right. Active nav links show a 2px red bottom border and red text. On scroll, the bar gains a subtle shadow (0 2px 8px rgba(48,48,48,0.06)) to separate from content.

### Forms
**`text-input`** — A white input field with 1px #e0e0e0 border, 8px radius, and 48px height. On focus, the border doubles to 2px and turns brand red — no outline ring, just the thickened border. Error state swaps the border to red immediately. Placeholder text is #aaaaaa. Used for search, email signup, and checkout fields.

**`select-input`** — Matches text-input dimensions and border treatment, with a custom dropdown arrow in #707070. The selected value appears in ink, while unselected options show in muted gray.

### Footer
**`footer`** — A deep near-black (#231f20) section with light gray text (#eceaea) at 14px. Links are 14px medium weight and turn white on hover. The footer contains four columns: Product categories, Support links, Company info, and a newsletter signup form. Social media icons appear in the bottom bar, separated by a 1px #2b2b2b hairline. The newsletter input matches the text-input style but with a white border on the dark background.

### Badges
**`badge-sale`** — Red (#d12121) pill with white uppercase text, pinned to product card images. 4px radius, 2px vertical padding, 8px horizontal. Appears for discounted items.

**`badge-new`** — Green (#289551) pill for new arrivals. Same shape and typography as sale badge.

**`badge-sustainability`** — Dark green (#1f3521) pill for eco-friendly or recycled-material products. Same shape.

**`badge-out-of-stock`** — Gray (#aaaaaa) pill for unavailable items. Same shape.

### Accordion
**`accordion`** — White background with a 1px #e2e6eb bottom border separating each item. The header uses 16px semibold with a chevron icon that rotates on expand. Panel content pads at 16px left/right and 24px top/bottom. Used for product descriptions, specs, and FAQ sections.

### Quantity Selector
**`quantity-selector`** — A horizontal 44px-tall control with a 1px #e0e0e0 border and 8px radius. Minus and plus buttons are 44px squares with #f3f3f3 background, flanking a centered numeric display. Used on product detail pages and cart.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack full-width; hero banner reduces to 240px height; footer stacks to single column; search bar moves to expandable overlay |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links only; footer shows two columns; hero banner at 320px; search bar remains visible but compact |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; four-column footer; hero banner at 400px; search bar full-width in nav |
| Wide | > 1440px | Max-width container at 1440px, centered; product grid expands to four columns; hero banner at 480px with parallax effect |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Nav hamburger icon is 48px × 48px tap area
- Quantity selector buttons are 44px × 44px
- Product card tap targets (title, price, image) are full-card-width

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Product filters collapse to a slide-out drawer on mobile
- Footer columns collapse to a single stacked column below 744px
- Hero banner text overlay collapses to a single headline on mobile (secondary text hidden)
- Accordion panels are used on mobile to collapse product specs and descriptions

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Font family not confirmed**: The extracted `font-family` declarations returned only `inherit` and `monospace`, which are likely fallbacks. The actual brand font (possibly Inter, Open Sans, or a custom D'Addario typeface) could not be determined. The typography block uses Inter as a reasonable approximation based on the brand's clean, geometric aesthetic.
- **Hover states**: While some hover behaviors are inferred (button darkening, card shadow lift), exact transition durations and easing curves were not extracted. Assumed 200ms ease-in-out.
- **Error and validation styling**: Error message colors, iconography, and form validation patterns were not observed. Red (#cf2027) is used for error borders by convention.
- **Dark mode**: No dark mode variant was detected. The footer's #231f20 background may hint at a potential dark mode palette, but it's not confirmed.
- **Sub-brand palettes**: D'Addario owns multiple brands (Evans, Planet Waves, Promark, etc.) that may have distinct color systems. Only the parent D'Addario palette is captured here.
- **Animation and motion**: Micro-interactions (loading spinners, page transitions, hover animations) were not extracted. The brand likely uses subtle transitions given its clean aesthetic.
- **Checkout widget colors**: The extracted color list includes several grays (#6b7280, #f9fafb, #f8f8f8) that may belong to Shopify's default checkout or third-party payment widgets (Klarna, Afterpay). These were excluded from the primary palette.
- **Stock image tones**: Some extracted colors (#dfd5c4, #eceaea) may be dominant tones from product photography rather than design system tokens. They appear in the footer text color but are flagged as uncertain.
