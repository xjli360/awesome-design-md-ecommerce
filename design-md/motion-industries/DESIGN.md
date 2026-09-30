---
version: alpha
name: "Motion Industries"
source_url: "https://www.motion.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Sixteen million SKUs, one search box — Motion Industries bets that catalog depth outweighs brand warmth, and the visual system agrees: spec sheets render faster than hero images, part numbers sit in monospace at `{typography.part-number}` weight, and the primary navigation bar arrives as a dense stripe in `{colors.primary}` anchoring every page before the product grid loads. The single extracted hex, `#313131`, is the near-black charcoal that carries all body copy and table text — a sign that the ink tier does the heaviest lifting, bearing manufacturer names, cross-reference codes, and availability callouts without typographic embellishment. Corner radii are deliberately minimal throughout: buttons sit at `{rounded.xs}` (4px), product cards at `{rounded.sm}` (8px), reflecting the procurement context where a buyer arrives with a PO number rather than a wishlist. The system font stack — system-ui, Segoe UI, Roboto, Helvetica Neue — signals zero tolerance for web font latency, a practical choice when maintenance managers check availability from a plant-floor tablet on intermittent connectivity. Category navigation spans bearings, power transmission, electrical, pneumatics, and fluid power, organized in a deep megamenu hierarchy rather than lifestyle collections; visual priority is faceted filtering and manufacturer logos, not editorial curation. Orange appears as the accent CTA (`{colors.accent}`) based on brand knowledge — Motion's marketing materials use a warm amber-orange to draw the eye to primary actions — though the exact hex could not be extracted due to Cloudflare anti-bot blocking on the live site. Price displays run larger than product imagery in many catalog views, and stock-status badges use a success/warning/danger system (`{colors.success}`, `{colors.warning}`, `{colors.danger}`) that mirrors industrial indicator-light conventions — green for in-stock, amber for limited, red for backorder — making procurement decisions scannable at a glance without reading prose.

colors:
  primary: "#004F9F"
  primary-dark: "#003D7A"
  primary-active: "#00336A"
  primary-disabled: "#80A7CF"
  accent: "#F47920"
  accent-active: "#D4641A"
  accent-disabled: "#F9BC90"
  ink: "#313131"
  body: "#444444"
  muted: "#6B6B6B"
  muted-soft: "#909090"
  hairline: "#D1D1D1"
  hairline-soft: "#E8E8E8"
  canvas: "#FFFFFF"
  surface-soft: "#F5F6F7"
  surface-card: "#FFFFFF"
  surface-dark: "#1A1A2E"
  on-primary: "#FFFFFF"
  on-accent: "#FFFFFF"
  on-dark: "#FFFFFF"
  success: "#27AE60"
  success-bg: "#EAF7EF"
  warning: "#E08A00"
  warning-bg: "#FFF8E7"
  danger: "#C0392B"
  danger-bg: "#FDF0EE"
  info: "#004F9F"
  info-bg: "#EBF2FA"
  part-number-bg: "#F0F4F9"
  promo: "#D4000F"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  part-number:
    fontFamily: "'Courier New', Courier, 'Roboto Mono', 'SF Mono', monospace"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  spec-value:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  price-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  label-upper:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  breadcrumb:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
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
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 44px
    hoverBackground: "{colors.accent-active}"
    disabledBackground: "{colors.accent-disabled}"
  button-primary-blue:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 44px
    hoverBackground: "{colors.primary-active}"
    disabledBackground: "{colors.primary-disabled}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 44px
    hoverBackground: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  button-sm-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
  search-bar:
    backgroundColor: "{colors.canvas}"
    inputTextColor: "{colors.ink}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    height: 48px
    submitButtonBackground: "{colors.accent}"
    submitButtonColor: "{colors.on-accent}"
    submitButtonWidth: 56px
    typography: "{typography.body-md}"
  top-account-bar:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    height: 36px
    linkColor: "{colors.on-dark}"
    borderBottom: "none"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
    logoHeight: 36px
    linkHoverBackground: "{colors.primary-active}"
    dropdownBackground: "{colors.canvas}"
    dropdownTextColor: "{colors.ink}"
    dropdownBorder: "1px solid {colors.hairline}"
  category-megamenu:
    backgroundColor: "{colors.canvas}"
    headerColor: "{colors.primary}"
    headerTypography: "{typography.title-sm}"
    linkColor: "{colors.body}"
    linkTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    columnGap: "{spacing.xl}"
    padding: "{spacing.lg}"
    rounded: "{rounded.none}"
    shadow: "0 4px 12px rgba(0,0,0,0.12)"
  breadcrumb-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.breadcrumb}"
    separatorColor: "{colors.muted-soft}"
    padding: "{spacing.sm} 0"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageBackground: "{colors.surface-soft}"
    imageHeight: 160px
    partNumberTypography: "{typography.part-number}"
    partNumberColor: "{colors.primary}"
    partNumberBackground: "{colors.part-number-bg}"
    titleTypography: "{typography.body-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.ink}"
    ctaButton: "button-primary"
    hoverShadow: "0 2px 8px rgba(0,0,0,0.10)"
  part-number-badge:
    backgroundColor: "{colors.part-number-bg}"
    textColor: "{colors.primary}"
    typography: "{typography.part-number}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  availability-badge-instock:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
    iconName: "check-circle"
  availability-badge-limited:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
    iconName: "clock"
  availability-badge-backorder:
    backgroundColor: "{colors.danger-bg}"
    textColor: "{colors.danger}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
    iconName: "x-circle"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.title-sm}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.spec-value}"
    valueColor: "{colors.ink}"
    rowBorder: "1px solid {colors.hairline-soft}"
    alternateRowBackground: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
  quantity-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 40px
    width: 72px
    buttonColor: "{colors.muted}"
    buttonHoverColor: "{colors.primary}"
  facet-filter:
    backgroundColor: "{colors.canvas}"
    headerTypography: "{typography.title-sm}"
    headerColor: "{colors.ink}"
    optionTypography: "{typography.body-sm}"
    optionColor: "{colors.body}"
    checkboxAccent: "{colors.primary}"
    countColor: "{colors.muted}"
    countTypography: "{typography.caption}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.xs}"
    activeBackground: "{colors.info-bg}"
  price-block:
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    unitColor: "{colors.muted}"
    unitTypography: "{typography.body-sm}"
    salePriceColor: "{colors.promo}"
    originalPriceDecoration: "line-through"
    originalPriceColor: "{colors.muted}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaButton: "button-primary"
    minHeight: 320px
    padding: "{spacing.section} {spacing.xl}"
  promo-banner:
    backgroundColor: "{colors.promo}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    height: 36px
    linkColor: "{colors.on-primary}"
    linkDecoration: underline
  footer:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "#A8C4E5"
    linkHoverColor: "{colors.on-dark}"
    headingTypography: "{typography.label-upper}"
    linkTypography: "{typography.body-sm}"
    borderTop: "4px solid {colors.accent}"
    padding: "{spacing.xxl} 0"
  account-dashboard-tile:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    headerBackground: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.title-sm}"
    bodyPadding: "{spacing.base}"

## Components

### Buttons

**`button-primary`** — Orange CTA (`{colors.accent}`, #F47920) on all primary purchase actions including Add to Cart, Request Quote, and checkout steps. Sits at 44px height with `{rounded.xs}` corners and `{typography.button-md}` (15px/600). Hover darkens to `{colors.accent-active}`; disabled state washes to `{colors.accent-disabled}`.

**`button-primary-blue`** — Same geometry as `button-primary` but in brand blue (`{colors.primary}`). Used for secondary-emphasis CTAs like "Find a Branch," "Contact Sales," and account-management actions where orange would compete with adjacent commerce elements.

**`button-secondary`** — White canvas with a `{colors.primary}` border and blue text. Pairs with `button-primary-blue` as a ghost peer; used for "Compare," "Save to List," and cancel/back flows. Hover fills `{colors.surface-soft}` to confirm interactivity without committing to full color.

**`button-ghost`** — Transparent background, blue text, no border. Applied inside product cards and table rows for space-constrained inline links like "See All Variants" or "View Datasheet."

### Search

**`search-bar`** — The highest-priority UI element on every catalog and category page. Input at full width with a 2px `{colors.primary}` border, height 48px, and a fixed 56px orange submit button (`{colors.accent}`) flush-right. System-font body text at 16px. Autocomplete dropdown inherits `{colors.surface-soft}` rows with `{typography.body-sm}` labels and manufacturer codes in `{typography.part-number}` monospace.

### Navigation

**`top-account-bar`** — A 36px dark-blue bar (`{colors.primary-dark}`) above the main nav carrying account links, order tracking, branch locator, and phone. Text at `{typography.body-sm}` in white; the high contrast signals utility-first rather than decorative intent.

**`nav-bar`** — 60px blue bar (`{colors.primary}`) with the Motion logo at 36px height, the main search bar, and icon buttons for account and cart. Link hover states darken to `{colors.primary-active}` rather than adding underlines.

**`category-megamenu`** — Full-width dropdown on a white canvas, organized in labeled column groups (Bearings, Power Transmission, Electrical, etc.). Column headers in `{colors.primary}` at `{typography.title-sm}`; links at `{typography.body-sm}` in `{colors.body}`. No imagery — purely text hierarchy reflecting the catalog's information density.

**`breadcrumb-bar`** — 36px strip in `{colors.surface-soft}` above product content. Crumb links at `{typography.breadcrumb}` in `{colors.muted}`; active/current segment in `{colors.ink}`. Separator uses a forward slash or chevron in `{colors.muted-soft}`.

### Product Cards & Catalog

**`product-card`** — Border card (`{colors.hairline}`, `{rounded.sm}`) with a white image zone on `{colors.surface-soft}` at 160px, a monospace part-number chip (`{typography.part-number}`, `{colors.primary}`, `{colors.part-number-bg}` pill), body title at `{typography.body-sm}`, and a price-plus-CTA footer row. Card lifts to `hoverShadow` on hover with no radius change, keeping the industrial geometry stable.

**`part-number-badge`** — Inline pill with monospace type at 13px/600, primary-blue text on a pale blue background (`{colors.part-number-bg}`). Applied wherever a manufacturer part number, Motion catalog number, or cross-reference code appears in line with prose text.

**`spec-table`** — Two-column key-value grid with alternating `{colors.surface-soft}` row backgrounds and hairline dividers. Labels at `{typography.spec-label}` in `{colors.muted}`; values at `{typography.spec-value}` in `{colors.ink}`. Section headers use `{typography.title-sm}` on a `{colors.surface-soft}` full-width row. The most space-intensive component on PDP pages.

**`quantity-input`** — 72px-wide number input flanked by increment/decrement buttons, 40px tall, `{rounded.xs}`. Tap targets on each button are minimum 32×40px. Sits directly left of the primary Add to Cart button.

**`facet-filter`** — Left-rail accordion of filterable dimensions (Brand, Availability, Bore Diameter, Series, etc.). Each option is a labeled checkbox with a count badge at `{typography.caption}` in `{colors.muted}`. Active filters fill `{colors.info-bg}` rows. Headings at `{typography.title-sm}`. Collapses to a slide-up sheet on mobile.

### Availability & Pricing

**`availability-badge-instock`** / **`availability-badge-limited`** / **`availability-badge-backorder`** — Three-state system using `{colors.success}`, `{colors.warning}`, and `{colors.danger}` text on matching `_bg` fills. All use `{typography.label-upper}` (11px, uppercase, 0.8px tracking) with a leading status icon. Mirrors the traffic-light logic of plant-floor indicator panels — the target audience reads this convention instantly.

**`price-block`** — Primary price at `{typography.price-display}` (22px/700) in `{colors.ink}`, with a per-unit label at `{typography.body-sm}` in `{colors.muted}`. Sale overrides display the promotional price in `{colors.promo}` (#D4000F) with the original struck through in `{colors.muted}`.

### Layout

**`hero-banner`** — Full-width blue hero (`{colors.primary}`) at 320px minimum height, headline at `{typography.display-xl}`, subhead at `{typography.body-md}`, single orange CTA button. Used on homepage and category landing pages; product catalog pages skip the hero to surface search and facets immediately.

**`promo-banner`** — 36px red strip (`{colors.promo}`) above the account bar for site-wide promotions, free-freight thresholds, or seasonal campaigns. Dismissed state collapses the row entirely.

**`footer`** — Dark blue (`{colors.primary-dark}`) with a 4px top accent border in `{colors.accent}`. Four-column link grid with `{typography.label-upper}` section heads and `{typography.body-sm}` links in muted blue (#A8C4E5). Social, legal, and compliance links in a secondary row below.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; facet filters collapse to a bottom sheet triggered by a "Filter" pill button; megamenu becomes a full-screen accordion drawer; search bar fills full width below the logo row; account bar collapses to icon-only |
| Tablet | 744–1128px | Two-column product grid; left-rail facets render as collapsible panels, not a drawer; megamenu remains a dropdown but narrows to two columns; search bar retains full-width placement in nav |
| Desktop | 1128–1440px | Three-column product grid; four-column facet rail at 240px fixed width; megamenu spans four to six columns; price block and quantity input stack horizontally on PDP |
| Wide | > 1440px | Grid adds a fourth product column; content max-width at 1440px centered; hero banner background extends to viewport edge while content remains constrained |

### Touch Targets

- All primary CTA buttons minimum 44×44px
- Quantity increment/decrement buttons minimum 40×40px; full row tap area extends to 44px
- Facet checkboxes minimum 44px row height to accommodate industrial gloves or thick-finger use cases
- Nav icon buttons (cart, account, search) minimum 48×48px on mobile
- Breadcrumb links minimum 36px tap height with `{spacing.sm}` vertical padding

### Collapsing Strategy

- Left-rail facet filter becomes a "Filter & Sort" floating button that opens a bottom sheet with full facet tree at mobile widths
- Category megamenu collapses to a hamburger drawer with top-level accordion expand; subcategories indent one level rather than opening nested drawers
- Spec table scrolls horizontally rather than reflowing — preserves label-value column alignment for comparison reading
- Account and order-management utility links in the top bar collapse into the hamburger menu on mobile rather than an icon overflow
- Promo banner remains visible on all breakpoints but reduces to a single-line centered message on mobile (no dismiss button to save vertical space)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Full site palette not extractable**: motion.com returned a Cloudflare challenge page ("Just a moment...") during extraction; only `#313131` was captured. All other colors (primary blue, accent orange, surface tones) are derived from brand knowledge of Motion Industries' marketing materials and should be verified against the live design system
- **Primary blue hex unconfirmed**: `#004F9F` is a reasonable approximation of Motion's brand blue based on publicly visible logo and marketing assets; the exact hex may differ from the production design token
- **Accent orange hex unconfirmed**: `#F47920` (amber-orange) is based on brand knowledge; Motion's marketing sometimes uses a slightly warmer or cooler orange variant
- **No custom font detected**: The entire type system uses OS system fonts (system-ui, Segoe UI, Roboto). If Motion uses a licensed typeface (e.g., in print or video), it was not detectable on the web build
- **Component interaction patterns unverified**: Hover, focus, and active states are extrapolated from standard B2B e-commerce conventions; actual Motion design tokens for state variants require inspection of the live DOM
- **Account/B2B portal design unknown**: Logged-in procurement portal, PO management, and contract pricing views could not be accessed or scraped; those surfaces may deviate significantly from the public catalog design
- **Dark mode unknown**: No `prefers-color-scheme` tokens were detectable; it is unclear whether Motion supports a dark variant
