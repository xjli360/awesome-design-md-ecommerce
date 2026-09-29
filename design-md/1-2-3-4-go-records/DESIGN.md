---
version: alpha
name: "1-2-3-4 Go! Records"
source_url: "https://1234gorecords.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record store that wears its punk and garage-rock DNA on its sleeve, anchored by a raw #cc3b3b red that hits like a Marshall stack on ten. The brand lives in the tension between that shouty primary and a near-black #111111 ink — no pastels, no soft gradients, just the voltage of a storefront sign against a dark interior. Allerta Stencil, a typeface borrowed from military stencils and skate-park graffiti, runs the display hierarchy at 28px and 22px, its hard edges echoing the sharp corners of a record sleeve. The canvas is #fafafa, barely off-white, like the paper of a well-thumbed zine, while #e1e1e1 hairlines and #aaaaaa muted tones keep the structure readable without softening the attitude. Buttons are solid red blocks with {rounded.xs} — a concession to usability that still refuses to go pill-shaped. The product grid uses {rounded.none} on cards; the only curve in the system is the {rounded.full} search bar, a necessary portal into the inventory. This is a store that trusts its stock photography and album art to do the emotional work, keeping chrome and ornament to a minimum. The secondary red #bd0000 and a faded pink #e99292 appear in sale badges and sold-out markers, extending the palette without diluting the core voltage. The nav is a single dark band at #222222, the footer a deeper #040404 — the brand reads as a physical space translated into code, where the digital interface defers to the records themselves.

colors:
  primary: "#cc3b3b"
  primary-active: "#bd0000"
  primary-disabled: "#e99292"
  ink: "#111111"
  body: "#222222"
  muted: "#aaaaaa"
  muted-soft: "#e1e1e1"
  hairline: "#e1e1e1"
  hairline-soft: "#eeeeee"
  canvas: "#fafafa"
  surface-soft: "#fbfbfb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  nav-bg: "#222222"
  footer-bg: "#040404"
  sale-badge: "#bd0000"
  sold-out: "#e99292"
  accent-dark: "#272727"
  accent-darker: "#1e1e1e"

typography:
  display-xl:
    fontFamily: "'Allerta Stencil', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
  display-lg:
    fontFamily: "'Allerta Stencil', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.3px
  display-md:
    fontFamily: "'Allerta Stencil', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  title-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Allerta Stencil', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Allerta Stencil', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Allerta Stencil', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  badge:
    fontFamily: "'Allerta Stencil', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sold-out:
    backgroundColor: "{colors.sold-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  section-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: 24px 0
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  filter-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px

## Components

### Buttons
**`button-primary`** — The store's primary call-to-action, a solid #cc3b3b red block with {rounded.xs} corners and Allerta Stencil uppercase text. On hover or active, it deepens to #bd0000 (`{colors.primary-active}`). The disabled state fades to #e99292 (`{colors.primary-disabled}`), a washed-out pink that signals unavailability without ambiguity. The 44px height and 12px 24px padding give it presence without overwhelming the product grid.

**`button-secondary`** — An outlined alternative on a white canvas with #111111 ink text. Uses the same Allerta Stencil uppercase and {rounded.xs} corners. The active state fills the background with #e1e1e1 (`{colors.hairline}`), providing a subtle press effect. Used for "View All" links, filter resets, and secondary actions that shouldn't compete with the primary red.

### Navigation
**`nav-bar`** — A 60px dark band at #222222 (`{colors.nav-bg}`) spanning the full viewport width. Navigation links use Allerta Stencil uppercase at 14px in white, with the active state switching to #cc3b3b (`{colors.primary}`). The bar is intentionally compact — no dropdowns, no mega-menus, just the essential store sections: Home, New Arrivals, Vinyl, Merch, About. The search bar sits as a {rounded.full} pill within the nav on desktop, or expands below on mobile.

### Product Cards
**`product-card`** — A minimal, zero-radius container that lets the album art do the talking. The card has no background fill (transparent, inheriting from the #fafafa canvas) and no border — just the product image, title in `{typography.title-sm}`, and price in `{typography.price}`. On hover, a subtle shadow or slight scale transform can be applied, but the default state is flat and unadorned. Sale and sold-out badges (`{badge-sale}`, `{badge-sold-out}`) overlay the top-left corner of the image when applicable.

### Forms & Inputs
**`text-input`** — A white field with a 1px #e1e1e1 hairline border and {rounded.xs} corners, using Open Sans body text. On focus, the border switches to #cc3b3b (`{colors.primary}`) to indicate active state. The 44px height matches the button height for consistent form layouts. Used for newsletter signups, search queries, and contact forms.

### Search
**`search-bar`** — The only fully rounded element in the system, a {rounded.full} pill that serves as the gateway to the store's inventory. White background with #111111 text, using Open Sans body copy. The pill shape is a deliberate contrast to the otherwise angular system — it signals "this is where you find things" as a friendly portal. On focus, the border or outline shifts to #cc3b3b.

### Footer
**`footer`** — A deep #040404 (`{colors.footer-bg}`) band at the bottom of every page, with muted #aaaaaa link text that brightens to white on hover. Links use Open Sans at 14px, not the stencil typeface — the footer is for information, not attitude. Sections include Store Hours, Location, Shipping Info, and Social Links. Padding is generous at 48px 24px to give the dark area breathing room.

### Badges
**`badge-sale`** — A compact #bd0000 red label with white Allerta Stencil uppercase text, {rounded.xs} corners, and 4px 8px padding. Overlays product images to flag discounted items. The red is slightly darker than the primary to ensure legibility against album art.

**`badge-sold-out`** — Uses the faded pink #e99292 (`{colors.sold-out}`) with white text, signaling unavailability without the urgency of the sale badge. Same dimensions and typography as the sale badge.

### Hero
**`hero`** — A full-width section with a #111111 (`{colors.ink}`) background and white Allerta Stencil display text at 28px. Used for the homepage header, collection features, and seasonal promotions. The dark backdrop makes the red primary buttons and album art pop dramatically. Padding is 64px 24px, giving the headline room to breathe.

### Filter Tags
**`filter-tag`** — Pill-shaped tags (the only other {rounded.full} element besides the search bar) for filtering products by genre, format, or price range. Default state is a #fbfbfb soft surface with #111111 text. Active state fills with #cc3b3b red and white text. The pill shape differentiates filters from buttons, making the interface scannable.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; search bar moves below nav; hero padding reduces to 32px 16px; filter tags wrap to two rows |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; search bar remains in nav; hero text reduces to 22px |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; search bar as pill in nav; hero at full 28px display |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero centered with max-width 1200px |

### Touch Targets
- All buttons and links: minimum 44px height (WCAG compliant)
- Filter tags: minimum 36px height with 16px horizontal padding
- Nav links: 44px tap area even if text is smaller
- Search bar: 44px height on all breakpoints
- Product cards: entire card is tappable, minimum 120px height

### Collapsing Strategy
- Nav links collapse to a hamburger menu below 744px
- Product grid columns reduce by one on each breakpoint down (4→3→2→1)
- Filter tags wrap to two rows on mobile, single row on tablet and above
- Hero section reduces padding and font size on mobile
- Footer links stack vertically on mobile, horizontal on tablet and above
- Search bar expands to full width below the nav on mobile, remains in nav on tablet and above

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only primary button hover was extracted (#bd0000). Secondary button, link, and card hover states are inferred from common patterns but not confirmed from the live site.
- **Error styling**: No form validation, error message, or error state colors could be extracted. The system uses #cc3b3b for focus states, but error-specific colors (e.g., red for field errors) are unknown.
- **Dark mode**: No dark mode implementation was detected. The site uses a light canvas (#fafafa) with dark nav and footer — a dark mode variant would need to be designed from scratch.
- **Sub-brand palettes**: No secondary brand colors for seasonal campaigns, exclusive releases, or collaborations were found. The palette is limited to the core red, black, white, and gray tones.
- **Typography scale**: Font sizes for display-xl (28px) and display-lg (22px) were inferred from heading patterns. Intermediate sizes (display-md at 18px) and smaller text variants (caption at 12px) are estimated based on common e-commerce patterns.
- **Animation and transition**: No animation durations, easing functions, or transition properties were extracted. The system likely uses simple CSS transitions (0.2s ease), but this is unconfirmed.
- **Spacing scale**: The spacing tokens (xxs through section) are based on a standard 4px/8px grid system common in Shopify stores. Actual spacing values from the live site may vary by a few pixels.
- **Component shadows**: No box-shadow values were extracted. Product cards and modals may use subtle shadows that weren't captured in the color extraction process.
- **Font weights**: Allerta Stencil only comes in Regular (400) weight. Open Sans weights (400, 600) are inferred from common usage — exact weights for body vs. title text are unconfirmed.
- **Checkout and cart**: Shopify's default checkout styling may override the brand's design system. Cart drawer, checkout button, and payment form styles are not captured here.
