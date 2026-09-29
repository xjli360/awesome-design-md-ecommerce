---
version: alpha
name: "Salazar Packaging"
source_url: "https://www.salazarpackaging.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Corrugated crimson meets fulfillment logic at Salazar Packaging — the primary red (#c0372f) reads like a hazmat-border stripe or a shipping-label dash, and the site pairs it against deep navy (#003388) with the decisiveness of a warehouse floor plan rather than a retail mood board. Poppins absorbs the weight of category headers and product names; Open Sans handles the dense specification copy — unit counts, sheet calipers, weight limits, pallet minimums — at 14–16px without inducing fatigue across long comparison sessions. Amber (#ffbb00) surfaces only at bulk-discount callouts and promotional badges, a flash of procurement urgency against an otherwise gray-white canvas. The bright link blue (#2ea3f2) carves a navigation lane distinct from the red CTA lane, so scan paths through product listings remain unambiguous when multiple affordances stack in a single row. Button shapes hold 6px corners (`{rounded.sm}`) — not the pill softness of a consumer brand, but enough curvature to signal a digital interface rather than a printed form. Surface layering is spare: near-white (#f5f5f5) canvas under card-gray (#eeeeee) tiles creates enough depth that product photography — corrugated kraft, clear polybag, white foam — reads without competition. Courier New appears for SKU labels and quantity values, a typographic register borrowed from actual packing slips and inventory systems that the site's procurement audience already knows how to scan. Trust signals arrive as an icon-paired navy band immediately below the hero, amber-tinted icons marking shipping thresholds, bulk-savings tiers, recyclability claims, and live support. The overall palette — red and navy with amber accents and neutral grays — positions Salazar as a no-nonsense fulfillment partner whose catalog site is as legible and efficient as the boxes it ships.

colors:
  primary: "#c0372f"
  primary-active: "#9f2c26"
  primary-disabled: "#f78da7"
  secondary: "#003388"
  secondary-active: "#26323d"
  accent: "#ffbb00"
  accent-soft: "#fdf497"
  link: "#2ea3f2"
  link-active: "#0693e3"
  danger: "#cf2e2e"
  warning: "#ff6900"
  ink: "#222222"
  body: "#555555"
  muted: "#848484"
  muted-soft: "#a7a7a7"
  hairline: "#d9d9d9"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#eeeeee"
  surface-mid: "#ededed"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"
  on-accent: "#222222"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Poppins', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Poppins', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-mono:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Poppins', 'Open Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', 'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Poppins', 'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Poppins', 'Open Sans', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0

rounded:
  none: 0px
  xs: 3px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 44px
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.secondary}"
    border: "2px solid {colors.secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "10px 22px"
    height: 44px
    hoverBackgroundColor: "{colors.secondary}"
    hoverTextColor: "{colors.on-secondary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 44px
    placeholderColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    height: 48px
    inputTypography: "{typography.body-md}"
    inputColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitTypography: "{typography.button-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 68px
    borderBottom: "1px solid {colors.hairline}"
    topBarBackgroundColor: "{colors.secondary}"
    topBarTextColor: "{colors.on-secondary}"
    topBarTypography: "{typography.caption}"
    topBarHeight: 36px
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    skuTypography: "{typography.label-mono}"
    skuColor: "{colors.muted}"
    hoverBorder: "1px solid {colors.primary}"
    hoverShadow: "0 4px 12px rgba(0,0,0,0.08)"
  hero-banner:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.hairline-soft}"
    accentBarColor: "{colors.primary}"
    accentBarHeight: 4px
    minHeight: 480px
    paddingVertical: "{spacing.section}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.title-sm}"
    labelColor: "{colors.ink}"
    hoverBackgroundColor: "{colors.primary}"
    hoverLabelColor: "{colors.on-primary}"
    hoverBorder: "1px solid {colors.primary}"
  trust-strip:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.accent}"
    paddingVertical: "{spacing.lg}"
    gap: "{spacing.xl}"
  bulk-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  promo-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  sale-badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  filter-tag:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.on-primary}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 14px"
  sku-chip:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.muted}"
    typography: "{typography.label-mono}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.accent}"
    borderTop: "3px solid {colors.primary}"
    paddingTop: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Flat red (#c0372f) rectangle with 6px corners (`{rounded.sm}`), 44px tall, Poppins semi-bold 15px. Hover deepens to #9f2c26 with no transition delay — the response is immediate, matching the no-frills procurement tone. Disabled state uses a muted pinkish fill (#f78da7) to preserve shape recognition without implying interactivity. This is the sole "add to cart" and "request quote" button across the catalog.

**`button-secondary`** — White fill with a 2px navy border (#003388) and matching navy text, same height as primary. Hover inverts the fill to solid navy with white text, a clean two-state swap that establishes the secondary tier without a third color entering the palette. Pairs with primary on product pages for "Get a Custom Quote" alongside "Add to Cart."

**`button-ghost`** — Transparent background, link-blue text (#2ea3f2), no border. Used inline within spec tables, info callout panels, and "See all" prompts where a full button would overpower surrounding copy. Hover underlines the label.

**`button-accent`** — Amber fill (#ffbb00) with dark ink text (#222222), reserved for bulk-discount CTAs ("Save 20% on 500+") and promotional hero overlays. The amber commands attention against navy backgrounds without carrying the urgency of red.

### Text Input / Search

**`text-input`** — White canvas, 1px hairline border (#d9d9d9), 6px radius, 44px tall. Focus state swaps to a 2px red border, anchoring the user's eye during form entry. Open Sans 16px keeps the input register visually level with the body copy throughout the catalog.

**`search-bar`** — Wider than a standard input and bounded by a 2px red border at rest, signaling primary nav function from the moment the page loads. The right-inset submit button fills red with white Poppins text, forming a single compound unit. Deployed in the top nav and repeated at the top of every category landing page.

### Navigation

**`nav-bar`** — Two-tier structure: a 36px navy top bar carrying utility links (account, phone number, order tracking) in small Open Sans caption type, and a 68px white main bar with Poppins semi-bold category links. The navy top bar visually anchors the stack and separates procurement utilities from product browsing. Logo sits left; the red-bordered search bar occupies center; cart and account icons cluster right.

**`breadcrumb`** — Open Sans 12px in muted gray (#848484), slash-separated. The active terminal segment shifts to ink (#222222). Positioned flush below the nav on category and product pages; never truncated — full category paths matter for procurement navigation.

### Product Card

**`product-card`** — White card, 1px hairline border, 6px radius, 16px padding. Product name in Poppins 15px semi-bold ink; price in Poppins 22px bold red (#c0372f); spec copy in Open Sans 14px body gray. The SKU appears below the spec block in Courier New 13px muted gray, referencing the packing-slip convention the procurement audience already reads. On hover, the border activates to red and a soft shadow lifts the card off the grid. Bulk-tier badges stack in the top-right corner using amber or red chips.

### Hero Banner

**`hero-banner`** — Full-width navy (#003388) panel with a 4px red accent bar across the top edge. Display-xl Poppins (40px, 700) headline in white; sub-head in hairline-soft gray (#eeeeee) to reduce visual competition with the headline. A primary red button anchors the left column copy block. Minimum 480px height to allow product photography or illustrated catalog imagery to breathe on the right half. Section-scale vertical padding (64px) ensures nothing feels cramped at large viewport widths.

### Category Tiles

**`category-tile`** — Near-white (#f5f5f5) cards in a 4- or 6-column grid, hairline border, 6px radius. On hover the full tile fills red and the label inverts to white — a decisive interaction that avoids ambiguity in a dense catalog grid. A product-category icon or small thumbnail sits above the label; no description copy keeps tiles compact and scan-friendly.

### Badges

**`bulk-badge`** — Amber (#ffbb00) fill, dark ink text, uppercase 11px Open Sans, 3px radius. Signals multi-unit pricing tiers on product cards and listing rows.

**`promo-badge`** — Red (#c0372f) fill, white text, same scale. Marks featured or regionally promoted SKUs.

**`sale-badge`** — Danger red (#cf2e2e) fill, white text. Used for clearance or end-of-line pricing to visually distinguish from routine promotional treatment.

### Trust Strip

**`trust-strip`** — Full-width navy band immediately below the hero, carrying 4–5 icon+text pairs: free shipping threshold, bulk-discount tiers, recyclable materials claim, fast restock, live support. Icons render in amber (#ffbb00) against navy. Open Sans 14px. 32px horizontal gap between pairs. On mobile collapses to a 2×2 + 1 stacked grid.

### SKU Chip

**`sku-chip`** — Courier New monospace label on a mid-surface (#ededed) background with 3px radius, used inline in product spec tables, cart line items, and order confirmation rows. Provides visual continuity with physical packing slips and warehouse pick-list printouts.

### Filter Tags

**`filter-tag`** — Used in facet sidebars and category filter rows. Default: near-white fill, hairline border, Open Sans 14px. Active state fills red with white text. Open Sans (not Poppins) keeps filter rows light and scannable when a dozen active-filter chips stack in a row.

### Footer

**`footer`** — Near-black (#222222) background with a 3px red top border. Four-column layout on desktop: Products, Company, Resources, Contact. Section headings in Poppins 15px semi-bold white; links in Open Sans 14px muted gray (#a7a7a7), shifting to amber (#ffbb00) on hover. Newsletter signup row uses a standard text-input with an inline primary button. 48px top padding creates breathing room beneath the content grid above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top nav collapses to hamburger + logo + cart icon; utility top bar hides; trust strip reflows to 2×3 stacked icon grid; hero height reduces to 320px; display-xl headline downsizes to 26px; filter panel slides in as a left drawer |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level category links inline, secondary links collapse; hero image stacks below copy block; category tiles shift to 3-column grid; trust strip stays horizontal at 3 items |
| Desktop | 1128–1440px | Three- or four-column product grid; full two-tier nav bar visible; hero two-column split; category tiles 4- or 6-column; filter sidebar pinned left of product grid |
| Wide | > 1440px | Content max-width 1280px centered with increased side margins; product grid stays at four columns; hero gains extra horizontal padding; footer columns gain breathing room |

### Touch Targets

- Primary and secondary buttons maintain 44px minimum height on all touch viewports
- Filter tags expand to 40px tap height on mobile
- Nav hamburger and cart icon are each 44×44px tap targets
- Product card tap area covers the full card surface, including the image region above the title
- Category tiles maintain a 48px minimum height for label tap zone on mobile

### Collapsing Strategy

- The two-tier nav merges to a single row on tablet; the navy utility top bar hides, with account and phone links moving into the hamburger drawer
- Category tile hover fills are replaced by tap-activated states on touch devices to eliminate hover-flicker on iOS
- The filter sidebar becomes a full-height slide-in drawer at tablet and below, triggered by a "Filters" button above the product grid count
- SKU chips and breadcrumbs remain visible at all breakpoints — spec legibility is a procurement priority, not a cosmetic choice
- Bulk-badge and promo-badge chips remain on product cards at all breakpoints; sale-badge is the only badge that collapses to an icon-only pill below 375px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No web font file URLs confirmed; Poppins and Open Sans inferred from `font-family` stacks — weights and optical sizes beyond 400/600/700 not verified from the live site
- Many colors in the extracted list (#f78da7, #9b51e0, #7bdcb5, #00d084, #8ed1fc) appear to originate from the Divi WordPress block-editor color palette rather than the brand identity and were excluded from the design system
- ETmodules (Divi icon font) and FontAwesome confirmed as icon fonts; specific glyph sets, style (line vs. filled), and icon sizing not extractable from CSS alone
- No confirmed border-radius values from live site; `{rounded.sm}` (6px) inferred from typical Divi theme defaults
- `primary-disabled` (#f78da7) sourced from the Divi palette; may not be the site's actual disabled-state color — verify against interactive form elements
- Logo mark colors, SVG assets, and any gradient usage not extractable from the page scan
- Dark-mode or high-contrast variant not detected; design system assumes light-only
- Meta theme-color absent — no confirmed mobile browser status-bar color intent
- Exact grid column counts for category tiles and product listings not verified; values inferred from industry convention for catalog-style DTC sites
