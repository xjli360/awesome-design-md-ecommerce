---
version: alpha
name: "Ergo Direct"
source_url: "https://www.ergodirect.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The deep-sea blue at #014d73 — closer to the ink on a clinical reference chart than to the sky-blue of consumer electronics — announces that this is a brand selling prevention, not decoration. ErgoDirect pairs that navy foundation against a vitality green (#009122) that confirms add-to-cart actions and in-stock status, borrowing a color vocabulary from medical-device dashboards rather than home-goods catalogues. The near-black #1a1a2e anchors headlines, while body copy descends through #1f2937 and settles into #6b7280 for metadata — a stepped gray ramp designed to make dense specification tables scannable by facilities managers comparing torque ratings and monitor weight capacities across dozens of SKUs.

  Type runs in Lato — a geometric humanist with clinical precision at small sizes — set at moderate weights; heavy display type would signal bravado, and this brand signals reliability. The rounded system is deliberately conservative: `{rounded.xs}` at 4px for input fields and filter chips, `{rounded.sm}` at 8px for primary buttons, with nothing softer than `{rounded.md}` in the product grid. Hard corners on utility interfaces reinforce a procurement mindset rather than a lifestyle one. Canvas sits at #f8fafc, barely off-white, with card surfaces on pure white against hairline borders at #e0e3e8, organizing grids of arms, stands, and mounts without decorative flourish.

  Alert red (#dc2626) marks clearance pricing and warning states; amber (#f59e0b) tags promotional callouts; a lighter sky tone (#0ea5e9) surfaces for informational notices. The secondary blue #0066a1 handles hyperlinks and secondary CTAs, sitting one rung below the primary #014d73 in visual hierarchy. Both blues — plus the green accent — read as purposeful system signals rather than expressive color choices, which is appropriate for a catalog where a buyer must quickly distinguish a $150 entry-level arm from a $600 professional dual mount.

  The brand's visual logic mirrors its product promise: reduce pain by making the right choice obvious. Dense but legible grid layouts, well-separated badge typologies, and a font stack that defaults to Lato then Roboto then system sans-serif all serve a user who is comparing, evaluating, and purchasing rather than browsing for inspiration. Nothing in the system reaches for warmth or whimsy; every token earns its place by making a specification clearer or a decision faster.

colors:
  primary: "#014d73"
  primary-active: "#013e5c"
  primary-disabled: "#ccdbe3"
  secondary-blue: "#0066a1"
  sky: "#0ea5e9"
  sky-tint: "#cfedfb"
  ink: "#1a1a2e"
  body: "#1f2937"
  muted: "#6b7280"
  muted-light: "#9ca3af"
  hairline: "#e0e3e8"
  hairline-soft: "#e5e7eb"
  canvas: "#f8fafc"
  surface-soft: "#f1f5f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#009122"
  accent-green-dark: "#116600"
  accent-green-tint: "#cce9d3"
  alert-red: "#dc2626"
  alert-red-tint: "#f8d4d4"
  amber: "#f59e0b"
  amber-tint: "#fdecce"
  dark-navy: "#313143"
  slate: "#64748b"

typography:
  display-xl:
    fontFamily: "Lato, Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Lato, Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-md:
    fontFamily: "Lato, Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Lato, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "Lato, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Lato, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Lato, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "Lato, Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Lato, Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-original:
    fontFamily: "Lato, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
    textDecoration: line-through
  button-md:
    fontFamily: "Lato, Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "Lato, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.25px
  nav-link:
    fontFamily: "Lato, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  label:
    fontFamily: "Lato, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "Lato, Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.25px
  spec-label:
    fontFamily: "Lato, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 700
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    border: "1px solid {colors.hairline}"
  button-add-to-cart:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-light}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 42px
    focusBorder: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
    topBarBackground: "{colors.primary-active}"
    topBarTypography: "{typography.caption}"
    topBarTextColor: "{colors.on-primary}"
    topBarHeight: 34px
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    shadow: "0 4px 16px rgba(0,0,0,0.12)"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    imageBackground: "{colors.canvas}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    shadow: "0 1px 4px rgba(0,0,0,0.06)"
    hoverShadow: "0 4px 12px rgba(0,0,0,0.10)"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    minHeight: 400px
    overlayStart: "rgba(1,77,115,0.72)"
    overlayEnd: "rgba(1,62,92,0.90)"
  badge-sale:
    backgroundColor: "{colors.alert-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-in-stock:
    backgroundColor: "{colors.accent-green-tint}"
    textColor: "{colors.accent-green-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-low-stock:
    backgroundColor: "{colors.amber-tint}"
    textColor: "{colors.amber}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-out-of-stock:
    backgroundColor: "{colors.alert-red-tint}"
    textColor: "{colors.alert-red}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-info:
    backgroundColor: "{colors.sky-tint}"
    textColor: "{colors.secondary-blue}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 42px
    submitBackground: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitTypography: "{typography.button-md}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: none
  spec-table:
    backgroundColor: "{colors.surface-card}"
    labelColor: "{colors.body}"
    valueColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline-soft}"
    altRowBackground: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
  trust-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    iconColor: "{colors.primary}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.lg} {spacing.section}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.primary}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-light}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 36px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "#c6c8ca"
    linkColor: "{colors.sky-tint}"
    headingTypography: "{typography.label}"
    headingColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    borderTop: "4px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — The primary CTA runs #014d73 at 44px height with {rounded.sm} corners and Lato Bold at 15px with 0.25px letter-spacing. Hover deepens to {colors.primary-active} (#013e5c); disabled state uses the pale {colors.primary-disabled} tint (#ccdbe3) so inactive states read clearly without disappearing entirely on the white canvas.

**`button-add-to-cart`** — Add-to-cart actions use {colors.accent-green} (#009122) rather than the primary blue, creating an unmistakable visual cue that this button commits a transaction. It stands 4px taller than standard CTAs at 48px to signal conversion importance on product detail pages, where it competes with specification data for attention.

**`button-secondary`** — A 1px {colors.primary} border on a white canvas, matching the primary button's dimensions at 44px. Used for Compare, Request Quote, and secondary navigation actions where the primary CTA is already occupied by Add to Cart.

**`button-ghost`** — Smaller ghost variant at {typography.button-sm} (13px) for inline actions like View Details or filter resets. Uses {colors.hairline} border to reduce visual weight alongside dense product grids and spec tables.

### Product Card

**`product-card`** — White surface ({colors.surface-card}) with a 1px {colors.hairline-soft} border and {rounded.xs} corners, reading as a catalog card rather than a lifestyle tile. The image well uses {colors.canvas} (#f8fafc) to harmonize product shots that have varying backgrounds. Title runs {typography.title-sm} (Lato 700/16px); sale price in {typography.price-sm} (Lato 700/18px) with original price struck through in {typography.price-original}. Hover lifts shadow from a 1px ambient base to a 4px lift without translate animation — appropriate for a procurement interface where hover indicates intent rather than play.

### Badges

**`badge-sale`** — Red (#dc2626) tag at {rounded.xs}, 11px Lato Bold, placed in the top-left corner of product card image wells for price-reduced SKUs. Pair with {typography.price-original} struck-through text to complete the discount signal.

**`badge-in-stock`** / **`badge-low-stock`** / **`badge-out-of-stock`** — A three-state inventory typology using the green/amber/red signal system, each with a tinted background drawn from the extracted palette (accent-green-tint, amber-tint, alert-red-tint). These badges are load-bearing for B2B buyers comparing multiple SKUs for bulk office procurement; they must read without relying on color alone, so the text label is always present.

**`badge-info`** — Sky-tint (#cfedfb) background with {colors.secondary-blue} text, used for shipping estimates, free-setup-guide flags, and compatibility notices on product cards.

**`badge-new`** — Primary blue pill used for recently launched SKUs, keeping the green reserved exclusively for stock status to prevent signal collision.

### Navigation

**`nav-bar`** — Two-tier header: a 34px utility bar in {colors.primary-active} (#013e5c) holds phone number, shipping threshold notice, and account links at {typography.caption}; below it the main nav at 60px in {colors.primary} (#014d73) carries the logo, category mega-menu links, search, and cart icon. All text reverses to {colors.on-primary}.

**`nav-dropdown`** — White card anchored below the main nav with a 3px {colors.primary} top accent line and a 16px soft drop shadow. Category columns organize Arms, Stands, Accessories, and Brands in a multi-column grid, with a featured product tile or promotional banner at the rightmost column.

### Search

**`search-bar`** — A 42px input field with {rounded.xs} border and a {colors.primary} submit button attached flush-right, forming a single unified control. Placeholder text in {colors.muted}. Appears both embedded in the nav bar at desktop and as a full-width element below the hero on the homepage.

### Spec Table

**`spec-table`** — Alternating-row table using {colors.surface-soft} every other row against white, with {typography.spec-label} (Lato Bold 13px) for attribute names — Load Capacity, Tilt Range, VESA Compatibility, Monitor Weight — and {typography.body-sm} for values. This component appears on every product detail page and is the primary conversion tool for buyers confirming fit with existing monitor hardware.

### Trust Strip

**`trust-strip`** — A horizontal row of 4–5 icon+label pairs (Free Shipping, Lifetime Support, Ergonomist-Curated, Easy Returns) rendered in {colors.surface-soft} with a 1px {colors.hairline} top border. Icons tint to {colors.primary}; labels in {typography.caption} at {colors.body}. Positioned below the hero section or above the footer depending on page type.

### Filter Chips

**`filter-chip`** — Pill-shaped ({rounded.full}) filter toggles for Brand, Weight Capacity, Monitor Size, and Finish on category pages. Inactive state uses white fill with {colors.hairline} border; active state flips to {colors.primary} fill with white text. Scrolls horizontally as a single row on tablet, wraps on desktop sidebar.

### Footer

**`footer`** — Dark canvas at {colors.ink} (#1a1a2e) with a 4px {colors.primary} top border as the single brand accent. Column headings in {typography.label} (uppercase, 12px, white); links in {typography.body-sm} at #c6c8ca. A bottom row holds legal links, copyright, and social icons at smaller weight. The deep navy floor echoes the brand primary without duplicating it.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; search moves to full-width row below logo bar; trust strip stacks to 2×2 grid; spec table switches to stacked label-above-value definition list |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories with a "More" overflow; mega-menu becomes a full-width drawer from the left; filter chips scroll horizontally in a single row |
| Desktop | 1128–1440px | Three-column product grid; full two-tier nav with mega-dropdown; left sidebar filter panel on category pages; spec table full horizontal with all columns visible |
| Wide | > 1440px | Four-column product grid; max-width 1440px container centered; hero banner fills viewport width with contained inner content block; trust strip icons space evenly across full width |

### Touch Targets

- All interactive buttons minimum 44px height on mobile
- Filter chips minimum 36px height with invisible 4px vertical padding to reach 44px tap zone
- Product card Add to Cart expands to full-width on mobile
- Nav hamburger icon minimum 44×44px tap zone
- Pagination controls minimum 44px height with 8px gap between items
- Badge-interactive variants (if filterable) minimum 32px height with horizontal padding to widen tap area

### Collapsing Strategy

- Mega-menu nav → hamburger side drawer; category nesting preserved inside accordion panels within the drawer
- Horizontal filter chips → "Filter & Sort" modal bottom sheet on mobile with Apply and Clear All actions
- Two-tier desktop nav → single-tier on mobile; utility bar (phone, shipping notice) collapses entirely; phone number promoted to footer
- Spec table → stacked definition list on mobile, label above value, full-width rows separated by {colors.hairline-soft}
- Trust strip → 2×2 grid on mobile, single horizontal row at tablet and above
- Footer multi-column grid → single-column accordion on mobile, each column heading toggling its link list

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color present; mobile browser chrome tint is not determinable from extraction
- No design tokens file or CSS custom properties extracted; spacing, radius, and shadow values are inferred from the ergonomics/B2B category norm and the extracted color palette rather than confirmed CSS variables
- Exact brand-set Lato weight scale (which specific numeric weights are used) not confirmed; 400 and 700 are inferred from category conventions
- Mega-menu column count, category hierarchy depth, and featured-tile placement not confirmed from extraction
- Logo dimensions, wordmark clear-space rules, and co-branding lockup guidelines not available
- #d63384 (magenta/pink) appears in extracted colors but its specific use context — promotional banner, brand partner accent, or framework artifact — was not confirmed
- Dark mode support status unknown; no prefers-color-scheme media query evidence detected in extraction
- Cart drawer vs. cart page pattern not determinable from extraction
- Whether Lato is self-hosted or loaded via Google Fonts not confirmed; font-display strategy unknown
