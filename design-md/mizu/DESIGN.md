---
version: alpha
name: "Mizu"
source_url: "https://mizulife.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A stainless-steel water-bottle brand that wraps its cold-touch metal in a warm, approachable palette — #2332d5 (a vivid, almost-electric blue) is the primary voltage, appearing on CTAs, add-to-cart buttons, and the brand's signature straw-lid accents, while #303030 and #616161 anchor body text and product names in a grounded, industrial gray scale. The canvas is #f3f3f3, a soft off-white that reads as more tactile than pure white, and product cards float on #ffffff with hairline borders at #b5b5b5 — the effect is clean but not sterile, like a well-organized gear closet. Montserrat runs across the site at moderate weights (400–600), with display headlines sitting at 24–32px in weight 600, never shouting; the brand trusts its product photography — glossy steel, condensation beads, outdoor backdrops — to carry the sensory load. Signature moves include a persistent sticky cart indicator with a {rounded.full} badge showing item count, a search bar with a {rounded.sm} field and a blue magnifying-glass icon, and product cards that use a two-line title truncation with a subtle ellipsis. The checkout flow leans on Shopify's native components but the brand's blue (#2332d5) reappears on the "Add to Cart" and "Buy It Now" buttons, creating a consistent thread from browse to purchase. There is no dark mode; the entire experience lives in light gray and white, with the blue acting as a cold-weather accent — like a flash of sky through a forest canopy.

colors:
  primary: "#2332d5"
  primary-active: "#1a26b0"
  primary-disabled: "#a8b2ff"
  ink: "#303030"
  body: "#616161"
  muted: "#808080"
  muted-soft: "#b5b5b5"
  hairline: "#b5b5b5"
  hairline-soft: "#d0d0d0"
  canvas: "#f3f3f3"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#29845a"
  accent-orange: "#f48120"
  accent-red: "#ea5455"
  badge-blue: "#dee6ff"
  badge-green: "#cdfee1"
  badge-yellow: "#fff8db"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
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
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-outline-active:
    backgroundColor: "{colors.badge-blue}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.surface-card}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
    backgroundColor: "{colors.surface-card}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-sticky:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 44px
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  search-icon:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    height: 20px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.surface-card}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  badge-new:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.accent-green}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-yellow}"
    textColor: "#4f4700"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-bestseller:
    backgroundColor: "{colors.badge-blue}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  accordion-header:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Buy It Now", and "Subscribe". Renders in the brand's vivid blue (#2332d5) with white text and an 8px corner radius. On hover, darkens to `primary-active` (#1a26b0); when disabled, shifts to a pale blue-gray (#a8b2ff) with white text. The button maintains a consistent 44px height and 12px/24px padding for comfortable tap targets on mobile.

**`button-secondary`** — A ghost-style button on the off-white canvas background (#f3f3f3), used for "Learn More" and secondary checkout actions. On hover, the background fills with the soft surface color (#f0f0f0). The borderless design keeps the focus on the product photography.

**`button-outline`** — A bordered variant with a 2px solid primary-blue stroke and transparent fill, used for "View Details" on product cards and "Compare" actions. On hover, the background fills with the badge-blue tint (#dee6ff) and the border darkens to `primary-active`.

### Navigation
**`nav-bar`** — A fixed 72px header with white background, containing the brand logo (left), navigation links (center), and cart icon with badge (right). Navigation links are uppercase Montserrat 600 at 14px with 0.5px letter-spacing, creating a crisp, outdoor-gear aesthetic. On scroll, a subtle box-shadow appears to separate the nav from content. The active page link renders in primary blue.

**`nav-link`** — Inline navigation items with 8px/16px padding. Default state is ink (#303030); active state switches to primary blue (#2332d5). No underline or border — the color shift alone signals state.

### Cards
**`product-card`** — A white card with 12px corner radius containing a square product image (1:1 aspect ratio), title, and price. The image has rounded top corners matching the card radius, while the bottom corners remain square to meet the content area cleanly. On hover, a subtle shadow lifts the card 4px off the surface. Title uses 16px/600 Montserrat, price uses 16px/400 in body gray (#616161).

**`product-card-image`** — The top portion of the product card, with rounded top corners (12px) and a 1:1 aspect ratio. Images are typically lifestyle shots of bottles in outdoor settings, with the product centered.

### Forms
**`text-input`** — Standard input field with a 1px hairline border (#b5b5b5), 8px corner radius, and 44px height. On focus, the border thickens to 2px primary blue. Error state switches to a 2px red border (#ea5455). Used for email capture, search queries, and checkout fields.

**`search-bar`** — A compact search field on the soft gray surface (#f0f0f0), with a magnifying glass icon and placeholder text in muted gray (#808080). On focus, the background switches to white and a 2px primary-blue border appears. The icon sits at 20px height.

### Badges
**`badge-new`** — A small green badge on a pale green background (#cdfee1), used to flag newly launched products. Text reads "NEW" in 11px/600 Montserrat with dark green text (#29845a). 4px corner radius and 2px/8px padding keep it compact.

**`badge-sale`** — A yellow badge on a pale yellow background (#fff8db) with dark amber text (#4f4700). Used for promotional pricing or limited-time offers.

**`badge-bestseller`** — A blue badge on a pale blue background (#dee6ff) with primary-blue text (#2332d5). Used to highlight top-selling products.

### Footer
**`footer`** — A dark footer section on ink (#303030) background, with links in muted-soft gray (#b5b5b5). Links hover to white. The footer contains three columns: customer service, about Mizu, and social links. Padding is 48px top/bottom with 16px sides.

**`footer-link`** — Inline footer links at 14px/500 Montserrat. Default state is muted-soft gray; hover state transitions to white (#ffffff).

### Hero
**`hero-banner`** — A full-width banner section on the canvas background (#f3f3f3) with 64px vertical padding. The hero contains a headline in display-xl (32px/600), a subheading in body-md (16px/400), and a primary CTA button. Typically paired with a full-bleed product image on the right side.

**`hero-cta`** — A larger primary button variant at 48px height with 14px/32px padding, used exclusively in the hero section. Same primary blue background and white text as `button-primary`, but with more generous proportions to anchor the page.

### Quantity Selector
**`quantity-selector`** — A horizontal control on the product page for adjusting item count. Rendered on the soft gray surface (#f0f0f0) with 8px corner radius and 40px height. Contains a minus button, the current quantity (centered), and a plus button — each 40px square with transparent background and ink text.

### Accordion
**`accordion-header`** — A clickable header row for product details, shipping info, and care instructions. Uses title-sm typography (16px/600) with ink text on white background. Padding is 16px top/bottom with no horizontal padding — the header spans the full content width.

**`accordion-content`** — The expandable content area below each accordion header. Uses body-sm typography (14px/400) in body gray (#616161) with 16px bottom padding. Content typically includes bullet lists or short paragraphs.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product cards stack in single column; hero banner reduces to 48px padding; search bar moves to expandable icon; footer stacks vertically |
| Tablet | 744–1128px | Nav links visible but condensed; product cards in 2-column grid; hero retains full layout with reduced font sizes; footer in 2-column layout |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero at full typography scale; footer in 3-column layout |
| Wide | > 1440px | Max-width container at 1440px with centered content; product cards in 4-column grid; increased whitespace in hero |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav links have 8px/16px padding, providing 30px+ tap targets
- Quantity selector buttons are 40px squares — meets minimum but close to edge; consider 44px on mobile
- Cart badge is 20px diameter — small but acceptable for informational display (not a primary tap target)
- Search icon is 20px — consider increasing to 24px on mobile for easier tapping

### Collapsing Strategy
- **Navigation**: On mobile (< 744px), the full nav link list collapses behind a hamburger icon. The logo and cart badge remain visible. A slide-out drawer reveals links on tap.
- **Product Grid**: On mobile, the 3-column grid collapses to single column. On tablet, it collapses to 2 columns.
- **Footer**: On mobile, the 3-column footer collapses to a single vertical stack. Accordion-style sections may be used for long link lists.
- **Hero**: On mobile, the hero banner reduces vertical padding from 64px to 48px, and the headline drops from 32px to 24px. The product image may move below the text.
- **Search**: On mobile, the search bar collapses to a magnifying glass icon that expands to a full-width input on tap.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only primary button and product card hover states were reliably extracted. Secondary button, link, and footer link hover states are inferred from common patterns.
- **Error styling**: Text input error state (red border) is inferred from the presence of #ea5455 in the palette. No error message typography or iconography was extracted.
- **Focus states**: Focus ring styling (color, width, offset) was not extracted. The text-input focus state uses a 2px border as a common pattern.
- **Dark mode**: No dark mode exists on the live site. The palette is entirely light-mode.
- **Sub-brand palettes**: Mizu may have seasonal or collection-specific color schemes (e.g., limited edition bottle colors) that were not captured.
- **Typography scale**: Only Montserrat was extracted. Heading sizes (display-xl through display-md) are estimated from common Shopify patterns and may differ from the actual site.
- **Spacing scale**: The spacing tokens (xxs through section) are based on common e-commerce patterns. Actual site spacing may vary.
- **Component states**: Disabled states for buttons, loading states for product cards, and empty states for search results were not extracted.
- **Checkout components**: Shopify's native checkout flow may override Mizu's design system. The primary blue appears on "Add to Cart" but checkout button styling may differ.
- **Animation and transitions**: No transition durations, easing functions, or animation patterns were extracted.
- **Iconography**: The search icon and cart icon styles (stroke width, size, color) were not extracted beyond basic dimensions.
- **The extracted color list contains many Shopify-widget and social-icon colors (#005bd3, #006fcf, #8051ff, #7367f0, #f72119, #5e5873, #b9b9c3). The true brand palette is likely narrower — the primary blue (#2332d5), ink (#303030), body (#616161), and canvas (#f3f3f3) are the core four. The accent colors (green, orange, red) are inferred from their presence in the extracted list but may not be active brand colors.
