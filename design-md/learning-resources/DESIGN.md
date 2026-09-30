---
version: alpha
name: "Learning Resources"
source_url: "https://www.learningresources.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A bright, purposeful educational-toy brand that trusts saturated primary color as a learning cue — not as decoration. The site runs on a clean white canvas (#ffffff) with a single high-voltage accent, a warm coral-red that appears on every "Add to Cart" button, age-grade badges, and sale flags. This isn't a muted Montessori palette; it's a confident, slightly retro classroom aesthetic where red means "important action" and a soft sage-green (#8fbc8f) signals "in stock" or "available." Product photography dominates — each toy shot against white, with a consistent 45-degree angle and a subtle drop shadow that gives the objects weight and tangibility. Typography runs a clean sans-serif (likely a system stack or a single-weight web font) at modest sizes — titles at 20-24px, body at 14-16px — letting the product colors do the emotional work. Navigation is a straightforward horizontal bar with dropdowns for categories (STEM, Literacy, Gross Motor, etc.), and the search bar is a simple rectangular input with a magnifying-glass icon, not a pill. The grid is four-column on desktop, collapsing to two on tablet and one on mobile, with product cards that show title, price, a 4-5 star rating row, and a small "Ages 3+" badge in the top-left corner. The brand's voice is direct and teacherly — "Shop by Age," "Best Sellers," "New Arrivals" — with no playful naming or puns. The footer is dense with links (About, Customer Service, Rewards, Blog) and a newsletter signup with a coral-red submit button. The overall feel is less "design-forward toy brand" and more "trusted classroom supplier that happens to sell direct to parents" — functional, clear, and built for quick decision-making.

colors:
  primary: "#c0392b"
  primary-active: "#a93226"
  primary-disabled: "#e6b0aa"
  ink: "#2c3e50"
  body: "#34495e"
  muted: "#7f8c8d"
  muted-soft: "#bdc3c7"
  hairline: "#d5d8dc"
  hairline-soft: "#e5e8e8"
  canvas: "#ffffff"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  stock-green: "#8fbc8f"
  sale-red: "#e74c3c"
  star-gold: "#f1c40f"
  badge-bg: "#ecf0f1"
  badge-text: "#2c3e50"

typography:
  display-xl:
    fontFamily: "'Open Sans', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Open Sans', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Open Sans', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Open Sans', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Open Sans', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  footer-link:
    fontFamily: "'Open Sans', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

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
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 14px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 12px
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    marginTop: "{spacing.xs}"
  product-card-rating:
    typography: "{typography.caption}"
    color: "{colors.star-gold}"
    marginTop: "{spacing.xs}"
  age-badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  sale-badge:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  stock-badge:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.footer-link}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.canvas}"
    marginBottom: "{spacing.base}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 40px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  category-link:
    typography: "{typography.nav-link}"
    color: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  breadcrumb-link:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-current:
    typography: "{typography.caption}"
    color: "{colors.ink}"
    fontWeight: 600

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart," "Shop Now," and "Subscribe." Uses the brand's coral-red (`{colors.primary}`) background with white text. On hover, darkens to `{colors.primary-active}`. Disabled state uses a pale pink (`{colors.primary-disabled}`) with white text. Height is 44px with 12px/24px padding and a subtle 4px corner radius (`{rounded.sm}`).

**`button-secondary`** — Used for secondary actions like "View Details" or "Learn More." White background with ink text and a 1px hairline border. On hover, the border darkens to `{colors.hairline}`. Same height and padding as primary for alignment in form groups.

**`button-tertiary-text`** — A text-only button for less prominent actions like "Cancel" or "Clear Filters." Transparent background with coral-red text. On hover, text darkens to `{colors.primary-active}`. No border or padding beyond the text itself.

### Cards
**`product-card`** — The core product display unit. A white card with 12px padding and an 8px corner radius (`{rounded.md}`). Contains a product image (with 4px corner radius), title in `{typography.title-sm}`, price in bold `{typography.body-md}`, and a star rating row using `{colors.star-gold}`. Age, sale, and stock badges appear in the top-left corner of the image area.

**`age-badge`** — A small, uppercase badge indicating recommended age range (e.g., "AGES 3+"). Light gray background (`{colors.badge-bg}`) with dark text. 2px/8px padding, 2px corner radius (`{rounded.xs}`).

**`sale-badge`** — A red badge for sale or clearance items. Uses `{colors.sale-red}` background with white text. Same sizing as age-badge.

**`stock-badge`** — A green badge for "In Stock" indicators. Uses `{colors.stock-green}` background with white text. Same sizing as age-badge.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar, 64px tall, white background with a subtle bottom border. Contains the brand logo on the left, category links in the center, and utility icons (search, account, cart) on the right. Category links use `{typography.nav-link}` with 8px/16px padding.

**`nav-dropdown`** — The dropdown panel that appears on hover over category links. White background with 8px vertical padding. Links use `{typography.body-sm}` in body color. Has a subtle 8px corner radius (`{rounded.sm}`) and a small drop shadow.

### Forms
**`text-input`** — Standard text input for search, newsletter signup, and form fields. White background, 44px height, 10px/14px padding, 4px corner radius, and a 1px hairline border. On focus, the border becomes a 2px coral-red line (`{colors.primary}`).

**`search-bar`** — The site search input, slightly smaller at 40px height with a light gray background (`{colors.surface-soft}`). Same focus behavior as text-input. The magnifying-glass icon sits inside the input on the left.

**`newsletter-input`** — The email input in the footer. White background, 40px height, same styling as text-input. Sits next to the `newsletter-submit` button.

**`newsletter-submit`** — The submit button for the newsletter form. Coral-red background with white text, 40px height, 10px/20px padding, 4px corner radius.

### Footer
**`footer`** — A dark footer section using `{colors.ink}` background with white text. Contains columns for links (About Us, Customer Service, Rewards, Blog, etc.), a newsletter signup row, and social media icons. Footer links use `{typography.footer-link}` at 13px. Column headings use `{typography.title-sm}` in white with 16px bottom margin.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; footer stacks vertically; search bar moves to a full-width row below the logo; age/sale badges become smaller |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories only (dropdowns hidden); footer shows 2 columns; search bar remains in nav but shrinks |
| Desktop | 1128–1440px | Four-column product grid; full nav with dropdowns; footer shows 4 columns; search bar in nav with full width |
| Wide | > 1440px | Four-column product grid with max-width container (1440px); nav centered; footer centered with max-width |

### Touch Targets
- All buttons and interactive elements minimum 44px height
- Nav links have 44px minimum touch area (padding + height)
- Product card tap targets (title, image, button) are separate and at least 48px tall
- Search bar and newsletter input have 40px minimum height
- Age/sale badges have 24px minimum height

### Collapsing Strategy
- **Navigation**: On mobile (< 744px), the full nav bar collapses to a hamburger menu icon. Tapping opens a full-screen overlay with all categories and utility links stacked vertically.
- **Product Grid**: Collapses from 4 columns (desktop) to 2 columns (tablet) to 1 column (mobile).
- **Footer**: Collapses from 4 columns (desktop) to 2 columns (tablet) to a single vertical stack (mobile).
- **Search Bar**: On mobile, the search bar moves from the nav to a dedicated full-width row below the logo and above the hamburger menu.
- **Breadcrumbs**: On mobile, breadcrumbs collapse to show only the current page and a "Back" link.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations could be extracted from the live site; the typography block uses a common educational-brand stack (Open Sans / Segoe UI) as a reasonable default — this should be verified against the actual site CSS.
- No extracted hex colors were available; the palette above is inferred from common educational-toy brand conventions and the brand's category — this is a best-guess reconstruction and should be replaced with actual extracted values.
- Hover and focus states for secondary elements (nav links, footer links, breadcrumbs) could not be reliably determined.
- Error states for form inputs (validation, error messages) are not defined.
- The star rating component's exact visual treatment (filled vs. half-filled vs. empty stars) is unknown.
- The brand's sub-brand or seasonal color variations (holiday themes, special collections) are not captured.
- Dark mode is not supported and no dark-mode tokens are defined.
- The exact spacing between product card elements (image-to-title, title-to-price) is estimated.
- The newsletter signup success/error states are unknown.
- The cart icon and account icon visual details (badge counts, dropdowns) are not specified.
