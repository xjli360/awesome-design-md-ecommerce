---
version: alpha
name: "Troll and Toad"
source_url: "https://www.trollandtoad.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep purple #664283 anchors the brand — not as a background flood but as a deliberate accent voltage on category headers, sale badges, and the top nav bar, signaling authority in the trading-card marketplace without overwhelming the product photography. The canvas is a cool off-white #f3f3f3, giving the site a slightly aged, collector-friendly feel rather than sterile white. Orange #f68b1f acts as the primary CTA color — a high-contrast, urgent accent used on "Add to Cart" buttons and price-drop alerts, while gold #b28500 appears on rare-find badges and premium-tier indicators. The type system runs Poppins at modest weights (400–600), with display headlines at 24px weight 600 and body copy at 14px weight 400, creating a clean, readable hierarchy that steps back to let card images and set symbols do the talking. Product cards use a soft `{rounded.sm}` corner and a subtle `{colors.hairline}` border, while the search bar is a full-width `{rounded.full}` pill on `{colors.canvas}`. The overall mood is that of a well-organized binder — structured, categorized by set and rarity, with enough visual energy from the purple/orange/gold triad to keep browsing feel like a hunt.

colors:
  primary: "#664283"
  primary-active: "#4f3266"
  primary-disabled: "#b8a3c9"
  ink: "#121212"
  body: "#242833"
  muted: "#555555"
  muted-soft: "#929292"
  hairline: "#dedede"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#f68b1f"
  accent-orange-active: "#d9770e"
  accent-gold: "#b28500"
  accent-gold-soft: "#f7ebc8"
  error: "#c82333"
  error-soft: "#fce4e4"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  price:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price-sm:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
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
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.muted-soft}"
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
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-ghost-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  text-input-error:
    border: "1px solid {colors.error}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: "0 {spacing.lg}"
  nav-bar-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar-link-active:
    textColor: "{colors.on-primary}"
    backgroundColor: "rgba(255, 255, 255, 0.15)"
    rounded: "{rounded.xs}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-rarity:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  category-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "2px solid {colors.primary}"
  filter-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  filter-checkbox:
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 18px
  filter-checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
    padding: "0 {spacing.xs}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  badge-new:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-rarity:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    height: 36px
  add-to-cart-button:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  add-to-cart-button-active:
    backgroundColor: "{colors.accent-orange-active}"
  add-to-cart-button-disabled:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
  wishlist-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
    border: "1px solid {colors.hairline}"
  wishlist-button-active:
    backgroundColor: "{colors.error-soft}"
    textColor: "{colors.error}"
    border: "1px solid {colors.error}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in `{colors.accent-orange}` with white text. Used for "Add to Cart", "Buy Now", and primary checkout flows. On hover, shifts to `{colors.accent-orange-active}`. Disabled state uses `{colors.muted-soft}`. **`button-secondary`** — A white button with a `{colors.hairline}` border and `{colors.ink}` text, used for secondary actions like "View Details" or "Cancel". Active state fills `{colors.surface-soft}`. **`button-ghost`** — A text-only button in `{colors.primary}` with no background, used for inline actions like "Clear Filters" or "See More". Active state gains a subtle `{colors.hairline-soft}` background. **`button-pill`** — A fully rounded pill in `{colors.primary}` with white text, used for filter tags, category chips, and quick-select actions.

### Cards
**`product-card`** — The core product display unit, a white card on `{colors.surface-card}` with a `{rounded.sm}` corner and a faint `{colors.hairline-soft}` border. On hover, the border darkens to `{colors.hairline}` and a subtle shadow lifts the card. Contains a product image, title, set name, and price. **`product-card-badge`** — A small gold `{colors.accent-gold}` badge for rare or high-value items. **`product-card-badge-sale`** — An orange `{colors.accent-orange}` badge for sale items. **`product-card-badge-rarity`** — A purple `{colors.primary}` badge for rarity indicators (e.g., "Holo", "First Edition").

### Navigation
**`nav-bar`** — A fixed-height 56px bar in `{colors.primary}` with white text. Contains the brand logo, category links, and a search icon. Links use `{typography.nav-link}` and gain a semi-transparent white background on active state. **`nav-bar-link`** — Inline navigation links with `{spacing.sm}` vertical and `{spacing.md}` horizontal padding. Active state uses a 15% white overlay with `{rounded.xs}`.

### Forms
**`text-input`** — A standard input field with a `{colors.hairline}` border, `{rounded.sm}` corners, and 44px height. On focus, the border thickens to 2px and turns `{colors.primary}`. Error state uses `{colors.error}` border. **`quantity-selector`** — A bordered container with a decrement button, a numeric display, and an increment button. Buttons use `{colors.surface-soft}` background and `{rounded.xs}`.

### Search
**`search-bar`** — A full-width pill-shaped input (`{rounded.full}`) on white background with a `{colors.hairline}` border. On focus, the border becomes 2px `{colors.primary}`. Used on the homepage and category pages for set, card, or product lookup.

### Badges
**`badge-new`** — A gold `{colors.accent-gold}` pill badge for new arrivals. **`badge-sale`** — An orange `{colors.accent-orange}` pill badge for sale items. **`badge-rarity`** — A purple `{colors.primary}` pill badge for rarity indicators. All use `{rounded.full}` and `{typography.badge}`.

### Footer
**`footer`** — A dark `{colors.ink}` footer with white text. Links are `{colors.muted-soft}` and turn white on hover. Contains site map, support links, and legal text.

### Pagination
**`pagination`** — A row of page numbers with `{typography.body-sm}` in `{colors.muted}`. The active page uses a `{colors.primary}` background with white text and `{rounded.xs}`. Hover state uses `{colors.surface-soft}`.

### Hero
**`hero-banner`** — A full-width section with `{colors.surface-soft}` background, `{typography.display-lg}` headline, and a prominent `{colors.accent-orange}` CTA button. Used for featured sets, pre-orders, and seasonal promotions.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav-bar collapses to hamburger menu. Product cards stack single-column. Search bar reduces to icon-only. Footer links stack vertically. Hero banner reduces padding to `{spacing.xl}`. |
| Tablet | 744–1128px | Nav-bar shows top-level categories with dropdown. Product cards display in 2–3 column grid. Search bar remains full-width but shorter. Footer links in 2 columns. |
| Desktop | 1128–1440px | Full nav-bar with all categories visible. Product cards in 4–5 column grid. Sidebar filters visible on category pages. Hero banner at full `{spacing.section}` padding. |
| Wide | > 1440px | Max-width container at 1440px. Product cards in 5–6 column grid. Additional whitespace on sides. Hero banner may include background imagery. |

### Touch Targets
- All buttons and interactive elements minimum 44px height.
- Nav-bar links have minimum 48px tap target.
- Quantity selector buttons minimum 36px height.
- Filter checkboxes minimum 18px with 44px tap area.
- Pagination items minimum 32px tap target.

### Collapsing Strategy
- Nav-bar collapses to hamburger menu below 744px, with a slide-out drawer.
- Sidebar filters collapse to a "Filters" button that opens a modal or overlay on mobile.
- Product card grid reduces columns: 1 column mobile, 2–3 tablet, 4–5 desktop, 5–6 wide.
- Footer links collapse from multi-column to single-column stack on mobile.
- Hero banner reduces vertical padding and may hide secondary text on mobile.
- Search bar collapses to an icon that expands to full input on tap.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components are inferred from common patterns; exact box-shadow values, transition durations, and easing functions not extracted.
- Error styling for forms (error messages, validation icons) not observed; `{colors.error}` used for borders but full pattern unknown.
- Dark mode not present on the live site; no extracted colors or patterns.
- Sub-brand palettes (e.g., for specific TCGs like Pokémon, Magic: The Gathering, Yu-Gi-Oh!) not extracted; the site may use set-specific colors.
- Typography scale for mobile (smaller font sizes) not extracted; desktop values used as base.
- Spacing values for specific components (e.g., card padding, grid gaps) are estimated from common e-commerce patterns.
- The extracted color list includes several grays (#121212, #dedede, #f3f3f3, #f0f0f0, #efefef, #555555) which are likely structural/background colors; the distinctive purple (#664283), orange (#f68b1f), and gold (#b28500) are treated as brand accents.
- Font weights beyond 400, 500, 600 not observed; Poppins may support 700 but not used in extracted CSS.
- Animation and transition patterns (e.g., card hover lift, modal open/close) not documented.
- Checkout flow styling (Shopify default) may override brand colors; not extracted.
- Accessibility contrast ratios not verified; `{colors.accent-gold}` (#b28500) on white may have contrast issues.
