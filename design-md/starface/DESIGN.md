---
version: alpha
name: "Starface"
source_url: "https://starface.world"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Starface is a skincare brand that feels like a party on your face — a joyful, unapologetically playful rebellion against the shame and seriousness that often surrounds acne. The brand’s visual identity is built on a foundation of high-voltage contrast: a screaming yellow `#fdff00` (the brand’s primary voltage) against a soft, almost saccharine pink `#ff9cee` and a crisp, clinical blue `#1990c6` that grounds the energy. The canvas is a clean `#dedede` light grey, not a sterile white, which gives the entire experience a soft, approachable warmth. The typography is dominated by the rounded, friendly forms of ABC Diatype Rounded, used in heavy and black weights for headlines that feel bold and confident, paired with the monospaced, technical edge of GT Pressura Mono Text for accents and data — a clever nod to the brand’s “pimple patch as medical device” credibility. The signature design move is the pill-shaped button and the full-round badge (`{rounded.full}`), used for the iconic star-shaped patch itself, which is both product and logo. Every corner is soft (`{rounded.sm}` for cards, `{rounded.lg}` for modals), and the spacing is generous, letting the bright colors breathe. The mood is optimistic, loud, and inclusive — a skincare brand that says “spots are fine, have fun.”

colors:
  primary: "#fdff00"
  primary-active: "#e5e600"
  primary-disabled: "#fefecc"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#dedede"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#121212"
  accent-pink: "#ff9cee"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  star-yellow: "#fdff00"
  star-pink: "#ff9cee"
  badge-green: "#00c853"
  badge-red: "#ff1744"

typography:
  display-xl:
    fontFamily: "'ABC Diatype Rounded Black', 'ABC Diatype Rounded', -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'ABC Diatype Rounded Heavy', 'ABC Diatype Rounded', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'ABC Diatype Rounded Heavy', 'ABC Diatype Rounded', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'ABC Diatype Rounded', -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'ABC Diatype Rounded', -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'ABC Diatype Rounded', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'ABC Diatype Rounded', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'ABC Diatype Rounded', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'GT Pressura Mono Text', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'ABC Diatype Rounded Heavy', 'ABC Diatype Rounded', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 800
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'ABC Diatype Rounded Heavy', 'ABC Diatype Rounded', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 800
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "'ABC Diatype Rounded', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'ABC Diatype Rounded Heavy', 'ABC Diatype Rounded', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 800
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'GT Pressura Mono Text', monospace"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-accent-pink:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  icon-button-circle:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "3px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "2px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.md}"
    objectFit: contain
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-section-accent-pink:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-section-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  badge-new:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-eco:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  star-patch-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand’s signature yellow `{colors.primary}` with dark `{colors.on-primary}` text. Uses the heavy rounded font `{typography.button-md}` and a full pill shape `{rounded.full}`. On hover, shifts to a slightly darker yellow `{colors.primary-active}`. Disabled state uses a pale yellow `{colors.primary-disabled}` with muted text. **`button-secondary`** — An outlined variant on the `{colors.canvas}` background with a 2px solid `{colors.ink}` border. Maintains the same pill shape and typography. Active state fills the background with `{colors.hairline}`. **`button-tertiary-text`** — A text-only button with no background or border, using the same heavy typography for a clean, minimal action. **`button-pill-accent-pink`** and **`button-pill-accent-blue`** — Secondary accent buttons using the brand’s pink and blue palette, used for promotional or secondary CTAs like “Shop Now” or “Learn More.”

### Cards
**`product-card`** — A white `{colors.surface-card}` card with `{rounded.lg}` corners and `{spacing.base}` padding. The product image inside uses `{rounded.md}` and `object-fit: contain`. A **`product-card-badge`** sits on top, using the yellow `{colors.primary}` with `{rounded.full}` and monospaced `{typography.badge}` text for a technical, medical-device feel. Cards are used for product listings, bundles, and subscription options.

### Navigation
**`top-nav`** — A fixed-height 64px bar on the `{colors.canvas}` background. Navigation links use `{typography.nav-link}` (heavy, uppercase, 14px). Active links are indicated with a 3px `{colors.primary}` bottom border. Inactive links use `{colors.muted}`. The nav includes the Starface star logo, a search icon, and a cart icon.

### Forms & Inputs
**`text-input`** — A white `{colors.surface-card}` input with `{rounded.sm}`, a 2px `{colors.hairline}` border, and `{typography.body-md}`. On focus, the border switches to `{colors.primary}`. **`search-bar`** — A pill-shaped `{rounded.full}` input with a 2px `{colors.hairline}` border, used in the header and on search pages. Focus state uses the yellow `{colors.primary}` border. **`quantity-selector`** — A pill-shaped control for adjusting product quantities, using `{colors.surface-soft}` background.

### Hero Sections
**`hero-section`** — Full-width sections that use the brand’s yellow `{colors.primary}`, pink `{colors.accent-pink}`, or blue `{colors.accent-blue}` as full backgrounds. They feature `{typography.display-xl}` headlines and generous `{spacing.section}` padding. These are used for major campaigns, product launches, and seasonal promotions.

### Badges
**`badge-new`** — A pink `{colors.accent-pink}` pill badge for new arrivals. **`badge-sale`** — A red `{colors.badge-red}` pill badge for sale items. **`badge-eco`** — A green `{colors.badge-green}` pill badge for eco-friendly or sustainable products. All use `{typography.badge}` (monospaced, uppercase). **`star-patch-badge`** — A 32x32px circular badge in the brand yellow, used to represent the iconic star-shaped pimple patch itself, often placed on product images or in the cart.

### Footer
**`footer`** — A dark `{colors.ink}` background with white `{colors.canvas}` text. Links use `{typography.link}` and are white. The footer contains brand information, customer service links, social media icons, and a newsletter signup.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, top-nav collapses to hamburger menu, hero sections stack vertically, product cards display in a 2-column grid, buttons become full-width, search bar collapses to icon-only, footer links stack. |
| Tablet | 744–1128px | Two-column layout for product grids, top-nav remains expanded but with reduced padding, hero sections use a single column with larger type, search bar is full-width but with reduced height. |
| Desktop | 1128–1440px | Three-column product grids, full top-nav with all links visible, hero sections use two-column layouts (text + image), search bar is a compact pill in the nav. |
| Wide | > 1440px | Four-column product grids, maximum content width of 1440px centered, hero sections use full-width imagery with overlaid text, search bar remains a compact pill. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px and a minimum width of 44px on mobile.
- Icon buttons are 40x40px minimum.
- Quantity selector and badge elements are 40px tall.
- Product card images are at least 200px tall on mobile.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile (< 744px). The menu overlay uses `{colors.canvas}` background with `{colors.ink}` text.
- Product filters collapse to a single “Filter” button that opens a bottom sheet on mobile.
- Footer links collapse into accordion-style sections on mobile.
- Hero sections collapse from side-by-side text and image to stacked on mobile.
- Search bar collapses to an icon-only button that expands to a full-width input on tap.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (e.g., text-input, search-bar, nav-links) could not be reliably extracted from the live site and are inferred from brand patterns.
- Error styling for form inputs (e.g., red border, error message typography) is not present in the extracted data.
- Dark mode or high-contrast mode tokens are not defined.
- Sub-brand or seasonal palette variations (e.g., Halloween, Pride) are not captured.
- The exact font-weight values for ABC Diatype Rounded variants (e.g., 400, 600, 700, 800, 900) are inferred from common usage and may not match the actual font files.
- The `object-fit: contain` declaration found in the hints is applied to product card images but may also apply to other media elements.
- The `inherit` font-family declaration found in the hints is not used as a primary token.
- The `#121212` color is used for `ink` but may also be used for other text or background elements.
- The `#136f99` color is used for `accent-blue-dark` but may have other uses (e.g., hover states for blue buttons).
