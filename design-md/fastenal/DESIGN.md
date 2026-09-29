---
version: alpha
name: "Fastenal"
source_url: "https://www.fastenal.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Fastenal's navy (#003471) is not chosen for aesthetics — it's the color of a hard hat industry's trust signal, stamped on every header bar, every login prompt, and every primary CTA across a catalogue that spans over a million SKUs. The design is unapologetically utilitarian: a dense left-rail category tree, SKU-level search with part number autocomplete, and bulk pricing tables that prioritize data density over whitespace. Red (#CC1418) appears sparingly, anchoring the logo and critical alerts rather than carrying emotional warmth. Typography runs on system-stack sans-serifs — crisp, zero-license, rendering cleanly on the factory-floor laptop running Windows 10. Rounded corners sit near zero: form inputs and cards use tight {rounded.xs} geometry that signals precision over personality. The canvas is an industrial white (#FFFFFF) with a cool gray surface ({colors.surface-soft}) for alternating table rows and category panels — no gradients, no hero photography blur, no ambient brand video. Navigation is category-first: a mega-menu sorted by supply type (Fasteners, Safety, Electrical, Tools) runs the width of the viewport, structured to intercept the buyer who already knows their commodity but needs to confirm spec and price tier. Account login anchors the top-right with heavy visual weight because the majority of revenue flows through registered B2B accounts, vendor-managed inventory programs, and EDI connections — not anonymous carts. Product cards expose part number, unit of measure, minimum order quantity, and tiered price breaks without hover. The footer carries a full sitemap column set plus a prominent store-locator link, reflecting Fastenal's hybrid model of online ordering backed by over 3,400 physical branch locations. Everything resolves to efficiency: the designer's brief here was to not get in the way.

colors:
  primary: "#003471"
  primary-active: "#002557"
  primary-disabled: "#8099b8"
  primary-light: "#d6e4f7"
  accent-red: "#CC1418"
  accent-red-active: "#a51013"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  hairline: "#cccccc"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#002557"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  success: "#2e7d32"
  warning: "#e65100"
  error: "#CC1418"
  table-row-alt: "#f9f9f9"
  price-highlight: "#CC1418"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.35
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
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-primary:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  nav-secondary:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  part-number:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  price-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  label-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: 9px 19px
    height: 40px
  button-accent:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-accent-active:
    backgroundColor: "{colors.accent-red-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "none"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
    height: 38px
    focusBorder: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    padding: 10px 16px
    height: 44px
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.xs}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-primary}"
    height: 56px
    borderBottom: "none"
    utilityStrip:
      backgroundColor: "{colors.surface-dark}"
      typography: "{typography.body-sm}"
      textColor: "{colors.on-primary}"
      height: 36px
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-secondary}"
    border: "1px solid {colors.hairline}"
    columnHeaderTypography: "{typography.title-md}"
    columnHeaderColor: "{colors.primary}"
    shadow: "0 4px 8px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm}"
    partNumberTypography: "{typography.part-number}"
    partNumberColor: "{colors.muted}"
    priceTypography: "{typography.price-md}"
    priceColor: "{colors.price-highlight}"
    titleTypography: "{typography.title-sm}"
    hoverBorder: "1px solid {colors.primary}"
  product-detail-hero:
    backgroundColor: "{colors.canvas}"
    imageArea:
      border: "1px solid {colors.hairline}"
      rounded: "{rounded.sm}"
    priceTypography: "{typography.price-lg}"
    priceColor: "{colors.price-highlight}"
    partNumberTypography: "{typography.part-number}"
    sectionDivider: "1px solid {colors.hairline-soft}"
  pricing-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.label-sm}"
    cellTypography: "{typography.body-sm}"
    altRowBackgroundColor: "{colors.table-row-alt}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
  category-sidebar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    activeColor: "{colors.primary}"
    activeTypography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    sectionHeaderTypography: "{typography.title-md}"
    sectionHeaderColor: "{colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-in-stock:
    backgroundColor: "{colors.success}"
    textColor: "#ffffff"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  quantity-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 36px
    width: 80px
    controlColor: "{colors.primary}"
  account-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    shadow: "0 2px 8px rgba(0,0,0,0.10)"
    rounded: "{rounded.sm}"
    headerTypography: "{typography.title-sm}"
    headerColor: "{colors.primary}"
  alert-error:
    backgroundColor: "#fff5f5"
    textColor: "{colors.error}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.error}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  alert-info:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.primary}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.ink}"
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — Navy (#003471) fill with white uppercase text at 14px/700 weight, 40px height, and 2px corner radius. Hover and focus darken to `{colors.primary-active}`; disabled desaturates to `{colors.primary-disabled}` while retaining white text. Used for account actions, quote submissions, and procurement workflow CTAs.

**`button-secondary`** — White canvas with a 1px navy border and navy text — deployed for "Add to Quote," "Compare," and "Save for Later" alongside the primary accent button. Matches primary height so paired buttons form a stable horizontal row without hierarchy confusion.

**`button-accent`** — Red (#CC1418) fill for highest-stakes conversion CTAs such as "Add to Cart" on product detail pages. Used sparingly; its scarcity preserves urgency at the purchase moment. Active state deepens to `{colors.accent-red-active}`.

**`button-ghost`** — Transparent background with navy text and no border, used for low-priority inline actions like "View All" links within category panels and dashboard widget footers. No minimum height constraint — scales to surrounding line height.

### Search
**`search-bar`** — The dominant UI element across every page context, the search bar renders with a 2px navy border and a flush navy submit button on the right. Autocomplete surfaces part numbers, brand names, category strings, and recent account searches. On mobile the bar expands full-width on tap from a collapsed icon state in the utility strip.

### Navigation
**`nav-bar`** — Two-tier header structure: a 36px utility strip in `{colors.surface-dark}` (dark navy) carrying account links, cart count, and store locator at `{typography.body-sm}`; below it, a 56px primary bar in `{colors.primary}` holding the Fastenal wordmark and top-level category links at `{typography.nav-primary}`. Always opaque — no scroll-away or transparency variant.

**`mega-menu`** — Full-viewport-width dropdown with 4–6 columns of hierarchical category links. Column headers use `{typography.title-md}` in `{colors.primary}`; sub-items use `{typography.nav-secondary}` in `{colors.ink}`. No promotional tiles or imagery — the menu is pure navigation data optimized for scan speed.

**`breadcrumb`** — Small `{typography.body-sm}` path trail in `{colors.muted}` with chevron separators. The terminal item renders in `{colors.ink}` at normal weight. Truncated to two ancestors with ellipsis on mobile viewports.

### Product Card
**`product-card`** — Square product image, part number in monospace `{typography.part-number}` colored `{colors.muted}`, product name in `{typography.title-sm}`, and price in `{typography.price-md}` colored `{colors.price-highlight}`. A 1px `{colors.hairline}` border with 2px radius defines the card boundary; hover promotes border to `{colors.primary}`. UOM and minimum order quantity appear as `{typography.caption}` below the price.

### Pricing Table
**`pricing-table`** — Tier pricing (e.g., 1–9, 10–24, 25–99, 100+) sits as the central B2B conversion element on every product detail page. Header row runs `{colors.primary}` fill with white `{typography.label-sm}` uppercase labels. Data rows alternate between `{colors.canvas}` and `{colors.table-row-alt}`. No rounded corners anywhere in the table. The active tier (matching current quantity) receives a left-border accent in `{colors.primary}`.

### Category Sidebar
**`category-sidebar`** — Left-rail tree navigation on `{colors.surface-soft}` with a 1px hairline right border. Section headers in `{typography.title-md}` navy; sub-category links in `{typography.body-md}`. The active leaf node is bolded in `{colors.primary}` with a 2px left accent bar. Collapses to a "Filters" drawer overlay below tablet breakpoint.

### Badges
**`badge-new`** — Navy pill with white `{typography.label-sm}` uppercase text, 2px radius, tight 2×6px padding. Applied to recently added SKUs in search results and category grids.

**`badge-sale`** — Red (#CC1418) fill using the same geometry as `badge-new`. Marks promotional pricing events and clearance items.

**`badge-in-stock`** — Green (`{colors.success}`) fill with `{typography.caption}` white text. Signals immediate branch or distribution-center availability without requiring a hover state.

### Alerts
**`alert-error`** — Light red tint background with `{colors.error}` text and border, used for form validation, order failures, and out-of-stock notifications. Rendered at `{typography.body-sm}` with `{spacing.sm}` vertical and `{spacing.base}` horizontal padding.

**`alert-info`** — `{colors.primary-light}` background with navy text and border, used for account notices, shipping estimate disclaimers, and compliance callouts.

### Account Menu
**`account-menu`** — Dropdown card anchored to the account icon in the utility strip. White canvas with 1px hairline border, 2px shadow, and `{rounded.sm}` corners. Header shows the logged-in user's name in `{typography.title-sm}` navy. Body links use `{typography.body-sm}`. Includes fast links to Order History, VMI Dashboard, Saved Lists, and Account Settings.

### Footer
**`footer`** — Four-to-five column utility footer on `{colors.surface-soft}` with a 3px `{colors.primary}` top border as the sole brand flourish. Column headers in `{typography.title-sm}` ink; links in `{typography.body-sm}` colored `{colors.primary}`. Covers Products, Resources, About Fastenal, and Store Locator. No imagery or brand photography — purely informational and compliance-oriented.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Category sidebar hidden behind "Filters" drawer; mega-menu replaced by hamburger accordion; search expands full-width on tap; product grid collapses to 1 column; pricing table scrolls horizontally with sticky first column |
| Tablet | 744–1128px | 2-column product grid; category sidebar collapses to a horizontal filter chip strip above the grid; search persists at ~60% width in header; mega-menu renders at 2–3 columns |
| Desktop | 1128–1440px | Full 3–4 column product grid; category sidebar visible at fixed width; mega-menu at full column count; dual-strip header at full spec |
| Wide | > 1440px | Content capped at ~1400px max-width centered in viewport; side gutters expand; product grid can extend to 5 columns on broad category pages |

### Touch Targets
- Primary CTAs (Add to Cart, Add to Quote) maintain minimum 44×44px touch area on mobile
- Quantity increment and decrement controls are padded to 40px tap area regardless of visual size
- Category drawer links maintain 48px row height for comfortable thumb navigation
- Nav utility strip items in the collapsed hamburger expand to full-width 48px rows

### Collapsing Strategy
- Left category sidebar → horizontal filter chip strip at tablet, full-screen drawer at mobile
- Mega-menu → hamburger slide-in with accordion category expansion at ≤744px
- Dual-tier header → single bar with utility items moved into hamburger at mobile
- Pricing table → horizontal scroll with sticky quantity-break column at mobile
- Multi-column footer → single-column stacked accordion at mobile
- Breadcrumb → truncated to two ancestors with ellipsis separator on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site returned HTTP 403 Access Denied — zero live hex colors or font stacks were extractable; all values are derived from widely observed Fastenal brand identity (navy blue primary, red accent, system-font stack) and should be treated as approximations
- Exact primary blue hex unverified — #003471 is a plausible match from logo reproductions; published brand guides have cited values ranging from #003087 to #002F6C across different eras
- Exact red accent hex unverified — #CC1418 is estimated from logo color; the live site may use a value such as #D4001C or #C8101A
- Font stack unconfirmed — Arial assumed as the dominant system font for an enterprise industrial brand of this generation; a licensed web font cannot be ruled out
- Interactive states (focus rings, hover transitions, press feedback) not observed from live source — all state values are inferred from industrial B2B conventions
- Mobile navigation and drawer behavior not verified from live source — collapsing strategy inferred from comparable industrial catalogue sites
- VMI dashboard, Fastenal Managed Inventory portal, and EDI ordering interface styling are likely distinct from the public catalogue and are not covered here
- Dark mode or high-contrast accessibility mode existence unknown
- Spacing and padding values in the live component system not verifiable without DOM inspection
