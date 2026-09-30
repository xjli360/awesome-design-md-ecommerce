---
version: alpha
name: "MonsGeek"
source_url: "https://www.monsgeek.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A mechanical-keyboard brand that builds its visual identity around a deep, confident blue (#006799) — not the playful pastels or industrial grays typical of the hobby, but a saturated primary that reads as both premium and approachable. The brand tagline "Make Cool Gears Accessible" is reflected in a design system that balances enthusiast-grade detail with clean, uncluttered interfaces. Type runs on Poppins across three weights (Regular, Medium, Bold), with display sizes that lean into the geometric, slightly technical feel of the font — uppercase badges and tight letter-spacing on buttons echo the precision of keyboard switches. The palette extends into a controlled range of greens (#1e3828, #0f1f18) and accent tones (#82c0c7, #9de1bc) that suggest PCB colors and keycap gradients without overwhelming the primary blue. Cards and containers use soft rounding ({rounded.sm} to {rounded.md}), while CTAs and badges adopt pill shapes ({rounded.full}) that contrast with the otherwise rectilinear product photography. The system relies on a warm off-white canvas (#eeeeee) rather than pure white, giving the storefront a slightly softer, more editorial feel than the stark black-and-white of many tech brands. Navigation stays minimal — a single top bar with dropdowns, no mega-menus — letting the product grid do the heavy lifting. The extracted palette includes a wide range of generic web colors (multiple grays, blues, and bright accents like #f78da7 and #ff6900), suggesting either a WordPress-based backend or third-party widget integrations; the true brand voice lives in the consistent use of #006799 across primary actions, headers, and key links.

colors:
  primary: "#006799"
  primary-active: "#005580"
  primary-disabled: "#b3d4e6"
  ink: "#111111"
  body: "#32373c"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#e5e7eb"
  hairline-soft: "#ededed"
  canvas: "#eeeeee"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#1e3828"
  accent-green-light: "#0f1f18"
  accent-teal: "#82c0c7"
  accent-mint: "#9de1bc"
  badge-red: "#cf2e2e"
  badge-orange: "#ff6900"
  badge-yellow: "#fcb900"
  badge-green: "#7bdcb5"
  badge-blue: "#8ed1fc"
  badge-purple: "#9b51e0"

typography:
  display-xl:
    fontFamily: "'Poppins-Bold', 'Poppins', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins-Bold', 'Poppins', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Poppins-Medium', 'Poppins', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins-Medium', 'Poppins', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins-Medium', 'Poppins', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins-Regular', 'Poppins', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins-Regular', 'Poppins', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins-Regular', 'Poppins', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Poppins-Medium', 'Poppins', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Poppins-Medium', 'Poppins', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Poppins-Medium', 'Poppins', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  link:
    fontFamily: "'Poppins-Regular', 'Poppins', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins-Bold', 'Poppins', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  price:
    fontFamily: "'Poppins-Medium', 'Poppins', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
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
  button-primary-hover:
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
    padding: 12px 24px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-hover:
    boxShadow: 0 4px 12px rgba(0,0,0,0.08)
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.price}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-new:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: 1px solid "{colors.hairline}"
  search-bar-focus:
    border: 2px solid "{colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.on-primary}"
  section-header:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
    padding: "{spacing.xl} 0 {spacing.lg}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    height: 32px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand blue (#006799) with white uppercase Poppins Medium text. Hover state darkens to `{colors.primary-active}` (#005580). Disabled state fades to a pale blue `{colors.primary-disabled}` (#b3d4e6). Used for "Add to Cart", "Buy Now", and primary form submissions.

**`button-secondary`** — An outlined or ghost-style button on the warm off-white canvas (`{colors.canvas}` #eeeeee). Hover adds a soft background fill (`{colors.hairline-soft}` #ededed). Used for "Learn More", "View Details", and secondary actions.

**`button-ghost`** — Text-only button with the brand blue as the text color, no background or border. Used for inline actions like "Clear Filters" or "Cancel".

**`button-pill`** — A compact, fully rounded button (`{rounded.full}`) with smaller uppercase text. Used for quick-add actions on product cards, filter resets, or promotional badges.

### Cards
**`product-card`** — The core product display unit. A white card (`{colors.surface-card}`) with soft 12px rounding (`{rounded.md}`). The product image sits at the top with rounded top corners only, creating a subtle separation from the text below. The title uses `{typography.title-sm}` (16px Poppins Medium) and the price uses `{typography.price}` (18px Poppins Medium). Hover state adds a light box shadow for depth.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar at 64px height on the warm canvas background. Links use `{typography.nav-link}` (14px Poppins Medium with 0.3px letter-spacing). Dropdown menus appear as white cards with soft 8px rounding and tight padding.

**`nav-dropdown`** — A white card panel that appears on hover or click of nav items. Contains product category links in `{typography.body-sm}`.

### Forms
**`text-input`** — Standard text input fields with a white background, 1px hairline border (`{colors.hairline}` #e5e7eb), and 8px rounding. On focus, the border thickens to 2px and switches to the brand blue. Used for search, email signup, and checkout forms.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a white background and hairline border. On focus, the border becomes 2px brand blue. Used in the header for product search.

### Badges
**`badge`** — Small uppercase labels in Poppins Bold at 11px with 0.8px letter-spacing. The default badge uses the brand blue background. Variants include `badge-sale` (red #cf2e2e for discounts) and `badge-new` (green #7bdcb5 for new arrivals). All badges use 4px rounding (`{rounded.xs}`) and tight 2px/8px padding.

### Filters
**`filter-chip`** — Pill-shaped filter toggles (`{rounded.full}`) at 32px height with soft background (`{colors.surface-soft}`). Active state fills with the brand blue and white text. Used in product listing pages for category, switch type, and layout filters.

### Hero
**`hero-banner`** — Full-width promotional banner with the brand blue background and white text. Uses `{typography.display-xl}` (36px Poppins Bold) for the headline and `{typography.body-md}` for the subtitle. Padding is generous at 64px vertical.

### Footer
**`footer`** — A dark footer section with near-black background (`{colors.ink}` #111111) and muted gray text (`{colors.muted-soft}` #9ca3af). Links use `{typography.link}` (14px Poppins Regular). Vertical padding is 48px, with 64px horizontal padding on desktop.

### Pagination
**`pagination-button`** — Square-ish buttons (8px rounding) for page navigation. Active page uses the brand blue fill; inactive pages use the warm canvas background. Each button is 36px tall with 8px/12px padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 columns). Nav collapses to hamburger menu. Hero banner reduces padding to 32px. Filter chips stack vertically. Search bar moves to a dedicated overlay. Footer links stack in single column. |
| Tablet | 744–1128px | Two-column product grid. Nav remains visible with condensed links. Filter chips wrap in a horizontal strip. Hero banner uses 48px padding. Footer uses 2-3 column layout. |
| Desktop | 1128–1440px | Three-column product grid. Full nav with dropdowns. Filter chips in horizontal row. Hero banner at full padding (64px). Footer in 4-column layout. |
| Wide | > 1440px | Four-column product grid. Max-width container (1440px) for content. Hero banner may use a wider background with constrained text. Footer remains 4-column with max-width. |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility.
- Filter chips are 32px height — acceptable for touch but could be increased to 36px on mobile.
- Nav dropdowns have 8px padding around links to ensure 44px tap targets.
- Search bar is 44px height on all breakpoints.

### Collapsing Strategy
- Primary navigation collapses to a hamburger icon below 744px.
- Product grid reduces from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Filter chips stack vertically on mobile; horizontal scroll on tablet.
- Footer links collapse from 4 columns to 2 columns on tablet, single column on mobile.
- Hero banner text reduces in size on mobile (from 36px to 24px).
- Search bar becomes a full-screen overlay on mobile with larger input field.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors include many generic web palette colors (multiple grays, blues, and bright accent colors like #f78da7, #ff6900, #fcb900, #7bdcb5, #8ed1fc, #0693e3, #9b51e0, #974df3, #7e3bd0) that likely come from WordPress theme defaults, WooCommerce widgets, or third-party integrations rather than the brand's intentional palette. The true brand primary (#006799) and secondary greens (#1e3828, #0f1f18, #82c0c7, #9de1bc) were identified by frequency and contextual usage.
- Font-family declarations include "Open Sans" and "DM Sans" alongside Poppins — these may be fallback fonts or used in specific widget areas. Poppins was chosen as the primary brand font based on the three weight-specific declarations (Poppins-Bold, Poppins-Medium, Poppins-Regular).
- Hover states for buttons and cards are inferred from common e-commerce patterns, not extracted from live CSS.
- Error and validation styling (form errors, out-of-stock states) not available from extraction.
- Dark mode or high-contrast mode not detected.
- Animation durations, easing curves, and transition properties not extracted.
- Box shadows and elevation levels not reliably extracted from the live site.
- Iconography style and sizing not determined — the site may use custom SVG icons or a library.
- Product card image aspect ratios and dimensions not confirmed.
- Checkout flow styling (cart, shipping, payment) not captured — may use a third-party checkout.
