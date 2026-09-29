---
version: alpha
name: "NL Beauty"
source_url: "https://nlbeauty.bg"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  NL Beauty is a Bulgarian makeup and cosmetics brand that speaks with the confidence of a global player while maintaining an earthy, approachable warmth. The palette is anchored by a deep teal-green (#108474) that appears across primary buttons, badges, and accent elements — a bold choice that avoids the predictable pink or black of conventional beauty brands. This primary voltage is supported by a rich, almost forest-like secondary palette: #102b26, #031612, and #01150f create depth in footers and overlays, while #3c9342 and #478947 introduce a fresh, botanical accent for sale tags or eco-friendly messaging. The brand is not afraid of drama — #a70100, #c31818, #d02f2e, and #d3413c form a family of reds used for error states, limited-edition badges, and price reductions, with #d50000 as an urgent callout. Warmth comes through #e9d8d1, #d8a598, and #b05e69 — blush and terracotta tones that soften the interface on product cards and promotional banners. The neutral backbone is clean and editorial: #f9fafb and #f5f5f5 for canvases, #e8e8e8 and #dedede for hairlines, #eeeeee and #f6f6f6 for soft surfaces, with #141414, #333333, and #545454 building a legible text hierarchy. Gold accents (#f4b453, #fcd46c) appear sparingly on loyalty badges and highlight stars. Typography runs on DM Sans as the primary workhorse — clean, geometric, and modern — with HelveticaNeueCyr, Inter, and Syne as supporting voices for display moments and nav. Corners are generally soft but not pill-like: buttons use `{rounded.sm}` (8px), cards use `{rounded.md}` (12px), and only search or promo banners reach `{rounded.full}`. The overall feeling is premium but not precious — a beauty brand that trusts color and photography over excessive ornamentation.

colors:
  primary: "#108474"
  primary-active: "#0d6b5e"
  primary-disabled: "#8fc7b9"
  ink: "#141414"
  body: "#333333"
  muted: "#545454"
  muted-soft: "#929292"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  border-strong: "#bdbfbf"
  canvas: "#f9fafb"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-strong: "#eeeeee"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-red: "#a70100"
  accent-red-soft: "#c31818"
  accent-red-badge: "#d02f2e"
  accent-red-urgent: "#d50000"
  accent-green: "#3c9342"
  accent-green-soft: "#478947"
  accent-gold: "#f4b453"
  accent-gold-light: "#fcd46c"
  accent-blush: "#e9d8d1"
  accent-terracotta: "#d8a598"
  accent-rose: "#b05e69"
  dark-forest: "#102b26"
  dark-deep: "#031612"
  dark-pitch: "#01150f"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'DM Sans', 'Syne', 'Inter', 'HelveticaNeueCyr', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'DM Sans', 'Syne', 'Inter', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'DM Sans', 'Inter', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'DM Sans', 'Inter', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'DM Sans', 'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', 'HelveticaNeueCyr', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', 'HelveticaNeueCyr', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', 'HelveticaNeueCyr', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'DM Sans', 'HelveticaNeueCyr', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'DM Sans', 'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'DM Sans', 'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'DM Sans', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'DM Sans', 'HelveticaNeueCyr', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.hairline}"
    padding: 10px 22px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-accent-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.hairline}"
    padding: 8px 20px
    height: 36px
  icon-button-circle:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.hairline}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.accent-red}"
    padding: 12px 16px
    height: 48px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  textarea-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.hairline}"
    padding: 12px 16px
    minHeight: 120px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1.5px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.06)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
  product-badge-sale:
    backgroundColor: "{colors.accent-red-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-limited:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-eco:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  price-display:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  price-sale:
    typography: "{typography.title-md}"
    textColor: "{colors.accent-red}"
  price-original:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: "line-through"
  color-swatch:
    rounded: "{rounded.full}"
    height: 28px
    width: 28px
    border: "2px solid transparent"
  color-swatch-selected:
    rounded: "{rounded.full}"
    height: 28px
    width: 28px
    border: "2px solid {colors.ink}"
  color-swatch-ring:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid {colors.hairline}"
  star-rating:
    textColor: "{colors.accent-gold}"
    fontSize: 16px
  star-rating-empty:
    textColor: "{colors.hairline}"
    fontSize: 16px
  hero-banner:
    backgroundColor: "{colors.dark-forest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 400px
  hero-banner-light:
    backgroundColor: "{colors.accent-blush}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    minHeight: 360px
  hero-overlay:
    backgroundColor: "{colors.dark-pitch}"
    opacity: 0.3
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    height: 56px
    borderBottom: "1px solid {colors.hairline-soft}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid {colors.primary}"
    height: 56px
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    height: 56px
  footer:
    backgroundColor: "{colors.dark-forest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.link}"
    opacity: 1
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "10px 16px"
    height: 44px
  newsletter-submit:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 44px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.md} 0"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  modal-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: "0 8px 32px rgba(0,0,0,0.12)"
  toast-success:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  toast-error:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  toast-warning:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  loading-spinner:
    borderColor: "{colors.hairline}"
    borderTopColor: "{colors.primary}"
    height: 24px
    width: 24px
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 36px
    minWidth: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 36px
    minWidth: 36px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
    padding: "0 {spacing.sm}"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 52px
  add-to-cart-button-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 52px
  wishlist-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  wishlist-button-active:
    backgroundColor: transparent
    textColor: "{colors.accent-red}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
    border: "1px solid {colors.hairline-soft}"
  review-stars:
    textColor: "{colors.accent-gold}"
    fontSize: 14px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, using the brand teal (#108474) on white text. Rounded at 8px (`{rounded.sm}`) with 12px vertical and 24px horizontal padding at 44px height. On hover, shifts to `button-primary-active` (#0d6b5e) for a darker, more grounded state. When disabled, uses `button-primary-disabled` (#8fc7b9) to visually signal inactivity while maintaining brand recognition.

**`button-secondary`** — An outlined variant for less prominent actions. Uses a white canvas background with a 2px hairline border (#dedede) and ink text. On hover or active state, the border swaps to the primary teal and the background shifts to surface-soft (#f5f5f5), creating a subtle but clear differentiation from the primary button.

**`button-tertiary-text`** — A text-only button with no background or border, using the primary teal for text color. Used for ghost actions like "Cancel", "View all", or "Learn more". Maintains the same 44px height and button-md typography for alignment consistency.

**`button-accent-red`** — An urgent action button using the brand's red family (#a70100). Used for "Clearance", "Limited Stock", or destructive confirmations. Slightly shorter at 40px with button-sm typography to differentiate from primary CTAs.

**`button-accent-gold`** — A warm accent button using gold (#f4b453) with dark ink text. Used for loyalty program signups, special offers, or seasonal promotions where the teal would feel too cool. Same dimensions as the red accent button.

**`button-pill-primary`** and **`button-pill-outline`** — Fully rounded pill buttons at 36px height, used for filter chips, tag selection, and compact inline actions. The pill-primary uses solid teal fill; the pill-outline uses a transparent background with a 1.5px hairline border. Both use button-sm typography.

### Cards
**`product-card`** — The primary product display container, using a white surface-card background with subtle shadow (0 1px 3px rgba(0,0,0,0.06)) and 12px corner rounding. On hover, the shadow deepens to 0 4px 12px rgba(0,0,0,0.1) for a lifted effect. The product image area uses a 1:1 aspect ratio with top-rounded corners matching the card radius.

**`product-badge-*`** — A family of four badge variants for product cards: `sale` (red #d02f2e), `new` (teal #108474), `limited` (gold #f4b453 with dark text), and `eco` (green #3c9342). All use uppercase badge typography at 11px, 4px corner rounding, and tight 2px/8px padding. Positioned absolutely over the product image.

**`review-card`** — Customer review container with white background, 12px rounding, 16px padding, and a soft hairline border (#e8e8e8). Star ratings use the gold accent (#f4b453) at 14px, with empty stars rendered in hairline (#dedede).

**`color-swatch`** and **`color-swatch-selected`** — Circular swatches at 28px diameter with full rounding. The selected state adds a 2px ink-colored ring. A larger `color-swatch-ring` variant at 32px with a hairline border is used for the swatch selector UI where the outer ring indicates the available color family.

### Navigation
**`nav-bar`** — Fixed or sticky top navigation at 72px height, white canvas background with a soft hairline bottom border (#e8e8e8). Nav links use uppercase DM Sans at 14px weight 500 with 0.2px letter spacing. The active link state uses the primary teal with a 2px bottom border. On scroll, the sticky variant adds a subtle box-shadow.

**`category-strip`** — A horizontal scrollable strip below the hero, 56px height, with a soft hairline bottom border. Category tabs use button-sm typography; the active tab shows a 2px teal bottom border and teal text, while inactive tabs use muted (#545454) text.

**`search-bar`** — A fully rounded search input at 48px height, using a surface-soft (#f5f5f5) background with a soft hairline border. On focus, the background shifts to white and the border becomes 1.5px teal. The pill shape (`{rounded.full}`) gives it a friendly, approachable feel.

### Forms
**`text-input`** — Standard text input at 48px height with 8px rounding, white background, 1.5px hairline border, and 12px/16px padding. Focus state swaps the border to primary teal. Error state uses the red accent (#a70100) border. The textarea variant extends to a minimum 120px height with the same styling.

**`select-input`** — Matches text-input dimensions and styling, used for dropdown selectors like sorting, filtering, and quantity. The chevron icon uses the muted text color.

**`newsletter-input`** and **`newsletter-submit`** — A paired input/button combination for email signup. The input is 44px with 8px rounding and a standard hairline border. The submit button uses the gold accent (#f4b453) with dark text, creating a warm, inviting call-to-action that stands apart from the primary teal system.

### Footer
**`footer`** — A dark forest green (#102b26) footer section with white text at 48px vertical padding and 64px section padding. Links are white at 80% opacity, increasing to full opacity on hover. The newsletter section within the footer uses the gold-accented submit button to draw attention.

### Feedback & State
**`toast-*`** — Three toast variants: success (green #3c9342), error (red #a70100), and warning (gold #f4b453 with dark text). All use 8px rounding, body-sm typography, and 12px/24px padding. Displayed at the top or bottom of the viewport with a slide-in animation.

**`modal-overlay`** and **`modal-card`** — A 50% opacity black scrim overlay with a white modal card at 12px rounding, 24px padding, and a deep shadow (0 8px 32px rgba(0,0,0,0.12)). The card uses body-md typography for content and title-md for headings.

**`loading-spinner`** — A 24px circular spinner with a hairline border and a teal top border for the rotating segment. Used across async actions like add-to-cart, search, and page transitions.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 columns), nav collapses to hamburger menu, category strip becomes horizontally scrollable with no active indicator, hero banners reduce to 280px min-height, product cards use full-width with reduced padding, footer stacks vertically, search bar moves to a full-width overlay, quantity selector becomes touch-friendly at 48px height |
| Tablet | 744–1128px | Two-column product grid (2-3 columns), nav shows limited links with "More" dropdown, category strip shows 4-5 visible tabs with scroll, hero banners at 360px min-height, product cards in 2-column grid, footer splits into 2-column layout, search bar remains in nav but expands on focus |
| Desktop | 1128–1440px | Three-column product grid (3-4 columns), full nav with all links visible, category strip shows 6-8 tabs, hero banners at 400px min-height, product cards in 3-column grid with hover effects, footer in 4-column layout, search bar in nav with full width |
| Wide | > 1440px | Max-width container at 1440px with centered content, four-column product grid, expanded hero with parallax or video background, additional whitespace around product cards, footer in 4-column layout with max-width constraint |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons and swatches use 36px minimum touch target with adequate spacing
- Quantity selector and pagination buttons use 40px and 36px respectively
- Mobile nav hamburger and cart icons use 48px touch targets
- Color swatches include invisible touch extension to meet 44px minimum

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px, with a slide-out drawer
- Category strip becomes a horizontal scroll container on mobile, hiding overflow tabs
- Product grid reduces from 4 columns to 1 column on the smallest screens
- Footer sections collapse into accordion-style expandable panels on mobile
- Search bar transforms from inline to full-screen overlay on mobile
- Hero banners reduce height and stack content vertically on mobile
- Secondary navigation (breadcrumbs, sub-categories) collapses into dropdown selectors

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components were inferred from common patterns; exact transition durations and easing curves (ease-in-out, cubic-bezier) were not extractable from the static site
- Error state styling for form inputs (error messages, icon placement, animation) was not observed on the live site
- Focus ring styles (color, width, offset, outline vs box-shadow) were not consistently present in the extracted CSS
- Dark mode or high-contrast mode overrides were not detected
- Sub-brand or collection-specific color palettes (e.g., holiday collections, collaborations) were not available
- Animation and motion specifications (duration, delay, spring physics, stagger timing) were not extractable
- Typography scale for mobile (smaller font sizes, adjusted line heights) was not reliably captured from the responsive CSS
- Specific spacing values for nested components (card grids, list items, stacked elements) were inferred from general spacing tokens
- Dropdown menu styles (mega menu, nested navigation, flyout positioning) were not observed
- Tooltip and popover component styles (arrow positioning, z-index, animation) were not present
- Loading skeleton or placeholder styles for async content were not detected
- Print stylesheet overrides were not available
- RTL (right-to-left) language support was not confirmed
- Accessibility-specific styles (skip links, focus indicators, aria states) were not fully extractable
- Custom checkbox and radio button styles were not observed in the extracted CSS
- Table and data display component styles were not present on the site
- Progress bar and step indicator component styles were not detected
- Cookie consent banner and GDPR-related component styles were not observed
