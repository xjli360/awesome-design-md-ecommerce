---
version: alpha
name: "Redeye Records"
source_url: "https://www.redeyerecords.co.uk"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A teal #2e9b8d pulse runs through an otherwise monochrome record-store grid — that single accent color appears on the "Add to Basket" button, the search bar's focus ring, and the genre-filter highlight, giving a specialist dance-music shop a clean, almost clinical confidence. The canvas is #f6f6f6, a warm off-white that softens the dense product grid, while body text sits in #484848 rather than pure black, reducing contrast fatigue during long browsing sessions. Product cards use #ffffff surfaces with a #e4e4e4 hairline, creating a subtle separation that lets album art — often high-contrast and colorful — do the visual heavy lifting. The typography stack leans on Kanit for headings, a geometric sans-serif with sharp terminals that echoes the precision of electronic music production, while body copy falls back to Helvetica Neue and Arial for reliable readability. Navigation is minimal: a sticky top bar with the brand logo, search input, basket icon, and a "Sign In" link, all sitting on #ffffff. The search bar is the most interactive element on the page, with a full-width input that expands on focus and uses the teal accent for its border. Genre and format filters (Vinyl, CD, Merch) are rendered as pill-shaped buttons with `{rounded.full}`, using #f1f1f1 backgrounds that toggle to #2e9b8d when active. The overall feel is utilitarian but intentional — a tool for digging through thousands of dance records, not a lifestyle brand. The footer collapses to a single column on mobile, stacking shipping info, social links, and payment icons (Visa, Mastercard, PayPal) in #707070 text on #f6f6f6.

colors:
  primary: "#2e9b8d"
  primary-active: "#117a8b"
  primary-disabled: "#abdde5"
  ink: "#484848"
  body: "#484848"
  muted: "#707070"
  muted-soft: "#818182"
  hairline: "#e4e4e4"
  hairline-soft: "#f1f1f1"
  canvas: "#f6f6f6"
  surface-soft: "#f1f1f1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  error: "#bd2130"
  success: "#1e7e34"
  warning: "#d39e00"
  info: "#0c5460"
  badge-new: "#d39e00"
  badge-sale: "#bd2130"
  badge-sold-out: "#6c757d"
  link: "#0062cc"
  link-visited: "#545b62"
  star-rating: "#d39e00"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Kanit, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Kanit, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "Kanit, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Kanit, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
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
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "Kanit, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "Kanit, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Kanit, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
  badge:
    fontFamily: "Kanit, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "Kanit, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary}"
  button-pill-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  button-pill-filter-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.primary}"
  genre-filter-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} 0"
  genre-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  genre-tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
  pagination-button-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
    border: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Basket" and checkout flows. Filled with the brand teal `{colors.primary}` (#2e9b8d) with white text. On hover, shifts to `{colors.primary-active}` (#117a8b). Disabled state uses `{colors.primary-disabled}` (#abdde5) with muted text. Height is 44px with `{rounded.sm}` corners.

**`button-secondary`** — Outlined alternative for secondary actions like "View Details" or "Clear Filters". White background with `{colors.ink}` text and a `{colors.hairline}` border. Active state swaps the border to `{colors.primary}`. Same 44px height as primary for alignment in forms.

**`button-pill-filter`** — Genre and format filter pills used in the category strip. Small, rounded-full buttons with `{colors.surface-soft}` background and `{colors.ink}` text. Active state fills with `{colors.primary}` and white text. Height is 36px with 8px horizontal padding.

### Cards
**`product-card`** — The core product display unit. A white card (`{colors.surface-card}`) with `{rounded.sm}` corners and 8px padding. Contains a square album art image with `{rounded.xs}`, the release title in `{typography.title-md}`, artist name, format badge, and price in `{typography.price}`. On hover, a subtle box shadow lifts the card. Badges for "New", "Sale", or "Sold Out" appear as small uppercase labels in the top-left corner.

### Forms & Inputs
**`text-input`** — Standard text input for search, login, and checkout forms. White background with `{colors.hairline}` border and `{rounded.sm}` corners. On focus, the border thickens to 2px and switches to `{colors.primary}`. Height is 44px with 16px horizontal padding.

**`search-bar`** — The primary search input, identical in styling to `text-input` but with a distinct role. On focus, the border becomes 2px `{colors.primary}`. The search bar is the most prominent interactive element on the page, often spanning the full width of the content area on mobile.

### Navigation
**`nav-bar`** — Sticky top navigation bar, 64px tall, white background with a `{colors.hairline}` bottom border. Contains the brand logo (left), search bar (center on desktop, expandable on mobile), account/sign-in link, and basket icon (right). Navigation links use `{typography.nav-link}` in Kanit medium.

**`genre-filter-strip`** — A horizontal scrollable strip of filter pills below the nav. Contains genre tabs (House, Techno, Drum & Bass, etc.) and format tabs (Vinyl, CD, Merch). Each pill is `{rounded.full}` with `{colors.surface-soft}` background. Active pills use `{colors.primary}` fill.

### Footer
**`footer`** — Simple footer with `{colors.canvas}` background and `{colors.hairline}` top border. Text is `{colors.muted}` (#707070) in `{typography.body-sm}`. Contains columns for customer service links, about info, social media icons, and payment method logos. Links turn `{colors.primary}` on hover. On mobile, columns stack vertically.

### Badges
**`badge-new`** — Yellow (#d39e00) background for new arrivals.
**`badge-sale`** — Red (#bd2130) background for sale items.
**`badge-sold-out`** — Gray (#6c757d) background for out-of-stock items.
All badges use `{typography.badge}` (Kanit 11px uppercase) with white text and `{rounded.xs}` corners.

### Pagination
**`pagination-button`** — Numbered page buttons at the bottom of search results. White background with `{colors.hairline}` border and `{rounded.sm}` corners. Active page uses `{colors.primary}` fill. Disabled buttons (for first/last page limits) use `{colors.surface-soft}` background with muted text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 items per row). Search bar collapses to icon-only, expands on tap. Genre filter strip scrolls horizontally. Footer stacks vertically. Nav bar height reduces to 56px. Product card padding reduces to 4px. |
| Tablet | 744–1128px | Two-column product grid. Search bar remains visible but narrower. Genre filter strip shows 4-5 pills before overflow scroll. Footer has 2-column layout. Nav bar at 64px. |
| Desktop | 1128–1440px | Three-column product grid. Full-width search bar. Genre filter strip shows all pills. Footer has 4-column layout. Standard nav bar. |
| Wide | > 1440px | Four-column product grid. Max-width container (1440px) centered. All elements at maximum comfortable size. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px for touch accessibility.
- Filter pills are 36px tall — acceptable for touch but close to the 44px recommendation.
- Product card images are tappable and link to product detail pages.
- Basket icon and account link in nav are 44x44px tap targets.

### Collapsing Strategy
- **Mobile:** Search bar collapses to an icon button; tapping expands it to full-width input. Genre filter strip scrolls horizontally. Footer columns collapse to a single stack. Product grid goes to 1-2 columns.
- **Tablet:** Search bar remains visible but narrower. Genre filter strip shows limited pills with overflow scroll. Footer uses 2-column layout.
- **Desktop:** All elements at full width. Genre filter strip shows all pills. Footer uses 4-column layout.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards and buttons were inferred from common e-commerce patterns; the live site may use different transitions or shadows.
- Error styling for form validation (red borders, error messages) was not extractable from the static analysis.
- The exact font sizes and weights for Kanit headings were estimated from the extracted font-family declaration and common usage; the live site may use different sizes.
- The brand's logo (SVG or image) was not extracted; its exact dimensions and color are unknown.
- Dark mode is not supported and was not detected on the live site.
- The checkout flow (Shopify Pay, Klarna, Afterpay) colors were filtered from the extracted palette; the brand's actual checkout styling may differ.
- Sub-brand or seasonal color palettes (e.g., for sale events, genre-specific landing pages) were not detected.
- The `#0062cc` blue appears in the extracted palette and is likely used for standard link styling, but its exact usage context is unconfirmed.
