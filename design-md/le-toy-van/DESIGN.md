---
version: alpha
name: "Le Toy Van"
source_url: "https://letoyvan.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A world of wooden play built on a canvas of #f5f5f5, where the brand's signature voltage comes not from a single primary but from a constellation of accent colors — the warm #ec8816 of a painted sun, the deep #2c2a41 of a storybook night sky, and the clear #9ebadc of a nursery wall. The extracted palette reads like a well-stocked toy box: #d10000 for a fire engine, #199800 for a forest glade, #7069bc for a fairy's cloak, all set against a system of soft grays (#dedede, #b9b9b9, #e5e5e5) that keep the visual field calm and child-safe. Typography defaults to Arial and Helvetica — a pragmatic, legible choice that prioritizes readability over personality, letting the wooden textures and painted details carry the emotional weight. Buttons and badges use generous {rounded.sm} corners, while product cards and hero panels lean into {rounded.md} to soften the geometry of a digital storefront. The navigation bar sits at a compact height, with a sticky header that collapses on scroll, and the search bar adopts a pill shape ({rounded.full}) that feels approachable rather than clinical. The brand's eco-ethical positioning surfaces in muted earth tones (#4b556c, #777575) used for body text and secondary labels, while the primary call-to-action (#ec8816) glows like a wooden block catching afternoon light. There is no hard edge here — every corner, every gray, every accent is chosen to evoke the warmth of a playroom floor.

colors:
  primary: "#ec8816"
  primary-active: "#d4760a"
  primary-disabled: "#f5d6a8"
  ink: "#2c2a41"
  body: "#3c3c3c"
  muted: "#777575"
  muted-soft: "#979797"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#f5f5f5"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#9ebadc"
  accent-purple: "#7069bc"
  accent-red: "#d10000"
  accent-green: "#199800"
  accent-navy: "#134791"
  accent-sky: "#a3daff"
  accent-lavender: "#d4d2e2"
  badge-sale: "#e74c3c"
  badge-new: "#199800"
  star-rating: "#ec8816"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
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
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-sale:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
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
    padding: 12px 24px
    height: 44px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    textColor: "{colors.accent-red}"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.md}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  category-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
  category-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: 0 0 16px 0
  breadcrumb-link:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-current:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  wishlist-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
  wishlist-button-active:
    backgroundColor: transparent
    textColor: "{colors.accent-red}"
    rounded: "{rounded.full}"
    height: 40px
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  review-count:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  toast-success:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  toast-error:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 10px
  modal-overlay:
    backgroundColor: "rgba(44, 42, 65, 0.6)"
  modal-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
  drawer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    width: 320px
  drawer-header:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: 16px 24px
  drawer-close:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in {colors.primary} (#ec8816) with white text on a {rounded.sm} pill. On hover, it shifts to {colors.primary-active} (#d4760a); when disabled, it fades to {colors.primary-disabled} (#f5d6a8). Used for "Add to Cart", "Shop Now", and primary checkout flows.

**`button-secondary`** — A white button with {colors.ink} text, used for secondary actions like "View Details" or "Continue Shopping". On hover, it gains a subtle {colors.hairline} border. The outline variant (`button-secondary-outline`) uses a transparent background with a 1px {colors.hairline} border.

**`button-pill-primary`** — A fully rounded ({rounded.full}) compact button used for filter tags, category pills, and quick-add actions. Uses {typography.button-sm} for a tighter fit.

**`add-to-cart-button`** — The hero CTA on product pages, taller (48px) with more generous padding (14px 32px) to anchor the purchase flow. Uses {typography.button-md} weight 600.

### Navigation
**`nav-bar`** — A fixed-top navigation bar at 64px height on a {colors.canvas} background. On scroll, it collapses to 56px and gains a {colors.surface-card} background with a subtle {colors.hairline} bottom border. The logo sits left-aligned, with nav links centered or right-aligned depending on viewport.

**`nav-link`** — Inline navigation links using {typography.nav-link} (14px, weight 600). The active state uses {colors.primary} text color. On mobile, these collapse into a hamburger drawer.

**`search-bar-pill`** — A fully rounded search input with a {colors.surface-card} background, used in the header. On focus, it may expand or reveal a dropdown with recent searches.

### Cards
**`product-card`** — The primary product display unit, a white card with {rounded.md} corners. Contains an image area ({colors.surface-soft} background), a title in {typography.title-sm}, and a price in {typography.price}. Sale prices render in {colors.accent-red}. Badges overlay the top-left corner of the image.

**`product-card-badge`** — A small uppercase badge in {colors.accent-red} (#e74c3c) for sale items, or {colors.accent-green} (#199800) for new arrivals. Uses {typography.badge} (11px, weight 700, uppercase) with {rounded.xs} corners.

**`category-card`** — A larger card used for collection browsing, with a full-width image and a centered title in {typography.title-md}. Used on the homepage and category landing pages.

### Forms
**`text-input`** — A standard text input with {colors.surface-card} background, {colors.body} text, and {rounded.sm} corners. On focus, it gains a 2px {colors.primary} border. Used for search, newsletter signup, and checkout fields.

**`newsletter-input`** — A compact input (40px height) paired with `newsletter-button` in the footer. The button uses {colors.primary} background and sits adjacent to the input.

**`quantity-selector`** — A compact input with increment/decrement buttons, used on product pages and cart. Rendered at 40px height with {rounded.sm} corners.

### Footer
**`footer-section`** — A dark footer on {colors.ink} (#2c2a41) background with white text. Contains link columns, a newsletter signup, and social icons. Links use {typography.link} and headings use {typography.title-sm}.

**`footer-link`** — White text links on the dark footer background. On hover, they may underline or shift to {colors.primary}.

### Feedback & Utility
**`toast-success`** — A green toast notification on {colors.accent-green} background, used for "Added to Cart" confirmations. Appears at the top of the viewport and auto-dismisses after 3 seconds.

**`toast-error`** — A red toast on {colors.accent-red} background, used for error states like "Out of Stock" or validation failures.

**`tooltip`** — A dark tooltip on {colors.ink} background with white text, used for icon explanations and truncated text. Appears on hover with a small arrow.

**`modal-overlay`** — A semi-transparent overlay using rgba(44, 42, 65, 0.6) — the brand's ink color at 60% opacity. Used for quick-view modals, size guides, and confirmation dialogs.

**`drawer`** — A slide-in panel from the right side, 320px wide, used for mobile navigation and cart preview. Contains a header with a close button and scrollable content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger drawer; product cards stack single-column; hero panel reduces to 280px height; footer stacks vertically; search bar moves into drawer |
| Tablet | 744–1128px | Nav links visible; product cards in 2-column grid; hero panel at 360px height; footer in 2-column layout; search bar visible in header |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3- or 4-column grid; hero panel at 440px height; footer in 4-column layout; search bar expanded with placeholder text |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero panel at 520px height; all elements centered within max-width |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44px height
- Icon buttons and wishlist buttons are 40px with adequate padding
- Quantity selector buttons are 40px with clear hit areas
- Mobile nav drawer links have 48px tap targets
- Product card CTAs ("Add to Cart") are 48px tall on mobile

### Collapsing Strategy
- Primary navigation collapses to a hamburger icon at < 744px
- Product filters collapse into a "Filter" button that opens a drawer on mobile
- Footer link columns collapse into accordion sections on mobile
- Product image galleries collapse from thumbnails to a single swipeable strip
- Multi-column layouts (product grids, category cards) collapse to single column on mobile
- Search bar collapses from full-width to an icon that opens a modal on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted font list only returned system fonts (Arial, Helvetica, sans-serif) — the brand may use a custom web font (e.g., a Google Font or self-hosted typeface) that was not detected. If a brand font exists, it should replace the system fallbacks in the typography block.
- Hover and focus states for most components (beyond primary button) could not be reliably extracted — the above uses reasonable defaults (darkened backgrounds, border highlights) that should be verified against the live site.
- Error styling for form validation (red borders, error message typography) was not observed and uses common defaults.
- The extracted color list is dominated by grays and neutrals — the brand's true accent palette may be more limited or more saturated than represented. The accent colors chosen (#ec8816, #9ebadc, #7069bc, #d10000, #199800) are the most distinctive non-gray values in the extraction.
- Dark mode was not observed and is not implemented.
- Sub-brand or seasonal color palettes (e.g., holiday collections, collaborations) are not captured.
- Animation and transition durations/easings were not extracted — standard 200-300ms ease-in-out is assumed.
- The platform is Shopify, so checkout components (payment buttons, cart drawer) may use Shopify's default styling rather than the brand's custom tokens.
- Social media icon colors (e.g., Facebook blue, Instagram gradient) were filtered from the extraction but may appear on the live site.
