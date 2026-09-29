---
version: alpha
name: "Monti Kids"
source_url: "https://montikids.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A soft, airy ecosystem for early childhood development, Monti Kids uses a pastel-inflected palette anchored on #c1e9ff — a pale, milky cerulean that reads as nursery-light rather than brand-primary. The site wraps its Montessori-aligned product boxes in rounded corners ({rounded.lg}) and generous whitespace, with secondary washes of #e1fcff and #bde7ff creating a layered, aquatic atmosphere that never tips into baby-blue cliché. Typography runs Shopify Sans Medium and Shopify Sans Regular at modest weights — the brand trusts its product photography and clean layout over typographic drama, letting the wooden toys and play-kit materials carry the sensory load. The extracted palette (#5b5b5b, #f4f5f6, #eceafb, #f0edfe, #e9e8fb) suggests a muted, lavender-tinged gray scale alongside the primary blue, giving the interface a gentle, unforced femininity without leaning into pink. Buttons and CTAs use the cerulean primary against white text, while secondary surfaces in #f4f5f6 and #ecf7fc create soft card boundaries. The overall effect is one of deliberate calm — a digital environment designed to feel as safe and unhurried as the Montessori method itself.

colors:
  primary: "#c1e9ff"
  primary-active: "#9dd8f5"
  primary-disabled: "#e1fcff"
  ink: "#5b5b5b"
  body: "#5b5b5b"
  muted: "#8a8a8a"
  muted-soft: "#b0b0b0"
  hairline: "#e0e0e0"
  hairline-soft: "#eceafb"
  canvas: "#ffffff"
  surface-soft: "#f4f5f6"
  surface-card: "#ffffff"
  surface-lavender: "#eceafb"
  surface-blue-soft: "#ecf7fc"
  surface-blue-light: "#e1fcff"
  surface-blue-mid: "#bde7ff"
  surface-purple-soft: "#f0edfe"
  surface-purple-light: "#e9e8fb"
  on-primary: "#5b5b5b"
  on-primary-white: "#ffffff"
  badge-new: "#c1e9ff"
  badge-sale: "#eceafb"

typography:
  display-xl:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Shopify Sans Regular', 'Shopify Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Shopify Sans Regular', 'Shopify Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Shopify Sans Regular', 'Shopify Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Shopify Sans Regular', 'Shopify Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Shopify Sans Regular', 'Shopify Sans', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Shopify Sans Regular', 'Shopify Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px

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
    textColor: "{colors.on-primary-white}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary-white}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary-white}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  text-input-error:
    border: "1px solid #d32f2f"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-blue-light}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary-white}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "10px 20px"
    height: 44px
  search-icon:
    color: "{colors.muted}"
    size: 18px
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.body}"
    hoverColor: "{colors.ink}"
  social-icon:
    color: "{colors.muted}"
    size: 20px
    hoverColor: "{colors.ink}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base}"
  tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary-white}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  age-badge:
    backgroundColor: "{colors.surface-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  rating-stars:
    color: "#f5a623"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with `{colors.primary}` (#c1e9ff) against white text. Used for "Add to Cart", "Subscribe", and "Shop Now" actions. On hover, shifts to `{colors.primary-active}` (#9dd8f5). Disabled state uses `{colors.primary-disabled}` (#e1fcff) with muted text. Height is 44px with `{rounded.sm}` corners — friendly but not pill-shaped.

**`button-secondary`** — Outlined alternative with white background, ink text, and a 1px hairline border. Used for "Learn More" and secondary checkout actions. Same 44px height and `{rounded.sm}` as primary for visual consistency.

**`button-tertiary`** — Text-only button with no background or border. Used for "Cancel", "Skip", and inline navigation. Hover adds a subtle underline or opacity shift.

**`button-pill-primary`** — Compact pill-shaped button (`{rounded.full}`) at 36px height, used for filter chips, age-selector toggles, and mobile CTAs. Uses the same primary color scheme.

### Cards
**`product-card`** — The core product display unit: white surface with `{rounded.lg}` (16px), subtle box shadow (0 2px 8px rgba(0,0,0,0.06)), and 16px padding. The product image sits in a 1:1 aspect ratio with `{rounded.md}`. Title uses `{typography.title-md}`, price uses `{typography.title-sm}`. Badges (new, sale, age-range) sit as small uppercase labels with `{rounded.xs}`.

**`product-card-badge`** — Small promotional tag, typically "NEW" or "BEST SELLER". Uses `{colors.badge-new}` background (#c1e9ff) with ink text, `{typography.badge}` (11px uppercase), and tight 2px/8px padding.

### Navigation
**`nav-bar`** — Fixed top navigation at 72px height, white background with a soft hairline bottom border (`{colors.hairline-soft}`). Links use `{typography.nav-link}` (14px medium weight). Active state has a 2px bottom border in `{colors.primary}`.

**`search-bar`** — Full-rounded pill (`{rounded.full}`) at 44px height with a 1px hairline border. Uses body-md typography and a muted search icon. Focus state gains a primary-colored border.

### Forms
**`text-input`** — Standard input field at 48px height with `{rounded.sm}`, 1px hairline border, and 12px/16px padding. Focus state uses a 2px primary border. Error state uses a red border (#d32f2f).

**`select-dropdown`** — Matches text-input dimensions and styling, with a custom dropdown arrow in muted color.

### Tabs & Filters
**`tab-active`** / **`tab-inactive`** — Pill-shaped filter toggles (`{rounded.full}`) at 32px height. Active tab fills with primary color and white text; inactive uses `{colors.surface-soft}` (#f4f5f6) with muted text. Used for product category filtering and age-range selection.

**`age-badge`** — Small lavender pill (`{colors.surface-lavender}`) for displaying recommended age ranges (e.g., "0-3 months", "3-6 months"). Uses uppercase badge typography.

### Hero & Footer
**`hero-section`** — Full-width promotional banner using `{colors.surface-blue-light}` (#e1fcff) background with `{typography.display-xl}` heading. Contains a `hero-cta` button matching primary button styling but with larger padding (14px/32px) and 48px height for visual prominence.

**`footer-section`** — Soft gray background (`{colors.surface-soft}`) with body-sm typography. Links use `{typography.link}` with hover darkening to ink. Social icons sit at 20px in muted color, darkening on hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked hero content, 16px page margins, buttons full-width |
| Tablet | 744–1128px | Two-column product grid, expanded nav links, 24px page margins, hero with side-by-side layout |
| Desktop | 1128–1440px | Three-column product grid, full top nav, 32px page margins, hero with larger typography |
| Wide | > 1440px | Max-width container at 1440px, centered content, four-column product grid |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target
- Product cards have 16px minimum tap padding
- Tab and filter pills are minimum 32px tall with 16px horizontal padding
- Mobile nav hamburger icon is 44x44px
- Search bar maintains 44px height on all breakpoints

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport shrinks
- Hero section stacks vertically below 744px (image above text)
- Footer link columns collapse to single column below 744px
- Tab/filter strips become horizontally scrollable on mobile
- Accordion sections replace multi-column layouts below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors are predominantly light pastels and grays — the brand's true primary may be a more saturated color not captured in the extraction (e.g., a deeper blue or green used in logos or photography). The palette above represents the site's background/surface colors accurately but may miss accent or brand-mark colors.
- Font-family extraction returned only "Shopify Sans Medium" and "Shopify Sans Regular" — the brand may use additional weights (Light, Bold) not present in the sampled pages.
- No meta theme-color was found; mobile browser chrome color is unknown.
- Hover states for buttons and links are inferred from common patterns, not extracted from live CSS.
- Error states for forms (validation messages, error icons) are not documented — the brand may use custom error styling.
- Dark mode is not supported and likely not implemented.
- Sub-brand or collection-specific color variations (e.g., "Monti Kids Play Kits" vs. "Monti Kids Toys") are not captured.
- Animation and transition timings (ease curves, durations) are not extracted.
- Icon set and illustration style are not documented — the brand may use custom Montessori-themed illustrations.
- Checkout flow colors (Shopify Pay, Klarna, Afterpay widgets) were filtered out but may appear on cart pages.
