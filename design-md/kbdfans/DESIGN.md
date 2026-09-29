---
version: alpha
name: "KBDfans"
source_url: "https://kbdfans.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The checkout button on KBDfans lives at #fb485e — a coral that reads somewhere between fire-engine alarm and neon-salmon, hot enough to arrest a product-grid scroll without torching the mostly dark-neutral interface built around #121212. Two reds anchor the brand: the coral-primary for CTAs and interactive highlights, and #d7030b — a deeper, near-arterial red — reserved for group-buy countdowns and stock-pressure states, creating a two-tier urgency vocabulary that maps directly onto the keyboard community's calendar anxiety around limited runs. The near-black field absorbs product photography cleanly; anodized aluminum cases and POM plates render crisply against the low-reflectance background, so the brand shell stays recessive and lets the hardware carry visual weight.

  No custom font stack was recovered from the live extraction; the typographic feel is a clean geometric grotesque — likely a system font stack or a runtime-loaded web font. Weight contrast does the structural work: product display names push weight 700, specification labels hold at 600, and body descriptions settle at 400 across a 14–15px range that accommodates dense compatibility tables and switch-feel breakdowns without fatigue. All-caps tracked labels on navigation tabs, stock badges, and category chips lend a technical spec-sheet register that fits an audience fluent in keyboard jargon.

  The overall UX register is pragmatic-collector rather than aspirational lifestyle. The homepage opens to an organized product grid with sale badges, group-buy timer overlays, and hot-swap compatibility indicators rather than editorial splash screens or ambient video loops. SKU matrices, build-kit bundle callouts, and per-switch acoustic ratings live in the card layer rather than a filtered discovery flow, presupposing a customer who already understands what a gasket mount or PCB hot-swap socket means and is optimizing for fast spec verification. #dedede provides the only stretch of neutral lightness — used for dividers, input borders, and disabled-state fills — while the canvas stays bright white to keep product images color-accurate across displays.

colors:
  primary: "#fb485e"
  primary-active: "#d7030b"
  primary-disabled: "#fd9caa"
  danger: "#d7030b"
  ink: "#121212"
  body: "#2a2a2a"
  muted: "#888888"
  hairline: "#dedede"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  group-buy-bg: "#d7030b"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-uppercase:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.01em
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.01em
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.05em
    textTransform: uppercase

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
    height: 48px
    hover:
      backgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "1px solid {colors.hairline}"
    hover:
      border: "1px solid {colors.ink}"
  button-outline-danger:
    backgroundColor: transparent
    textColor: "{colors.danger}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.danger}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    padding: "10px {spacing.base}"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoArea: 140px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    hoverColor: "{colors.primary}"
    padding: "0 {spacing.md}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    comparePriceColor: "{colors.muted}"
    padding: "{spacing.base}"
    hover:
      boxShadow: "0 4px 16px rgba(0,0,0,0.08)"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  group-buy-badge:
    backgroundColor: "{colors.group-buy-bg}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  stock-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  switch-option-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "6px 12px"
    minHeight: 40px
    selected:
      border: "2px solid {colors.primary}"
      textColor: "{colors.primary}"
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selected:
      border: "2px solid {colors.primary}"
      outlineGap: "2px solid {colors.canvas}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px {spacing.base}"
    height: 40px
    iconColor: "{colors.muted}"
  countdown-timer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    digitTypography: "{typography.display-md}"
    labelTypography: "{typography.label-uppercase}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    rowDivider: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — The add-to-cart and checkout trigger, filled in {colors.primary} (#fb485e) with white label set in {typography.button-md} at 600 weight. On hover it steps to {colors.primary-active} (#d7030b), staying within the red-family register rather than changing hue, and the {rounded.sm} (8px) corner is used consistently across all transactional buttons — the brand avoids pill shapes on purchase actions to keep the tone direct. The disabled variant (`button-primary-disabled`) uses {colors.primary-disabled}, a pastel tint of the primary, which maintains the color vocabulary without implying affordance.

**`button-secondary`** — White fill, {colors.ink} text, and a 1px {colors.hairline} border at rest. Used for wishlist, "View Details," and secondary PDP actions. Border upgrades to full {colors.ink} on hover without any fill change, communicating interactivity through contrast alone.

**`button-outline-danger`** — Transparent fill with {colors.danger} text and border at {typography.button-sm} scale. Reserved for remove-from-cart and destructive form actions; shares the same red as `button-primary-active` to make danger states visually coherent with the primary palette.

### Text Input

**`text-input`** — {colors.canvas} fill, 1px {colors.hairline} border upgrading to {colors.ink} on focus at 44px height. Placeholder color is {colors.muted} at {typography.body-md}. Used in checkout forms, address fields, and the group-buy notification signup; the focus treatment is border-only with no ring or shadow, keeping form density clean on long checkout flows.

### Navigation

**`nav-bar`** — 64px-tall white bar with a 1px {colors.hairline} bottom separator. Logo sits in a 140px-wide left anchor; the center carries category dropdowns (Keyboards, Switches, Keycaps, Accessories, Group Buys); the right cluster holds the search bar, account icon, and cart. The entire center nav collapses behind a hamburger at tablet and below.

**`nav-link`** — {typography.body-md} at weight 400, color shifts to {colors.primary} on hover — the same coral as the CTA buttons, anchoring the single-brand-color interactive vocabulary across both navigation and transaction surfaces.

### Product Card

**`product-card`** — White {colors.surface-card} surface with a nearly invisible 1px {colors.hairline-soft} border at rest; on hover, a shallow box shadow (0 4px 16px rgba black at 8%) lifts the card without heavy elevation. Product name renders at {typography.title-sm}, price at {typography.price-display} in {colors.ink}, with the compare-at (original) price struck through in {colors.muted} alongside the sale badge. The sale badge overlays the image at top-left in {colors.primary}; group-buy cards carry a {colors.group-buy-bg} badge to visually separate pre-sale from discounted inventory at a glance in mixed grids.

### Badges

**`sale-badge`** — Compact {rounded.xs} block, {colors.primary} fill, white {typography.badge} text at 11px uppercase. Appears on card image overlays and inline beside collection-list prices.

**`group-buy-badge`** — Structurally identical to `sale-badge` but uses {colors.group-buy-bg} (#d7030b) to distinguish limited-window pre-orders from in-stock discounts in a single visual scan.

**`stock-badge`** — Neutral {colors.surface-soft} fill with {colors.body} text; carries fulfillment states like "In Stock," "Ships Next Week," and "Sold Out" where urgency signaling is not the intent.

### Switch / Color Selectors

**`switch-option-chip`** — Outlined selector chip for switch types (Linear, Tactile, Clicky, Silent) and other attribute variants. Rest state uses {colors.hairline} border at {rounded.xs}; selected state upgrades to a 2px {colors.primary} border with {colors.primary} text. Chips run left-to-right in a wrapping row on desktop, switching to a horizontal scroll row on mobile.

**`color-swatch`** — A 24px circle with a transparent 2px border at rest; the selected state adds a {colors.primary} outer ring with a 2px {colors.canvas} gap between swatch fill and ring, creating a legible selection indicator against any swatch color including near-white and near-black options.

### Search Bar

**`search-bar`** — {rounded.full} pill shape in {colors.surface-soft} with a left-aligned magnifier icon in {colors.muted}. Placeholder in {colors.muted} at {typography.body-sm}. On mobile the bar expands to a full-screen overlay with a pinned close button, allowing the search experience to occupy the viewport without fighting the product grid.

### Hero Banner

**`hero-banner`** — Full-bleed {colors.surface-dark} (#121212) panel with the headline in {typography.display-xl} ({colors.on-dark}) and a supporting line in {typography.body-md}. Minimum 480px tall; on desktop a product photograph fills the right half in a 50/50 split over the dark background. New-collection reveals and seasonal sale promotions use the same template; the dark canvas ensures high-contrast legibility regardless of image content.

### Countdown Timer

**`countdown-timer`** — A dark-panel component ({colors.surface-dark}) with digit blocks set in {typography.display-md} ({colors.on-dark}) and {typography.label-uppercase} unit labels (HH, MM, SS) below each block. The separator dot between digit pairs uses {colors.primary} to tie the timer's visual accent back to the CTA color. Applied to group-buy open and close deadlines and to flash-sale end times; this is the highest-urgency signal in the product detail page hierarchy.

### Spec Table

**`spec-table`** — Two-column or multi-column table for keyboard specifications: layout, mount type, PCB type, plate material, typing angle, weight, and connector. Header row carries {colors.surface-soft} fill with {typography.caption} labels; body rows alternate transparent and {colors.hairline-soft} backgrounds. Outer border at {colors.hairline} with {rounded.sm} clip. Present on nearly every keyboard product detail page and on build-kit landing pages that compare multiple configurations.

### Footer

**`footer`** — Full-width {colors.surface-dark} (#121212) block. Link column headings use {typography.label-uppercase} in {colors.hairline}; body links at {typography.body-sm} inherit {colors.on-dark} at rest and shift to {colors.primary} on hover. Column structure covers Shop, Support, Community, Social, and Legal. The newsletter signup row embeds a single text input with an inverted-border treatment (1px {colors.hairline} stroke over the dark background) and a {button-primary} submit button.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; search expands to full-screen overlay; hero stacks copy above image; switch-option-chips scroll horizontally; countdown timer digit blocks arranged 2×2 |
| Tablet | 744–1128px | 2-column product grid; nav shows logo and icons only with hamburger still active; hero splits 60/40 copy/image; spec table becomes horizontally scrollable |
| Desktop | 1128–1440px | 4-column product grid; full nav with dropdown menus; hero 50/50 split; spec table full-width inline |
| Wide | > 1440px | Centered 1440px max-width container; product grid holds 4 columns with increased card padding; hero image extends edge-to-edge behind a centered text column |

### Touch Targets

- All primary buttons minimum 44×44px tap target per WCAG 2.5.5
- Cart, account, and hamburger icon buttons padded to 44×44px tap area
- Switch-option-chips minimum 40px tall with {spacing.sm} gap between chips
- Color swatches padded to 36×36px tap area around the 24px visual circle
- Nav dropdown links minimum 44px tall row height in the mobile drawer

### Collapsing Strategy

- Category nav fully collapses to a full-height slide-in drawer at ≤ 1127px; dropdown hover states become tap-to-expand accordions
- Product filter sidebar on collection pages collapses to a bottom-sheet modal on mobile, invoked by a "Filter & Sort" pill button pinned above the grid
- Spec tables scroll horizontally on mobile rather than reflowing, preserving column alignment for multi-attribute comparisons
- Cart sidebar becomes a full-screen modal on mobile
- Group-buy countdown timer stacks into a 2×2 digit grid below 480px viewport width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family stack extracted from live site; typeface is either a Shopify theme system font or a JS-loaded web font (Inter, Neue Haas Grotesk, and GT Walsheim are common in this store category) — all typography tokens default to the system sans-serif stack and must be verified against the live CSS
- Only four hex values extracted; no confirmed secondary accent color, success/warning/info semantic states, loyalty or tier badge palette, or community-rank color system
- No border-radius values confirmed from live CSS; {rounded.sm} (8px) is assumed from Shopify-store conventions and the extracted category context
- No spacing scale confirmed from live extraction; all spacing tokens are conventional Shopify defaults
- No confirmed hover/active state transition timings or easing curves
- Dark-mode toggle support unknown — {colors.surface-dark} (#121212) appears in hero and footer but whether a site-wide dark mode is available is unconfirmed
- Group-buy vs. pre-order vs. interest-check badge differentiation beyond fill color (icons, border patterns) not confirmed from extraction
- No confirmed icon system or icon library; KBDfans likely uses a custom or licensed icon set not captured in HTML/CSS extraction
