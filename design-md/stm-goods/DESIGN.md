---
version: alpha
name: "STM Goods"
source_url: "https://www.stmgoods.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A bag and case brand that uses a sharp orange (#ff671b) as its primary voltage — not as a playful accent but as a serious signal of durability and utility, appearing on CTAs, sale badges, and the brand's "DuraShock" drop-protection iconography. The palette is otherwise restrained: a warm near-black (#231f20) for ink, a cool medium gray (#727272) for body text, and a soft off-white (#f9fafb) for the canvas, with a secondary teal (#108474) used sparingly for eco-friendly product lines and sustainability callouts. Typography relies on Libre Franklin for headings and Nunito Sans for body, both geometric sans-serifs that read as modern and functional rather than fashion-forward. Product cards use a subtle {rounded.sm} corner radius and a light gray (#eeeeee) background that separates them from the white page without casting a shadow, keeping the focus on the product photography. The site's most distinctive structural move is the "DuraShock" badge — a small orange pill with white text that sits on product images, using {rounded.full} and the primary orange, signaling impact protection before the user reads a single spec. Navigation is a minimal two-row affair: utility links (search, account, cart) in a thin top strip, then the main category row with drop-downs. The overall feel is industrial but clean — a brand that sells protective gear for devices and trusts orange to do the work of reassurance.

colors:
  primary: "#ff671b"
  primary-active: "#cf3f02"
  primary-disabled: "#f58720"
  ink: "#231f20"
  body: "#727272"
  muted: "#7b7b7b"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#f9fafb"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#108474"
  accent-yellow: "#fbcd0a"
  accent-blue: "#3086c8"
  accent-red: "#ee3b45"
  accent-green: "#279a4b"
  accent-purple: "#a89cc8"
  star-rating: "#fbcd0a"
  badge-sale: "#ff671b"
  badge-eco: "#108474"
  badge-new: "#3086c8"

typography:
  display-xl:
    fontFamily: "'Libre Franklin', 'Helvetica', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Libre Franklin', 'Helvetica', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Libre Franklin', 'Helvetica', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Libre Franklin', 'Helvetica', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', 'Helvetica', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', 'Helvetica', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Helvetica', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Helvetica', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', 'Helvetica', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', 'Helvetica', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
  micro-label:
    fontFamily: "'Nunito Sans', 'Helvetica', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
  button-md:
    fontFamily: "'Libre Franklin', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Libre Franklin', 'Helvetica', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.4px
  link:
    fontFamily: "'Nunito Sans', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Libre Franklin', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  nav-link-utility:
    fontFamily: "'Nunito Sans', 'Helvetica', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px

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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-pill-orange:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
  nav-bar-utility:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link-utility}"
    height: 32px
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.body-md}"
    color: "{colors.accent-red}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 8px
  product-card-badge-eco:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 8px
  product-card-badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 8px
  product-card-rating:
    color: "{colors.star-rating}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: 64px 24px
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    color: "{colors.canvas}"
    typography: "{typography.title-sm}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: 16px
  accordion-content:
    padding: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 40px
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: 16px 0
    border-bottom: "1px solid {colors.hairline}"
  cart-total:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 24px
    height: 48px
  checkout-button-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Shop Now", and "Explore" actions. Uses the brand's signature orange (#ff671b) on a white background with a subtle {rounded.xs} corner. On hover, shifts to a deeper burnt orange (#cf3f02). Disabled state uses a lighter orange (#f58720) to indicate unavailability while maintaining brand consistency.

**`button-secondary`** — An outlined alternative for less prominent actions like "Learn More" or "View Details". Uses a 2px solid ink border on a transparent background, with the same {rounded.xs} radius. Active state fills the background with the soft surface gray (#eeeeee). Works well on both white and light gray backgrounds.

**`button-tertiary-text`** — A text-only button for inline actions like "Read Reviews" or "See Specifications". Uses the primary orange for the text color with no background or border, keeping the UI clean while maintaining the brand's orange voltage.

**`button-pill-orange`** — A compact, fully rounded pill used for product badges (e.g., "DuraShock", "Sale") and small promotional tags. The {rounded.full} shape and tight padding (8px 16px) make it sit comfortably on product images without overwhelming the photography.

### Cards
**`product-card`** — The primary product display unit on collection pages and search results. Uses a light gray background (#eeeeee) to create visual separation from the white page without relying on shadows. The {rounded.sm} corner is subtle enough to feel industrial but soft enough to avoid harshness. Product images sit within the card with the same radius.

**`product-card-badge`** — A small orange pill overlaid on product images to signal key attributes. Three variants exist: orange for "DuraShock" and sale items, teal (#108474) for eco-friendly products, and blue (#3086c8) for new arrivals. Each uses {rounded.full} and the {typography.badge} font size (11px bold) for legibility at small scales.

### Navigation
**`nav-bar`** — The main navigation header at 80px height on a white background. Contains the brand logo, primary category links (Cases, Bags, Accessories, etc.) in Libre Franklin 14px semibold, and a search icon. Links use the ink color (#231f20) with no underline — active state is indicated by a subtle orange underline or bold weight.

**`nav-bar-utility`** — A thin 32px strip above the main nav for utility links (Search, Account, Cart, Currency Selector). Uses the soft surface gray (#eeeeee) background with muted text (#7b7b7b) in Nunito Sans 12px medium. This secondary strip keeps the main nav clean while providing access to account and cart functions.

**`nav-dropdown`** — A white dropdown panel that appears on hover over category links. Uses {rounded.sm} corners and 8px vertical padding for link spacing. Links are 14px semibold in Libre Franklin, matching the nav-link typography.

### Forms
**`text-input`** — Standard text input for search, newsletter signup, and checkout forms. Uses a 1px hairline border (#dedede) on a white background with {rounded.xs} corners. On focus, the border thickens to 2px and shifts to the primary orange (#ff671b). Error state uses a 2px red (#ee3b45) border.

**`select-input`** — Dropdown selectors for product options (size, color, quantity) and address forms. Matches the text-input styling with the same dimensions and border treatment. The dropdown arrow uses the ink color.

**`search-bar`** — A fully rounded search input ({rounded.full}) used in the navigation and mobile search overlays. Uses a 1px hairline border on a white background with 10px vertical padding. On focus, the border becomes 2px orange. The pill shape differentiates search from other form inputs and signals its utility function.

### Footer
**`footer`** — A dark footer section using the ink color (#231f20) as background with white text. Contains link columns, social media icons, and legal text. Links use the muted-soft gray (#aaaaaa) to reduce visual weight against the dark background. Headings are white in Nunito Sans 16px bold. Padding of 48px top and bottom provides breathing room.

**`footer-link`** — Footer navigation links in 14px Nunito Sans regular, colored in muted-soft gray (#aaaaaa) on the dark background. Hover state shifts to white for clarity.

### Cart & Checkout
**`cart-item`** — Individual line items in the cart drawer or page. Uses a white background with a 1px hairline bottom border for separation. Each item shows the product image, title, selected options, quantity selector, and price. The layout is clean and minimal, letting the product photography do the work.

**`quantity-selector`** — A compact control for adjusting item quantities in the cart. Uses a 1px hairline border with {rounded.xs} corners. The decrement and increment buttons use the soft surface gray background to visually separate them from the quantity display.

**`checkout-button`** — The primary checkout action, styled identically to `button-primary` but with a slightly taller height (48px) to accommodate the checkout flow. Uses the full primary orange with white text and {rounded.xs} corners.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; search bar moves to overlay; footer links collapse into accordions; hero banner reduces padding to 32px |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories with dropdowns; search bar remains in header but shrinks width; footer shows two-column link layout |
| Desktop | 1128–1440px | Full three-to-four-column product grid; complete nav with all categories visible; search bar at full width in utility strip; footer shows four-column link layout |
| Wide | > 1440px | Max-width container (1440px) centered; product grid expands to five columns; all elements at maximum comfortable size |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card tap targets are the full card area, not just the title or price
- Mobile nav hamburger icon is 44x44px with adequate padding
- Quantity selector buttons are 40x40px minimum
- Accordion headers in mobile footer are 44px tall for easy tapping

### Collapsing Strategy
- Main navigation collapses to a hamburger menu below 744px, with a slide-out drawer showing all categories and utility links
- Product filters collapse to a "Filter" button that opens a modal overlay on mobile
- Footer link columns collapse to accordion panels on mobile, with the first panel open by default
- Product image galleries collapse to a single-image carousel with dot indicators on mobile
- Multi-column product grids collapse to single column on mobile, two columns on tablet

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (especially nav links, footer links, and product card interactions) could not be reliably extracted — the site may use underline, color shift, or shadow changes that weren't visible in static extraction
- Error state styling for form validation (beyond the red border noted) is unknown — error messages, iconography, and animation timing are not captured
- The extracted color list includes many grays and neutrals that may be framework defaults or stock image tones — the true brand palette likely uses fewer colors than listed, but the most distinctive (orange #ff671b, teal #108474, and near-black #231f20) are confirmed as intentional
- Font weights for Libre Franklin and Nunito Sans beyond 400, 500, 600, and 700 are unknown — the site may use 300 or 800 weights for specific applications
- Dark mode styling is not present in the extracted data — the site appears to be light-mode only
- Animation and transition timing (hover effects, dropdown animations, cart drawer slide-in) are not captured
- The "DuraShock" badge and other product-specific iconography may have custom SVG or icon font implementations not reflected in the component tokens
- Sub-brand or collection-specific color variations (e.g., limited edition colors, collaboration palettes) are not captured
- Checkout flow styling beyond the primary button is unknown — Shopify's default checkout may override some brand styling
- Mobile navigation drawer animation and overlay behavior (slide direction, scrim opacity, close button placement) could not be determined from static extraction
