---
version: alpha
name: "Science Company"
source_url: "https://www.sciencecompany.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Laboratory safety green — #117744, deep as a fume hood indicator — anchors every primary action on sciencecompany.com, a palette choice that reads less like brand strategy and more like institutional habit: the same green that marks "safe exit" and "eyewash station" now marks "Add to Cart." The second extracted color, a pure #ff0000 with no warm or cool offset, functions as the system's alarm register: required-field markers, out-of-stock notices, sale-price deltas. Together the two chromatic signals mirror the binary of a lab environment — proceed or stop — with no decorative third tone in between.

  The type stack is conspicuously institutional: Calibri sits at the sans-serif slot (Microsoft Office's default since 2007), while Cambria Math occupies the serif role, a font designed specifically to render chemical formulas and mathematical notation at screen resolution. Times New Roman appears as the fallback roman. This is not a typographic system assembled for brand expression; it is the stack of a catalog built by scientists for scientists, where legibility of unit abbreviations (mL, µL, mmol/L) and CAS registry numbers at small sizes matters more than display charisma. The "swiss" and "roman" entries in the font-family strings are generic CSS category names, confirming the type system never reached a font-selection phase — it simply inherited browser and OS defaults.

  Navigation relies on a dense category tree — chemicals, glassware, safety equipment, pH meters, microscopes — organized as a flat mega-menu rather than progressive disclosure. Product cards carry SKU identifiers, unit-price breaks for bulk purchasing, and SDS (Safety Data Sheet) badge links, prioritizing compliance information over lifestyle imagery. The canvas is white with minimal surface differentiation; the design system's job is to stay out of the way of a catalog with thousands of SKUs and let the green primary carry all wayfinding. Buttons are utilitarian rectangles rather than rounded pill shapes, reinforcing the functional-over-expressive ethos. The overall register is that of a government lab supply catalog translated to e-commerce with minimal aesthetic intervention — a coherence that communicates reliability to a customer base that values reproducibility above all.

colors:
  primary: "#117744"
  primary-active: "#0d5c35"
  primary-disabled: "#8bbba3"
  primary-light: "#e8f4ee"
  danger: "#ff0000"
  danger-soft: "#ffe5e5"
  ink: "#222222"
  body: "#444444"
  muted: "#777777"
  hairline: "#cccccc"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-header: "#f0f0f0"
  on-primary: "#ffffff"
  link: "#117744"
  link-visited: "#0d5c35"
  sale-price: "#ff0000"
  sku-label: "#555555"

typography:
  display-xl:
    fontFamily: "Calibri, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "Calibri, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "Calibri, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Calibri, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "Calibri, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Calibri, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Calibri, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "Calibri, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  scientific-label:
    fontFamily: "'Cambria Math', Cambria, 'Times New Roman', Times, serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  sku:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  button-md:
    fontFamily: "Calibri, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "Calibri, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "Calibri, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "Calibri, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Calibri, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 10px
  xl: 16px
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
    padding: 9px 18px
    height: 38px
    border: none
  button-primary-hover:
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
    padding: 8px 17px
    height: 38px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 42px
    width: "100%"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 6px 10px
    height: 34px
    border: "1px solid {colors.hairline}"
    focus-border: "1px solid {colors.primary}"
  quantity-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 6px 8px
    height: 34px
    width: 60px
    border: "1px solid {colors.hairline}"
    textAlign: center
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 38px
    border: "1px solid {colors.hairline}"
    focus-border: "1px solid {colors.primary}"
    placeholder-color: "{colors.muted}"
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 38px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-top-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 30px
    paddingX: "{spacing.lg}"
  category-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderTop: "1px solid {colors.hairline}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    shadow: "0 4px 8px rgba(0,0,0,0.1)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    hover-border: "1px solid {colors.primary}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.link}"
    hover-textDecoration: underline
  product-card-sku:
    typography: "{typography.sku}"
    textColor: "{colors.sku-label}"
    marginTop: "{spacing.xs}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.price-display}"
    textColor: "{colors.sale-price}"
  product-card-original-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  sds-badge:
    backgroundColor: "{colors.danger-soft}"
    textColor: "{colors.danger}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
    border: "1px solid {colors.danger}"
    fontWeight: 600
  hazard-badge:
    backgroundColor: "#fff3cd"
    textColor: "#856404"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
    border: "1px solid #ffc107"
  bulk-pricing-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    header-backgroundColor: "{colors.primary}"
    header-textColor: "{colors.on-primary}"
    header-typography: "{typography.title-sm}"
    row-hover-backgroundColor: "{colors.primary-light}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    separator: "/"
    active-textColor: "{colors.ink}"
    link-textColor: "{colors.link}"
  category-sidebar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderRight: "1px solid {colors.hairline}"
    paddingX: "{spacing.md}"
    active-textColor: "{colors.primary}"
    active-fontWeight: 600
  required-field-marker:
    textColor: "{colors.danger}"
    typography: "{typography.body-sm}"
    content: "*"
  footer:
    backgroundColor: "{colors.surface-header}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.lg}"
    link-textColor: "{colors.link}"

## Components

### Buttons

**`button-primary`** — A flat, low-radius rectangle (#117744 fill, white text) that functions as the principal call to action across the catalog. Hover darkens the fill to `{colors.primary-active}` (#0d5c35); the shape does not animate or elevate. Disabled state washes out to `{colors.primary-disabled}` with suppressed cursor — no ghost or outline variant is used for disabled. The height is 38px rather than the 44-48px common in consumer DTC, reflecting a density-optimized catalog context where many actions compete on one page.

**`button-secondary`** — Outlined variant using the same green as a border and text color against a white fill. Hover applies a light green wash (`{colors.primary-light}`) to confirm the affordance without inverting to solid fill. Used for secondary actions like "View Details," "Add to Wishlist," and comparison controls alongside the primary `button-cart`.

**`button-cart`** — Full-width primary button specialized for the product page add-to-cart action. Shares styling with `button-primary` but stretches to fill its container column, keeping it visually prominent in a two-column product layout.

### Search

**`search-bar`** + **`search-submit`** — The search bar is the dominant UI element in the header, spanning most of the horizontal space between the logo and cart icon. It uses a hairline-bordered input with green focus ring and a solid green submit button affixed to the right end, forming a compound control. Placeholder text is muted gray. This pattern mirrors traditional e-commerce catalog search rather than the floating pill-shaped search of consumer lifestyle brands.

### Navigation

**`nav-bar`** — White background, 60px tall, separated from content by a hairline border. Logo anchors left; search bar occupies center; account and cart icons anchor right. No sticky behavior documented — likely static scroll. Above it, **`nav-top-strip`** is a 30px green bar carrying phone/contact or promotional copy in white caption type — a catalog convention that leads with availability rather than brand copy.

**`category-mega-menu`** — A wide flyout panel opening below the category nav items, organized as a multi-column list of subcategories. No imagery or featured-product slots; pure taxonomy navigation. Border and subtle drop shadow delineate the panel from page content.

**`category-sidebar`** — Appears on catalog listing pages as a left-rail filter/navigation tree with a light gray background. Active category item is highlighted in green text with heavier weight. Nested subcategory indentation communicates depth without icons.

### Product Card

**`product-card`** — Dense rectangular card with a hairline border and no corner radius (reflecting the zero-decoration catalog posture). On hover, the border color shifts to green as the only interactive signal. Card body includes product image, `product-card-title` (green underlined link on hover), `product-card-sku` in monospace, and price block. The SKU is visually separated in `{typography.sku}` — Courier New — making part numbers scannable in a way that Calibri at small size does not allow.

**`product-card-price`** and **`product-card-sale-price`** — Normal price renders in dark ink at 20px weight 700. When a sale exists, sale price takes `{colors.sale-price}` (#ff0000) — the only decorative use of red in the system — and original price renders in muted gray with strikethrough.

### Compliance & Safety Components

**`sds-badge`** — A small red-bordered badge reading "SDS" (Safety Data Sheet) that links to the product's regulatory documentation. The red-on-pink treatment uses the danger palette (`{colors.danger}`, `{colors.danger-soft}`) making it visually distinct from product UI without being alarming. Required on chemical product listings.

**`hazard-badge`** — An amber-toned badge for GHS hazard classification symbols and UN transport categories. Color is outside the extracted palette (amber, #856404 on #fff3cd) but is a regulatory convention rather than a brand decision.

**`bulk-pricing-table`** — A structured table showing per-unit price at quantity breaks (e.g., 1–9 / 10–49 / 50+). Header row uses the green primary as a table header background with white text; data rows alternate between white and `{colors.surface-soft}`; hovered rows apply `{colors.primary-light}`. This component is central to the B2B purchasing flow and appears on most product pages.

### Breadcrumb & Wayfinding

**`breadcrumb`** — Standard forward-slash separated trail in 13px muted gray, with ancestor links in green and current page in dark ink. No icon separator; visually recedes behind the product title.

### Footer

**`footer`** — Light gray background with hairline top border, containing link columns for customer service, policy pages, and contact information. Typography is 13px Calibri in body color; links are green without underline, gaining underline on hover. No social icon row or brand imagery — functional close to a government-agency footer.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column catalog grid; mega-menu collapses to accordion drawer; search bar moves below logo; nav-top-strip hidden; product-card stacks image above text |
| Tablet | 744–1128px | Two-column product grid; category sidebar collapses to filter toggle above grid; search bar retains header position but narrows; bulk-pricing-table scrolls horizontally |
| Desktop | 1128–1440px | Three-column product grid; full category sidebar visible in left rail; mega-menu active; header fully expanded with search spanning center zone |
| Wide | > 1440px | Content max-width capped (likely 1200px); outer margins increase; grid remains three columns; no additional layout changes detected |

### Touch Targets

- Buttons are 38px tall — below the 44px iOS recommendation; mobile views should override to min-height 44px
- Quantity input at 60px wide may require tap-target padding on mobile
- Category sidebar links require minimum 40px tap height on accordion mobile version
- SDS badge links should include at least 8px vertical padding on mobile to meet accessibility thresholds

### Collapsing Strategy

- Primary nav collapses to hamburger icon opening a full-height left-side drawer
- Mega-menu subcategories become accordion sections within the drawer
- Category sidebar becomes an off-canvas filter panel toggled by a "Filter" button above the grid
- Bulk pricing table uses horizontal scroll with visible scroll indicator rather than collapsing rows
- nav-top-strip is hidden on mobile to preserve header height for logo and hamburger

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only two hex colors extracted (#117744 and #ff0000); all neutral palette values (ink, muted, hairline, surface tones) are inferred from catalog-site conventions, not confirmed from the live site
- No brand custom typeface — the font stack is entirely system/OS fonts (Calibri, Cambria Math, Times New Roman); no hosted web font detected; font sizes and weights throughout are estimated from catalog-context norms
- No design token file, Figma library, or brand style guide publicly available to cross-reference
- Exact nav height, product grid column gaps, and card padding values not extractable from static analysis — values are estimated
- Hover and focus state animations (if any) not documented; the site likely uses browser defaults
- Dark mode support not detected; assumed light-only
- Logo treatment (wordmark vs. pictorial mark, exact sizing in header) not confirmed from extraction
- Amber hazard badge colors are regulatory convention, not extracted from the site palette
