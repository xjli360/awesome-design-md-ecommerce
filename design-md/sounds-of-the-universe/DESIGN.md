---
version: alpha
name: "Sounds of the Universe"
source_url: "https://www.soundsoftheuniverse.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A dark, monochrome storefront where #313131 ink dominates the canvas — not as a background but as the primary brand voltage, appearing in navigation bars, product titles, and button fills with the weight of a record sleeve. The site reads like a crate-digger’s notebook: dense, text-forward, and unapologetically utilitarian, with system fonts (Apple system stack, Roboto, Helvetica Neue) doing all the work. There are no decorative illustrations, no hero photography — just rows of album covers in a tight grid, each one a 200px square with a white border (`{rounded.xs}`) and the title set in `{typography.body-sm}` beneath it. The search bar sits at the top in a full-width `{rounded.none}` strip, not a pill, and the primary CTA (“Add to Basket”) is a solid `{colors.primary}` rectangle with `{rounded.sm}` corners and white text. Category navigation runs as a horizontal scroll of text links in `{colors.muted}` with a single `{colors.ink}` underline on the active state. The overall feel is that of a record shop that trusts its inventory over its interface — the design steps back and lets the album art speak.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#7a7a7a"
  muted-soft: "#9e9e9e"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#313131"
  link-hover: "#1a1a1a"
  badge-new: "#e63946"
  badge-sale: "#2a9d8f"
  star-rating: "#313131"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  nav-link-muted:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  icon-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.badge-new}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link-muted}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link-muted}"
    borderBottom: "1px solid {colors.hairline-soft}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-artist:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-sm}"
    fontWeight: 600
    marginTop: "{spacing.xs}"
  badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
    fontWeight: 600
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
  filter-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "6px 14px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for “Add to Basket” and checkout flows. Solid `{colors.primary}` fill with white text, `{rounded.sm}` corners, and a 44px height that meets touch-target minimums. On hover, shifts to `{colors.primary-active}` (#1a1a1a). Disabled state uses `{colors.primary-disabled}` (#a0a0a0) with no hover shift.

**`button-secondary`** — An outlined alternative for secondary actions like “View Details” or “Save for Later”. White background with `{colors.ink}` text and a 1px `{colors.hairline}` border. Maintains the same 44px height and `{rounded.sm}` corners as the primary button for visual consistency.

**`button-tertiary-text`** — A text-only button used for inline actions like “Clear filters” or “Cancel”. No background, no border, uses `{colors.ink}` at `{typography.button-md}`. Hover state adds a subtle underline.

**`button-pill`** — A compact, fully rounded button used for genre tags or quick-filter chips. Smaller padding (8px 20px) and `{typography.button-sm}`. Used in the category strip for active filter indicators.

### Cards
**`product-card`** — The core inventory unit: a tight 200px square album cover image with `{rounded.xs}` corners, followed by the title in `{typography.title-sm}`, the artist name in `{colors.muted}` `{typography.caption}`, and the price in bold `{typography.body-sm}`. The card itself has no background fill — it relies on the white canvas and the album art’s own color. On hover, a subtle `{colors.surface-soft}` background appears behind the text block.

**`product-card-title`** — Album title set in 14px/600 weight, `{colors.ink}`. Truncated to one line with ellipsis for long titles.

**`product-card-artist`** — Artist name in 12px regular weight, `{colors.muted}`. Also single-line truncated.

**`product-card-price`** — Price in 14px/600 weight, `{colors.ink}`, with a 4px top margin from the artist line. For sale items, the original price is shown in `{colors.muted-soft}` with a strikethrough.

### Navigation
**`nav-bar`** — A 64px fixed top bar with white background and a 1px `{colors.hairline}` bottom border. Contains the store logo (text-based, no image) on the left, a full-width search bar in the center, and utility icons (cart, account) on the right. The search bar is a `{rounded.none}` rectangle with `{colors.surface-soft}` background — deliberately unpillowed.

**`nav-link-active`** — Active nav link with a 2px `{colors.primary}` bottom border underline. Text is `{colors.ink}` at 14px/600 weight.

**`nav-link-inactive`** — Inactive nav link in `{colors.muted}` at 14px/400 weight. No underline.

**`category-strip`** — A horizontal scrollable strip of genre/category links below the nav bar. White background, `{colors.muted}` text, 1px `{colors.hairline-soft}` bottom border. Active category uses `{colors.ink}` with a 2px `{colors.primary}` underline.

### Forms
**`text-input`** — Standard input field with white background, `{colors.hairline}` border, `{rounded.xs}` corners, and 44px height. On focus, the border thickens to 2px `{colors.primary}`. Error state uses a 2px `{colors.badge-new}` border.

**`select-dropdown`** — Matches the text-input styling but with a dropdown arrow icon. Same height, border, and corner radius.

**`quantity-selector`** — A compact input for cart quantities, with a `{colors.hairline}` border and `{rounded.xs}` corners. Contains a minus button, the quantity number, and a plus button, all in a single 44px-tall row.

### Footer
**`footer`** — A dark footer strip using `{colors.primary}` as background with white text. Contains three columns: “About Us”, “Customer Service”, and “Connect”. Links are white at `{typography.link}`. Padding is `{spacing.xl}` vertical, `{spacing.base}` horizontal.

### Badges
**`badge`** — A small uppercase label for “New Arrivals”, using `{colors.badge-new}` (#e63946) background with white text. `{rounded.xs}` corners, 2px 8px padding, 11px/700 weight.

**`badge-sale`** — Same shape as `badge` but with `{colors.badge-sale}` (#2a9d8f) background. Used for “Sale” or “Clearance” indicators.

### Search
**`search-bar`** — The primary search input, spanning the full width of the nav bar. `{colors.surface-soft}` background, `{rounded.none}`, 48px height. No border — the soft gray background distinguishes it from the white nav bar. Placeholder text in `{colors.muted-soft}`.

### Pagination
**`pagination`** — Page numbers in `{colors.muted}` at `{typography.body-sm}`. The active page gets a `{colors.primary}` background with white text and `{rounded.xs}` corners. Previous/Next arrows are text links in `{colors.muted}`.

### Filter Tags
**`filter-tag`** — A pill-shaped chip for active filters, using `{colors.surface-soft}` background with `{colors.ink}` text. 6px 14px padding, `{rounded.full}`. Active state uses `{colors.primary}` background with white text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 columns), nav bar collapses to hamburger menu, search bar moves below nav, category strip becomes a horizontal scroll, footer stacks to single column, product cards use full width with 2-up grid |
| Tablet | 744–1128px | Two-column product grid (3-4 columns), nav bar shows limited links with “More” dropdown, search bar remains in nav but shrinks width, category strip shows 6-8 visible items with scroll |
| Desktop | 1128–1440px | Three-column product grid (4-5 columns), full nav bar with all links visible, search bar at 400px max-width, category strip shows all items, footer in three columns |
| Wide | > 1440px | Four-column product grid (5-6 columns), max-width container at 1440px centered, search bar at 480px max-width, additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height (48px for primary CTA)
- Icon buttons are 36px × 36px with `{rounded.full}` corners
- Filter tags are 32px tall with generous 14px horizontal padding
- Product card images are at least 150px × 150px on mobile
- Category strip items have 24px padding for easy tapping

### Collapsing Strategy
- **Nav links**: On mobile (< 744px), all nav links collapse into a hamburger menu. The logo and cart icon remain visible.
- **Category strip**: On mobile, the category strip becomes a horizontal scroll with a fade gradient on the right edge to indicate more content.
- **Product grid**: Transitions from 2 columns (mobile) to 3-4 (tablet) to 4-5 (desktop) to 5-6 (wide). The grid uses CSS `auto-fill` with `minmax(180px, 1fr)`.
- **Footer**: On mobile, the three-column footer stacks vertically. Each section gets a collapsible accordion with a chevron toggle.
- **Search bar**: On mobile, the search bar moves from the nav bar to a full-width strip below it, with a dedicated search icon in the nav.
- **Breadcrumbs**: On mobile, breadcrumbs truncate to show only the current page and a “Back” link.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only primary button hover was extracted (#1a1a1a). All other hover states (links, cards, filter tags) are inferred from common patterns and may differ from the live site.
- **Error styling**: Text-input error state border color (#e63946) is inferred from the badge-new color — actual error styling may use a different red or include iconography.
- **Focus rings**: No focus-visible styles were extractable. The design likely uses browser defaults or a custom `{colors.primary}` outline.
- **Dark mode**: The site does not appear to have a dark mode variant. All extracted colors assume a light canvas.
- **Sub-brand palettes**: No secondary or tertiary brand colors were found beyond the single `#313131` primary. The badge colors (#e63946, #2a9d8f) are inferred from common ecommerce patterns.
- **Typography weights**: Only system font stacks were extracted. All font weights (400, 600, 700) are assumed based on common usage — the live site may use different weights for specific contexts.
- **Spacing scale**: The spacing tokens are based on a standard 4px/8px grid. Actual spacing on the live site may vary, especially in the product grid and footer.
- **Animation/transitions**: No transition durations or easing functions were extractable. The site likely uses simple 150-200ms ease transitions for hover states.
- **Checkout flow**: The extracted colors may include Shopify checkout widget colors (Klarna, Afterpay) that are not part of the brand’s design system. These have been excluded.
- **Social media icons**: Any social icon colors (Facebook blue, Twitter blue, Instagram gradient) were filtered out as they are not brand colors.
