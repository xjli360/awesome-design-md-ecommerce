---
version: alpha
name: "Electrolux"
source_url: "https://www.electrolux.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Sweden's largest appliance maker relies on a single confident mid-blue — approximately #1461a4 — to carry its entire premium signal across CTAs, navigation highlights, and section anchors; there is no secondary accent color, no warm copper or terracotta to soften the engineering tone. The effect is deliberately institutional: Electrolux has been building household appliances since 1919, and the UI signals that lineage through restraint rather than personality. Type runs in a clean humanist sans-serif at modest weights — headline displays sit around 32–40px at weight 600 rather than the heavy 800+ favored by DTC newcomers; the brand trusts large product photography and generous whitespace to carry the premium message. Backgrounds are almost exclusively white (#ffffff) and a very light cool gray (#f4f4f4) for alternating content bands, with near-black charcoal (#1a1a1a) for body text — the palette reduces to four or five genuine hues across the entire experience. Cards appear with shallow elevation and minimal radii ({rounded.sm}), keeping the industrial appliance context without feeling heavy; pill shapes are avoided entirely in favor of nearly-square button corners ({rounded.xs}) that read as precise and utilitarian. The grid is generous at desktop — typically four product columns collapsing to two on tablet and single-column on mobile — with consistent {spacing.section} rhythm between content zones. Energy-rating badges in EU label colors, specification comparison drawers, and filter-by-spin-speed chips form the signature components: this is a site where the user's first question is always "does it reach 1600 rpm?" and the layout architecture answers before the first scroll.

colors:
  primary: "#1461A4"
  primary-active: "#0D4A87"
  primary-disabled: "#9EC0DE"
  primary-light: "#E8F1F9"
  ink: "#1A1A1A"
  body: "#444444"
  muted: "#767676"
  hairline: "#E0E0E0"
  hairline-soft: "#F0F0F0"
  canvas: "#FFFFFF"
  surface-soft: "#F4F4F4"
  surface-card: "#FFFFFF"
  surface-dark: "#0D2340"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  energy-a-plus: "#009640"
  energy-f: "#ED1C24"
  error: "#D32F2F"
  success: "#1B8A3F"

typography:
  display-xl:
    fontFamily: "'Electrolux Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Electrolux Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Electrolux Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Electrolux Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Electrolux Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Electrolux Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Electrolux Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Electrolux Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  label-xs:
    fontFamily: "'Electrolux Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Electrolux Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Electrolux Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Electrolux Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  price-display:
    fontFamily: "'Electrolux Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  spec-value:
    fontFamily: "'Electrolux Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 11px 22px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 32px
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderTop: "3px solid {colors.primary}"
    shadow: "0 8px 24px rgba(0,0,0,0.10)"
    padding: "{spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    imageAspectRatio: "4/3"
    gap: "{spacing.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-xs}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 480px
    paddingX: "{spacing.xxl}"
    paddingY: "{spacing.section}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaSpacing: "{spacing.lg}"
  hero-banner-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 480px
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
  promo-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 40px
    paddingX: "{spacing.base}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.spec-value}"
    labelTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    rowEvenBackground: "{colors.surface-soft}"
    rowOddBackground: "{colors.canvas}"
    cellPadding: "12px 16px"
  energy-badge:
    rounded: "{rounded.none}"
    labelTypography: "{typography.label-xs}"
    ratingFontWeight: 700
    ratingFontSize: 20px
    colorAPlus: "{colors.energy-a-plus}"
    colorF: "{colors.energy-f}"
    width: 72px
  comparison-drawer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "2px solid {colors.primary}"
    padding: "{spacing.lg}"
    maxColumns: 3
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
    height: 36px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
    padding: 6px 14px
    height: 36px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted}"
    gap: "{spacing.xs}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    height: 44px
    padding: 0 16px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "#9EC0DE"
    typography: "{typography.body-sm}"
    legalTypography: "{typography.caption}"
    padding: "{spacing.xxl} 0"
  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveTextColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    height: 36px
    width: 36px

## Components

### Buttons
**`button-primary`** — Solid {colors.primary} (#1461a4) fill with white label rendered in {typography.button-md}, 48px tall with {rounded.xs} (2px) corners that signal precision over friendliness. Hover and active states step down to {colors.primary-active} (#0d4a87); disabled state washes out to {colors.primary-disabled} with `cursor: not-allowed`. Used for all primary conversion actions: "Add to Cart", "Shop Now", "Get a Quote".

**`button-secondary`** — White fill with a 2px {colors.primary} border and blue label in {typography.button-md}. On hover, the fill shifts to {colors.primary-light} and the border deepens to {colors.primary-active}. Appears alongside primary CTAs on product cards and at the top of comparison surfaces.

**`button-ghost`** — Transparent with a 1px {colors.hairline} border and {colors.primary} label. Reserved for lower-hierarchy actions like "Learn More" or filter resets; sits without visual competition on {colors.surface-soft} section backgrounds.

### Product Card
**`product-card`** — White {colors.surface-card} tile with a 1px {colors.hairline} border and {rounded.sm} corners. A 4:3 product image occupies the top half; below it sits the model name in {typography.title-sm}, a key spec line (capacity, energy class) in {typography.body-sm} at {colors.muted}, then price in {typography.price-display}, and a full-width `button-primary` at the base. The optional `product-card-badge` — zero-radius, {colors.primary} fill — pins to the image's top-left corner for "Best Seller" or promotional overlays, using {typography.label-xs} uppercase.

### Nav Bar
**`nav-bar`** — White 72px header with the Electrolux wordmark logo left-aligned, mega-menu category links centered, and utility icons (search, account, cart) right-aligned. A 1px {colors.hairline} bottom border separates it from page content. On dark hero sections the `nav-bar-dark` variant swaps to {colors.surface-dark} background with {colors.on-dark} labels. The `mega-menu` drops on hover with a 3px {colors.primary} top accent border, {spacing.xxl} internal padding, and a soft box shadow; it houses sub-category links in {typography.body-md} with small product image thumbnails.

### Hero Banner
**`hero-banner`** — Full-width section on {colors.surface-soft} background at a minimum 480px height. Headline in {typography.display-xl} sits left-aligned with a {typography.body-md} subheadline below it; one or two CTAs follow at {spacing.lg} gap. The `hero-banner-dark` variant — used for product launches and seasonal campaigns — replaces the background with {colors.surface-dark} and all copy shifts to {colors.on-dark}. Product imagery always bleeds to the right edge at desktop.

### Spec Table
**`spec-table`** — Two-column key/value grid for technical specifications. Labels in {typography.body-sm} at {colors.body}; values in {typography.spec-value} medium weight. Rows alternate between {colors.canvas} and {colors.surface-soft} for scannability. The table has no outer border — it floats cleanly on white backgrounds. Used in product detail pages and inside the `comparison-drawer`.

### Energy Badge
**`energy-badge`** — EU-format energy label at 72px wide with {rounded.none} corners. The rating letter renders at 20px weight-700 inside a color block that maps A+ through the scale from {colors.energy-a-plus} green (#009640) toward {colors.energy-f} red (#ed1c24). Scale labels use {typography.label-xs} uppercase. Appears on product cards and at the top of each product detail page — one of the clearest signature UI elements for the appliance category.

### Comparison Drawer
**`comparison-drawer`** — Fixed bottom tray that slides up when the user checks two or more products. {colors.surface-soft} background with a 2px {colors.primary} top accent stripe. Holds up to three product columns, each with thumbnail, name, key spec snippet, price in {typography.price-display}, and a "Remove" ghost link. A persistent "Compare Now" CTA uses the full `button-primary` style.

### Filter Chips
**`filter-chip`** and **`filter-chip-active`** — {rounded.full} pill-shaped selectors for faceted filtering (Capacity, Spin Speed, Energy Rating, Colour). Inactive: white fill, {colors.hairline} border, {colors.body} label. Active: {colors.primary} fill, white label. Both variants are 36px tall in {typography.button-sm}. A horizontal scroll container holds the chip row on mobile without wrapping.

### Promo Strip
**`promo-strip`** — Full-width 40px announcement bar in {colors.primary} with centered {typography.body-sm} white copy. Positioned above `nav-bar` for sitewide messaging: seasonal sale deadlines, free delivery thresholds, or sustainability certifications. Dismissible on mobile with an `×` icon.

### Search Bar
**`search-bar`** — 44px inline input with {rounded.xs} corners, {colors.hairline} default border, and a magnifier icon right-aligned inside the field. On focus, border upgrades to 2px {colors.primary}. Appears in the mega-menu panel and as a standalone header on the search results page with results pre-populating below at 200ms debounce.

### Footer
**`footer`** — {colors.surface-dark} base with {colors.on-dark} copy and a lightened blue (#9ec0de) for hyperlinks, maintaining contrast against the dark field. Four-column layout (Products, Support, Company, Social) with {typography.body-sm} links; legal copy and certifications in {typography.caption}. Country/region selector and social icons anchor the bottom row.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero stacks (image above, text below); comparison drawer reduces to a floating chip showing selected count; spec table scrolls horizontally; filter chips in horizontal scroll row |
| Tablet | 744–1128px | Two-column product grid; hero goes side-by-side at reduced min-height (360px); nav shows text links but no mega-menu hover panel; comparison drawer shows two columns |
| Desktop | 1128–1440px | Four-column product grid; full mega-menu on hover; hero at 480px min-height; comparison drawer full three-column layout |
| Wide | > 1440px | Content max-width ~1400px centered with auto side margins; product grid stays four columns; hero image can extend full bleed behind a capped text container |

### Touch Targets
- All primary and secondary CTAs minimum 48×48px
- Filter chips minimum 36px tall, 80px minimum width for comfortable tap
- Nav utility icons (search, cart, account) padded to 44×44px tap area on mobile
- Product card entire tile surface is tappable, not just the title link
- Pagination controls minimum 36×36px with 8px gap between items

### Collapsing Strategy
- Four-column product grid → two-column (tablet) → single-column (mobile) via CSS grid `repeat(auto-fill, minmax(280px, 1fr))`
- Mega-menu hover panel → accordion disclosure inside a full-screen mobile drawer, opened by hamburger
- Spec table → horizontal scroll container on viewports below 744px, with sticky first column for label
- Comparison drawer → collapses to a fixed bottom chip on mobile showing product count with a "View" tap to expand full drawer
- Footer four-column layout → stacked single-column with each section in a disclosure accordion on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site (likely loaded via JavaScript bundle or behind anti-bot protection); all palette values are inferred from widely documented Electrolux brand identity guidelines and may not match the current site exactly
- No font-family stacks were detected; "Electrolux Sans" is referenced from brand presentation materials but the exact web font serving method, weight range, and WOFF2 filenames are unconfirmed
- Button corner radius is inferred as {rounded.xs} (2px) from product photography and brand presentation style; actual computed value may be 0px or 4px
- Full EU energy label color scale (A through G, seven steps) is not defined — only A+ green and F red are included; intermediate rating colors (B through E) require additional specification
- Dark-mode or high-contrast accessibility variant is not documented
- Exact box-shadow / elevation token values for product cards and mega-menu drop panels were not extractable
- Mobile navigation gesture behavior (swipe-to-close drawer, scroll-lock behavior) is not confirmed
- Regional variants (North America vs. Europe) may differ significantly in layout and color application; this spec targets the global/European presentation
