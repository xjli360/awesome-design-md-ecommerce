---
version: alpha
name: "Fully (MillerKnoll)"
source_url: "https://www.fully.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Fully's product pages lead with a dimension table before any lifestyle photography — frame height range and weight capacity precede the well-lit loft scene because a standing-desk buyer needs to know if 22–48 inches clears their monitor arm before they need to imagine the space. This spec-forward hierarchy shapes the entire visual language: the site runs almost entirely on a near-black / canvas-white axis, with #252525 doing the heavy lifting as both ink and primary CTA so the interface reads as a tool rather than a mood board. Photography supplies all the warmth; the UI withholds it on purpose. Against that austerity, corner radii stay deliberately crisp — {rounded.xs} on badges and spec labels, {rounded.sm} on cards and input fields — nothing rolls into a pill. The MillerKnoll partnership adds a heritage layer: Herman Miller chair listings share the same product-card treatment as Fully's own desk line, requiring rigidly consistent component tokens across two product families. The configurator flow — frame finish → surface material → cable-management tier → accessories — demands a spec-table component where typographic weight hierarchy carries as much signal as color: {typography.title-md} for the attribute name, {typography.body-sm} for the value, {typography.caption} for the fine-print tolerance. Spacing follows a functional rather than editorial rhythm: {spacing.xl} for the product-card grid gap, {spacing.section} to separate category blocks, {spacing.lg} inside card padding. The nav sits at a fixed height with category anchors that collapse to a hamburger without drama. Body paragraphs in {typography.body-md} carry dense ergonomic-health content; caption type handles the dozens of dimensions that distinguish a $400 frame from a $900 one. The overall effect is a brand that competes on specification depth — direct about the fact that good workspace furniture is chosen with a tape measure and a budget spreadsheet, not a Pinterest board.

colors:
  primary: "#252525"
  primary-active: "#000000"
  primary-disabled: "#aaaaaa"
  ink: "#252525"
  body: "#3d3d3d"
  muted: "#6b6b6b"
  muted-soft: "#959595"
  hairline: "#e2e2e2"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-strong: "#ededed"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  spec-label: "#6b6b6b"
  spec-value: "#252525"
  badge-new: "#252525"
  badge-sale: "#c0392b"
  badge-text: "#ffffff"
  configurator-selected: "#252525"
  configurator-border: "#e2e2e2"

typography:
  display-xl:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-strong:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-lg:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.2px
  price-sm:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.05px
  badge:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.ink}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 54px
    width: 100%
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    paddingHorizontal: "{spacing.xl}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.10)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
    imageAspectRatio: "4/3"
    hoverBoxShadow: "0 4px 16px rgba(0,0,0,0.10)"
    gap: "{spacing.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-sm}"
    textColor: "{colors.badge-sale}"
  product-card-price-original:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 560px
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
    displayTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    layout: split-left-text-right-image
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  spec-table:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    rowPaddingVertical: "{spacing.sm}"
    rowPaddingHorizontal: "{spacing.base}"
    rowBorderBottom: "1px solid {colors.hairline-soft}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.spec-label}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.spec-value}"
    alternateRowBackground: "{colors.surface-soft}"
  configurator-swatch:
    size: 40px
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.configurator-border}"
    borderSelected: "2px solid {colors.configurator-selected}"
    gap: "{spacing.sm}"
  configurator-option-label:
    typography: "{typography.caption-strong}"
    textColor: "{colors.ink}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 260px
    borderRight: "1px solid {colors.hairline}"
    paddingVertical: "{spacing.lg}"
    paddingHorizontal: "{spacing.base}"
    sectionHeaderTypography: "{typography.title-sm}"
    optionTypography: "{typography.body-sm}"
    gap: "{spacing.md}"
  filter-checkbox:
    size: 18px
    rounded: "{rounded.xs}"
    borderUnchecked: "1.5px solid {colors.hairline}"
    backgroundChecked: "{colors.primary}"
    borderChecked: "1.5px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
    paddingHorizontal: "{spacing.base}"
    iconColor: "{colors.muted}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-strong}"
    paddingVertical: "{spacing.sm}"
    paddingHorizontal: "{spacing.base}"
    textAlign: center
    height: 40px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.xl}"
    columns: 4
    borderTop: none
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    height: 40px
    width: 40px

## Components

### Buttons

**`button-primary`** — Solid #252525 fill with white text, 48px tall, 8px radius, weight-600 label at 15px. The near-black CTA is consistent across the entire funnel — add-to-cart, configurator confirm, checkout — so no secondary color accent competes for attention. Hover deepens to `#000000`; disabled grays to `{colors.primary-disabled}` with `cursor: not-allowed`.

**`button-secondary`** — White fill with a 1.5px #252525 border, same radius and height as primary. Used for secondary actions like "Learn More" or "Compare" on PDP pages. Hover fills with `{colors.surface-soft}` to signal interactivity without color drama.

**`button-add-to-cart`** — A full-width variant of `button-primary` at 54px tall, used in the sticky PDP purchase bar and the product-card quick-add overlay. Slightly taller to meet touch-target comfort for a high-intent action.

**`button-text`** — No background or border; underlined link-style text at `{typography.button-sm}`. Reserved for low-priority actions like "View full specs" within a spec block or "Read assembly guide" in the footer content zone.

### Navigation

**`nav-bar`** — Fixed-top, 64px tall, white background with a 1px `{colors.hairline}` bottom border. Category links in `{typography.nav-link}` with dropdown panels (`nav-dropdown`) that open below on hover. Logo sits left; search, wishlist, and cart icons cluster right at 24px each with `{spacing.sm}` gaps. On scroll past the hero, a subtle box-shadow at 2px strengthens the separation.

**`nav-dropdown`** — White panel with `{rounded.sm}` corners, `0 8px 24px rgba(0,0,0,0.10)` shadow. Mega-menu layout for Desks and Chairs: left column lists subcategory links, right column surfaces up to 4 featured products as mini-cards with image, name, and starting price.

### Product Card

**`product-card`** — White background, 1px soft hairline border, 8px radius, 24px padding. Image occupies the top 4:3 slot; title in `{typography.title-sm}`, price in `{typography.price-sm}` below. Hover lifts to `0 4px 16px rgba(0,0,0,0.10)`. Badge overlays (New, Sale) anchor to the top-left of the image with `{spacing.sm}` inset. Sale price appears in `{colors.badge-sale}` with the original crossed out in `{colors.muted}`.

### Spec Table

**`spec-table`** — The spec table is a first-class component on every Fully PDP. It renders as a bordered table with 1px `{colors.hairline}` edges and alternating row backgrounds (`{colors.surface-soft}` on even rows). Attribute names appear in `{typography.spec-label}` at `{colors.spec-label}` (medium-gray); values in `{typography.body-sm}` at `{colors.spec-value}`. Row height is 40px minimum to accommodate two-line values (common for "Min Height / Max Height" cells).

### Configurator

**`configurator-swatch`** — 40px square swatches for finish selection (white oak, black, walnut, etc.), 4px radius, 1.5px gray border that becomes a 2px `{colors.primary}` border when selected. A checkmark icon overlays the selected swatch. Labels beneath use `{typography.caption-strong}`. The swatch row scrolls horizontally on mobile when option count exceeds 5.

### Filters

**`filter-sidebar`** — 260px fixed-width left sidebar on desktop. Section headers in `{typography.title-sm}`, options in `{typography.body-sm}`. Checkboxes (`filter-checkbox`) are 18px square with 4px radius; checked state fills `{colors.primary}` white checkmark. A sticky "Apply Filters" `button-primary` pins to the sidebar bottom on mobile filter drawer.

### Hero

**`hero-section`** — Split layout: text block on left occupies ~45% of width, product/lifestyle image fills the right 55%. `{colors.surface-soft}` background avoids competing with product imagery. Headline in `{typography.display-xl}`, subhead in `{typography.body-md}`, primary CTA button below. Minimum 560px tall on desktop; stacks to image-above-text on mobile.

### Promo Banner

**`promo-banner`** — Full-width 40px tall strip at the very top of the page in `{colors.primary}` / `{colors.on-primary}`, `{typography.caption-strong}`, centered text. Used for free-shipping thresholds, sale countdowns, and coupon codes. Dismissible with an X at right edge on desktop; persists on mobile.

### Search

**`search-bar`** — 44px tall, `{colors.surface-soft}` background, 1px hairline border, `{rounded.xs}` radius. Expands to full-width overlay on activation with results appearing as a dropdown panel matching `nav-dropdown` styling. Results group into Products, Categories, and Articles with small product thumbnails beside each product result.

### Footer

**`footer`** — Full-width `{colors.primary}` dark background, 4-column grid on desktop (Shop, Help, About, Social). Headings in `{typography.title-sm}` white, links in `{typography.body-sm}` white at 80% opacity, 1.4 line-height for dense link lists. Newsletter signup renders as a single `text-input` + inline `button-primary` pair. Legal row at the very bottom in `{typography.caption}` at `{colors.muted-soft}`.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + icon tray; filter-sidebar becomes bottom-sheet drawer; hero stacks image above text; spec-table scrolls horizontally; configurator swatches wrap to 2 rows |
| Tablet | 744–1128px | 2-column product grid; nav shows top-level links, hides subcategory dropdown; filter-sidebar collapses to horizontal filter chips above grid; hero uses condensed split layout at 70/30 |
| Desktop | 1128–1440px | 3-column product grid; full mega-menu nav-dropdown; 260px filter-sidebar visible; hero at full 45/55 split |
| Wide | > 1440px | Max-width container at 1440px centered with auto horizontal margins; product grid expands to 4 columns; hero image gains parallax treatment |

### Touch Targets

- All tappable controls (nav links, filter checkboxes, configurator swatches) maintain a minimum 44×44px touch target even when the visual element is smaller
- `button-add-to-cart` grows to 56px tall on mobile to reduce mis-tap rate on the high-intent action
- Spec-table rows are 48px tall on mobile to allow accurate row selection for comparison tools
- Configurator swatches expand to 48px on mobile, gap widens to `{spacing.md}`

### Collapsing Strategy

- Navigation collapses at 744px to a hamburger icon; secondary nav links (Help, Account) move into the hamburger panel
- Filter sidebar becomes a full-screen bottom-sheet modal triggered by a "Filter & Sort" button above the product grid
- 4-column footer becomes 2-column stacked at tablet, single-column accordion at mobile (each section header toggles its links)
- Mega-menu dropdowns are replaced by accordion expansion within the mobile nav panel
- Hero split layout stacks to vertical with image first, text block below, at mobile breakpoint

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Accent / brand color not extracted**: The site delivers color tokens via JavaScript (platform-shopify: False suggests a custom stack). Only #252525 was captured from static HTML. Fully's site historically uses a warm accent color for promotions and highlights — specific hex could not be confirmed and was not fabricated here.
- **Font families not extracted**: Zero font-family stacks were found in static CSS. The typography tokens above use an inferred clean sans-serif stack (Inter/DM Sans/system-ui) consistent with the workspace furniture category; actual font must be confirmed by inspecting the live site with JS enabled.
- **Primary CTA color ambiguity**: With only #252525 extracted, it is unclear whether CTAs are near-black or use an unextracted accent. The design above uses #252525 as primary; if a brand-accent color exists, it should replace `{colors.primary}` on buttons and the promo banner.
- **Herman Miller co-brand treatment**: The page title reads "Herman Miller Store" suggesting a co-branded or white-label experience. Logo lockup rules, co-brand typography variants, and any Herman Miller color overrides were not verifiable.
- **Configurator interaction states**: Active step indicators, progress bar colors, and error states within the multi-step desk configurator could not be extracted from static markup.
- **Dark mode support**: Unknown whether the site supports a dark-mode media query; no `prefers-color-scheme` tokens were extractable.
- **Icon library**: Custom icon set vs. licensed library (Phosphor, Heroicons, etc.) unknown; icon stroke weight and style not confirmed.
