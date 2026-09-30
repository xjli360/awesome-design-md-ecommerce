---
version: alpha
name: "StarTech"
source_url: "https://www.startech.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A utilitarian, information-dense industrial brand that speaks through a restrained palette of #404040 ink, #ebebeb surface, and #bd2426 signal red — the single accent that marks every "Add to Cart," "Buy Now," and critical alert. The brand lives in a world of spec sheets, compatibility matrices, and port diagrams; typography runs system-native (-apple-system, Arial, Helvetica Neue) at modest sizes with zero decorative weight, trusting clarity over character. Navigation is a dense horizontal strip of category links (Docking Stations, Cables, Adapters, Mounts) with a prominent search bar and a persistent cart badge, all on a #ffffff canvas. Product cards are tight rectangles with a 4:3 thumbnail, a model number in bold, a truncated description, and a price block anchored by the red CTA — no whitespace is wasted. The secondary palette of #62a1d8 (informational blue), #9bca3e (compatibility green), and #f68b1f (warning orange) forms a semaphore system for status badges: "In Stock" in green, "Discontinued" in orange, "New" in blue. Corners are minimal — 4px on buttons, 8px on cards — and the overall feel is that of a well-organized warehouse catalog rendered as a web page, where every pixel earns its place by conveying a fact.

colors:
  primary: "#bd2426"
  primary-active: "#a01e20"
  primary-disabled: "#e8a0a1"
  ink: "#404040"
  body: "#595959"
  muted: "#737373"
  muted-soft: "#bfbfbf"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  info-blue: "#62a1d8"
  success-green: "#9bca3e"
  warning-orange: "#f68b1f"
  error-red: "#de5052"
  stock-green: "#516b1d"
  link-blue: "#0051c3"
  badge-new: "#2f7bbf"
  badge-discontinued: "#904b06"
  dark-bg: "#272727"
  dark-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.47
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
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
    padding: 9px 19px
    height: 40px
  button-tertiary-link:
    backgroundColor: transparent
    textColor: "{colors.link-blue}"
    typography: "{typography.link}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
  text-input-focus:
    borderColor: "{colors.info-blue}"
    boxShadow: "0 0 0 2px rgba(98, 161, 216, 0.3)"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.title-md}"
    color: "{colors.primary}"
  product-card-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-in-stock:
    backgroundColor: "{colors.success-green}"
    textColor: "{colors.on-primary}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
  badge-discontinued:
    backgroundColor: "{colors.warning-orange}"
    textColor: "{colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
    height: 40px
  search-bar-focus:
    borderColor: "{colors.info-blue}"
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.dark-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    typography: "{typography.title-sm}"
  spec-table-row-alt:
    backgroundColor: "{colors.surface-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in #bd2426 signal red with white text and 4px corners. Used exclusively for "Add to Cart," "Buy Now," and "Checkout" actions. On hover, darkens to #a01e20; disabled state fades to #e8a0a1 with white text. Height is 40px with 10px vertical padding and 20px horizontal padding.

**`button-secondary`** — A white button with #404040 text and a 1px #dedede border, used for "Learn More," "Compare," and "View Details" actions. Same 40px height and 4px corners as primary, but with 9px top/bottom padding to account for the border. Hover state adds a 1px #404040 border.

**`button-tertiary-link`** — A text-only link styled as a button, using #0051c3 link blue. Used for "View Specs," "Download Driver," and "Support" actions. No background, no border, no padding — just the link typography token.

### Cards
**`product-card`** — A white card with 8px corners and 16px padding, containing a 4:3 aspect ratio thumbnail, model number in title-sm, a truncated description in body-sm, and a price block. The price is rendered in title-md with the primary red color. Hover state adds a subtle box-shadow. Badges appear in the top-left corner with 4px corners and uppercase 11px text.

**`badge-in-stock`** — Green (#9bca3e) badge with white text, used to indicate immediate availability. 4px corners, 2px vertical padding, 6px horizontal padding.

**`badge-new`** — Blue (#2f7bbf) badge for newly released products. Same dimensions as in-stock badge.

**`badge-discontinued`** — Orange (#f68b1f) badge for end-of-life products. Same dimensions.

### Navigation
**`nav-bar`** — A 56px white bar with a sticky position on scroll. Contains the StarTech logo on the left, a dense horizontal strip of category tabs in the center, a search bar, and a cart icon with a badge count on the right. On scroll, a subtle 1px shadow appears below the bar.

**`category-tab`** — A text-only tab in #737373 muted gray, with 8px vertical and 12px horizontal padding. The active tab uses #404040 ink color with a 2px #bd2426 bottom border.

**`search-bar`** — A 40px tall input with 4px corners, white background, and #dedede border. On focus, the border shifts to #62a1d8 info blue with a 2px blue ring.

### Forms
**`text-input`** — A 40px tall input field with 4px corners, 8px vertical and 12px horizontal padding. Uses body-md typography. Focus state shows a #62a1d8 border with a 2px rgba(98, 161, 216, 0.3) box-shadow ring.

### Footer
**`footer`** — A dark (#272727) footer section with white text, 48px vertical padding. Links are rendered in #bfbfbf muted-soft color with link typography. The footer contains columns for Support, Company, Resources, and Connect.

### Spec Table
**`spec-table`** — A full-width table with #dedede borders, used on product detail pages to display technical specifications. Headers use a #f5f5f5 background with title-sm typography. Alternating rows use the same light background for readability.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row), nav collapses to hamburger menu, category tabs hidden, search bar becomes icon-only, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid (2 cards per row), nav shows 4-5 category tabs with overflow menu, search bar visible with reduced width, footer in 2-column layout |
| Desktop | 1128–1440px | Three-column product grid (3 cards per row), full category tab strip visible, search bar at full width, footer in 4-column layout |
| Wide | > 1440px | Four-column product grid (4 cards per row), max-width container at 1440px centered, additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px touch target (40px height + padding)
- Nav links have 44px minimum tap area
- Product card CTAs are 40px tall with 20px horizontal padding
- Search bar is 40px tall with 12px padding

### Collapsing Strategy
- On mobile, the full category nav collapses into a hamburger menu with a slide-out drawer
- The product grid collapses from 4 columns to 1 column
- The search bar collapses to a magnifying glass icon that expands on tap
- The footer collapses from 4 columns to a single stacked column
- Spec tables on mobile become horizontally scrollable or collapse to a key-value list view

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the Cloudflare-blocked page; the above are best guesses based on common patterns
- Error state styling for form inputs (red border, error message typography) is not confirmed
- Dark mode or high-contrast mode variants are not present in the extracted data
- The exact spacing scale (padding, margins) is inferred from common e-commerce patterns; the extracted CSS did not include spacing variables
- The typography scale is reconstructed from system font stacks; the brand may use custom weights or sizes not captured
- The Cloudflare challenge page prevented extraction of actual product page layouts, hero banners, and interactive states
- Sub-brand or regional color variations (e.g., StarTech Canada, StarTech EU) are unknown
- The extracted color list includes many grays and accent colors that may be from stock images or UI chrome rather than brand tokens; the primary red (#bd2426) and secondary accents are the most likely brand colors
- Animation and transition durations/easings are not available
- Iconography style (line vs. filled, stroke weight) could not be determined
