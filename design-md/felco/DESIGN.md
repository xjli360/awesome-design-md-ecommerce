---
version: alpha
name: "Felco"
source_url: "https://www.felco.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Red handle on a steel blade — that single chromatic signal has identified Felco pruning shears in nurseries, vineyards, and professional orchards for over seven decades, and the digital storefront distills the same logic: a near-black canvas (#1f1f1f) against which Felco red (#e30613) functions as both brand signature and interaction cue. The site runs Instrument Sans across every weight, a geometric contemporary sans-serif that echoes the precision-engineering ethos without drifting into the cold clinical register of industrial catalogs. Headlines land at weight 600–700 in sizes that stay restrained — display tops out around 48px, letting product photography of forged-aluminum handles and hardened-steel blades do the selling. The type system favors generous line-heights (1.5 on body, 1.3 on titles) to give dense technical specifications room to breathe beside warranty language and replacement-part tables. Rounded corners stay minimal: buttons and inputs use `{rounded.xs}` to `{rounded.sm}`, and product cards barely soften at `{rounded.md}` — the brand signals durability and function, not consumer-lifestyle softness. A warm amber accent (#ffb503) punctuates promotional badges, limited-edition callouts, and star ratings, pairing with the dominant red to evoke the physical warmth of sun-lit fieldwork. The surface system layers a pure white canvas beneath soft gray (#f2f2f2) section bands, with hairline borders at #dedede separating comparison-table rows and filter panels. Product cards sit flush on white surfaces with generous `{spacing.lg}` gutters, foregrounding the tool silhouette rather than decorative chrome. Navigation keeps a fixed 72px bar on desktop with sticky category tabs for Pruning, Cutting, Maintenance — functional wayfinding that mirrors how professionals think about their kit.

colors:
  primary: "#e30613"
  primary-active: "#bf0510"
  primary-disabled: "#ffe5e7"
  ink: "#1f1f1f"
  ink-deep: "#121212"
  body: "#737373"
  muted: "#bfbfbf"
  hairline: "#dedede"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-amber: "#ffb503"
  accent-amber-soft: "#fff9e5"
  success: "#008060"
  success-soft: "#e5fff6"
  error: "#d72c0d"
  error-soft: "#ffe5e7"
  star-rating: "#f2b600"

typography:
  display-xl:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.36px
  display-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.28px
  title-lg:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.11px
  title-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-lg:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.1px
  button-lg:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0
  nav-link:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  uppercase-label:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.8px
    textTransform: uppercase
  spec-value:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 1.5px solid {colors.ink}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 1.5px solid {colors.ink}
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 52px
    width: 100%
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.ink}
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 72px
    borderBottom: 1px solid {colors.hairline}
    boxShadow: 0 1px 4px rgba(0,0,0,0.06)
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid {colors.primary}
    padding: 12px 16px
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid transparent
    padding: 12px 16px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    boxShadow: 0 4px 16px rgba(0,0,0,0.08)
    border: 1px solid {colors.hairline}
  product-image-container:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    aspectRatio: 1 / 1
    padding: "{spacing.lg}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section-lg} {spacing.xxl}"
    minHeight: 520px
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xxl}"
    minHeight: 440px
  promo-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.uppercase-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.uppercase-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: 1px solid {colors.hairline-soft}
  spec-table-label:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  spec-table-value:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.spec-value}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px 12px 44px
    height: 48px
    border: 1px solid transparent
    borderFocus: 1px solid {colors.ink}
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    border: 1px solid {colors.hairline}
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  breadcrumb-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
  toast-success:
    backgroundColor: "{colors.success-soft}"
    textColor: "{colors.success}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  toast-error:
    backgroundColor: "{colors.error-soft}"
    textColor: "{colors.error}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
---

## Components

### Buttons

**`button-primary`** — Solid Felco red (#e30613) fill with white text set in Instrument Sans 600. Corners use `{rounded.xs}` (4px) keeping the tool-brand sharpness. On hover, background darkens to `{colors.primary-active}` (#bf0510) with a 150ms ease transition. Disabled state swaps to the pale red tint `{colors.primary-disabled}` with muted body-color text, signaling inactivity without losing the red association.

**`button-secondary`** — White fill with a 1.5px solid ink border. Text matches `{colors.ink}` at button-lg weight. Hover fills the surface to `{colors.surface-soft}` while maintaining the border. Used for secondary actions: "View specifications", "Compare models", "Find a dealer".

**`button-add-to-cart`** — Full-width variant of primary at 52px height, placed below price and quantity on PDP. Slightly taller tap target acknowledges that users often reach this control after scrolling spec tables on mobile.

### Navigation

**`nav-bar`** — Fixed 72px-tall white bar with a 1px `{colors.hairline}` bottom border. Logo sits left, main category links center (Pruning, Cutting, Maintenance, Accessories, Parts), utility icons right (search, account, cart). On scroll, gains a subtle box-shadow for depth separation without color shift.

**`category-tab-active` / `category-tab-inactive`** — Horizontal tab strip below the nav on category pages. Active tab carries a 2px red bottom border; inactive tabs show `{colors.body}` text with no border. Transitions between states on click with a 200ms slide.

### Product Card

**`product-card`** — White card with `{rounded.md}` corners and a 1px `{colors.hairline-soft}` border. Product image sits inside a `{colors.surface-soft}` container at 1:1 aspect with generous internal padding so the tool silhouette floats. Below the image: product name in `{typography.title-md}`, model number in `{typography.caption}`, price in `{typography.title-lg}`. On hover, border sharpens to `{colors.hairline}` and a 4px–16px shadow lifts the card.

### Hero Banner

**`hero-banner`** — Full-bleed dark (`{colors.ink}`) section with white display text and a product cutout image. Minimum height 520px to give the tool photograph breathing room. CTA button uses `button-primary`. Alternatively, `hero-banner-light` provides a `{colors.surface-soft}` background with dark text for seasonal or editorial content.

### Badges

**`promo-badge`** — Amber (#ffb503) background with dark ink text in `{typography.uppercase-label}`. Applied to limited-edition or seasonal promotions. Compact 4px 8px padding keeps it tight against product card corners.

**`new-badge`** — Red primary background with white text, same label typography and sizing. Marks newly launched products in collection grids.

### Specification Table

**`spec-table-row`** — Alternating rows are not used; instead, each row separates with a 1px `{colors.hairline-soft}` bottom border. Label column uses `{typography.body-sm}` in muted color; value column uses `{typography.spec-value}` (14px, weight 600) in ink. Rows stack vertically on mobile with label above value.

### Search

**`search-input`** — Pill-ish input with `{rounded.sm}` and `{colors.surface-soft}` resting background. A magnifying-glass icon sits 16px from the left edge. On focus, background transitions to white and a 1px ink border appears. Search overlay expands below with recent searches and suggested products.

### Footer

**`footer`** — Dark ink background matching the hero treatment, creating a bookend effect. Four columns: Products, Support, Company, Legal. Links render in `{colors.muted}` and brighten to white on hover. Bottom row contains locale selector, social icons, and copyright in `{typography.caption}`.

### Toast Notifications

**`toast-success`** — Light green tint background with `{colors.success}` text, used for add-to-cart confirmations and wishlist additions. Appears top-center, auto-dismisses after 4 seconds.

**`toast-error`** — Light red tint with `{colors.error}` text for validation failures and out-of-stock alerts.

### Breadcrumb

**`breadcrumb`** — Inline path using `{typography.body-sm}` with chevron separators. Ancestor links in `{colors.body}`, current page in `{colors.ink}`. Placed above the product title on PDP with `{spacing.sm}` bottom margin.

### Quantity Selector

**`quantity-selector`** — Inline stepper with minus/plus buttons flanking a numeric input. 44px height, `{rounded.xs}` corners, 1px hairline border. Buttons highlight to `{colors.surface-soft}` on press.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid. Nav collapses to hamburger + logo + cart icon. Hero text drops to `{typography.display-md}`. Spec tables stack label/value vertically. Footer columns collapse to accordions. |
| Tablet | 744–1128px | Two-column product grid. Nav shows condensed category links. Hero maintains full height but text shifts to `{typography.display-lg}`. PDP image and details stack vertically with image full-width. |
| Desktop | 1128–1440px | Three-to-four column product grid. Full horizontal nav with all categories visible. PDP uses side-by-side layout (60% image gallery, 40% details). Spec table shows two-column key-value pairs. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Grid expands to four columns with larger card images. Hero can show split layout (text left, product cutout right). Additional whitespace in section padding using `{spacing.section-lg}`. |

### Touch Targets

- All interactive elements maintain a minimum 44×44px tap area on mobile and tablet.
- Quantity selector buttons expand to full 44px touch targets even though their visual footprint is smaller.
- Category tabs gain 16px horizontal padding on touch devices for comfortable swiping.
- Footer accordion headers use 52px height for reliable thumb tapping.

### Collapsing Strategy

- Navigation category links collapse behind a hamburger icon below 744px; search moves into the slide-out menu with a prominent input at the top.
- Product filter sidebar converts to a bottom-sheet modal on mobile, triggered by a sticky "Filter" button.
- Specification tables lose their side-by-side layout below 744px and stack as label-then-value blocks with increased vertical spacing.
- Footer columns convert from a four-column grid to stacked accordions with `{colors.hairline}` dividers.
- Hero banner CTAs stack vertically on mobile with full-width buttons.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one font family (Instrument Sans) was detected; the site may load additional display or monospace faces via JavaScript that were not captured in static extraction.
- No CSS custom properties or design-token variables were extractable — all color values are inferred from rendered styles rather than a published token system.
- Icon system (size, stroke width, icon set name) could not be determined from extraction; likely uses inline SVGs loaded dynamically.
- Motion/animation durations and easing curves are estimated (150–200ms ease) rather than extracted.
- Several extracted colors (#049cff, #35ee7a, #f9423a, #f1e04d) appear to be Shopify system or notification colors rather than brand-owned tokens and have been excluded from the palette.
- Dark-mode treatment is not evident on the live site; this spec assumes light-mode only.
- Exact grid gutter values and container max-widths beyond the 1440px cap could not be confirmed.
