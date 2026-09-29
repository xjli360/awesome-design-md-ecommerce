---
version: alpha
name: "Rhodia"
source_url: "https://www.rhodiapads.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Lime green at `#72c02c` is where the entire site concentrates its color budget — a single mid-spectrum accent cutting through a strict progression of grays that runs from near-black `#080808` through charcoal `#444444`, smoke `#777777`, pale ash `#bbbbbb`, and a near-white page surface at `#f5f5f5`. Everything else is functional: hairline borders at `#eeeeee` dissolve into card backgrounds, Bootstrap-derived alert fills confirm actions in success green (`#dff0d8`), warning amber (`#fcf8e3`), danger rose (`#f2dede`), and info blue (`#d9edf7`) without emotional charge. Type runs Open Sans first, falling through Arial, Helvetica Neue, and Helvetica — a humanist sans-serif that matches the mechanical precision of Rhodia's grid-ruled paper without feeling clinical. Consolas and Courier New handle monospace contexts — product codes, ruling specifications, the small numeric data that stationery buyers read closely.

  Layout architecture descends from Bootstrap 3's twelve-column grid: `.container` max-widths, stacked-label forms, `#eeeeee` hairline input borders that nearly disappear against the `#f5f5f5` page surface. There is no hero theatrics — no full-bleed photography draped in gradient scrims, no auto-playing motion. Product photography earns its space on a clean white or light-gray stage so the physical object — pad weight, cover color, ruling fineness — can do the persuading. Each product card carries its ruling system (dot, graph, lined, blank) as a small typographic badge below the product name, the one editorial classification the catalog navigation does not handle on its own.

  Corners are square to barely-rounded at `{rounded.xs}` — four pixels — consistent with the hard geometry of a spiral-bound pad's trimmed edge or a French-ruled margin column. Buttons deploy the lime green against white text, a contrast that clears WCAG AA at this saturation. The navigation is horizontal and category-first, cart and account icons anchored right — a structural vocabulary closer to a library reference shelf than a lifestyle campaign. Rhodia's customers are reading gram-weight, ruling pitch, and acid-free certification rather than brand narrative, and the UI defers accordingly: section spacing is generous between product groups, economical within each grid cell.

colors:
  primary: "#72c02c"
  primary-active: "#5a9a22"
  primary-disabled: "#b8df8c"
  ink: "#080808"
  body: "#444444"
  muted: "#777777"
  muted-soft: "#9d9d9d"
  hairline: "#eeeeee"
  hairline-soft: "#e7e7e7"
  hairline-strong: "#bbbbbb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  link: "#337ab7"
  alert-success-bg: "#dff0d8"
  alert-success-text: "#3c763d"
  alert-warning-bg: "#fcf8e3"
  alert-warning-text: "#8a6d3b"
  alert-danger-bg: "#f2dede"
  alert-danger-text: "#a94442"
  alert-info-bg: "#d9edf7"
  alert-info-text: "#31708f"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  button-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  mono-sm:
    fontFamily: "Consolas, 'Courier New', Menlo, Monaco, monospace"
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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "10px 20px"
    height: 40px
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
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "9px 19px"
    height: 40px
    border: "1px solid {colors.hairline-strong}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "9px 19px"
    border: "1px solid {colors.primary}"
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    height: 36px
    border: "1px solid {colors.hairline-strong}"
    borderFocus: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted-soft}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    height: 36px
    border: "1px solid {colors.hairline-strong}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 50px
    borderBottom: "1px solid {colors.hairline}"
    linkHoverColor: "{colors.primary}"
    activeColor: "{colors.primary}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"
    itemHoverBackground: "{colors.surface-soft}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    imagePadding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.body}"
    padding: "{spacing.base}"
    hoverBorderColor: "{colors.hairline-strong}"
  paper-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
    border: "1px solid {colors.hairline}"
  ruling-type-label:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  hero-strip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
    borderBottom: "1px solid {colors.hairline}"
  category-nav:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    activeTextColor: "{colors.primary}"
    activeBorderBottom: "2px solid {colors.primary}"
    itemPadding: "10px {spacing.base}"
  product-detail-meta:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-md}"
    codeTypography: "{typography.mono-sm}"
    codeColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    separatorColor: "{colors.hairline-strong}"
    activeColor: "{colors.body}"
  alert-success:
    backgroundColor: "{colors.alert-success-bg}"
    textColor: "{colors.alert-success-text}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline-strong}"
    rounded: "{rounded.xs}"
    padding: "12px {spacing.base}"
  alert-warning:
    backgroundColor: "{colors.alert-warning-bg}"
    textColor: "{colors.alert-warning-text}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline-strong}"
    rounded: "{rounded.xs}"
    padding: "12px {spacing.base}"
  alert-danger:
    backgroundColor: "{colors.alert-danger-bg}"
    textColor: "{colors.alert-danger-text}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline-strong}"
    rounded: "{rounded.xs}"
    padding: "12px {spacing.base}"
  footer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.link}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} 0"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.body}"

## Components

### Buttons

**`button-primary`** — The lime-green primary button (`#72c02c` fill, white text, `{rounded.xs}` corners) is deployed for all purchase-intent actions: Add to Cart, Checkout, Submit. At 40px height with 10px 20px padding it reads as a utility element rather than a marketing statement — no shadow, no gradient, no uppercase treatment. Hover and active states darken to `{colors.primary-active}` (`#5a9a22`); disabled fades to `{colors.primary-disabled}` (`#b8df8c`) with a not-allowed cursor.

**`button-secondary`** — White fill with a `{colors.hairline-strong}` (`#bbbbbb`) border and `{colors.body}` text. Paired with `button-primary` for two-action rows (e.g., Continue Shopping alongside Checkout), identical in height so the pair aligns cleanly. Hover lightens the border to `{colors.hairline-soft}`.

**`button-ghost`** — Transparent fill, `{colors.primary}` border and label. Used for secondary CTAs on light-background panels where a filled button would compete with the primary hierarchy — for example, a "Learn More" alongside a filled "Buy Now".

**`button-sm`** — Compact 32px version of `button-primary`. Same lime-green fill and `{rounded.xs}` corners; deployed for in-card Quick Add actions and filter submission buttons where space is constrained.

### Form Controls

**`text-input`** — 36px height, `{rounded.xs}` corners, `{colors.hairline-strong}` border that shifts to `{colors.primary}` on focus without a box-shadow. Labels stack above inputs per Bootstrap 3 form conventions. Placeholder text renders in `{colors.muted-soft}` (`#9d9d9d`). Background is `{colors.canvas}` so the white field reads cleanly against `{colors.surface-card}` page backgrounds.

**`select-input`** — Matching dimensions and border behavior to `text-input`. Deployed on product detail pages for format selectors (A4, A5, No. 16, Rhodiarama) and ruling type choices. No custom dropdown arrow styling was detected — relies on the browser native control.

### Navigation

**`nav-bar`** — White, 50px tall, with a 1px `{colors.hairline}` bottom border. Category links in `{typography.nav-link}` (Open Sans 14px/600) turn `{colors.primary}` on hover. Cart and account links right-aligned via Bootstrap's `navbar-right` pattern. Collapses to a hamburger toggle (Bootstrap `.navbar-toggle`) below 768px. No sticky behavior.

**`nav-dropdown`** — White panel with `{colors.hairline}` border and `{rounded.xs}` corners, appearing below hovered category links. Items use `{typography.body-md}` and shift to `{colors.surface-soft}` background on hover — a minimal hover state that does not interrupt the scan.

**`category-nav`** — A secondary horizontal strip below the main nav on catalog and category pages. Lists sub-categories (Graph, Dot Grid, Lined, Blank, by cover color). Active item displays `{colors.primary}` text with a 2px solid `{colors.primary}` bottom border. Functions as a filter rail at desktop; becomes a horizontally scrollable strip on mobile.

**`breadcrumb`** — Compact `{typography.body-sm}` trail in `{colors.muted}` with `>` character separators in `{colors.hairline-strong}`. Final active crumb uses `{colors.body}`. No background, no border — purely navigational prose.

### Product Card

**`product-card`** — White card with 1px `{colors.hairline}` border and `{rounded.xs}` corners. On hover the border lifts to `{colors.hairline-strong}`. The product image occupies the upper portion with `{spacing.base}` internal padding. Below: product name in `{typography.title-sm}`, a format/size line in `{typography.body-sm}`, the `paper-badge` ruling chip, and finally the price in `{typography.price}` (18px/700). A `button-sm` Add to Cart anchor sits at the card base.

**`paper-badge`** — A small flat chip showing the ruling type: "DOT GRID", "GRAPH", "LINED", "BLANK", or a product series designation like "N°5 PAD". No fill beyond `{colors.surface-soft}`, a `{colors.hairline}` border, and `{typography.badge}` (11px, uppercase, 0.5px tracking). Corners are `{rounded.none}` — the square edge reinforces the precision-instrument register of the ruling vocabulary.

**`ruling-type-label`** — Inline text in `{typography.caption}` / `{colors.muted}` used on the product detail page to label ruling pitch or grid specification (e.g., "5mm ruling", "3.5mm dot spacing"). Not a chip — just a prose-weight metadata line that follows the product name hierarchy.

### Product Detail

**`product-detail-meta`** — A `{colors.surface-soft}` panel with `{colors.hairline}` border listing product specifications: sheet size, page count, cover weight (g/m²), paper weight (g/m²), acid-free status, and SKU. Labels in `{typography.caption}`, values in `{typography.body-md}`, the product SKU rendered in `{typography.mono-sm}` (Consolas) to signal it is a lookup code rather than editorial text. Padding `{spacing.base}` on all sides; `{rounded.xs}` corners.

### Hero

**`hero-strip`** — A low-drama `{colors.surface-card}` band spanning full container width. Heading in `{typography.display-xl}` (Open Sans 36px/700), body copy in `{typography.body-md}`. No background image — photography appears in the adjacent product grid rather than behind type. A single `button-primary` CTA. A 1px `{colors.hairline}` bottom border separates it from the catalog grid below.

### Alerts

**`alert-success`**, **`alert-warning`**, **`alert-danger`** — Bootstrap 3 alert pattern: colored fill from the corresponding `{colors.alert-*-bg}` token, text in `{colors.alert-*-text}`, `{rounded.xs}` corners, 1px `{colors.hairline-strong}` border. Used respectively for cart confirmation ("Item added"), stock caution ("Only 3 left"), and checkout errors. No custom icons — FontAwesome glyphs from the Bootstrap bundle serve as prefixes.

### Footer

**`footer`** — `{colors.surface-card}` background, 1px `{colors.hairline}` top border, `{spacing.section}` vertical padding. Section headings in `{typography.title-sm}` / `{colors.body}`. Link columns in `{typography.body-sm}` / `{colors.link}` (`#337ab7`). Copyright line in `{colors.muted}`. Standard four-column Bootstrap grid: About, Products, Retailers, Contact.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Hamburger nav collapse; single-column product grid; category-nav becomes horizontal scroll strip; product-detail-meta stacks label/value pairs vertically; footer columns stack to single column |
| Tablet | 768–992px | Two-column product grid; full nav links visible; category-nav fully rendered; hero-strip single-column prose + CTA; footer in two columns |
| Desktop | 992–1200px | Three-column product grid; nav dropdowns active; category-nav as filter rail; hero-strip with generous side padding |
| Wide | > 1200px | `.container` caps at 1170px (Bootstrap 3 default); four-column product grid; wide margins fill remaining viewport; no further layout changes |

### Touch Targets

- `button-primary` and `button-secondary` at 40px height meet the 40px minimum for primary actions
- `button-sm` at 32px is used only for in-card secondary actions; maintain at least 8px gap to adjacent targets
- `text-input` and `select-input` at 36px are adequate for thumb interaction; avoid grouping more than two inputs in a single row on mobile
- Nav-bar at 50px height provides sufficient tap area for all nav links without additional padding adjustments

### Collapsing Strategy

- Primary nav collapses to Bootstrap `.navbar-toggle` hamburger below 768px; all category and utility links move into a vertical off-canvas or accordion drawer
- `category-nav` subcategory strip shifts to horizontal scroll with `-webkit-overflow-scrolling: touch` on mobile; active pill remains visible at scroll position 0
- Product grid reflows 4 → 3 → 2 → 1 column via Bootstrap responsive grid classes across breakpoints
- `product-detail-meta` spec panel reflows from two-column label/value layout to single-column stacked list at mobile
- Footer reflows from four columns to two at tablet, single column at mobile; heading/links remain visually grouped per section

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Rhodia's physical product identity features a prominent orange cover color (approximately #E65100–#E87722) that does not appear in the extracted palette; orange is likely present only in product photography rather than CSS, meaning the digital primary accent (`#72c02c` lime green) and the physical brand primary are non-identical
- The extracted palette contains numerous colors that match Bootstrap 3 default alert and component variables exactly (`#3c763d`, `#8a6d3b`, `#a94442`, `#5cb85c`, `#5bc0de`, `#f0ad4e`, `#d9534f` and their tinted variants); these likely survived the framework filter and do not represent intentional brand choices beyond a Bootstrap base
- Active and disabled state colors for `button-primary` were derived by hue-preserving lightness adjustment from `#72c02c`; exact computed values were not confirmed from source CSS
- No custom typeface detected; Open Sans is confirmed loaded but the specific weight subset (300 / 400 / 600 / 700) was not captured — some weights may not be loaded, affecting bold display rendering
- No brand-specific icon set identified beyond FontAwesome (Glyphicons Halflings in the extracted stacks, consistent with Bootstrap 3 bundled icons); cart, wishlist, and account icon SVGs not inspected
- CSS transition timing for card hover, button states, and dropdown animation not captured
- Mobile hamburger drawer animation style (slide, fade, overlay) not confirmed from extraction
- Container max-width and gutter widths assumed to be Bootstrap 3 defaults (1170px container, 30px gutters); not confirmed from source
