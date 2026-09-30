---
version: alpha
name: "J-Subculture"
source_url: "https://www.j-subculture.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  An import shop that feels like a well-organized warehouse aisle lit by fluorescent tubes and staffed by people who know exactly where every SKU lives. The palette is almost entirely system — #337ab7 (a mid-blue that suggests a corporate portal rather than a boutique), #777777 for body text, #eeeeee for backgrounds, and a full suite of Bootstrap alert colors (#3c763d green, #8a6d3b yellow, #a94442 red, #31708f teal) that the site uses for shipping statuses, stock warnings, and membership tier badges. There is no brand color in the conventional sense; the most distinctive accent is #337ab7, which appears on primary CTAs and the top nav, but it reads as a framework default rather than a deliberate choice. The typography stack is equally utilitarian — Arial, Helvetica Neue, and sans-serif for body copy, with monospace (Consolas, Monaco, Menlo) reserved for product codes and tracking numbers that appear in small, tightly-spaced tables. Rounded corners are minimal: buttons use `{rounded.xs}` (4px), cards use `{rounded.sm}` (8px), and the search bar is a simple rectangle with `{rounded.none}`. The site prioritizes density over whitespace — product listings stack in tight grids with 8px gaps (`{spacing.sm}`), and every inch of the viewport carries information: prices in bold, stock counts in muted gray, shipping estimates in green badges. The overall impression is of a tool, not a destination — a proxy shopping service that wants you to find your item, add it to cart, and move on.

colors:
  primary: "#337ab7"
  primary-active: "#286090"
  primary-disabled: "#9d9d9d"
  ink: "#080808"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#9d9d9d"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#3c763d"
  success-bg: "#dff0d8"
  success-border: "#d6e9c6"
  warning: "#8a6d3b"
  warning-bg: "#fcf8e3"
  warning-border: "#faebcc"
  danger: "#a94442"
  danger-bg: "#f2dede"
  danger-border: "#ebccd1"
  info: "#31708f"
  info-bg: "#d9edf7"
  info-border: "#bce8f1"
  badge-green: "#5cb85c"
  badge-blue: "#5bc0de"
  badge-yellow: "#f0ad4e"
  badge-red: "#d9534f"
  badge-green-hover: "#449d44"
  badge-blue-hover: "#31b0d5"
  badge-yellow-hover: "#ec971f"
  badge-red-hover: "#c9302c"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  mono-code:
    fontFamily: "Consolas, Menlo, Monaco, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  mono-sm:
    fontFamily: "Consolas, Menlo, Monaco, monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
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
    padding: 8px 16px
    height: 36px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  button-secondary-hover:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  button-success:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 30px
  button-danger:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 30px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 36px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 1px {colors.primary}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 36px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 50px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-link:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.md}"
  nav-bar-link-active:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.xs}"
    height: 200px
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-stock:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xxs}"
  product-card-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    border: "1px solid {colors.success-border}"
  badge-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning}"
    border: "1px solid {colors.warning-border}"
  badge-danger:
    backgroundColor: "{colors.danger-bg}"
    textColor: "{colors.danger}"
    border: "1px solid {colors.danger-border}"
  badge-info:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.info}"
    border: "1px solid {colors.info-border}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 1px {colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.base}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.md}"
    borderBottom: "2px solid {colors.hairline}"
  table-cell:
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  table-cell-mono:
    textColor: "{colors.body}"
    typography: "{typography.mono-code}"
    padding: "{spacing.sm} {spacing.md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  pagination-link:
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.sm}"
    rounded: "{rounded.xs}"
  pagination-link-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.sm}"
    rounded: "{rounded.xs}"
  pagination-link-disabled:
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.sm}"
    rounded: "{rounded.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and "Sign In". A solid blue rectangle with white text, minimal 4px rounding, and compact 8px vertical padding. On hover, darkens to `{colors.primary-active}` (#286090). Disabled state uses `{colors.primary-disabled}` (#9d9d9d) to signal non-interactivity. **`button-secondary`** — A gray-toned alternative for "Cancel", "Back", and secondary actions. Uses `{colors.surface-soft}` background and darkens to `{colors.hairline}` on hover. **`button-success`** and **`button-danger`** — Smaller, colored buttons used for inline actions like "Confirm Shipment" (green) or "Cancel Order" (red). These use `{typography.button-sm}` and tighter 6px vertical padding to fit inside table rows and card footers.

### Cards
**`product-card`** — The primary content container for product listings. A white rectangle with 8px rounding, a thin `{colors.hairline}` border, and 8px padding. The image area occupies the top 200px with `{rounded.xs}` corners. Below, the title uses `{typography.title-sm}` in `{colors.ink}`, the price uses `{typography.title-md}` for emphasis, and stock status appears as a `{typography.caption}` in `{colors.muted}`. A badge component overlays the top-right corner of the image for sale, pre-order, or limited-edition flags.

### Badges
**`badge-success`**, **`badge-warning`**, **`badge-danger`**, **`badge-info`** — Status indicators used across the site for shipping states, stock levels, and membership tiers. Each has a tinted background, matching text color, and a subtle border. Success (green) signals "In Stock" or "Shipped", warning (yellow) signals "Low Stock" or "Pending", danger (red) signals "Out of Stock" or "Cancelled", and info (blue) signals "Pre-Order" or "New Arrival". Badges are compact — 2px vertical padding, 6px horizontal, 4px rounding — and sit inline with text or inside card overlays.

### Navigation
**`nav-bar`** — A fixed 50px top bar with white background and a single `{colors.hairline}` bottom border. Links use `{typography.nav-link}` (13px bold) in `{colors.primary}` with 12px horizontal padding. The active link switches to `{colors.ink}` and gains a 2px `{colors.primary}` bottom border. The nav contains category links (Anime, Manga, Figures, Electronics, etc.) and a cart icon with a badge count.

### Forms
**`text-input`** and **`select-input`** — Standard form controls with 36px height, 4px rounding, and a `{colors.hairline}` border. On focus, the border shifts to `{colors.primary}` with a 1px box-shadow ring. Used for search queries, shipping addresses, and payment forms. The select input uses the same dimensions but includes a dropdown arrow (browser default).

### Search
**`search-bar`** — A rectangular input with no rounding, 40px height, and a `{colors.hairline}` border. On focus, it gains a `{colors.primary}` border and shadow. The search bar sits prominently at the top of the page, often accompanied by a category dropdown and a submit button using `{button-primary}`. No pill shapes or rounded corners — the design favors utility over friendliness.

### Tables
**`table-header`** and **`table-cell`** — Used extensively for order histories, tracking details, and product specifications. Headers have a `{colors.surface-soft}` background and bold text. Cells use `{typography.body-sm}` with `{colors.hairline-soft}` bottom borders. For tracking numbers and product codes, `{table-cell-mono}` switches to `{typography.mono-code}` (Consolas/Menlo) for precise readability.

### Pagination
**`pagination-link`** — A series of numbered links at the bottom of product listings. Active page uses `{colors.primary}` background with white text; inactive pages use `{colors.primary}` text on transparent background. Disabled links (first/last page) fade to `{colors.muted-soft}`. Each link has 4px rounding and compact 4px/8px padding.

### Footer
**`footer`** — A full-width section with `{colors.surface-soft}` background and a `{colors.hairline}` top border. Contains links to Help, About, Terms, and Privacy in `{colors.primary}`. Text is `{typography.body-sm}` in `{colors.muted}`. Padding is generous at 24px vertical and 16px horizontal, providing breathing room after the dense product grids above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Product cards stack in single column; nav bar collapses to hamburger menu; tables become scrollable horizontally; search bar reduces to icon-only on load |
| Tablet | 768–1024px | Product cards in 2-column grid; nav links remain visible but reduce font size; tables show full width with horizontal scroll on overflow |
| Desktop | 1024–1440px | Product cards in 3–4 column grid; full nav bar visible; search bar with category dropdown visible; tables display normally |
| Wide | > 1440px | Product cards in 4–5 column grid; max-width container at 1440px; additional whitespace on sides |

### Touch Targets
- All buttons and links: minimum 44x44px tap target (enforced via padding and height)
- Nav bar links: 50px height ensures comfortable tapping
- Product card images: 200px height with tap-to-zoom
- Pagination links: 36px height with 8px horizontal padding
- Form inputs: 36px height with 12px padding

### Collapsing Strategy
- Top nav collapses to hamburger menu below 768px; menu slides in from left
- Product grid collapses from 4 columns to 2 to 1 as viewport shrinks
- Tables with more than 4 columns become horizontally scrollable on mobile
- Footer links stack vertically on mobile (single column)
- Search bar collapses to icon-only on mobile; expands to full input on tap
- Sidebar filters (category, price range) collapse to a toggleable drawer below 768px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted hover states for secondary buttons, links, or badges beyond what's listed — hover colors for `button-success`, `button-danger`, and badge variants are inferred from Bootstrap defaults
- No extracted active/focus states for form inputs beyond the primary blue ring — error states, success states, and validation styling are unknown
- No extracted dark mode or high-contrast mode — the site appears to use only light mode
- No extracted animation or transition durations — hover effects likely use instant color swaps without easing
- No extracted spacing for mobile-specific layouts — responsive padding/margins are estimated
- No extracted font weights beyond 400 and 700 — the site may use 600 for some headings but it's not distinguishable from 700 in extraction
- No extracted brand-specific icons or illustrations — the site likely uses generic Font Awesome or Glyphicons (Glyphicons Halflings found in font stack)
- No extracted color for the cart badge count — likely uses `{colors.badge-red}` (#d9534f) but not confirmed
- The extracted color palette is dominated by Bootstrap defaults (#337ab7, #5cb85c, #d9534f, etc.) — the brand's true primary may be different if custom CSS overrides exist but weren't captured
- No extracted typography scale for mobile — all font sizes are desktop estimates
- No extracted border-radius for modals, tooltips, or dropdowns — these may use different rounding than the listed components
