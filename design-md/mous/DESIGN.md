---
version: alpha
name: "Mous"
source_url: "https://www.mous.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep teal (#005050) and cyan (#00bec8) brand voltage that reads as engineered precision meets underwater calm — the primary #005050 appears across every product detail page header, navigation bar, and checkout button, while #00bec8 acts as a secondary accent on hover states and interactive icons. The palette is unusually aquatic for a phone case brand: #108474 (a jade green) and #007575 (a darker teal) create a layered ocean gradient that feels deliberate rather than decorative. White canvas (#ffffff) and near-white surfaces (#f9fafb, #f0f0f0) keep the product photography — glossy aramid fiber, carbon fiber, and leather textures — as the hero. The brand uses Brandon Text (a geometric sans-serif with soft rounded terminals) for headings and body copy, giving the interface a friendly precision that matches their "limitless" product positioning. Rounded corners are generous but not pill-shaped: product cards use {rounded.md} (12px), buttons use {rounded.sm} (8px), and the search bar uses {rounded.full} (9999px) as a single soft gesture. The color #fbcd0a (a warm marigold) appears sparingly on sale badges and limited-edition callouts, providing the only warmth in an otherwise cool system. The brand's signature design move is the "Clarity" product card — a full-bleed hero image with a translucent overlay (#005050 at 60% opacity) and white text, creating a glassy depth effect that mimics the phone case's own transparency.

colors:
  primary: "#005050"
  primary-active: "#007575"
  primary-disabled: "#7b7b7b"
  ink: "#1d1d1d"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#bbbbbb"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#00bec8"
  accent-marigold: "#fbcd0a"
  accent-jade: "#108474"
  accent-orange: "#e26106"
  accent-lavender: "#a89cc8"
  accent-pink: "#d16bcd"
  star-rating: "#fbcd0a"
  error: "#e26106"
  success: "#108474"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Brandon Text', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Brandon Text', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "'Brandon Text', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Brandon Text', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Brandon Text', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Brandon Text', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Brandon Text', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Brandon Text', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Brandon Text', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Brandon Text', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Brandon Text', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Brandon Text', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Brandon Text', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Brandon Text', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Brandon Text', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  link:
    fontFamily: "'Brandon Text', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Brandon Text', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    height: 36px
    border: "1px solid {colors.primary}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "2px solid {colors.primary}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  top-nav-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
    rounded: "{rounded.sm}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
    rounded: "{rounded.sm}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-new:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: "400px"
  hero-banner-overlay:
    backgroundColor: "rgba(0, 80, 80, 0.6)"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
    padding: "{spacing.xs} 0"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
    padding: "{spacing.xs} 0"
  section-header:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
    padding: "{spacing.xl} 0 {spacing.base}"
  section-subheader:
    typography: "{typography.body-lg}"
    textColor: "{colors.body}"
    padding: "0 0 {spacing.lg}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: "1px"
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: "1px"
  badge-sale:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-limited:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-eco:
    backgroundColor: "{colors.accent-jade}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: "16px"
  review-count:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.base} 0"
  toast-success:
    backgroundColor: "{colors.accent-jade}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  toast-error:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: "40px"
    padding: "0 {spacing.sm}"
  color-swatch:
    rounded: "{rounded.full}"
    height: "32px"
    width: "32px"
    border: "2px solid transparent"
  color-swatch-selected:
    rounded: "{rounded.full}"
    height: "32px"
    width: "32px"
    border: "2px solid {colors.primary}"
  material-swatch:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
    height: "40px"
  material-swatch-selected:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
    height: "40px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and "Shop Now" actions. Rendered in the brand's deep teal {colors.primary} with white text and {rounded.sm} corners. On hover, shifts to {colors.primary-active} (#007575). When disabled, uses {colors.primary-disabled} (#7b7b7b) to indicate non-interactivity.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details". Uses a white background with a 2px {colors.primary} border and matching text. Active state inverts to {colors.surface-soft} background with {colors.primary-active} border.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel" or "Skip". On hover, gains a subtle {colors.surface-soft} background. Maintains {colors.primary} text throughout.

**`button-pill`** — A compact, fully rounded variant used for filter tags, category pills, and quick-select actions. Uses {colors.primary} background with white text and {rounded.full} corners. The outline variant uses transparent background with a 1px {colors.primary} border.

### Navigation
**`top-nav`** — A fixed-position header bar at 64px height with white background and a 1px {colors.hairline} bottom border. Contains the brand logo (left), navigation links (center), and utility icons (right — search, account, cart). On scroll, gains a subtle box shadow for depth. Navigation links use uppercase Brandon Text at 14px/600 weight with {colors.body} text, switching to {colors.primary} with a 2px bottom border when active.

**`nav-link`** — Individual navigation items with {spacing.sm} padding and {rounded.sm} corners. Inactive links use {colors.body} text; active links use {colors.primary} with a 2px bottom border. No background change on hover — the brand relies on text color and underline for state indication.

### Cards
**`product-card`** — The primary product display component, used on collection pages and search results. Features a 1:1 aspect ratio product image with {rounded.md} top corners, followed by product title ({typography.title-sm}) and price ({typography.body-md}). The card has a white background, {rounded.md} corners, and a subtle 1px/3px box shadow. On hover, the shadow deepens to 4px/12px for lift effect.

**`product-card-badge`** — Overlay badges positioned absolutely at the top-left of product images. Three variants exist: sale (marigold {colors.accent-marigold} with dark text), sold out (gray {colors.muted} with white text), and new (cyan {colors.accent-cyan} with white text). All use {typography.badge} (11px/700 weight, uppercase) with {rounded.xs} corners and 4px/8px padding.

### Forms
**`text-input`** — Standard text input fields used for email, name, and address forms. White background with 1px {colors.hairline} border and {rounded.sm} corners. On focus, the border thickens to 2px and switches to {colors.primary}. Error state uses a 2px {colors.error} (#e26106) border.

**`select-input`** — Dropdown select fields matching the text input styling: white background, 1px {colors.hairline} border, {rounded.sm} corners, and 48px height. Uses the same focus and error state patterns as text inputs.

**`search-bar`** — A pill-shaped search field ({rounded.full}) with white background and 1px {colors.hairline} border. On focus, the border thickens to 2px {colors.primary}. Positioned in the top nav and on the search results page.

### Footer
**`footer`** — A dark footer section with {colors.ink} (#1d1d1d) background and white text. Contains link columns, brand information, and social icons. Footer links use {colors.muted-soft} (#bbbbbb) text with no underline, switching to white on hover. Padding is generous at {spacing.section} (64px) top and bottom.

### Badges & Indicators
**`badge-sale`** — A marigold {colors.accent-marigold} badge with dark text, used to highlight discounted products. Uses {typography.badge} with {rounded.xs} corners and minimal padding.

**`badge-limited`** — An orange {colors.accent-orange} badge for limited edition products. White text on orange background, same typography and corner treatment as sale badge.

**`badge-eco`** — A jade {colors.accent-jade} badge for eco-friendly or sustainable product lines. White text on green background.

**`star-rating`** — Gold {colors.star-rating} (#fbcd0a) stars at 16px, accompanied by a review count in {colors.muted} using {typography.caption}.

### Product Detail
**`color-swatch`** — Circular 32px swatches for product color selection. Selected state shows a 2px {colors.primary} border; unselected shows transparent border. The swatch color itself is set dynamically based on the product variant.

**`material-swatch`** — Rectangular swatches for material selection (e.g., Aramid Fiber, Leather, Carbon Fiber). Uses {rounded.sm} corners with a 1px {colors.hairline} border and {typography.caption} text. Selected state uses a 2px {colors.primary} border and {colors.surface-soft} background.

**`quantity-selector`** — A compact 40px height control with minus/plus buttons and a centered numeric display. Uses {rounded.sm} corners with 1px {colors.hairline} border.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger menu replaces top nav links, product cards stack vertically, search bar collapses to icon, footer links collapse to accordion |
| Tablet | 744–1128px | Two-column product grid, top nav shows limited links (Shop, About, Support), search bar remains expanded but shorter, footer uses 2-column layout |
| Desktop | 1128–1440px | Full top nav with all links, three-column product grid, expanded search bar, 4-column footer |
| Wide | > 1440px | Max-width container at 1440px, centered content, product grid expands to 4 columns, hero banners use full-width with max-height constraints |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons are 40x40px with 48px touch area via padding
- Color and material swatches are 32px with 44px touch area via padding
- Quantity selector buttons are 40x40px
- Search bar maintains 48px height across all breakpoints

### Collapsing Strategy
- Top nav links collapse to hamburger menu below 744px
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer link columns collapse to accordion sections below 744px
- Secondary navigation (category strip) collapses to horizontal scroll on mobile
- Hero banner text reduces from {typography.display-xl} (36px) to {typography.display-lg} (28px) on mobile
- Product card badges reposition from absolute overlay to inline below image on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; primary-active and button-secondary-active are best guesses based on color relationships
- Error and validation styling for forms is inferred from the extracted error color (#e26106); actual error message placement and iconography unknown
- Dark mode is not present on the live site; no dark theme tokens available
- The extracted font list includes "JudgemeIcons" and "JudgemeStar" which are third-party review widget fonts, not brand typography
- "Baskerville" in the extracted fonts may be used for limited editorial content or product descriptions; not confirmed as a brand font
- The extracted color #a89cc8 (lavender) and #d16bcd (pink) appear to be social media icon colors or checkout widget accents, not brand colors
- #779f74 (sage green) and #1e3f5a (navy) appear infrequently; may be used for specific product lines or limited editions
- Spacing values for components like product-card padding and hero-banner minHeight are inferred from common e-commerce patterns; actual values may vary
- The "Clarity" product card overlay effect (translucent #005050 at 60%) is visually observed but exact opacity and implementation details are estimated
- Animation durations and easing curves are not extracted; the site likely uses standard 200-300ms ease-in-out transitions
- Checkout flow components (cart drawer, shipping form, payment form) are not included as they use Shopify's default checkout
