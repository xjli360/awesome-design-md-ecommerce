---
version: alpha
name: "Anker"
source_url: "https://www.anker.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep blue-black canvas of #080a0f — the color of a phone screen in standby — grounds a brand that sells the promise of never being unpowered. The extracted palette is dominated by a cold, technical spectrum: #1d1d1f ink, #75787f muted steel, and a single electric accent in #00befa that reads like a charging indicator LED. Anker's typography stack is pure system — Apple's San Francisco (-apple-system, Helvetica Neue) and monospace fallbacks (SFMono-Regular, Consolas) — suggesting a brand that doesn't editorialize with type but lets product photography and spec sheets carry the story. Buttons use {rounded.full} pill shapes at 48px height, a shape borrowed from the charging cables and power banks themselves. The secondary accent cluster — #00db84 (charging-complete green), #ff9900 (warning amber), #da3c3c (error red) — maps directly to battery-status semantics. This is a brand that thinks in voltage, capacity, and uptime: the hero section is likely a dark-field product shot with a glowing ring or LED strip, not a lifestyle scene. The Shopify platform backbone means checkout components (PayPal blue, Klarna pink) leak into the palette, but the core Anker identity is the black field and the cyan pulse.

colors:
  primary: "#00befa"
  primary-active: "#10b5ec"
  primary-disabled: "#6d9ebf"
  ink: "#1d1d1f"
  body: "#75787f"
  muted: "#9ca3af"
  muted-soft: "#e2e2e2"
  hairline: "#e4e5e6"
  hairline-soft: "#f1f3f5"
  canvas: "#080a0f"
  surface-soft: "#f5f5f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#f2f2f2"
  battery-green: "#00db84"
  warning-amber: "#ff9900"
  error-red: "#da3c3c"
  badge-cyan: "#22b8cf"
  badge-green: "#37b679"
  link-blue: "#0070f3"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  spec-value:
    fontFamily: "SFMono-Regular, Consolas, 'Liberation Mono', Menlo, Courier, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
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
  section: 80px

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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: 2px solid "{colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-dark-active:
    backgroundColor: "#1a1a1f"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 24px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.error-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 44px
    border: 1px solid "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.error-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-eco:
    backgroundColor: "{colors.battery-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
  spec-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  spec-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: 48px 0
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-dark}"
  footer-link-hover:
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    padding: 80px 0
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subheadline:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  rating-stars:
    color: "{colors.warning-amber}"
    size: 16px
  progress-bar-track:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px

## Components

### Buttons
**`button-primary`** — The primary call-to-action on light backgrounds. Uses the cyan #00befa as a full fill with white text in a pill shape ({rounded.full}). On hover, shifts to #10b5ec. Disabled state drops to a muted blue-gray. Used for "Add to Cart", "Shop Now", and "Learn More" across product pages and hero sections.

**`button-secondary`** — An outlined variant for secondary actions on light backgrounds. Transparent fill with a 2px cyan border and cyan text. On hover, fills solid cyan. Used for "Compare Models", "View Details", and "Read Reviews".

**`button-dark`** — The primary CTA on the dark canvas background. Uses the dark canvas fill with light text. On hover, lightens slightly to #1a1a1f. Used in hero sections and dark-themed promotional blocks.

**`button-ghost`** — A text-only button with no background or border. Used for "Cancel", "Skip", and tertiary navigation actions. On hover, may add a subtle background tint.

### Cards
**`product-card`** — A white card with {rounded.md} corners and 16px padding. Contains a square product image with {rounded.sm}, title, price, rating stars, and action buttons. On hover, elevates with a subtle box shadow. Used across collection pages, search results, and recommended product grids.

**`product-image`** — Square aspect ratio container with soft rounded corners. May include a "NEW", "SALE", or "ECO" badge overlaid in the top-left corner. Badges use the {badge} typography with brand-specific background colors.

### Navigation
**`nav-bar`** — A fixed 64px bar on the dark canvas background. Contains the Anker logo on the left, nav links in the center, and search/cart icons on the right. Nav links use {nav-link} typography and turn cyan on hover/active. On mobile, collapses to a hamburger menu.

**`search-bar`** — A pill-shaped input field on white background with 44px height. Used in the nav bar on desktop and as a full-width element on mobile. On focus, the border becomes cyan.

### Forms
**`text-input`** — Standard 48px input with 12px padding and {rounded.sm} corners. Default border is {hairline}. On focus, gets a 2px cyan border. Error state uses a red border. Used in checkout forms, account settings, and contact pages.

### Badges
**`badge-new`** — Cyan background with white uppercase text. Used to mark newly released products. **`badge-sale`** — Red background for discounted items. **`badge-eco`** — Green background for environmentally friendly products (e.g., solar chargers, recycled packaging).

### Spec Table
**`spec-table`** — A light gray (#f5f5f7) container with {rounded.sm} corners and 16px padding. Contains rows of spec labels and values. Labels use {caption} typography in muted gray. Values use monospace {spec-value} typography in dark ink. Used on product detail pages to display technical specifications like wattage, capacity, dimensions, and weight.

### Progress Bar
**`progress-bar-track`** — A 4px tall pill-shaped track in light gray. **`progress-bar-fill`** — The cyan fill that animates to show charging progress, battery level, or loading state. Used in product detail pages for battery indicators and in checkout for step progress.

### Quantity Selector
**`quantity-selector`** — A compact 40px control with decrement and increment buttons flanking a numeric display. Used on cart and product detail pages. Buttons are square with {rounded.sm} corners.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text shrinks to 28px; search bar becomes full-width; spec tables stack vertically; quantity selector becomes full-width |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero text at 36px; search bar in nav; spec tables in two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav; hero text at 48px; search bar in nav; spec tables in two columns |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero text at 48px with larger margins |

### Touch Targets
- All buttons and interactive elements minimum 44px height
- Nav bar links minimum 44px tap area
- Quantity selector buttons 40px x 40px
- Product card tap area covers entire card
- Search bar minimum 44px height

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Product grid collapses from 4 columns to 1 column on mobile
- Spec tables collapse from two-column layout to stacked single column
- Footer links collapse from multi-column to single-column accordion
- Hero section reduces padding from 80px to 40px on mobile
- Search bar moves from nav to full-width below nav on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted colors include many Shopify checkout widget colors (Klarna pink #f81ce5, PayPal blue #0070f3, Afterpay green #37b679) that are not part of Anker's brand palette — these should be excluded from production use
- Font family declarations are entirely system stack; no custom brand font was detected on the live site
- Hover and active states for most components are inferred from common patterns, not extracted from the live site
- Error state styling for forms (red border) is assumed from the presence of #da3c3c in the palette
- Dark mode variant is not defined; the brand uses a dark canvas (#080a0f) as its primary background but may also have light mode pages
- Sub-brand palettes (e.g., Anker Soundcore, Anker PowerCore, AnkerWork) may have distinct color systems not captured here
- Typography scale (font sizes, weights, line heights) is estimated from common e-commerce patterns and the brand's technical positioning; not extracted from the live site
- Animation and transition durations are not specified
- Product card shadow values are estimated
- Rating star component color (#ff9900) is assumed from the warning-amber in the palette
- The extracted palette is heavily weighted toward generic web blues and grays; the most distinctive brand color is #00befa (cyan), which is used as primary
