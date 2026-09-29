---
version: alpha
name: "TP-Link"
source_url: "https://www.tp-link.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A networking brand that signals reliability through a teal-cyan primary (#4acbd6) — a color that reads as cool, technical, and connected, not warm or consumer-friendly. The palette is dominated by deep charcoal (#36444b, #1d2529) and a spectrum of grays (#a7a9ac, #bdbec0, #c8cfd2, #e9eaeb) that create a serious, infrastructure-grade atmosphere. The single accent of amber (#ffcb00) appears sparingly, likely for promotional badges or urgency indicators, while the teal carries primary CTAs and interactive elements. Typography relies on system fonts with AktivGrotesk-Corp as the brand face — a clean, neutral sans-serif that avoids personality in favor of legibility across router configuration pages and product spec sheets. The design language is fundamentally rectangular: sharp corners on product cards, navigation bars, and buttons, with only the occasional pill shape (`{rounded.full}`) for search inputs or filter tags. White canvas (#fefefe) provides breathing room for dense technical content, while hairline borders (#d8d8d8, #e1e1e1) segment information without visual noise. The overall feel is that of a control panel — functional, precise, and engineered for utility rather than delight.

colors:
  primary: "#4acbd6"
  primary-active: "#24bbc7"
  primary-disabled: "#a6a1a1"
  ink: "#1d2529"
  body: "#36444b"
  muted: "#6f7476"
  muted-soft: "#a7a9ac"
  hairline: "#d8d8d8"
  hairline-soft: "#e1e1e1"
  canvas: "#fefefe"
  surface-soft: "#f8f9fb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-amber: "#ffcb00"
  accent-amber-active: "#edbd00"
  accent-amber-disabled: "#ffdb4c"
  badge-new: "#4acbd6"
  badge-sale: "#ffcb00"
  dark-surface: "#212121"
  dark-muted: "#4a4b4b"
  dark-hairline: "#cacaca"
  error: "#c13515"
  success: "#005564"

typography:
  display-xl:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.3px
  link:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  spec-value:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  spec-label:
    fontFamily: "'AktivGrotesk-Corp', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
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
    padding: 10px 24px
    height: 40px
  button-primary-lg:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 23px
    height: 40px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  button-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 24px
    height: 40px
  button-amber-active:
    backgroundColor: "{colors.accent-amber-active}"
    textColor: "{colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.section}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.spec-value}"
    border: "1px solid {colors.hairline-soft}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.spec-label}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table-row:
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  spec-table-row-hover:
    backgroundColor: "{colors.surface-soft}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.base}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
    fontWeight: 600
  breadcrumb-separator:
    textColor: "{colors.hairline}"
    padding: "0 {spacing.xs}"
  filter-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    border: "1px solid {colors.hairline}"
  filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  loading-spinner-lg:
    color: "{colors.primary}"
    size: 40px
  rating-stars:
    color: "{colors.accent-amber}"
    size: 16px
  rating-stars-empty:
    color: "{colors.hairline}"
  toggle-switch:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-switch-active:
    backgroundColor: "{colors.primary}"
  toggle-switch-thumb:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  modal-overlay:
    backgroundColor: "rgba(0,0,0,0.5)"
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: "0 8px 32px rgba(0,0,0,0.12)"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header-hover:
    backgroundColor: "{colors.surface-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
  tab-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline-soft}"
  tab-active:
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    borderBottom: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  tab-inactive:
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    padding: "{spacing.sm} {spacing.base}"
  tab-hover:
    textColor: "{colors.body}"
  notification-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "1px 6px"
    fontSize: 10px
  quick-view-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 36px
    border: "1px solid {colors.hairline}"
  quick-view-button-hover:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.primary}"
    textColor: "{colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with teal-cyan (#4acbd6) and white text. Used for "Buy Now", "Add to Cart", and "Shop Now" actions on product pages. Hover shifts to a darker teal (#24bbc7), while disabled state drops to a muted gray (#a6a1a1). The 4px corner radius (`{rounded.sm}`) is the brand's standard button treatment — never fully pill-shaped except for filter tags. A larger variant (`button-primary-lg`) exists for hero sections and promotional banners, with 48px height and 32px horizontal padding.

**`button-secondary`** — An outlined button with white fill and teal border, used for secondary actions like "Compare" or "Learn More". The 2px stroke maintains visual weight parity with the filled primary. Active state darkens the border to #24bbc7.

**`button-amber`** — An accent button filled with amber (#ffcb00) and dark text (#1d2529), reserved for urgency signals: limited-time offers, flash sales, or price-drop alerts. The amber active state (#edbd00) provides a subtle darkening on hover.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel", "View Details", or dismissible close buttons. Hover adds a subtle background via `{colors.surface-soft}`.

### Navigation
**`nav-bar`** — A fixed-height 64px bar with white background and a soft bottom border (#e1e1e1). Navigation links use 14px medium-weight type with 0.3px letter spacing. The active link is underlined with a 2px teal stroke (#4acbd6). On scroll, the bar gains a subtle box shadow (`0 2px 8px rgba(0,0,0,0.08)`) for visual separation from content.

**`breadcrumb`** — A horizontal trail of 13px gray links separated by hairline-colored slashes. The active (current) page is rendered in dark ink (#1d2529) with 600 weight. Used on product detail and category pages to maintain spatial orientation.

### Cards
**`product-card`** — A rectangular card with no border radius, a 1px soft hairline border (#e1e1e1), and a 1:1 aspect ratio image area. The card is entirely flat — no shadow, no elevation — until hover, when it lifts with a 4px/12px box shadow and the border darkens to #d8d8d8. Title sits in 16px semibold, price in 16px regular. Badges (new, sale) are positioned over the image area with uppercase 11px type and 2px horizontal padding.

**`spec-table`** — A bordered table with alternating row treatment for technical specifications. Headers use 12px uppercase labels in a soft gray background (#f8f9fb). Rows have a subtle hover state (#f8f9fb) for readability on dense spec sheets. Used extensively on router and networking product pages.

### Forms
**`text-input`** — A 40px tall input with 1px hairline border, 4px corner radius, and 16px horizontal padding. Focus state swaps to a 2px teal border (#4acbd6). Error state uses a 2px red border (#c13515). The input background is always white, ensuring high contrast against the soft canvas (#fefefe).

**`select-input`** — Matches the text-input dimensions and border treatment, with a custom dropdown arrow in `{colors.muted}`. Used for product filtering (Wi-Fi standard, speed rating, number of ports) on category pages.

**`search-bar`** — A full-pill (`{rounded.full}`) 44px tall input with a 1px hairline border and 20px horizontal padding. Focus state thickens the border to 2px teal. The pill shape is the only rounded-full element in the system, distinguishing search from all other inputs.

### Footer
**`footer`** — A dark section (#212121) with white text and 64px vertical padding. Links render in light gray (#a7a9ac) and shift to teal (#4acbd6) on hover. Column headings use 16px semibold white type. The footer typically contains product categories, support links, and legal information in a multi-column layout.

### Badges & Tags
**`product-card-badge`** — A teal-filled (#4acbd6) uppercase label with 2px corner radius (`{rounded.xs}`), used for "NEW" or "BEST SELLER" indicators. The amber variant (`product-card-badge-sale`) uses #ffcb00 for "SALE" or "DEAL" tags. Both use 11px bold type with 0.5px letter spacing.

**`filter-tag`** — A pill-shaped (`{rounded.full}`) tag with soft gray background and 1px hairline border, used for active filter indicators on category pages. Active state fills with teal and white text. Tags are 12px with 4px/12px padding.

### Modals & Overlays
**`modal-overlay`** — A 50% opacity black scrim covering the viewport. The modal content panel uses white background, 8px corner radius (`{rounded.md}`), and a 8px/32px box shadow for depth. Used for quick-view product previews, configuration wizards, and confirmation dialogs.

### Loading States
**`loading-spinner`** — A 24px teal (#4acbd6) circular spinner for inline loading states (add to cart, filter results). A 40px variant (`loading-spinner-lg`) is used for page-level loading. The spinner uses a continuous rotation animation with no text label.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav replaces top nav, search bar collapses to icon, footer stacks vertically, spec tables convert to stacked label-value pairs |
| Tablet | 744–1128px | 2-column product grid, top nav shows 4-5 links with overflow menu, search bar remains full but reduced width, footer uses 2-column layout |
| Desktop | 1128–1440px | 3-4 column product grid, full top nav with dropdowns, search bar at 400px max-width, footer uses 4-column layout, spec tables render as horizontal tables |
| Wide | > 1440px | 4-5 column product grid, max-width container at 1440px, search bar expands to 480px, additional whitespace around content sections |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Filter tags and badges are 28px minimum — acceptable for touch but not ideal; consider 36px minimum for mobile filter interactions
- Hamburger menu icon is 44x44px with 8px padding around the icon
- Product card CTAs ("Add to Cart") are 48px tall on mobile vs 40px on desktop
- Search icon in mobile collapsed state is 44x44px

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px; dropdown menus become full-screen overlays
- Product comparison table collapses to stacked card layout below 744px; each spec becomes a labeled row
- Footer columns collapse to single column below 744px; accordion pattern for section headings
- Sidebar filters collapse to a horizontal scrollable strip on mobile, with a "Filters" button that opens a bottom sheet
- Breadcrumb trail truncates to show only current page and parent category on mobile, with "..." for intermediate levels
- Multi-step product configuration (router setup wizards) collapses to single-page scroll on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components are inferred from common patterns; actual TP-Link hover animations and transitions (duration, easing) were not extractable
- Error states for forms (validation messages, error icons) are assumed based on industry standard; brand-specific error styling may differ
- Dark mode palette is inferred from the dark footer (#212121) and may not represent a full dark mode implementation
- The amber accent (#ffcb00) usage pattern is assumed for sale badges and urgency; actual application may vary across regions
- Font weights beyond 400, 500, 600, 700 are not confirmed; AktivGrotesk-Corp may support additional weights not present in extracted CSS
- Sub-brand palettes (Archer, Deco, Tapo, Kasa) may have distinct color systems not captured in the global palette
- Animation specifications (duration, easing curves, stagger delays) are not available
- Focus-visible styles for keyboard navigation were not extractable
- Print stylesheet behavior is unknown
- RTL language support and layout mirroring are not confirmed
- The extracted color list includes many grays that may be framework defaults or stock image tones; the true brand palette may be more limited than the 29 extracted hexes suggest
