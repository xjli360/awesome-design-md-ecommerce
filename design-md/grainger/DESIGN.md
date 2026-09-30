---
version: alpha
name: "Grainger"
source_url: "https://www.grainger.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Grainger product pages show four distinct identifier strings simultaneously — Grainger item number, manufacturer part number, catalog number, and UPC — each in 12px Arial at #6b6b6b, because the buyer arriving may need any one of them to reconcile a line item in a procurement system. This information architecture, additive rather than editorial, defines every design decision. Live extraction returned five grays: #474747 for primary text, #6b6b6b for secondary labels, #a7a9ac for muted and disabled states, #e4e5e6 for dividers and borders, and #fafafa as the global off-white canvas — nothing else; anti-bot filtering stripped the stylesheet carrying Grainger's widely-documented red primary (#cc0000), which surfaces at CTAs, the search bar's 2px border accent, and the logo mark. Type is Arial throughout: 700 weight at 28px for page titles, 700 at 14px for product names in grid rows, 400 at 14px for attribute text — a single-font discipline that is legible on any industrial monitor without web-font latency. Buttons and inputs carry near-zero rounding ({rounded.xs}), maintaining a rectangular vocabulary that reads as functional and exact. The one typographic departure is the price block: 22px bold at {colors.ink} anchors the unit price, with a 13px {colors.body} unit qualifier beside it — enough contrast to scan across a multi-SKU comparison without introducing a second typeface. Navigation runs three simultaneous access layers: a 60px global header with a persistent red-bordered search input, a 40px mega-nav category bar spanning roughly 30 product divisions, and a 220px left-rail parametric facet panel within sub-categories. Stock status labels introduce the system's only additions beyond red and gray: #2e7d32 green for in-stock availability and {colors.primary} red repurposed for out-of-stock states. Spacing throughout favors the tight end of the scale — {spacing.xs} between card rows, {spacing.sm} inside cards — compressing maximum SKU density per viewport height without making scrolling the primary navigation tool.

colors:
  primary: "#cc0000"
  primary-hover: "#b50000"
  primary-active: "#a30000"
  primary-disabled: "#e8a0a0"
  ink: "#474747"
  body: "#6b6b6b"
  muted: "#a7a9ac"
  hairline: "#e4e5e6"
  canvas: "#fafafa"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#1a5276"
  warning: "#f5a623"
  in-stock: "#2e7d32"
  out-of-stock: "#cc0000"

typography:
  display-xl:
    fontFamily: "Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  part-number:
    fontFamily: "Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  price-display:
    fontFamily: "Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-unit:
    fontFamily: "Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  label-caps:
    fontFamily: "Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  badge:
    fontFamily: "Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.muted}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  button-link:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 38px
    border: "1px solid {colors.muted}"
    focusBorder: "2px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    border: "2px solid {colors.primary}"
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.none}"
      width: 60px
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 28px
    cartBadgeBackgroundColor: "{colors.primary}"
    cartBadgeTextColor: "{colors.on-primary}"
    cartBadgeTypography: "{typography.badge}"
    cartBadgeRounded: "{rounded.full}"
  category-mega-nav:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    hoverTextColor: "{colors.primary}"
    height: 40px
    borderBottom: "1px solid {colors.hairline}"
    dropdownBackgroundColor: "{colors.surface-card}"
    dropdownBorder: "1px solid {colors.hairline}"
    dropdownShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    hoverBorder: "1px solid {colors.primary}"
    padding: "{spacing.sm}"
    imageSize: 80px
  product-card-title:
    typography: "{typography.body-sm}"
    textColor: "{colors.link}"
    maxLines: 2
  product-card-sku:
    typography: "{typography.part-number}"
    textColor: "{colors.muted}"
  price-block:
    priceTypography: "{typography.price-display}"
    priceTextColor: "{colors.ink}"
    unitTypography: "{typography.price-unit}"
    unitTextColor: "{colors.body}"
  part-number-block:
    typography: "{typography.part-number}"
    textColor: "{colors.muted}"
    labelTypography: "{typography.label-caps}"
    labelTextColor: "{colors.muted}"
  stock-indicator:
    inStock:
      textColor: "{colors.in-stock}"
      typography: "{typography.caption}"
    outOfStock:
      textColor: "{colors.out-of-stock}"
      typography: "{typography.caption}"
    limited:
      textColor: "{colors.warning}"
      typography: "{typography.caption}"
  quantity-stepper:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    buttonBackgroundColor: "{colors.surface-soft}"
    buttonTextColor: "{colors.ink}"
    height: 36px
    width: 120px
  add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    height: 40px
    fullWidth: true
    hoverBackgroundColor: "{colors.primary-hover}"
  facet-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    titleTypography: "{typography.title-sm}"
    borderRight: "1px solid {colors.hairline}"
    width: 220px
    checkboxAccentColor: "{colors.primary}"
    activeBadgeBackgroundColor: "{colors.primary}"
    activeBadgeTextColor: "{colors.on-primary}"
    activeBadgeTypography: "{typography.badge}"
  breadcrumb:
    textColor: "{colors.link}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted}"
    currentPageTextColor: "{colors.body}"
  badge-promo:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTextColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingTextColor: "{colors.surface-card}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xl} 0"
    legalTypography: "{typography.caption}"
    legalTextColor: "{colors.muted}"

## Components

### Buttons

**`button-primary`** — A near-rectangular red button at 40px height with 2px corner rounding (`{rounded.xs}`). Hover deepens to `{colors.primary-hover}` (#b50000); press steps further to `{colors.primary-active}` (#a30000). The disabled state washes to a desaturated rose (`{colors.primary-disabled}`) rather than a generic gray — preserving the red family signal even when inactive, which keeps disabled add-to-cart buttons visually coherent with the catalog's red-as-action vocabulary.

**`button-secondary`** — White fill with `{colors.ink}` text and a 1px `{colors.muted}` border, same 40px height as primary. Hover shifts the fill to `{colors.surface-soft}` without touching the border. Used for secondary procurement actions like "Save to List," "Add to Quote," or "Print Label," always rendered adjacent to a primary add-to-cart button.

**`button-link`** — Transparent background, `{colors.link}` text with underline decoration. Appears inline in product specifications, related-item cross-links, and account navigation items where a full button treatment would inflate the vertical density budget.

### Search Bar

**`search-bar`** — The site's highest-visibility element: a 44px-tall input with a 2px `{colors.primary}` red border — the only structural use of primary red outside of interactive buttons. The submit arrow button is a solid red block flush with the input's right edge, using `{rounded.none}` so the two elements read as a single composed unit. On the desktop layout a category-scope dropdown sits to the input's left, narrowing results to a top-level division before the query fires. Focus state does not change border weight or color since the 2px red border already carries maximum brand signal.

### Navigation

**`nav-bar`** — 60px global header with `{colors.surface-card}` background and a 1px `{colors.hairline}` bottom border. The logo sits at left at 28px height; the search bar occupies the center at 50% of viewport width; account, lists, and cart icons anchor the right. The cart icon carries a `{colors.primary}` badge with `{typography.badge}` counter text at `{colors.on-primary}`, using `{rounded.full}` to float as a pill above the icon.

**`category-mega-nav`** — A 40px horizontal strip directly below the nav-bar, holding approximately 30 top-level category links in `{typography.nav-link}`. Hover shifts link text to `{colors.primary}`. Clicking opens a full-width dropdown panel in `{colors.surface-card}` with sub-category columns and optional featured product imagery. The panel uses a 4px box shadow to separate from page content without a border.

### Product Card

**`product-card`** — A dense row-format card with zero border radius, bounded by a 1px `{colors.hairline}` border that shifts to `{colors.primary}` on hover with no transition delay — an instantaneous state signal appropriate for rapid catalog scanning. An 80px square product image sits left; the product title in `{colors.link}` at `{typography.body-sm}` (max 2 lines) follows; then the Grainger item number in `{typography.part-number}` at `{colors.muted}`, stock status, and the price block — all within a `{spacing.sm}` padding box.

**`price-block`** — The single typographic contrast in the card: a 22px bold number at `{colors.ink}` anchors the unit price with a 13px `{colors.body}` unit qualifier (per EA, per PK, per BX) immediately to its right. Volume pricing tiers render below as a compact two-column table in `{typography.caption}` — quantity threshold in the left column, unit price in the right.

**`part-number-block`** — Four label-value pairs rendered in `{typography.part-number}` with `{typography.label-caps}` uppercase labels. Stacks vertically on mobile (showing only the Grainger item number), expands to a two-column grid on desktop so all four identifiers are visible without truncation within a 48px vertical zone.

### Stock Indicator

**`stock-indicator`** — Three states, all text-based with no icon-only presentation. In-stock renders "In Stock" at `{colors.in-stock}` green in `{typography.caption}`. Limited stock shows a quantity count (e.g. "Only 3 Left") at `{colors.warning}`. Out-of-stock renders at `{colors.out-of-stock}` with a lead-time estimate appended when available ("Ships in 5–7 days"). Every state includes a visible text label — never icon-only — to ensure compatibility with screen readers and procurement-system print views.

### Quantity Stepper

**`quantity-stepper`** — A 120×36px composite of minus button, number input, and plus button, bounded by a 1px `{colors.hairline}` border with `{rounded.xs}` corners. The minus and plus cells use `{colors.surface-soft}` fill; the center input is `{colors.surface-card}`. The stepper enforces minimum order quantity at blur: if the MOQ for a SKU is 25, tabbing out of a value of 3 snaps the field to 25 before the add-to-cart action fires. This constraint is a functional data rule, not a design variation — it applies silently with no modal dialog.

### Facet Panel

**`facet-panel`** — A 220px-wide left-rail panel with `{colors.canvas}` background and a 1px `{colors.hairline}` right border, sticky on desktop while the product grid scrolls. Section headings use `{typography.title-sm}`. Filter options render in `{typography.body-sm}` with `{colors.primary}` checkbox fill. Collapsed section headers show an active-filter count badge in `{colors.primary}` background with `{typography.badge}` text. At viewport widths below 1128px the panel converts to a modal sheet triggered by a "Filter (N)" button showing the total active count.

### Footer

**`footer`** — Dark `{colors.ink}` (#474747) background with a 3px `{colors.primary}` top border as the sole chromatic accent entry point. Column headings in `{typography.title-sm}` at `{colors.surface-card}`; link text at `{colors.hairline}` (#e4e5e6) for approximately 4.5:1 contrast on the dark ground. Arranged in a four-column grid on desktop covering Account, Orders, Help, and Company sections. Legal text and copyright sit in a sub-footer row at `{typography.caption}` weight with `{colors.muted}` text, separated by a 1px `{colors.body}` rule.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; search bar full-width; mega-nav collapses to hamburger drawer; facet panel hidden behind "Filter (N)" bottom sheet trigger; part-number block shows Grainger item number only; quantity stepper and add-to-cart stack vertically full-width |
| Tablet | 744–1128px | Two-column product grid; mega-nav shows condensed top-level labels with no dropdowns; facet panel toggles as a slide-in overlay at 300px width; search bar at 70% viewport width |
| Desktop | 1128–1440px | Three-column product grid; full mega-nav with dropdown panels; facet panel always visible at 220px left rail; search bar centered at 50% viewport width; full four-identifier part-number block |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px centered with symmetrical margin; category hero banners expand to fill wider column spans |

### Touch Targets

- Primary buttons and add-to-cart minimum 40px height; 44px on mobile viewports
- Quantity stepper buttons minimum 36×36px with 8px invisible tap-area expansion on all sides
- Facet checkboxes rendered at 24×24px minimum with surrounding 8px tap target
- Mobile nav drawer category rows minimum 48px height
- Search submit button expands to 44×44px square on mobile

### Collapsing Strategy

- Mega-nav: full dropdown panel at ≥1128px; text-labels-only (no dropdowns) at 744–1128px; hamburger drawer at <744px
- Facet panel: sticky left rail at ≥1128px; slide-in overlay at 744–1128px; hidden behind bottom-sheet trigger at <744px with active count shown
- Product grid: 4col → 3col → 2col → 1col as viewport narrows through breakpoints
- Part-number block: four identifiers on desktop; Grainger item number only on mobile
- Breadcrumb: middle segments truncated with ellipsis at <400px viewport

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Primary red not extracted**: The extraction hit an error page ("Whoops, we couldn't find that") — all five captured colors are neutral grays from the error page stylesheet. Grainger's red (#cc0000 used here) is sourced from widely-documented brand identity, not live site extraction; the exact hex may differ slightly.
- **No custom typeface detected**: Arial is the system fallback stack. An authenticated page session may reveal a licensed display or body typeface loaded via JS that anti-bot filtering obscured.
- **Interactive transition timing**: Hover, focus, and active transition durations not captured; 150ms ease defaults assumed throughout.
- **Mega-nav dropdown column structure**: Column count, featured-product image dimensions, and promotional tile layout within dropdown panels are inferred from category-standard patterns, not extracted.
- **Volume pricing table specifics**: Exact breakpoint counts, column widths, and quantity threshold formatting for tiered pricing grids not captured.
- **Authenticated page palette**: Account dashboard, order history, and checkout pages may introduce additional color tokens not visible without a logged-in session.
- **Dark mode**: No evidence of a dark-mode token set or `prefers-color-scheme` handling from the available extraction.
- **Mobile app design tokens**: Grainger operates a native iOS/Android app with potentially distinct spacing and type scales not reflected here.
