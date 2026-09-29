---
version: alpha
name: "Hardgraft"
source_url: "https://www.hardgraft.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A leather-goods brand that builds its entire visual identity around a single metallic thread: #ab8c52, an aged-brass gold that appears in every button, every badge, every underline, and every hover state — not as a flashy accent but as the quiet structural color of a well-worn belt buckle. The canvas is #f5f2ec, a warm off-white that reads like unbleached linen or the inside of a vintage wallet, while #212121 ink provides the deep contrast of a hand-stamped monogram. Hardgraft’s typography is a deliberate collision: the display voice is alternate-gothic-no-3-d, a compressed, muscular sans that feels like a shipping-stencil mark on a crate, while body copy runs in brandon-grotesque or davis-sans — softer, more readable, the kind of type you’d find in a small-batch catalog. The brand uses {rounded.xs} (4px) on nearly everything — buttons, cards, inputs — a radius so subtle it’s almost a chamfer, like the edge of a leather strap that’s been skived and burnished rather than cut with a laser. There are no pill shapes, no bubbly friendliness; the system is rectilinear and grounded. Product photography dominates over UI chrome: the nav is a thin strip of {colors.canvas} with {colors.ink} links, the footer is dense with legal and support links in {colors.muted} (#a49c8b), and the only decorative flourish is the gold line — a 1px {colors.primary} border that appears on hover under nav items and on the top edge of the footer. The overall mood is that of a workshop ledger: serious, material, unimpressed by trends.

colors:
  primary: "#ab8c52"
  primary-active: "#9a7e4a"
  primary-disabled: "#d3d3ca"
  ink: "#212121"
  body: "#2e2e2e"
  muted: "#a49c8b"
  muted-soft: "#b0a38b"
  hairline: "#cecec4"
  hairline-soft: "#d9d9d9"
  canvas: "#f5f2ec"
  surface-soft: "#f7f4ef"
  surface-card: "#fcfbf9"
  on-primary: "#ffffff"
  gold-accent: "#e8d4ae"
  badge-bg: "#868154"
  badge-text: "#ffffff"
  footer-bg: "#282c2e"
  footer-text: "#c0c0c0"
  error: "#c13515"
  success: "#7d784e"

typography:
  display-xl:
    fontFamily: "'alternate-gothic-no-3-d', 'big-caslon-fb', sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.5px
  display-lg:
    fontFamily: "'alternate-gothic-no-3-d', 'big-caslon-fb', sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.5px
  display-md:
    fontFamily: "'alternate-gothic-no-3-d', 'big-caslon-fb', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
  display-sm:
    fontFamily: "'alternate-gothic-no-3-d', 'big-caslon-fb', sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.5px
  title-md:
    fontFamily: "'brandon-grotesque', 'davis-sans', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  title-sm:
    fontFamily: "'brandon-grotesque', 'davis-sans', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'brandon-grotesque', 'davis-sans', 'instrument-sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'brandon-grotesque', 'davis-sans', 'instrument-sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'brandon-grotesque', 'davis-sans', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "'brandon-grotesque', 'davis-sans', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'brandon-grotesque', 'davis-sans', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'brandon-grotesque', 'davis-sans', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'brandon-grotesque', 'davis-sans', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'brandon-grotesque', 'davis-sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'brandon-grotesque', 'davis-sans', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  footer-link:
    fontFamily: "'brandon-grotesque', 'davis-sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  price:
    fontFamily: "'brandon-grotesque', 'davis-sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 0
    height: auto
  button-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-icon:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 44px
    width: 44px
  button-icon-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 1px {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 0
  product-card-image:
    rounded: "{rounded.xs} {rounded.xs} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
    padding: "0 {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.footer-link}"
    padding: "{spacing.xxl} 0"
    borderTop: "2px solid {colors.primary}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.footer-text}"
    typography: "{typography.footer-link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.gold-accent}"
    typography: "{typography.footer-link}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.gold-accent}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    color: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    border: "1px solid {colors.hairline}"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-trigger-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.title-sm}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.primary}"
    height: 2px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"

## Components

### Buttons
**`button-primary`** — The brand’s primary call-to-action, rendered in {colors.primary} (#ab8c52) with white text and a tight {rounded.xs} corner. On hover, the background shifts to {colors.primary-active} (#9a7e4a), a deeper, more burnished gold. The disabled state uses {colors.primary-disabled} (#d3d3ca), a muted gray-beige that signals the button is inert. All primary buttons use {typography.button-md} — 14px uppercase brandon-grotesque with 0.5px letter-spacing, giving them the weight of a stamped metal label.

**`button-secondary`** — An outlined variant on a {colors.canvas} background with {colors.ink} text and a 1px {colors.hairline} border. Active state swaps the border to {colors.primary}, creating a subtle gold outline. Used for “Add to Wishlist” and secondary checkout actions. Same typography and height as primary, but with 11px/23px padding to account for the border.

**`button-text`** — A borderless, backgroundless button used for inline actions like “View Details” or “Clear Cart.” Hover state shifts text color to {colors.primary}, the only visual feedback. No padding or fixed height — it flows with surrounding text.

**`button-icon`** — A 44px square icon button (cart, search, menu) with transparent background. On hover, a {colors.surface-soft} background appears and the icon shifts to {colors.primary}. The tight {rounded.xs} corner keeps it consistent with the rest of the system.

### Text Inputs & Forms
**`text-input`** — A 48px tall input on {colors.canvas} with a 1px {colors.hairline} border and {rounded.xs} corners. Focus state adds a 1px {colors.primary} border and a matching box-shadow ring. Error state swaps the border to {colors.error} (#c13515). Placeholder text uses {colors.muted-soft}. The input uses {typography.body-md} (16px brandon-grotesque) for readability.

**`select-input`** — Matches the text-input dimensions and styling, with a custom dropdown arrow in {colors.primary}. The chevron is the only decorative element — no background fill, no rounded container.

**`textarea`** — Same border and radius as text-input, but with no fixed height. Used for order notes or contact forms. Padding is 12px 16px on all sides.

### Navigation
**`nav-bar`** — A 64px fixed-height bar on {colors.canvas} with a 1px {colors.hairline-soft} bottom border. Logo sits left-aligned, navigation links are center-aligned (or right-aligned on mobile). The bar is intentionally thin — no mega-menus, no search bars embedded in the nav.

**`nav-link`** — Uppercase 13px brandon-grotesque with 0.5px letter-spacing. Active state gets a 2px {colors.primary} bottom border. Hover state shifts text to {colors.primary} without the border — the gold color alone is the signal. Padding is 8px 16px for comfortable tap targets.

### Product Cards
**`product-card`** — A white ({colors.surface-card}) card with {rounded.xs} corners and no shadow — the brand relies on the product photography for depth. The image fills the top with matching corner radius, then the title ({typography.title-sm}) and price ({typography.price}) stack below with {spacing.base} padding. Badges (sale, new, exclusive) appear as {colors.badge-bg} (#868154) rectangles with white uppercase text, positioned over the top-left of the image.

### Footer
**`footer`** — A dark section on {colors.footer-bg} (#282c2e) with {colors.footer-text} (#c0c0c0) links. The top edge is marked by a 2px {colors.primary} line — the only gold accent in the footer. Column headings use {colors.gold-accent} (#e8d4ae) in {typography.title-sm}. Links hover to the same gold. The footer is dense with 4-5 columns of links, legal text, and social icons.

### Accordion
**`accordion-trigger`** — Used on product pages for “Details,” “Shipping,” “Returns.” The trigger is a full-width button with {typography.title-sm} and a 1px {colors.hairline-soft} bottom border. Active state shifts text to {colors.primary}. The content panel uses {typography.body-sm} with {spacing.base} bottom padding.

### Dividers
**`divider`** — A 1px {colors.hairline} line used between sections. **`divider-strong`** — A 2px {colors.primary} line used sparingly, typically as a section header underline or the footer top border.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces nav links, footer collapses to single column, hero text reduces to {typography.display-md} |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, footer in two columns, hero uses {typography.display-lg} |
| Desktop | 1128–1440px | Three-column product grid, full nav bar, footer in four columns, hero uses {typography.display-xl} |
| Wide | > 1440px | Max-width container at 1440px, product grid can expand to four columns, hero remains centered with max-width |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px and minimum width of 44px.
- Nav links have 8px 16px padding, providing a 44px+ tap area.
- Icon buttons are exactly 44px square.
- Product card tap targets are the entire card, not just the title or price.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger menu. The drawer slides in from the left, full-height, with nav links stacked vertically.
- The product filter sidebar (if present) collapses into a bottom sheet or a toggleable overlay.
- The footer collapses from 4 columns to 1 column, with accordion-style expandable sections for each column.
- The hero section reduces font sizes and may stack the image above the text rather than side-by-side.
- Product image galleries switch from a thumbnail strip to a swipeable carousel.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for `button-secondary` and `button-text` are inferred from common patterns; exact color transitions (e.g., background opacity changes) were not extractable.
- Error styling for forms (error messages, icon placement) is assumed; the extracted palette includes #c13515 as a likely error red, but its usage is not confirmed.
- Dark mode is not present on the live site; no dark-mode tokens are defined.
- Sub-brand or collection-specific palettes (e.g., limited-edition drops) could not be extracted.
- The exact font stack order for `alternate-gothic-no-3-d` and `big-caslon-fb` is inferred; the live site may use different fallback ordering.
- `letterSpacing` values for display fonts are estimated from common practice; exact values were not extractable from CSS.
- The `badge-bg` color (#868154) is assumed from the extracted palette; its exact usage (sale vs. new vs. exclusive) is not confirmed.
- Loading states (skeleton screens, shimmer animations) were not observed.
- The `tooltip` component is defined based on convention; its exact styling on the live site is unknown.
- Checkout flow styling (Shopify checkout overrides) was not extractable; the brand may use default Shopify checkout or a custom theme.
