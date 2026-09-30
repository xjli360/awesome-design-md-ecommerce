---
version: alpha
name: "Four Horsemen Studios"
source_url: "https://sourcehorsemen.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A dark, mythic collector's marketplace where deep charcoal (#1a1a1a) and bone-white (#f5f5f0) stage action figures as museum artifacts. The brand's primary voltage is a muted crimson (#8b0000) that reads as aged blood or oxidized iron — used sparingly on price tags, sold-out badges, and cart buttons, never as a decorative wash. Product photography dominates the canvas at 1200px wide, with figures shot against black voids that make every armor joint and sculpted fur detail pop like a diorama. Type runs a condensed sans-serif at 14–18px for body copy, with display heads at 32px in a heavier weight that echoes the chiseled lettering on vintage toy packaging. The navigation is a persistent black bar with white text and a single search icon — no mega-menu, no category dropdowns, just "Shop All," "Mythic Legions," "Pre-Orders," and "About." Checkout flows through Shopify's standard widget, but the product grid uses a tight 4-column layout with `{rounded.sm}` (4px) corners on cards and `{rounded.full}` pill badges for "New" and "Pre-Order" tags. The overall feel is that of a specialty boutique for serious collectors — dark, focused, and unapologetically niche.

colors:
  primary: "#8b0000"
  primary-active: "#660000"
  primary-disabled: "#4a4a4a"
  ink: "#1a1a1a"
  body: "#2a2a2a"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#333333"
  hairline-soft: "#444444"
  canvas: "#f5f5f0"
  surface-soft: "#e8e8e0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#f5f5f0"
  sold-out-badge: "#8b0000"
  pre-order-badge: "#4a90d9"
  new-badge: "#2e7d32"
  sale-badge: "#e65100"
  star-rating: "#ffb400"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Industry', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  display-lg:
    fontFamily: "'Industry', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  display-md:
    fontFamily: "'Industry', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  display-sm:
    fontFamily: "'Industry', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.2px
  title-md:
    fontFamily: "'Industry', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.15px
  title-sm:
    fontFamily: "'Industry', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Industry', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Industry', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Industry', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Industry', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Industry', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase

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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 32px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    backgroundColor: "{colors.ink}"
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-sold-out:
    opacity: 0.5
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.new-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-pre-order:
    backgroundColor: "{colors.pre-order-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 40px
    border: 1px solid "{colors.hairline}"
  search-icon:
    textColor: "{colors.muted}"
    height: 20px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} 0"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
  product-grid:
    gap: "{spacing.base}"
    columns: 4
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: 1px solid "{colors.hairline}"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    height: 48px
  cart-icon:
    textColor: "{colors.on-dark}"
    height: 24px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Checkout," and "Subscribe." Rendered in the brand's deep crimson (`{colors.primary}`) with white uppercase text. On hover, shifts to `{colors.primary-active}` (#660000) for a darker, pressed-in feel. Disabled state uses `{colors.primary-disabled}` (#4a4a4a) with muted text to signal unavailability.

**`button-secondary`** — Used for secondary actions like "View Details" or "Continue Shopping." White background with dark ink text, bordered by a subtle `{colors.hairline}` stroke on hover. Active state fills with `{colors.surface-soft}` (#e8e8e0) for tactile feedback.

**`button-tertiary`** — A text-only button for inline actions like "Clear Filters" or "Cancel." No background, no border — relies entirely on `{colors.ink}` text with underline on hover. Keeps the collector's interface clean and uncluttered.

**`button-pill`** — Reserved for compact, high-visibility badges and filter toggles. Full pill shape (`{rounded.full}`) with condensed uppercase text. Used for "New Arrivals" filters and "Shop Now" quick-links on the hero section.

### Cards
**`product-card`** — The core product display unit, a white card with `{rounded.sm}` corners and no shadow — the brand relies on the dark product photography against the white card for contrast. Image area fills the top with a dark background (`{colors.ink}`) to make figure details pop. Title and price sit below in a clean stack. Sold-out items get 50% opacity (`{colors.product-card-sold-out}`) to visually de-emphasize without removing.

**`product-card-image`** — The image container uses `{rounded.sm}` on top corners only, creating a subtle visual break between photo and text. Background is always `{colors.ink}` to maintain the studio-photography aesthetic even on white cards.

### Badges
**`badge`** — Generic notification badge in crimson (`{colors.primary}`) with white uppercase text. Used for "Sold Out" and "Limited Edition" tags. Pill-shaped (`{rounded.full}`) with tight padding to sit cleanly on product images.

**`badge-new`** — Green badge (`{colors.new-badge}`) for recently released figures. Same pill shape and uppercase typography as the generic badge but in a distinct color to catch the collector's eye.

**`badge-pre-order`** — Blue badge (`{colors.pre-order-badge}`) for upcoming releases. Signals availability for reservation rather than immediate purchase.

**`badge-sale`** — Orange badge (`{colors.sale-badge}`) for discounted items. Used sparingly — the brand doesn't run frequent sales, so this badge carries weight when it appears.

### Navigation
**`nav-bar`** — A persistent, full-width black bar (`{colors.ink}`) at 60px height. White text in uppercase Industry font with `{rounded.none}` — no softening, no gradient. Links are spaced evenly with `{spacing.lg}` between them. The active link uses the brand crimson (`{colors.primary}`) as an underline accent.

**`nav-link-active`** — Active nav item in crimson text, signaling the current section. No background change — the color shift alone indicates state.

**`nav-link-inactive`** — Inactive nav items in white (`{colors.on-dark}`) with no hover effect beyond a subtle opacity shift. Keeps the bar clean and focused.

### Forms
**`text-input`** — Standard input field with white background, dark text, and a `{colors.hairline}` border. On focus, the border switches to `{colors.primary}` for clear visual feedback. Error state uses the same crimson border to indicate validation issues.

**`quantity-selector`** — A compact input for adjusting item quantities on product pages. White background with hairline border, matching the text-input style but narrower in width.

### Footer
**`footer`** — A dark footer matching the nav bar in `{colors.ink}`. Links are in `{colors.muted-soft}` (#999999) on hover, with generous padding (`{spacing.xxl}` top/bottom) and `{spacing.section}` horizontal margins. Contains legal text, social links, and brand copyright in `{colors.muted}`.

### Hero
**`hero-section`** — Full-width dark section (`{colors.ink}`) with `{spacing.section}` padding. Features a large display title (`{typography.display-xl}`) in white and a subtitle in muted-soft. Used for new line announcements and seasonal campaigns.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Product grid collapses to 2 columns; nav bar becomes hamburger menu; hero padding reduces to `{spacing.xl}`; font sizes drop one step (display-xl → display-lg) |
| Tablet | 744–1128px | Product grid shows 3 columns; nav links remain visible but condensed; hero maintains full padding |
| Desktop | 1128–1440px | Full 4-column product grid; all nav links visible; hero at full `{spacing.section}` padding |
| Wide | > 1440px | Max-width container at 1440px centered; product grid stays 4 columns with increased gap |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav links have 44px tap targets even when text is smaller
- Product card images are fully tappable with 44px minimum hit area
- Badges are not interactive — they're purely visual indicators

### Collapsing Strategy
- Nav bar collapses to hamburger menu below 744px, with a slide-out drawer from the left
- Product grid reduces columns from 4 → 3 → 2 as viewport shrinks
- Hero section reduces vertical padding by 50% on mobile
- Footer links stack vertically on mobile, with `{spacing.sm}` between items
- Search bar becomes full-width on mobile, replacing the nav search icon

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font-family declarations could not be extracted from the live site; the typography block uses educated guesses based on the brand's industry (collector/action-figure) and common Shopify themes. Actual fonts may differ.
- No meta theme-color was found; the dark nav bar may or may not extend to the browser chrome.
- Hover and focus states for all components are inferred from common patterns — exact animation durations, shadow depths, and transition curves are unknown.
- Error styling for forms (validation messages, error icons) could not be extracted.
- The brand may use additional accent colors for specific product lines (Mythic Legions sub-brands) that weren't visible in the extracted palette.
- Dark mode is not implemented — the site uses a light canvas with dark nav/footer consistently.
- Checkout styling uses Shopify's default widget, which may not match the brand's custom design tokens.
- Social media icon colors and hover states could not be reliably extracted.
- The star-rating color (#ffb400) is inferred from common e-commerce patterns, not extracted from the live site.
