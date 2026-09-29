---
version: alpha
name: "Grasshopper Film"
source_url: "https://grasshopperfilm.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep blue #003388 anchors a film distributor’s site that feels like a gallery wall — clean, quiet, and letting the posters do the talking. The single extracted color is a saturated navy that appears in the top navigation bar, footer backgrounds, and as a hover accent on film titles, giving the entire experience a consistent, serious tone without any secondary brand color to dilute it. The Shopify-powered storefront keeps a stark white canvas (#ffffff) for product pages, with film posters bleeding edge-to-edge and minimal text overlays. There are no rounded corners on major containers — the site uses sharp 0px corners on film grids and navigation, with only the smallest 4px rounding on add-to-cart buttons and filter tags, creating a deliberate contrast between the softness of cinema and the precision of a gallery catalog. Typography runs a straightforward system font stack (likely -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto) at modest sizes — film titles at 18-20px, body copy at 14-16px — with no display-level hero type or decorative headings. The absence of a secondary color, the reliance on white space, and the use of a single brand blue across all interactive elements suggests a design system built for maximum editorial focus: the films themselves are the color palette.

colors:
  primary: "#003388"
  primary-active: "#002266"
  primary-disabled: "#8099bb"
  ink: "#111111"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  film-rating: "#ffc107"
  sold-out: "#dc3545"
  preorder: "#28a745"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
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
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
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
  lg: 16px
  xl: 24px
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
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
  text-input-error:
    border: "1px solid {colors.sold-out}"
    rounded: "{rounded.xs}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-bar-sticky:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    boxShadow: "0 2px 4px rgba(0,0,0,0.1)"
  nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-link-active:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.on-primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "2/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sold-out:
    backgroundColor: "{colors.sold-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  filter-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
  filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 14px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  loading-spinner-small:
    color: "{colors.primary}"
    size: 16px
  error-message:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.sold-out}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
  success-message:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.preorder}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and "Subscribe" flows. Rendered as a solid blue rectangle with 4px rounding, white text, and 10px vertical / 20px horizontal padding. On hover, the background deepens to `#002266` with no other visual change. The disabled state uses a muted blue-gray `#8099bb` to indicate unavailability while maintaining brand consistency.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Learn More". Uses a white background with a 2px solid blue border and blue text. On hover, the background shifts to a soft gray `#f5f5f5` and the border deepens. This button sits alongside the primary in product cards and collection pages, providing a clear visual hierarchy without competing for attention.

**`button-tertiary-text`** — A text-only button used for inline actions like "Clear Filters" or "Cancel". No background or border, just blue text that underlines on hover. The smallest visual footprint, reserved for low-importance interactions within filter bars and form sections.

### Cards
**`product-card`** — The core content container for film listings across collection pages, search results, and category grids. A white background with no rounding, relying entirely on the film poster image (2:3 aspect ratio) to communicate the product. The title sits below in 14px semibold, with the price in 14px regular muted gray. A badge overlay in the top-left corner uses the primary blue for "New Release" or "Pre-order" labels, with a red variant for "Sold Out" states. Cards have no border or shadow — the grid spacing provides separation.

**`product-card-image`** — The film poster fills the full width of the card with no rounding, maintaining the sharp, gallery-like presentation. The 2:3 aspect ratio matches standard movie poster dimensions, ensuring consistency across all film entries regardless of actual image proportions.

### Navigation
**`nav-bar`** — A fixed-height 56px bar in the primary blue that spans the full viewport width. Contains the brand name/logo on the left and navigation links (Films, Shop, About, etc.) in uppercase 14px semibold white text. Links have no background on default state; the active page is indicated by a 2px white bottom border. On scroll, a subtle box-shadow appears to separate the nav from page content. The bar collapses to a hamburger menu on mobile.

**`nav-link`** — Navigation items use 14px semibold uppercase type with 0.5px letter spacing for a refined, editorial feel. Default state is solid white; hover adds no background change but the link remains white. Active state adds a 2px white bottom border. Padding of 16px between links provides comfortable tap targets.

### Forms
**`text-input`** — Standard form input for search, newsletter signup, and checkout fields. A white background with a 1px light gray border and 4px rounding. On focus, the border thickens to 2px and turns the primary blue, providing clear visual feedback. Error states swap the border to red `#dc3545`. Height is 40px with 10px vertical padding for comfortable typing.

**`search-bar`** — A dedicated search input that lives in the nav or as a standalone component on collection pages. Identical styling to `text-input` but with a search icon positioned inside the left padding. On focus, the border transitions to 2px primary blue. The input clears on escape key or when clicking a close icon that appears on text entry.

### Footer
**`footer`** — A full-width section in the primary blue background, containing navigation links, social media icons, and copyright information. Links are white 14px regular weight with a hover state that shifts to a lighter muted tone. Padding of 48px vertical and 24px horizontal provides breathing room. The footer uses no rounding, maintaining the site's sharp, clean aesthetic.

### Hero
**`hero-section`** — A full-width white section at the top of the homepage and featured collection pages. Contains a 28px bold title and a 16px muted subtitle, with generous 64px vertical padding. No background color or image — the hero relies on typography and whitespace to establish hierarchy. The section sits flush with the nav bar below, creating a seamless reading experience.

### Badges
**`product-card-badge`** — A small label overlaid on product card images, using the primary blue background with white uppercase 11px bold text and 4px rounding. Padding of 2px vertical and 8px horizontal creates a compact tag. Used for "New", "Pre-order", and "Exclusive" labels. The `product-card-badge-sold-out` variant swaps the background to red for clear unavailability signaling.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product grid goes to 2 columns; hero padding reduces to 32px; filter tags stack vertically; footer links stack in single column |
| Tablet | 744–1128px | Nav links remain visible but reduce padding; product grid uses 3 columns; hero maintains 64px padding; filter tags wrap in a 2-row layout |
| Desktop | 1128–1440px | Full nav with all links; product grid uses 4 columns; hero at full padding; filter tags in a single horizontal row |
| Wide | > 1440px | Content max-width at 1440px with auto margins; product grid expands to 5 columns; hero content centered with max-width 1200px |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Nav links have 16px horizontal padding ensuring comfortable tap targets on mobile
- Filter tags have 12px vertical padding for easy tapping on touch devices
- Product card images are fully tappable, with the entire card area as the hit target

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-in drawer for links
- Product grid columns reduce from 5 to 2 on mobile, maintaining readability
- Filter section collapses into a "Filter" button that opens a modal overlay on mobile
- Footer link columns stack vertically on mobile, with each category becoming an accordion section
- Search bar collapses to an icon on mobile, expanding to full width on tap
- Hero section reduces vertical padding from 64px to 32px on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one brand color (#003388) was extractable from the live site; secondary, tertiary, and accent colors are inferred from common e-commerce patterns rather than extracted data
- No font-family declarations were found in the extracted data; the system font stack used here is an assumption based on common Shopify implementations
- Hover and active states for all components are inferred from standard web patterns, not extracted from the live site
- Error styling (form validation, 404 pages, empty states) is not extractable from the provided data
- Dark mode or high-contrast mode variants are not present in the extracted data
- Sub-brand or collection-specific color variations (e.g., for film series or special editions) are unknown
- Animation and transition timings (hover effects, page transitions, loading states) are not extractable
- Iconography style and sizing (social media icons, cart icon, search icon) are not documented in the extracted data
- The specific Shopify theme or framework used may introduce additional design tokens not captured here
- Print styles, focus indicators, and reduced-motion preferences are not extractable from the provided data
