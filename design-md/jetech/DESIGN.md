---
version: alpha
name: "JETech"
source_url: "https://www.jetechins.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Filtering by device generation is the first gesture JETech asks of its visitors — category pages reorganize around phone model rather than product type, treating hardware compatibility as the governing navigational logic. This makes the storefront's aesthetic intentionally utilitarian: no hero lifestyle photography, no ambient mood direction, just white-canvas grids holding flat-lay shots of polycarbonate slabs and tempered glass panels photographed edge-on so the 0.33mm thickness reads as engineered precision. The estimated primary blue (approximately #0066CC, unconfirmed by live extraction — see Known Gaps) carries CTAs, selected filter states, and active navigation indicators with a cool, mid-register technology tone that signals dependability over excitement; against the white canvas it reads almost institutional, closer to a hardware configurator than a fashion accessory shop. Product cards do significant information work: star ratings with parenthetical review counts, compatibility strings such as "for iPhone 15 Pro Max," sale badges in high-contrast red (#CC0000), and stacked color-variant chips all coexist within a card roughly 240px wide. This density mirrors marketplace logic — maximum signal per centimeter of screen — rather than editorial restraint. No custom webfonts were detected during extraction, pointing to a system-font-stack strategy that keeps catalogue load times fast across hundreds of SKUs. Badges shoulder editorial hierarchy: SALE, NEW, and BEST SELLER appear in tight-tracked uppercase at 11px, adding emphasis without requiring additional image assets. Corners throughout are softly rounded at approximately 4px — cards, buttons, filter chips, and search fields all share this low-key radius that keeps the grid from reading sterile while still conveying a no-nonsense engineering sensibility. A dark footer anchored at near-black (#1A1A1A) with gray-toned links provides visual terminus, while a thin primary-blue top bar carries promotional messaging in reversed white type — a structural frame that brackets the browsing experience without demanding attention.

colors:
  primary: "#0066CC"
  primary-active: "#004FA3"
  primary-disabled: "#99C2E8"
  ink: "#1A1A1A"
  body: "#333333"
  muted: "#777777"
  hairline: "#E0E0E0"
  hairline-soft: "#F0F0F0"
  canvas: "#FFFFFF"
  surface-soft: "#F8F8F8"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  sale: "#CC0000"
  on-sale: "#FFFFFF"
  star: "#FF9900"
  badge-new: "#0066CC"
  badge-bestseller: "#FF6600"
  price-strike: "#999999"
  link-muted: "#CCCCCC"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  compat-tag:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
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
    rounded: "{rounded.xs}"
    padding: "10px 20px"
    height: 40px
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "9px 19px"
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
    height: 40px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    height: 40px
  nav-top-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    activeTextColor: "{colors.primary}"
    activeBorderBottom: "2px solid {colors.primary}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    imageAspectRatio: "1:1"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-sm}"
  rating-row:
    starColor: "{colors.star}"
    countColor: "{colors.muted}"
    typography: "{typography.caption}"
  price-display:
    salePriceColor: "{colors.sale}"
    regularPriceColor: "{colors.ink}"
    strikePriceColor: "{colors.price-strike}"
    salePriceTypography: "{typography.price-lg}"
    regularPriceTypography: "{typography.price-lg}"
    strikePriceTypography: "{typography.price-sm}"
  sale-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-sale}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  new-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  bestseller-badge:
    backgroundColor: "{colors.badge-bestseller}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  compatibility-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.primary}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  trust-badge-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    iconColor: "{colors.primary}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
  compat-string:
    textColor: "{colors.muted}"
    typography: "{typography.compat-tag}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.link-muted}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} 0"
  footer-sub:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.body}"
    padding: "{spacing.base} 0"

## Components

### Buttons

**`button-primary`** — Solid `{colors.primary}` (#0066CC) fill at 40px height with `{rounded.xs}` (4px) radius, carrying `{typography.button-md}` in `{colors.on-primary}` white. The active/pressed state deepens to `{colors.primary-active}` (#004FA3); disabled washes the fill to `{colors.primary-disabled}` without opacity reduction, preserving legibility against the white canvas. Primary buttons are placed sparingly — Add to Cart and primary hero CTAs only — so the blue retains signal value across dense catalogue grids where `{colors.primary}` already appears in filter chips and nav indicators.

**`button-secondary`** — White fill with a 1px `{colors.primary}` border and matching blue text, sharing the 40px height and 4px radius of the primary. Used for secondary actions such as "View All" section anchors and filter-reset controls. On hover the border and label deepen to `{colors.primary-active}` without flooding the background, maintaining contrast hierarchy against the filled primary variant.

**`button-ghost`** — Transparent background with `{colors.body}` text at `{typography.button-sm}`, underline present. Used for inline text-link actions such as breadcrumb ancestry, "Show More" expand triggers, and legal footer links. No explicit border or height constraint; minimum touch target achieved through vertical padding.

### Inputs

**`text-input`** — 40px height, `{rounded.xs}` radius, 1px `{colors.hairline}` border that sharpens to `{colors.primary}` on focus with no animation delay. Placeholder text renders in `{colors.muted}`. Labels sit statically above the field at `{typography.caption}` weight in `{colors.body}` — no floating label animation. Used across account forms, checkout fields, and any inline filter inputs.

**`search-bar`** — Extends the text-input treatment with an attached submit button filled `{colors.primary}` carrying a search-icon glyph in `{colors.on-primary}`. The input and button share a single 40px height container with no gap, presenting as a single joined unit. Featured in the masthead on desktop and within the mobile drawer. The field border transitions to `{colors.primary}` on focus; the submit button deepens to `{colors.primary-active}` on press.

### Navigation

**`nav-top-bar`** — A 36px promotional strip pinned at the very top of every page, filled solid `{colors.primary}` with centered `{typography.caption}` in `{colors.on-primary}`. Carries free-shipping thresholds or active promotions. This blue-before-logo moment is JETech's strongest brand signal on first paint — device-accessories shoppers arriving from search ads orient instantly to the primary color before the logo loads.

**`nav-bar`** — 60px white bar with a 1px `{colors.hairline}` bottom rule. Logo anchors left; primary category links center in `{typography.nav-link}`; search and cart icons right. Category dropdowns open on hover exposing a white panel with `{rounded.sm}` corners and a soft drop shadow. On mobile, the bar collapses to logo-left plus hamburger-right; the drawer slides in from the left with the full category tree rendered as an accordion.

**`category-tab`** — Horizontal tab strip used on category landing pages to filter by device family (iPhone, Samsung, iPad, Tablet, etc.). Inactive: `{colors.muted}` text at `{typography.nav-link}`, no background fill. Active: `{colors.primary}` text with a 2px `{colors.primary}` underline, no filled pill — a lightweight active state that keeps the white surface intact beneath the tab row.

**`breadcrumb`** — Single-line path at `{typography.caption}`. Ancestor nodes render in `{colors.muted}`; current node renders in `{colors.ink}`. Slash character separators, no chevron icons, no wrapping on desktop. Sits directly above the page heading, below the nav-bar.

### Product Display

**`product-card`** — White `{colors.surface-card}` surface with a 1px `{colors.hairline-soft}` border and `{rounded.xs}` radius. No box shadow. Product image fills a 1:1 square at the card top; badge slots (up to two stacked at top-left of the image) follow; then the product title at `{typography.body-sm}` in two-line max with ellipsis; then a `rating-row`; then the `price-display` block; then color-variant chips if applicable. Cards in four-column desktop grids carry consistent padding via `{spacing.md}` on all sides. The entirely tappable card surface on mobile avoids the common accessibility failure of title-only tap targets.

**`rating-row`** — Five-position star row filled solid `{colors.star}` (#FF9900), immediately followed by a parenthetical review count in `{colors.muted}` at `{typography.caption}`. Stars are solid SVG fills, not outlines; fractional ratings render as a clipped partial fill on the terminal star. This orange-star pattern is deliberately familiar to accessories shoppers cross-referencing products from marketplace listings.

**`price-display`** — Sale state: `{typography.price-lg}` (22px bold) in `{colors.sale}` (#CC0000) beside a struck-through original at `{typography.price-sm}` (16px regular) in `{colors.price-strike}`. The 6px size differential between the two makes the discount legible at a glance without requiring a percentage-off badge. Regular state: single price in `{colors.ink}` at `{typography.price-lg}`. No currency symbol size reduction — the dollar sign matches the numeral weight.

**`sale-badge`** — `{colors.sale}` fill, `{colors.on-sale}` text, `{typography.badge}` (11px, 700 weight, uppercase, 0.5px tracking), `{rounded.xs}` radius, 2px top / 6px horizontal padding. Positioned at the top-left corner of the product card image, overlapping the image edge by 0px (flush to the image container boundary). When SALE and a secondary badge both appear, SALE occupies the upper slot.

**`new-badge`** and **`bestseller-badge`** — Structurally identical to `sale-badge` but filled `{colors.badge-new}` (primary blue, #0066CC) and `{colors.badge-bestseller}` (#FF6600 orange) respectively. The color distinction lets shoppers scan for novelty vs. popularity without reading the label text. Both share the same 11px uppercase `{typography.badge}` and `{rounded.xs}` radius.

### Brand-Signature Components

**`compatibility-filter`** — Pill-shaped chips (`{rounded.full}`, 6px–14px padding) that reorganize the product grid by device model. Inactive: `{colors.surface-soft}` background, `{colors.body}` text, 1px `{colors.hairline}` border. Active: solid `{colors.primary}` fill, `{colors.on-primary}` text, 1px `{colors.primary}` border. Chips render in a single scrollable row on mobile; they wrap to multiple rows on desktop when the device family list is long. This component is JETech's defining UX pattern — the primary navigational gesture on every category page rather than a secondary filter panel.

**`hero-banner`** — Full-width `{colors.primary}` panel carrying a `{typography.display-xl}` headline in `{colors.on-primary}`, a `{typography.body-md}` supporting line, and a `button-secondary` CTA (white fill, primary border) that contrasts against the blue field. On desktop, a product silhouette or lifestyle shot bleeds off the right edge within the panel. On mobile the layout stacks vertically — text above, image below — and the heading scales down to `{typography.display-md}`.

**`trust-badge-strip`** — A full-width band in `{colors.surface-soft}` with a 1px `{colors.hairline}` top border, no rounded corners. Contains three to five icon-and-label pairs (shield for warranty, truck for shipping, arrow for returns, certification marks) at `{typography.caption}` in `{colors.body}`, with icons at approximately 24px in `{colors.primary}`. Appears immediately below the hero or at the top of category pages. The flat-edge, full-bleed treatment distinguishes it from product cards and prevents it from being mistaken for a content module.

**`compat-string`** — A single line below the product title at `{typography.compat-tag}` in `{colors.muted}` listing the compatible device(s) — e.g., "Compatible with iPhone 15 / 15 Pro." Not a badge; no background fill or border. Truncates with ellipsis if the compatibility string exceeds one line. This text is the product's secondary identifier after the title and functions as a second-pass filter for shoppers scanning a grid.

**`footer`** — Near-black `{colors.ink}` full-width panel at `{spacing.xxl}` vertical padding. Column headings at `{typography.title-sm}` in `{colors.on-dark}`; body links at `{typography.body-sm}` in `{colors.link-muted}` (#CCCCCC). Four standard columns: Customer Service, Products, About JETech, Follow Us. A `footer-sub` row below carries copyright and policy links at `{typography.caption}` in `{colors.muted}`, separated by a 1px `{colors.body}` top rule.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with full-height left drawer; compatibility filters collapse to a single horizontally scrollable chip row; hero stacks text above image; trust strip shows two icons only; price-display font scales down one step |
| Tablet | 744–1128px | Two-column product grid; nav retains icon row with text labels; compatibility filters wrap to two rows; hero goes side-by-side with smaller image; category tabs scroll horizontally |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with hover dropdowns; compatibility filters render as a full wrapping chip grid; hero at full height with bleed image |
| Wide | > 1440px | Content constrained to ~1400px max-width and centered; product grids expand to four or five columns; hero background image extends to fill additional horizontal space with CSS object-position |

### Touch Targets

- Compatibility filter chips minimum 36px tall on mobile; 4px gap between chips in scroll row
- Nav icons (search, cart, hamburger) minimum 44×44px hit area
- Entire product card surface is tappable on mobile, not just the title link
- Color variant chips minimum 32×32px with `{spacing.xs}` gap between swatches
- Footer links minimum 36px tall on mobile with `{spacing.md}` vertical padding between rows
- Badges on product cards do not need to be tappable independently; tap targets resolve to the parent card

### Collapsing Strategy

- Primary nav collapses at 744px to hamburger icon; left-side drawer slides in over content with a 50% opacity scrim behind it
- Compatibility filter row converts from a wrapping grid (desktop) to a horizontally scrollable single row (mobile) to prevent multi-row height growth that would push products below the fold
- Hero banner switches from two-column (text left, product image right) to stacked (text then image) below 744px; `{spacing.section}` vertical padding reduces to `{spacing.xl}` on mobile
- Trust badge strip reduces from five icons to two on mobile, retaining shipping guarantee and return policy as the highest-trust signals
- Footer four-column grid collapses to two columns on tablet, and to a full-width accordion (one section per trigger) on mobile, with sections closed by default except Customer Service

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the live site at jetechins.com appears to load color tokens via JavaScript or returns a bot-resistant response; every color value in this file is estimated from brand category knowledge and tech-accessories conventions, not confirmed by live CSS extraction. The primary blue (#0066CC) is a reasonable estimate but must be verified against the site's computed stylesheet before use in production.
- **No font families detected** — no `@font-face` declarations or external font CDN links were found during extraction; the system-font stack used throughout this file is an inference. JETech may use a licensed sans-serif such as Open Sans, Roboto, or a proprietary webfont loaded via a JavaScript font loader that was not evaluated.
- **No meta theme-color present** — browser chrome tinting behavior is unconfirmed; the estimated primary blue is used as a stand-in.
- **Badge exact colors unverified** — SALE red (#CC0000) and BEST SELLER orange (#FF6600) reflect common e-commerce conventions in the accessories category; actual computed values may differ from these estimates.
- **Star rating color source** — #FF9900 mirrors the Amazon marketplace star color and is widely used in the accessories vertical; JETech's own star SVG fill may differ slightly.
- **Platform unconfirmed** — the site is not identified as Shopify or any other detectable platform; component patterns such as cart-drawer animation timing, product option selector markup, and checkout flow styling are inferred from category conventions rather than confirmed platform templates.
- **Exact border-radius values** — the 4px (`{rounded.xs}`) estimate is based on visual brand conventions for tech-accessories storefronts; actual computed radius values should be confirmed by inspecting live rendered elements before locking tokens.
- **Promotional top-bar content and presence** — the `nav-top-bar` component is inferred from common DTC accessories patterns; whether JETech uses this pattern and its exact background color (assumed `{colors.primary}`) could not be confirmed from extraction.
