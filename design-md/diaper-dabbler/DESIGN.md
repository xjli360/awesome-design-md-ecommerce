---
version: alpha
name: "Diaper Dabbler"
source_url: "https://diaperdabbler.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A pastel-soft baby-care marketplace that wraps diaper sampling in a playful, trustworthy shell anchored on a crisp white canvas (#ffffff) and a distinctive pale teal (#108474) that reads as clean without being clinical. The brand's visual signature is a surprising pink accent (#db7093) — pale carnation, not bubblegum — that appears on sale badges, promotional banners, and secondary CTAs, tempering the teal's authority with warmth. A secondary teal wash (#c1e6e6) and a faint sage surface (#edf5f5) create layered backgrounds that keep product photography from floating in white space. Buttons use a generous 8px radius (`{rounded.sm}`) rather than pills, and the primary CTA in #108474 sits on a white button with #ffffff text — a quiet inversion that signals "we're different from the big-box baby stores." The type system runs Nunito Sans, a rounded humanist sans-serif that reinforces the soft, approachable tone; body copy at 16px in #555555 keeps readability high for tired parents shopping on mobile. Star ratings and review badges use a warm yellow (#fbcd0a) as the only saturated accent, while social icons and checkout widgets introduce blues (#3b5998, #1da1f2) that are clearly platform-driven, not brand. The overall effect is a clean, uncluttered storefront that feels like a well-organized nursery — organized, gentle, and just a little bit playful.

colors:
  primary: "#108474"
  primary-active: "#0d6b5e"
  primary-disabled: "#a3d5d0"
  ink: "#222222"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#888888"
  hairline: "#dadada"
  hairline-soft: "#e9e9e9"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  surface-wash: "#edf5f5"
  on-primary: "#ffffff"
  accent-pink: "#db7093"
  accent-pink-active: "#c95a7d"
  star-yellow: "#fbcd0a"
  teal-light: "#c1e6e6"
  badge-sale: "#ff5268"
  badge-sale-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
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
    padding: 12px 24px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-wash}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-accent-pink:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-accent-pink-active:
    backgroundColor: "{colors.accent-pink-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.badge-sale}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-mobile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 60px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: 0 0 16px 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.xs} {spacing.base}"
  product-card-variant-select:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    margin: "{spacing.sm} {spacing.base}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.badge-sale-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-star:
    backgroundColor: "{colors.star-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  footer:
    backgroundColor: "{colors.surface-wash}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.primary}"
  section-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xl} 0 {spacing.base}"
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
    border: "1px solid {colors.primary}"
  review-stars:
    color: "{colors.star-yellow}"
    fontSize: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Subscribe & Save", and checkout initiation. Rendered in the brand teal (#108474) with white text and an 8px radius (`{rounded.sm}`). On hover, shifts to a deeper teal (`{colors.primary-active}`) with no border change. Disabled state uses a washed-out teal (`{colors.primary-disabled}`) with white text, signaling the action is unavailable. Height is a comfortable 48px with 12px/24px padding.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details". Uses a white background with teal text and a 2px teal border. On active state, the background shifts to the light teal wash (`{colors.surface-wash}`) and the border deepens. Same 48px height and 8px radius as the primary button for visual consistency.

**`button-accent-pink`** — A promotional variant reserved for limited-time offers, clearance items, and special events. Uses the pale carnation pink (#db7093) as background with white text. This button creates visual hierarchy when placed alongside primary teal buttons — the pink signals "special" or "limited" without being alarmist. Active state darkens to `{colors.accent-pink-active}`.

**`button-sm`** — A compact version for inline actions like "Quick Add" on product cards or "Apply" in filter bars. Uses the primary teal at 36px height with 8px/16px padding and smaller button typography (`{typography.button-sm}`).

### Cards
**`product-card`** — The core product display unit, a white card with a 12px radius (`{rounded.md}`) containing a product image (top corners rounded, bottom corners square), title in 16px/600 weight, price in 14px body, and a variant selector dropdown. The card has no border but relies on the white surface against the soft background (`{colors.surface-soft}` or `{colors.surface-wash}`) for separation. Padding is 0 around the image, then 8px/16px for text content.

### Badges
**`badge-sale`** — A bright red-pink (#ff5268) badge with white uppercase text, used to flag discounted items. Small 4px radius and tight 2px/8px padding keep it unobtrusive but visible. Always positioned at the top-left corner of product images.

**`badge-new`** — A pink (#db7093) badge for new arrivals or recently added products. Same dimensions as the sale badge but in the brand's accent pink to distinguish "new" from "sale" without competing for attention.

**`badge-star`** — A warm yellow (#fbcd0a) badge with dark text for displaying rating scores or "Top Rated" labels. Uses smaller caption typography and sits inline with review counts.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height on desktop, with white background and a subtle bottom border (`{colors.hairline-soft}`). Contains the brand logo, category links in 15px/600 weight, a search bar, and cart icon. On mobile, collapses to 60px height with a hamburger menu and condensed logo.

**`nav-bar-mobile`** — The mobile variant at 60px height. The search bar moves to a toggleable overlay, and category links become a slide-out drawer. The cart icon remains visible.

### Forms
**`text-input`** — Standard text input fields used in search, newsletter signup, and account forms. White background with a light gray border (`{colors.hairline}`) and 8px radius. On focus, the border becomes a 2px teal stroke. Error state switches to a 2px red-pink stroke (`{colors.badge-sale}`). Height is 48px with 12px/16px padding for comfortable touch targets.

**`quantity-selector`** — A compact inline control for adjusting product quantities, with minus/plus buttons flanking a numeric display. Uses a white background with a single hairline border and 8px radius. Height is 44px to sit alongside buttons without dominating.

### Search
**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a soft gray background (`{colors.surface-soft}`) and subtle border. On focus, the background turns white and the border becomes a 2px teal stroke. Height is 44px with generous padding for easy tapping. The placeholder text uses the muted gray (#7b7b7b).

### Filters
**`filter-chip`** — Pill-shaped filter options for sorting by size, brand, or diaper type. White background with a hairline border and 6px/16px padding. Active state fills with the brand teal and white text. Multiple chips can be active simultaneously.

### Footer
**`footer`** — A full-width footer on a light teal wash background (`{colors.surface-wash}`) with links in muted gray, organized in columns. Link text uses 14px/400 weight and shifts to teal on hover. Contains standard sections: Shop, Support, About, and Social. Social icons use their respective brand colors (#3b5998 for Facebook, #1da1f2 for Twitter, #bd081d for Pinterest).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 items), hamburger nav, search becomes overlay, filter chips stack vertically, footer collapses to single column, buttons go full-width |
| Tablet | 744–1128px | Two-column product grid, nav links condensed to dropdowns, filter chips wrap in rows, footer splits into 2 columns |
| Desktop | 1128–1440px | Three-column product grid, full nav bar visible, filter chips inline, footer in 4 columns |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, extra whitespace on sides |

### Touch Targets
- All interactive elements (buttons, inputs, chips) maintain minimum 44px height for touch accessibility
- Product card tap targets are the entire card, not just text
- Filter chips are 36px+ tall with 16px+ horizontal padding
- Quantity selector buttons are 44px x 44px tap areas
- Nav links on mobile have 48px tap targets

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger menu with a slide-out drawer
- Search bar collapses to an icon that opens a full-width overlay input
- Product grid collapses from 3-4 columns to 1-2 columns
- Filter chips collapse from inline to stacked with a "Filters" toggle button
- Footer columns collapse from 4 to 1, stacking vertically
- Product images switch from landscape to square crop on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states** for most components were not extractable from static CSS; active/focus states are inferred from common patterns
- **Error styling** for forms beyond the text-input error border is unknown (error messages, validation icons, inline help text)
- **Dark mode** is not present on the live site; no dark palette exists
- **Sub-brand palettes** (if any for subscription tiers or gift registries) could not be identified
- **Animation and transition durations** are not documented; the site appears to use minimal transitions
- **Typography scale** is inferred from common e-commerce patterns; exact font sizes for every heading level may vary
- **Spacing system** is estimated from common patterns; the exact spacing scale may differ in production
- **Checkout-specific components** (Shopify checkout overrides) were not extractable
- **The extracted color list is heavily polluted with social media brand colors (#3b5998, #1da1f2, #bd081d, #344e86) and Shopify/Afterpay/Klarna widget colors (#0d95e8, #aa0719). The brand's true primary (#108474) and accent (#db7093) were identified as the most distinctive non-platform colors.**
- **Font stack is inferred from extracted declarations; Nunito Sans appears to be the primary brand font, but exact weights and fallback order may differ**
