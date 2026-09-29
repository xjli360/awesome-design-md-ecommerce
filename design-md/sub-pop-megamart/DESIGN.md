---
version: alpha
name: "Sub Pop Megamart"
source_url: "https://megamart.subpop.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record label merch store that wears its black-on-black-on-black palette like a stage uniform — `#231f20` (a near-black with a whisper of brown warmth, not pure `#000`) is the background for the entire shopping experience, while `#dedede` silver-gray provides the only text and linework, and `#121212` (a colder, deeper black) appears in product-image shadows and footer blocks. The brand makes zero attempt at "retail warmth": no white canvas, no pastel accents, no lifestyle photography. Instead, product thumbnails sit on `#231f20` like artifacts in a vitrine, with `{rounded.xs}` (4px) corners that feel more functional than friendly — just enough to keep edges from cutting. The single visual voltage comes from album art and band logos, which are allowed to be full-color, fluorescent, or metallic; the store frame itself stays out of the way. Typography is a single sans-serif at moderate weights — no display face, no italic, no uppercase navigation — and the cart icon is a simple SVG outline in `#dedede`. The checkout flow (Shopify-powered) introduces its own blue and green buttons, but those are clearly widget intrusions, not brand decisions. Sub Pop Megamart is a dark room with a spotlight on the records.

colors:
  primary: "#231f20"
  primary-active: "#121212"
  primary-disabled: "#3a3637"
  ink: "#dedede"
  body: "#dedede"
  muted: "#9a9a9a"
  muted-soft: "#6a6a6a"
  hairline: "#3a3637"
  hairline-soft: "#2d2a2b"
  canvas: "#231f20"
  surface-soft: "#2d2a2b"
  surface-card: "#1c1a1b"
  on-primary: "#dedede"
  on-dark: "#dedede"
  accent-album: "#ffffff"
  badge-new: "#e0e0e0"
  badge-sale: "#dedede"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.ink}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
  button-secondary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 0px
  product-card-image:
    backgroundColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.sm} 0"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    padding: "{spacing.xs} {spacing.sm} {spacing.sm}"
  badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  badge-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
    border: "1px solid {colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
    borderTop: "1px solid {colors.hairline}"
  cart-icon:
    textColor: "{colors.ink}"
    height: 24px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 36px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary action button on a dark canvas. Uses the same `#231f20` as the background but is distinguished by a `1px solid #dedede` outline and uppercase sans-serif text. On hover (`button-primary-active`), the background shifts to `#121212` for a subtle dark-on-dark depth cue. Disabled state (`button-primary-disabled`) drops to `#3a3637` background with `#6a6a6a` text, making the button recede into the interface.

**`button-secondary`** — The inverted variant: `#dedede` silver fill with `#231f20` text. Used for "Add to Cart" on product pages where the primary button would blend into the card background. Same uppercase 14px/600 weight typography and zero border-radius — no softening anywhere.

**`button-ghost`** — A text-only button with no background or border. Used for "Cancel" in modals, "Clear" in search, and secondary navigation links. Inherits the same uppercase button typography but sits flush against the dark canvas.

### Cards
**`product-card`** — A minimal container for album/merch listings. Uses `#1c1a1b` (`surface-card`) — slightly darker than the `#231f20` canvas — to create a subtle product-zone separation without a visible border. The product image occupies a 1:1 square with `{rounded.xs}` (4px) corners. Title and price stack below with no padding between them, keeping the card compact.

**`product-card-image`** — The square album-art or product-photo area. Background defaults to `#121212` for images that don't fill the frame. The 4px radius is the only rounding in the entire card — no pill shapes, no soft corners.

### Navigation
**`nav-bar`** — A 60px fixed-height bar at the top of every page. Background matches the canvas (`#231f20`), with a single `1px solid #3a3637` bottom border as the only separation. Navigation links use 14px/500 weight sans-serif with no uppercase transformation. The active link (`nav-link-active`) gets a `2px solid #dedede` bottom border — the only underline in the system.

### Forms
**`text-input`** — A dark-field input on `#2d2a2b` (`surface-soft`) with `1px solid #3a3637` border. Text appears in `#dedede` at 16px/400. On focus, the border switches to `#dedede` — the only focus indicator in the system. No rounded corners, no placeholder styling beyond the same muted gray.

**`search-bar`** — A compact 40px input for the site search. Same dark-field treatment as `text-input` but with tighter padding. Sits in the nav bar or a dedicated search page.

### Badges
**`badge`** — A solid silver (`#dedede`) label with black (`#231f20`) text. Used for "NEW" or "SALE" markers on product cards. Zero border-radius, uppercase 11px/700. The badge sits directly on the product image or card, never floating with a shadow.

**`badge-outline`** — An outlined variant for "PRE-ORDER" or "EXCLUSIVE" tags. Transparent background with a `1px solid #dedede` border and silver text. Same typography and zero rounding.

### Footer
**`footer`** — A dark-on-dark footer block on `#121212` background. Text is `#6a6a6a` (`muted-soft`) at 14px/400 — intentionally low contrast to keep the footer from competing with product content. A `1px solid #3a3637` top border separates it from the main content area. Links within the footer use the standard `link` typography.

### Cart
**`cart-icon`** — A simple SVG outline of a shopping bag or cart, rendered in `#dedede`. 24px height, no fill, no badge dot — the only indicator is the item count rendered as a `badge` next to the icon.

**`quantity-selector`** — A compact 36px control for adjusting cart item quantities. Uses the same dark-field (`#2d2a2b`) and `1px solid #3a3637` border as text inputs. Buttons for increment/decrement are simple `+` and `−` glyphs in `#dedede`, with no background change on hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 column), nav collapses to hamburger, search bar moves below nav, footer stacks vertically, product cards full-width |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, search bar in nav, footer in two columns |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, search bar in nav, footer in three columns |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, extra whitespace on sides |

### Touch Targets
- All buttons and interactive elements: minimum 44px height (WCAG 2.2 compliant)
- Cart icon and quantity selector buttons: minimum 44x44px tap area (icon may be smaller but padded)
- Nav links on mobile: 48px tap height for easy finger targeting
- Search bar: 40px height on desktop, 48px on mobile for touch

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows
- Footer sections stack vertically on mobile (single column)
- Search bar moves from inline nav position to full-width below nav on mobile
- Product card images maintain 1:1 aspect ratio at all breakpoints

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were found on the live site — the system font stack `'Helvetica Neue', Helvetica, Arial, sans-serif` is inferred from common Shopify defaults and should be verified against the brand's actual design tokens
- Only three hex colors were extracted from the live site (`#231f20`, `#dedede`, `#121212`) — all other colors in the palette (muted grays, surface variants, badge colors) are interpolated from these three and may not match the brand's actual secondary palette
- Hover and focus states for most components are inferred from common dark-theme patterns — the actual brand may use different transitions, color shifts, or micro-interactions
- Error styling (form validation, out-of-stock indicators, error messages) was not observed on the live site
- The Shopify checkout flow introduces its own blue (`#007aff`) and green (`#34c759`) button colors that are not part of the Sub Pop brand — these should be overridden or accepted as widget defaults
- No typography scale was found — all font sizes, weights, and line heights are estimated from common e-commerce patterns on a dark theme
- No spacing or rounded token values were extracted — all values are based on standard design-system conventions for a minimal dark storefront
- Dark mode is not applicable (the site is already dark by default), but no light mode or high-contrast variant was observed
- No animation or transition timing data was captured (hover fades, page transitions, loading states)
- The brand may use a custom font (e.g., Sub Pop's own typeface) that was not detected in the CSS extraction
