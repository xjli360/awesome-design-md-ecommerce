---
version: alpha
name: "Wesco International"
source_url: "https://www.wesco.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Seventeen colors extracted from a single Wesco International page tell the whole story — this is not a brand anchored on one primary and two neutrals, but a traffic-management system for industrial procurement, where #bd2426 marks price alerts and urgent callouts, #9bca3e signals in-stock availability, #f68b1f flags promotional pricing, and #163959 commands the navigation bar with the authority of a regulatory standard. Type runs exclusively in Arial at every scale — no custom typeface, no web font payload — a choice that reads as deliberate when load time across a plant-floor browser matters more than brand distinctiveness. The spacing system stays compressed: 8px and 12px gaps dominate product listing grids, where showing five additional part numbers per scroll is worth more than padding generosity. Buttons carry minimal rounding ({rounded.sm}, 4px) — functional, not playful — and the primary CTA in deep navy ({colors.primary}) signals supplier trust over urgency, a deliberate departure from the alert-orange or alarm-red also present in the palette. Product cards lean entirely on text density: manufacturer name, part number in courier monospace, description snippet, unit-of-measure, and price tier compete at 13–14px without hero imagery. The three-color badge logic — lime-green availability chips, red restriction notices, orange promotional callouts — creates information-density that functions as rapid visual triage for a maintenance buyer scanning 400 line items per session. Search with autocomplete is the real homepage: a 48px input bar inside a {colors.canvas} container with a {colors.primary} submit control represents the entire value proposition compressed into one interaction. Footer menus cascade four columns deep into supplier, compliance, and account-management links — the navigation model is hierarchical and exhaustive, not editorial.

colors:
  primary: "#163959"
  primary-hover: "#0f2840"
  primary-disabled: "#8aadca"
  action-blue: "#2f7bbf"
  action-blue-soft: "#62a1d8"
  link: "#0051c3"
  alert-red: "#bd2426"
  alert-red-hover: "#521010"
  alert-red-soft: "#de5052"
  success-green: "#9bca3e"
  success-green-dark: "#516b1d"
  success-green-soft: "#bada7a"
  promo-orange: "#f68b1f"
  promo-orange-dark: "#904b06"
  promo-orange-soft: "#f9b169"
  promo-amber: "#ee730a"
  promo-amber-dark: "#c16508"
  ink: "#272727"
  body: "#404040"
  muted: "#595959"
  muted-soft: "#737373"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  disabled-fill: "#bfbfbf"
  canvas: "#ffffff"
  surface-soft: "#ebebeb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-alert: "#ffffff"
  on-success: "#272727"

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
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.44
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0
  label-upper:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.36
    letterSpacing: 0.6px
    textTransform: uppercase
  part-number:
    fontFamily: "courier, monaco, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 12px
  xl: 20px
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
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
  button-alert:
    backgroundColor: "{colors.alert-red}"
    textColor: "{colors.on-alert}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    borderColor: "{colors.action-blue}"
    outline: "2px solid {colors.action-blue-soft}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 0 0 0 12px
    height: 48px
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitWidth: 56px
    submitRounded: "{rounded.none}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    subNavBackgroundColor: "{colors.action-blue}"
    topBannerBackgroundColor: "{colors.ink}"
    topBannerTextColor: "{colors.on-primary}"
    topBannerTypography: "{typography.caption}"
    topBannerHeight: 32px
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    partNumberTypography: "{typography.part-number}"
    descTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    manufacturerTypography: "{typography.caption}"
    manufacturerColor: "{colors.muted}"
  availability-badge:
    backgroundColor: "{colors.success-green}"
    textColor: "{colors.on-success}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  availability-badge-out:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  alert-badge:
    backgroundColor: "{colors.alert-red}"
    textColor: "{colors.on-alert}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  promo-badge:
    backgroundColor: "{colors.promo-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  price-block:
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    unitTypography: "{typography.caption}"
    unitColor: "{colors.muted}"
    salePriceColor: "{colors.alert-red}"
    originalPriceDecoration: line-through
    originalPriceColor: "{colors.muted}"
  data-table:
    headerBackgroundColor: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.body-sm}"
    headerFontWeight: 700
    rowBackgroundColor: "{colors.canvas}"
    rowAltBackgroundColor: "#f7f7f7"
    rowTextColor: "{colors.body}"
    rowTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    cellPadding: 8px 12px
  breadcrumb:
    textColor: "{colors.link}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.body}"
    typography: "{typography.caption}"
  hero-category-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    minHeight: 200px
    padding: "{spacing.xl} {spacing.lg}"
    overlayOpacity: 0.6
  sidebar-filter:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    sectionHeadTypography: "{typography.title-sm}"
    sectionHeadColor: "{colors.ink}"
    optionTypography: "{typography.body-sm}"
    optionColor: "{colors.body}"
    checkedColor: "{colors.action-blue}"
    expandIconColor: "{colors.muted}"
    rounded: "{rounded.none}"
    width: 240px
  pagination:
    backgroundColor: "{colors.canvas}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveTextColor: "{colors.link}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 10px
  account-badge:
    backgroundColor: "{colors.action-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "#aacde9"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    legalTypography: "{typography.caption}"
    legalColor: "{colors.muted-soft}"
    dividerColor: "{colors.muted}"
    padding: "{spacing.xxl} {spacing.lg}"

## Components

### Buttons

**`button-primary`** — Deep navy (#163959) fill with white 14px/700 Arial, 4px radius ({rounded.sm}), 40px height. On hover transitions to `button-primary-hover` (#0f2840); disabled state uses a washed mid-blue ({colors.primary-disabled}) that clearly communicates non-interactivity. This is the "Add to Cart" and primary account-action button; its restraint — navy rather than the alert-orange or alarm-red also in the palette — signals the B2B trust register where the buyer will return hundreds of times.

**`button-secondary`** — White fill with a 1px navy border and navy type, same geometry as primary. Used for "Save for Later," "Add to List," and comparison actions where multiple CTAs must coexist on a product detail page without a hierarchy fight.

**`button-alert`** — Alarm red (#bd2426) fill with white type, same 40px height and {rounded.sm}. Reserved for urgent procurement actions: "Request a Quote" expiry CTAs, restricted-item callouts, and cart-deletion confirmations where the color carries semantic weight rather than brand personality.

**`button-ghost`** — Transparent background with link-blue (#0051c3) type, no visible border. Used for inline text actions — "View All," "See More Specs," expand/collapse controls in dense specification tables — where adding a filled button would create visual clutter in an already information-dense layout.

### Search Bar

**`search-bar`** — The functional center of the Wesco page: a 48px-tall input spanning most of the header width, white fill with {colors.hairline} border and {rounded.sm} on the left, flush-joined on the right to a 56px navy submit button ({rounded.none} on that edge) carrying a magnifier icon. Autocomplete dropdown opens at full input width, {colors.surface-soft} background, {typography.body-sm} suggestion lines; keyboard-selected rows highlight in {colors.action-blue-soft}. The compound shape (radiused left, square right seam, colored submit) is the single most recognizable element in the Wesco UI.

### Navigation

**`nav-bar`** — Two-tier structure: a 32px top utility bar ({colors.ink}) carrying account links, location selector, and phone number in 12px white type; below it a 56px primary nav band in deep navy (#163959) with category mega-menu triggers in {typography.nav-link} white. Mega-menus expand to full-width panels with two or three columns of category links. A sub-category strip in {colors.action-blue} can appear between the primary bar and the page for deep catalog contexts. Mobile collapses the entire structure to a hamburger that reveals a slide-in drawer with accordion category sections.

### Product Card

**`product-card`** — Text-first, image-secondary. The card carries manufacturer name in 12px muted gray, part number in {typography.part-number} (courier monospace — the only monospace application in the system, making part numbers scannable in a list of text), description in 13px body, an availability badge, unit price in 20px/700 ({typography.price-display}), unit-of-measure label in 12px muted gray, and a primary CTA button. Border is 1px {colors.hairline} with {rounded.xs} (2px) — nearly square, signaling specification-driven rather than lifestyle product culture.

### Availability Badges

**`availability-badge`** — Lime-green (#9bca3e) fill with near-black text in 11px all-caps ({typography.label-upper}), 2px×6px padding. Used for "In Stock," "Ships Today," and branch-availability labels. The green is bright enough to scan from peripheral vision across 30+ results. **`availability-badge-out`** switches to {colors.hairline} fill with {colors.muted} text for "Out of Stock" and "Backordered" states without collapsing the badge slot, preserving grid alignment across mixed-availability result sets.

### Alert and Promo Badges

**`alert-badge`** — Alarm red (#bd2426) fill, white type, same 11px all-caps geometry. Applied to restricted-item labels, hazmat flags, and price-expiry warnings. **`promo-badge`** — Safety orange (#f68b1f) fill with white type for "Sale," "Contract Price," and "Clearance" labels. The three badge colors — green, red, orange — form a traffic-light triage system readable at catalog-list density without requiring the buyer to read the label text first.

### Price Block

**`price-block`** — Standard price at 20px/700 Arial ({typography.price-display}) in {colors.ink}. Sale price replaces the standard price in {colors.alert-red}, with original price rendered at matching scale in {colors.muted} with `line-through` decoration. Unit-of-measure (EA, CS, BX, FT) follows in 12px {colors.muted} — omitting this label in a procurement context risks an order-of-magnitude purchasing error, so it is never truncated.

### Data Table

**`data-table`** — The workhorse for product specifications, order history, and catalog cross-reference. Header row sits in {colors.surface-soft} with 700-weight {typography.body-sm}. Alternate rows use #f7f7f7 for legibility across 8–15 columns. Cell padding is 8px×12px — tight enough to maximize information per viewport without row-height collapse. Part numbers within cells use {typography.part-number} (courier monospace) to visually separate them from adjacent description text in the same row.

### Hero Category Banner

**`hero-category-banner`** — A 200px-minimum-height band in {colors.primary} with optional background product photography behind a 60% opacity navy overlay. Heading at {typography.display-md} (24px/700) in white; body text at {typography.body-md} in white at 0.85 opacity. Used on category landing pages as the visual anchor before the filter sidebar and product grid begin. The overlay approach preserves readability while allowing the brand to show relevant equipment photography without requiring high-contrast asset production.

### Sidebar Filter

**`sidebar-filter`** — Fixed 240px left column on desktop, section headings in {typography.title-sm}, checkbox option lists in {typography.body-sm}. No rounding — filter panel edges are square throughout. Checked states use {colors.action-blue} for checkbox fill and label. Expand/collapse section icons in {colors.muted} use ＋/− characters. On mobile the filter panel slides in as a bottom sheet from a sticky "Filter & Sort" bar at the bottom of the viewport.

### Footer

**`footer`** — Dark charcoal ({colors.ink}) background, four-column link grid. Section headings in {typography.title-sm} white; link text in {typography.body-sm} at an approximated muted-blue (#aacde9, not confirmed from extraction — see Known Gaps). Legal and compliance text in {typography.caption} at {colors.muted-soft}. A full-width {colors.muted} hairline separates the link column zone from the bottom compliance strip carrying certifications and copyright.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with slide-in category drawer; search bar full-width below the header band; filter panel becomes a bottom sheet behind a sticky "Filter & Sort" bar; data tables scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; primary nav condensed with icon+label pairs; search bar remains full-width; sidebar filter visible at 200px width |
| Desktop | 1128–1440px | Three-column product grid; full mega-menu navigation active; 240px sidebar filter; full two-tier nav bar at combined 88px height |
| Wide | > 1440px | Four-column product grid; container max-width 1440px centered; additional "Customers Also Bought" recommendation column may appear |

### Touch Targets
- All buttons maintain 40px minimum height; interactive list rows pad to 44px on mobile
- Filter checkboxes expand to 44px touch target height via vertical padding on mobile
- Product card CTA button expands to full card width on mobile
- Pagination controls use 44px × 44px minimum tap area
- Badge elements are display-only and not interactive; no minimum size requirement

### Collapsing Strategy
- Mega-menus collapse to accordion-style category sections inside the hamburger drawer
- Filter sidebar collapses to a sticky bottom bar on mobile; tapping opens a full-screen bottom sheet with apply/close controls
- Data tables with more than 4 columns collapse to horizontal-scroll containers rather than stacking rows — stacking would break part-number-to-value associations
- Top utility bar (phone number, account links, location) hides fully on mobile; account access moves into the hamburger drawer header
- Price block and availability badge are always visible at every breakpoint — never collapsed or hidden

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Footer link color (#aacde9 used as approximation) was not confirmed from extraction; exact token may differ and is not declared in the colors block
- No proprietary typeface identified; Arial confirmed as the system font, but no custom weight variants, variable font axes, or licensed alternatives documented
- Exact mega-menu layout (column count, icon presence per category, subcategory depth, hover vs. click trigger) could not be verified from static extraction
- The color #0051c3 may be a Cloudflare or framework-injected default rather than a deliberate Wesco brand choice — flagged as uncertain; used only for link states
- Hover and focus transition timing and easing curves are not extractable from color snapshot
- Authenticated vs. guest nav state differences (account badge, order-count indicator, contract-pricing display) not captured
- Cart and checkout page component treatment not included — procurement checkout likely has additional address, approval-workflow, and PO-number fields with distinct UI patterns
- Mobile header height and drawer animation duration not confirmed from extraction
