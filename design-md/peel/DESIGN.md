---
version: alpha
name: "Peel"
source_url: "https://www.buypeel.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A teal #108474 so deep and saturated it reads like oxidized copper — that single hex is the brand's entire argument for why a phone case can be both minimal and memorable. Peel's visual system is a study in reduction: product photography floats on #eeeeee canvases, text runs in Barlow at modest weights, and the only decorative flourish is the occasional Baskerville italic for a product name. The site reads like a magazine spread that happens to sell accessories — generous margins, full-bleed hero images, and a checkout flow that inherits Shopify's default #5c5f62 gray for form labels rather than introducing a custom palette. What makes Peel distinctive is what it refuses to do: no gradients, no drop shadows, no badge explosions. The primary CTA is a flat teal rectangle with white text, and the secondary action is an underlined link — no outline buttons, no pill shapes. Product cards use `{rounded.xs}` (4px) corners, barely perceptible, preserving the sharpness of the phone silhouette. The brand's secondary accent, a warm gold #fbcd0a, appears only in the star-rating widget and a single promotional banner, never competing with the teal. Typography stays in a tight range: 14–16px body, 20–24px display, with line heights never exceeding 1.5. The nav bar is a thin 48px strip, the logo sits left in Barlow Medium, and the cart icon is the only right-side element. Every design decision reads as "we edited until nothing remained to take away."

colors:
  primary: "#108474"
  primary-active: "#0d6b5e"
  primary-disabled: "#a3d5cc"
  ink: "#222222"
  body: "#3a3a3a"
  muted: "#626262"
  muted-soft: "#9e9e9e"
  hairline: "#cfcfcf"
  hairline-soft: "#e0e0e0"
  canvas: "#eeeeee"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  star-gold: "#fbcd0a"
  error-red: "#c13515"
  success-green: "#108474"

typography:
  display-xl:
    fontFamily: "'Barlow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Barlow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Barlow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Barlow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Barlow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Barlow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Barlow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Barlow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Barlow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Barlow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Barlow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Barlow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    rounded: "{rounded.none}"
    padding: 0
    height: auto
  button-secondary-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 40px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.error-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
    padding: 0 24px
  nav-logo:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 0
  product-card-image:
    rounded: "{rounded.xs}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-card-rating:
    color: "{colors.star-gold}"
    fontSize: 14px
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.base}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.surface-card}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.error-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 40px
    border: 1px solid "{colors.hairline}"
  cart-icon:
    color: "{colors.ink}"
    fontSize: 20px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    height: 36px
    border: 1px solid "{colors.hairline}"

## Components

### Buttons
**`button-primary`** — The single call-to-action style across the site. A flat teal rectangle with white uppercase Barlow Medium text. No border-radius, no shadow, no icon. On hover, the background shifts to `{colors.primary-active}` (#0d6b5e). The disabled state uses `{colors.primary-disabled}` (#a3d5cc) with white text. Height is 44px with 12px vertical padding and 24px horizontal.

**`button-secondary`** — Not a bordered outline button but a text link styled as an action. Uses `{typography.link}` — underlined Barlow Regular 14px in `{colors.primary}`. No padding, no background, no border. On hover, the text color shifts to `{colors.primary-active}`. Used for "View Details" and "Continue Shopping" links.

### Cards
**`product-card`** — A minimal product display with a white background and 4px rounded corners. The product image fills the top with the same `{rounded.xs}`. Below, the title uses `{typography.title-sm}` in `{colors.ink}`, the price uses `{typography.body-sm}` in `{colors.muted}`, and the star rating renders in `{colors.star-gold}` (#fbcd0a). No border, no shadow — the card is distinguished only by its placement on the `{colors.canvas}` (#eeeeee) background.

### Navigation
**`nav-bar`** — A thin 48px strip on `{colors.canvas}` (#eeeeee). The logo sits left in Barlow Medium 20px. Navigation links use `{typography.nav-link}` (Barlow Medium 14px) in `{colors.ink}`. The cart icon is the only right-side element, rendered as a simple outline icon in `{colors.ink}`. No search bar in the nav — search is a separate component on the product listing page.

### Forms
**`text-input`** — A simple rectangle with a 1px `{colors.hairline}` (#cfcfcf) border, no border-radius, 40px height, and 10px/12px padding. Text uses `{typography.body-sm}` (Barlow Regular 14px) in `{colors.body}` (#3a3a3a). On focus, the border changes to `{colors.primary}` (#108474). Error state uses a `{colors.error-red}` (#c13515) border.

### Footer
**`footer`** — A dark section on `{colors.ink}` (#222222) with white text. Links use `{typography.link}` in white. Padding is `{spacing.xl}` (32px) vertical and `{spacing.lg}` (24px) horizontal. The footer is divided into columns for customer service, about, and social links — all text, no icons.

### Badges
**`badge-new`** — A small teal rectangle with white uppercase Barlow Bold 10px text. Padding is 2px vertical, 6px horizontal. No border-radius. Used sparingly — only for truly new product launches.
**`badge-sale`** — Identical shape but with `{colors.error-red}` (#c13515) background. Used for clearance items.

### Search
**`search-bar`** — A standalone component on the product listing page. A white rectangle with a 1px `{colors.hairline}` border, 40px height, no border-radius. Text input uses `{typography.body-sm}`. No search icon — the bar is minimal to match the brand's aesthetic.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, nav collapses to hamburger, hero text reduces to 20px, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, hero maintains 24px display |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, hero at 28px display, max-width container |
| Wide | > 1440px | Max-width 1440px container centered, product grid remains three-column, extra whitespace on sides |

### Touch Targets
- All buttons and links: minimum 44px height for tap targets
- Cart icon: 44x44px tap area (icon is 20px with 12px padding)
- Product card images: full-width tap target
- Quantity selector: 36px height with 44px tap area via padding

### Collapsing Strategy
- Mobile: nav links collapse into hamburger menu, product grid goes single-column, footer columns stack
- Tablet: nav links remain visible but "Shop All" and "About" may collapse into a "More" dropdown
- Desktop: full nav visible, product grid at three columns, footer in four-column layout

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors are heavily weighted toward grays (#eeeeee through #646464) with only one distinctive accent: #108474 (teal). The gold #fbcd0a appears only in star ratings and one banner. The teal is assumed to be the primary brand color based on its use in CTAs and the brand name's association with "green" (peel of a fruit), but this is an inference — the extraction did not capture the full palette.
- Font-family declarations included "Barlow" and "Baskerville" but the exact usage split is unclear. Baskerville appears to be used only for product name italics on hero images; Barlow is the system font. The `-apple-system` and `Inter` declarations may be Shopify theme defaults.
- No hover state colors for text links or secondary buttons were extracted — only the primary button hover (#0d6b5e) is inferred from the active state pattern.
- Error and success styling for forms is assumed from common e-commerce patterns — no extraction confirmed these.
- The star-rating gold (#fbcd0a) may be a Shopify widget default rather than a brand color.
- No dark mode or high-contrast mode tokens were extracted.
- The checkout flow uses Shopify's default palette — the brand's custom colors may not extend there.
- No animation or transition timing values were extracted (hover transitions, page load animations, etc.).
