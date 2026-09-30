---
version: alpha
name: "Klutz"
source_url: "https://www.scholastic.com/klutz"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand that treats craft instruction like a playground manual — bright, direct, and unafraid of mess. Klutz’s visual system is built on a white canvas (#ffffff) that lets the saturated product photography do the heavy lifting, with a primary accent of #e3000f — a stop-sign red that appears on the logo, instructional arrows, and key call-to-action buttons, giving every page a sense of confident, no-nonsense guidance. The typography runs a clean sans-serif stack (Arial, Helvetica, system-ui) at moderate weights, never competing with the step-by-step photography that is the real content hero. Cards and buttons use a soft 8px radius (`{rounded.sm}`), friendly without being childish, while the product grid relies on generous 24px gaps (`{spacing.lg}`) and a consistent 16px padding inside every tile. The brand’s signature move is the “Klutz Certified” badge — a small, red-accented label that appears on product cards and detail pages, signaling that the item has been kid-tested and approved. Navigation is minimal: a simple top bar with the logo, a search icon, and a cart icon, all in `{colors.ink}` (#222222) against the white canvas. The footer is dense but structured, with links organized under bold category headers and a prominent “Klutz Guarantee” callout in `{colors.muted}` (#666666). There is no gradient, no shadow-heavy card, no decorative flourish — every design decision serves clarity and action, mirroring the brand’s promise that “the book comes with everything you need.”

colors:
  primary: "#e3000f"
  primary-active: "#c2000d"
  primary-disabled: "#f5b3b8"
  ink: "#222222"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d9d9d9"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  badge-certified-bg: "#e3000f"
  badge-certified-text: "#ffffff"
  badge-new-bg: "#f5a623"
  badge-new-text: "#222222"
  star-rating: "#f5a623"
  link: "#e3000f"
  link-hover: "#c2000d"
  error: "#d32f2f"
  success: "#2e7d32"
  warning: "#f5a623"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  footer-heading:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0
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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
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
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  text-input-error:
    border: "1px solid {colors.error}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-logo:
    height: 36px
  nav-bar-icon:
    height: 24px
    textColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.badge-certified-bg}"
    textColor: "{colors.badge-certified-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.star-rating}"
    marginTop: "{spacing.xs}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    marginTop: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-heading:
    typography: "{typography.footer-heading}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.sm}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.sm}"
  footer-link-hover:
    textColor: "{colors.primary}"
  footer-guarantee:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for “Add to Cart,” “Shop Now,” and “Subscribe.” Rendered in `{colors.primary}` (#e3000f) with white text and an 8px radius (`{rounded.sm}`). On hover, the background shifts to `{colors.primary-active}` (#c2000d). The disabled state uses `{colors.primary-disabled}` (#f5b3b8) with white text, signaling that the action is unavailable. **`button-secondary`** — A bordered alternative for less prominent actions like “View Details” or “Learn More.” Uses a white background, `{colors.ink}` text, and a 1px `{colors.hairline}` border. On hover, the border becomes `{colors.ink}` and the background shifts to `{colors.surface-soft}`. **`button-tertiary-text`** — A text-only button for inline actions like “Cancel” or “Clear.” Uses `{colors.primary}` text on a transparent background, with no border or padding. On hover, the text shifts to `{colors.primary-active}`. **`button-pill`** — A compact, fully rounded button used for filter tags and quick actions. Uses `{colors.primary}` background, white text, and `{rounded.full}`. Height is 36px, padding is 8px 20px.

### Cards
**`product-card`** — The primary content container for the product grid. A white card (`{colors.surface-card}`) with an 8px radius (`{rounded.sm}`) and 16px padding. The product image sits at the top with a 4px radius (`{rounded.xs}`) and a 1:1 aspect ratio. Below the image, the title uses `{typography.title-sm}`, the price uses `{typography.body-md}` with 600 weight, and the rating uses `{typography.caption}` in `{colors.star-rating}` (#f5a623). A badge (`{colors.badge-certified-bg}`) may appear in the top-left corner of the image, using `{typography.badge}` with uppercase text. **`hero-banner`** — A full-width section at the top of category and landing pages. Uses a `{colors.surface-soft}` background, `{typography.display-xl}` for the headline, and a single `{colors.primary}` CTA button. Padding is `{spacing.section}` on the vertical axis and `{spacing.lg}` on the horizontal.

### Navigation
**`nav-bar`** — A fixed top bar at 64px height, white background (`{colors.canvas}`), with a 1px bottom border in `{colors.hairline-soft}`. Contains the Klutz logo (36px height) on the left, and icon buttons for search and cart (24px each) on the right. Navigation links use `{typography.nav-link}` with `{colors.ink}`. **`category-tag`** — A pill-shaped filter tag used in category navigation. Uses `{colors.surface-soft}` background, `{colors.ink}` text, and `{rounded.full}`. The active state uses `{colors.primary}` background with white text.

### Forms
**`text-input`** — A standard input field for forms (search, checkout, newsletter). White background, `{colors.ink}` text, 44px height, 12px 16px padding, and an 8px radius (`{rounded.sm}`). The border is 1px `{colors.hairline}`. On focus, the border becomes 2px `{colors.primary}` with no outline. The error state uses a 1px `{colors.error}` border. **`select-dropdown`** — A styled select element matching the text-input dimensions and radius. Uses the same border and focus states. **`quantity-selector`** — A compact input for adjusting product quantities. 40px height, 8px 12px padding, bordered with `{colors.hairline}`. Contains increment/decrement buttons with transparent background and `{colors.ink}` text.

### Footer
**`footer`** — A dense, structured footer with a `{colors.surface-soft}` background. Links are organized under `{typography.footer-heading}` headers (uppercase, 700 weight). Each link uses `{typography.link}` in `{colors.muted}` with `{spacing.sm}` margin-bottom. On hover, links shift to `{colors.primary}`. **`footer-guarantee`** — A highlighted callout within the footer, using a white background (`{colors.canvas}`), 1px `{colors.hairline}` border, and 16px padding. Contains the “Klutz Guarantee” message in `{typography.body-sm}`.

### Badges
**`product-card-badge`** — A small, red-accented label (`{colors.badge-certified-bg}`) with white uppercase text (`{typography.badge}`). Used to indicate “Klutz Certified,” “New,” or “Best Seller” status. Rounded with `{rounded.xs}`, padding 2px 8px. The “New” variant uses `{colors.badge-new-bg}` (#f5a623) with `{colors.badge-new-text}` (#222222).

### Accordion
**`accordion-header`** — A clickable header for collapsible sections (product details, shipping info). Uses `{typography.title-sm}` in `{colors.ink}`, with 16px vertical padding and a 1px bottom border in `{colors.hairline-soft}`. **`accordion-content`** — The expanded content area, using `{typography.body-sm}` in `{colors.body}`, with 8px top padding and 16px bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 column), nav-bar height reduces to 56px, hero-banner padding reduces to 32px vertical, footer links stack vertically, category-tags wrap to multiple rows, search-bar becomes full-width, product-card padding reduces to 12px, font sizes drop one step (display-xl becomes 28px, display-lg becomes 24px) |
| Tablet | 744–1128px | Two-column product grid, nav-bar remains at 64px, hero-banner uses 48px vertical padding, footer links in 2 columns, category-tags in a single scrollable row, product-card padding at 16px, font sizes at default |
| Desktop | 1128–1440px | Three-column product grid, nav-bar at 64px, hero-banner uses 64px vertical padding, footer links in 4 columns, category-tags in a single row with overflow scroll, product-card padding at 16px, font sizes at default |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, nav-bar at 64px, hero-banner uses 80px vertical padding, footer links in 4 columns, category-tags in a single row, product-card padding at 16px, font sizes at default |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px on mobile and tablet.
- Icon buttons in the nav-bar are 44x44px touch targets, even if the icon itself is 24px.
- Category-tag pills have a minimum height of 36px on mobile.
- Quantity-selector buttons are 40x40px touch targets.
- Accordion headers have a minimum height of 48px on mobile.

### Collapsing Strategy
- On mobile (< 744px), the nav-bar collapses to a single row with the logo, a hamburger menu icon, and the cart icon. The search bar moves to a collapsible overlay triggered by a search icon.
- The footer collapses from a multi-column layout to a single vertical stack on mobile.
- Product filters (category-tags) collapse into a horizontal scrollable strip on mobile and tablet, with a “Filters” button that opens a modal overlay.
- The hero-banner collapses to a single image with overlaid text on mobile, removing the CTA button to a separate section below.
- Accordion sections are collapsed by default on mobile and tablet, with only the first section expanded on desktop.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted font-family declarations were found on the live site. The typography stack uses a generic sans-serif fallback (Arial, Helvetica, system-ui) based on common web defaults. The brand may use a custom typeface (e.g., Klutz-branded font) that was not detectable from the error page crawl.
- No extracted hex colors were returned from the live site crawl (the page title was “Error Page”). The primary color (#e3000f) and all other color tokens are inferred from the Klutz brand identity as documented in public materials (logo, packaging, and product photography). This is a best-effort reconstruction, not a live extraction.
- Hover, focus, and active states for all components are based on common accessibility patterns and may not match the exact brand implementation.
- Error styling for forms (text-input-error) uses a generic red (#d32f2f) — the brand may use a different error color or pattern.
- The “Klutz Certified” badge and its variants are based on common brand usage; the exact badge design (icon, shape, placement) may differ on the live site.
- Dark mode is not supported and no dark-mode tokens are defined.
- The nav-bar collapse behavior (hamburger menu) is assumed; the live site may use a different mobile navigation pattern.
- No data on the brand’s loading states, skeleton screens, or empty states.
- No data on the brand’s animation or transition timing (ease curves, durations).
- The product-card aspect ratio (1:1) is an assumption; actual product images may use different ratios (e.g., 4:5, 3:4).
- The footer layout (4 columns on desktop) is inferred from common e-commerce patterns; the live site may use a different structure.
- No data on the brand’s use of icons (SVG, custom set, or Font Awesome). The nav-bar icons are assumed to be simple line icons.
- The brand’s checkout flow (cart, shipping, payment) is not documented and may use a third-party provider with its own design system.
