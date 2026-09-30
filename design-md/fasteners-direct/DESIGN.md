---
version: alpha
name: "Fasteners Direct"
source_url: "https://www.fastenersdirect.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Three operational signal colors — #008a06 green, #f1a500 amber, and #aa273d red — carry all the weight that brand personality might otherwise bear at Fasteners Direct. They appear as stock badges, clearance stickers, and discontinuation flags, borrowing logic from warehouse bin-labeling rather than consumer marketing. The surrounding canvas is held in neutral grays (#f5f5f5 surface-soft, #e5e5e5 hairlines, #757575 muted type) and a near-black charcoal (#313440) nav bar that signals industrial procurement rather than retail discovery. Arial runs the entire typographic system — no custom font, no license cost, no personality beyond legibility at 13–14px in a browser table cell. Rounded corners compress to {rounded.xs} (4px) on buttons and inputs; the product card drops to {rounded.none}, rendering as a data row rather than an editorial tile. Spacing is dense by consumer standards: {spacing.sm} gutters between specification fields, {spacing.base} between table rows, because the buyer's job is to locate a M8×1.25 hex bolt in grade 10.9 across 200 SKUs, not to browse. The primary action — 'Add to Cart' — appears in #008a06 and nowhere else on the page, so a procurement manager scanning dense listings can locate the buy action in under a second without reading labels. Quantity discount tiers render in a compact table beneath the main price, each row striped in #f5f5f5 against white, borrowing tabular density from spreadsheet UX rather than commerce convention. Alert states replicate traffic-light semantics precisely: #ffdddd backgrounds for errors, #fffdea for warnings, and #d5ffd8 for confirmations — soft tints of their full-saturation signal hues that keep the status readable without overpowering product data beside it. The #f1a500 amber surfaces on clearance and promotional badges exclusively, concentrating scarcity signaling into one attention-catching hue without competing with the green buy button. At wide viewports, a fixed 220px category sidebar locks left, presenting an alphabetized fastener family hierarchy — bolts, nuts, screws, washers, anchors, rivets — as plain-text navigation, the functional equivalent of a printed catalog index rendered without ornament.

colors:
  primary: "#008a06"
  primary-active: "#006605"
  primary-disabled: "#d5ffd8"
  accent-amber: "#f1a500"
  accent-amber-dark: "#db8f1d"
  sale-red: "#aa273d"
  sale-red-deep: "#90273c"
  error: "#d14343"
  error-alt: "#cc4749"
  error-bg: "#ffdddd"
  success-bg: "#d5ffd8"
  warning-bg: "#fffdea"
  ink: "#313440"
  body: "#474747"
  muted: "#757575"
  muted-soft: "#8f8f8f"
  hairline: "#e5e5e5"
  hairline-soft: "#ececec"
  hairline-strong: "#dfdfdf"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  nav-dark: "#313440"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link-blue: "#476bef"
  link-blue-hover: "#002fe1"
  link-blue-alt: "#007dc6"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  price:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  part-number:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  table-header:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
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
    padding: 10px 18px
    height: 40px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 9px 17px
    height: 40px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.muted}"
  button-sm:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 6px 12px
    height: 30px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 10px
    height: 36px
    focusBorder: "1px solid {colors.link-blue}"
  quantity-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    width: 60px
    height: 36px
    textAlign: center
  nav-bar:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 52px
    padding: "0 {spacing.base}"
  sub-nav:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    height: 36px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 38px
    padding: "0 {spacing.sm}"
  search-button:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 0 16px
    height: 38px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm}"
  product-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} {spacing.base}"
    stripedBackground: "{colors.surface-soft}"
  stock-badge-in-stock:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  stock-badge-out-of-stock:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  sale-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  clearance-badge:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.price}"
  price-sale:
    textColor: "{colors.sale-red}"
    typography: "{typography.price}"
  price-was:
    textColor: "{colors.muted}"
    typography: "{typography.price-sm}"
    textDecoration: line-through
  part-number-display:
    textColor: "{colors.muted}"
    typography: "{typography.part-number}"
    backgroundColor: "{colors.surface-soft}"
    padding: "2px 6px"
    rounded: "{rounded.xs}"
  specification-table:
    backgroundColor: "{colors.surface-card}"
    headerBackground: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.table-header}"
    cellTextColor: "{colors.body}"
    cellTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    stripedRow: "{colors.surface-soft}"
  quantity-discount-table:
    backgroundColor: "{colors.surface-card}"
    headerBackground: "{colors.ink}"
    headerTextColor: "{colors.on-dark}"
    headerTypography: "{typography.table-header}"
    cellTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    stripedRow: "{colors.surface-soft}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    separator: "/"
    activeTextColor: "{colors.ink}"
  category-sidebar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    width: 220px
  alert-error:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.error}"
    padding: "{spacing.sm} {spacing.base}"
  alert-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  alert-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.accent-amber-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.accent-amber}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The 'Add to Cart' button in #008a06 green is the single saturated action color on the page; nothing else in the layout shares that hue, so procurement users scanning dense SKU lists locate it without reading. Hover darkens to #006605 via `button-primary-hover`; the disabled state drains to #d5ffd8, the softest tint of the same green family, signaling inactivity without switching hue families.

**`button-secondary`** — White fill with a 1px #e5e5e5 border, visually flush with surrounding specification table grid lines. Used for 'Request a Quote', 'Print Page', and secondary catalog actions. Hover lifts background to #f5f5f5 and strengthens border to #757575, a subtle depth shift on a background that is already nearly white.

**`search-button`** — Amber #f1a500 fill paired directly with the search input field, distinguishing the find action from the buy action at the color level. A buyer reads amber as 'search' and green as 'purchase' without requiring label decoding.

### Navigation

**`nav-bar`** — 52px full-width charcoal (#313440) bar containing the logo, search input with amber search button, account link, and cart icon in white type. No visual complexity; the dark ground frames the white page and makes the amber search button the only warm element in the top chrome.

**`sub-nav`** — A secondary 36px strip in #f5f5f5 with a #e5e5e5 bottom border carrying top-level category links in 13px Arial. The color step from charcoal to light gray creates a clear hierarchy: brand identity above, category navigation below.

**`category-sidebar`** — Fixed 220px left rail in #f5f5f5 with 1px #e5e5e5 border, listing fastener families in 13px Arial at compact row heights. The active category applies a solid #008a06 fill with white text — the same binary green-or-not logic as the stock badge, reinforcing a consistent visual language across navigation and inventory status.

### Product Display

**`product-card`** — Zero-radius bordered container that renders closer to a spreadsheet row than a retail tile. Part number appears in `part-number` monospace type for scanner legibility, product title in `title-sm` bold, price in `price` typography, stock badge top-right. Padding stays at {spacing.sm} to maximize SKU density per viewport.

**`product-row`** — List-view variant alternating rows between #ffffff and #f5f5f5 stripes. Part number, description, unit of measure, unit price, and `quantity-input` collapse into a single horizontal band at `body-sm` type size, mirroring a purchase-order line item layout.

**`specification-table`** — The dominant component on product detail pages. Header row in #f5f5f5 with uppercase 12px bold Arial labels (thread size, pitch, length, material, finish, tensile strength, standard). Row alternation in #f5f5f5 against white. Every column width is fixed to prevent reflow when values vary in character count.

**`quantity-discount-table`** — Black-header table ({colors.ink} fill, white type) showing quantity-break pricing below the main price display. Minimum quantity, unit price, and percentage savings arrange into three columns with {spacing.sm} row padding. The dark header contrasts against the main specification table above it, grouping pricing logic visually apart from physical properties.

**`part-number-display`** — Monospace 13px label with 0.5px letter-spacing in a #f5f5f5 pill, used inline and in search results. Monospace rendering ensures part numbers with similar prefixes (e.g. M8X1.0-25 vs. M8X1.25-25) align at fixed character positions when stacked in list view.

### Badges and Status

**`stock-badge-in-stock`** — #d5ffd8 background with #008a06 text, the tinted-to-full-saturation pairing that reads as 'safe' without overwhelming the product title beside it. Applied inline next to per-SKU availability counts.

**`stock-badge-out-of-stock`** — #ffdddd background with #d14343 red text. Mirrors the in-stock badge structure exactly, swapping only the hue family. The structural symmetry means a user parsing a mixed list page reads status from color alone.

**`sale-badge`** — Solid #f1a500 amber with white type, used for volume-discount callouts and limited-time pricing. Amber concentrates promotional attention without touching the green buy-action territory.

**`clearance-badge`** — Solid #aa273d dark red with white type, reserved for discontinued or final-lot inventory. Darker and more urgent than the error alert tint, signaling no restock expected.

### Alerts

**`alert-error`** / **`alert-success`** / **`alert-warning`** — Three traffic-light alert bands using soft tints as backgrounds (#ffdddd / #d5ffd8 / #fffdea) against the full-saturation hue for text and border. Structural padding matches at {spacing.sm} vertical, {spacing.base} horizontal across all three. Applied respectively to cart validation failures, order confirmations, and low-stock warnings. The soft-tint-plus-full-saturation formula matches the stock badge pairing, extending the same signal language from inline badges to page-level notifications.

### Footer

**`footer`** — Matching #313440 charcoal as the nav bar, creating a dark top-and-bottom frame around a white page core. White body links at 13px Arial organized into columns: shop by category, account, customer service, and legal. Column widths are fixed; no decorative imagery.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 551px | Single-column layout; category sidebar collapses into a hamburger-accessible off-canvas drawer; product grid becomes single-column rows; search bar stacks full-width above nav chrome |
| Tablet | 551–801px | Two-column product grid; sidebar may collapse to a top filter bar; quantity-discount table enables horizontal scroll; sub-nav category strip scrolls horizontally |
| Desktop | 801–1261px | Three-column product grid; category sidebar fixed at 220px left; specification tables expand to full content-column width |
| Wide | > 1261px | Max-width container (approx. 1280–1440px) centered with auto margins; sidebar and content column proportions locked; no additional layout change beyond centering |

### Touch Targets
- 'Add to Cart' button minimum 40px height maintained at all breakpoints
- Quantity input minimum 36px height; stepper increment/decrement arrows padded to 40px touch width each
- Nav links minimum 44px touch row height in the mobile off-canvas drawer
- Category sidebar items minimum 36px row height on touch devices
- Badge elements are display-only and excluded from tap-target requirements

### Collapsing Strategy
- Category sidebar collapses to an off-canvas drawer triggered by a hamburger icon at < 801px; selected category state persists on close/reopen
- Specification tables below 551px collapse to vertically stacked label-above-value pairs; borders retained
- Quantity-discount pricing table enables horizontal scroll on tablet; collapses to a vertical tier list on mobile
- Sub-nav category strip wraps to two-row horizontal scroll on tablet; converts to drawer item on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.
- No custom font family detected; Arial confirmed from extraction but a custom heading font loading via JavaScript or icon font cannot be ruled out
- Exact nav bar height not extractable from static hints; 52px is an estimate based on industrial B2B site norms
- Logo treatment (wordmark vs. lockup, exact dimensions and color reversal on dark nav) not recoverable from color/font extraction
- Search button may be square (0px radius) rather than {rounded.xs}; extraction did not confirm corner treatment on input controls
- Mobile menu structure (flat list vs. accordion expand vs. mega-menu panel) not confirmed from static data
- Hover and focus transition durations not available from extraction; defaults to browser native unless overridden
- Exact column widths in desktop product grid (2 vs. 3 vs. 4 column) not confirmed; 3-column is an estimate
- Pricing display logic for 'price per hundred' vs. 'price each' units-of-measure formatting not extractable
- Font Awesome version (5 vs. 6) used for UI icons cannot be determined from media-query hints alone
