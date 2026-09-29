---
version: alpha
name: "Riley Home"
source_url: "https://rileyhome.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Riley Home is a bath brand that feels like a warm, textured sanctuary — not cold spa minimalism but something softer, more tactile, with a palette anchored in earthy greens and sun-baked neutrals. The primary voltage is a deep teal-green (#108474) that appears on CTAs, navigation accents, and product badges, while a secondary warm clay (#e3ad7c) and a dusty sand (#bfa999) echo natural materials like terracotta and linen. The canvas is a clean off-white (#f9fafb) with surface cards in pure white (#ffffff) and soft muted backgrounds in barely-there gray (#f4f6f8, #edf5f5). Typography runs Assistant — a clean, slightly condensed sans-serif — at moderate weights (400–600), with display sizes around 28–32px and body text at 14–16px. The brand avoids heavy black text, using a dark brown (#3a2210) for ink and a medium gray (#7b7b7b) for muted copy, creating a softer reading experience. Signature design moves include pill-shaped buttons (`{rounded.full}`) and search bars, softly rounded product cards (`{rounded.md}` ~12px), and a persistent top nav with a clean white background and subtle hairline (#dedede). The overall mood is calm, considered, and residential — this is a brand that wants to feel like the best part of your morning routine, not a clinical bathroom showroom.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#a3d5c8"
  ink: "#3a2210"
  body: "#3a3a3a"
  muted: "#7b7b7b"
  muted-soft: "#bfa999"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#f9fafb"
  surface-soft: "#f4f6f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#e3ad7c"
  accent-sand: "#bfa999"
  accent-error: "#d72c0d"
  accent-sale: "#980707"
  star-rating: "#f1e04d"
  link-blue: "#1990c6"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
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
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 48px
    border: 1px solid "{colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: 1px solid "{colors.primary}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
  button-tertiary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
  button-warm:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.accent-error}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid "{colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid "{colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    border: 2px solid "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-badge-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-badge-sold-out:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    height: 400px
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
  footer-link:
    color: "{colors.accent-warm}"
    typography: "{typography.link}"
  footer-heading:
    color: "{colors.surface-card}"
    typography: "{typography.title-sm}"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0
    borderBottom: 1px solid "{colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: 0 0 16px 0
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: 1px solid "{colors.hairline}"
    height: 40px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 8px 12px
  add-to-cart-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    height: 64px
    borderTop: 1px solid "{colors.hairline}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: 6px 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Shop Now", and checkout flows. Rendered as a full-width or inline pill with a deep teal-green fill (`{colors.primary}`) and white text (`{colors.on-primary}`). On hover, shifts to a darker shade (`{colors.primary-active}`) with no border or shadow change. The disabled state uses a muted pastel green (`{colors.primary-disabled}`) with white text, signaling the action is unavailable without visual noise.

**`button-secondary`** — An outlined variant used for less prominent actions like "View Details" or "Continue Shopping". It has a white background, dark brown text (`{colors.ink}`), and a subtle border (`{colors.hairline}`). On active state, the background shifts to a soft gray (`{colors.surface-soft}`) and the border adopts the primary green, creating a gentle emphasis without competing with the primary button.

**`button-tertiary`** — A text-only button used for inline actions like "Clear Filters" or "Cancel". It has no background or border, relying solely on the primary green text color. On hover, a soft gray background appears to provide a hit target cue. This button never carries heavy visual weight — it's designed to recede next to primary and secondary buttons.

**`button-warm`** — A secondary accent button using the warm clay tone (`{colors.accent-warm}`) instead of the primary green. Used for promotional banners, seasonal collections, or "Treat Yourself" moments where the brand wants to signal warmth rather than utility. The dark brown ink text (`{colors.ink}`) ensures readability against the warm background.

### Navigation
**`nav-bar`** — A fixed top navigation bar with a clean white background and a soft bottom border (`{colors.hairline-soft}`). It sits 72px tall and contains the brand logo on the left, category links in the center, and utility icons (search, account, cart) on the right. Category links use uppercase, 14px, weight 600 type with 0.5px letter spacing for a refined, editorial feel.

**`nav-link-active`** — The active category link is underlined with a 2px primary green border and uses the primary green text color. This creates a clear, understated indicator of the current section without relying on background fills or heavy visual weight.

**`nav-link-inactive`** — Inactive links use the muted gray (`{colors.muted}`) and lack any underline. On hover, they shift to the ink color (`{colors.ink}`) with a subtle transition, providing feedback without animation excess.

### Cards
**`product-card`** — The core product display unit, used in grid and list views. It has a white background, soft 12px rounded corners (`{rounded.md}`), and contains a product image (rounded at the top corners only), title, price, star rating, and optional badges. On hover, a gentle box shadow lifts the card slightly, creating depth without breaking the flat aesthetic. The card uses body-sm typography for product names and caption for prices.

**`product-card-hover`** — The hover state adds a subtle box shadow (`0 4px 12px rgba(0,0,0,0.08)`) and a slight scale transform (1.01) to create a tactile, elevated feel. No border changes or color shifts occur — the brand trusts shadow depth over color changes for interaction feedback.

### Forms
**`text-input`** — Standard text input used for search, email signup, and address forms. It has a white background, 8px rounded corners (`{rounded.sm}`), a subtle border (`{colors.hairline}`), and 16px body text. On focus, the border thickens to 2px and adopts the primary green, providing a clear but gentle focus indicator. Error states use a red border (`{colors.accent-error}`) with an optional error message in caption type.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a soft gray background (`{colors.surface-soft}`) that blends into the page. On focus, it expands to a white background with a primary green border, creating a clear active state. The placeholder text uses muted gray (`{colors.muted}`) and the input uses body-md type for readability.

### Badges
**`product-badge-sale`** — A small, rectangular badge with a deep red background (`{colors.accent-sale}`) and white uppercase text. Used to flag discounted items. The badge sits in the top-left corner of product images and uses tight padding (2px 8px) to minimize visual intrusion.

**`product-badge-new`** — A green badge (`{colors.primary}`) with white text, used for new arrivals. It follows the same dimensions and placement as the sale badge but uses the brand's primary color to signal freshness rather than urgency.

**`product-badge-sold-out`** — A muted sand-colored badge (`{colors.muted-soft}`) with white text, used for out-of-stock items. The muted tone signals unavailability without creating a negative visual association.

### Footer
**`footer`** — A full-width footer with a dark brown background (`{colors.ink}`) and white text. It contains columns for customer service, about links, social icons, and a newsletter signup. Links use the warm clay accent (`{colors.accent-warm}`) for a touch of warmth against the dark background. Section headings use title-sm type in white, while body links use link typography.

### Accordion
**`accordion-trigger`** — Used in product descriptions, FAQ sections, and mobile navigation. The trigger is a full-width clickable area with no background, title-sm type, and a bottom border (`{colors.hairline-soft}`). On click, the content panel slides open with a smooth transition. The trigger includes a plus/minus icon that rotates on open state.

**`accordion-content`** — The expandable content panel below each accordion trigger. It uses body-md type for readability and has no background or border of its own — it relies on the trigger's bottom border for visual separation.

### Quantity Selector
**`quantity-selector`** — A compact, horizontally arranged control for adjusting item quantities in the cart or on product pages. It has a white background, 8px rounded corners, and a subtle border. The minus and plus buttons sit on either side of the numeric display, with no background of their own. The entire control is 40px tall to align with standard form elements.

### Filter Chips
**`filter-chip`** — Used in collection pages for filtering by size, color, material, or price range. Each chip is a pill with a soft gray background and muted text. When active, the chip fills with the primary green and white text, providing clear visual feedback for the selected filter. Chips are horizontally scrollable on mobile and wrap naturally on desktop.

### Add to Cart Bar
**`add-to-cart-bar`** — A sticky bottom bar that appears on product detail pages on mobile and tablet. It contains the product price on the left and a full-width "Add to Cart" button on the right. The bar has a white background with a top border, sits 64px tall, and ensures the primary action is always accessible without scrolling.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger navigation, sticky add-to-cart bar, accordion-style footer, full-width buttons, reduced hero height (250px) |
| Tablet | 744–1128px | Two-column product grid, visible top nav with condensed links, sticky add-to-cart bar removed, hero height at 350px, filter chips become horizontal scroll |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links, hero at 400px, filter sidebar appears, product cards show hover states |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, hero at 450px, additional whitespace around product cards |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px on mobile and tablet
- Filter chips and badge elements are at least 32px tall for comfortable tapping
- Quantity selector buttons are 40px × 40px minimum
- Nav bar links have 48px tap targets even if text is smaller

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile (< 744px), with the logo centered and cart/account icons remaining visible
- Product filters collapse into a bottom sheet or modal on mobile and tablet
- Footer columns collapse into an accordion pattern on mobile, with only section headings visible by default
- Product image galleries collapse from thumbnail strip to single-image swipe on mobile
- Multi-column product grids collapse to single column on mobile, two columns on tablet

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hover and focus states for all interactive elements (colors, shadows, transitions) could not be reliably extracted from the live site
- Error state styling for forms (border colors, icon placement, message typography) is inferred from common patterns rather than verified
- Dark mode or high-contrast mode specifications are not present in the current site
- Sub-brand or seasonal palette variations (holiday, clearance, collaboration) are not documented
- Animation timing and easing curves (transitions, hover effects, page loads) are not specified
- Specific icon set details (SVG library, stroke widths, sizes) are not captured
- Typography scale for mobile viewports (smaller display sizes, adjusted line heights) is not verified
- Checkout flow specific components (progress bar, payment forms, order summary) are not documented
- Accessibility specifications (focus rings, aria labels, color contrast ratios) are not confirmed
- Print stylesheet specifications are not available
