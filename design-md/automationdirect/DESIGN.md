---
version: alpha
name: "AutomationDirect"
source_url: "https://www.automationdirect.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Before e-commerce was normalized in heavy industry, AutomationDirect was shipping PLCs direct to engineers at prices that bypassed the distributor tier entirely — the site's design follows that same logic, stripping ornament to keep spec data, part numbers, and price breaks at zero distance from the buyer. The canvas holds at a clean #FFFFFF with a dense, catalog-native grid; the brand's primary medium blue (#0073AE) anchors the navigation bar and category headers, while a warm orange (#F47920) carries every primary CTA, add-to-cart button, and promotional callout. A deeper navy (#003E7E) caps the very top of every page in a thin announcement bar, creating a two-tone header system that reads as institutional rather than consumer. Typography runs on a tight Arial-based stack — no proprietary web font — which signals that the audience is plant-floor engineers and procurement managers who open ten tabs at a time and need data density over editorial polish. Product cards surface stock status, model numbers, and list-vs.-discounted prices without soft-touch imagery; a green in-stock badge (#2E7D32) is as close to a lifestyle accent as the product grid gets. Form factors lean utilitarian: inputs are rectangular (`{rounded.none}` to `{rounded.xs}`), button corners are minimal (`{rounded.xs}`), and the component language deliberately avoids pill shapes and soft radii that consumer brands use to signal approachability. Search is the site's primary navigation mechanism — a mega-search bar with category-scoped selectors at the top of every page reflects an audience that arrives knowing exactly what part number or product family they need. AutomationDirect's design is a direct consequence of its business model: remove the friction, surface the data, win on price — and trust that engineers can read a datasheet without needing a hero video to get there.

colors:
  primary: "#0073AE"
  primary-active: "#005A87"
  primary-disabled: "#7FBAD6"
  accent-orange: "#F47920"
  accent-orange-active: "#D4640D"
  accent-orange-disabled: "#F9BE90"
  header-navy: "#003E7E"
  footer-deep-navy: "#002A5C"
  ink: "#1A1A1A"
  body: "#333333"
  muted: "#666666"
  hairline: "#CCCCCC"
  hairline-soft: "#E5E5E5"
  canvas: "#FFFFFF"
  surface-soft: "#F5F5F5"
  surface-card: "#FFFFFF"
  surface-alt: "#EAF4FA"
  on-primary: "#FFFFFF"
  on-orange: "#FFFFFF"
  success: "#2E7D32"
  danger: "#C62828"
  warning: "#FF6F00"
  link: "#0073AE"
  link-visited: "#5B2D8E"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  part-number:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  price-display:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  table-header:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  table-body:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 3px
  sm: 4px
  md: 8px
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
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-orange}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.on-orange}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.accent-orange-disabled}"
    textColor: "{colors.on-orange}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    border: "1px solid {colors.primary}"
    height: 40px
  button-secondary-active:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  button-add-to-cart:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-orange}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 40px
    iconLeft: cart-icon
  nav-announcement-bar:
    backgroundColor: "{colors.header-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 32px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-category-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 36px
    borderTop: "1px solid rgba(255,255,255,0.2)"
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderTop: "2px solid {colors.accent-orange}"
    shadow: "0 4px 12px rgba(0,0,0,0.15)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
    padding: 0 12px
  search-category-select:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderRight: none
    height: 40px
  search-submit:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-orange}"
    rounded: "{rounded.xs}"
    height: 40px
    width: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 10px
    height: 36px
  text-input-focus:
    border: "1px solid {colors.primary}"
    outline: "2px solid rgba(0,115,174,0.25)"
  text-input-error:
    border: "1px solid {colors.danger}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm}"
    shadow: none
  product-card-part-number:
    typography: "{typography.part-number}"
    textColor: "{colors.muted}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-list-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  product-card-badge-in-stock:
    backgroundColor: "{colors.success}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  product-card-badge-low-stock:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  product-card-badge-new:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-orange}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.table-header}"
    cellTextColor: "{colors.body}"
    cellTypography: "{typography.table-body}"
    border: "1px solid {colors.hairline}"
    rowStripe: "{colors.surface-soft}"
  breadcrumb:
    textColor: "{colors.link}"
    typography: "{typography.body-sm}"
    separator: "/"
    separatorColor: "{colors.muted}"
    activeColor: "{colors.muted}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    hoverBorder: "1px solid {colors.primary}"
    hoverBackground: "{colors.surface-alt}"
  promo-banner:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent-orange}"
    typography: "{typography.body-md}"
    borderLeft: "4px solid {colors.accent-orange}"
    padding: "{spacing.md} {spacing.base}"
  compare-checkbox:
    accentColor: "{colors.primary}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  quantity-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 36px
    width: 64px
  pagination:
    textColor: "{colors.primary}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.header-navy}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-bottom-bar:
    backgroundColor: "{colors.footer-deep-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"

## Components

### Buttons

**`button-primary`** — The primary CTA in the AutomationDirect system is orange (#F47920), not the blue that anchors the navigation. This deliberate inversion — blue for structure, orange for action — creates an unmistakable hierarchy on dense product pages where both colors appear simultaneously. The active state darkens to #D4640D; the disabled state washes to a pale #F9BE90. Corner radius is minimal (`{rounded.xs}`, 3px) and height sits at 40px, sized for desktop-primary workflows rather than touchscreen-first ones.

**`button-secondary`** — A white-canvas button with a 1px primary-blue border and matching label text, used for secondary actions such as "Download Datasheet," "Request a Quote," or "View All." Hover and active states shift the background to the light blue tint (`{colors.surface-alt}`) while the border darkens to `{colors.primary-active}`. Same 3px radius keeps it visually consistent with the primary.

**`button-add-to-cart`** — Functionally identical to `button-primary` but carries a cart icon on the left and lives exclusively on product cards and product detail pages. The "ADD TO CART" label appears in uppercase bold, making it the most prominent single element on any catalog listing page.

**`button-ghost`** — A text-only blue link-button with no border or background, used for tertiary actions like pagination arrows, "Show More," and filter toggles. No border-radius is needed since there is no visible container.

### Search

**`search-bar`** — The dominant interface element on every page. A compound control: a category-scoped dropdown (`search-category-select`) flush-left with no right border, a wide text input occupying the center, and an orange submit button (`search-submit`) on the right. The entire assembly sits inside the blue nav bar and spans the majority of the available width. The category selector defaults to "All Products" and allows narrowing scope to PLCs, Drives, Sensors, Safety, and other major product families before submitting.

**`search-category-select`** — A native `<select>` element with a light-gray tinted background and no right border, forming a seamless left cap to the search input. Intentionally unstyled to match browser defaults, reflecting an audience that expects form controls to behave predictably. Height is fixed at 40px to align flush with the sibling input.

### Navigation

**`nav-announcement-bar`** — A 32px-tall band in deep navy (#003E7E) at the absolute top of every page. Carries short promotional lines ("Free 2-day shipping on orders over $49"), account links, and phone support references in caption-size white text. Does not collapse on scroll.

**`nav-bar`** — The primary 48px navigation bar in medium blue (#0073AE). Contains the AutomationDirect wordmark logo in white, the scoped search assembly at center, and right-rail icons for My Account, Saved Lists, and Cart with an item-count badge overlay. The search assembly consumes the majority of bar width, signaling search as the primary navigation mode.

**`nav-category-strip`** — A second 36px bar directly below `nav-bar` in the same primary blue, separated by a subtle semi-transparent white hairline. Holds the top-level product category tabs (PLCs, AC Drives, HMIs, Sensors, etc.) as horizontal text links. Hover triggers the mega-menu.

**`nav-mega-menu`** — A full-width white panel that drops below the category strip on hover. A 2px orange top border (`{colors.accent-orange}`) visually locks it to the triggering tab. The interior is a multi-column grid of subcategory links, each prefixed with a small product-family icon. A box shadow (`0 4px 12px rgba(0,0,0,0.15)`) lifts the panel above page content without obscuring it.

### Product Cards

**`product-card`** — The catalog grid card prioritizes data density over image display. A small product image floats left; the right column stacks the part number in monospace (`{typography.part-number}`), the product name in bold (`{typography.title-sm}`), a short description excerpt, a stock status badge, and a price block. On hover, a "Compare" checkbox appears in the card's top-left corner. The card border is a 1px hairline (`{colors.hairline}`); no shadow is used — the grid relies on whitespace to separate entries, not elevation.

**`product-card-badge-in-stock` / `product-card-badge-low-stock` / `product-card-badge-new`** — Uppercase 11px status badges anchored beneath the product name. Green (#2E7D32) for in-stock, amber (#FF6F00) for low-stock or backorder, and orange (#F47920) for newly introduced products. These badges are the most saturated elements in any catalog row and serve as the primary at-a-glance signal for procurement buyers scanning large result sets.

### Spec Table

**`spec-table`** — The central component of every Product Detail page. A full-width two-column table (attribute | value) with a light-gray header row (`{colors.surface-soft}`) and alternating row stripes on the same gray. Table headers are bold 13px; cell values are regular 13px. All borders are 1px hairline. Part numbers appearing within table cells render in monospace (`{typography.part-number}`) to distinguish them visually from prose values. The table is not paginated — all specs display inline, prioritizing completeness over brevity.

### Category Tiles

**`category-tile`** — Square tiles used on category landing pages and the homepage to navigate into product families. A small product-family icon appears above the category label text. Default background is light gray (`{colors.surface-soft}`); hover shifts the border to primary blue and background to the light blue tint (`{colors.surface-alt}`). Deployed in 3×3 or 4×4 grids depending on the product depth of the page.

### Promotional Banner

**`promo-banner`** — An inline content banner used to surface promotions, new product launches, or training webinar announcements within category or homepage content. A 4px left border in orange (`{colors.accent-orange}`) provides the accent signal; the background is the light blue tint (`{colors.surface-alt}`). This component is used inline and in-page, not as a fixed overlay or interstitial.

### Footer

**`footer`** — Full-width deep navy (#003E7E) footer organized into four link-group columns (Products, Support, Company, Connect). All links and text are white (`{colors.on-primary}`); hover affordance comes from underline, not color shift. Vertical padding is generous (`{spacing.xxl}`) to provide visual separation from the last content section. A narrower `footer-bottom-bar` in the darkest navy (#002A5C) holds copyright notice, legal links, and industry certifications at caption scale.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger menu replaces both nav bars; search collapses to icon that expands to full-width overlay; product grid shifts to single-column list view; spec table scrolls horizontally; announcement bar hides |
| Tablet | 744–1128px | Search bar narrows but remains visible; product grid is 2-column; mega-menu becomes an accordion slide-in drawer; category strip wraps or hides overflow behind a scroll indicator |
| Desktop | 1128–1440px | Full two-row nav with category strip; product grid 3–4 columns; spec table inline; full three-part search compound |
| Wide | > 1440px | Page content caps at ~1400px max-width; additional whitespace added to left/right gutters; product grid may expand to 5 columns on large catalog result pages |

### Touch Targets
- All buttons, links, and checkboxes maintain a minimum 36px tap target height on mobile breakpoints
- Quantity input expands to full-row layout on mobile for easier numeric entry with the numeric keypad
- Product card Compare checkbox hit area expands to 24×24px on touch breakpoints
- Mega-menu is replaced by a native accordion on touch — no hover dependency remains in the mobile nav

### Collapsing Strategy
- Left-rail category facet panel collapses into a slide-in drawer triggered by a "Filter" button above the product grid on mobile and tablet
- The three-part search compound (category select + text input + submit) collapses on mobile to a single full-width input with a fixed "All Products" scope; the category selector reappears inside the filter drawer
- Breadcrumb truncates middle segments with an ellipsis control below 744px, always preserving the first (Home) and last (current page) nodes
- Footer link columns stack vertically into collapsible accordion sections on mobile, collapsed by default

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site (anti-bot protection or JS-rendered design tokens) — all color values above are based on widely-observed brand patterns and carry elevated uncertainty; verify against computed CSS in DevTools before production use
- No font-family stacks were extracted — Arial/Helvetica assumption is based on the brand's B2B utilitarian positioning and visible rendering patterns; a licensed or custom typeface may be in use
- Exact nav bar heights, padding values, and search assembly dimensions are approximated from visual inspection of comparable industrial catalog sites — not confirmed from computed CSS
- AutomationDirect's quantity-break price table logic (tiered pricing at 1/5/10/50/100 unit thresholds) could not be fully mapped without live data extraction — a dedicated `price-tier-table` component would be needed
- Icon system (product-family icons in mega-menu and category tiles, UI icons in nav bar) is undocumented — may be a custom icon font, SVG sprite, or third-party icon library
- Specific hover/focus transition timing functions and durations are not documented — confirm via DevTools animation inspection
- Promotional and sale badge logic (clearance, limited time, refurbished) is not fully mapped; additional badge variants beyond in-stock/low-stock/new may exist
