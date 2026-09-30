---
version: alpha
name: "Gossamer Gear"
source_url: "https://www.gossamergear.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand built for the trail, where #4990e2 — a cool, confident blue — acts as the single voltage that powers primary CTAs, cart buttons, and key interactive elements against a near-white canvas of #f2f2f2. The tagline "take less. do more." isn't just copy; it's a design philosophy visible in the generous whitespace, the restrained use of #ad1e36 as an accent for sale badges and urgency signals, and the absence of decorative clutter. Typography runs clean and utilitarian — likely a system sans-serif stack — with body text in #121212 for maximum readability under trailhead glare, while #242833 provides a slightly softer ink for secondary information. The palette's muted tones — #dedede for hairline borders, #ededed for surface cards — keep the visual field quiet, letting product photography of ultralight shelters and packs do the heavy lifting. Buttons carry a modest {rounded.sm} radius — friendly but not pill-shaped, suggesting durability over whimsy. The checkout flow introduces #334fb4 as a secondary blue, perhaps for trust signals or shipping highlights, while the overall system avoids gradient or shadow excess. This is a site that trusts its products to sell themselves, using color and space to say: the gear is light, the experience should feel lighter.

colors:
  primary: "#4990e2"
  primary-active: "#3578c7"
  primary-disabled: "#b3d4f5"
  ink: "#121212"
  body: "#242833"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#dedede"
  hairline-soft: "#e5e7eb"
  canvas: "#f2f2f2"
  surface-soft: "#f9fafb"
  surface-card: "#ededed"
  on-primary: "#ffffff"
  accent-sale: "#ad1e36"
  accent-sale-soft: "#fce8ec"
  secondary-blue: "#334fb4"
  star-rating: "#f59e0b"
  error: "#dc2626"
  success: "#16a34a"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 6px
  md: 10px
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
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
  button-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
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
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
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
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.price}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} 0"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  badge-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.secondary-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-active:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
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
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
  accordion-content:
    padding: "0 0 {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's distinctive blue (#4990e2) with white text. Used for "Add to Cart", "Checkout", and "Shop Now" actions. On hover, shifts to `{colors.primary-active}` (#3578c7) for a subtle depth cue. Disabled state uses `{colors.primary-disabled}` (#b3d4f5) to indicate non-interactivity while maintaining brand color presence.

**`button-secondary`** — An outlined variant on the light canvas background, with a 2px hairline border and dark ink text. Active state fills the border to solid ink, providing a clear visual hierarchy below primary actions. Used for "Learn More", "View Details", and secondary form submissions.

**`button-tertiary-text`** — A text-only link styled as a button, using the primary blue for color. No background or border — just clean, clickable text. Used for "Cancel", "Clear Filters", and inline navigation prompts where visual weight should be minimal.

**`button-sale`** — An urgent accent button using `{colors.accent-sale}` (#ad1e36) for clearance items, limited-time offers, and final markdowns. Shares the same dimensions and typography as `button-primary` but swaps the blue for a deep crimson that signals savings without feeling aggressive.

### Cards
**`product-card`** — The core product display unit, a clean white card on `{colors.surface-card}` (#ededed) background. The product image occupies the top portion with a `{rounded.md}` top radius, while title and price sit below with generous padding. A sale badge overlays the top-left corner of the image when applicable, using `{colors.accent-sale}` for immediate visibility.

### Navigation
**`nav-bar`** — A fixed 72px header on the light canvas background, separated from content by a single hairline border. Navigation links are uppercase, 14px, weight 600, with the active page indicated by a 2px primary-blue underline. The search bar sits as a pill-shaped input to the right, maintaining the brand's utilitarian but friendly character.

### Forms
**`text-input`** — Standard form inputs with a 1px hairline border and 6px corner radius. On focus, the border thickens to 2px and shifts to primary blue for clear keyboard focus indication. Error states use a 2px red border with `{colors.error}` (#dc2626) for accessibility.

### Footer
**`footer`** — A dark anchor for the page, using `{colors.ink}` (#121212) as background with light text. Links start in `{colors.muted-soft}` and brighten to white on hover, creating a clear interactive hierarchy against the dark backdrop. Padding is generous at 48px top and bottom, giving the footer breathing room from content above.

### Badges
**`badge-sale`** — A small, uppercase label in deep crimson (#ad1e36) with white text, used to flag discounted items on product cards and collection pages. The 2px horizontal padding keeps it compact while remaining legible.

**`badge-new`** — A secondary badge in `{colors.secondary-blue}` (#334fb4) for new arrivals or recently added products. Shares the same dimensions and typography as the sale badge but uses a cooler blue to differentiate the message.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to 24px; buttons become full-width; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero maintains 28px display; side-by-side footer columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at 36px display; standard button widths |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero text scales to 40px; additional whitespace on product cards |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets extend to full card area for easy selection
- Navigation hamburger icon is 48x48px on mobile
- Quantity selector buttons are 44x44px minimum
- Search bar maintains 48px height across all breakpoints

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product filters collapse to a slide-out drawer on mobile
- Footer link columns stack vertically below 744px
- Hero section reduces padding from 64px to 32px on mobile
- Product card grid reduces from 4 columns to 1 column on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font family could not be reliably extracted from the live site; Inter is a reasonable assumption for a modern outdoor brand but should be verified against the actual CSS
- Hover and focus states for most components are inferred from common patterns rather than extracted from live CSS
- Error state styling for forms (error messages, validation icons) is not documented from live data
- Dark mode preferences and associated color tokens are not available
- Sub-brand or collection-specific palette variations (e.g., "Mariposa" vs "Gorilla" pack lines) are not captured
- Animation durations, easing curves, and transition properties are not extracted
- Modal, tooltip, and dropdown component styling is not documented
- Checkout flow specific styling (Shopify checkout overrides) is not captured
- Print stylesheet behavior is unknown
- Focus ring styles for keyboard navigation are not documented
