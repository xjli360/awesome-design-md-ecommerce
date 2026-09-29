---
version: alpha
name: "Umbrella Entertainment"
source_url: "https://shop.umbrellaent.com.au"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, cinephile-friendly storefront where the brand voltage comes from a distinctive teal (#108474) — not a generic retail blue but an earthy, almost medicinal green that signals curation over commodity. That teal anchors the primary CTA, the header background, and the checkout flow, while a sharp marigold accent (#fff302) and a warmer butter (#fbcd0a) provide the only two bright notes in an otherwise restrained palette of warm grays (#eeeeee, #dedede, #e9e9e9) and near-blacks (#1e1e1e, #121212). The typography runs Nunito Sans across headings and body, a rounded humanist sans-serif that keeps the site approachable despite the serious film-collector inventory. Product cards use soft corners (`{rounded.sm}`) and generous whitespace (`{spacing.lg}` between rows), while the search bar and primary buttons take a slightly tighter radius (`{rounded.xs}`) that reads as intentional rather than sharp. The footer collapses into a dense, link-heavy grid of columns — a deliberate choice for a catalog business where discoverability matters more than visual air. A faint lavender (#a89cc8) appears in badge and sale-flag contexts, an unexpected tertiary that nods to the brand's willingness to break its own rules for emphasis. The overall feel is that of a well-stocked independent video store translated into a single-page app: warm grays, teal shelving, yellow price tags, and the quiet confidence of a collection that doesn't need to shout.

colors:
  primary: "#108474"
  primary-active: "#0d6b5e"
  primary-disabled: "#a3d4c9"
  ink: "#1e1e1e"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#888888"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#fff302"
  accent-butter: "#fbcd0a"
  accent-lavender: "#a89cc8"
  badge-sale: "#fff302"
  badge-new: "#108474"
  star-rating: "#fbcd0a"
  social-facebook: "#3b5998"
  social-twitter: "#1da1f2"
  social-pinterest: "#e60023"
  social-linkedin: "#0073b1"
  error-red: "#dd4b39"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.25px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  footer-link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
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
  section: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.muted}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-accent-yellow-active:
    backgroundColor: "{colors.accent-butter}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  text-input-error:
    border: "2px solid {colors.error-red}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-link-active:
    textColor: "{colors.accent-yellow}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  product-card-hover:
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "2/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-lavender:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.footer-link}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.footer-link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.md}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xl} {spacing.lg}"
    rounded: "{rounded.none}"
  hero-banner-accent:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    height: 44px
    width: 44px
  add-to-cart-button:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 48px
  add-to-cart-button-active:
    backgroundColor: "{colors.accent-butter}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  checkout-button-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 36px
    width: 36px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    height: 24px
    width: 24px
  social-icon-hover:
    textColor: "{colors.on-primary}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.body}"
  breadcrumb-link-hover:
    textColor: "{colors.primary}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    padding: "0 {spacing.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand teal (#108474) with white text and a tight 4px corner radius (`{rounded.xs}`). On hover, it shifts to `{colors.primary-active}` (#0d6b5e) for a subtle depth cue. The disabled state uses `{colors.primary-disabled}` (#a3d4c9), a desaturated teal that maintains legibility without inviting interaction. Height is 44px with 12px/24px padding — compact enough for dense product grids but generous enough for checkout flows.

**`button-secondary`** — An outlined variant with a white background, ink text, and a 1px hairline border. Used for "View Details," "Cancel," and secondary product actions. Active state swaps the border to `{colors.muted}` and the background to `{colors.surface-soft}` (#f2f2f2). Same 44px height and 4px radius as the primary button for consistent row alignment.

**`button-accent-yellow`** — The high-energy variant reserved for "Add to Cart," sale promotions, and limited-time offers. Uses `{colors.accent-yellow}` (#fff302) background with ink text. Active state shifts to `{colors.accent-butter}` (#fbcd0a). This button is the brand's loudest visual element — it appears only where conversion intent is highest.

### Cards
**`product-card`** — A white card with 8px corner radius (`{rounded.sm}`) and 8px padding. The product image occupies the top with a 2:3 aspect ratio and 4px radius. Below, the title uses `{typography.title-sm}` (16px, weight 600) and the price uses `{typography.body-md}` (16px, weight 400) in `{colors.body}` (#555555). On hover, a subtle box-shadow (0 2px 8px rgba(0,0,0,0.08)) lifts the card without animation — a quiet, print-like interaction.

**`badge-sale`** — A small uppercase label with `{colors.accent-yellow}` background and ink text. Used for discount flags, clearance items, and limited editions. The 4px radius and 2px/8px padding keep it compact enough to overlay on product images without obscuring the artwork.

**`badge-new`** — Teal-background badge for new arrivals and pre-orders. Uses `{colors.primary}` with white text. Same dimensions as `badge-sale` but signals freshness rather than discount.

**`badge-lavender`** — The tertiary badge color (`{colors.accent-lavender}` #a89cc8), used sparingly for exclusive editions, signed copies, or special collections. Its unexpected presence breaks the teal-yellow binary and signals something outside the normal catalog.

### Navigation
**`nav-bar`** — A full-width teal strip (`{colors.primary}`) at 60px height. Navigation links are white with 16px horizontal padding. The active link uses `{colors.accent-yellow}` to indicate the current section — a bright, unmistakable state that leverages the brand's only saturated accent. The bar collapses to a hamburger menu below 744px.

**`search-bar`** — A pill-shaped input (`{rounded.full}`) with white background, 1px hairline border, and 44px height. On focus, the border thickens to 2px and turns `{colors.primary}`. The pill shape is the only fully rounded element in the system — it stands out against the otherwise angular interface, signaling that search is a primary entry point.

### Forms
**`text-input`** — Standard 44px input with 4px radius, white background, and hairline border. Focus state uses a 2px teal border. Error state uses `{colors.error-red}` (#dd4b39) border — the only place this red appears in the system, reserved exclusively for validation feedback.

**`quantity-selector`** — A bordered container with two square buttons (44x44px) flanking a central text display. The buttons use `{colors.surface-soft}` background and `{typography.button-sm}`. This component appears on product detail pages and cart line items.

### Footer
**`footer`** — A dark section (`{colors.ink}` #1e1e1e) with muted-soft (#888888) link text. Column headings use `{colors.on-primary}` (#ffffff) at `{typography.title-sm}`. Links hover to white. The footer uses 48px vertical padding and 24px horizontal padding, with columns collapsing to a single stack on mobile. Social icons sit at the bottom in muted-soft, shifting to white on hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav-bar collapses to hamburger; product cards go single-column; footer columns stack vertically; search bar reduces to icon-only; hero banner text shrinks to `{typography.display-md}`; filter chips wrap to two rows |
| Tablet | 744–1128px | Nav-bar shows full links; product cards in 2-3 column grid; footer shows 2 columns; search bar remains full-width; hero banner uses `{typography.display-lg}` |
| Desktop | 1128–1440px | Product cards in 4-column grid; footer shows 4 columns; search bar centered in header; hero banner uses `{typography.display-xl}`; filter chips in single horizontal row |
| Wide | > 1440px | Max-width container at 1440px; product cards in 5-column grid; additional whitespace on left/right; hero banner may include background image |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Search bar and text inputs are 44px tall — meets WCAG 2.1 touch target guidelines
- Quantity selector buttons are 44x44px squares
- Filter chips are 36px tall with 16px horizontal padding — slightly below ideal but acceptable for desktop; on mobile they expand to 44px
- Social icons are 24x24px with 8px padding — below the 44px target but acceptable as secondary elements

### Collapsing Strategy
- **Nav-bar**: Full horizontal links on desktop/tablet → hamburger menu on mobile (< 744px). The hamburger icon uses `{colors.on-primary}` on the teal background.
- **Footer**: 4-column grid on desktop → 2-column on tablet → single column on mobile. Column order remains consistent.
- **Product grid**: 5 columns on wide → 4 on desktop → 3 on tablet → 2 on small tablet → 1 on mobile.
- **Filter chips**: Single horizontal scrollable row on desktop → wrap to two rows on mobile with "Show More" toggle for overflow.
- **Hero banner**: Full-width with large text on desktop → reduced text size and optional image removal on mobile to save vertical space.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only `button-primary`, `button-secondary`, `button-accent-yellow`, `product-card`, `footer-link`, `breadcrumb-link`, and `social-icon` have documented hover states. Other interactive elements (filter chips, pagination, nav links) may have hover behaviors that couldn't be reliably extracted from the live site.
- **Error styling**: Only `text-input-error` is documented. Form-level error messages, validation summaries, and toast notifications were not observed.
- **Dark mode**: No dark mode implementation was detected. The brand uses a light canvas (#f9fafb) with dark ink (#1e1e1e) — a dark mode would need to invert this relationship.
- **Sub-brand palettes**: The extracted hex list includes social media brand colors (#3b5998, #1da1f2, #dd4b39, #e60023, #0073b1) which are likely from share buttons, not the brand's own palette. These are documented as `social-*` tokens but may not be actively used in the design system.
- **Animation/transition**: No transition durations, easing curves, or animation specifications were extracted. The site appears to use minimal motion (only hover box-shadow on product cards).
- **Typography scale**: The extracted font-family declarations include "JudgemeIcons" and "JudgemeStar" — these are review-widget icon fonts, not part of the brand's typographic system. The primary typeface is Nunito Sans, with Arial and Helvetica as fallbacks. Baskerville appears in the extracted list but was not observed in use — it may be a legacy or widget font.
- **Spacing scale**: The spacing tokens are inferred from common e-commerce patterns. The exact values for `section` (64px) and `xxl` (48px) are estimates based on footer and hero padding.
- **Checkout flow**: Shopify's default checkout may override brand colors. The `checkout-button` component uses the brand teal, but Shopify's checkout template may inject its own styling for payment forms, address fields, and order summaries.
- **Star rating color**: The `star-rating` token uses `{colors.accent-butter}` (#fbcd0a) based on the extracted yellow tones, but the exact implementation (filled vs. empty stars, half-star rendering) was not observed.
