---
version: alpha
name: "Electric & Rose"
source_url: "https://www.electricandrose.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A coastal lifestyle brand that builds its visual identity on a foundation of crisp whites (#fafafa) and soft warm beiges (#faf4e8), punctuated by a signature red (#bc0000) that appears in primary calls-to-action, sale badges, and accent lines — a deliberate voltage against an otherwise airy, sun-bleached palette. The brand name itself suggests a duality: the electric charge of that red against the organic, rose-tinted softness of its supporting tones (#f9d3d3, #ffeae8, #fdd0d0). Typography leans on Arapey, a serif with genuine italic character, for display moments — a choice that reads as hand-lettered and personal rather than corporate. The extracted hex list reveals a brand that lives in the neutral zone (a dozen shades of gray from #d5d5d5 to #1e1e1e) but refuses to be boring, using that red as a consistent exclamation point. A secondary green (#007f5f) with its own soft halo (#e5fff8) suggests an eco-conscious or botanical sub-brand layer, possibly for sustainability messaging or collection drops. The Shopify platform backbone means product cards, collection grids, and cart drawers follow a familiar ecommerce rhythm, but the brand's visual choices — the serif type, the blush-toned surfaces, the restrained use of high-saturation color — push toward a boutique editorial feel rather than a volume-driven marketplace.

colors:
  primary: "#bc0000"
  primary-active: "#c60808"
  primary-disabled: "#f9d3d3"
  ink: "#222222"
  body: "#313131"
  muted: "#808080"
  muted-soft: "#bababa"
  hairline: "#d5d5d5"
  hairline-soft: "#e5e5e5"
  canvas: "#fafafa"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red-soft: "#ffeae8"
  accent-green: "#007f5f"
  accent-green-soft: "#e5fff8"
  accent-warm: "#faf4e8"
  accent-rose: "#fdd0d0"

typography:
  display-xl:
    fontFamily: "'Arapey', 'Times New Roman', Times, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Arapey', 'Times New Roman', Times, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Arapey', 'Times New Roman', Times, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Arapey', 'Times New Roman', Times, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Arapey', 'Times New Roman', Times, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Arapey', 'Times New Roman', Times, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Times New Roman', Times, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Times New Roman', Times, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Times New Roman', Times, serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  button-md:
    fontFamily: "'Times New Roman', Times, serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Times New Roman', Times, serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Times New Roman', Times, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Arapey', 'Times New Roman', Times, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Times New Roman', Times, serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 0
    height: auto
  button-text-hover:
    textColor: "{colors.primary}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-sold-out:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginTop: "{spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "14px 32px"
    marginTop: "{spacing.lg}"
  collection-grid:
    gap: "{spacing.base}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "10px 24px"
    height: 44px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    width: 400px
  cart-item-title:
    typography: "{typography.title-md}"
  cart-item-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  cart-total:
    typography: "{typography.title-lg}"
    borderTop: "1px solid {colors.hairline}"
    paddingTop: "{spacing.base}"
  cart-checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "14px 32px"
    height: 48px
    width: "100%"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginBottom: "{spacing.xl}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered as a sharp rectangle with no border radius, using the signature red (#bc0000) background and white uppercase serif text. On hover, the background shifts to a slightly deeper red (#c60808). The disabled state fades to a soft rose (#f9d3d3) with muted text, signaling unavailability without visual noise. The uppercase letter-spacing (0.5px) and serif typeface give even a simple "Shop Now" button a literary, editorial weight.

**`button-secondary`** — An outlined variant on a white canvas with a 1px hairline border and ink-colored text. The active state darkens the border to the ink color and adds a soft surface background. Used for "View All" links, secondary checkout paths, and filter toggles. The sharp corners match the primary button, maintaining a consistent silhouette across the button family.

**`button-text`** — A borderless, backgroundless text button that inherits the button-md typography. On hover, the text color shifts to the primary red, creating a subtle underline-like effect without an actual underline. Used for "Read More" links, accordion toggles, and inline navigation prompts.

**`button-pill`** — A fully rounded variant reserved for newsletter signup prompts, filter chips, and mobile navigation triggers. Uses the primary red background with smaller uppercase text (button-sm). The pill shape offers a visual alternative to the brand's otherwise sharp-cornered button system, signaling a different interaction mode — more casual, more dismissible.

### Cards
**`product-card`** — A minimal product presentation with no border radius, no shadow, and no background color distinction from the page canvas. The product image sits flush to the card edges, with the title and price stacked below at tight spacing (8px between elements). A badge overlays the top-left corner of the image for sale or new-arrival indicators. The sold-out variant uses an ink-colored badge instead of red. The card's restraint lets the product photography carry the visual weight — the brand trusts its imagery, not its chrome.

**`product-card-badge`** — A small, sharp-cornered label pinned to the top-left of product images. Uses the primary red for active promotions and ink black for sold-out status. The uppercase badge typography at 11px with 0.5px letter-spacing reads as a price tag or inventory stamp rather than a promotional sticker.

### Navigation
**`nav-bar`** — A full-width white header at 72px height with a single hairline-soft bottom border. Navigation links use Arapey at 16px with generous horizontal padding (16px). The active or current page link shifts to the primary red. The bar remains fixed on scroll, providing persistent access to the brand's collection categories, search, and cart.

**`nav-link`** — A text-only navigation item with no background or border. The hover state is a color transition to the primary red, with no underline or other decoration. The link's simplicity reflects the brand's editorial approach — navigation is a table of contents, not a billboard.

### Forms
**`text-input`** — A sharp-cornered input field with a 1px hairline border and 16px horizontal padding. On focus, the border thickens visually by switching to the ink color. Error states use the primary red border. The input height (48px) matches the primary button height, allowing clean horizontal alignment in form layouts.

**`newsletter-input`** — A slightly shorter input (44px) paired with an equally tall submit button. The input uses body-sm typography and a hairline border. The submit button uses the primary red with button-sm uppercase text. The pair forms a single visual unit — the input and button touch at their shared edge, creating a seamless join.

**`search-bar`** — A full-width input with the same dimensions and styling as the text-input, but used specifically for product and content search. The focus state swaps the hairline border for an ink-colored one. No search icon is specified — the brand may use a text label or a separate icon button.

### Footer
**`footer`** — A dark inversion of the brand's light palette, using the ink color (#222222) as background and white for primary text. Links appear in muted-soft (#bababa) and shift to white on hover. The footer contains the brand's secondary navigation, social links, newsletter signup, and legal text. The dark background creates a clear visual boundary between the airy product pages and the site's conclusion.

**`newsletter-submit`** — A primary-red button at 44px height, matching the newsletter input. Uses button-sm typography. The button sits flush against the input's right edge, forming a single combined control.

### Cart
**`cart-drawer`** — A 400px-wide slide-in panel from the right side of the viewport. Uses the white canvas background with ink text. Cart items display title in title-md and price in body-md, separated by a hairline border at the total. The checkout button spans the full width of the drawer, using the primary button styling. The drawer's width accommodates product titles, quantities, and variant selectors without crowding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to display-md; buttons become full-width; cart drawer becomes full-width; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses display-lg; buttons remain inline; cart drawer at 400px |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at display-xl; standard button sizing; cart drawer at 400px |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero centered with max-width; cart drawer at 400px |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Nav links have 16px horizontal padding, creating a minimum 48px tap target width
- Product card images are tappable as entire cards, not just the title link
- Cart drawer close button is a minimum 44x44px target
- Search bar and newsletter input are 44px+ in height

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu at < 744px viewport width
- Product grid reduces from 3-4 columns to 2 columns at tablet, then 1 column at mobile
- Hero section reduces font size and padding at mobile, with the CTA becoming full-width
- Footer links stack vertically at mobile, with each link group in its own row
- Cart drawer becomes full-width on mobile, overlaying the entire viewport
- Secondary navigation (utility links like account, search) collapses into the hamburger menu at mobile
- Collection filters may collapse into a dropdown or slide-in panel at tablet and below

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for most components were inferred from the primary color shift pattern — the live site may use different transitions or effects
- Error state styling for forms (validation messages, error icons) was not extractable from the color list alone
- The secondary green (#007f5f) and its soft halo (#e5fff8) appear in the extracted colors but their specific usage context (sustainability badges, collection tags, eco-labels) is unconfirmed
- Font weights beyond the extracted Arapey and Times declarations are assumed — the live site may use additional weights or a different body font entirely
- Shadow and elevation values (box-shadow, drop-shadow) were not extractable from the color list
- The brand's logo treatment, including any SVG or image-based wordmark, is not captured in this design system
- Animation and transition timing values (durations, easing curves) are not specified
- Dark mode or high-contrast mode variants are not defined
- The extracted color list includes many near-identical grays — the exact mapping of each to specific UI elements may differ from the assignments above
- Checkout-specific styling (Shopify checkout overrides) is not included
- Social media icon colors and brand-specific iconography are not defined
- The brand's photography style guide (image ratios, filters, overlays) is not captured
