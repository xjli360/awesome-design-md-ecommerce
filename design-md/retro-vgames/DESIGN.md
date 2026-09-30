---
version: alpha
name: "Retro vGames"
source_url: "https://retrovgames.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, dark canvas of #111111 forms the backdrop for a retro gaming marketplace where #dc9814 — a warm, oxidized-gold accent — fires across every primary CTA, price badge, and "Add to Cart" button. The site reads like a well-lit game shop after hours: the ink-black background (#111111) pushes product photography forward while #eeeeee body text on #222222 surface cards keeps readability high without breaking the mood. Navigation runs a clean monochrome hierarchy — #555555 muted links against the dark canvas, #2074c1 as the sole blue anchor for account and cart icons. Product cards sit on #222222 surfaces with {rounded.sm} corners, each carrying a gold price badge (#dc9814) that acts as the brand's single color voltage. The typography stack defaults to system fonts (InterVariable, -apple-system, Arial) — no custom typeface, which keeps page weight low and load times fast for a catalog-heavy store. Search bars and filter dropdowns use {rounded.xs} on #2b2b2b fields with #737373 placeholder text, while the footer collapses into a dense #111111 column stack with #6b7280 legal links. The overall effect is a utilitarian, collector-focused interface — the gold (#dc9814) is the only warmth, and it's deployed sparingly enough that every instance feels like a find.

colors:
  primary: "#dc9814"
  primary-active: "#c48510"
  primary-disabled: "#7a5a0a"
  ink: "#111111"
  body: "#eeeeee"
  muted: "#737373"
  muted-soft: "#6b7280"
  hairline: "#2b2b2b"
  hairline-soft: "#353c4e"
  canvas: "#111111"
  surface-soft: "#222222"
  surface-card: "#222222"
  on-primary: "#111111"
  accent-blue: "#2074c1"
  accent-red: "#df0202"
  accent-teal: "#03b5d2"
  star-rating: "#dc9814"
  badge-bg: "#dc9814"
  badge-text: "#111111"

typography:
  display-xl:
    fontFamily: "InterVariable, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "InterVariable, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.25px
  title-md:
    fontFamily: "InterVariable, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "InterVariable, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "InterVariable, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "InterVariable, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "InterVariable, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "InterVariable, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "InterVariable, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.25px
  link:
    fontFamily: "InterVariable, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "InterVariable, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "InterVariable, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "InterVariable, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: 0

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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    typography: "{typography.button-sm}"
  button-icon:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.primary}"
    rounded: "{rounded.xs}"
  text-input-placeholder:
    textColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  product-card-hover:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.body}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-rating:
    textColor: "{colors.star-rating}"
    typography: "{typography.caption}"
  filter-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
  filter-dropdown-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    rounded: "{rounded.xs}"
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    height: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  footer-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: 32px 16px
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.body}"
  cart-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    padding: 2px 6px
  icon-circle:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 36px
  icon-circle-hover:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The gold anchor of the interface. Uses `{colors.primary}` (#dc9814) background with `{colors.on-primary}` (#111111) text for high contrast. On hover, shifts to `{colors.primary-active}` (#c48510). Disabled state drops to `{colors.primary-disabled}` (#7a5a0a) with reduced opacity. Used for "Add to Cart", "Checkout", and primary form submissions.

**`button-secondary`** — Dark surface button for secondary actions like "View Details" or "Save for Later". Background is `{colors.surface-card}` (#222222) with `{colors.body}` (#eeeeee) text. Active state fills to `{colors.hairline}` (#2b2b2b). Used alongside primary buttons in product cards and modals.

**`button-tertiary-text`** — Text-only link-style button for "Cancel", "Clear Filters", or "Learn More". Uses `{colors.accent-blue}` (#2074c1) to distinguish from standard body links. No background or border.

**`button-icon`** — Circular icon button for cart, account, and search icons in the nav bar. Transparent background with `{colors.muted}` (#737373) icon color. On hover, icon shifts to `{colors.body}` (#eeeeee).

### Cards
**`product-card`** — The primary content container for game listings. Dark surface (`{colors.surface-card}` #222222) with `{rounded.sm}` corners and `{spacing.md}` padding. On hover, background shifts to `{colors.hairline}` (#2b2b2b) for a subtle lift effect. Contains a product image (full-width, `{rounded.xs}`), title (`{typography.product-card-title}`), price (`{typography.product-card-price}` in gold), and optional rating stars (`{colors.star-rating}`).

**`product-card-badge`** — Small gold pill for "New", "Sale", or "Rare" tags. Uses `{colors.badge-bg}` (#dc9814) with `{colors.badge-text}` (#111111) and `{typography.badge}` (uppercase, 12px, bold). Positioned top-left on product images.

### Navigation
**`nav-bar`** — Fixed top navigation at 64px height on `{colors.canvas}` (#111111). Logo sits left, nav links center, icon buttons right. Links use `{typography.nav-link}` (15px, weight 500) in `{colors.muted}` (#737373). Active page link shifts to `{colors.body}` (#eeeeee). Hover state shifts to `{colors.primary}` (#dc9814). Cart icon carries a `{components.cart-badge}` with `{colors.accent-red}` (#df0202) for item count.

**`search-bar`** — Prominent search input on `{colors.surface-card}` (#222222) with `{rounded.sm}` corners. On focus, border shifts to `{colors.primary}` (#dc9814). Placeholder text in `{colors.muted}` (#737373). Includes a search icon button at the right edge.

### Forms
**`text-input`** — Standard form input for checkout fields, account forms, and filter text entries. Dark surface (`{colors.surface-card}` #222222) with `{rounded.xs}` corners. Focus state adds a `{colors.primary}` (#dc9814) border. Placeholder text in `{colors.muted}` (#737373).

**`filter-dropdown`** — Dropdown select for sorting and filtering game catalogs (by platform, genre, price range). Dark surface with `{rounded.xs}` corners. Active state highlights the selected option with `{colors.primary}` (#dc9814) border and text color.

### Footer
**`footer-section`** — Dense footer on `{colors.canvas}` (#111111) with `{colors.muted}` (#737373) text. Links use `{colors.muted-soft}` (#6b7280) and shift to `{colors.body}` (#eeeeee) on hover. Organized in a multi-column layout on desktop, collapsing to a single column on mobile. Includes legal text, social links, and a copyright notice.

### Pagination
**`pagination-button`** — Numbered page buttons at the bottom of catalog listings. Dark surface (`{colors.surface-card}` #222222) with `{colors.muted}` (#737373) text. Active page uses `{colors.primary}` (#dc9814) background with `{colors.on-primary}` (#111111) text. Previous/Next arrows use the same styling.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card), nav collapses to hamburger menu, search bar moves below nav, footer stacks vertically, filter dropdowns become full-width |
| Tablet | 744–1128px | Two-column product grid (2 cards), nav links visible (5 max), search bar inline with nav, filter dropdowns in a horizontal row |
| Desktop | 1128–1440px | Three-column product grid (3 cards), full nav with all links, search bar centered, filter sidebar on left |
| Wide | > 1440px | Four-column product grid (4 cards), max-width container at 1440px, centered layout with generous side margins |

### Touch Targets
- All buttons and interactive elements maintain minimum 44x44px touch target
- Icon buttons in nav bar are 40x40px with 36px icon area
- Product card tap targets (title, price, add-to-cart) are at least 44px tall
- Filter dropdowns and search bar are 44px tall
- Pagination buttons are 36x36px with 8px gap between

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px; hamburger icon is 44x44px
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Filter sidebar on desktop becomes a horizontal filter strip on tablet, then a collapsible accordion on mobile
- Footer multi-column layout collapses to single column below 744px
- Search bar moves from inline nav position (desktop/tablet) to below the nav (mobile)
- Breadcrumbs hide on mobile; replaced by a "Back" button

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components were inferred from the extracted color palette; actual hover/focus colors may differ on the live site
- Error state styling for form inputs (red borders, error messages) could not be reliably extracted; `{colors.accent-red}` (#df0202) is a candidate but not confirmed
- Dark mode is not applicable since the entire site is already dark-themed (#111111 canvas)
- Sub-brand or category-specific color variations (e.g., "Nintendo" vs "PlayStation" sections) were not observed
- Custom font weights beyond the standard InterVariable range (400, 500, 600, 700) may exist but were not detected
- Animation durations, easing curves, and transition properties were not extracted
- Modal and overlay component styles (e.g., cart drawer, quick view) were not captured
- The extracted color list includes many grays (#d3d4d5, #e2e2e2, #f4f4f4, etc.) that likely belong to third-party widgets (Shopify checkout, payment badges) rather than the brand itself; the true brand palette is dominated by #111111, #222222, #dc9814, and #eeeeee
- No custom font was detected; the site relies entirely on system fonts (InterVariable, -apple-system, Arial) — this may be intentional for performance or a gap in extraction
- Checkout flow components (payment forms, address fields, order summary) were not analyzed
- Accessibility contrast ratios between `{colors.body}` (#eeeeee) on `{colors.canvas}` (#111111) pass WCAG AA, but gold text (#dc9814) on dark surfaces (#222222) may need verification
