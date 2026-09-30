---
version: alpha
name: "JJGames"
source_url: "https://www.jjgames.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A retro game retailer that wears its inventory like a badge of honor, anchored on a deep crimson #660000 that reads as worn-in arcade carpet and late-night CRT glow. The brand's primary voltage is #e47911 — a burnt orange that fires across every add-to-cart button, price tag, and category pill, cutting through the dark canvas like a neon OPEN sign in a strip mall. Two reds (#e4282c and #d30708) handle urgency signals — sold-out badges, clearance flags, and cart notifications — while #ff9999 softens the palette as a hover-state blush on secondary actions. The system runs on system fonts (Arial, Geneva, Helvetica, Verdana) with no custom typeface, a pragmatic choice that prioritizes page speed and legibility over brand typography; the site loads fast on a 2010s browser in a basement. Cards use sharp corners ({rounded.none}) for product thumbnails and soft {rounded.sm} for buttons, a mix that feels more warehouse than showroom. The search bar sits as a full-width orange-outlined field, and the footer stacks category links in dense columns — this is a site built for scanning, not lingering. The palette's gray (#8e8e8e and #aaaaaa) handles secondary text and dividers, keeping the focus on the reds and oranges that signal "this is where the deals are."

colors:
  primary: "#e47911"
  primary-active: "#d06b0f"
  primary-disabled: "#f5c48a"
  ink: "#222222"
  body: "#333333"
  muted: "#8e8e8e"
  muted-soft: "#aaaaaa"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#e4282c"
  accent-red-dark: "#d30708"
  accent-red-soft: "#ff9999"
  brand-crimson: "#660000"

typography:
  display-xl:
    fontFamily: "Arial, Geneva, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, Geneva, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Geneva, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Geneva, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Geneva, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Geneva, Helvetica, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Geneva, Helvetica, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Geneva, Helvetica, Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, Geneva, Helvetica, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Geneva, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Geneva, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Geneva, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  link:
    fontFamily: "Arial, Geneva, Helvetica, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Geneva, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
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
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-danger:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-danger-active:
    backgroundColor: "{colors.accent-red-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "2px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-item:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
    height: 60px
  nav-bar-item-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
    height: 60px
    borderBottom: "3px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 48px
    border: "2px solid {colors.primary}"
  search-bar-icon:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 48px
    width: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "1/1"
    objectFit: "cover"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    fontWeight: 700
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-clearance:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  footer:
    backgroundColor: "{colors.brand-crimson}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
    hoverTextColor: "{colors.accent-red-soft}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
    fontWeight: 700
    marginBottom: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.brand-crimson}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} 0"
  breadcrumb-active:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    fontWeight: 600
  pagination:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "4px 12px"
  pagination-disabled:
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  cart-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
    padding: "0 6px"
  filter-checkbox:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
    border: "2px solid {colors.hairline}"
  filter-checkbox-checked:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
    border: "2px solid {colors.primary}"
  rating-stars:
    color: "{colors.primary}"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in burnt orange {colors.primary} with white text and bold 700-weight type. Used for "Add to Cart," "Checkout," and primary form submissions. On hover, shifts to {colors.primary-active}; disabled state fades to {colors.primary-disabled}. **`button-secondary`** — A white button with a subtle gray border, used for "View Details," "Continue Shopping," and secondary actions. Active state gains a dark ink border. **`button-danger`** — Reserved for destructive actions like "Remove from Cart" or "Cancel Order," using {colors.accent-red} that deepens to {colors.accent-red-dark} on hover. **`button-pill`** — A compact, fully rounded variant used for filter tags and quick-select options, sized at 36px height for dense layouts.

### Cards
**`product-card`** — The core inventory display unit, a white card with no border-radius and a soft hairline border. The product image fills the top with a 1:1 aspect ratio and no rounding — the sharp corners reinforce the utilitarian, warehouse feel. The title sits below in 16px/600 weight, with the price in {colors.primary} at 16px/700 weight. Badges overlay the top-left of the image: red for "Sale," gray for "Sold Out," orange for "Clearance." Cards stack in a responsive grid with 16px gaps. **`product-card-badge`** — Small, sharp-cornered labels that communicate inventory status at a glance. Three variants cover the core states: sale (red), sold-out (gray), and clearance (orange).

### Navigation
**`nav-bar`** — A 60px white bar with a bottom border, housing the brand logo on the left and category links on the right. Active nav items underline with a 3px {colors.primary} bar. The search bar sits below the nav on mobile, or inline on desktop. **`nav-bar-item`** — Individual navigation links with 16px horizontal padding. Active state uses {colors.primary} text and a bottom border. **`category-pill`** — Filter pills for console generations (NES, SNES, PS1, etc.), rendered as fully rounded chips in soft gray. The active pill fills with {colors.primary} and white text.

### Forms
**`text-input`** — Standard input fields with a 1px hairline border and 44px height. On focus, the border thickens to 2px and shifts to {colors.primary}. Error state uses a 2px {colors.accent-red} border. **`select-input`** — Dropdown selectors matching the text-input dimensions, used for sorting and filtering. **`filter-checkbox`** — Square checkboxes with 2px hairline borders. Checked state fills with {colors.primary} and white checkmark.

### Search
**`search-bar`** — A full-width input field with a 2px {colors.primary} border, paired with a square orange icon button on the right. The input uses body-md type for readability. On mobile, the search bar collapses into a single icon that expands on tap. **`search-bar-icon`** — A 48px square button in {colors.primary} with a white magnifying glass icon.

### Footer
**`footer`** — A deep crimson {colors.brand-crimson} footer with white text, organized into columns of category links. Headings use 16px/700 weight, links use 14px/400 weight with a blush hover state. The footer spans the full width and includes copyright and social links at the bottom.

### Hero
**`hero-banner`** — A full-width banner in {colors.brand-crimson} with white display text and a single orange CTA button. Used for seasonal sales, new arrivals, and clearance events. The CTA uses {colors.primary} with white text and 48px height.

### Badges & Indicators
**`cart-badge`** — A small red circle overlaying the cart icon, displaying the item count. Uses {colors.accent-red} background with white text, fully rounded. **`rating-stars`** — Star icons in {colors.primary} for user reviews, sized at 16px. **`pagination`** — Page number links at the bottom of product listings. The active page fills with {colors.primary}; disabled pages use {colors.muted-soft}.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; search bar becomes an expandable icon; footer stacks vertically; hero banner reduces padding to 32px; category pills wrap to two rows. |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; search bar remains full-width; footer splits into two columns; hero banner uses 48px padding. |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; search bar full-width; footer in four columns; hero banner uses 64px padding. |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; nav and footer centered; hero banner max-width 1200px. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Category pills and filter chips are 32px height, which is below the 44px recommendation but standard for dense filter strips.
- Cart badge is 20px — a visual indicator only, not a touch target.
- Pagination links are 36px minimum tap area.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-out drawer.
- The search bar collapses into a single icon that expands to a full-width field on tap.
- The footer's multi-column layout collapses to a single column with accordion-style expandable sections.
- Category filter pills wrap to a second row on mobile, with a "Show More" link if exceeding two rows.
- Product grid reduces from 4 columns on wide to 1 column on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components are inferred from common patterns; actual site hover colors may differ.
- Error state styling for forms (text-input-error) is assumed; no extracted data confirms the exact border color or error message typography.
- The hero banner component is inferred from the brand's color palette and category; no extracted data confirms its exact layout or CTA styling.
- Dark mode is not supported and no extracted data suggests a dark-mode palette.
- The brand's logo color and typography are unknown; the nav-bar assumes a white background with ink text.
- No extracted data for success, warning, or info alert components.
- The rating-stars component is assumed based on common e-commerce patterns; actual star color and size may vary.
- Footer link hover color (#ff9999) is inferred from the extracted palette; actual hover state may differ.
- The brand-crimson (#660000) is used for the footer and hero; it may also appear in other contexts not captured.
- No data on the brand's secondary or tertiary color usage beyond the extracted hex list.
- The extracted font list (Arial, Geneva, Helvetica, Verdana) is used literally; no custom web fonts were detected.
- The site may use additional system fonts or fallbacks not captured in the extraction.
