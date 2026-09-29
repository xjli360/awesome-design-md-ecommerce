---
version: alpha
name: "Fellowes"
source_url: "https://www.fellowes.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The amber signal of #fdb913 — a yellow sharp enough to read on product safety panels and warehouse shelving — is how Fellowes announces itself against a field of corporate navy (#234479) and machine-gray neutrals. The site operates in two registers: a deep institutional blue that handles navigation bars, section anchors, and primary CTAs, and a yellow that fires only where attention must land immediately — promotional banners, category hover states, and search submit buttons. Together the two colors replicate the brand's physical product language, where navy housings and yellow safety indicators have been the visual grammar of desktop shredders since the early 2000s.

  Segoe UI carries all type, a deliberate alignment with the Windows productivity desktop where most Fellowes equipment lives out its working life; there are no custom display faces, and the type system earns contrast through weight and size rather than any expressive letterform. Cards sit on an off-white field (#fbfbfb) with 1px hairline borders (#e0e0e0) and minimal 4px corner rounding — practical geometry that avoids both the harsh right-angle severity of industrial parts catalogs and the pill-shaped warmth of consumer lifestyle brands. The register is workbench, not boutique.

  A MDB-origin semantic palette runs underneath the brand layer — green (#14a44d) for stock availability and order confirmations, red (#dc4c64) for out-of-stock and errors, amber (#e4a11b) for low-stock urgency — which suggests the frontend builds on a Bootstrap-family component library rather than a bespoke design system. These utility colors appear throughout the catalog in badge chips, toast alerts, and inline status text, and they should be treated as functional rather than brand-expressive. The dark near-black footer (#1f1b1b) grounds the page and provides a second canvas for the yellow top-border accent stripe, restating the two-color vocabulary at the bottom of every scroll. Spacing is generous for a catalog: 64px section breaks, internal card padding that lets SKU names and pricing read without crowding, and a mobile layout that keeps the yellow promo strip persistent while collapsing the nav into a drawer.

colors:
  primary: "#234479"
  primary-active: "#1a3460"
  primary-disabled: "#9fa6b2"
  accent: "#fdb913"
  accent-active: "#e4a11b"
  accent-on: "#1f1b1b"
  interactive: "#3b71ca"
  interactive-active: "#386bc0"
  ink: "#1f1b1b"
  body: "#332d2d"
  muted: "#757575"
  muted-light: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#fbfbfb"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#14a44d"
  success-dark: "#0c622e"
  error: "#dc4c64"
  error-dark: "#842e3c"
  warning: "#e4a11b"
  warning-dark: "#896110"
  info: "#54b4d3"
  info-dark: "#326c7f"
  scrim: "#262626"

typography:
  display-xl:
    fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  label-upper:
    fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  button-md:
    fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-on}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-accent-hover:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.accent-on}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    padding: 10px 14px
    typography: "{typography.body-md}"
    focusBorderColor: "{colors.interactive}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
    accentStripeColor: "{colors.accent}"
    accentStripeHeight: 3px
  nav-bar-utility:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    imagePadding: "{spacing.base}"
    bodyPadding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
  product-badge-new:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-on}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  product-badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  product-badge-bestseller:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    accentColor: "{colors.accent}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section}"
  category-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    labelTypography: "{typography.title-sm}"
    padding: "{spacing.lg}"
  category-card-hover:
    borderColor: "{colors.accent}"
    backgroundColor: "{colors.surface-soft}"
  promo-banner:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-on}"
    typography: "{typography.title-md}"
    padding: 12px "{spacing.base}"
    textAlign: center
  search-bar:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.interactive}"
    rounded: "{rounded.xs}"
    inputTypography: "{typography.body-md}"
    submitBackgroundColor: "{colors.accent}"
    submitTextColor: "{colors.accent-on}"
    height: 44px
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.muted-light}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
  alert-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
  alert-error:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
  alert-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.accent-on}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
  stock-badge-instock:
    textColor: "{colors.success}"
    typography: "{typography.caption-bold}"
  stock-badge-lowstock:
    textColor: "{colors.warning}"
    typography: "{typography.caption-bold}"
  stock-badge-outofstock:
    textColor: "{colors.error}"
    typography: "{typography.caption-bold}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    typography: "{typography.button-sm}"
    padding: 6px 14px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.hairline}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    accentBorderColor: "{colors.accent}"
    accentBorderHeight: 3px
    padding: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — The navy CTA (#234479) is the workhorse of the Fellowes interaction layer, used for "Add to Cart", "Shop Now", and most page-level CTAs. It sits at 44px height with `{rounded.xs}` (4px) corner rounding that reads as practical without any consumer friendliness; hover darkens to `{colors.primary-active}` (#1a3460). Disabled state shifts to `{colors.primary-disabled}` (#9fa6b2) with no opacity trick, keeping it crisp in dense catalog layouts.

**`button-accent`** — The yellow variant (`{colors.accent}`, #fdb913) is reserved for highest-priority moments: featured campaign CTAs, homepage "Shop Now" calls, and promotional landing pages. Text renders in `{colors.accent-on}` (#1f1b1b) for WCAG compliance against the bright background. Use sparingly — one or two per page — to preserve the yellow's attention signal across the catalog.

**`button-secondary`** — White fill with a 2px `{colors.primary}` border and matching text color. Used for secondary actions placed alongside a primary or accent CTA, such as "Compare" or "Learn More" beside an "Add to Cart". Hover fills `{colors.surface-soft}` and advances the border to `{colors.primary-active}`.

### Navigation

**`nav-bar`** — A solid navy (#234479) bar at 60px with white logotype and white nav labels in `{typography.nav-link}`. A 3px yellow accent stripe (`{colors.accentStripeColor}`) sits at the bar's bottom edge and also marks the active hover state on individual nav items, tying both brand colors into a single component. Above it, `nav-bar-utility` in `{colors.ink}` (#1f1b1b) carries locale, account, and cart links in `{typography.caption}`.

### Product Card

**`product-card`** — Cards use white fill, a 1px `{colors.hairline}` border, and `{rounded.xs}` corners, sitting on the `{colors.canvas}` (#fbfbfb) page background. Product images carry internal padding rather than edge-bleeding, giving the studio photography room to breathe. Titles render in `{typography.title-sm}`, prices in `{typography.price-display}` (24px/700). Badges (`product-badge-new`, `product-badge-sale`, `product-badge-bestseller`) are flat rectangles with `{rounded.none}` — the label-tape visual language of physical office equipment carried into the UI.

### Hero Banner

**`hero-banner`** — A full-width navy panel with headline in `{typography.display-xl}` (white) and supporting copy in `{typography.body-md}`. The `{colors.accent}` yellow appears in decorative rules, subheading highlights, or inline CTA labels to break the monochrome field without introducing a third color. Desktop layout splits image right / text left; mobile stacks full-width image above text block. Minimum height 480px with `{spacing.section}` padding.

### Category Cards

**`category-card`** — Grid tiles linking to product lines (Shredders, Laminators, Calculators, Binding) carry a 2px `{colors.hairline}` border that switches to `{colors.accent}` on hover, using the yellow as a discovery signal rather than filling the card with it. Background shifts to `{colors.surface-soft}` on hover. Labels in `{typography.title-sm}`. This hover pattern is the primary mechanism for yellow's secondary appearance in the catalog.

### Promotional Banner

**`promo-banner`** — A full-width `{colors.accent}` stripe with `{colors.accent-on}` text in `{typography.title-md}`, used for site-wide offers, shipping thresholds, and seasonal campaigns. Centered text, persistent across all breakpoints (with reduced padding on mobile). Sits above or immediately below the `nav-bar-utility` strip depending on campaign state.

### Search Bar

**`search-bar`** — White input with `{colors.hairline}` border and a yellow submit button (`{colors.accent}`), restating the navy-and-yellow vocabulary in a single component. Focus ring on the input uses `{colors.interactive}` (#3b71ca). Height 44px, `{rounded.xs}` radius. Used in the main header and, at mobile, as a full-width element inside the hamburger drawer.

### Alerts and Stock States

**`alert-success`**, **`alert-error`**, **`alert-warning`** — Toast and inline alerts use the MDB-origin semantic fills: green (#14a44d) for confirmations, red (#dc4c64) for errors, amber (#e4a11b) for cautions. White text on all three. Stock badges (`stock-badge-instock`, `stock-badge-lowstock`, `stock-badge-outofstock`) render as colored text labels only — no pill fill — using `{typography.caption-bold}` against the card background.

### Filter Chips

**`filter-chip`** / **`filter-chip-active`** — Pill-shaped chips (`{rounded.full}`) for category and feature filtering. Inactive state uses `{colors.surface-soft}` fill with `{colors.hairline}` border; active chips invert to `{colors.primary}` fill with white text. The full radius on chips is the only `{rounded.full}` usage in the system; all other interactive elements hold `{rounded.xs}`.

### Footer

**`footer`** — Near-black (#1f1b1b) with a 3px `{colors.accent}` top border that bookends the yellow from the promo banner at the top of the page. Column headings in `{typography.title-sm}`, links in `{typography.body-sm}` using `{colors.hairline}` (#e0e0e0) for reduced brightness. Social icons via Font Awesome 6. Columns collapse to accordion panels on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces `nav-bar` menu links; hero stacks to image-above-text; `promo-banner` text scales to `{typography.body-sm}`; product filters move to a modal drawer |
| Tablet | 744–1128px | Two-column product grid; secondary nav links collapse into a "More" dropdown; hero uses split layout at reduced padding; filter chips appear as a horizontal scroll row |
| Desktop | 1128–1440px | Three- or four-column product grid; full `nav-bar` with mega-menu dropdowns; hero at full 480px min-height; filter sidebar visible |
| Wide | > 1440px | Content max-width ~1400px, outer canvas stays `{colors.canvas}`; no additional layout changes |

### Touch Targets

- All buttons and nav links maintain a minimum 44×44px touch target
- Mobile hamburger button is 48×48px
- Product card tap area covers the full card face including image and label row
- Search submit button meets 44px height
- Filter chips maintain 36px minimum height with horizontal padding

### Collapsing Strategy

- `nav-bar-utility` hides on mobile; account and cart migrate into the hamburger drawer
- Mega-menu category dropdowns flatten into accordion panels inside the mobile drawer
- `promo-banner` persists across all breakpoints with padding and font scaling reduced at mobile
- Product filter sidebar collapses to a bottom-sheet modal on mobile and a drawer on tablet
- Footer columns stack vertically on mobile with accordion expand for each section; `{colors.accent}` top border remains visible at all widths

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected; Segoe UI is a Windows system font and generic `sans-serif` is the only fallback. Exact rendered font weights and sizes were estimated from standard Segoe UI conventions rather than extracted computed values.
- Meta theme-color was not set; the navy `{colors.primary}` (#234479) is assumed as the mobile chrome color based on nav background usage.
- `surface-card` (#ffffff) is inferred — the extracted palette tops out at #fbfbfb. True card-level white may differ.
- Numerous extracted colors (#14a44d, #dc4c64, #e4a11b, #54b4d3, #1266f1, #f93154, #00b74a) match MDB framework utility defaults rather than deliberate brand palette choices; they are assigned to semantic roles but may not carry brand intent.
- Exact button heights, padding values, and border radii were estimated from Bootstrap/MDB defaults rather than measured from live computed styles.
- No design token manifest, CSS custom-property file, or Figma export was accessible during extraction.
- Dark mode or alternate theme: no evidence found in extracted data.
- Icon set beyond Font Awesome (e.g. custom product-category glyphs) not confirmed from extraction.
