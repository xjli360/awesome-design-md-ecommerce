---
version: alpha
name: "Jackpot Records"
source_url: "https://jackpotrecords.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A record store that feels like a basement archive lit by a single warm bulb, Jackpot Records uses a near-black canvas of `#303030` — not white — as its primary container, a deliberate inversion of the typical retail site. The palette is stripped to three values: the deep ink of `#303030` for headers and backgrounds, a silver-gray `#a9a9a9` for body copy and secondary text, and a soft off-white `#f1f1f1` for cards and surface highlights. There is no brand color in the traditional sense — no accent hue, no signature red or blue — which makes the site feel like a utilitarian catalog, a digital shelf where the product photography (album covers, movie posters) supplies all the color. Typography runs Arial and Helvetica Neue at modest weights, with display sizes rarely exceeding 24px; the site trusts its dense grid of vinyl spines and Blu-ray cases to do the visual work. Buttons are pill-shaped (`{rounded.full}`) but rendered in `#303030` on `#f1f1f1`, a quiet reversal of the usual light-on-dark CTA. The overall mood is that of a secondhand shop’s inventory sheet: functional, slightly worn, and entirely focused on the object.

colors:
  primary: "#303030"
  primary-active: "#1a1a1a"
  primary-disabled: "#606060"
  ink: "#303030"
  body: "#a9a9a9"
  muted: "#808080"
  muted-soft: "#999999"
  hairline: "#404040"
  hairline-soft: "#4a4a4a"
  canvas: "#303030"
  surface-soft: "#3a3a3a"
  surface-card: "#f1f1f1"
  on-primary: "#f1f1f1"
  on-card: "#303030"
  badge-new: "#a9a9a9"
  badge-sale: "#a9a9a9"
  star-rating: "#a9a9a9"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
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
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-card}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 23px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 36px
  icon-button-outline:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 36px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.surface-card}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 40px
  search-input:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    placeholderColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-card}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.on-card}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.on-card}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
  category-tab-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.surface-card}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    textColor: "{colors.body}"
    typography: "{typography.link}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.surface-card}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.base}"
  badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  loading-spinner:
    color: "{colors.body}"
    size: 24px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
    height: 32px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a dark pill (`{rounded.full}`) on the `#f1f1f1` card surface. Text is `{colors.on-primary}` at 14px weight 600. On hover, background shifts to `{colors.primary-active}` (`#1a1a1a`). Disabled state uses `{colors.primary-disabled}` (`#606060`). Secondary variant flips the relationship: `{colors.surface-card}` background with `{colors.on-card}` text, bordered only by the card edge.

**`button-secondary`** — Used for less prominent actions like "Add to Wishlist" or "View Details". Same pill shape and height as primary, but background is `{colors.surface-card}` and text is `{colors.on-card}`. Hover state adds a subtle `{colors.hairline}` border.

**`button-tertiary-text`** — A text-only button for inline actions like "Clear Filters" or "Cancel". No background, no border. Text color is `{colors.body}`. Hover state changes to `{colors.surface-card}`.

### Navigation
**`top-nav`** — A fixed-height 64px bar on the `{colors.canvas}` background. Contains the store logo (left), category links (center), and utility icons (cart, account, search — right). Nav links use `{typography.nav-link}` at 14px weight 600. Active link is `{colors.surface-card}`, inactive is `{colors.muted}`.

**`category-strip`** — A horizontal scrollable strip below the top nav, containing genre or format filters (Vinyl, CD, Blu-ray, etc.). Each tab is a pill (`{rounded.full}`) with `{spacing.sm}` horizontal padding. Active tab has `{colors.surface-soft}` background and `{colors.surface-card}` text; inactive tabs are transparent with `{colors.muted}` text.

### Cards
**`product-card`** — The core inventory unit: a `{colors.surface-card}` (`#f1f1f1`) rectangle with `{rounded.sm}` (4px) corners and 8px padding. Contains a square 1:1 product image (album art or movie poster) with `{rounded.sm}`, followed by title (`{typography.title-sm}`) and price (`{typography.body-md}`). An optional badge (e.g., "NEW", "SALE") sits in the top-left corner of the image, using `{colors.badge-new}` background and `{colors.canvas}` text in 10px uppercase.

### Forms
**`search-bar`** — A pill-shaped input (`{rounded.full}`) on `{colors.surface-soft}` background, 40px tall. Placeholder text in `{colors.muted}`. The input itself is transparent, inheriting the bar's background. A search icon (magnifying glass) sits at the left edge in `{colors.body}`.

**`quantity-selector`** — A compact 32px-tall control with minus/plus buttons and a numeric display. Background is `{colors.surface-soft}`, text is `{colors.body}`, corners are `{rounded.sm}`.

### Footer
**`footer`** — A dark section (`{colors.canvas}`) with `{spacing.xl}` vertical padding. Contains links in `{colors.body}` (`{typography.link}`) and legal/copyright text in `{colors.muted}` (`{typography.body-sm}`). Dividers between sections use `{colors.hairline}`.

### Loading & Feedback
**`loading-spinner`** — A 24px circular spinner in `{colors.body}`, used for async operations like loading more products or processing a cart update.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 items per row). Top nav collapses to hamburger menu. Category strip becomes a horizontal scroll with no visible labels — only icons. Search bar moves to a full-width row below the nav. Footer links stack vertically. |
| Tablet | 744–1128px | Two-column product grid (3–4 items per row). Top nav shows limited links (Home, Vinyl, Movies, More). Category strip shows text labels for top 4 genres. Search bar remains in nav but shrinks to 200px. |
| Desktop | 1128–1440px | Three-column product grid (4–5 items per row). Full top nav with all category links. Category strip shows all genre labels. Search bar expands to 320px. Footer displays in a 3-column layout. |
| Wide | > 1440px | Four-column product grid (6 items per row). Max-width container at 1440px, centered. Category strip has extra padding. Search bar max-width 400px. |

### Touch Targets
- All buttons and interactive elements minimum 44px height (primary, secondary, icon buttons).
- Category tabs and nav links minimum 36px height.
- Quantity selector buttons minimum 32px height.
- Search bar minimum 40px height.
- Product card tap target (entire card) links to product detail page.

### Collapsing Strategy
- Top nav links collapse into a hamburger menu at < 744px.
- Category strip collapses to icon-only pills at < 744px.
- Product grid reduces columns from 6 to 2 as viewport shrinks.
- Footer links stack vertically on mobile.
- Search bar moves from inline in nav to full-width below nav on mobile.
- Sidebar filters (if present) collapse into a bottom sheet or modal on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Extracted only static colors. Hover, focus, and active states for buttons, links, and cards are inferred from primary-active and primary-disabled values — actual site behavior may differ.
- **Error styling**: No error states (form validation, 404 page, empty search results) were extractable. The page title "Something went wrong" suggests a generic error page exists, but its design is unknown.
- **Dark mode**: The site already uses a dark canvas (`#303030`), so a separate dark mode may not exist. However, the `#f1f1f1` cards suggest a light-content-on-dark-background pattern that could invert for accessibility.
- **Sub-brand palettes**: No secondary brand colors (e.g., for sale badges, genre tags, or promotional banners) were found. The `badge-new` and `badge-sale` tokens use the generic `#a9a9a9` — actual badges may have distinct colors.
- **Typography scale**: Only system fonts (Arial, Helvetica) were detected. The site may use a custom font loaded via JavaScript or a third-party service that wasn't captured. The typography tokens above are best-guess sizes based on common e-commerce patterns.
- **Spacing scale**: The spacing tokens are standard increments. Actual site spacing may vary, especially for product card padding and grid gaps.
- **Animation & transitions**: No CSS transitions or animation properties were extracted. The site likely uses simple fades or slides for modals and menus, but specifics are unknown.
- **Accessibility**: No focus ring styles, ARIA labels, or contrast ratios were extractable. The `#a9a9a9` body text on `#303030` background has a contrast ratio of approximately 4.5:1 (WCAG AA for normal text), but this should be verified.
- **Checkout flow**: As a Shopify site, the checkout is handled by Shopify's default UI, which may use different colors (e.g., Shopify green `#5e8e3e` or blue `#007bff`). The extracted colors filtered out framework defaults, but the checkout may still have its own palette.
- **Product detail page**: The design of the product detail page (larger image, description, add-to-cart button, reviews) was not extractable from the available hints. The `product-card` component covers the listing view only.
- **Mobile navigation**: The hamburger menu and its submenu styling (slide-in, dropdown, etc.) are not documented. The collapse strategy assumes a standard pattern.
