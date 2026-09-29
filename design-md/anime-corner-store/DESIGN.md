---
version: alpha
name: "Anime Corner Store"
source_url: "https://www.animecornerstore.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A high-voltage collector's marketplace that wears its fandom on its sleeve, where #ffff99 (a warm, almost buttery yellow) saturates the page background like sunlight through a shojo manga panel, while #0000ff — a pure, unapologetic primary blue — anchors every link and interactive element with the confidence of a shonen protagonist. The palette is unapologetically bright: #ffff00 and #ffff66 extend the yellow family into highlights and hover states, #ff9933 and #ff9900 bring a burnt-orange accent for sale tags and category badges, and #ffffa0 softens the canvas for card surfaces. Typography runs Arial at modest sizes — there is no custom brand typeface, no variable font, just the workhorse sans-serif that has powered the web since the 90s, set at 12–14px for body copy and 16–18px for navigation links, with bold weights doing the work that color alone cannot. The navigation is a dense horizontal strip of category links — Figurines, DVDs, Soundtracks, Apparel, Books, Manga, Yaoi — each separated by pipe characters and underlined on hover with that same #0000ff, creating a visual rhythm that feels like a well-worn bookmark. Product cards stack in a tight grid with thin #ffffa0 borders and generous internal padding, each featuring a thumbnail, a truncated title in bold blue link text, and a price in #ff9933. The search bar is a simple text input with a yellow background and blue border, no pill rounding, no icon — just a functional gateway into a catalog that spans thousands of SKUs. The overall effect is nostalgic, earnest, and utterly unpretentious: a store that prioritizes inventory density and clear information hierarchy over visual polish, where the yellow canvas is both a brand signature and a practical choice for making blue links pop.

colors:
  primary: "#0000ff"
  primary-active: "#0000cc"
  primary-disabled: "#9999ff"
  ink: "#000000"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  canvas: "#ffff99"
  surface-soft: "#ffffa0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#ff9933"
  accent-warm-active: "#ff9900"
  accent-highlight: "#ffff00"
  accent-highlight-soft: "#ffff66"
  link-visited: "#800080"
  price: "#ff9933"
  badge-sale: "#ff0000"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
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
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
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
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-secondary-active:
    backgroundColor: "{colors.accent-warm-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 6px 10px
    height: 32px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: auto
    padding: "{spacing.sm} {spacing.base}"
  nav-link:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    textDecoration: none
  nav-link-hover:
    textColor: "{colors.primary-active}"
    textDecoration: underline
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-thumbnail:
    width: 100%
    height: auto
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.link}"
    textColor: "{colors.primary}"
    margin: "{spacing.xs} 0"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.price}"
    fontWeight: 700
  badge-new:
    backgroundColor: "{colors.accent-highlight}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 32px
    border: "1px solid {colors.primary}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    outline: none
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.lg} {spacing.base}"
    border-top: "1px solid {colors.hairline}"
  footer-link:
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    textDecoration: underline
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} 0"
    border-bottom: "1px solid {colors.hairline}"
  category-link:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    textDecoration: none
    padding: "0 {spacing.sm}"
  category-link-hover:
    textColor: "{colors.primary-active}"
    textDecoration: underline
  page-title:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    margin: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in pure #0000ff with white text and 4px border radius. Used for "Add to Cart", "Checkout", and "Submit" actions. On hover, shifts to #0000cc. When disabled, fades to #9999ff with reduced opacity.

**`button-secondary`** — An orange-toned alternative button using #ff9933, reserved for "View Details", "Pre-Order", and "Notify Me" actions. On hover, deepens to #ff9900. Shares the same 36px height and 8px 16px padding as the primary button.

### Navigation
**`nav-bar`** — A full-width horizontal strip on the #ffff99 canvas background, containing category links separated by pipe characters. The bar has no fixed height — it wraps naturally as categories are added. Each link is #0000ff, bold Arial at 13px, with underline on hover.

**`nav-link`** — Standard navigation link in #0000ff, no underline by default, underline on hover. Visited links turn #800080. Active page links may be rendered without underline but with a slightly darker blue.

**`category-strip`** — A secondary navigation row below the main nav, listing subcategories or featured sections. Uses the same pipe-separated link pattern as the main nav but with slightly smaller spacing.

### Cards
**`product-card`** — A white card on the #ffff99 canvas, bordered with #e0e0e0. Contains a thumbnail image (full width, auto height), a truncated product title as a blue link, and a price in bold #ff9933. No border radius — the card is a simple rectangle. Internal padding is 8px.

**`product-card-title`** — The product name, rendered as a 13px blue link with underline. Truncated to one line with ellipsis for long titles.

**`product-card-price`** — The price display in bold 14px #ff9933. Sale prices may be shown in #ff0000 with the original price struck through in #999999.

### Badges
**`badge-new`** — A small yellow (#ffff00) badge with black text, 4px border radius, used to flag newly added products. Text is bold 11px Arial.

**`badge-sale`** — A red (#ff0000) badge with white text, same dimensions as the new badge. Used for clearance or discounted items.

### Forms
**`text-input`** — Standard text input field with white background, 1px #cccccc border, 4px border radius, and 32px height. On focus, the border becomes 2px solid #0000ff with no outline.

**`search-bar`** — A dedicated search input with #ffffa0 background and #0000ff border, 32px height. On focus, the border thickens to 2px. No search icon — just a plain text field.

### Footer
**`footer`** — A full-width footer on the #ffff99 canvas with a top border of #cccccc. Contains copyright text in #666666 and a row of blue links for "About Us", "Site Help", "Privacy Policy", and "Contact". Links are underlined by default.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Navigation collapses to a single row of top-level categories with a "More" dropdown. Product cards stack in a single column. Search bar moves below the nav. Footer links stack vertically. |
| Tablet | 744–1128px | Navigation shows two rows of categories. Product cards display in a 2-column grid. Search bar remains in the header. Footer links display in two columns. |
| Desktop | 1128–1440px | Full navigation bar with all categories visible. Product cards in a 3-column grid. Search bar in the header. Footer links in a single row. |
| Wide | > 1440px | Maximum content width of 1440px, centered. Product cards in a 4-column grid. All other elements scale proportionally. |

### Touch Targets
- All navigation links: minimum 44px tap target height
- Buttons: 36px height with 16px horizontal padding
- Product card links: entire card area is tappable
- Search bar: 32px height, but the surrounding area includes 8px padding for easier tapping

### Collapsing Strategy
- Main navigation: categories beyond the first 8 collapse into a "More Categories" dropdown on tablet and mobile
- Product grid: columns reduce from 4 to 3 to 2 to 1 as viewport narrows
- Footer links: horizontal row collapses to stacked list on mobile
- Search bar: moves from header to below the nav on mobile to maintain header compactness

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex colors are dominated by yellow tones (#ffff99, #ffff00, #ffff66, #ffffa0) and a single blue (#0000ff), with orange accents (#ff9933, #ff9900). This appears to be the brand's actual palette, but hover states for all elements could not be reliably extracted.
- Font-family extraction returned HTML fragments mixed with Arial declarations. The site appears to use Arial exclusively, but exact font sizes and weights are inferred from common patterns rather than extracted CSS.
- No meta theme-color was found, so browser chrome styling is unknown.
- The site does not appear to use Shopify or any modern e-commerce framework, so component patterns (cart drawer, checkout flow, payment forms) are not available.
- No dark mode or high-contrast mode styling was detected.
- Error states (validation, 404, empty search results) could not be extracted.
- Loading states and skeleton screens are not present in the extracted data.
- The brand's logo and its sizing/spacing rules could not be determined from the extraction.
