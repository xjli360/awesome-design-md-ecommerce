---
version: alpha
name: "Microscope.com"
source_url: "https://www.microscope.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The deep navy of #163959 functions less as branding and more as a procurement declaration — this is a catalog built for lab managers and purchasing officers, not for casual browsing. Microscope.com deploys color not as identity but as operational language: reds (#bd2426, #de5052) signal promotional urgency and sale pricing; orange (#f68b1f, #ee730a) drives every primary add-to-cart CTA; a layered green spectrum (#9bca3e, #bada7a, #516b1d) marks stock availability; and three tiers of blue (#62a1d8, #2f7bbf, #163959) create a visual hierarchy from body links through nav states to header anchors. The font stack is entirely system — Arial and Helvetica Neue, no webfonts — which gives the interface the same authority a printed lab catalog would carry, where specification density matters more than typographic sophistication. Navigation runs heavy: a slim utility bar across the top holds phone numbers and account controls on a white canvas, while the full-width navy bar below organizes mega-menu categories (compound, stereo, digital, electron, fluorescence) in white bold type at 13px. Product cards are rectangular and zero-radius, a hairline border against white, with a 4:3 product image, bold price in 20px, model number in caption gray, and an orange CTA button flush to the bottom edge. Spec tables stripe in #ebebeb alternating rows to keep magnification ranges, stage dimensions, and illumination specs readable without color noise. The canvas is white throughout with {colors.surface-soft} panels carrying filter sidebars. Surface variation comes from alternating stripe rows and the navy-to-white layering in navigation, not from decorative gradients or imagery. Rounded corners appear only as a 4px concession in form inputs and badges — the broader grid vocabulary is rectangular and grid-forward, matching the instrument photography it frames.

colors:
  primary: "#2f7bbf"
  primary-dark: "#163959"
  primary-light: "#62a1d8"
  primary-bright: "#0051c3"
  primary-active: "#1a5a9a"
  primary-disabled: "#a0c4e8"
  accent: "#f68b1f"
  accent-active: "#ee730a"
  accent-dark: "#c16508"
  accent-deeper: "#904b06"
  accent-light: "#f9b169"
  promo-red: "#bd2426"
  promo-red-light: "#de5052"
  promo-red-dark: "#521010"
  stock-green: "#9bca3e"
  stock-green-light: "#bada7a"
  stock-green-dark: "#516b1d"
  ink: "#272727"
  body: "#404040"
  muted: "#595959"
  muted-soft: "#737373"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  border-mid: "#bfbfbf"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-stripe: "#ebebeb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: -0.3px
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
    textDecoration: line-through
  spec-label:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.2px
  breadcrumb:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  mono-spec:
    fontFamily: "courier, monaco, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
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
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.accent-light}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
  button-secondary-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-navy:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-mid}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 36px
    typography: "{typography.body-md}"
    focusBorder: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 8px 40px 8px 12px
    height: 38px
    typography: "{typography.body-md}"
    focusBorder: "1px solid {colors.primary}"
    submitButtonBackground: "{colors.accent}"
    submitButtonColor: "{colors.on-accent}"
    submitButtonRounded: "{rounded.none}"
  nav-bar-utility:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    linkColor: "{colors.primary}"
    typography: "{typography.caption}"
    height: 32px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 44px
    logoColor: "{colors.on-dark}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingColor: "{colors.primary-dark}"
    linkColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    shadowY: 4px
    shadowColor: "rgba(0,0,0,0.12)"
    padding: "{spacing.lg}"
    columnGap: "{spacing.xl}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-md}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    imageAspect: "4/3"
    titleTypography: "{typography.title-sm}"
    modelTypography: "{typography.caption}"
    modelColor: "{colors.muted}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    comparePriceTypography: "{typography.price-compare}"
    comparePriceColor: "{colors.muted-soft}"
    ctaBackground: "{colors.accent}"
    ctaColor: "{colors.on-accent}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
  price-badge:
    backgroundColor: "{colors.promo-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
    textTransform: uppercase
  stock-badge:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  low-stock-badge:
    backgroundColor: "{colors.accent-dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  out-of-stock-badge:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  category-badge:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  spec-table:
    backgroundColor: "{colors.canvas}"
    stripeBg: "{colors.surface-stripe}"
    border: "1px solid {colors.hairline}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-md}"
    valueColor: "{colors.ink}"
    monoValueTypography: "{typography.mono-spec}"
    rowHeight: 36px
    cellPadding: "8px 12px"
  breadcrumb-nav:
    textColor: "{colors.primary}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.muted}"
    typography: "{typography.breadcrumb}"
    gap: "{spacing.xs}"
  filter-sidebar:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    width: 240px
    padding: "{spacing.base}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.ink}"
    optionTypography: "{typography.body-md}"
    optionColor: "{colors.body}"
    countColor: "{colors.muted-soft}"
    dividerColor: "{colors.hairline}"
  compare-bar:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    height: 56px
    padding: "0 {spacing.lg}"
    ctaBackground: "{colors.accent}"
    ctaColor: "{colors.on-accent}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
  hero-banner:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    subColor: "{colors.hairline-soft}"
    ctaBackground: "{colors.accent}"
    ctaColor: "{colors.on-accent}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    minHeight: 320px
    padding: "{spacing.xxl} {spacing.xl}"
  quantity-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.border-mid}"
    rounded: "{rounded.none}"
    controlBackground: "{colors.surface-stripe}"
    controlColor: "{colors.ink}"
    width: 80px
    height: 36px
    typography: "{typography.body-md}"
  pagination:
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackground: "{colors.canvas}"
    inactiveTextColor: "{colors.primary}"
    inactiveBorder: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    size: 32px
    typography: "{typography.button-sm}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.primary-light}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
    dividerColor: "{colors.primary}"
    legalBackground: "{colors.ink}"
    legalTypography: "{typography.caption}"
    legalColor: "{colors.muted-soft}"

## Components

### Buttons

**`button-primary`** — The main CTA uses orange (#f68b1f) rather than the brand navy, a deliberate separation ensuring the button reads against both white product cards and dark navy header zones simultaneously. Active state drops to #ee730a; disabled washes to the pale #f9b169. Height is 40px with {rounded.xs} (4px) — the smallest concession to softening in an otherwise rectangular UI.

**`button-secondary`** — Outlined with a 1px {colors.primary} border and matching blue text on a white fill. Used for secondary actions like "Request a Quote," "Add to Wishlist," or "Compare." On hover, border and text darken to {colors.primary-active} (#1a5a9a).

**`button-navy`** — A solid dark navy button ({colors.primary-dark}) for header account actions, login prompts, and footer zone CTAs where orange would create visual conflict against orange promo badges nearby. White text throughout all states.

**`button-link`** — Inline blue text links with underline, used throughout product descriptions, spec callout footnotes, and "see all in category" navigation. Font weight matches surrounding body copy rather than bolding.

### Navigation

**`nav-bar-utility`** — A slim 32px white bar at the very top of the page carries phone support numbers, sign-in and account links, and cart access. Type is 12px {colors.muted}, links in {colors.primary}. Separated from the main nav by a {colors.hairline-soft} border-bottom.

**`nav-bar`** — The primary 44px navy bar ({colors.primary-dark}) holds the logo left-aligned and mega-menu category links right. All text is white 13px bold. No visible border-bottom — the color shift from white utility bar to navy creates the visual break. The search bar lives between these two tiers or inline in the navy bar depending on viewport.

**`mega-menu`** — Full-width white panel that drops on hover from nav category labels. Columns are spaced {spacing.xl} apart, each headed by a {typography.title-sm} category name in {colors.primary-dark}. Subcategory links render in {colors.primary} at 14px. A 4px shadow grounds the panel against the page. No border-radius — panel edges are square.

### Product Cards

**`product-card`** — Strictly rectangular ({rounded.none}) white cards with a 1px {colors.hairline} border. Product image fills a 4:3 container at top. Below: title in 14px bold, model/SKU in 12px {colors.muted}, price in 20px bold {colors.ink}, and where applicable a struck-through compare price in 14px {colors.muted-soft}. An orange "Add to Cart" button spans the card's full bottom width. Sale items receive a {colors.promo-red} badge on the image top-left corner.

### Badges

**`price-badge`** — Red (#bd2426) flag on product images and list rows marking sale pricing and clearance items. Uppercase 11px bold text, {rounded.xs}, positioned at the top-left of the product thumbnail. A lighter variant ({colors.promo-red-light}) appears on hover states.

**`stock-badge`** — Green (#9bca3e) pill confirming item availability, displayed on product tiles below the model number and prominently on the product detail page header. Low-stock items use the darker {colors.accent-dark} variant to signal urgency without triggering the red alert register.

**`category-badge`** — Light blue (#62a1d8) chip applied to products spanning multiple instrument families (e.g., a stereo microscope cross-listed under "Digital"). Compact 3px 8px padding so it doesn't dominate the card at small sizes.

### Spec Table

**`spec-table`** — The visual workhorse of every product detail page. Rows alternate between white and {colors.surface-stripe} (#ebebeb), no column dividers. Left-column labels render in {typography.spec-label} (12px uppercase, 0.3px tracking) in {colors.muted}; right-column values in {typography.body-md} in {colors.ink}. Numeric tolerances, part numbers, and model codes use {typography.mono-spec} (Courier) to preserve column alignment and signal machine-readable precision. No rounded corners anywhere in the table.

### Search

**`search-bar`** — Full-width input (38px tall) with a flush orange submit button on the right edge ({colors.accent}, no border-radius where it meets the input). At rest the input border is {colors.hairline}; on focus it shifts to a 1px {colors.primary} border. Suggests model numbers, SKUs, magnification specs, and category names. The orange submit button visually anchors the search zone with the same CTA vocabulary as add-to-cart.

### Filters

**`filter-sidebar`** — A 240px left-column panel on collection pages, {colors.surface-soft} background with a 1px {colors.hairline} right border. Stacked accordion sections cover Brand, Microscope Type, Magnification Range, Price, Application, and Illumination. Each option is 14px with a parenthetical count in {colors.muted-soft}. Checkboxes use the standard system style; no custom styled inputs detected.

### Compare

**`compare-bar`** — A sticky bottom bar in {colors.primary-dark} that appears when two or more products are queued for comparison. Shows small product thumbnails with an × remove control, a count label in white, and an orange "Compare Now" CTA. The bar anchors at z-index above the footer and collapses on mobile to thumbnails-only with no label text.

### Hero Banner

**`hero-banner`** — Full-width navy panel used on category landing pages and promotional campaigns. Heading at {typography.display-xl} (28px bold white), supporting text at {typography.body-md} in {colors.hairline-soft} for slightly softened contrast. Orange CTA button below. Minimum height 320px; banner image where present bleeds to the right while text block holds left-justified within the content container.

### Footer

**`footer`** — Dark navy ({colors.primary-dark}) multi-column link panel. Column headings in white 14px bold, links in {colors.primary-light} (#62a1d8) that shift to white on hover. Four to five columns: Shop by Type, Brands, Resources, Support, About. Below the main body, a thin {colors.primary} divider separates a darker legal strip in {colors.ink} with 12px {colors.muted-soft} copyright and policy links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; mega-menu collapses to hamburger drawer with accordion subcategories; filter sidebar becomes a bottom sheet triggered by floating "Filters" button; hero banner stacks text block above image; utility nav collapses to icon-only (phone, account, cart) |
| Tablet | 744–1128px | Two-column product grid; nav logo and hamburger only, search bar moves to inline below nav; filter sidebar toggles as an overlay panel with close button; compare bar shows thumbnails with truncated titles |
| Desktop | 1128–1440px | Three-column product grid; full mega-menu on hover; filter sidebar persistent as left column; breadcrumbs fully visible; compare bar with full labels and CTA |
| Wide | > 1440px | Four-column product grid; content max-width ~1400px with auto side margins; hero banner image bleeds to viewport edge while text container stays within content width |

### Touch Targets

- Primary CTA buttons: 40px height minimum (44px including tap area padding on mobile)
- Nav links in mobile drawer: 48px row height for reliable thumb reach
- Pagination items: 32px desktop, expanded to 44px on mobile viewports
- Quantity increment/decrement controls: 36px square; expand to 44px square on touch devices
- Filter checkboxes: 24px tap region with 12px visible box, 12px gap between adjacent options
- Compare checkbox on product card: 32px target in lower-left corner

### Collapsing Strategy

- Mega-menu → hamburger drawer at < 1024px; categories become accordion rows with expand chevron; subcategory links indent under open parent
- Filter sidebar → slide-up modal sheet (100vw, 80vh max) on mobile and tablet; "Apply Filters" sticky button at sheet bottom
- Spec table → horizontal scroll container on mobile with the label column pinned sticky-left so spec names remain visible while values scroll
- Compare bar → thumbnails collapse to 32px circles, label text hidden, "Compare" CTA remains visible at reduced 32px height
- Breadcrumbs → show only final two segments on mobile with an ellipsis linking to the root category
- Hero banner → text block stacks above image at < 744px; image crops to 16:9 portrait center

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site was behind Cloudflare bot protection at extraction time; actual DOM values for border-radius, padding rhythm, and exact font-weight usage could not be confirmed from live CSS
- No custom webfont was found — system font stack confirmed (Arial / Helvetica Neue), but heading weight distribution and specific font-size scale across all headings is inferred rather than measured
- Exact nav bar heights (utility bar vs primary bar) are estimated from visual density conventions for catalog-style e-commerce; actual pixel values unconfirmed
- Button border-radius: {rounded.xs} (4px) is a reasonable estimate for a near-flat catalog UI, but the true value could be 0px (fully square); no live DOM measurement available
- Whether the green and orange palettes signal category-specific theming (each instrument family gets a hue) or purely functional states (stock levels, promotions) is unclear without catalog page access
- Hover and focus transition timings, box-shadow values, and animation curves are entirely inferred
- Product card max-width, image container exact dimensions, and grid gutter values not directly measured
- Dark mode support and any high-contrast accessibility variant unknown
- Whether the site uses a legacy non-Shopify custom platform or a headless stack could not be determined from the blocked page response
