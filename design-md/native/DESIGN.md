---
version: alpha
name: "Native"
source_url: "https://www.nativecos.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Native is a clean, honest body-care brand that uses color as a signal of purity and efficacy rather than decoration. The palette is anchored by a deep navy {colors.primary} (#0a1f8f) that reads as trustworthy and clinical, paired with a crisp white canvas (#f7f7f7) and soft off-whites (#f5f5f5, #fafafa) that keep the experience airy and approachable. Accents of red (#e63235, #e40e47) and orange (#b2441e) appear sparingly on badges, sale markers, and secondary actions, injecting just enough energy to draw the eye without overwhelming the calm baseline. The typography system relies on a single clean sans-serif stack (inheriting from system fonts) with modest weights — display sizes hover around 24–28px at weight 600, body text at 14–16px at weight 400, and buttons at 14px weight 500 — letting the product photography and generous whitespace do the heavy lifting. Rounded corners are minimal: small buttons use {rounded.sm} (8px), cards and inputs use {rounded.md} (12px), and only the search bar and hero badges reach {rounded.full} (9999px), preserving a friendly but not overly playful feel. The brand's signature move is the navy-on-white hero section with a single bold headline, a pill-shaped search or CTA button, and a clean product grid below — no clutter, no noise, just clean. Simple. Effective.

colors:
  primary: "#0a1f8f"
  primary-active: "#293273"
  primary-disabled: "#8ca5de"
  ink: "#121212"
  body: "#2e3133"
  muted: "#707070"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#eaeaea"
  canvas: "#f7f7f7"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#e63235"
  accent-red-dark: "#d02f2e"
  accent-orange: "#b2441e"
  accent-green: "#4d9c4c"
  accent-green-dark: "#478947"
  accent-purple: "#7f5fca"
  badge-new: "#e40e47"
  star-rating: "#121212"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px

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
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
  text-input-error:
    borderColor: "{colors.accent-red}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  product-card-badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 14px 24px
    height: 56px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  badge-pill:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-red}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 11px
  badge-pill-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-pill-purple:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  star-rating:
    textColor: "{colors.star-rating}"
    typography: "{typography.caption}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 40px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Subscribe", and "Shop Now" actions. Rendered as a solid navy rectangle with white text, 8px rounded corners, and 12px vertical padding. On hover, it shifts to `{colors.primary-active}` (#293273). The disabled state uses `{colors.primary-disabled}` (#8ca5de) with reduced opacity. **`button-secondary`** — An outlined variant with a white fill and navy text, used for secondary actions like "Learn More" or "View Details". On hover, the background shifts to `{colors.surface-soft}` (#f5f5f5). **`button-tertiary`** — A text-only button with no background or border, used for less prominent actions like "Cancel" or "Skip". **`button-pill`** — A fully rounded pill-shaped button used in hero sections and promotional banners. Same navy fill as primary but with 9999px border-radius and slightly taller height (48px). **`button-pill-outline`** — The outlined counterpart to the pill button, used for "Get Started" or "Explore" CTAs on dark backgrounds.

### Cards
**`product-card`** — The standard product display card with a white background, 12px rounded corners, and a 4:5 aspect ratio image area. The card contains an image (rounded top corners), a product title in `{typography.title-sm}`, a price in `{typography.body-sm}` with `{colors.muted}`, and optional badges. Badges appear in the top-left corner and come in three variants: red for "Best Seller" (`{colors.accent-red}`), pink-red for "New" (`{colors.badge-new}`), and orange for "Sale" (`{colors.accent-orange}`). Cards have no border but use subtle shadow on hover.

### Navigation
**`nav-bar`** — A fixed top navigation bar with a white background, 64px height on desktop, collapsing to 56px on scroll. Contains the brand logo on the left, nav links in the center, and utility icons (search, account, cart) on the right. Active nav links use `{colors.primary}` text, inactive links use `{colors.muted}`. The nav bar gains a bottom border (`{colors.hairline}`) on scroll. **`nav-link-active`** and **`nav-link-inactive`** define the two states for navigation items.

### Forms
**`text-input`** — Standard text input fields with a white background, 8px rounded corners, 48px height, and 16px horizontal padding. The focus state adds a 2px `{colors.primary}` border. Error state uses a 2px `{colors.accent-red}` border. Used for email signup, search queries, and checkout forms. **`quantity-selector`** — A compact horizontal control with minus/plus buttons flanking a numeric display, used on product detail pages. Background is `{colors.surface-soft}` (#f5f5f5) with 8px rounded corners.

### Footer
**`footer`** — A dark footer section with `{colors.ink}` (#121212) background and `{colors.muted-soft}` (#999999) text. Contains columns of links with `{colors.canvas}` headings, social media icons, and legal text. Links use `{colors.muted-soft}` and lighten on hover. The footer has 48px vertical padding on all sides.

### Badges
**`badge-pill`** — Small pill-shaped badges used for product attributes like "Best Seller", "New", or "Limited Edition". Available in red (`{colors.accent-red}`), green (`{colors.accent-green}`), and purple (`{colors.accent-purple}`) variants. Text is uppercase, 11px, weight 600, with 4px vertical and 12px horizontal padding. **`badge-pill-outline`** — An outlined version with a white background and red text, used on product cards with busy backgrounds.

### Accordion
**`accordion`** — Collapsible content sections used on product detail pages for ingredients, usage instructions, and reviews. The header uses `{colors.surface-soft}` (#f5f5f5) with `{colors.ink}` text, and the content panel uses a white background with `{colors.body}` text. Both sections have 16px vertical and 24px horizontal padding.

### Hero
**`hero-section`** — Full-width hero banners with a navy (`{colors.primary}`) background and white text. Contains a headline in `{typography.display-xl}`, optional subtitle, and a pill-shaped search or CTA button (`{hero-search}`). The hero has 64px vertical padding and 16px horizontal padding. Used on the homepage and category landing pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 col), nav collapses to hamburger menu, hero text reduces to 22px, buttons become full-width, footer stacks vertically, search bar moves to mobile drawer |
| Tablet | 744–1128px | Two-column product grid (2 col), nav links remain visible but condensed, hero maintains 28px headline, buttons remain inline, footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grid (3 col), full nav bar with all links, hero at full size, buttons inline, footer uses 4-column layout |
| Wide | > 1440px | Four-column product grid (4 col) on category pages, max-width container (1440px) centered, hero remains full-width with max-width content |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons (search, cart, account) are 44x44px on mobile, 40x40px on desktop
- Quantity selector buttons are 40x40px minimum
- Accordion headers are 48px tall for easy tapping
- Nav bar links have 48px touch targets on mobile

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger menu with a slide-out drawer
- Product grids collapse from 3–4 columns to 1 column on mobile
- Footer sections collapse into accordion-style expandable groups on mobile
- Hero sections reduce vertical padding from 64px to 32px on mobile
- Multi-step checkout collapses to a single-page scroll form on mobile
- Search bar moves from the nav bar to a full-screen overlay on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons could not be fully extracted from the live site
- Error styling for form validation (border colors, error message typography) is inferred from common patterns
- Dark mode color overrides are not present in the extracted data
- Sub-brand or seasonal palette variations (e.g., holiday collections) are not captured
- Focus ring styles (outline, offset, color) are not reliably extracted
- Loading states (spinners, skeleton screens) are not defined
- Animation and transition timing values (duration, easing) are missing
- Dropdown and select menu styling is not captured
- Modal and overlay component specifications are absent
- Tooltip and popover styling is not defined
- The exact font family used could not be determined (extracted as "inherit"); a standard system font stack is assumed
- Specific border widths (other than inferred 1px and 2px) are not reliably extracted
- Shadow/elevation values (box-shadow) are not present in the extracted data
- Checkbox and radio button styling is not captured
- Toggle switch component specifications are missing
- Progress bar and stepper component styling is not defined
- Table styling (headers, rows, zebra striping) is not captured
- Pagination component specifications are absent
- Breadcrumb navigation styling is not defined
- Rating display (star icons) sizing and spacing is inferred
- Social media icon colors and hover states are not captured
- Newsletter signup form error and success states are not defined
- Cart drawer and mini-cart styling is not captured
- Mobile bottom navigation bar specifications are missing
- Pull-to-refresh and swipe gesture styling is not defined
- Print stylesheet overrides are not captured
- Accessibility-focused high-contrast mode overrides are not present
- RTL (right-to-left) language support is not defined
- Custom scrollbar styling is not captured
- Video player and media gallery component styling is not defined
- Countdown timer and promotional banner styling is not captured
- Loyalty program and rewards badge styling is not defined
- Gift card and promotional code input styling is not captured
- Multi-step form progress indicator styling is not defined
- File upload component styling is not captured
- Date picker and calendar component styling is not defined
- Color swatch and product variant selector styling is not captured
- Size chart modal and tooltip styling is not defined
- Customer review and rating component styling is not captured
- FAQ accordion and search styling is not defined
- Store locator and map component styling is not captured
- Subscription management and recurring order styling is not defined
- Back-in-stock notification form styling is not captured
- Wishlist and saved items component styling is not defined
- Gift wrapping and personalization options styling is not captured
- Shipping calculator and estimated delivery styling is not defined
- Payment method and card input styling is not captured
- Order confirmation and thank-you page styling is not defined
- Account dashboard and order history styling is not captured
- Mobile app-specific styling (if applicable) is not defined
