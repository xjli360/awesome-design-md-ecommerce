---
version: alpha
name: "18 East"
source_url: "https://18east.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, saturated red #d02e2e cuts through a near-black #0b0b0b canvas like a climbing rope against a night sky — this is the brand's primary voltage, a signal of durability and intent rather than fashion. The palette is deliberately compressed: ink #1a1a1a and body #3e3e3e sit close to the extremes, while muted #808080 and muted-soft #b3b3b3 provide just enough breathing room for product photography to dominate. A warm off-white #f1efe8 surfaces as the secondary canvas, softening the high-contrast black/red binary into something that reads as lived-in rather than sterile. The accent palette is sparse but purposeful — a sage green #56ad6a for sold-out or low-stock indicators, a pale peach #fff7f2 for sale badges, and a muted marigold #ecbd5e for seasonal callouts. There are no pill-shaped buttons, no soft rounded cards, no friendly search orbs; instead, the interface uses sharp {rounded.none} corners on primary actions and only the slightest {rounded.xs} on input fields, reinforcing a no-nonsense outdoor ethos. Typography is absent from extracted CSS, but the system likely favors a condensed or utilitarian sans-serif at modest weights — the brand trusts material quality and editorial photography over typographic flourish. Navigation is a single-tier horizontal bar with dropdowns, product cards use full-bleed imagery with minimal overlays, and the footer is a dense information grid. The site runs on Shopify, so checkout components inherit platform defaults, but the storefront itself feels like a gear closet: dark, efficient, and built to be navigated by people who know what they're looking for.

colors:
  primary: "#d02e2e"
  primary-active: "#b32525"
  primary-disabled: "#f3cbcb"
  ink: "#1a1a1a"
  body: "#3e3e3e"
  muted: "#808080"
  muted-soft: "#b3b3b3"
  hairline: "#d3d3d3"
  hairline-soft: "#e6e6e6"
  canvas: "#f1efe8"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#56ad6a"
  accent-peach: "#fff7f2"
  accent-marigold: "#ecbd5e"
  accent-red-soft: "#ff6d6d"
  accent-red-dark: "#d43747"
  badge-sold-out: "#56ad6a"
  badge-sale: "#fff7f2"
  badge-new: "#ecbd5e"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
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
    padding: 12px 24px
    height: 44px
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
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 40px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-sold-out:
    typography: "{typography.badge}"
    textColor: "{colors.accent-sage}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 40px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.canvas}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
  hero-overlay:
    backgroundColor: "rgba(0, 0, 0, 0.4)"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  collection-grid:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
  collection-title:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  add-to-cart-button-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  add-to-cart-button-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. Rendered as a sharp-cornered rectangle in the brand red #d02e2e with white uppercase text. On hover, shifts to `{colors.primary-active}` (#b32525). Disabled state uses `{colors.primary-disabled}` (#f3cbcb) with muted text. Used for "Add to Cart", "Shop Now", and primary checkout flows. Height is 44px with 12px 24px padding.

**`button-secondary`** — Used for secondary actions like "View Details" or "Learn More". Rendered on the warm off-white canvas `{colors.canvas}` with ink text. Active state fills with `{colors.hairline}` (#d3d3d3). Shares the same sharp-cornered {rounded.none} treatment as primary buttons.

**`button-outline`** — A transparent-background variant with a 1px solid `{colors.ink}` border for utility actions like "Clear Filters" or "Cancel". Padding is reduced by 1px on each side to account for the border. Height matches the standard 44px.

### Text Inputs
**`text-input`** — Standard form input for search, newsletter signup, and checkout fields. Uses a subtle {rounded.xs} corner (4px) — the only rounded element in the system. Background is `{colors.canvas}` with `{colors.ink}` text. Focus state adds a 2px `{colors.primary}` border. Height is 40px with 10px 12px padding.

**`select-input`** — Dropdown selectors for size, color, and quantity. Matches text-input styling with {rounded.xs} corners and the same height/padding. Uses a custom chevron icon in `{colors.muted}`.

### Navigation
**`nav-bar`** — A single-tier horizontal navigation bar at 64px height. Background is `{colors.canvas}` (#f1efe8) with uppercase nav links in `{colors.ink}`. Sticky variant (`nav-bar-sticky`) adds a 1px bottom border in `{colors.hairline}` (#d3d3d3) when scrolled. Contains brand logo on the left, primary links in the center, and utility icons (search, account, cart) on the right.

**`nav-link`** — Uppercase, 14px, weight 600 with 0.5px letter spacing. Active and hover states shift text color to `{colors.primary}` (#d02e2e). Padding is 8px 12px for comfortable tap targets.

### Product Cards
**`product-card`** — A minimal, full-bleed product display with no rounded corners. The image area (`product-card-image`) fills the top portion with a `{colors.surface-soft}` (#f7f7f7) placeholder. Below, the title uses `{typography.title-sm}` (16px, weight 600) and the price uses `{typography.body-sm}` (14px, weight 400). Sold-out items show a `product-card-sold-out` badge in `{colors.accent-sage}` (#56ad6a). Cards are arranged in a responsive grid with 16px gaps.

### Badges
**`badge`** — Small, sharp-cornered labels for product status. The default badge uses `{colors.primary}` (#d02e2e) with white text. Three semantic variants exist: `badge-sold-out` in sage green (#56ad6a), `badge-sale` in pale peach (#fff7f2) with red text, and `badge-new` in marigold (#ecbd5e) with ink text. All use uppercase 11px weight 700 type with 0.5px letter spacing and 2px 8px padding.

### Search
**`search-bar`** — A simple text input for site search, styled identically to `text-input` with {rounded.xs} corners. Placeholder text in `{colors.muted}` (#808080). Focus state shifts text to `{colors.ink}` and adds a red border. On mobile, the search bar expands to full width below the nav.

### Footer
**`footer-section`** — A dense information grid on a `{colors.ink}` (#1a1a1a) background. Column headings use `{typography.title-sm}` in `{colors.canvas}` (#f1efe8). Links use `{typography.link}` (14px, weight 400) in `{colors.muted-soft}` (#b3b3b3) and shift to `{colors.canvas}` on hover. Contains brand info, customer service links, legal text, and social icons.

### Hero
**`hero-section`** — Full-width promotional banner on a dark `{colors.ink}` background with white text. Uses `{typography.display-xl}` (32px, weight 700) for headlines. A semi-transparent overlay (`hero-overlay`) at 40% black sits over background imagery. The CTA button (`hero-cta`) matches `button-primary` styling. Typically used for seasonal collections or new arrivals.

### Collection Grid
**`collection-grid`** — The main product listing layout on `{colors.canvas}` (#f1efe8). Collection titles use `{typography.display-md}` (24px, weight 600) in `{colors.ink}`. Products are arranged in a responsive grid with 16px gaps. On mobile, the grid collapses to 2 columns; on tablet, 3 columns; on desktop, 4 columns.

### Cart
**`quantity-selector`** — A compact input for adjusting item quantities in the cart. Uses {rounded.xs} corners and matches text-input dimensions (40px height, 8px 12px padding). Includes increment/decrement buttons on either side.

**`add-to-cart-button`** — The primary purchase action, taller than standard buttons at 48px with 14px 32px padding. Uses `{colors.primary}` (#d02e2e) with white uppercase text. Active state shifts to `{colors.primary-active}` (#b32525). Disabled state uses `{colors.primary-disabled}` (#f3cbcb) with `{colors.muted}` text. Sharp {rounded.none} corners throughout.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product grid goes to 2 columns; hero text reduces to 24px; footer stacks vertically; search bar expands full-width below nav |
| Tablet | 744–1128px | Nav remains horizontal but reduces link spacing; product grid at 3 columns; hero maintains 28px text; footer uses 2-column layout |
| Desktop | 1128–1440px | Full nav with all links visible; product grid at 4 columns; hero at 32px text; footer uses 4-column layout |
| Wide | > 1440px | Max-width container at 1440px with centered content; product grid can expand to 5 columns; hero text scales to 36px |

### Touch Targets
- All buttons and links maintain minimum 44px height for touch accessibility
- Nav links have 8px 12px padding, providing ~40px tap targets
- Quantity selector increment/decrement buttons are 32px × 32px minimum
- Product card images are tappable full-width

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Footer columns collapse from 4 → 2 → 1 as viewport narrows
- Product grid reduces columns: 4 → 3 → 2
- Hero overlay text reduces font size and may stack vertically on mobile
- Search bar moves from nav to below-nav full-width on mobile
- Secondary navigation (breadcrumbs, filters) collapses to dropdown or toggle on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extracted from the live site CSS; the typography block uses a fallback stack of system sans-serif fonts. The brand likely uses a custom or licensed typeface (possibly a condensed sans-serif like Trade Gothic or a utilitarian family like Helvetica Now) that could not be identified.
- Hover and focus states for text inputs, select inputs, and search bars were inferred from common patterns; exact border colors and transition durations are unknown.
- Error styling for form validation (red borders, error message typography) was not extractable.
- Dark mode is not present on the site; all extracted colors assume a light theme.
- Sub-brand or seasonal palette variations (e.g., holiday collections, collaborations) were not captured.
- Checkout components inherit Shopify's default styling and were not analyzed separately.
- Social media icon colors and hover states were not extracted.
- The hero overlay gradient or pattern (if any) could not be determined from extracted data.
- Animation durations, easing curves, and transition properties are not documented.
- The exact font sizes for display typography were estimated based on common outdoor apparel brand patterns; the site may use slightly different values.
