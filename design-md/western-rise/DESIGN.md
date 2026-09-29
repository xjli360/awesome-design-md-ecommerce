---
version: alpha
name: "Western Rise"
source_url: "https://westernrise.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep navy (#272d45) and slate (#848587) palette frames an outdoor apparel brand that trusts performance fabric to do the talking — the site is a quiet, functional stage for technical gear, not a mountain-scape postcard. The extracted hex list reveals a restrained system: #222222 and #121212 for ink, #f1f0ed for canvas, and a single distinctive accent in #b2f9e9 — a mint-teal that surfaces on sale badges and secondary CTAs, reading as fresh air rather than brand bombast. Typography runs Geist, a clean geometric sans that echoes the brand's "less is more" ethos; headings sit at moderate weights (500-600) and body copy at 14-16px with generous line-height, letting product photography and fabric detail carry the story. The navigation bar uses a fixed white canvas with subtle shadow, and product cards employ soft {rounded.sm} corners and minimal borders — the design trusts the product's own silhouette. A persistent "Free Shipping & Returns" banner in #2c2c2c on #f1f0ed sets a low-anxiety tone from the first scroll. The checkout flow inherits Shopify's default widget colors (#0e7a82 for a teal accent, #2c3e50 for dark sections), but the brand's own palette stays cool, neutral, and deliberately underlit — the digital equivalent of a well-packed duffel.

colors:
  primary: "#272d45"
  primary-active: "#1e2338"
  primary-disabled: "#848587"
  ink: "#222222"
  body: "#2c2c2c"
  muted: "#848587"
  muted-soft: "#d3d4dd"
  hairline: "#e5e5e5"
  hairline-soft: "#dedede"
  canvas: "#f1f0ed"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  accent-mint: "#b2f9e9"
  accent-teal: "#0e7a82"
  accent-navy-dark: "#121212"
  on-primary: "#ffffff"
  on-accent: "#121212"
  sale-badge: "#b2f9e9"
  banner-bg: "#2c2c2c"
  banner-text: "#f1f0ed"
  star-rating: "#272d45"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Geist', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Geist', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Geist', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "'Geist', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Geist', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Geist', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Geist', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Geist', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Geist', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Geist', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Geist', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Geist', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Geist', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  link:
    fontFamily: "'Geist', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  nav-link:
    fontFamily: "'Geist', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  price:
    fontFamily: "'Geist', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  price-sale:
    fontFamily: "'Geist', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
    textDecoration: line-through

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
  button-accent:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "3:4"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
    color: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  banner-top:
    backgroundColor: "{colors.banner-bg}"
    textColor: "{colors.banner-text}"
    typography: "{typography.caption}"
    height: 36px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
  footer-link-hover:
    color: "{colors.accent-mint}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 40px
  size-selector-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: "14px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Shop Now", and checkout entry points. Rendered in deep navy (#272d45) with white text and a subtle 4px corner radius. On hover, shifts to a darker navy (#1e2338). The disabled state drops to slate (#848587), signaling unavailability without visual noise. Padding is generous at 12px 24px, giving the button a solid, tactile presence that matches the brand's durable product positioning.

**`button-secondary`** — An outlined or canvas-toned alternative for secondary actions like "Learn More" or "View Details". Uses the same typography and height as the primary button but with a canvas background (#f1f0ed) and ink text (#222222), keeping the visual hierarchy flat and approachable. Active state inverts to primary navy.

**`button-accent`** — Reserved for promotional or sale-related CTAs, surfaced in the mint-teal accent (#b2f9e9) with dark text (#121212). Used sparingly — typically on sale badges, limited-time banners, or clearance sections — to create a moment of visual relief against the predominantly cool palette.

**`button-text`** — A borderless, backgroundless link-style button for actions like "Clear Filters" or "Cancel". Uses primary navy text on hover, with no padding beyond the text itself.

### Cards
**`product-card`** — The core product display unit, used on collection pages, search results, and related-product grids. A white card with a 3:4 aspect-ratio product image, soft 4px rounding, and minimal spacing between image and text. The title sits in 16px medium weight, price in 16px semibold, and sale prices are struck through in muted slate (#848587). A mint-teal badge overlays the top-left corner of the image for sale items, using uppercase 11px bold type.

**`product-card-badge`** — A small, uppercase label pinned to the product image corner. Background is the accent mint (#b2f9e9), text is dark (#121212), with 2px rounding and tight padding. Used exclusively for "SALE" or "NEW" indicators — never for sizing or color swatches.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, using the canvas background (#f1f0ed) with a subtle drop shadow on scroll. Links are 14px medium weight with 0.2px letter-spacing, and the logo sits left-aligned. The bar collapses to a hamburger menu on mobile, with a slide-out drawer for category links.

**`banner-top`** — A persistent 36px utility banner above the main nav, rendered in dark gray (#2c2c2c) with light text (#f1f0ed). Displays shipping and returns messaging in 13px regular weight. Fixed to the top of the viewport on all screen sizes.

### Forms
**`text-input`** — Standard input field for email signups, search, and checkout forms. Uses a canvas background (#f1f0ed) with 4px rounding and 12px 16px padding. On focus, gains a 2px navy border (#272d45). Height is 44px for comfortable touch targeting.

**`quantity-selector`** — A compact input for cart quantity adjustments, using the same canvas background and 44px height as text inputs. Typically paired with plus/minus icon buttons.

**`size-selector`** — A pill-shaped button group for size selection (XS–XXL). Inactive buttons use canvas background with ink text; the active selection fills with primary navy and white text. Each button is 40px tall with 8px 16px padding.

### Footer
**`footer-section`** — The site footer, rendered in the primary navy (#272d45) with white text. Links are 14px regular weight and shift to mint-teal (#b2f9e9) on hover. The footer includes accordion-style sections on mobile (collapsible by category) and a multi-column layout on desktop.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; footer accordions; banner text truncates to "Free Shipping & Returns" |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; footer in two columns; search bar remains full-width |
| Desktop | 1128–1440px | Three-column product grid; full nav links visible; footer in four columns; search bar pinned to nav |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to four columns; all elements centered with generous margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch compliance.
- Size selector buttons are 40px tall with 16px horizontal padding, exceeding the 44px tap target when including padding.
- Product card images are tappable with no minimum size requirement, but the entire card area is clickable.
- Hamburger menu icon is 44x44px with 8px internal padding.

### Collapsing Strategy
- Top navigation collapses to a hamburger drawer on mobile (< 744px), with category links hidden behind a slide-out panel.
- Footer sections collapse to accordion panels on mobile, with only headings visible by default.
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Search bar moves from a prominent nav-level element on desktop to a collapsible icon-triggered field on mobile.
- Banner text truncates on mobile to a single line, with the full message available on tap.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text inputs, size selectors, and quantity selectors were not fully extractable from the live site; focus border color is inferred from the primary palette.
- Error states (form validation, out-of-stock messaging, payment failures) were not observed and are not defined.
- Dark mode is not present on the live site; no dark-mode palette has been defined.
- The extracted hex list includes several generic web colors (#2c3e50, #0e7a82) that may be Shopify checkout defaults rather than brand-specific tokens — these have been noted as `accent-teal` and `accent-navy-dark` but should be verified against the brand's actual design assets.
- Font stack includes `oke-widget-icons` and `oke-widget-icons!important`, which are third-party review widget fonts — not part of the brand's core typography system.
- Sub-brand or seasonal palette variations (e.g., for "Evolution" or "Diversion" product lines) were not observed.
- Animation and transition durations (button hover, card lift, nav scroll shadow) were not extractable from static CSS.
