---
version: alpha
name: "Square Enix Store"
source_url: "https://www.squareenixstore.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep-crimson storefront (#8b0000) that signals fandom rather than retail — the same blood-red that crowns Final Fantasy logos and marks the brand's most iconic collector's editions, now serving as the primary voltage for every "Pre-order" CTA, cart badge, and limited-quantity alert. Against a near-black canvas (#121212), this red reads as urgent and ceremonial, not promotional; it's the color of a summon materia, not a clearance tag. The secondary accent (#006400) — a dense forest green — appears on pre-order buttons and exclusive-edition badges, creating a Christmas-of-gaming tension that's unmistakably Square Enix. Type runs Inter at moderate weights (400–600), with display headlines rarely exceeding 24px; the brand trusts its key art — Amano illustrations, CG renders, and 4K screenshots — to carry emotional weight rather than oversized typography. Product cards use thin hairline borders (#dedede) on white surfaces (#ffffff), but the site's dominant mode is dark: black nav bars, black footers, black product-detail backgrounds that frame glowing screenshots like a theater curtain. The store's Shopify backbone surfaces in pill-shaped search bars ({rounded.full}) and generously padded buttons (14px vertical), but the overall feel is less marketplace and more museum gift shop — a place where a $300 statue of Sephiroth sits beside a $10 soundtrack, both rendered with the same solemn {rounded.sm} corner radius and the same dark reverence.

colors:
  primary: "#8b0000"
  primary-active: "#660000"
  primary-disabled: "#c8c8c8"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#006400"
  accent-orange: "#ee9441"
  accent-green-bright: "#3ed660"
  badge-new: "#ee9441"
  badge-exclusive: "#006400"
  badge-sale: "#8b0000"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0

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
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-accent-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
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
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link:
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.muted}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "top-left"
  product-card-badge-exclusive:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-lg}"
    height: 400px
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  cart-icon:
    textColor: "{colors.canvas}"
    height: 24px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.lg}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  skeleton:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.sm}"
    height: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in deep crimson (#8b0000) on white text. Used for "Pre-order", "Add to Cart", and "Buy Now" actions. On hover, darkens to `#660000`; disabled state drops to `#c8c8c8` with white text, signaling unavailability. Padding is generous (14px vertical, 24px horizontal) with a soft 8px corner radius.

**`button-secondary`** — A white button with a thin `#dedede` border, used for "View Details", "Wishlist", and secondary checkout actions. Text is near-black (`#121212`). On hover, the border thickens subtly. Same 48px height as primary for alignment in forms.

**`button-accent-green`** — Forest green (`#006400`) button reserved for exclusive-edition pre-orders and "Collector's Edition" CTAs. Same dimensions and radius as primary. The green signals scarcity and premium tier.

**`button-accent-orange`** — Marigold orange (`#ee9441`) button used for "Notify Me" and "Coming Soon" actions. Text is dark ink for contrast. This is the brand's anticipatory color — not yet available, but coming.

**`button-pill`** — A smaller, fully rounded pill button used for filter tags, "New" badges, and quick-add actions. Uses `{rounded.full}` and tighter padding (10px vertical, 20px horizontal). Height is 36px.

### Cards
**`product-card`** — A white card with `{rounded.sm}` corners and 16px padding. The product image fills the top with a matching corner radius and a 1:1 aspect ratio. Title sits below in `{typography.title-sm}` (14px, medium weight), price in `{typography.body-sm}` at `{colors.muted}`. Badges overlay the top-left corner of the image — crimson for sale, green for exclusive, orange for new.

**`product-card-badge`** — Small uppercase label (11px, 600 weight, 0.5px letter spacing) with 2px vertical padding and 8px horizontal. Background matches the badge type: `{colors.primary}` for sale, `{colors.accent-green}` for exclusive, `{colors.accent-orange}` for new. Positioned absolutely at the top-left of the card image with `{rounded.xs}`.

### Navigation
**`nav-bar`** — A fixed black (`#121212`) bar at 64px height. Logo sits left, nav links center, search and cart icons right. Links are white `{typography.nav-link}` (14px, medium weight). Active link or hover state shifts to crimson `{colors.primary}`. On scroll, the bar compresses to 56px. The cart icon carries a crimson badge with white count text, `{rounded.full}` at 18px.

**`nav-link`** — Inline navigation text at 14px/500 weight. Default white on dark nav, active state crimson. No underline — the color shift is the only affordance.

### Forms
**`text-input`** — White input with `{rounded.sm}`, 48px height, and a `#dedede` border. On focus, the border becomes a 2px crimson stroke. Placeholder text is `{colors.muted}`. Used for search, email signup, and address forms.

**`search-bar`** — A pill-shaped (`{rounded.full}`) input at 48px height with 12px vertical and 20px horizontal padding. On dark backgrounds (hero banners, footer), a dark variant inverts to black background with white text and a muted border.

**`quantity-selector`** — A compact 40px-high input with `{rounded.sm}` and a `#dedede` border. Used on product detail pages for cart quantity adjustment. Buttons for increment/decrement sit inside the border.

### Footer
**`footer`** — Full-width black (`#121212`) section with 48px vertical padding. Links are `{colors.muted-soft}` at 14px, shifting to white on hover. Organized in columns by category (Games, Merchandise, Support, About). Social icons and newsletter signup sit in the bottom row. A thin `{colors.muted}` divider separates the link columns from the copyright line.

### Hero
**`hero-banner`** — A 400px-tall dark section (`#121212`) with a full-bleed background image (game key art). White headline in `{typography.display-lg}` (24px, 600 weight) overlays the left side. A single crimson CTA button sits below the headline. The banner may include a gradient overlay from `{colors.ink}` to transparent for text readability.

### Loading & Skeleton
**`loading-spinner`** — A 24px crimson spinner, used during product list loading and checkout transitions. Centered in the container.

**`skeleton`** — A 16px-tall placeholder bar in `{colors.hairline-soft}` with `{rounded.sm}`, used while product cards and images load. Multiple skeletons stack to form a card outline.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column (100% width); hero banner height reduces to 280px; footer links stack vertically; search bar moves to a full-width overlay; buttons become full-width for easier tapping |
| Tablet | 744–1128px | Nav shows limited links (Games, Merchandise, Support) with hamburger for overflow; product cards in 2-column grid; hero banner at 360px; footer in 2-column layout; search bar remains in nav but shrinks to icon-only on scroll |
| Desktop | 1128–1440px | Full nav with all links visible; product cards in 3- or 4-column grid; hero banner at 400px; footer in 4-column layout; search bar full-width in nav; side cart drawer on product pages |
| Wide | > 1440px | Max-width container at 1440px, centered; product cards in 4- or 5-column grid; hero banner may extend to full viewport width with content constrained to 1440px; larger product images; additional whitespace around sections |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px on mobile for touch accessibility
- Nav hamburger icon is 48x48px with 8px padding
- Cart icon is 44x44px with 4px padding
- Quantity selector buttons are 44x44px
- Product card tap target is the entire card (minimum 120px height)
- Filter chips and badge tags are 36px minimum height

### Collapsing Strategy
- On mobile, the top nav collapses to a hamburger menu with a full-screen overlay drawer; search becomes a sticky icon that expands to a full-width input on tap
- Product filters collapse into a bottom sheet or modal on mobile; on tablet they become a collapsible sidebar
- The footer link columns collapse from 4 columns to 2 on tablet, to a single stacked column on mobile
- The hero banner's secondary text and smaller CTAs collapse on mobile, leaving only the headline and primary CTA
- Product image galleries collapse from a row of thumbnails to a swipeable carousel on mobile
- Accordion sections (product details, reviews) are collapsed by default on all breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from static CSS; the active/darkened state for `button-primary` is inferred from common patterns rather than observed
- Error state styling for text inputs (red border, error message typography) was not present in extracted styles
- Dark mode is not supported; the site uses a fixed dark nav/footer with white content areas — no system-preference toggle was found
- Sub-brand palettes (Final Fantasy red, Dragon Quest blue, Kingdom Hearts pink) may exist in product-specific pages but were not extracted from the main store shell
- The extracted hex list includes `#3ed660` (bright green) and `#ee9441` (orange) — these may be Shopify checkout widget colors or stock-image tones rather than intentional brand accents. They are included here as `accent-green-bright` and `accent-orange` but should be verified against live product badges and CTAs
- Font weight for `display-xl` (600) is an assumption based on Inter's typical usage; the extracted CSS only showed `font-family: Inter` without explicit weight declarations
- Line-height values for typography are estimated from common Inter rendering; the extracted CSS did not include explicit line-height rules
- The `#006400` green is unusually dark for a secondary accent — it may be a Shopify admin color or a legacy holdover; verify against actual "Exclusive" badges on the live site
- No animation or transition durations were extracted; the site likely uses 150-300ms ease transitions for hover states
- The `#c8c8c8` disabled color may be too light for accessibility; verify contrast ratios against white text
- No data on mobile nav drawer animation, cart slide-in behavior, or product quick-view modals
- Shopify-specific elements (checkout button, payment icons, cart drawer) may override these tokens with their own styling
