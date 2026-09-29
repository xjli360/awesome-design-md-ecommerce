---
version: alpha
name: "Plugable"
source_url: "https://plugable.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A utilitarian electronics brand that speaks through a #006341 green — the color of a circuit board's solder mask, of a "go" indicator on a powered dock — used as the primary voltage across CTAs, badges, and the top nav's active state. The palette is a mix of hardware-store grays (#5c677a, #88888d, #636763) and signal colors (#ce3525 for errors, #f9b434 for warnings), with a surprising secondary accent in #e83e8c (a hot pink that appears on sale badges and promotional ribbons). Typography runs proxima-nova as the brand face, backed by system sans-serifs, set at moderate sizes with tight line heights — the brand trusts spec sheets and comparison tables over editorial prose. Product cards use a clean white canvas ({colors.canvas}) with a soft {rounded.sm} corner, while the hero section deploys a full-bleed image with a green overlay gradient. The overall feel is "reliable hardware company that invested in a proper web store" — no whimsy, no lifestyle photography, just docks, cables, and adapters presented with the clarity of a data sheet.

colors:
  primary: "#006341"
  primary-active: "#004d32"
  primary-disabled: "#80b1a0"
  ink: "#111100"
  body: "#262626"
  muted: "#5c677a"
  muted-soft: "#88888d"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  error: "#ce3525"
  warning: "#f9b434"
  sale-accent: "#e83e8c"
  success: "#19c37d"
  info: "#5bc0de"
  link: "#3793ff"
  dark-bg: "#121212"

typography:
  display-xl:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.11
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.14
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.17
    letterSpacing: 0
  title-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.22
    letterSpacing: 0
  title-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.25px
  link:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-danger:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  price-display:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  sale-price:
    typography: "{typography.price}"
    textColor: "{colors.error}"
  badge-sale:
    backgroundColor: "{colors.sale-accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-stock:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  hero-overlay-gradient:
    backgroundImage: "linear-gradient(135deg, {colors.primary} 0%, rgba(0,99,65,0.8) 100%)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 44px
  footer-section:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 16px
  table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 10px 12px
  table-cell:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 10px 12px
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 10px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Buy Now", and "Shop All" links. Filled with the brand green (#006341) and white text, with a subtle 4px corner radius. On hover, darkens to `{colors.primary-active}` (#004d32). Disabled state uses `{colors.primary-disabled}` (#80b1a0) with white text.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "Compare". White background with green text and a 1px green border. Active state shifts to `{colors.surface-soft}` background with darker green text.

**`button-danger`** — Reserved for destructive actions like "Remove from Cart" or "Cancel Order". Uses the error red (#ce3525) as background with white text.

### Cards
**`product-card`** — The primary product display unit on collection pages and search results. A white card with 4px rounded corners and 12px padding. On hover, the background shifts to `{colors.surface-soft}` (#f4f4f4). The product image sits at the top with matching 4px rounded corners and a 1:1 aspect ratio. Below the image, the product title uses `{typography.title-sm}`, the price uses `{typography.price}`, and any badges (sale, new, in-stock) appear as small pills in the top-left corner of the image.

**`spec-badge`** — A small pill-shaped tag used to display technical specifications like "USB-C", "4K@60Hz", "100W PD". Uses `{colors.surface-soft}` background with `{colors.muted}` text, fully rounded corners, and tight padding.

### Navigation
**`nav-bar`** — A 64px-tall fixed header with white background. Navigation links use uppercase proxima-nova at 14px with 0.5px letter-spacing. The active link or current section uses the brand green color. The nav includes a search icon that expands into the full `{search-bar}` component on click.

**`search-bar`** — A pill-shaped search input with full border radius, white background, and 44px height. Used in the nav and on the search results page. Includes a magnifying glass icon on the left and a clear button on the right when text is entered.

### Forms
**`text-input`** — Standard text input for forms (address, email, search queries). White background with 4px rounded corners, 44px height, and 10px/12px padding. Focus state adds a 2px green border.

**`select-input`** — Dropdown select styled consistently with text inputs. Same dimensions and corner radius, with a custom dropdown arrow icon.

### Footer
**`footer-section`** — A dark background (#121212) section at the bottom of every page. Contains columns of links, contact information, and legal text. Links use `{colors.muted-soft}` (#88888d) and lighten to white on hover. The footer includes the Plugable logo in white, social media icons, and a copyright notice.

### Accordion
**`accordion-header`** — Used on product pages for "Specifications", "What's in the Box", and "Compatibility" sections. A light gray (#f4f4f4) background with 4px rounded corners and 12px/16px padding. Includes a chevron icon that rotates on open.

**`accordion-content`** — The expandable content area below the header. White background with 16px padding. Contains spec tables, bullet lists, or descriptive text.

### Tables
**`table-header`** — Used in comparison tables and spec sheets. Light gray background with bold text and 10px/12px padding. The first column is typically the spec name, with subsequent columns for different product variants.

**`table-cell`** — Standard table cell with white background and body text. Alternating rows may use `{colors.surface-soft}` for readability.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked footer, accordion specs always collapsed, search bar collapses to icon |
| Tablet | 744–1128px | Two-column product grid, full nav with dropdowns, two-column footer, comparison tables scroll horizontally |
| Desktop | 1128–1440px | Three-column product grid, full nav with mega-menu, four-column footer, full comparison tables |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, extended footer with additional legal links |

### Touch Targets
- All buttons and interactive elements minimum 44px height
- Nav links minimum 44px tap area (even if text is smaller)
- Accordion headers minimum 48px tap area
- Product card tap targets (add to cart, quick view) minimum 44px
- Search icon minimum 44x44px tap area
- Footer links minimum 44px tap area

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Product filters collapse to a slide-out drawer on mobile
- Comparison tables collapse to a scrollable horizontal container on tablet
- Footer link columns stack vertically on mobile
- Accordion sections are collapsed by default on all breakpoints
- Search bar collapses to icon-only on mobile, expands to full input on tap
- Product image gallery collapses to single-image view on mobile, thumbnails become dots

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for form inputs (beyond basic color changes) could not be reliably extracted — assume 2px green focus ring on all interactive elements
- Error state styling for forms (red border, error message placement) not observed
- Success state styling for forms (green border, checkmark) not observed
- Loading states (spinners, skeleton screens) not observed
- Dark mode variant not present on the live site
- Sub-brand or product-line-specific color variations (e.g., "Plugable Pro" or "Plugable Gaming") not observed
- Animation durations and easing curves not extracted — assume 200ms ease-in-out for all transitions
- Dropdown/mega-menu hover behavior and timing not observed
- Modal/dialog overlay styling not observed
- Tooltip styling not observed
- The extracted color list includes several Shopify checkout widget colors (#5bc0de, #e83e8c, #19c37d, #3793ff) and social icon colors (#884488 for Instagram) — these are not brand colors but platform defaults
- The brand's true secondary palette beyond green and gray is unclear from extraction — the hot pink (#e83e8c) appears on sale badges but may be a Shopify default rather than a brand choice
