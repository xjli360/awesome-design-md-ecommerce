---
version: alpha
name: "Creality"
source_url: "https://www.creality.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The print-bed status indicator—a neon #17cc5f that reads equal parts factory signal and gaming RGB—anchors every primary CTA on Creality's site, from the hero "Shop Now" to the cart confirmation. That green runs through a fundamentally dark-mode product experience: near-black panels at #1e1e1e form the hero canvas, lighter #383838 and #363131 surfaces hold secondary content, and the light-mode product-listing pages shift to a blue-tinged off-white #f5f6fa that keeps the brand from feeling purely industrial. CrealitySans, a custom brand typeface, carries all display headings; HarmonyOS Sans SC fills the CJK character set for Chinese-market parity, reflecting that Creality is a Shenzhen-originating manufacturer whose site serves both domestic and global maker audiences simultaneously. A second voltage—electric cyan at #00bbff and #03bef1—appears on feature callouts and secondary graphic elements, mapping directly to the green/blue status LEDs present on physical Creality hardware: green means go, cyan means information. Rounded corners are restrained and utilitarian: {rounded.sm} on buttons and inputs, {rounded.md} on product cards, {rounded.full} reserved only for filter chips and search fields. Typography weights skew heavier than lifestyle brands—600–700 for titles at 18–24px—because the audience reads watt ratings and layer-resolution specs, not aspirational copy. The many Ant Design system colors (#1677ff, #722ed1, #13c2c2) visible in extraction belong to dashboard and admin surfaces beneath the consumer storefront and are excluded from the component system below. Prices display prominently at 24px/700 with struck-through originals beside them; the product card is the commercial engine, and everything else on the page drives toward it.

colors:
  primary: "#17cc5f"
  primary-hover: "#24ca49"
  primary-active: "#15b854"
  primary-disabled: "#dcf7de"
  primary-muted: "#8ff2ad"
  ink: "#1e1e1e"
  body: "#383838"
  body-secondary: "#3a3c52"
  muted: "#5a5c62"
  muted-soft: "#98999e"
  hairline: "#cbccd1"
  hairline-soft: "#ebedf5"
  canvas: "#ffffff"
  canvas-page: "#f5f6fa"
  surface-soft: "#ebedf5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  dark-canvas: "#1e1e1e"
  dark-surface: "#363131"
  dark-surface-alt: "#3a3c52"
  accent-cyan: "#00bbff"
  accent-cyan-alt: "#03bef1"
  status-error: "#e73c3c"
  status-warning: "#fa8c16"
  status-success: "#52c41a"
  badge-hot-fill: "#fa541c"

typography:
  display-xl:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  spec-label:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-original:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  button-lg:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'CrealitySans', 'HarmonyOS Sans SC', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 10px
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    border: "1.5px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
  button-ghost-dark:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.canvas}"
    rounded: "{rounded.sm}"
    padding: 10px 24px
    height: 40px
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
    placeholderColor: "{colors.muted-soft}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
    padding: 10px 48px 10px 16px
    height: 44px
    iconColor: "{colors.muted}"
    iconFocusedColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.dark-surface}"
    logoAccentColor: "{colors.primary}"
    activeIndicatorColor: "{colors.primary}"
    activeIndicatorHeight: 2px
  nav-bar-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoAccentColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    originalPriceTypography: "{typography.price-original}"
    originalPriceColor: "{colors.muted-soft}"
    originalPriceDecoration: line-through
    badgePosition: top-left
    hoverShadow: "0 4px 16px rgba(0,0,0,0.10)"
    hoverTransform: translateY(-2px)
    hoverTransition: "transform 0.2s ease, box-shadow 0.2s ease"
  hero-banner:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.canvas}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.muted-soft}"
    accentColor: "{colors.primary}"
    minHeight: 560px
    padding: "{spacing.xxl} {spacing.section}"
  hero-banner-gradient:
    background: "linear-gradient(135deg, {colors.dark-canvas} 0%, {colors.dark-surface-alt} 100%)"
    textColor: "{colors.canvas}"
    headingTypography: "{typography.display-xl}"
    accentColor: "{colors.accent-cyan}"
    accentAlt: "{colors.accent-cyan-alt}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 40px
    linkColor: "{colors.on-primary}"
    linkDecoration: underline
  spec-badge:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.canvas}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  spec-badge-highlight:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.status-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-hot:
    backgroundColor: "{colors.badge-hot-fill}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    height: 34px
    border: "1px solid {colors.hairline}"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    height: 34px
    border: "1px solid {colors.primary}"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.canvas-page}"
    headerTypography: "{typography.title-sm}"
    headerColor: "{colors.ink}"
    cellTypography: "{typography.body-sm}"
    cellColor: "{colors.body}"
    checkIconColor: "{colors.primary}"
    xIconColor: "{colors.status-error}"
    borderColor: "{colors.hairline}"
    stickyColumnBorder: "2px solid {colors.hairline}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.hairline}"
  rating-stars:
    filledColor: "{colors.primary}"
    emptyColor: "{colors.hairline}"
    countTypography: "{typography.caption}"
    countColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.primary}"
    borderTop: "1px solid {colors.dark-surface}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Solid #17cc5f fill at 44px tall, CrealitySans 600/16px, {rounded.sm} corners, padding 12px 28px. Hover brightens to #24ca49 via a short 0.15s ease transition; press darkens to #15b854; disabled bleaches to the #dcf7de tint with {colors.muted-soft} text. Used for every primary commerce action: "Shop Now", "Add to Cart", "Check Out".

**`button-secondary`** — Transparent background with a 1.5px #17cc5f border and matching green text. Structurally identical in height and padding to button-primary so both variants can sit side-by-side on a product detail page without optical misalignment. Common for "Add to Wishlist" and "Compare" actions.

**`button-ghost-dark`** — 1px white border, white text on dark hero backgrounds. The thinner border reads lighter against #1e1e1e, creating visual hierarchy when paired with button-primary on the same dark section.

**`button-sm`** — 32px-tall green fill for inline card actions like "Buy Now"; uses {typography.button-sm} at 13px/500 weight to avoid competing with the product title.

### Navigation

**`nav-bar`** — Dark #1e1e1e bar at 64px height. The Creality wordmark has its 'C' mark rendered in {colors.primary} against white text. Primary nav links are 15px/500 in CrealitySans, white on dark, with a 2px {colors.primary} underline appearing on the active section. Cart icon carries a small green dot badge for item count. A 1px {colors.dark-surface} border-bottom separates it from page content.

**`nav-bar-light`** — White-background variant used on product-listing inner pages; ink-colored links, {colors.hairline-soft} border bottom, logo accent still green. Both nav variants share identical 64px height so page layout does not shift on route transitions.

### Inputs

**`text-input`** — 42px height with 1px {colors.hairline} border transitioning to {colors.primary} on focus. No box-shadow on focus—the green border color change is sufficient and keeps the aesthetic flat. Placeholder at {colors.muted-soft}.

**`search-bar`** — Pill-shaped ({rounded.full}) field with a magnifier icon at {colors.muted}. Present in the nav (collapsed to icon on mobile) and as a prominent element on search results pages. Icon color shifts to {colors.primary} on focus alongside the border change.

### Product Cards

**`product-card`** — 1px {colors.hairline-soft} border, {rounded.md} corners, white surface. Hover lifts 2px with a diffuse shadow (`0 4px 16px rgba(0,0,0,0.10)`) via a 200ms ease transition. Price displays at {typography.price-display} (24px/700) with struck-through original price in {colors.muted-soft}. Badge stickers (NEW, SALE, HOT) are absolutely positioned at top-left, color-coded green/red/orange respectively. Card image area uses a white background to avoid clashing with product renders shot on white.

### Hero & Banners

**`hero-banner`** — Full-bleed #1e1e1e background, {typography.display-xl} heading in white, body subhead in {colors.muted-soft}, and a green primary CTA button. Minimum height 560px with generous `{spacing.xxl} {spacing.section}` padding. Product photography or 3D render fills the right half of the composition.

**`hero-banner-gradient`** — Variant that blends {colors.dark-canvas} to the near-purple {colors.dark-surface-alt} diagonally. Secondary graphic elements (speed indicators, layer-resolution callouts) are rendered in {colors.accent-cyan} (#00bbff) against the gradient, creating the green-action / cyan-information visual grammar.

**`announcement-bar`** — 40px solid {colors.primary} strip pinned above the nav for promotions and limited-time offers. White {typography.body-sm} text with underlined white links. Dismissible via a × icon at the right edge.

### Badges & Labels

**`badge-new`** — #17cc5f fill, white uppercase text at 11px/700, {rounded.xs}. Overlaid at top-left of product card image areas for new product launches.

**`badge-sale`** — #e73c3c fill, identical geometry. Distinguishes sale/discount events from new arrivals at a glance.

**`badge-hot`** — #fa541c orange fill for trending or high-demand products. Three-color badge vocabulary (green/red/orange) maps to maker-audience signal conventions without needing text labels.

**`spec-badge`** — Dark #363131 pill with white {typography.spec-label} text used inline within product-detail spec grids (e.g., "600 mm/s max speed", "300×300×300 mm"). A highlight variant uses {colors.primary} fill for marketing-forward claims that belong in ad copy rather than a spec table.

### Comparison & Filters

**`comparison-table`** — Multi-column printer comparison grid with sticky left model-name column. Check marks in {colors.primary}, ✗ in {colors.status-error}. Column headers on {colors.canvas-page}, body rows white. Used extensively for Ender vs. K1 series purchase decisions.

**`category-chip`** / **`category-chip-active`** — Pill-shaped filter tags in {colors.surface-soft} with {colors.muted} text; active state inverts to {colors.primary} fill, white text. Used in both horizontal filter strips on listing pages and sidebar filter panels.

### Footer

**`footer`** — #1e1e1e background with four-column link grid. Section headings in white {typography.title-sm}; body links in {colors.muted-soft} transitioning to {colors.primary} on hover. Bottom bar holds social icons, regional store selectors, and certification logos. 1px {colors.dark-surface} top border separates the footer from the last page section.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger drawer replaces horizontal nav; hero heading scales to {typography.display-md} (28px); search collapses to tap icon; spec tables scroll horizontally; comparison table replaced with a "Compare" select UI |
| Tablet | 744–1128px | Two-column product grid; nav items condensed with icon-only secondary links; hero heading at {typography.display-lg} (36px); side filter panel becomes a bottom-sheet or slide-in drawer |
| Desktop | 1128–1440px | Three- or four-column product grids; full horizontal nav with mega-menu category dropdowns; hero at full {typography.display-xl} (48px); comparison table fully visible |
| Wide | > 1440px | Max-width container ~1440px centered; hero images extend full-bleed behind the container; four- or five-column product grids on category landing pages |

### Touch Targets

- All primary buttons minimum 44px tall (button-primary, button-secondary)
- Nav icons minimum 40×40px tap area
- Product card full image area acts as a tap target for navigation on mobile
- Filter chips minimum 34px height ({category-chip})
- Close and dismiss icons on modals and drawers minimum 44×44px

### Collapsing Strategy

- Mega-menu nav collapses to a left-slide hamburger drawer at < 1128px; drawer uses nested accordion for product category tiers
- Three-column hero feature strips (speed / precision / connectivity) collapse to horizontal swipe carousel on mobile with no visible pagination controls
- Comparison table collapses to a floating "Compare bar" that activates when two or more products are checkbox-selected on mobile
- Four-column footer link grid collapses to accordion sections on mobile, each section starts collapsed
- Announcement bar persists across all breakpoints; long promotional copy truncates to a single line with ellipsis

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact nav height (estimated 64px) not confirmed from extraction; transparent-on-scroll and sticky transition variants not captured
- Shadow token values on product-card hover approximated; no shadow scale extracted from the live site
- Hero section treatment (parallax scroll, video autoplay, static image) not determinable from color extraction alone
- CrealitySans typeface metrics (x-height, cap-height, precise tracking) unavailable; letterSpacing values are estimates
- Modal and overlay design (backdrop blur amount, scrim opacity, animation easing) not in extracted data
- Dark-mode vs. light-mode page split logic not fully documented; hero/landing pages appear dark-first, product listings light-first, but the rule is not confirmed
- Ant Design system colors (#1677ff, #722ed1, #13c2c2, #52c41a, #fadb14, #fa541c, #2f54eb, etc.) appear in extraction and belong to internal dashboard/CMS surfaces — excluded from this consumer-facing design system
- Sale price color treatment on product cards not confirmed; some templates may render the discounted price in {colors.status-error} rather than the standard {colors.ink}
- Exact logo lockup dimensions and clear-space rules not extractable from static scrape
