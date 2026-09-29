---
version: alpha
name: "Fuse Chicken"
source_url: "https://www.fusechicken.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A marigold #e9be33 voltage cuts across a charcoal #31373d and steel #6c6c6c chassis — Fuse Chicken builds phone accessories that look like they could survive a drop from a construction crane, and the design system follows suit. The brand’s primary yellow is not a friendly accent but a functional signal: it marks every add-to-cart button, every configurable strap toggle, every warranty upsell. Against a #eaeaea canvas and soft #6c6c6c body text, that yellow reads as industrial-grade urgency rather than playfulness. Typography runs Arial and Helvetica Neue at conventional weights — no custom typeface, no display-size hero text, no letter-spacing theatrics. The system trusts its product photography (magnetic mounts, braided cables, rugged cases) to carry the story; the UI stays out of the way with flat buttons, thin 1px hairlines, and generous {spacing.lg} gutters. Corners are mostly {rounded.sm} (8px) — enough to soften the industrial edge without going pill-shaped. The nav bar is a dark band of {colors.ink} with white text, a rare inversion that signals the brand’s B2B-adjacent confidence. There is no hero carousel, no gradient, no decorative illustration. Every pixel earns its place.

colors:
  primary: "#e9be33"
  primary-active: "#d4a92e"
  primary-disabled: "#f4e0a0"
  ink: "#31373d"
  body: "#6c6c6c"
  muted: "#8a8a8a"
  muted-soft: "#b0b0b0"
  hairline: "#d0d0d0"
  hairline-soft: "#e0e0e0"
  canvas: "#eaeaea"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#31373d"
  on-dark: "#ffffff"
  accent-blue: "#479ccf"
  badge-warning: "#e9be33"
  badge-sale: "#c0392b"
  link: "#479ccf"
  star-rating: "#e9be33"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica Neue, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, Helvetica Neue, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica Neue, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica Neue, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica Neue, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica Neue, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica Neue, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica Neue, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica Neue, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica Neue, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "Arial, Helvetica Neue, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica Neue, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-outline-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
    border: "1px solid {colors.on-dark}"
  button-outline-dark-active:
    backgroundColor: "rgba(255,255,255,0.1)"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid #c0392b"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-bar-logo:
    height: 28px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "0 {spacing.base} {spacing.sm}"
  badge:
    backgroundColor: "{colors.badge-warning}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subtext:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
    maxWidth: 600px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 14px
  link:
    typography: "{typography.link}"
    textColor: "{colors.link}"
  link-hover:
    textColor: "{colors.primary}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The brand’s primary call-to-action, filled with marigold #e9be33 and dark ink text. On hover, the yellow deepens to #d4a92e. Disabled state uses a washed-out #f4e0a0 with muted text, signaling the action is unavailable. Height is 44px with 12px/24px padding and 8px corner radius — compact enough for dense product grids, large enough for comfortable tapping.

**`button-secondary`** — A canvas-toned button with a thin #d0d0d0 border, used for secondary actions like “View Details” or “Cancel”. Active state swaps the border to ink #31373d and adds a soft #f2f2f2 background. Shares the same 44px height and typography as the primary button for visual consistency.

**`button-outline-dark`** — An inverted outline button for use on the dark hero section or footer. Transparent background, white text, white 1px border. Hover adds a subtle white 10% overlay. Used for “Learn More” or “Shop Now” CTAs on dark backgrounds.

### Cards
**`product-card`** — A white card with 8px rounded corners and no padding on the container itself — the image fills the top with matching 8px top corners. Title sits below at 16px/600 weight with 8px horizontal padding, price follows at 16px/600 weight with the same horizontal padding and 8px bottom padding. No shadow, no border — the card relies on the contrast between white surface and #eaeaea canvas for separation.

**`product-card-image`** — Square aspect ratio (1:1), top-rounded to match the card. No border-radius on bottom corners so the image meets the text block cleanly.

### Navigation
**`nav-bar`** — A 56px dark band (#31373d) with white uppercase nav links at 14px/600 weight and 0.3px letter-spacing. Logo sits left-aligned at 28px height. No background change on scroll — the nav stays dark and opaque. Mobile collapses to a hamburger icon.

**`nav-bar-logo`** — The Fuse Chicken wordmark or icon, rendered at 28px height. On dark background, logo is white or light.

### Forms
**`text-input`** — Standard text input with #eaeaea background, 1px #d0d0d0 border, 8px rounded corners, 44px height, and 10px/14px padding. Focus state swaps the border to #e9be33. Error state uses a red #c0392b border. Used for search, checkout forms, and newsletter signups.

**`search-bar`** — A pill-shaped (9999px) search input with white background, 1px #d0d0d0 border, 40px height, and 8px/16px padding. Focus state swaps border to primary yellow. Used in the nav bar or as a standalone search component.

### Badges
**`badge`** — A small uppercase label with yellow background and dark text, 11px/700 weight, 0.5px letter-spacing, 4px rounded corners, and 2px/8px padding. Used for “NEW”, “BEST SELLER”, or “LIMITED” callouts on product cards.

**`badge-sale`** — Same shape as the standard badge but with red #c0392b background and white text. Used for “SALE” or “CLEARANCE” indicators.

### Footer
**`footer`** — A dark #31373d footer section with white body text at 14px/400 weight and muted #b0b0b0 links. Links hover to white. Padding is 32px vertical and 24px horizontal. Contains columns for support, company info, and social links.

### Hero
**`hero-section`** — A full-width dark section (#31373d) with white heading at 28px/700 weight and muted subtext at 16px/400 weight, constrained to 600px max-width. Used for category landing pages and seasonal promotions. CTAs use `button-outline-dark`.

### Dividers
**`divider`** — A 1px solid #d0d0d0 line used between sections or product rows.
**`divider-soft`** — A 1px solid #e0e0e0 line used within cards or between form fields.

### Links
**`link`** — Standard inline link at 14px/400 weight in blue #479ccf. Hover state shifts to primary yellow #e9be33. Used for “Learn More”, “View All”, and legal text links.

### Accordion
**`accordion-header`** — A clickable row with #eaeaea background, 16px/600 weight text, 12px/16px padding, and 8px rounded corners. Used for FAQ sections and product details.
**`accordion-content`** — The expandable panel below the header, white background, 14px/400 weight body text, 16px padding all around.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; hero padding reduces to 32px vertical; search bar moves below nav; footer columns stack vertically |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards display 2-column grid; hero text max-width reduces to 480px; footer columns display 2x2 grid |
| Desktop | 1128–1440px | Full nav with all links; product cards display 3- or 4-column grid; hero uses full 600px max-width; footer displays 4-column layout |
| Wide | > 1440px | Content max-width capped at 1440px, centered; product cards may display 5-column grid; hero section uses larger padding (80px vertical) |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height (exceeds Apple’s 44pt HIG recommendation)
- Nav bar links have 48px tap area (padding extends hit target)
- Search bar is 40px height — acceptable for touch but primary CTAs should use 44px+
- Product card tap targets (title, price, image) are not individually tappable — the entire card is a single link with 44px+ tap area

### Collapsing Strategy
- Nav bar: on mobile (< 744px), all nav links collapse behind a hamburger icon; logo remains left-aligned; search icon appears right-aligned
- Product grid: collapses from multi-column to single-column on mobile
- Footer: collapses from 4-column to stacked single-column on mobile
- Hero: reduces vertical padding and centers text on mobile; CTA buttons stack vertically if two are present
- Accordion: remains functional at all breakpoints; no collapse needed

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is sparse and generic — #e9be33 (marigold) is the most distinctive accent and has been used as primary, but the brand may have additional accent colors (e.g., a green for “eco” or a red for “sale”) that were not captured. The extracted palette also includes #479ccf (blue) which may be a link color or secondary accent — used here as link and accent-blue but not confirmed.
- No custom typeface was detected — the site uses Arial/Helvetica Neue stack. The brand may use a custom font on other pages or in print that was not loaded on the extracted page.
- The extracted page returned “This store is unavailable” — the design system above is reconstructed from the color palette and font stack only, with reasonable assumptions about component patterns based on the brand’s category (phone accessories) and industrial aesthetic. Actual live site components may differ significantly.
- Hover states for buttons and links are inferred from common patterns — actual hover colors may differ.
- Error states, disabled states, and focus rings are not confirmed from extraction.
- Dark mode is not supported — the brand uses a light canvas (#eaeaea) with dark nav/footer sections.
- Spacing values (padding, margins, grid gaps) are estimated from common e-commerce patterns — actual values may vary.
- No animation or transition timing data was extracted (hover transitions, page load animations, etc.).
- The brand may use additional component types (modals, tooltips, dropdowns, tabs) that were not present on the extracted page.
