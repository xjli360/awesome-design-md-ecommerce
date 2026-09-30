---
version: alpha
name: "Reckless Records"
source_url: "https://www.reckless.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A Chicago institution that wears its inventory like a badge of honor, Reckless Records builds its digital storefront on a deep black ink (#111111) canvas that makes every album cover, DVD spine, and seven-inch sleeve pop like a jewel in a dark crate. The extracted palette reads like a record store's back room — muted grays (#868e96, #464a4e) for secondary text and dividers, with sharp accent colors that map directly to vinyl genres and price tags: a deep indigo (#004085) for the header and primary actions, a forest green (#155724) for in-stock badges, a teal (#0c5460) for special-edition callouts, and a warm amber (#856404) for sale markers. The typography stack leans hard on system fonts — Apple's San Francisco via -apple-system, Roboto for Android, and Helvetica Neue for legacy — giving the site a fast, utilitarian feel that prioritizes browsing speed over brand theater. Buttons use tight {rounded.sm} corners (8px), not the pill shapes of modern ecommerce; the search bar sits as a simple input with a magnifying-glass icon, not a floating orb. The nav bar is a single dark band (#111111) with white text, carrying the store's name and a handful of links — no mega-menus, no lifestyle photography. This is a site built for people who already know what they want: a specific pressing, a rare import, a used CD that's been out of print for years. The design gets out of the way.

colors:
  primary: "#004085"
  primary-active: "#00336b"
  primary-disabled: "#809ec4"
  ink: "#111111"
  body: "#464a4e"
  muted: "#868e96"
  muted-soft: "#818182"
  hairline: "#dae0e5"
  hairline-soft: "#cfd2d6"
  canvas: "#ffffff"
  surface-soft: "#ececf6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  stock-badge: "#155724"
  stock-badge-bg: "#b1dfbb"
  sale-badge: "#856404"
  sale-badge-bg: "#ffe8a1"
  special-edition: "#0c5460"
  special-edition-bg: "#abdde5"
  error: "#721c24"
  error-bg: "#f1b0b7"
  link: "#0062cc"
  link-hover: "#1d2124"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
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
    padding: 10px 20px
    height: 40px
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
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-link:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.link}"
    padding: 4px 0
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: "0 {spacing.lg}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: "8px {spacing.md}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.on-dark}"
  search-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px {spacing.md}"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-input-focus:
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  product-card-hover:
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
  product-title:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
  product-artist:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  product-price:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
  badge-stock:
    backgroundColor: "{colors.stock-badge-bg}"
    textColor: "{colors.stock-badge}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.sale-badge-bg}"
    textColor: "{colors.sale-badge}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.xs}"
  badge-special:
    backgroundColor: "{colors.special-edition-bg}"
    textColor: "{colors.special-edition}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.xs}"
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "6px {spacing.md}"
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "6px {spacing.md}"
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-dark}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and "Search" actions. Rendered in the deep indigo {colors.primary} (#004085) with white text on an 8px rounded rectangle. On hover, the background shifts to {colors.primary-active} (#00336b); disabled state uses {colors.primary-disabled} (#809ec4). Height is a compact 40px with 10px vertical padding, keeping the button proportional to the dense product listings.

**`button-secondary`** — Used for "View Details", "Clear Filters", and secondary checkout actions. White background with {colors.ink} text and a 1px {colors.hairline} border. Active state fills with {colors.surface-soft} (#ececf6). Same 40px height and 8px corner radius as the primary button for visual consistency.

**`button-link`** — Text-only link button for actions like "Cancel", "Reset", or "See All". Uses the system link blue {colors.link} (#0062cc) with no background or border. Hover shifts to {colors.link-hover} (#1d2124). Minimal 4px vertical padding keeps it inline with surrounding text.

### Navigation
**`top-nav`** — A 56px dark band (#111111) spanning the full viewport width. Contains the store name on the left and navigation links on the right. White text on black — no logo mark, just the wordmark "Reckless Records" in the system font stack. Padding of 24px on each side.

**`nav-link`** — Navigation items rendered in white with 8px vertical and 12px horizontal padding. Active state has a 2px white bottom border. No hover background change — the brand trusts the underline to signal location.

**`search-input`** — A simple 40px text input with 8px corner radius, white background, and a 1px {colors.hairline} border. On focus, the border switches to {colors.primary} (#004085). No search button — the magnifying glass icon sits inside the input as a decorative element.

### Cards
**`product-card`** — The core inventory display unit: a white card with 8px rounded corners and 8px padding. Contains the album art (full-width), the title in {typography.title-md}, the artist in {typography.body-sm} in {colors.muted}, and the price in {typography.title-md}. On hover, a subtle box-shadow lifts the card 2px off the page.

**`product-title`** — Album or movie title set in 18px/600 weight. Truncates to one line with ellipsis for long titles.

**`product-artist`** — Artist name in 14px regular weight, colored {colors.muted} (#868e96). Sits below the title with 4px margin.

**`product-price`** — Price displayed in 18px/600 weight in {colors.ink}. No currency symbol prefix — the site uses a simple "$" before the number in the markup.

### Badges
**`badge-stock`** — Green badge on a light green background (#b1dfbb / #155724) indicating items currently in stock. 12px uppercase font with 0.3px letter spacing, 4px corner radius, 2px vertical and 4px horizontal padding.

**`badge-sale`** — Amber badge (#ffe8a1 / #856404) for sale or clearance items. Same sizing and typography as the stock badge.

**`badge-special`** — Teal badge (#abdde5 / #0c5460) for special editions, imports, or rare pressings. Same sizing and typography.

### Filters & Pagination
**`filter-dropdown`** — Genre, format, and condition selectors rendered as 36px inputs with 8px corner radius, white background, and a 1px {colors.hairline} border. Uses system-native dropdown styling — no custom chevron or animation.

**`pagination-button`** — Page number buttons at the bottom of search results. 36px height, 8px corner radius, white background with {colors.hairline} border. Active page uses {colors.primary} background with white text. Hover state adds a subtle background tint.

### Footer
**`footer`** — Full-width dark band (#111111) at the bottom of every page. Contains store information, hours, location, and links to policies. Text in {colors.muted} (#868e96) with link hover states shifting to white. 48px vertical padding on top and bottom, 24px horizontal padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item per row); top-nav collapses to hamburger menu; search bar moves below nav; badges stack vertically; filter dropdowns become full-width |
| Tablet | 744–1128px | Two-column product grid; top-nav links visible but condensed; search bar remains in nav; filter dropdowns in a horizontal row |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links; search bar with expanded width; filter sidebar on left |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px centered; filter sidebar remains; additional whitespace around product cards |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px touch target height on mobile.
- Product cards have a minimum 120px height to ensure tap targets for title, artist, and price are adequately spaced.
- Filter dropdowns and pagination buttons are 36px minimum height on mobile, with 8px padding to prevent accidental taps.
- Badges are 20px minimum height to remain tappable on small screens.

### Collapsing Strategy
- Top navigation collapses to a hamburger icon at < 744px, revealing a full-screen overlay menu with links and store information.
- Product grid collapses from 4 columns to 1 column on mobile, with album art scaling to full width.
- Filter sidebar collapses to a horizontal scroll strip on tablet, and to a single "Filter" button on mobile that opens a bottom sheet.
- Search bar collapses from an expanded input with placeholder text to a compact icon-only button on mobile, expanding to full width on tap.
- Footer links collapse from a multi-column layout to a single vertical stack on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex colors are heavily weighted toward Bootstrap alert and badge defaults (success green, danger red, warning amber, info teal) — the brand's true accent palette may be more limited. The deep indigo (#004085) and black (#111111) are the most distinctive and likely represent the brand's primary and ink colors, but this is an inference.
- No font-family declarations beyond system stacks were found — the brand may use a custom typeface on non-extracted pages or in imagery.
- Hover and focus states for most components are inferred from common patterns; the live site may use different transitions or color shifts.
- Error and validation styling (form errors, out-of-stock messages, search-no-results) could not be extracted.
- Dark mode support is unknown — the site's heavy use of black ink suggests it may already function as a de facto dark mode.
- Checkout flow styling (cart page, payment forms, order confirmation) was not captured.
- Mobile navigation animation and overlay behavior are inferred from common patterns; the actual implementation may differ.
- The extracted palette includes several colors (#1b1e21, #1d2124, #bd2130, #d39e00, #1e7e34, #117a8b) that appear to be Bootstrap utility classes rather than intentional brand colors — these should be verified against the live design.
