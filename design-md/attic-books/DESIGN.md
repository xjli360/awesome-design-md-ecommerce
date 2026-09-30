---
version: alpha
name: "Attic Books"
source_url: "https://www.atticbooks.ca"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A slate-and-ink independent bookstore anchored on #7796a8 — a muted, weathered blue-grey that reads like old library walls rather than a retail brand color. The palette is drawn from the physical inventory: #231f20 (near-black ink) for body text, #dedede for soft page-like surfaces, and #8da7b6 as a secondary atmospheric tone. The brand makes no attempt to feel modern or digital-first; instead it leans into the materiality of antiquarian bookselling — dark wood shelves, aged paper, the patina of well-handled stock. The meta theme-color of #7796a8 carries across every page, and the Shopify platform is deliberately under-designed, letting the book covers, maps, and prints provide all the color the eye needs. There is no hero carousel, no lifestyle photography, no brand typography system — the site is essentially a catalog dressed in a bookstore's walls. The accent colors #3d9970 (a muted olive-green, likely for "add to cart" or stock indicators) and #ff4136 (a restrained red for sale tags or error states) appear sparingly, never competing with the inventory. The design trusts that a 19th-century map or a leather-bound Dickens folio is more compelling than any UI flourish. Corners are mostly square ({rounded.none}) or very softly broken ({rounded.xs} for inputs), reinforcing the un-softened, analog feel. The result is a bookstore that happens to have a website — not a brand that happens to sell books.

colors:
  primary: "#7796a8"
  primary-active: "#6a8a9c"
  primary-disabled: "#b8cdd8"
  ink: "#231f20"
  body: "#444444"
  muted: "#8da7b6"
  muted-soft: "#aec3cf"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#3d9970"
  accent-red: "#ff4136"
  dark-ink: "#121212"

typography:
  display-xl:
    fontFamily: "'Georgia', 'Times New Roman', 'Palatino Linotype', serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Georgia', 'Times New Roman', 'Palatino Linotype', serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Georgia', 'Times New Roman', 'Palatino Linotype', serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "'Georgia', 'Times New Roman', 'Palatino Linotype', serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Georgia', 'Times New Roman', 'Palatino Linotype', serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Georgia', 'Times New Roman', 'Palatino Linotype', serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Arial, 'Lucida Grande', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, 'Lucida Grande', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, 'Lucida Grande', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', Arial, 'Lucida Grande', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Arial, 'Lucida Grande', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Arial, 'Lucida Grande', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, 'Lucida Grande', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Helvetica Neue', Arial, 'Lucida Grande', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, 'Lucida Grande', sans-serif"
    fontSize: 14px
    fontWeight: 600
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-accent-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0px
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: 48px 24px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 4px 10px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the bookstore's slate-blue {colors.primary} with white text. Corners are square ({rounded.none}), reinforcing the analog, un-softened feel of the brand. On hover, the background shifts to {colors.primary-active} (#6a8a9c). The disabled state uses {colors.primary-disabled} (#b8cdd8) with white text, signaling the action is unavailable without visual noise.

**`button-secondary`** — A white button with {colors.ink} text and a subtle {colors.hairline} border. Used for less prominent actions like "Cancel" or "View Details". The active state fills the background with {colors.surface-soft} (#f5f5f5). No rounding — consistent with the brand's square-corner ethos.

**`button-accent-green`** — A green button using {colors.accent-green} (#3d9970), reserved for positive actions like "Add to Cart" or "In Stock" confirmations. Square corners, white text, and the same 44px height as the primary button.

**`button-accent-red`** — A red button using {colors.accent-red} (#ff4136), used sparingly for "Sale" indicators, error states, or destructive actions like "Remove from Cart". Square corners maintain the brand's unadorned visual language.

### Navigation
**`nav-bar`** — A white header bar at 64px height, containing the store name (set in serif display type) and navigation links in {typography.nav-link} — uppercase, 14px, weight 600, with 0.5px letter spacing. Links use {colors.ink} with no background or rounding. The bar becomes sticky on scroll, maintaining the same white background and height.

**`breadcrumb`** — Secondary navigation rendered in {typography.caption} (13px, weight 400) in {colors.muted} (#8da7b6). The active breadcrumb segment switches to {colors.ink} (#231f20) to indicate the current page. No separators are styled — the brand relies on standard slash characters.

### Cards
**`product-card`** — A minimal card with no background fill (transparent on white canvas) and no rounding. The card consists of a product image (on a {colors.surface-soft} placeholder background) and text below: the title in {typography.title-sm} (16px, weight 600, serif) and the price in {typography.body-md} (16px, weight 400, sans-serif). No shadow, no border — the card is simply a stacked layout of image and text.

**`product-card-badge`** — A small red badge using {colors.accent-red} with white text, positioned over the product image. Set in {typography.badge} (11px, weight 700, uppercase, 0.5px letter spacing). Square corners. Used for "Sale", "New Arrival", or "Rare" indicators.

### Forms
**`text-input`** — A white input field with a 1px {colors.hairline} border and {rounded.xs} (4px) — the only component in the system with any rounding, and even that is minimal. Text is set in {typography.body-md} (16px, weight 400). On focus, the border changes to {colors.primary} (#7796a8). Padding is 10px vertical, 12px horizontal.

**`search-bar`** — A dedicated search input matching the text-input styling: white background, {colors.hairline} border, {rounded.xs} corners, 44px height. The placeholder text uses {colors.muted} (#8da7b6). No search icon is specified — the brand may use a simple text label or a minimal SVG.

### Footer
**`footer`** — A dark footer section with {colors.ink} (#231f20) background and white text. Content is set in {typography.body-sm} (14px, weight 400). Links within the footer use {colors.muted-soft} (#aec3cf) to reduce contrast slightly against the dark background. Padding is 48px vertical, 24px horizontal.

### Pagination
**`pagination`** — Page numbers rendered in {typography.body-sm} (14px, weight 400) in {colors.body} (#444444). The active page number receives a {colors.primary} background with white text and 4px horizontal padding. No rounding — consistent with the brand's square-corner approach.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav links collapse to hamburger menu; hero section reduces padding to 32px 16px; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but may wrap; hero padding at 40px 24px |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links visible; max-width container at 1128px |
| Wide | > 1440px | Four-column product grid; content centered with max-width 1440px; additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav link tap targets are at least 44px × 44px, even if the text is smaller
- Product card images are tappable with minimum 120px height on mobile
- Search bar maintains 44px height across all breakpoints

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Footer sections stack vertically on mobile (single column)
- Breadcrumbs truncate on mobile, showing only the current and parent page
- Secondary buttons may hide on mobile, replaced by a single primary action

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extracted from the live site. The typography block uses educated guesses based on common bookstore/serif pairings (Georgia for display, Helvetica Neue for body). The actual brand may use a different serif or sans-serif.
- Hover states for buttons and links are inferred from the primary color shift; actual hover values may differ.
- Error styling for form inputs (border color, error message typography) was not extracted.
- Dark mode is not supported — the brand uses a white canvas exclusively.
- Sub-brand or seasonal color palettes (e.g., holiday promotions) were not observed.
- The extracted color list includes #3d9970 and #ff4136, which may be Shopify checkout-widget defaults (green for add-to-cart, red for sale). Their usage as brand accents is speculative.
- No spacing or rounded values were extracted from the live site; all values are inferred from common bookstore e-commerce patterns and the brand's analog aesthetic.
- Loading states, skeleton screens, and empty states were not observed.
- The brand's logo or wordmark typography was not extracted; the site may use a custom logotype.
