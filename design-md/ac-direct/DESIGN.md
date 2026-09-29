---
version: alpha
name: "AC Direct"
source_url: "https://www.acdirect.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  One charcoal — #313131 — is the entire extracted signal from a site that sits behind anti-bot protection, yet that single tone tells the whole story: this is a spec-sheet brand where the product grid does the persuading and the UI stays out of the way. AC Direct sells cleanroom filtration, HVAC units, and industrial air-handling equipment direct to facilities managers, contractors, and engineers — a buyer who reads BTU ratings before brand names. The system-font stack (no custom typeface has been loaded or detected) reinforces that posture: no Cereal, no Canela, no Graphik — just `-apple-system` and Roboto doing their honest work at whatever weight the OS prefers. Because the extraction hit only Cloudflare's holding page, the palette below is reconstructed from industrial HVAC e-commerce convention rather than scraped pixels: a utility blue primary for CTAs and navigation, the confirmed charcoal as the ink anchor, and a close-to-white canvas that lets product photography and technical datasheets read cleanly. Rounded corners sit at `{rounded.xs}` to `{rounded.sm}` — no pill shapes, no expressive radii; corners are cut sharp the way duct flanges are. Spacing is generous in the product grid (breathing room between units and filter specs) and compact in the utility nav (part numbers, model search, account links). The overall register is closer to Grainger or McMaster-Carr than to a consumer appliance brand: dense information, reliable type hierarchy, and a single brand color doing the load-bearing CTA work across every add-to-cart, get-a-quote, and spec-download action on the page. Known color and typographic gaps are large; agents consuming this file should treat the inferred tokens as functional scaffolding, not extracted truth, and refresh from a live crawl when Cloudflare protection is lifted.

colors:
  primary: "#1a5fa8"
  primary-active: "#154d8a"
  primary-hover: "#1d6bbf"
  primary-disabled: "#a0bddb"
  accent-orange: "#e05c00"
  accent-orange-active: "#c45200"
  ink: "#313131"
  body: "#444444"
  muted: "#767676"
  muted-soft: "#999999"
  hairline: "#d6d6d6"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#313131"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#2a7a3b"
  warning: "#b45309"
  error: "#c0392b"
  badge-new: "#e05c00"
  badge-sale: "#c0392b"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-bold:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  micro:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.36
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  button-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  part-number:
    fontFamily: "'Courier New', Courier, 'Lucida Console', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.5px
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.36
    letterSpacing: 0.8px
    textTransform: uppercase
  price-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: -0.25px

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
    padding: 10px 20px
    height: 42px
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
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 42px
    border: "2px solid {colors.primary}"
  button-add-to-cart:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 48px
    border: none
  button-add-to-cart-hover:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 9px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  text-input-error:
    border: "1px solid {colors.error}"
    backgroundColor: "#fff8f7"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: "0 {spacing.lg}"
  nav-top-utility:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  nav-category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.hairline}"
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
    gap: "{spacing.sm}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.10)"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-lg}"
    textColor: "{colors.ink}"
  product-card-part-number:
    typography: "{typography.part-number}"
    textColor: "{colors.muted}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.micro}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.micro}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-in-stock:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.micro}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
    padding: "0 {spacing.base}"
  search-submit-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    width: 56px
    height: 44px
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rowPadding: "{spacing.sm} {spacing.base}"
  category-hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    minHeight: 220px
    padding: "{spacing.xxl} {spacing.lg}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.ink}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    height: 36px
    width: 36px
  filter-sidebar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderRight: "1px solid {colors.hairline}"
    width: 240px
    padding: "{spacing.base}"
  filter-checkbox-active:
    accentColor: "{colors.primary}"
    labelTypography: "{typography.body-sm}"
    labelColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "#a8c8e8"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  trust-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    iconColor: "{colors.primary}"
  quote-request-cta:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    titleTypography: "{typography.title-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"

## Components

### Buttons

**`button-primary`** — A no-frills utility rectangle in the inferred industrial blue, 42px tall with `{rounded.xs}` corners and 600-weight label. Hover lifts to `{colors.primary-hover}`; active state drops to `{colors.primary-active}`; disabled renders the washed `{colors.primary-disabled}` without cursor affordance. Sizing is practical rather than generous — 10px vertical padding keeps the button grid-dense across PDP columns.

**`button-add-to-cart`** — The commercial primary action breaks from the navigation blue to use `{colors.accent-orange}`, signaling urgency and separating purchase intent from informational CTAs at a glance. Runs at 48px height with `{typography.button-lg}` at 700 weight; hover darkens to `{colors.accent-orange-active}`. This is the only component where corner radius is still `{rounded.xs}` but padding stretches to 24px horizontal, making it the widest tap target on the PDP.

**`button-secondary`** — Outlined variant with a 2px `{colors.primary}` border and transparent fill; text inherits the same primary blue. Used for secondary PDP actions like "Download Spec Sheet" or "Request Quote." Matches the height and radius of `button-primary` for consistent row alignment when the two appear side-by-side.

**`button-ghost`** — Lightweight hairline-bordered ghost for filter chips, sort selectors, and compare toggles. 13px type at 600 weight, compact 6px vertical padding. Sits visually quiet in dense filter sidebars.

### Search

**`search-bar`** — A left-aligned text field in `{colors.canvas}` with `{colors.hairline}` border fused on the right edge to `search-submit-button`. The submit button is a flush `{rounded.none}` blue rectangle — no pill shape, no magnifier-only icon; it reads "Search" or shows a search icon at 56px wide. This inline-attached layout mirrors industrial distributor patterns (Grainger, MSC) where part-number search is a primary workflow.

### Navigation

**`nav-top-utility`** — A 36px tall slim bar above the main nav in a darker `{colors.primary-active}` blue. Carries phone number, account login, and cart links in `{typography.caption}` white. Common on B2B industrial sites to surface phone support above the fold for buyers who won't complete online.

**`nav-bar`** — The main navigation rides on `{colors.surface-dark}` (#313131 charcoal), logo left, search bar center, cart/account right. 56px tall. The dark background against a likely white canvas creates a hard-band separation — no blurring or transparency effects. Category links drop to `nav-category-strip` below.

**`nav-category-strip`** — A 44px secondary row on `{colors.canvas}` holding category anchors (Cleanroom, HVAC, Filtration, etc.) in `{typography.nav-link}`. A bottom hairline divides it from the content area. Active category uses an underline in `{colors.primary}`.

### Product Cards

**`product-card`** — Bordered `{colors.hairline}` rectangle at `{rounded.xs}`, 1px border lifts to `{colors.primary}` on hover with a soft 2px box shadow. Image at 4:3 ratio sits above a tight data block: part number in `{typography.part-number}` (monospace, muted), product title in `{typography.title-sm}`, price in `{typography.price-lg}`, and an add-to-cart button. Stock badges (`badge-in-stock`, `badge-sale`) overlay the image corner in 2px×6px pill chips.

### Spec Table

**`spec-table`** — Two-column table with `{colors.surface-soft}` header rows and alternating white rows, `{colors.hairline}` borders on all cells. Labels render in `{typography.spec-label}` (11px, uppercase, 800ms letter-spacing) in `{colors.muted}`; values render in `{typography.body-sm}` in `{colors.ink}`. This is the primary information unit for HVAC equipment specs (CFM, BTU, MERV rating, voltage) — structured for scannable comparison, not narrative prose.

### Filter Sidebar

**`filter-sidebar`** — 240px fixed-width panel in `{colors.surface-soft}` with a right hairline border. Filter groups use `{typography.title-sm}` headings and `filter-checkbox-active` inputs with `{colors.primary}` accent. Collapsed groups show a chevron icon. On tablet, the sidebar converts to a horizontal filter strip above the product grid.

### Footer

**`footer`** — Full-width charcoal band (`{colors.surface-dark}`) in 3–4 columns: links, contact, certifications, and newsletter signup. Link color uses a desaturated blue (`#a8c8e8`) against the dark ground for contrast without full white brightness. Heading labels in `{typography.title-sm}` white, body links in `{typography.body-sm}`.

### Trust Badges

**`trust-badge`** — Row of 3–4 horizontal chips below the hero or in the nav band, each pairing an icon in `{colors.primary}` with a short bold label ("Free Shipping", "Factory Direct", "Certified HVAC"). 1px hairline border, `{rounded.xs}`, compact padding at `{spacing.sm}` vertical.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter sidebar collapses to a modal drawer triggered by "Filter" button; nav-top-utility hides; search bar moves into hamburger menu; trust badges stack vertically; breadcrumb truncated to 2 levels |
| Tablet | 744–1128px | 2-column product grid; filter sidebar converts to horizontal chip strip above grid; nav-category-strip wraps to 2 rows if needed; search bar remains visible in header |
| Desktop | 1128–1440px | 3-column product grid; filter sidebar shows at 240px fixed width left of grid; full nav with category strip; trust-badge row visible below hero |
| Wide | > 1440px | Grid max-width ~1360px centered with auto side margins; 4-column product grid optional; spec table expands to show additional columns |

### Touch Targets

- All primary buttons minimum 44px height on mobile
- Filter checkboxes padded to 44px tap height via increased row padding
- Search submit button widens to full-width below search field on mobile
- Pagination buttons minimum 44×44px, increased to 10px gap between items

### Collapsing Strategy

- Nav: hamburger at < 744px, all category links in slide-out drawer; logo and cart icon remain visible
- Filter sidebar: drawer modal on mobile, chip strip on tablet, persistent sidebar on desktop
- Spec table: horizontal scroll container on mobile with sticky first column (label)
- Product card: image above fold, data below; part number hidden on narrowest breakpoint
- Category hero: height collapses from 220px to 140px on mobile; display type scales from `{typography.display-md}` to `{typography.display-sm}`

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Site behind Cloudflare anti-bot protection** — the page title returned "Just a moment…" indicating extraction hit a challenge page, not the actual storefront. Only one hex color (#313131) was recovered.
- **Primary brand color unconfirmed** — the inferred blue (`#1a5fa8`) and accent orange (`#e05c00`) are derived from industrial HVAC e-commerce conventions, not extracted pixels. Verify against a live crawl.
- **No custom typeface detected** — the entire font stack is system UI. It is possible a custom webfont loads asynchronously after JS executes; a JS-enabled crawl would confirm or deny.
- **No theme-color meta tag** — prevents mobile browser chrome from confirming brand color.
- **Logo dimensions and lockup unknown** — unable to determine whether the logo is text-only, icon+wordmark, or how it sizes across breakpoints.
- **Color palette depth unknown** — secondary colors, alert states, and promotional colors are all inferred. The hairline, surface-soft, and muted tokens are standard defaults, not observed values.
- **Checkout and account UI unseen** — B2B industrial sites often have quote-request flows, purchase-order input, and net-30 account dashboards that require separate token considerations not modeled here.
- **Icon style unknown** — whether the site uses outline, filled, or custom industrial glyphs could not be determined from the blocked extraction.
