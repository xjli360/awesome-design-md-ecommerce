---
version: alpha
name: "GUND"
source_url: "https://gund.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A century-old plush brand that wraps its animals in a warm, muted palette anchored by #4f4b47 (a soft, warm charcoal) and #fcfaf9 (a cream-white canvas that feels like vintage cotton rather than sterile digital white). The brand’s signature voltage comes from #cb2c30, a deep crimson that appears on bows, tags, and accent details — never overwhelming the plush, always signaling gift-worthiness. Typography runs Montserrat across the system, a geometric sans-serif that balances the softness of the product with clean, legible structure. Product cards use generous whitespace and soft {rounded.lg} corners, letting the photographed animals — with their embroidered eyes and varied textures — do the emotional work. The navigation bar sits at a compact height with a centered logo, and the primary CTA appears as a solid #cb2c30 rectangle with white text, echoing the brand’s gift-box heritage. Secondary actions use a #fcfaf9 fill with #4f4b47 text, keeping the interface calm and approachable. The footer stacks links in a narrow column, with a #f3f3f3 background that gently separates it from the product grid. Throughout, the system avoids hard edges: buttons, cards, and search bars all carry {rounded.sm} to {rounded.lg} radii, creating a world where every corner feels as soft as the product inside.

colors:
  primary: "#cb2c30"
  primary-active: "#b02528"
  primary-disabled: "#e4a5a7"
  ink: "#4f4b47"
  body: "#3d4246"
  muted: "#777777"
  muted-soft: "#a0a0a0"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#fcfaf9"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#f3e2d0"
  accent-blush: "#e4c6be"
  accent-sage: "#dde5ed"
  accent-stone: "#dbc0a7"
  badge-red: "#d02c2f"
  link-blue: "#007bed"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
    padding: 11px 26px
    height: 48px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
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
    border: "2px solid {colors.badge-red}"
    padding: 11px 15px
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
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
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
    padding: 9px 19px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
    aspectRatio: "1 / 1"
    objectFit: "contain"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "0 {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: "top-left"
  hero-banner:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.none}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  footer-heading:
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    textTransform: uppercase
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base}"
  accordion-content:
    padding: "0 {spacing.base} {spacing.base}"
  breadcrumb:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
    fontWeight: 600
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
  pagination-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    padding: "8px 12px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "0 12px"
  rating-stars:
    color: "{colors.ink}"
    size: 16px
  wishlist-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
  wishlist-button-active:
    textColor: "{colors.primary}"
  social-icon:
    textColor: "{colors.muted}"
    size: 24px
  social-icon-hover:
    textColor: "{colors.primary}"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
    height: 56px
  checkout-button-active:
    backgroundColor: "{colors.primary-active}"
  checkout-button-disabled:
    backgroundColor: "{colors.primary-disabled}"
  cart-badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  promo-banner:
    backgroundColor: "{colors.accent-blush}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Shop Now", and checkout flows. Renders as a solid #cb2c30 rectangle with white uppercase Montserrat text and {rounded.sm} corners. On hover, shifts to `button-primary-active` (#b02528). Disabled state uses `button-primary-disabled` (#e4a5a7) with reduced opacity cursor.

**`button-secondary`** — Used for "View Details", "Learn More", and secondary checkout options. White fill with #4f4b47 text and a subtle 1px hairline border. On hover, the border darkens to #3d4246. Disabled state uses #dedede border with #a0a0a0 text.

**`button-secondary-outline`** — An outlined variant for "Wishlist" and "Compare" actions. Transparent background with a 2px #4f4b47 stroke. On hover, fills with #f3f3f3 background. Disabled state uses #dedede stroke.

**`button-pill-primary`** — A compact, fully rounded pill used for "Sale" badges, filter chips, and promotional tags. Uses the same #cb2c30 fill but with smaller typography and tighter padding to fit inline contexts.

### Navigation
**`nav-bar`** — A fixed-position top bar at 64px height with a white background and subtle bottom border. Contains the centered GUND logo, a hamburger menu (mobile), and links for "Shop", "About", "Gift Guide", and "Sale". The active link uses `nav-link-active` with #cb2c30 text; inactive links use `nav-link-inactive` with #777777 text.

**`nav-bar-sticky`** — A condensed 56px variant that appears on scroll. Drops the bottom border in favor of a soft box-shadow. All typography remains the same but padding compresses slightly.

**`search-bar`** — A pill-shaped search input with #f3f3f3 background and #dedede border. On focus, the border thickens to 2px and shifts to #cb2c30. Placeholder text uses #a0a0a0. Includes a magnifying glass icon on the left.

### Cards
**`product-card`** — A white card with {rounded.lg} corners containing a square product image (1:1 aspect ratio, object-fit: contain) and text details below. The image area has rounded top corners only. On hover, the card lifts with a subtle box-shadow. The title uses `product-card-title` (16px, 600 weight) and the price uses `product-card-price` (16px, 600 weight in #3d4246).

**`product-card-badge`** — A small red (#d02c2f) badge positioned at the top-left of the product image. Used for "New", "Sale", or "Best Seller" labels. White uppercase text at 11px with {rounded.xs} corners.

### Forms
**`text-input`** — Standard form input with white background, 1px #dedede border, and {rounded.sm} corners. On focus, the border becomes 2px #cb2c30. Error state uses 2px #d02c2f border. Includes a label above using `caption` typography.

**`select-input`** — Dropdown selector matching the text-input styling. Includes a custom chevron icon in #777777. On focus, the border matches the primary color.

**`quantity-selector`** — A compact horizontal control with minus/plus buttons flanking a numeric display. Uses {rounded.sm} corners and a 1px hairline border. Buttons are transparent with #4f4b47 text, and the numeric display uses `body-md` typography.

### Footer
**`footer`** — A full-width section with #f3f3f3 background, containing columns of links organized by category (Shop, About, Support, Connect). Each column has an uppercase heading in `footer-heading` and links in `footer-link`. On hover, links turn #cb2c30. The bottom of the footer includes copyright text in `caption-sm` typography.

**`accordion`** — Used on mobile for footer link groups and FAQ sections. A white card with 1px #dedede border and {rounded.sm} corners. The header is clickable and toggles the content area with a smooth height transition. The header includes a plus/minus icon in #777777.

### Badges & Indicators
**`cart-badge`** — A small red circle (#d02c2f) with white text, positioned on the cart icon in the nav bar. Displays the item count. Uses {rounded.full} for a perfect circle shape.

**`promo-banner`** — A full-width banner at the top of the page (above the nav bar) with #e4c6be background and centered text. Used for free shipping announcements, holiday promotions, and site-wide sales. Text uses `caption` typography in #4f4b47.

**`rating-stars`** — Five 16px star icons in #4f4b47, used on product cards and detail pages. Empty stars use #dedede. Half-star support is available for fractional ratings.

### Pagination
**`pagination`** — A horizontal row of page numbers and arrow buttons. The active page uses `pagination-active` with a #cb2c30 background and white text. Inactive pages use `pagination-inactive` with #777777 text. Arrow buttons use #4f4b47 text and are disabled (grayed out) at the first/last page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 col), hamburger nav, accordion footer, search bar collapses to icon, hero banner stacks vertically |
| Tablet | 744–1128px | Two-column product grid (2 col), full nav links visible, footer expands to 2-column layout, search bar expands to full width |
| Desktop | 1128–1440px | Three-column product grid (3 col), full nav with dropdowns, footer in 4-column layout, hero banner uses full width with text overlay |
| Wide | > 1440px | Four-column product grid (4 col), max-width container at 1440px, hero banner constrained to container width, extra whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum touch target of 44x44px.
- Product card images are fully tappable, linking to the product detail page.
- Quantity selector buttons are 44px wide to accommodate thumb taps.
- Accordion headers have 48px tap height for easy toggling.
- Nav bar links have 44px tap height on mobile.

### Collapsing Strategy
- On mobile (< 744px), the nav bar collapses to a hamburger menu with a slide-out drawer containing all links.
- The footer accordion collapses link groups into expandable sections on mobile, saving vertical space.
- Product filters collapse into a single "Filter" button that opens a modal overlay.
- The search bar collapses to a magnifying glass icon that expands to a full-width input on tap.
- The hero banner text and CTA stack below the image on mobile, rather than overlaying it.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow depth, scale) not extracted — assumed standard lift effect.
- Error and success states for form validation (inline messages, iconography) not observed.
- Dark mode or high-contrast mode not present on the live site.
- Sub-brand or seasonal color palettes (e.g., holiday, collaboration) not captured.
- Animation timing and easing curves (transitions, hover effects) not extracted.
- Focus ring styles for keyboard navigation not observed.
- Modal and overlay component styles (cart drawer, quick view) not extracted.
- Loading states (skeleton screens, spinners) not present in extracted data.
- The extracted color list includes several Shopify checkout and payment widget colors (#007bed, #334fb4, #5a5b5b) that are not part of the GUND brand system — these have been excluded from the palette.
- Font weights beyond 400, 500, 600, 700 not confirmed — Montserrat variable font may support intermediate weights.
- Letter-spacing values for body text are estimated based on common e-commerce patterns; exact values not extracted.
- The `object-fit: contain` declaration was found on product images but aspect ratio values are inferred.
