---
version: alpha
name: "Kinesis"
source_url: "https://kinesis-ergo.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep blue #3858e9 anchors a brand built for hands that never stop moving — this is the primary voltage that drives every CTA, product-highlight badge, and navigation accent across kinesis-ergo.com. The palette leans heavily on a near-black #1e1e1e for body text and a warm off-white #fafafa for canvas, creating a high-contrast reading environment suited to technical product specifications and ergonomic research. Red #cc1818 appears as a deliberate alert accent, used sparingly on sale badges and error states, while #4ab866 provides a secondary green for "in stock" indicators and positive confirmations. Typography runs a two-family system: Proxima Nova for body and interface copy at 16px with 1.5 line-height, and League Gothic for display headlines that set a condensed, industrial tone at 32px and 700 weight. Buttons are sharp-cornered rectangles with 8px rounding ({rounded.sm}), 48px height, and the primary blue filling the full background — no outline, no gradient, no pill shape. Product cards use a white surface ({rounded.md}) with a thin #e0e0e0 hairline, 16px padding, and a 4:3 product photo above the fold. The top navigation is a fixed 80px bar with the brand logo left-aligned, a centered product-family dropdown, and a right-aligned search icon and cart count badge in #cc1818. The overall feel is utilitarian and medical-device precise: high contrast, minimal decoration, generous vertical spacing ({spacing.section} at 64px between major sections), and a typographic hierarchy that prioritizes legibility over personality.

colors:
  primary: "#3858e9"
  primary-active: "#183ad6"
  primary-disabled: "#abb8c3"
  ink: "#1e1e1e"
  body: "#32373c"
  muted: "#757575"
  muted-soft: "#949494"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#fafafa"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#cc1818"
  accent-green: "#4ab866"
  accent-blue: "#4a8eff"
  accent-orange: "#ff6900"
  accent-yellow: "#fcb900"
  stock-badge: "#4ab866"
  sale-badge: "#cc1818"
  cart-count: "#cc1818"

typography:
  display-xl:
    fontFamily: "'league-gothic', 'Impact', 'Arial Black', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'league-gothic', 'Impact', 'Arial Black', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'league-gothic', 'Impact', 'Arial Black', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.2px
  badge:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-danger:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-active:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "4:3"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  badge-stock:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
  search-icon:
    textColor: "{colors.muted}"
    height: 20px
  cart-icon:
    textColor: "{colors.ink}"
    height: 24px
  cart-count-badge:
    backgroundColor: "{colors.cart-count}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-section-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.md}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.base}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 720px
  hero-subheadline:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: 560px
    marginTop: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. Filled with #3858e9 (`{colors.primary}`), white text, and 8px rounding (`{rounded.sm}`). On hover or active, shifts to #183ad6 (`{colors.primary-active}`). Disabled state uses #abb8c3 (`{colors.primary-disabled}`) with white text. Height is fixed at 48px with 14px top/bottom and 28px left/right padding. Used for "Add to Cart", "Shop Now", and primary form submissions.

**`button-secondary`** — Outline variant for secondary actions. White background (`{colors.canvas}`) with #3858e9 text and a 2px solid border matching the primary color. Active state fills with #f0f0f0 (`{colors.surface-soft}`) and shifts text to #183ad6. Same 48px height and 8px rounding as primary. Used for "Learn More", "Compare Models", and secondary form actions.

**`button-tertiary-text`** — Text-only button with no background or border. Uses #3858e9 text at 16px/600 weight. Hover state adds underline. Used for "View Details", "Cancel", and inline navigation links.

**`button-danger`** — Destructive action button filled with #cc1818 (`{colors.accent-red}`), white text, same 48px height and 8px rounding. Used for "Remove from Cart", "Delete Account", and irreversible actions.

### Text Inputs
**`text-input`** — Standard form input with white background, 48px height, 12px/16px padding, and 8px rounding. Border is 1px solid #e0e0e0 (`{colors.hairline}`). On focus, border switches to #3858e9 with a 2px blue box-shadow ring. Placeholder text uses #949494 (`{colors.muted-soft}`). Used for search, email signup, and checkout forms.

**`select-input`** — Dropdown select styled identically to text inputs: 48px height, 8px rounding, same border and focus states. Chevron icon uses #757575 (`{colors.muted}`). Used for product filtering (sort by, category, layout options).

### Navigation
**`nav-bar`** — Fixed top navigation bar, 80px height, white background, with a subtle 1px bottom border in #e0e0e0. On scroll, adds a light box-shadow (`0 1px 3px rgba(0,0,0,0.08)`). Logo sits left-aligned at 180px width. Product family dropdowns appear centered with 15px/500 weight type. Right side houses search icon and cart icon with count badge.

**`nav-link`** — Top-level navigation links at 15px/500 weight. Default color is #1e1e1e (`{colors.ink}`). Hover state adds a 2px bottom border in #3858e9. Active/current page uses #3858e9 text color. Dropdown menus appear on hover with white background, 8px rounding, and 4px top offset.

### Product Cards
**`product-card`** — White card with 12px rounding (`{rounded.md}`), 16px padding, and a 1px #e0e0e0 border. Product image occupies the top portion at a 4:3 aspect ratio with 8px rounding. Title uses 18px/600 weight (`{typography.title-md}`) with 8px top margin. Price sits below in 14px/400 weight at #757575 (`{colors.muted}`). Hover state lifts the card with a subtle translateY(-2px) and increased box-shadow.

**`badge-stock`** — Green badge (#4ab866) with white uppercase 11px/700 type, 2px/8px padding, and 4px rounding. Positioned top-left on product card images. Indicates "In Stock" or "Ready to Ship".

**`badge-sale`** — Red badge (#cc1818) with same styling as stock badge. Indicates "Sale" or "Clearance" pricing.

**`badge-new`** — Blue badge (#4a8eff) with same styling. Indicates "New Arrival" or "Recently Added" products.

### Search
**`search-bar`** — Pill-shaped search field with #f0f0f0 background, 44px height, 10px/20px padding, and full rounding (`{rounded.full}`). Search icon (#757575) sits left-aligned at 20px. Placeholder text reads "Search products..." in #949494. On focus, background shifts to white with a 2px #3858e9 border ring.

**`cart-count-badge`** — Small circular badge (#cc1818) with white 12px/500 type, 18px height, and minimum 18px width. Positioned top-right of the cart icon. Displays the number of items in the cart.

### Footer
**`footer-section-title`** — Section headers in the footer at 18px/600 weight with 24px bottom margin. Links below use 16px/400 weight at #757575 (`{colors.muted}`) with 8px vertical spacing between items. Hover state shifts link color to #3858e9. The footer background uses #fafafa (`{colors.canvas}`) with a 1px #e0e0e0 top border and 48px top padding.

### Hero
**`hero-section`** — Full-width hero banner with white background, 64px vertical padding, and 16px horizontal padding. Headline uses 48px League Gothic at 700 weight with -0.5px letter spacing, capped at 720px width. Subheadline uses 16px/400 weight Proxima Nova at #32373c (`{colors.body}`), capped at 560px width with 24px top margin. A primary CTA button sits below with 32px top margin.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically at full width; hero headline drops to 32px; search bar moves to mobile drawer; footer links stack in single column |
| Tablet | 744–1128px | Two-column product grid; nav shows condensed links (no dropdowns); hero headline at 40px; search bar remains visible but narrower; footer uses 2-column grid |
| Desktop | 1128–1440px | Full nav with dropdowns; three-column product grid; hero at full width; search bar at 360px max-width; footer uses 4-column grid |
| Wide | > 1440px | Max-width container at 1440px centered; product grid expands to 4 columns; hero content max-width scales proportionally; nav remains unchanged |

### Touch Targets
- All buttons and interactive elements minimum 44px height (48px standard)
- Search icon and cart icon minimum 44x44px tap area
- Nav links minimum 40px tap height
- Product card tap target covers entire card surface
- Footer links minimum 36px tap height

### Collapsing Strategy
- Top nav collapses to hamburger menu at < 744px; dropdown menus become accordion panels in mobile drawer
- Product grid collapses from 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile)
- Hero section reduces headline size and centers content on mobile
- Footer collapses from 4 columns → 2 columns (tablet) → 1 column (mobile)
- Search bar collapses to icon-only on mobile, expanding to full-width on tap
- Cart count badge remains visible at all breakpoints

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be reliably extracted from static CSS; active/disabled states are inferred from common patterns
- Error styling for form validation (red borders, error messages) was not present in extracted data; #cc1818 is assumed for error borders based on its use as alert accent
- Dark mode or high-contrast mode variants are not documented; the site appears to ship light-mode only
- Sub-brand or product-line-specific palettes (Advantage, Freestyle, etc.) may exist but were not captured
- Animation and transition timing values (durations, easing curves) were not extractable
- Dropdown menu exact dimensions, padding, and shadow values are estimated from common patterns
- The extracted font list includes system fallbacks and multiple sans-serif options; Proxima Nova and League Gothic are assumed as primary based on their presence in the list and brand context, but exact font weights and sizes are inferred from common usage patterns
- Checkout flow components (payment forms, address inputs) were not analyzed; Shopify Pay and other widget colors may appear in the extracted palette but are not part of the Kinesis design system
- Icon set details (SVG vs icon font, exact stroke widths, sizes) were not extractable
- Print stylesheet behavior is unknown
