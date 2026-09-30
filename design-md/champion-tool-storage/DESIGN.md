---
version: alpha
name: "Champion Tool Storage"
source_url: "https://www.championbuilt.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The first thing that registers on championbuilt.com is the hard contrast of #006fcf — a broad-shouldered, mid-spectrum industrial blue — pushing out of a near-black (#121212) field. This is not the cool tech-company cobalt or the navy of workwear heritage; it's the blue of powder-coated steel cabinets under a shop's fluorescent bar, confident and utilitarian. Champion Tool Storage sells workbenches and tool chests to tradespeople and garage builders who evaluate products by load ratings and drawer slide quality before aesthetics, and the visual language responds accordingly: dark backgrounds carry authority, the blue drives every action state and callout badge, and light gray (#dedede) handles structural dividers and secondary labels without softening the overall tenor. The site's meta theme-color is pure black, reinforcing a dark-first intent that places the brand closer to motorsport equipment than to home-improvement retail. Because no custom font stack was extractable from the live page — tokens appear to be injected via JavaScript — the typography system below defaults to a robust system sans-serif that preserves the brand's industrial register: compact letter-spacing on headings, weight-600 for labels and CTAs, weight-400 for body copy with no romantic flourishes. Buttons are squared to a low-radius geometry (`{rounded.xs}` or `{rounded.sm}`), echoing the rectilinear silhouette of steel cabinetry. Product cards operate on a dark surface rather than white, with the blue appearing as a hover state accent and badge fill. The overall interaction grammar is direct: one primary CTA per viewport section, minimal animation, and information density calibrated for buyers who already know what a 52-inch tool chest is and just need the specs.

colors:
  primary: "#006fcf"
  primary-active: "#0058a3"
  primary-disabled: "#80b7e7"
  primary-hover: "#0062b8"
  ink: "#121212"
  ink-on-dark: "#ffffff"
  body: "#2a2a2a"
  body-on-dark: "#e0e0e0"
  muted: "#666666"
  muted-on-dark: "#9e9e9e"
  hairline: "#dedede"
  hairline-dark: "#2e2e2e"
  canvas: "#ffffff"
  canvas-dark: "#000000"
  surface-soft: "#f5f5f5"
  surface-card: "#1a1a1a"
  surface-raised: "#222222"
  on-primary: "#ffffff"
  badge-promo: "#006fcf"
  badge-sale: "#c8001d"
  star-fill: "#f4a81d"

typography:
  display-xl:
    fontFamily: "'Arial Black', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Arial Black', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Arial Black', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  label-caps:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.4px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.2px
  spec-value:
    fontFamily: "'Arial Black', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 900
    lineHeight: 1
    letterSpacing: -0.3px
  spec-label:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.5px
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
    backgroundColor: "transparent"
    textColor: "{colors.ink-on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink-on-dark}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    fontSize: "{typography.body-md}"
  text-input-focus:
    borderColor: "{colors.primary}"
    outlineColor: "{colors.primary}"
    outlineWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.ink-on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "2px solid {colors.primary}"
    logoHeight: 36px
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink-on-dark}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink-on-dark}"
    rounded: "{rounded.xs}"
    imageBg: "{colors.surface-raised}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    padding: "{spacing.md}"
    border: "1px solid {colors.hairline-dark}"
  product-card-hover:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 1px {colors.primary}"
  badge-promo:
    backgroundColor: "{colors.badge-promo}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.ink-on-dark}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 560px
    paddingY: "{spacing.xxl}"
    accentColor: "{colors.primary}"
  spec-grid:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline-dark}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    labelColor: "{colors.muted-on-dark}"
    valueColor: "{colors.ink-on-dark}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    gap: "{spacing.xl}"
  breadcrumb:
    textColor: "{colors.muted-on-dark}"
    separatorColor: "{colors.hairline-dark}"
    activeColor: "{colors.ink-on-dark}"
    typography: "{typography.caption}"
  search-bar:
    backgroundColor: "{colors.surface-raised}"
    inputTextColor: "{colors.ink-on-dark}"
    placeholderColor: "{colors.muted-on-dark}"
    iconColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    height: 44px
    border: "1px solid {colors.hairline-dark}"
  star-rating:
    fillColor: "{colors.star-fill}"
    emptyColor: "{colors.hairline-dark}"
    typography: "{typography.caption}"
    reviewCountColor: "{colors.muted-on-dark}"
  compare-bar:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.ink-on-dark}"
    accentColor: "{colors.primary}"
    borderTop: "3px solid {colors.primary}"
    height: 72px
    typography: "{typography.button-sm}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    padding: "10px {spacing.base}"
    textAlign: center
  footer:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.muted-on-dark}"
    linkColor: "{colors.hairline}"
    headingColor: "{colors.ink-on-dark}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    paddingY: "{spacing.section}"

## Components

### Buttons
**`button-primary`** — Solid #006fcf fill on a `{rounded.xs}` (4px) container, 48px tall with uppercase 15px weight-700 text at 0.4px tracking — the squareness underscores that this is shop equipment, not software. Hover darkens to `{colors.primary-hover}` (#0062b8); active state pushes to `{colors.primary-active}` (#0058a3). Disabled renders at `{colors.primary-disabled}` and drops pointer events; no opacity hack.

**`button-secondary`** — Transparent fill with a 2px `{colors.hairline}` border, same height and typography as primary. On hover the border swaps to `{colors.primary}` and the background lifts to `{colors.surface-raised}`, keeping the industrial register without filling with color.

**`button-ghost`** — Blue text and 1px blue border, 40px height, used for secondary actions on product detail pages (e.g. "Compare", "Add to Wishlist") where visual hierarchy must stay below the main Add to Cart CTA.

### Navigation
**`nav-bar`** — Black (#000000) background, 64px tall, with a 2px #006fcf underline as the sole decorative element. Logo sits left, category mega-menus expand on hover with `{nav-dropdown}` panels floated below. The blue rule grounds the nav without color-flooding the chrome. Cart icon and account link sit right-aligned in icon form only.

**`nav-dropdown`** — Dark `{colors.surface-card}` panels with a 3px #006fcf top accent, no border radius, organized in a 3–4 column grid of category links. Category heads use `{typography.title-sm}`, links use `{typography.body-sm}` in `{colors.body-on-dark}`.

### Product Cards
**`product-card`** — Dark `{colors.surface-card}` (#1a1a1a) tile with a 1px `{colors.hairline-dark}` border and 4px radius. Product image renders on a slightly lighter `{colors.surface-raised}` background swatch. Title in `{typography.title-sm}`, price in `{typography.title-md}` white. Hover state adds a full 1px #006fcf outline via `box-shadow` to avoid layout shift. `badge-promo` and `badge-sale` chips overlap the image corner — square corners, bold caps, no radius.

### Hero Section
**`hero-section`** — Full-bleed black canvas, minimum 560px tall. Display headline in `{typography.display-xl}` (Arial Black, 40px, weight 900) anchors left or centered depending on layout variant. The primary CTA is always `button-primary`. A secondary blue rule or tinted overlay band frequently frames the subheadline. Product photography renders on dark backgrounds, often with a subtle bottom-gradient fade to canvas.

### Spec Grid
**`spec-grid`** — A dark tile grid used on product pages to present load capacity, drawer count, cabinet dimensions, and finish options. Labels in 10px uppercase `{typography.spec-label}` in `{colors.muted-on-dark}`; values in `{typography.spec-value}` (Arial Black 24px) in white. Cells sit on `{colors.surface-card}` with `{colors.hairline-dark}` dividers. This component is the product detail page's signature element — stats-heavy, no softening prose between numbers.

### Badges
**`badge-promo`** — Blue (#006fcf) chip, uppercase 11px weight-700, 0 radius, 4×8px padding. Used for "New", "Bestseller", "Limited Stock". **`badge-sale`** — Red (#c8001d) variant for discount pricing callouts. Both float over the product image top-left corner.

### Promo Banner
**`promo-banner`** — Full-width #006fcf bar at the very top of the page, above the nav. 10px uppercase label-caps text in white. Carries free-shipping thresholds, seasonal offers, or build promotions. No radius, edge-to-edge.

### Search
**`search-bar`** — Dark `{colors.surface-raised}` fill, 44px tall, `{rounded.xs}`. Magnifying-glass icon in #006fcf sits right-aligned inside the input. Focus state adds a 1px #006fcf border. On mobile it expands to full width in a drawer overlay.

### Star Rating
**`star-rating`** — #f4a81d fill stars against `{colors.hairline-dark}` empty stars. Review count in `{typography.caption}` `{colors.muted-on-dark}` beside the star cluster. Sits directly below the product title on both card and PDP.

### Compare Bar
**`compare-bar`** — Sticky bar that surfaces at the bottom of the viewport when 2+ products are checked for comparison. Black background, 3px #006fcf top border, 72px tall. Product thumbnails sit left; "Compare Now" button uses `button-primary` inline-right.

### Footer
**`footer`** — Black canvas, 3px #006fcf top border. Four-column link matrix (Products, Support, About, Social) at desktop. Column heads in `{typography.title-sm}` white; links in `{typography.body-sm}` `{colors.hairline}`. Bottom row has copyright in caption text and payment-method icon strip.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + slide-in drawer; hero headline drops to `{typography.display-md}`; spec-grid becomes 2-column; compare-bar stacks vertically |
| Tablet | 744–1128px | 2-column product grid; nav mega-menu replaced by accordion inside drawer; hero image scales to 50% width beside text |
| Desktop | 1128–1440px | 3-column product grid; full horizontal nav with mega-menu dropdowns; spec-grid 4-column; hero at full 560px min-height |
| Wide | > 1440px | Max content width 1400px centered; hero may expand to 640px; product grid optionally 4-column for large cabinets category |

### Touch Targets
- All buttons minimum 48px tall, 44px wide
- Nav drawer links minimum 52px tap height with generous padding
- Product card entire tile is tappable (full-card anchor)
- Compare checkbox uses a 44×44px hit area regardless of visual checkbox size

### Collapsing Strategy
- Mega-menu collapses to full-screen drawer with accordion category sections
- Promo banner persists on mobile, font reduces to 11px but banner stays 40px tall
- Spec grid collapses from 4-column to 2-column at tablet, single-column on narrow mobile
- Footer collapses from 4-column to 2-column at tablet, stacked single-column on mobile
- Compare bar stack becomes full-width CTA strip with scrollable thumbnail row

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font stack was extractable — the live site likely injects font tokens via JavaScript or Shopify theme settings. Typography above uses system Arial Black / Arial as a structural placeholder; the actual brand may use a licensed geometric or condensed sans-serif (common in tool/garage category: Bebas Neue, Barlow Condensed, or similar).
- Only three hex values were extracted (#006fcf, #dedede, #121212); error states, success states, and any secondary brand accent colors are inferred, not observed.
- Exact button radius values (site may use 0px true square or a 2–3px micro-radius) are unconfirmed; `{rounded.xs}` (4px) is a conservative estimate.
- Product photography art direction (lifestyle vs. white-bg studio vs. dark studio) unconfirmed from extraction; dark studio assumed from meta theme-color and surface palette.
- Animation/transition values (hover durations, drawer slide timing) not extractable; standard 150–200ms ease-out assumed.
- No price-display formatting tokens (installment messaging, per-unit pricing) confirmed from extraction.
