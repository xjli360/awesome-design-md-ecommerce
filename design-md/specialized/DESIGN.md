---
version: alpha
name: "Specialized"
source_url: "https://www.specialized.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A cycling brand that uses red (#da291c) not as an accent but as a structural claim — the same voltage that marks a Tarmac frame's downtube also fills the primary CTA, the sale badge, the cart icon, and the "Rider First" banner. The palette is overwhelmingly gray: twenty-one steps from #252525 (near-black ink) through #f8f8f8 (canvas) with a warm amber sub-palette (#ffe31b through #482300) that surfaces in limited-edition frames and seasonal hero shots. Typography runs DINPro for body and Degular for display, a mix of German functionalism and American modernism that mirrors the brand's engineering-meets-culture ethos. Corners are mostly sharp — buttons use {rounded.sm} (8px), cards use {rounded.md} (12px), and the only {rounded.full} appears on the search orb and filter pills. The site trusts high-contrast photography and generous whitespace over decorative UI; the product grid is a dense, information-rich field of 4-column cards with spec callouts, price, and a "Quick Add" button that appears on hover. The nav bar is a 48px strip of {colors.ink} with white text, a persistent search icon, and a cart badge that inherits {colors.primary}. The overall mood is serious, fast, and rider-obsessed — the brand's own tagline "Made for riders, by riders." appears in the page title and footer, not as a decorative overlay.

colors:
  primary: "#da291c"
  primary-active: "#b82216"
  primary-disabled: "#f5b3ae"
  ink: "#252525"
  body: "#3d3d3d"
  muted: "#7c7c7c"
  muted-soft: "#989898"
  hairline: "#dcdcdc"
  hairline-soft: "#f1f1f1"
  canvas: "#f8f8f8"
  surface-soft: "#f1f1f1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  amber-bright: "#ffe31b"
  amber-mid: "#f49543"
  amber-dark: "#7c440b"
  sale-badge-bg: "#da291c"
  sale-badge-text: "#ffffff"
  star-rating: "#252525"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Degular', 'DINPro', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Degular', 'DINPro', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Degular', 'DINPro', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Degular', 'DINPro', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'DINPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'DINPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'DINPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'DINPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'DINPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'DINPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0.2px
  badge:
    fontFamily: "'DINPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'DINPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'DINPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'DINPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'DINPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.3px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-orb:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 36px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 48px
  top-nav-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: 0 16px
  top-nav-link-active:
    textColor: "{colors.primary}"
  top-nav-link-hover:
    textColor: "{colors.primary}"
  nav-search-icon:
    textColor: "{colors.on-dark}"
    height: 24px
  nav-cart-icon:
    textColor: "{colors.on-dark}"
    height: 24px
  nav-cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "{spacing.xs} {spacing.base}"
  product-card-sale-badge:
    backgroundColor: "{colors.sale-badge-bg}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-quick-add:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 36px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-lg}"
    height: 600px
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.4
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.base}"
  section-heading:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  rating-stars:
    color: "{colors.star-rating}"
    height: 16px
  color-swatch:
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. Uses {colors.primary} (#da291c) as a full background fill with white text and 8px rounded corners ({rounded.sm}). On hover, the background shifts to {colors.primary-active} (#b82216) for a darker, more urgent state. The disabled state uses {colors.primary-disabled} (#f5b3ae) with white text, signaling the action is unavailable. All primary buttons use uppercase DINPro at 14px/700 weight with 0.5px letter spacing for a technical, performance-oriented feel.

**`button-secondary`** — An outlined alternative with a {colors.canvas} background, {colors.ink} text, and a 2px solid {colors.ink} border. On hover, the button inverts to a solid {colors.ink} fill with white text. Used for "Learn More" links, secondary product actions, and filter resets. Maintains the same uppercase DINPro typography and 44px height as the primary button.

**`button-tertiary-text`** — A text-only button with no background or border. Uses {colors.ink} text and the same uppercase DINPro typography. Appears in navigation dropdowns, account menus, and as "View All" links in category strips. On hover, text color shifts to {colors.primary}.

**`button-pill-primary`** — A fully rounded pill variant of the primary button, used for "Quick Add" on product cards and "Shop Now" in hero banners. Uses {colors.primary} background with white text and {rounded.full} for the pill shape. Typography is the smaller button-sm variant (12px/700 uppercase).

**`button-pill-outline`** — An outlined pill button with a transparent background, {colors.ink} text, and a 1px {colors.hairline} border. Used for filter chips, size selectors, and "Compare" toggles. On active state, the background fills with {colors.ink} and text inverts to white.

### Navigation
**`top-nav`** — A fixed 48px strip at the top of every page, using a full {colors.ink} (#252525) background with white text. Contains the Specialized "S" logo, category links (Bikes, Gear, Apparel, Accessories, Support), a search icon, and a cart icon with a {colors.primary} badge showing item count. Links use uppercase DINPro at 13px/600 weight. The active and hover states shift link color to {colors.primary}.

**`top-nav-link`** — Individual navigation items within the top bar. Uses {colors.on-dark} text by default, with a hover state that shifts to {colors.primary}. Each link has 16px horizontal padding. The active page link also uses {colors.primary} to indicate current section.

**`nav-cart-badge`** — A small circular badge overlaid on the cart icon, showing the number of items in the cart. Uses {colors.primary} background with white text in caption-sm typography (11px). The badge is fully rounded ({rounded.full}) and 18px tall.

### Cards
**`product-card`** — The primary product display unit, used in grid layouts across category pages and search results. Has a white background ({colors.surface-card}), {colors.ink} text, and 12px rounded corners ({rounded.md}). The card contains a product image (with rounded top corners only), a title in title-sm typography (16px/600), a price in body-md (16px/600 weight), and optional sale badges. On hover, a "Quick Add" button appears at the bottom of the image area.

**`product-card-sale-badge`** — A small rectangular badge overlaid on the product image, indicating a sale or clearance item. Uses {colors.sale-badge-bg} (#da291c) with white text in uppercase badge typography (11px/700). Has 4px rounded corners ({rounded.xs}) and 2px/8px padding.

**`product-card-quick-add`** — A hover-reveal button on product cards that allows adding an item to the cart without navigating to the product page. Uses {colors.ink} background with white text in button-sm typography (12px/700 uppercase). Has 8px rounded corners ({rounded.sm}) and is 36px tall.

### Forms
**`text-input`** — Standard text input fields used in search, account forms, and checkout. Has a {colors.canvas} background, {colors.ink} text, and a 1px {colors.hairline} border with 8px rounded corners ({rounded.sm}). On focus, the border thickens to 2px and shifts to {colors.primary}. Error states use a 1px {colors.primary} border. Input height is 48px with 12px/16px padding.

**`search-bar`** — The global search input, typically placed in the top nav or on the search page. Uses a pill shape ({rounded.full}) with a {colors.canvas} background, {colors.ink} text, and a 1px {colors.hairline} border. Height is 48px with 10px/20px padding. On focus, the border shifts to {colors.primary}.

### Hero
**`hero-banner`** — Full-width hero sections on the homepage and campaign pages. Uses a {colors.ink} background with white text in display-lg typography (36px/600). Height is 600px on desktop. Contains a headline, optional subtitle, and a primary CTA button. A semi-transparent overlay ({colors.scrim} at 40% opacity) sits between the background image and the text for readability.

**`hero-banner-cta`** — The primary call-to-action button within hero banners. Uses {colors.primary} background with white text in button-md typography (14px/700 uppercase). Has 8px rounded corners ({rounded.sm}) and is 48px tall with 14px/32px padding.

### Filters
**`filter-pill`** — Pill-shaped filter options used on category pages and search results. Has a {colors.canvas} background, {colors.ink} text, and a 1px {colors.hairline} border with full rounding ({rounded.full}). Uses button-sm typography (12px/700 uppercase). The active state fills the background with {colors.ink} and inverts text to white.

### Footer
**`footer`** — The site-wide footer with a {colors.ink} background and white text. Contains columns for product categories, support links, company information, and social media links. Uses body-sm typography (14px/400) for most content, with title-sm (16px/600) for column headings. Links use {colors.muted-soft} (#989898) by default and shift to white on hover. Padding is {spacing.xxl} (48px) top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces top nav links, hero height reduces to 400px, search bar collapses to icon-only, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, top nav shows 4-5 category links, hero height at 500px, search bar remains full-width in nav, footer shows 2-column layout |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all category links, hero at 600px, search bar in nav with text input visible, footer shows 4-column layout |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero at 600px with full-bleed background, all elements at maximum comfortable width |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44px height
- Filter pills and badge elements have a minimum touch target of 36px
- Icon buttons (search, cart, account) are 40px minimum
- Product card "Quick Add" buttons are 36px tall with 16px padding

### Collapsing Strategy
- Top nav category links collapse into a hamburger menu below 744px
- Product grid collapses from 4 columns to 1 column on mobile
- Footer columns collapse from 4 to 1 on mobile, with accordion-style expandable sections
- Hero banner text overlay shifts from left-aligned to center-aligned on mobile
- Search bar collapses to an icon-only trigger on mobile, expanding to full-width on tap
- Filter strip collapses to a single "Filter" button on mobile, opening a full-screen overlay

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list includes 30+ colors, but many are likely from stock photography, social media icons, or checkout widgets. The true brand palette is dominated by grays (#252525 through #f8f8f8) with a single red accent (#da291c) and a warm amber sub-palette (#ffe31b through #482300) that may be seasonal or campaign-specific. The amber colors appear in limited-edition bike frames and hero imagery but are not consistently used in UI elements.
- Font family declarations were extracted from CSS but exact weights, sizes, and line heights for each typography token were inferred from common web patterns and may not match the live site's exact values. The brand appears to use Degular for display headings and DINPro for body text, but the exact font stack order and fallbacks may vary.
- Hover, focus, active, and disabled states for many components (text-input, filter-pill, footer-link) were inferred from common patterns and may not match the live site's exact implementations.
- Error styling for forms (validation messages, error icons, input border colors) was not extracted and uses standard patterns.
- Dark mode is not supported on the live site; all UI is light mode with a dark nav and footer.
- The brand's sub-brand palettes (S-Works, Turbo, Roval, etc.) were not extracted and may use distinct accent colors.
- Animation and transition durations, easing functions, and micro-interactions were not extracted.
- The exact spacing scale (padding, margin, gap values) was inferred from common web patterns and may not match the live site's exact values.
- Iconography (search, cart, account, social media) was not extracted; all icons are assumed to be SVG-based with standard sizing.
- The product card's hover state (shadow, border, elevation) was not extracted and uses a standard 2px shadow on hover.
