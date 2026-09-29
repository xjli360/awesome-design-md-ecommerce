---
version: alpha
name: "Whitestone Dome"
source_url: "https://www.whitestonedome.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A precision-hardware brand that sells its glass screen protectors with the visual language of a medical device manufacturer — #231f20 near-black on #ffffff white, with #004085 as the single accent voltage that signals "this is the premium option." The brand's Shopify storefront reads as a series of product-as-artifact presentations: each screen protector floats on a white canvas, its edges defined by #dae0e5 hairline strokes, with callout badges in #155724 green for "Tempered Glass" and #856404 amber for "UV Cure Required." The typography stack is a deliberate collision — Big Caslon and Bodoni MT for display headings (a rare serif choice in the phone-accessories category) paired with system sans for body copy, suggesting a brand that wants to feel heirloom-quality rather than gadget-adjacent. Every product card uses `{rounded.sm}` corners, every CTA button is a `{rounded.sm}` rectangle in #004085 with white text, and the checkout flow inherits Shopify's default pill-shaped inputs (`{rounded.full}`). The meta theme-color #3d4246 — a warm dark gray — sets the browser chrome tone, reinforcing the brand's preference for charcoal over pure black. A persistent "Lifetime Warranty" badge in #155724 green and a "Free Shipping" badge in #0c5460 teal run across the top of the page, using `{typography.caption}` weight 600 to create a utility belt of trust signals. The overall feel is that of a premium electronics unboxing: restrained, high-contrast, with every color carrying a specific functional meaning rather than decorative intent.

colors:
  primary: "#004085"
  primary-active: "#003166"
  primary-disabled: "#b3d7ff"
  ink: "#231f20"
  body: "#383d41"
  muted: "#545b62"
  muted-soft: "#818182"
  hairline: "#dae0e5"
  hairline-soft: "#ececf6"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#155724"
  success-bg: "#b1dfbb"
  warning: "#856404"
  warning-bg: "#ffe8a1"
  error: "#721c24"
  error-bg: "#f1b0b7"
  info: "#0c5460"
  info-bg: "#abdde5"
  badge-green: "#155724"
  badge-teal: "#0c5460"
  badge-amber: "#856404"
  badge-red: "#721c24"
  star-rating: "#d39e00"
  meta-theme: "#3d4246"
  scrim: "#1b1e21"

typography:
  display-xl:
    fontFamily: "'Big Caslon', 'Bodoni MT', 'Cardo', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Big Caslon', 'Bodoni MT', 'Cardo', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Big Caslon', 'Bodoni MT', 'Cardo', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Big Caslon', 'Bodoni MT', 'Cardo', Georgia, serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
    color: "{colors.error}"

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
    rounded: "{rounded.sm}"
    padding: 12px 28px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: 8px 16px
  button-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
    width: 100%
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: "none"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(35,31,32,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 12px"
  trust-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
    height: 36px
  trust-badge:
    backgroundColor: "{colors.badge-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 10px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.hairline}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
  accordion-content:
    padding: "0 0 {spacing.base} 0"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 16px
  review-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  review-author:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  review-date:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 44px
    width: 44px
  breadcrumb:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
    padding: "0 {spacing.xs}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "4px 12px"
  pagination-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    padding: "4px 12px"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.6
  modal-dialog:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: "0 8px 32px rgba(35,31,32,0.12)"
  modal-close:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  section-header:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0 {spacing.base} 0"
  section-subheader:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    padding: "0 0 {spacing.lg} 0"
  feature-list:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0"
  feature-icon:
    color: "{colors.primary}"
    fontSize: 20px
    padding: "0 {spacing.sm} 0 0"
  warranty-badge:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 10px"
  shipping-badge:
    backgroundColor: "{colors.badge-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 10px"
  compatibility-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    border: "1px solid {colors.hairline}"
  compatibility-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in #004085 with white text and `{rounded.sm}` corners. Used for "Add to Cart", "Buy Now", and primary checkout flows. On hover, shifts to `{colors.primary-active}` (#003166). Disabled state uses `{colors.primary-disabled}` (#b3d7ff) with white text. Height is 44px with 12px/28px padding for a comfortable tap target.

**`button-secondary`** — An outlined variant with a white fill and #004085 border, used for secondary actions like "Learn More" or "View Details". Maintains the same 44px height as primary but uses 11px/27px padding to account for the 2px border. Active state darkens the border to `{colors.primary-active}`.

**`button-tertiary`** — A text-only button in #004085, used for inline actions like "Clear filters" or "Cancel". No background, minimal padding, uses `{typography.button-sm}` for a lighter footprint.

**`button-cart`** — The full-width "Add to Cart" button on product detail pages. Matches `button-primary` styling but spans 100% width and uses 14px/32px padding for a more substantial feel at 48px height.

### Navigation
**`nav-bar`** — A 64px white header with a 1px bottom border in `{colors.hairline}` (#dae0e5). Contains the brand logo (serif display), navigation links, and a search icon. The bar is fixed at the top on desktop, collapsing to a hamburger menu on mobile.

**`nav-link-active`** — Active navigation links use the brand's ink color (#231f20) with a 2px bottom border in `{colors.primary}` (#004085). Inactive links use `{colors.muted}` (#545b62). All nav links use `{typography.nav-link}` at 14px weight 600.

**`breadcrumb`** — Secondary navigation using `{typography.caption-sm}` in muted gray, with the current page in ink. Separators are `{colors.hairline}` with 4px horizontal padding.

### Cards
**`product-card`** — A white card with `{rounded.sm}` corners and a 1px border in `{colors.hairline-soft}` (#ececf6). On hover, the border strengthens to `{colors.hairline}` and a subtle shadow appears (0 2px 8px rgba(35,31,32,0.08)). The image area uses `{rounded.sm}` on top corners only. Title uses `{typography.title-md}` (18px weight 600), price uses `{typography.price}` (20px weight 700). Sale prices render in `{colors.error}` (#721c24).

**`review-card`** — A white card with `{rounded.sm}` corners, 1px `{colors.hairline-soft}` border, and 16px padding. Author name uses `{typography.caption}` (13px weight 600), date uses `{typography.caption-sm}` (12px weight 500) in muted gray. Star ratings render in `{colors.star-rating}` (#d39e00) at 16px.

### Badges & Tags
**`product-card-badge`** — Small uppercase badges in #155724 green with white text, `{rounded.xs}` corners, and 2px/8px padding. Used for "Tempered Glass", "UV Cure", "Premium" labels on product cards.

**`trust-badge`** — Teal badges (#0c5460) used in the trust bar for "Free Shipping" and "Lifetime Warranty" indicators. Same styling as product badges but with teal background.

**`warranty-badge`** / **`shipping-badge`** — Standalone badges in green and teal respectively, used in the persistent top trust bar and on product detail pages. Both use `{typography.badge}` (11px weight 700 uppercase).

**`compatibility-tag`** — Pill-shaped tags (`{rounded.full}`) in `{colors.surface-soft}` with `{colors.muted}` text and a 1px `{colors.hairline}` border. Used for phone model selectors (e.g., "iPhone 15 Pro", "Galaxy S24 Ultra"). Active state fills with `{colors.primary}` and white text.

### Forms & Inputs
**`text-input`** — Standard text input at 44px height with `{rounded.sm}` corners, 10px/14px padding, and a 1px `{colors.hairline}` border. On focus, the border becomes 2px solid `{colors.primary}` with no outline.

**`select-input`** — Matches text-input styling for dropdown selectors, used for quantity selection and variant pickers.

**`search-input`** — A pill-shaped search field (`{rounded.full}`) at 40px height with `{colors.surface-soft}` background and 8px/16px padding. Uses `{typography.body-sm}` (14px) for placeholder text.

**`quantity-selector`** — A horizontal stepper with a 44px height container, `{rounded.sm}` corners, and 1px `{colors.hairline}` border. Increment/decrement buttons are 44px squares with `{colors.surface-soft}` background.

### Modals & Overlays
**`modal-overlay`** — A full-screen scrim using `{colors.scrim}` (#1b1e21) at 60% opacity.

**`modal-dialog`** — White dialog with `{rounded.md}` (12px) corners, 24px padding, and a 0 8px 32px shadow using rgba(35,31,32,0.12). Close button is a 32px circle with `{colors.surface-soft}` background.

### Content Blocks
**`hero-banner`** — Full-width section with `{colors.ink}` background and white text, using `{typography.display-xl}` (36px Big Caslon). Contains an optional accent badge in `{colors.primary}` for promotional messaging. Section-level padding of 64px top/bottom and 24px sides.

**`trust-bar`** — A 36px utility bar at the top of the page with `{colors.surface-soft}` background, containing trust badges and shipping information. Uses `{typography.caption-sm}` (12px weight 500).

**`accordion`** — Collapsible sections with white background, 1px bottom border in `{colors.hairline}`, and `{typography.title-md}` headers. Content area uses `{typography.body-md}` with 16px bottom padding.

**`feature-list`** — Bullet-style feature lists with `{colors.primary}` icons at 20px and `{typography.body-sm}` text. Each item has 8px vertical padding.

### Footer
**`footer`** — Full-width dark footer using `{colors.ink}` background with white text. Links use `{colors.hairline}` (#dae0e5) and shift to white on hover. Section padding of 48px top/bottom and 24px sides. Contains columns for product categories, support links, and legal information.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero banner reduces to 32px font; trust bar wraps to two rows; search input moves to off-canvas drawer; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links with "More" dropdown; hero banner uses 28px font; trust bar remains single row but compresses badge text; sidebar filters become horizontal strip |
| Desktop | 1128–1440px | Full nav-bar with all links visible; three-column product grid; hero banner at full 36px display; sidebar filters visible on collection pages; product detail page shows two-column layout (gallery + info) |
| Wide | > 1440px | Max-width container at 1440px; four-column product grid; hero banner centered with max-width 1200px; additional whitespace around product cards; sticky nav-bar with full-width background |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons (search, cart, close) are 40–44px squares
- Quantity selector buttons are 44px squares
- Product card tap targets span full card width
- Accordion headers are minimum 48px tall for easy tapping
- Pagination items are 44px minimum with 12px padding

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with a slide-out drawer for full navigation
- Product filters collapse to a horizontal scroll strip on tablet, and to a "Filter" button with modal on mobile
- Trust bar badges truncate text on tablet (e.g., "Free Shipping" becomes "Free Ship.")
- Footer columns stack vertically on mobile, with accordion-style expandable sections
- Search transforms from inline input to full-screen overlay on mobile
- Product image gallery collapses from thumbnail strip to swipeable dots on mobile
- Multi-column feature lists collapse to single column below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors are heavily weighted toward Bootstrap alert/utility classes (success green, warning amber, error red, info teal) and Shopify checkout defaults — the brand's true accent palette may be narrower than the 30+ colors listed. The most distinctive brand color appears to be #004085 (a deep navy blue), but this should be verified against the brand's actual style guide.
- Font-family declarations include both serif (Big Caslon, Bodoni MT, Cardo) and system sans options, but the exact pairing strategy (which headings use serif vs. sans) could not be determined from extracted data alone. The serif usage is assumed for display headings based on the brand's premium positioning.
- Hover states for buttons and cards are inferred from common ecommerce patterns — actual hover transitions, shadows, and animations are not extractable from static CSS.
- Error states for form inputs (validation styling, error messages) are not present in extracted data — standard Shopify error patterns (#721c24 red with #f1b0b7 background) are assumed.
- Dark mode is not supported — the brand uses white canvas (#ffffff) exclusively.
- Sub-brand or collection-specific color variations (e.g., "Dome Glass" vs. "EZ Apply" product lines) could not be distinguished.
- Animation durations, easing curves, and micro-interaction timing are not extractable — standard 200–300ms ease-in-out is assumed.
- The brand's Shopify theme may override some default component styles — extracted data reflects the live site but may include theme-specific overrides that differ from the brand's intended design system.
- Responsive breakpoints are estimated based on common Shopify practice — actual breakpoints should be verified against the brand's theme settings.
