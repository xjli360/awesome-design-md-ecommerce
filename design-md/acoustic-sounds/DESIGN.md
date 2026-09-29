---
version: alpha
name: "Acoustic Sounds"
source_url: "https://acousticsounds.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep-catalog audiophile label and retailer that treats the record as an engineered artifact, not a nostalgic object. The palette is anchored on a deep teal (#006080) that reads like the felt of a turntable platter or the quiet glow of a preamp — it appears on every primary CTA, the top nav bar, and the site’s footer, establishing a consistent voltage that never competes with the album art. A secondary orange (#f04124) and a supporting amber (#794b02) serve as price tags, sale badges, and limited-edition flags, while a muted green (#43ac6a) signals in-stock availability and checkout confidence. The canvas is a warm off-white (#f5f5f5) rather than pure white, softening the reading experience across long browsing sessions. Typography runs Open Sans at modest weights (400 for body, 600 for headings) with generous line-height — the brand trusts album covers and track lists to carry the visual load rather than heavy display type. Buttons are softly rectangular (`{rounded.sm}`), product cards use `{rounded.md}` with a subtle border from `{colors.hairline}`, and the search bar sits as a full-width field rather than a pill, prioritizing scannability over friendliness. The overall mood is that of a well-lit listening room: serious but not cold, detailed but not fussy.

colors:
  primary: "#006080"
  primary-active: "#00526e"
  primary-disabled: "#b0d4e0"
  accent-orange: "#f04124"
  accent-orange-active: "#d32a0e"
  accent-amber: "#794b02"
  accent-green: "#43ac6a"
  accent-green-active: "#358753"
  ink: "#222222"
  body: "#444444"
  muted: "#6f6f6f"
  muted-soft: "#999999"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  canvas: "#f5f5f5"
  surface-soft: "#e7e7e7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent-orange: "#ffffff"
  on-accent-amber: "#ffffff"
  on-accent-green: "#ffffff"
  alert-bg: "#fcf8e3"
  alert-border: "#d08002"
  success-bg: "#dff0d8"
  success-border: "#3c9a5f"
  error-bg: "#f2dede"
  error-border: "#ea2f10"
  info-bg: "#d9edf7"
  info-border: "#0079a1"

typography:
  display-xl:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-lg:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: -0.2px
  display-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 21px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
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
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
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
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-accent-orange}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-accent-orange-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.on-accent-orange}"
    rounded: "{rounded.sm}"
  button-accent-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-accent-green}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-accent-green-active:
    backgroundColor: "{colors.accent-green-active}"
    textColor: "{colors.on-accent-green}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
  button-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
  text-input-error:
    borderColor: "{colors.accent-orange}"
    backgroundColor: "{colors.error-bg}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-link:
    color: "{colors.on-primary}"
    typography: "{typography.nav-link}"
  nav-link-active:
    color: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    borderColor: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    borderColor: "{colors.hairline}"
  product-card-hover:
    borderColor: "{colors.primary}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.accent-amber}"
  product-card-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-accent-orange}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-accent-amber}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-badge-stock:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-accent-green}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
  footer-link:
    color: "{colors.on-primary}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
  category-tab-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  alert:
    backgroundColor: "{colors.alert-bg}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.alert-border}"
  alert-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.ink}"
    borderColor: "{colors.success-border}"
  alert-error:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.ink}"
    borderColor: "{colors.error-border}"
  alert-info:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.ink}"
    borderColor: "{colors.info-border}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and "Sign In". Rendered in `{colors.primary}` with white text and `{rounded.sm}` corners. On hover, shifts to `{colors.primary-active}`. When disabled, fades to `{colors.primary-disabled}` with no pointer events.

**`button-accent-orange`** — Used for high-urgency actions like "Buy Now" or "Limited Stock". Uses `{colors.accent-orange}` background with white text. Active state uses `{colors.accent-orange-active}`. Typically paired with a `{product-card-badge-sale}` to reinforce urgency.

**`button-accent-green`** — Reserved for confirmatory actions like "In Stock" notifications or "Proceed to Secure Checkout". Uses `{colors.accent-green}` with active state `{colors.accent-green-active}`.

**`button-secondary`** — Outline-style button for less prominent actions like "View Details" or "Cancel". Uses `{colors.canvas}` background with `{colors.ink}` text and a 1px `{colors.hairline}` border. On hover, background shifts to `{colors.surface-soft}`.

**`button-link`** — Text-only button for navigational actions like "See all" or "Learn more". Uses `{colors.primary}` text color and `{typography.link}` styling. Underline appears on hover.

### Cards
**`product-card`** — The core content container for vinyl records, SACDs, and equipment listings. White background (`{colors.surface-card}`), `{rounded.md}` corners, and a 1px `{colors.hairline}` border. On hover, the border shifts to `{colors.primary}`. Contains album art (typically a square image), title (`{typography.title-sm}`), artist name (`{typography.body-sm}`), price (`{typography.price}` in `{colors.accent-amber}`), and optional badges.

**`product-card-badge`** — Small uppercase label pinned to the top-left of the product image. Uses `{colors.accent-orange}` background for "New Arrival" or "Limited Edition". Sale badges use `{colors.accent-amber}`. In-stock badges use `{colors.accent-green}`. All badges use `{typography.badge}` with `{rounded.xs}` corners.

### Navigation
**`nav-bar`** — Fixed top navigation bar with `{colors.primary}` background and white text. Height is 48px. Contains the brand logo (left), category links (center), and search/account icons (right). Active nav links have a 2px white bottom border.

**`category-strip`** — Horizontal scrollable strip below the nav bar for genre and format filtering (e.g., "Vinyl", "SACD", "DVD-Audio", "Jazz", "Classical"). Background is `{colors.surface-soft}`. Active category tabs use `{colors.primary}` background with white text; inactive tabs use `{colors.canvas}` with `{colors.body}` text. All tabs use `{rounded.sm}`.

### Forms
**`text-input`** — Standard input field for search, account forms, and checkout. White background, `{colors.hairline}` border, `{rounded.sm}` corners, and `{typography.body-md}` text. On focus, border shifts to `{colors.primary}`. Error state uses `{colors.accent-orange}` border with `{colors.error-bg}` background.

**`search-bar`** — Full-width text input used in the nav bar and on search results pages. Same styling as `text-input` but with a search icon inset on the left. Placeholder text uses `{colors.muted}`.

### Alerts
**`alert`** — Informational banner for system messages, shipping updates, or promotional notices. Uses `{colors.alert-bg}` (yellow) background with `{colors.alert-border}` (amber) left border. Success variant uses `{colors.success-bg}` (green) with `{colors.success-border}`. Error variant uses `{colors.error-bg}` (red) with `{colors.error-border}`. Info variant uses `{colors.info-bg}` (blue) with `{colors.info-border}`. All alerts use `{rounded.sm}` and `{typography.body-sm}`.

### Footer
**`footer`** — Full-width footer with `{colors.primary}` background and white text. Contains columns for customer service, account links, and brand information. Links use `{colors.on-primary}` with `{typography.link}` styling. Social icons are rendered in white. The footer includes a copyright line in `{typography.caption}`.

### Pagination
**`pagination`** — Page navigation for product listings and search results. Inactive page numbers use `{colors.canvas}` background with `{colors.body}` text. Active page uses `{colors.primary}` background with white text and `{rounded.sm}`. Previous/Next arrows are text-only links using `{colors.primary}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item per row), nav bar collapses to hamburger menu, category strip becomes a dropdown, search bar moves below nav, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, nav bar shows top-level categories only, category strip remains horizontal but scrollable, search bar remains in nav |
| Desktop | 1128–1440px | Three-column product grid, full nav bar with all categories, category strip fully visible, search bar in nav, footer has 4-column layout |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, nav bar and footer expand to full width |

### Touch Targets
- All buttons and links: minimum 44x44px tap target
- Category strip items: minimum 48px height for touch scrolling
- Product card images: full card width, minimum 200px height
- Search bar: full width on mobile, minimum 40px height
- Nav bar hamburger icon: 44x44px tap target

### Collapsing Strategy
- Nav bar: On mobile, all category links collapse into a slide-out hamburger menu. The logo and search icon remain visible.
- Category strip: On mobile, the horizontal strip is replaced by a select dropdown for genre/format filtering.
- Product grid: Columns reduce from 4 to 1 on mobile, ensuring album art remains legible.
- Footer: On mobile, the 4-column layout collapses to a single column with accordion-style expandable sections.
- Search bar: On mobile, the search bar moves from the nav bar to a dedicated row below, expanding to full width.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list is dominated by Bootstrap-like defaults (blues, grays, greens) and may include checkout-widget colors (Klarna, Afterpay) that are not part of the brand's design system. The most distinctive brand colors appear to be the deep teal (#006080) and the orange (#f04124), but the exact primary may differ on pages not sampled.
- Font-family declarations were limited to system fonts and Open Sans. The brand may use a custom typeface for display headings that was not captured in the extraction.
- Hover and active states for most components were inferred from common patterns and may not match the live site exactly.
- Error, success, and info alert colors were extracted from Bootstrap-style classes and may not be the brand's preferred palette.
- Dark mode is not supported and no dark-mode tokens were extracted.
- The brand's sub-brand or label-specific palettes (e.g., Analogue Productions, Universal Audio) were not captured.
- Spacing and sizing values are estimated based on common e-commerce patterns and may not reflect the exact pixel values used on the live site.
- The product card badge positioning and size are inferred; the live site may use different dimensions or placement.
