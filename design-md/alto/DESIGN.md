---
version: alpha
name: "Alto"
source_url: "https://www.viaalto.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, saturated teal (#108474) anchors Alto's leather accessories storefront, a color choice that reads as deliberate and grounded — not the expected black or brown of a leather-goods brand, but a verdant, almost tropical green that makes the product photography of phone cases and card holders feel like objects in a terrarium. The palette leans heavily on a warm, earthy secondary: #bb731b, a burnished ochre that appears in badges, sale tags, and accent elements, while #fbcd0a (a bright marigold) provides the occasional high-voltage jolt. The canvas is a cool, clinical #f9fafb, and the text hierarchy runs from #292929 for headlines through #444444 for body copy to #888888 for muted labels, creating a clean, editorial reading experience. Type is set in Nunito Sans and Baskerville — the former a rounded, friendly sans-serif for UI and product titles, the latter a classic serif for long-form descriptions and brand storytelling, a pairing that bridges modern utility with a sense of craftsmanship. Corners are soft but not pillowy: cards and buttons use {rounded.md} (12px) and {rounded.lg} (20px), while the primary CTA button is a full-height teal rectangle with white text, no border, and a hover state that deepens to a darker green. The site's Shopify roots are visible in the checkout-widget colors (#3b5998, #1da1f2, #dd4b39) that pepper the extracted palette, but the brand's own identity is unmistakable in the teal-and-ochre duotone that governs every product card, navigation bar, and footer section.

colors:
  primary: "#108474"
  primary-active: "#0d6b5e"
  primary-disabled: "#a3d4c9"
  ink: "#292929"
  body: "#444444"
  muted: "#888888"
  muted-soft: "#9e9e9e"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-ochre: "#bb731b"
  accent-marigold: "#fbcd0a"
  error: "#e74c3c"
  badge-new: "#a89cc8"
  badge-sale: "#bb731b"
  star-rating: "#fbcd0a"
  social-facebook: "#3b5998"
  social-twitter: "#1da1f2"
  social-google: "#dd4b39"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.44
    letterSpacing: 0
  body-lg:
    fontFamily: "'Baskerville', 'Georgia', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
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
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.ink}"
  button-ochre:
    backgroundColor: "{colors.accent-ochre}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 3px rgba(16, 132, 116, 0.15)"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.error}"
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
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    boxShadow: "0 1px 3px rgba(0, 0, 0, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    boxShadow: "0 10px 25px rgba(0, 0, 0, 0.08), 0 4px 10px rgba(0, 0, 0, 0.04)"
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    textColor: "{colors.error}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.md}"
    padding: "16px 32px"
    height: 56px
  section-heading:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0 {spacing.md} 0"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  star-rating:
    textColor: "{colors.star-rating}"
    fontSize: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    height: 40px
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "14px 24px"
    height: 48px
    width: "100%"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Shop Now," and checkout flows. Rendered as a solid teal rectangle with white text, 12px rounded corners, and 48px height. On hover, the background shifts to `{colors.primary-active}` (#0d6b5e) with no border change. In disabled state, the background fades to `{colors.primary-disabled}` (#a3d4c9) and cursor becomes not-allowed.

**`button-secondary`** — Used for "View Details," "Learn More," and secondary actions. A white background with a 1px `{colors.hairline}` border and `{colors.ink}` text. On hover, the border thickens to `{colors.ink}` and the background shifts to `{colors.surface-soft}`. Height matches the primary button at 48px for consistent alignment in forms.

**`button-ochre`** — An accent button reserved for promotional banners, limited-time offers, and "Sale" CTAs. Uses `{colors.accent-ochre}` (#bb731b) as background with white text. Same dimensions and rounded corners as `button-primary` to maintain rhythm in button groups.

### Cards
**`product-card`** — The primary product display unit, used in grid layouts on collection pages and search results. A white card with `{rounded.lg}` (20px) corners and a subtle box shadow. The card contains an image area with top-rounded corners, a title in `{typography.title-md}`, a price in `{typography.body-md}`, and optional badges. On hover, the shadow deepens and a slight translateY of -2px is applied. The card is fully clickable, linking to the product detail page.

**`product-card-image`** — The image container within a product card, with top corners rounded to match the card's `{rounded.lg}`. Aspect ratio is 1:1 for most product shots, with object-fit: cover applied. A secondary image appears on hover for products with multiple angles.

### Navigation
**`top-nav`** — A fixed-position header bar at 72px height with a white background and a subtle bottom border. Contains the brand logo on the left, navigation links in the center, and utility icons (search, account, cart) on the right. Active nav links use `{colors.primary}` text color, while inactive links are `{colors.muted}`. On mobile, the navigation collapses into a hamburger menu.

**`nav-link-active`** — The active state for top navigation items, distinguished by `{colors.primary}` text color and an optional underline indicator. No background change — the brand relies on color alone for active state differentiation.

### Forms
**`text-input`** — Standard text input used in search, newsletter signup, and checkout forms. A white background with a 1px `{colors.hairline}` border and 12px rounded corners. On focus, the border transitions to `{colors.primary}` with a 3px teal-tinted ring shadow. Error state uses `{colors.error}` (#e74c3c) border color. Height is 48px to match button heights for inline form layouts.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a `{colors.surface-soft}` background and subtle border. Used in the header and on search result pages. On focus, the background shifts to white and the border becomes `{colors.primary}`. Includes a search icon on the left and a clear button on the right when text is present.

### Badges
**`badge-new`** — A small, uppercase badge in `{colors.badge-new}` (#a89cc8, a muted lavender) used to flag newly added products. Text is white, 11px bold, with 4px rounded corners and minimal padding. Positioned at the top-left corner of product card images.

**`badge-sale`** — An ochre badge (`{colors.badge-sale}`) used for discounted items. Same typography and dimensions as `badge-new` but with a warm, attention-grabbing background. Appears alongside the original price, which is struck through.

**`badge-marigold`** — A bright yellow badge (`{colors.accent-marigold}`) used for "Best Seller" or "Limited Edition" tags. Uses `{colors.ink}` text for contrast against the yellow background.

### Footer
**`footer`** — A dark footer section with `{colors.ink}` background and white text. Contains columns for product categories, customer service, company info, and social links. Links are `{colors.muted-soft}` by default and transition to white on hover. The footer includes a newsletter signup form and copyright notice at the bottom.

### Hero
**`hero-banner`** — A full-width promotional banner with `{colors.primary}` background and white text. Used on the homepage and seasonal landing pages. Contains a headline in `{typography.display-xl}`, supporting text, and a prominent CTA button in `{colors.accent-marigold}` with `{colors.ink}` text. The banner may include background imagery or patterns overlaid with the teal background.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked hero layout, reduced font sizes |
| Tablet | 744–1128px | Two-column product grid, visible nav links, side-by-side hero |
| Desktop | 1128–1440px | Three-column product grid, full nav, multi-column footer |
| Wide | > 1440px | Max-width container at 1440px, centered content, four-column product grid |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product cards have a minimum 48px tap area for the entire card surface
- Navigation hamburger icon is 44x44px with adequate padding
- Quantity selector buttons are 40x40px with clear +/- labels
- Add-to-cart button spans full width on mobile for easy one-handed tapping

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with a slide-out drawer overlay
- Product grid reduces from 4 columns on wide screens to 1 column on mobile
- Footer columns stack vertically on mobile, with accordion-style expandable sections
- Hero banner text and CTA stack vertically on mobile, with reduced font sizes
- Search bar collapses to icon-only on mobile, expanding to full-width on tap
- Product filters collapse to a "Filter" button on mobile, opening a modal overlay

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and cards are inferred from common patterns; exact transition durations and easing functions were not extracted
- Error and validation styling for forms (error messages, success states) is assumed based on standard patterns; exact colors and positioning are unknown
- Dark mode is not implemented on the live site; no dark palette tokens are available
- The extracted font list includes JudgemeIcons and JudgemeStar, which are review-widget icon fonts — these are not part of the brand's primary typography system
- Social icon colors (#3b5998, #1da1f2, #dd4b39) are standard brand colors for Facebook, Twitter, and Google, not Alto-specific design tokens
- The extracted palette includes many grayscale values (#eeeeee, #e9e9e9, #f2f2f2, #dadada, #fafafa, #aaaaaa, #7b7b7b, #737373, #545454, #555555, #53514b) — these are likely used for borders, backgrounds, and text hierarchy but exact mappings are inferred
- The color #c1e6e6 appears in the extraction but its usage is unclear — may be a secondary background or accent
- The color #ffff00 (pure yellow) appears in the extraction but is likely a stock-image dominant tone or placeholder, not a brand color
- Sub-brand or seasonal palette variations are not documented
- Loading states, skeleton screens, and animation specifications are not available
- Print stylesheet behavior is unknown
