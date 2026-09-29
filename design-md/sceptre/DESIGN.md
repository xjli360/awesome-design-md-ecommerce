---
version: alpha
name: "Sceptre"
source_url: "https://www.sceptre.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every pixel of Sceptre's storefront confesses that engineering specs outrank visual pageantry — the entire interface ships on an unmodified Bootstrap 3 scaffold, its primary action blue (#337ab7) borrowed whole-cloth from the framework default rather than tuned to a brand-specific hue. This is deliberate utility: a monitor company whose customers sort by panel size, refresh rate, and VESA compatibility has no reason to interpose a decorative layer between the shopper and the comparison table. Type is set in a system stack headed by Helvetica Neue and Arial at comfortable reading weights; display headings rarely exceed 600 weight, letting product photography — edge-to-edge panels floating on matte bezels — carry the visual authority. The surface architecture is binary: a pure white canvas (#ffffff) overlaid with #f5f5f5 panel wells that section product grids from spec tables, separated by #e5e5e5 hairlines. Body copy lives at #555555, a half-step lighter than true black, while secondary annotations drop to #777777 muted gray. Rounded corners are almost absent — cards and buttons sit at `{rounded.xs}` (4px) or `{rounded.none}`, reinforcing the rectilinear geometry of the monitors themselves. A full Bootstrap contextual palette (#5cb85c success, #f0ad4e warning, #d9534f danger, #5bc0de info) drives stock badges, alert banners, and validation states, giving the catalog a dashboard-like information density more familiar from B2B tooling than consumer retail. Navigation is flat and wide, black-on-white with hover underlines, collapsing into a hamburger on mobile with no animated transitions — page weight matters when the audience comparison-shops across fifteen tabs.

colors:
  primary: "#337ab7"
  primary-active: "#286090"
  primary-disabled: "#7baed4"
  ink: "#080808"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#9d9d9d"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  border-strong: "#e7e7e7"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#5cb85c"
  success-active: "#449d44"
  success-text: "#3c763d"
  success-surface: "#dff0d8"
  success-border: "#d6e9c6"
  info: "#5bc0de"
  info-active: "#31b0d5"
  info-text: "#31708f"
  info-surface: "#d9edf7"
  info-border: "#bce8f1"
  warning: "#f0ad4e"
  warning-active: "#ec971f"
  warning-text: "#8a6d3b"
  warning-surface: "#fcf8e3"
  warning-border: "#faebcc"
  danger: "#d9534f"
  danger-active: "#c9302c"
  danger-text: "#a94442"
  danger-surface: "#f2dede"
  danger-border: "#ebccd1"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 30px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: 0
  title-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  button-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  spec-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  spec-value:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  code:
    fontFamily: "Menlo, Monaco, Consolas, 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 12px
  lg: 20px
  xl: 32px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  base: 15px
  lg: 24px
  xl: 30px
  xxl: 48px
  section: 60px
  gutter: 15px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
    border: 1px solid #2e6da4
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    border: 1px solid #204d74
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.65
  button-primary-lg:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 46px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
    border: 1px solid #cccccc
  button-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
    border: 1px solid #4cae4c
  button-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
    border: 1px solid #d43f3a
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
    border: 1px solid #cccccc
    focusBorder: 1px solid #66afe9
    focusShadow: "inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102,175,233,.6)"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 50px
    padding: "{spacing.base}"
    borderBottom: none
  nav-bar-brand:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.title-lg}"
    height: 50px
  nav-bar-link:
    backgroundColor: transparent
    textColor: "#9d9d9d"
    typography: "{typography.nav-link}"
    hoverColor: "{colors.on-dark}"
    padding: 15px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
    hoverBorder: 1px solid {colors.hairline}
    shadow: none
  product-card-image:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    aspectRatio: "16/9"
    objectFit: contain
  product-card-title:
    textColor: "{colors.primary}"
    typography: "{typography.title-md}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 400px
    padding: "{spacing.section} {spacing.base}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.spec-value}"
    rounded: "{rounded.none}"
    borderCollapse: collapse
    cellPadding: 8px
    stripedBackground: "{colors.surface-soft}"
    border: 1px solid #dddddd
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.spec-label}"
    padding: 8px
    border: 1px solid #dddddd
  alert-success:
    backgroundColor: "{colors.success-surface}"
    textColor: "{colors.success-text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: 1px solid {colors.success-border}
  alert-info:
    backgroundColor: "{colors.info-surface}"
    textColor: "{colors.info-text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: 1px solid {colors.info-border}
  alert-warning:
    backgroundColor: "{colors.warning-surface}"
    textColor: "{colors.warning-text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: 1px solid {colors.warning-border}
  alert-danger:
    backgroundColor: "{colors.danger-surface}"
    textColor: "{colors.danger-text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: 1px solid {colors.danger-border}
  breadcrumb:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 15px
    separator: "/"
    activeColor: "{colors.muted}"
    linkColor: "{colors.primary}"
  category-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
    linkColor: "{colors.primary}"
    activeBackground: "{colors.surface-soft}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
    linkColor: "#9d9d9d"
    linkHoverColor: "{colors.on-dark}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    border: 1px solid #dddddd
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    disabledColor: "{colors.muted}"
  badge-stock:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 3px 7px
  badge-outofstock:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 3px 7px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 34px
    padding: 6px 12px
    border: 1px solid #cccccc
    buttonBackground: "{colors.primary}"
    buttonColor: "{colors.on-primary}"

## Components

### Buttons
**`button-primary`** — Standard Bootstrap-derived blue button used for all primary CTAs including "Add to Cart," "View Product," and form submissions. Default height is 34px with compact 6px 12px padding; the large variant (`button-primary-lg`) stretches to 46px with 18px type for hero-level calls to action. Hover darkens to `{colors.primary-active}` with a tighter border (#204d74). Disabled state reduces opacity to 0.65 rather than swapping fill color.

**`button-secondary`** — White-fill button with a light gray border, used for "Cancel," "Reset," and secondary navigation actions. On hover the background drops to #e6e6e6 and the border darkens to #adadad. Maintains the same 34px height rhythm as primary buttons.

**`button-success`** — Green action button (#5cb85c) reserved for purchase-confirmation flows, warranty registration completion, and positive-state CTAs. Hover shifts to `{colors.success-active}`.

**`button-danger`** — Red destructive button (#d9534f) for cart-item removal, account deletion confirmations, and error-state resubmissions.

### Text Input
**`text-input`** — Single-line input with a 1px #cccccc border that transitions to a vivid #66afe9 glow on focus (Bootstrap's characteristic blue shadow). Placeholder text renders at `{colors.muted-soft}`. Error state swaps focus glow to `{colors.danger}` ring. Used across search, contact forms, and warranty registration.

### Navigation
**`nav-bar`** — Fixed-height 50px dark bar (#080808) running full-width. Brand logo sits left in white; nav links render in #9d9d9d and brighten to white on hover. No bottom-border — the dark fill provides sufficient separation from the white canvas below. Dropdown menus emerge with a 1px border-radius on #080808 background, maintaining the dark-on-dark motif.

**`nav-bar-link`** — Individual nav items with 15px horizontal padding. Active state underlines with a 2px white bottom-border rather than background-fill, keeping the bar visually lightweight.

### Product Card
**`product-card`** — Rectangular card with `{rounded.xs}` corners, thin #eeeeee border, and zero shadow. Product image fills the top region at 16:9 with `object-fit: contain` on a white field — essential for displaying monitors without cropping bezels. Title links render in `{colors.primary}` below the image. Price and spec callouts sit in `{typography.body-md}`. Hover raises border contrast to #e5e5e5 but adds no shadow or transform — motion is absent from the card grid.

### Hero Banner
**`hero-banner`** — Full-width dark (#080808) section featuring product photography (typically a monitor on a black background) with white overlay text at `{typography.display-xl}`. Minimum height 400px. CTA button uses `button-primary-lg` variant. Often implemented as a Bootstrap carousel with indicator dots and left/right chevron arrows.

### Spec Table
**`spec-table`** — Striped HTML table with alternating white and #f5f5f5 rows. Header cells use `{typography.spec-label}` (bold 14px). Cell padding is a uniform 8px. Borders are 1px solid #dddddd on all sides. This component dominates product detail pages — Sceptre shows 20-40 rows of specifications (resolution, panel type, response time, inputs, VESA mount size) in a single scrollable table.

### Alerts
**`alert-success`** / **`alert-info`** / **`alert-warning`** / **`alert-danger`** — Four contextual alert boxes following Bootstrap's color-coding system. Each combines a tinted background surface, matching border, and darkened text color for accessibility contrast. Used for stock notifications, shipping updates, form validation messages, and promotional announcements.

### Breadcrumb
**`breadcrumb`** — Horizontal path indicator on a #f5f5f5 background strip with "/" separators. Links in `{colors.primary}`; current page renders in `{colors.muted}` without a link. Standard pattern: Home / Monitors / 24" Monitors / [Product Name].

### Category Sidebar
**`category-sidebar`** — Left-rail navigation listing monitor categories (by size, resolution, feature set). Links in `{colors.primary}` with an #f5f5f5 active-state highlight. Bordered panel container matches the product card border styling.

### Pagination
**`pagination`** — Inline pill-row with individual page numbers bordered in #dddddd. Active page fills with `{colors.primary}` and white text. Previous/Next arrows bookend the row. Disabled states gray out to `{colors.muted}`.

### Footer
**`footer`** — Dark (#080808) full-width bar mirroring the nav-bar tone. Links in #9d9d9d brighten on hover. Contains legal links, social media icons (likely Font Awesome or Glyphicons), and copyright. Minimal vertical padding ({spacing.xl}).

### Search Bar
**`search-bar`** — Input-group pattern: text field with joined submit button. Input matches `text-input` styling; the attached button is `{colors.primary}` fill with a magnifying-glass glyph in white. Both elements share `{rounded.xs}` outside corners with 0px on the joined inner edge.

### Badges
**`badge-stock`** / **`badge-outofstock`** — Small label pills indicating inventory state. "In Stock" is green (#5cb85c); "Out of Stock" is red (#d9534f). Compact padding (3px 7px) with `{typography.caption}` 12px text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Navbar collapses to hamburger; product grid stacks to single column; hero carousel reduces to 250px min-height; spec table gains horizontal scroll; sidebar categories collapse above product grid; footer links stack vertically |
| Tablet | 768-992px | Two-column product grid; sidebar and content share 3:9 grid ratio; nav links visible but compressed padding; hero text scales to `{typography.display-md}` |
| Desktop | 992-1200px | Three-column product grid; full sidebar visible; nav-bar links at full spacing; hero banner at 400px+ height with `{typography.display-xl}` |
| Wide | > 1200px | Container maxes at 1170px centered; four-column product grid possible on category pages; generous whitespace flanks content |

### Touch Targets
- All buttons maintain minimum 34px height; large variants reach 46px
- Nav-bar links padded to 15px horizontal for 50px touch-row height
- Pagination items have 6px 12px padding producing ~34px tap targets
- Mobile hamburger toggle is 40x40px minimum
- Product card is fully tappable as a link block on mobile

### Collapsing Strategy
- Bootstrap 3's 12-column grid with 15px gutters; breakpoints at 768, 992, 1200px
- No CSS Grid or Flexbox layout — purely float-based columns that stack at mobile
- Category sidebar moves above product grid on mobile rather than becoming a drawer
- Spec tables convert to horizontally scrollable containers rather than reflowing
- Hero carousel navigation arrows hide on mobile; swipe gesture replaces them

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- All extracted colors correspond to Bootstrap 3 framework defaults — no custom brand palette could be isolated from the extraction. Sceptre may load brand-specific overrides via JavaScript or deeper CSS that the crawler did not capture.
- No custom web font detected; the site appears to rely entirely on system font stacks (Helvetica Neue / Arial). A brand wordmark font may exist only as an image/SVG logo.
- No CSS custom properties or design tokens found — the site predates CSS variable adoption, using compiled Bootstrap LESS/CSS.
- Meta theme-color not set, preventing reliable mobile browser chrome theming.
- Exact hero banner heights, carousel transition timings, and animation values could not be extracted statically.
- Glyphicons Halflings detected as the icon system — a legacy Bootstrap 3 icon font that may be supplemented or replaced with image assets for product-specific iconography.
- No dark-mode variant detected or inferred; the site operates exclusively in light mode.
