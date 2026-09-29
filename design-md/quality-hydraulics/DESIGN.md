---
version: alpha
name: "Quality Hydraulics"
source_url: "https://www.qualityhydraulics.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Amber arrives before blue — #ffb73e, a high-visibility safety orange that reads like a hydraulic coupling at operating pressure, leads the palette and claims every primary action on the page. The decision is industrial-honest: this is a working parts supplier where procurement happens under fluorescent shop light, not a consumer lifestyle brand asking for admiration. The #0079c7 utility blue recedes into secondary roles — informational links, hover states, supporting structure — while #222222 near-black handles virtually all body copy at serious density. No softening neutrals, no lifestyle photography gradients; the canon is dark type on white canvas with amber firing at checkout and quote-request moments. Because no custom typeface stack was captured from the live site, the design system defaults to a compact system-sans hierarchy at functional weights — bold at display, medium at button, regular at body — sized for scan-and-locate behavior from a user who already knows the part number. Corner radii are minimal, consistent with catalogue-grade UI: a 4px `{rounded.xs}` on inputs and a flat `{rounded.none}` on table rows signal precision over personality. The product card is the center of gravity: part number renders in monospace caption, stock status carries a small `{colors.in-stock}` green or `{colors.low-stock}` amber badge, and the add-to-cart button fires in the full amber primary. Category navigation uses the industrial blue as an active underline, keeping the amber reserved for conversion actions only — a discipline that preserves its signal value across a deep catalog of fittings, valves, cylinders, and pneumatic components. Section spacing is generous for a B2B property because filter panels, spec tables, and multi-image product views demand vertical room to breathe without feeling cluttered.

colors:
  primary: "#ffb73e"
  primary-active: "#e09a20"
  primary-disabled: "#ffd98a"
  ink: "#222222"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#1a1a1a"
  on-primary: "#222222"
  on-dark: "#ffffff"
  industrial-blue: "#0079c7"
  industrial-blue-active: "#005fa0"
  industrial-blue-muted: "#e6f2fa"
  in-stock: "#2e7d32"
  low-stock: "#e65c00"
  out-of-stock: "#b00020"
  status-bg: "#f0f7ff"
  warning-bg: "#fff8e6"
  error-bg: "#fff0f0"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  label-caps:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  part-number:
    fontFamily: "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.4px
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
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
    padding: 12px 24px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.industrial-blue}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1.5px solid {colors.industrial-blue}"
  button-secondary-active:
    backgroundColor: "{colors.industrial-blue-muted}"
    textColor: "{colors.industrial-blue-active}"
    border: "1.5px solid {colors.industrial-blue-active}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.industrial-blue}"
    padding: 10px 12px
    height: 42px
    placeholderColor: "{colors.muted-soft}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    padding: 10px 48px 10px 40px
    height: 46px
    iconColor: "{colors.muted}"
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.none}"
      width: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 40px
    activeIndicator:
      color: "{colors.industrial-blue}"
      height: 2px
  top-utility-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    height: 36px
    linkColor: "{colors.primary}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "3px solid {colors.primary}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
    rounded: "{rounded.none}"
    padding: "{spacing.lg} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspect: "1/1"
    partNumberTypography: "{typography.part-number}"
    partNumberColor: "{colors.muted}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
    hoverBorder: "1px solid {colors.industrial-blue}"
    hoverBoxShadow: "0 2px 8px rgba(0,121,199,0.15)"
  stock-badge:
    in-stock:
      backgroundColor: "#e8f5e9"
      textColor: "{colors.in-stock}"
      typography: "{typography.label-caps}"
      rounded: "{rounded.xs}"
      padding: "3px 8px"
    low-stock:
      backgroundColor: "{colors.warning-bg}"
      textColor: "{colors.low-stock}"
      typography: "{typography.label-caps}"
      rounded: "{rounded.xs}"
      padding: "3px 8px"
    out-of-stock:
      backgroundColor: "{colors.error-bg}"
      textColor: "{colors.out-of-stock}"
      typography: "{typography.label-caps}"
      rounded: "{rounded.xs}"
      padding: "3px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    accentColor: "{colors.primary}"
    minHeight: 380px
    padding: "{spacing.section} {spacing.xxl}"
    ctaButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.xs}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.industrial-blue}"
    padding: "{spacing.lg}"
    hoverBorder: "1px solid {colors.primary}"
    hoverAccentBar:
      height: 3px
      color: "{colors.primary}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBg: "{colors.surface-soft}"
    headerTypography: "{typography.label-caps}"
    headerColor: "{colors.muted}"
    cellTypography: "{typography.body-sm}"
    cellColor: "{colors.body}"
    keyTypography: "{typography.caption}"
    keyColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    rowStripeBg: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
  quote-request-banner:
    backgroundColor: "{colors.industrial-blue}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl} {spacing.xxl}"
    ctaButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.xs}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    activeColor: "{colors.body}"
    separatorColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.industrial-blue}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    height: 36px
    width: 36px
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    borderRight: "1px solid {colors.hairline}"
    checkboxAccent: "{colors.industrial-blue}"
    activeFilterPill:
      backgroundColor: "{colors.industrial-blue-muted}"
      textColor: "{colors.industrial-blue}"
      typography: "{typography.button-sm}"
      rounded: "{rounded.full}"
      padding: "4px 10px"
  alert-callout:
    info:
      backgroundColor: "{colors.status-bg}"
      borderLeft: "4px solid {colors.industrial-blue}"
      textColor: "{colors.body}"
      typography: "{typography.body-sm}"
      iconColor: "{colors.industrial-blue}"
    warning:
      backgroundColor: "{colors.warning-bg}"
      borderLeft: "4px solid {colors.primary}"
      textColor: "{colors.body}"
      typography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-caps}"
    headingColor: "{colors.primary}"
    linkColor: "#cccccc"
    linkHoverColor: "{colors.primary}"
    borderTop: "4px solid {colors.primary}"
    padding: "{spacing.section} {spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Filled amber (#ffb73e) on dark ink text, 44px tall with 4px corners and 24px horizontal padding. This is the sole conversion surface: Add to Cart, Request Quote, Submit Order. Active state deepens to #e09a20; disabled lightens to #ffd98a with muted text to signal unavailability without confusion in dense catalog contexts.

**`button-secondary`** — White fill with a 1.5px industrial-blue (#0079c7) stroke and matching text. Used for secondary actions like Save to List, Compare, and Print Spec Sheet where the amber must stay reserved for primary conversion. Active state fills lightly with `{colors.industrial-blue-muted}`.

**`button-ghost`** — Transparent background, ink text, no border. Ideal for in-table actions, filter-clear controls, and breadcrumb-adjacent navigation where a full button weight would over-compete.

### Search Bar

**`search-bar`** — Full-width input with a 2px hairline border that jumps to amber (#ffb73e) on focus, signaling the search function as a primary entry point. A loupe icon sits at 40px inset left; a square amber submit button caps the right edge flush with no gap. This is the dominant wayfinding tool for a multi-thousand SKU catalog where customers arrive with a part number already in hand.

### Navigation

**`nav-bar`** — 64px white bar, 1px hairline bottom border, logo at 40px height flush left. Link labels use `{typography.nav-link}` at weight 600; active links carry a 2px industrial-blue underline indicator. Preceded by `{top-utility-bar}` — a 34px dark band holding phone number, account login, and cart count in small type with amber accent links.

**`mega-menu`** — Drops below the nav on category hover with a 3px amber top border acting as a visible connection to the triggering item. White background, 4-column grid of category links organized under bold label-caps headings, deep shadow at 0 4px 16px to lift it off the page. No rounded corners — flush with page edges.

### Product Card

**`product-card`** — White surface, 1px hairline border, 4px corner radius. Part number renders in `{typography.part-number}` (monospace, muted) above the title for scan-first behavior. Price uses `{typography.price}` at 20px/700 weight. Stock status badge sits beneath the price. On hover the border transitions to industrial blue with a faint blue shadow. The Add to Cart button spans full width at the card bottom in amber primary.

### Stock Badges

**`stock-badge`** — Three states in small caps: in-stock renders green-on-pale-green, low-stock fires amber-on-pale-amber (reusing the primary hue to signal mild urgency without dedicated color), and out-of-stock shows crimson-on-pale-red. All 4px rounded, uppercase 11px/700 tracking.

### Spec Table

**`spec-table`** — Tight ruled table for technical data (port sizes, pressure ratings, flow ratings, materials). Header row in light gray with uppercase muted label-caps. Alternating stripe on data rows using `{colors.surface-soft}`. Key column values in monospace `{typography.caption}` for alignment across heterogeneous values. 1px hairline borders throughout, no rounding.

### Category Tiles

**`category-tile`** — Square or near-square tiles arranged in a 4–6 column grid below the hero. Light gray fill, hairline border, industrial-blue icon at center top, title in `{typography.title-sm}` below. On hover a 3px amber bar appears at the bottom edge and the border brightens — a compact signal that keeps amber visible without overusing it.

### Quote Request Banner

**`quote-request-banner`** — Full-bleed industrial-blue (#0079c7) band with white heading and body text, amber CTA button. Typically placed between catalog sections and above footer. No corner radius — edge-to-edge industrial authority.

### Alert Callout

**`alert-callout`** — Left-border accent strips for inline notices. Info variant uses 4px industrial-blue left border on pale blue background. Warning uses 4px amber left border on pale amber. Used in product pages for shipping lead-time notices, regulatory flags, and minimum order warnings.

### Footer

**`footer`** — Near-black (#1a1a1a) background with a 4px amber top rule acting as the visual bookend to the amber hero CTA above the fold. Column headings in label-caps at amber, link text at #cccccc softening to amber on hover. Phone and address in body-sm. Bottom bar holds copyright and legal links in muted-soft.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Mega-menu collapses to full-screen drawer with accordion category sections. Search bar becomes full-width sticky below nav. Product grid drops to 1-column. Filter sidebar converts to bottom-sheet modal. Spec table becomes horizontally scrollable. |
| Tablet | 744–1128px | Two-column product grid. Mega-menu remains dropdown but narrows to 2 columns. Filter sidebar may stay visible as a collapsible left panel at 220px. Hero banner reduces to 280px min-height. |
| Desktop | 1128–1440px | Three-column product grid. Full 4-column mega-menu. Filter sidebar pinned at 240px; content area takes remaining width. |
| Wide | > 1440px | Max content width capped at 1400px, centered. Four-column product grid. Hero padding scales with `{spacing.section}` + additional vspace. Category tile grid expands to 6 columns. |

### Touch Targets

- All interactive buttons minimum 44×44px native tap area
- Pagination items minimum 36×36px with 4px spacing between
- Filter checkboxes padded to 44px touch height even when visually smaller
- Category tiles minimum 80px height on mobile for reliable tap

### Collapsing Strategy

- Top utility bar hides fully on mobile; phone number moves into footer
- Mega-menu collapses to hamburger icon triggering a slide-in drawer
- Filter sidebar converts to a bottom-sheet triggered by a floating "Filter" pill
- Secondary nav tabs (account, orders, saved lists) collapse into a profile icon dropdown
- Spec table scrolls horizontally within a visible scroll-hint shadow on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font-family stack was detected from the live site; the design system falls back to system-sans and system-mono stacks. Actual brand typography (if a licensed face is used) would need to be confirmed by inspecting loaded font files or a CSS audit.
- No meta theme-color was set, so mobile browser chrome tinting preference is unresolvable from extracted data.
- Only three hex colors were recovered. Secondary grays, status greens/reds, and surface neutrals above are inferred from B2B industrial convention rather than extracted directly.
- Pricing display rules (tiered/volume pricing presentation, unit-of-measure display) could not be confirmed without authenticated catalog access.
- Whether the site uses a custom icon set, SVG sprite, or a library (FontAwesome, Material Icons) for product-category and UI icons is unknown.
- Exact nav height, logo lockup dimensions, and mega-menu column count require live DOM inspection to confirm.
- The site's platform (not Shopify per hints) is unconfirmed; cart, checkout, and account UI may follow a custom or legacy framework with constraints not captured here.
