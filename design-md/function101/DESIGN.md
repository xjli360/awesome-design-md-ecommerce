---
version: alpha
name: "Function101"
source_url: "https://www.function101.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A workspace-organization brand that lives in the gap between Apple’s industrial precision and the mess of real cables, using a muted slate palette anchored on #919da9 — a warm gray that reads as engineered rather than sterile. The brand’s signature voltage is #108474, a deep teal that appears on every primary CTA, add-to-cart button, and checkout link, giving the storefront a calm, authoritative pulse against the predominantly gray canvas (#f1f1f1, #f5f5f5, #eeeeee). Type runs Montserrat at moderate weights — display headlines sit at 24–32px in weight 600 rather than heavy 700+, letting product photography and clean whitespace carry the hierarchy. Product cards use soft corners ({rounded.sm} ~8px) and subtle hairline borders (#d9d9d9), while the search bar and primary buttons adopt a slightly more rounded form ({rounded.md} ~12px). The brand avoids hard corners entirely, preferring a gentle radius that suggests approachability rather than cold utility. A secondary accent of #75bcfb (a muted sky blue) appears on secondary actions and informational badges, while #d6001c serves as a restrained error/alert red — used sparingly, never as a primary brand color. The overall mood is organized but not minimalist: there’s enough gray variation (#898989, #7b7b7b, #5d6b82, #444749) to create depth without noise, and the teal acts as a wayfinding color across the navigation, footer links, and product highlights. The brand’s Shopify platform means checkout flows inherit standard Shopify UI patterns, but the product pages and collection grids feel purpose-built for the Apple ecosystem — clean, centered, with generous padding ({spacing.lg} and {spacing.xl}) around every element.

colors:
  primary: "#108474"
  primary-active: "#0d6b5c"
  primary-disabled: "#a3d4c5"
  ink: "#202020"
  body: "#444749"
  muted: "#7b7b7b"
  muted-soft: "#919da9"
  hairline: "#d9d9d9"
  hairline-soft: "#e9eaec"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#75bcfb"
  accent-blue-active: "#4a90e2"
  error-red: "#d6001c"
  error-red-active: "#b00015"
  star-rating: "#3d361e"
  badge-teal: "#108474"
  badge-gray: "#919da9"
  footer-bg: "#f1f1f1"
  scrim: "#000000"

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
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
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
    fontWeight: 500
    lineHeight: 1.38
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
    lineHeight: 1.38
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
    letterSpacing: 0.3px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.1px
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
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 16px
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-pill-teal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1:1"
    objectFit: "contain"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.md} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.error-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-info:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
    padding: "{spacing.xs} 0"
  footer-link-hover:
    color: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.none}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xl} {spacing.lg} {spacing.base} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline-soft}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  cart-total:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
    width: "100%"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand’s teal (#108474) with white text and a soft 8px radius. Used for "Add to Cart," "Subscribe," and primary checkout actions. On hover, shifts to a darker teal (#0d6b5c) with no border change. Disabled state uses a muted teal (#a3d4c5) with white text, signaling the action is unavailable without visual noise.

**`button-secondary`** — A bordered variant on a white background with dark ink text and a 1px hairline border (#d9d9d9). Used for "Learn More," "View Details," and secondary form actions. Active state fills the background with surface-soft (#f5f5f5) and darkens the border to muted (#7b7b7b). No text color change on hover — the border does the work.

**`button-tertiary-text`** — A text-only button with no background or border, using the primary teal for text. Used for "Cancel," "Clear Filters," and inline navigation links within cards. Hover state adds no underline — the brand trusts the color shift to communicate interactivity.

**`button-accent-blue`** — A smaller, lower-contrast button using the muted sky blue (#75bcfb) background with dark ink text. Used for informational actions like "Learn More About Compatibility" or "View Specs." Active state shifts to the darker blue (#4a90e2). Height is 36px, making it suitable for inline placement within product descriptions.

**`button-pill-teal`** — A fully rounded pill variant of the primary button, used sparingly for promotional CTAs like "Shop the Sale" or "Get 10% Off." Uses the same teal background and white text but with full rounding and slightly tighter padding (10px 20px) for a more compact, badge-like appearance.

### Cards
**`product-card`** — The core product display unit, a white card with a 1px soft hairline border (#e9eaec) and 8px rounded corners. Contains a square aspect-ratio image (object-fit: contain) at the top, followed by the product title in title-sm weight 500 and the price in body-md weight 400. No padding on the card itself — internal spacing is handled by child elements. On hover, the border shifts to a stronger hairline (#d9d9d9) and a subtle box shadow (0 2px 8px rgba(0,0,0,0.08)) lifts the card.

**`product-card-image`** — The image container within a product card, using object-fit: contain to preserve product proportions without cropping. The top two corners inherit the card’s 8px radius; bottom corners are square to meet the text area cleanly. Aspect ratio is 1:1 for consistency across the grid.

**`product-card-title`** — The product name line within a card, set in title-sm (16px, weight 500) with dark ink color. Padded 12px from the left and right, with 12px top margin from the image. No truncation — the brand prefers natural line breaks for longer product names.

**`product-card-price`** — The price line below the title, set in body-md (16px, weight 400) with body color (#444749). Padded 4px top from the title, 16px bottom from the card edge. Sale prices are handled by wrapping in a badge-sale component rather than changing the price text color.

### Navigation
**`top-nav`** — The primary navigation bar, a white strip 72px tall with a 1px soft hairline bottom border (#e9eaec). Contains the brand logo on the left, nav links in uppercase Montserrat weight 600 at 14px with 0.5px letter-spacing, and utility icons (search, cart, account) on the right. The bar is fixed at the top on desktop, collapsing into a hamburger menu on mobile.

**`nav-link-active`** — The active state for navigation links, using the primary teal (#108474) for text color. No underline or background change — the color shift alone signals the current page. Uppercase tracking is preserved from the base nav-link typography.

**`nav-link-inactive`** — The default state for navigation links, using muted gray (#7b7b7b) text. On hover, links shift to the primary teal. No background fill or border decoration — the brand relies on color and typography weight for hierarchy.

### Forms & Inputs
**`search-bar`** — The site search input, rendered as a 44px tall field with a surface-soft background (#f5f5f5), 1px hairline border (#d9d9d9), and 8px rounded corners. Text is body-sm (14px, weight 400) in body color (#444749). Padding is 10px 16px. On focus, the background shifts to white and the border changes to the primary teal (#108474), creating a clear active state without outline interference.

**`quantity-selector`** — A compact input for adjusting cart quantities, 40px tall with white background, 1px hairline border, and 8px rounded corners. Contains a numeric value centered between minus and plus buttons. The buttons are icon-button-circle components (36px, surface-soft background) placed at each end. Border shifts to primary teal on focus.

### Badges & Labels
**`badge-new`** — A small uppercase label in teal (#108474) with white text, 11px weight 600, 0.3px letter-spacing, and 4px rounded corners. Padding is 2px 8px. Used to flag newly added products or collections. The teal matches the primary brand color, creating visual consistency with CTAs.

**`badge-sale`** — A sale indicator in the brand’s error red (#d6001c) with white text, using the same typography and sizing as badge-new. Used sparingly — only for genuine markdowns, not as a decorative element. The red is the only high-saturation color in the badge system, ensuring it draws attention appropriately.

**`badge-info`** — An informational badge in the muted sky blue (#75bcfb) with dark ink text. Used for compatibility notes, "Free Shipping" indicators, or "Eco-Friendly" labels. The blue is the softest of the badge colors, signaling supplementary rather than urgent information.

### Footer
**`footer-section`** — The site footer, a full-width strip with footer-bg background (#f1f1f1) and body color text. Padding is 48px top/bottom and 24px left/right. Contains columns for product categories, customer support, company info, and social links. Typography is body-sm (14px, weight 400) for most text, with column headers in title-sm (16px, weight 500).

**`footer-link`** — Individual links within footer columns, set in link typography (14px, weight 500) with muted color (#7b7b7b). Each link has 4px vertical padding for comfortable touch targets. On hover, the color shifts to the primary teal (#108474). No underline decoration — the color change is sufficient.

### Hero & Collection
**`hero-banner`** — The primary hero section on the homepage and collection pages, using a surface-soft background (#f5f5f5) with dark ink text. Content is centered with 64px top/bottom padding and 24px left/right. The headline uses display-lg (28px, weight 600) with a supporting subtitle in body-md (16px, weight 400). A single hero-cta button sits below the text.

**`hero-cta`** — The call-to-action button within hero banners, slightly larger than the standard button-primary at 48px tall with 14px 32px padding. Uses the same teal background and white text but with more generous horizontal padding to anchor the hero composition. The 8px rounded corners match the rest of the button system.

**`collection-header`** — The header area above product grids on collection pages, a white strip with a 1px soft hairline bottom border. Contains the collection title in display-md (24px, weight 600) and optional description in body-md. Padding is 32px top, 24px left/right, 12px bottom. Sorting and filter controls sit below the header, aligned to the right.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu; product grid switches to 1 column; hero banner padding reduces to 32px top/bottom; search bar moves to a full-width overlay; footer columns stack vertically; product card images reduce to 3:4 aspect ratio |
| Tablet | 744–1128px | Top nav remains expanded but with reduced link spacing; product grid uses 2 columns; hero banner uses 48px padding; search bar remains in nav but shrinks to 36px height; footer uses 2-column layout |
| Desktop | 1128–1440px | Full top nav with all links visible; product grid uses 3 columns; hero banner at full 64px padding; search bar at 44px height; footer uses 4-column layout; product cards show hover shadow effects |
| Wide | > 1440px | Max-width container at 1440px with auto margins; product grid can expand to 4 columns if content allows; hero banner content max-width at 1128px centered; all other layouts scale proportionally |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons are 36px on desktop, 44px on mobile (with increased padding)
- Navigation links have 8px vertical padding on mobile to create 48px touch targets
- Quantity selector buttons are 40px tall with 12px internal padding
- Footer links have 12px vertical padding on mobile for comfortable tapping

### Collapsing Strategy
- Top navigation collapses to a hamburger menu at < 744px, with the menu panel sliding in from the left
- Product grid collapses from 3 columns to 2 at tablet, then 1 at mobile
- Footer columns collapse from 4 to 2 at tablet, then stack vertically at mobile
- Hero banner reduces vertical padding by 50% at mobile to conserve screen space
- Search bar transforms from inline to full-screen overlay at mobile, with auto-focus on open
- Product card hover effects (shadow, border change) are disabled at mobile — touch states use active color shifts instead
- Collection filters collapse into a slide-out drawer at mobile, with a "Filter" button toggling visibility

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components were inferred from common patterns rather than extracted from the live site — the extracted CSS did not include :hover pseudo-class styles
- Active/focus states for text inputs and quantity selectors were inferred — the live site may use different border colors or shadow treatments
- Error styling (form validation, error messages, input error states) was not extractable — the error red (#d6001c) is present in the palette but its application context is assumed
- Dark mode is not implemented on the live site — no dark-mode media queries or color variables were found
- The font-family "JudgemeStar" was found in extracted CSS but appears to be a third-party widget font (for review stars), not a brand typeface — it is excluded from the typography system
- The brand’s logo typeface could not be determined — it may use a custom wordmark or a different weight of Montserrat
- Sub-brand or collection-specific color variations (e.g., limited edition palettes) were not extractable
- The extracted color list includes many grays that may be Shopify default UI colors rather than intentional brand choices — the palette above selects the most frequently occurring and distinctive values
- Spacing values for components were estimated based on common e-commerce patterns and extracted element dimensions — exact pixel values may vary on the live site
- The "object-fit: contain" declaration was found in extracted CSS and is used for product images, but its exact container sizing is inferred
