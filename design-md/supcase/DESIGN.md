---
version: alpha
name: "Supcase"
source_url: "https://www.supcase.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A black-on-black-on-black design system where #111111 is the canvas, the ink, and the primary — a monochrome fortress built for the drop-and-scrape reality of phone cases. The brand's tagline "Gear Up. Stay Unbreakable." is literal: the site wraps everything in near-black surfaces (#111111) with silver-gray accents (#d1d1d1, #dcdcdc) that read as metal edges on a rugged case. HelveticaNeueLTStd-BlkCn at 700 weight drives display headlines with a compressed, authoritative punch — the kind of type that looks like it was stamped into aluminum. Roboto Condensed handles body copy, keeping the mechanical precision while adding readability. Buttons are chunky and pill-shaped ({rounded.full}) in #111111 with white text, or outlined in #d1d1d1 for secondary actions. The product grid uses soft white cards ({rounded.sm}) against a #f9f9f9 background, letting the black cases pop in product photography. There is no color warmth here — no blues, no reds, no gradients. The palette is intentionally industrial: black, white, and three shades of silver. This is a system that says "we don't need to be pretty, we need to survive a 6-foot drop."

colors:
  primary: "#111111"
  primary-active: "#000000"
  primary-disabled: "#555555"
  ink: "#111111"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d1d1d1"
  hairline-soft: "#dcdcdc"
  canvas: "#f9f9f9"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-silver: "#d1d1d1"
  accent-silver-light: "#dcdcdc"
  badge-new: "#111111"
  badge-sale: "#cc0000"
  rating-star: "#111111"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'HelveticaNeueLTStd-BlkCn', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'HelveticaNeueLTStd-BlkCn', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'HelveticaNeueLTStd-BlkCn', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Roboto Condensed', 'Roboto', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto Condensed', 'Roboto', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto Condensed', 'Roboto', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Roboto Condensed', 'Roboto', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto Condensed', 'Roboto', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Roboto Condensed', 'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto Condensed', 'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Roboto Condensed', 'Roboto', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Roboto Condensed', 'Roboto', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
    color: "#cc0000"

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
    rounded: "{rounded.full}"
    padding: 14px 32px
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
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 0
    border: "none"
    borderBottom: "2px solid transparent"
  button-tertiary-active:
    borderBottom: "2px solid {colors.ink}"
  button-pill-silver:
    backgroundColor: "{colors.accent-silver}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  top-nav-logo:
    height: 32px
  top-nav-cart-icon:
    color: "{colors.ink}"
    height: 24px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focused:
    border: "1px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.accent-silver-light}"
  hero-banner-cta:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 48px
  category-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  category-card-active:
    border: "2px solid {colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.accent-silver-light}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.accent-silver-light}"
  footer-link-hover:
    color: "{colors.on-primary}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
  rating-stars:
    color: "{colors.rating-star}"
    size: 16px
    gap: "{spacing.xxs}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. A solid #111111 pill with white uppercase Roboto Condensed text at 16px/600 weight. Used for "Add to Cart", "Shop Now", and checkout flows. On hover, shifts to pure black (#000000). Disabled state uses #555555 with reduced opacity. The pill shape ({rounded.full}) and uppercase letter-spacing give it a stamped, industrial feel.

**`button-secondary`** — An outlined variant with a 2px solid #111111 border on a transparent background. Same pill shape and typography as primary. Used for "Learn More", "View Details", and secondary product actions. Active state fills with #111111 and inverts text to white.

**`button-tertiary`** — A text-only link with an underline-on-hover effect. No background, no border radius. Used for "See All", navigation links, and inline actions. Active state shows a 2px bottom border in #111111.

**`button-pill-silver`** — A silver (#d1d1d1) pill button for less prominent actions like filter resets or secondary navigation. Uses smaller uppercase type at 14px.

**`icon-button`** — A 40x40 circular button with no background and an icon in #111111. Used for cart, search, and menu toggles. Hover adds a subtle background tint.

### Navigation
**`top-nav`** — A 64px fixed header on a white (#f9f9f9) canvas with a soft bottom border (#dcdcdc). Contains the SUPCASE logo (32px height), nav links in uppercase Roboto Condensed 14px/600, and a cart icon. Nav links are spaced generously with {spacing.lg} between items. The cart icon sits at 24px with a badge count in #111111.

**`top-nav-logo`** — The brand wordmark rendered at 32px height, typically in #111111 or white depending on the header variant. On dark hero sections, the logo inverts to white.

### Cards
**`product-card`** — A white card with 4px rounded corners ({rounded.sm}) and no border — relies on the #f9f9f9 canvas background for separation. Contains a 1:1 aspect ratio product image with top-rounded corners, a title in Roboto Condensed 16px/600, and a price in 18px/700. Sale prices render in #cc0000. A badge overlay (black or red) sits at the top-left corner for "NEW" or "SALE" indicators.

**`category-card`** — A white card with a 1px #dcdcdc border and 4px rounded corners. Contains a category image and title in Roboto Condensed 18px/600. Active state thickens the border to 2px #111111. Used for device model selection (iPhone 15, Samsung Galaxy S24, etc.).

### Forms
**`search-bar`** — A pill-shaped input field on a #f5f5f5 background with a 1px #dcdcdc border. 40px height with 16px horizontal padding. Focus state swaps the border to #111111. Placeholder text in #666666.

**`newsletter-input`** — A full-height pill input on white background with a #d1d1d1 border. 48px height. Paired with a solid black pill submit button.

**`quantity-selector`** — A compact 40px row with a border (#d1d1d1) and 4px rounded corners. Contains a minus button, the quantity number, and a plus button. Each button is 40x40 with no background.

### Hero
**`hero-banner`** — A full-width section on a #111111 background with white text. Uses display-xl (36px/700) for the headline and Roboto 16px for the subtitle in #dcdcdc. A white pill CTA button provides the primary action. Padding is generous at 64px vertical and 32px horizontal.

### Footer
**`footer`** — A #111111 background section with silver-gray (#dcdcdc) links and body text. Contains link columns, a newsletter signup, and social icons. Links hover to white. Padding matches the hero at 64px vertical.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card), hamburger menu replaces top nav links, hero text reduces to 24px, category cards stack vertically, footer collapses to single column |
| Tablet | 744–1128px | Two-column product grid (2 cards), top nav links visible but condensed, hero text at 28px, category cards in 2-column grid, footer in 2 columns |
| Desktop | 1128–1440px | Three-column product grid (3 cards), full top nav with all links, hero at 36px, category cards in 3-column grid, footer in 4 columns |
| Wide | > 1440px | Four-column product grid (4 cards), max-width container at 1440px centered, hero full-width with max-width content, category cards in 4-column grid |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Icon buttons are 40x40px (slightly below ideal but consistent with industry standards)
- Quantity selector buttons are 40x40px with adequate spacing
- Product card tap targets cover the full card area
- Nav links have 44px minimum tap area

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport shrinks
- Category cards follow the same column reduction
- Footer link columns stack vertically below 744px
- Hero banner reduces font size and padding on mobile
- Search bar remains visible but reduces width on mobile
- Cart icon persists across all breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is heavily monochrome (blacks, whites, grays) with no distinctive brand accent color. The #d1d1d1 and #dcdcdc values may be generic UI borders rather than intentional brand colors. The true brand identity may include a secondary accent (possibly red for sale badges, which we've inferred from common ecommerce patterns) that wasn't captured in extraction.
- Font sizes and weights for display and body typography are inferred from common usage patterns — the exact hierarchy may differ on the live site.
- Hover and focus states for most components (except buttons) are estimated based on industry standards rather than extracted data.
- Error states, form validation styling, and disabled input styling are not extracted.
- The checkout flow (Shopify-powered) likely uses a separate design system that we haven't captured.
- Dark mode support is not confirmed — the site's heavy use of black suggests it may already be dark-mode native.
- Animation and transition durations (hover fades, card entrance animations) are not documented.
- The badge system (NEW, SALE, BEST SELLER) colors beyond black and red are speculative.
- Social media icon colors and hover states are not extracted.
- Mobile navigation drawer styling (background, animation, link hierarchy) is not captured.
- The product quick-add or variant selector UI (color swatches, size pickers) is not documented.
