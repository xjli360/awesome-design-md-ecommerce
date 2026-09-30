---
version: alpha
name: "Eureka Ergonomic"
source_url: "https://eurekaergonomic.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A teal-and-coral voltage runs through Eureka Ergonomic's digital storefront, where #108474 (a deep, almost-jade teal) anchors primary actions and #c70000 (a sharp stop-sign red) marks sale badges and urgency cues — a color story that reads more outdoor-gear than furniture, giving the brand an unexpected athleticism. The palette is unusually wide for a DTC furniture brand: alongside the core teal and red sit #01bbd5 (a bright cyan accent), #fecb34 (a marigold yellow for star ratings and highlights), and a full grayscale from #222222 ink to #f9fafb canvas. This chromatic breadth, paired with Inter as the sole body typeface at moderate weights, creates a system that feels engineered rather than curated — every color has a job, every corner is softly squared at `{rounded.sm}` (8px) for buttons and `{rounded.md}` (12px) for cards. The brand's confidence shows in its use of #c70000 as a persistent accent: it appears on discount badges, "Shop Now" CTAs, and cart indicators, a consistent pulse that drives urgency without tipping into alarm. Product cards use generous `{spacing.lg}` padding and `{rounded.md}` corners, with the teal primary appearing on "Add to Cart" buttons and the cyan on secondary actions like "Quick View" — a two-tone system that distinguishes primary from secondary without relying on outline styles. The overall effect is of a brand that treats its furniture like performance equipment: clean, purposeful, and backed by a color system that never leaves a UI element unassigned.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#7bb5a9"
  ink: "#222222"
  body: "#3a3a3a"
  muted: "#7b7b7b"
  muted-soft: "#969595"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#01bbd5"
  accent-red: "#c70000"
  accent-yellow: "#fecb34"
  accent-dark: "#181716"
  star-rating: "#fecb34"
  badge-sale: "#c70000"
  badge-new: "#108474"
  link-blue: "#07a9fe"
  error: "#d21625"
  success: "#339999"

typography:
  display-xl:
    fontFamily: "'Inter', 'JudgemeStar', -apple-system, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', 'JudgemeStar', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', 'JudgemeStar', -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Inter', 'JudgemeStar', -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'JudgemeStar', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'JudgemeStar', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'JudgemeStar', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'JudgemeStar', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'JudgemeStar', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'JudgemeStar', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', 'JudgemeStar', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'JudgemeStar', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', 'JudgemeStar', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', 'JudgemeStar', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'JudgemeStar', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
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
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 38px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  product-card-sale-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-new-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-rating:
    color: "{colors.star-rating}"
    typography: "{typography.caption-sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
  cart-icon:
    color: "{colors.ink}"
    height: 24px
  cart-icon-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with `{colors.primary}` teal and white text. Used for "Add to Cart", "Shop Now", and primary form submissions. On hover, shifts to `{colors.primary-active}` (#0d6b5d). Disabled state uses `{colors.primary-disabled}` (#7bb5a9). Height is 44px with `{rounded.sm}` corners and 12px vertical padding.

**`button-secondary`** — Outline variant with white background, `{colors.ink}` text, and a `1px` `{colors.hairline}` border. Used for "Quick View", "Learn More", and secondary form actions. Matches `button-primary` in height and corner radius. Hover state darkens the border to `{colors.muted}`.

**`button-accent-red`** — Urgency-driven CTA using `{colors.accent-red}` (#c70000). Appears on sale banners, limited-time offers, and clearance sections. Same dimensions as `button-primary`. Hover state deepens to a darker crimson.

**`button-accent-cyan`** — A smaller, lighter accent button using `{colors.accent-cyan}` (#01bbd5). Used for tertiary actions like "Subscribe" or "Notify Me". Height is 38px with `{rounded.sm}` corners and 10px vertical padding.

### Cards
**`product-card`** — The primary product presentation unit. White background with `{rounded.md}` (12px) corners and `{spacing.base}` (16px) padding. Contains an image area with `{rounded.sm}` (8px) corners, a title in `{typography.title-sm}`, price in `{typography.body-md}`, and optional badges. Badges use `{rounded.xs}` (4px) and uppercase `{typography.badge}` — sale badges are `{colors.badge-sale}` red, new badges are `{colors.badge-new}` teal. Star ratings render in `{colors.star-rating}` marigold yellow.

**`hero-banner`** — Full-width promotional section with `{colors.surface-soft}` background and `{typography.display-xl}` heading. Uses `{spacing.section}` (64px) vertical padding and `{spacing.xl}` (32px) horizontal padding. The hero CTA is a larger `button-primary` at 48px height with 14px vertical padding.

### Navigation
**`nav-bar`** — Fixed top navigation at 72px height with white background and a `1px` `{colors.hairline-soft}` bottom border. Links use `{typography.nav-link}` (15px, weight 500). Active links render in `{colors.primary}` teal; inactive links in `{colors.muted}`. The cart icon sits at 24px with a red badge overlay.

### Forms
**`text-input`** — Standard input field at 44px height with `{rounded.sm}` corners, `{colors.hairline}` border, and `{colors.body}` text. Focus state swaps the border to `{colors.primary}` teal. Padding is 10px vertical, 16px horizontal.

**`search-bar`** — Pill-shaped search input using `{rounded.full}` (9999px) radius. Matches text-input height (44px) but uses `{rounded.full}` for a friendlier appearance. Focus state mirrors text-input with `{colors.primary}` border.

### Footer
**`footer-section`** — Dark footer using `{colors.ink}` (#222222) background and `{colors.canvas}` (#f9fafb) text. Links render in `{colors.muted-soft}` (#969595) and shift to white on hover. Vertical padding is `{spacing.xxl}` (48px) with `{spacing.xl}` (32px) horizontal padding.

### Accordion
**`accordion-header`** — Expandable section header with `{colors.ink}` text, `{typography.title-sm}`, and a `1px` `{colors.hairline-soft}` bottom border. Padding is `{spacing.md}` (12px) vertical and `{spacing.base}` (16px) horizontal. Content area uses `{colors.canvas}` background and `{colors.body}` text with `{spacing.base}` padding and `{spacing.lg}` bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked hero layout, reduced padding (base 12px), smaller display type (display-md), full-width buttons |
| Tablet | 744–1128px | Two-column product grid, visible top nav with condensed links, hero retains full-width but reduces padding to 32px, search bar collapses to icon |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links, hero at max-width 1200px centered, search bar full-width |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero expands to full viewport height with parallax, increased whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height per iOS HIG
- Cart icon badge is 18px minimum with 24px touch area
- Product card images are tappable with no minimum size constraint
- Accordion headers are 44px minimum height for touch
- Nav links have 44px minimum tap area

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Search bar collapses to icon-only trigger below 744px, expanding to full-width overlay on tap
- Product grid collapses from 4 columns to 2 columns at 1128px, then to 1 column at 744px
- Hero banner reduces vertical padding from 64px to 32px below 744px
- Footer link columns collapse to single-column stacked layout below 744px
- Accordion remains single-column at all breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from static CSS; the active/disabled states provided are inferred from common patterns
- Error state styling for form inputs (border color, helper text) not observed in extracted data
- Dark mode or high-contrast mode variants not present in extracted CSS
- Sub-brand or collection-specific color palettes (e.g., "Gaming" vs "Office" vs "Standing Desk") not distinguishable from extracted data
- Animation and transition timing values (hover transitions, page load animations) not captured
- Dropdown and mega-menu styling for navigation not observed
- Modal and overlay component styling (quick-view, cart drawer) not extracted
- Typography scale for mobile (responsive font sizes) not reliably extracted; desktop values provided
- The extracted color list includes many grayscale values (#eeeeee, #f0f0f0, #fafafa, #121212, #7d7d7d, #bfbfbf, #989898, #f6f7f8, #f2f2f2, #e2e2e2, #dadada, #edf5f5) that may represent unused CSS variables or framework defaults — the core palette above selects the most distinctive and frequently occurring values
- The JudgemeStar font family appears in extracted declarations but its usage (likely for review stars) is not fully documented
- Shopify-specific checkout and cart page styling not captured
- Mobile-specific navigation patterns (hamburger menu animation, slide-out drawer) not documented
