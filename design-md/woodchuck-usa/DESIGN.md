---
version: alpha
name: "Woodchuck USA"
source_url: "https://www.woodchuckusa.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand built on the warmth of natural wood grain against a near-black digital backdrop (#111111), where the primary green (#108474) reads less like a corporate accent and more like the patina of a well-worn leather journal. The site operates as a gift-and-accessories marketplace for customizable wooden products—flasks, watches, phone cases, and journals—and the design language mirrors the material: substantial, grounded, and slightly muted. The palette leans heavily on a spectrum of grays (#444444, #7b7b7b, #555555, #323232) that create a quiet hierarchy against the white canvas (#fafafa, #f9fafb, #f5f5f5), while the primary green appears in CTAs, navigation accents, and product badges. A secondary marigold (#fbcd0a) surfaces sparingly—perhaps for sale tags or star ratings—adding a single note of brightness. Typography runs Montserrat and Open Sans, with Montserrat likely carrying headings in a clean, slightly geometric weight, and Open Sans handling body copy for readability. The interface avoids hard corners entirely, using {rounded.sm} for buttons and cards, and {rounded.full} for search inputs and icon orbs. The Shopify platform underpins the experience, so checkout flows inherit those widget colors (#7367f0 for Shop Pay, etc.), but the brand's own visual system stays firmly in the wood-and-ink register. Product cards use generous whitespace, a single product image, and a subtle hairline (#dedede) to separate items, while the footer stacks utility links in a dense, muted grid. The overall effect is that of a specialty workshop's storefront: warm, unpretentious, and focused on the object rather than the interface.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#a3d5c9"
  ink: "#111111"
  body: "#444444"
  muted: "#7b7b7b"
  muted-soft: "#73706d"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#fafafa"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#fbcd0a"
  accent-purple: "#7367f0"
  dark-surface: "#23222a"
  dark-canvas: "#121212"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
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
    padding: 12px 24px
    height: 44px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px rgba(16,132,116,0.2)"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-bar-icon:
    textColor: "{colors.muted}"
    height: 20px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
  icon-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  badge-sale:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.body}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Customize Now", and checkout initiation. Rendered in the brand green (#108474) with white uppercase Montserrat text at 14px/600 weight. The {rounded.sm} corners keep the button feeling approachable but not pill-soft. On hover, the background shifts to `{colors.primary-active}` (#0d6b5d) for a subtle depth cue; disabled state uses `{colors.primary-disabled}` (#a3d5c9) with reduced opacity.

**`button-secondary`** — Used for secondary actions like "View Details" or "Continue Shopping". White background with dark ink text, matching the same 44px height and uppercase treatment as the primary. An outlined variant (`button-secondary-outline`) uses a transparent background with a 2px solid `{colors.primary}` border for cases where the secondary action needs brand color without full fill.

**`button-pill`** — A compact, fully rounded variant reserved for filter tags, category pills, and mobile navigation toggles. Uses smaller 12px uppercase text and tighter padding (10px 20px) to fit into constrained spaces like the category strip or mobile menu.

### Cards
**`product-card`** — The core product display unit, a white card with no internal padding (image sits flush to top edges) and {rounded.sm} corners. The product image fills the top half with matching top-radius rounding, while title, price, and any badges stack below with 12px padding. The card uses a subtle `{colors.hairline}` border on hover to indicate interactivity. Price is set in body-md weight 400 to avoid competing with the product title's 500 weight.

**`product-card-badge`** — A small marigold (#fbcd0a) label pinned to the top-left of the product image, used for "Sale" or "Best Seller" indicators. The `{typography.badge}` style (11px/700/uppercase) ensures readability at small sizes without overwhelming the product photo.

### Navigation
**`nav-bar`** — A fixed 72px header on white canvas, containing the brand logo (left), category links (center), and utility icons (search, account, cart — right). The nav uses `{typography.nav-link}` at 14px/500 with 0.3px letter spacing for a slightly refined feel. Active or hovered links drop to a 2px `{colors.primary}` bottom border. On scroll, the nav gains a subtle `boxShadow` for visual separation from content.

**`nav-link-active`** — The active state for navigation items, distinguished by the brand green underline. This is the primary wayfinding cue in the header, as the site avoids heavy background color changes.

### Forms
**`text-input`** — Standard form input for search, account forms, and checkout fields. White background with 12px padding and {rounded.sm} corners. On focus, a 2px `{colors.primary}` ring appears via `boxShadow` for clear keyboard navigation. The placeholder text uses `{colors.muted}` (#7b7b7b) for legibility without competing with entered text.

**`search-bar`** — A pill-shaped search input with a soft gray background (`{colors.surface-soft}` #f5f5f5), used in the header and mobile menu. The full rounding and lack of border make it feel integrated into the surface rather than a separate field. A search icon sits at the left edge in `{colors.muted}`.

### Footer
**`footer`** — A dark section anchored in `{colors.dark-surface}` (#23222a), with white headings and muted gray (#73706d) link text. The footer stacks 4-5 columns of utility links (Shop, Support, About, Legal) with generous `{spacing.section}` padding top and bottom. Social icons appear as `{icon-button}` circles in `{colors.surface-soft}` against the dark background.

### Badges & Indicators
**`badge-sale`** — Marigold (#fbcd0a) badge for promotional pricing, using the same `{typography.badge}` style. The warm yellow provides high contrast against both white cards and dark product images.

**`badge-new`** — Green (#108474) badge for new arrivals or limited editions, using white text for contrast. This badge shares the same shape and typography as the sale badge but uses the brand primary color to signal freshness rather than discount.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; search bar moves to mobile drawer; footer stacks to single column; hero section reduces padding to 32px |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories only; search bar remains visible but compact; footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav with all categories; search bar at full width; footer uses 4-column layout |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px centered; hero section uses full-width background with content constrained |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Icon buttons (search, cart, account) use 40px diameter circles with adequate tap area
- Product card links extend to full card area for easy tapping
- Nav links in mobile menu use 48px touch targets with adequate spacing
- Quantity selector buttons use 44px minimum touch area

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px, with a slide-in drawer for full category access
- Product filters collapse to a "Filter" button that opens a modal overlay on mobile
- Footer columns collapse to a single vertical stack with expandable sections (accordion pattern) below 744px
- Hero section reduces headline size from 36px to 28px on mobile, with reduced padding
- Product images switch from landscape to square aspect ratio on mobile for better vertical space usage

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for secondary buttons, text inputs, and links could not be reliably extracted from the live site CSS; the values provided are best-practice estimates based on the brand palette
- Error state styling for forms (validation colors, error message typography) was not visible in the extracted data; a red accent (#c13515 or similar) is assumed but not confirmed
- The exact font weights for Montserrat and Open Sans across different text levels are inferred from common Shopify implementations; the live site may use different weight combinations
- Dark mode styling is not present in the extracted data; the `dark-surface` and `dark-canvas` colors are inferred from footer and meta theme-color values
- Sub-brand or collection-specific color palettes (e.g., limited edition wood finishes) could not be extracted
- The accent-purple (#7367f0) is likely a Shopify Pay widget color rather than a brand color; it is included as a token but should be validated against actual brand usage
- Star rating and review widget styling (JudgemeStar font found) could not be fully mapped; colors and spacing for review components are estimated
- Animation durations, easing curves, and transition properties were not extractable from static CSS analysis
- The exact `letterSpacing` values for typography tokens are estimated based on common brand implementations; the live site may use tighter or looser tracking
