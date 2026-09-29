---
version: alpha
name: "Fat Brain Toys"
source_url: "https://www.fatbraintoys.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A bright, curious educational toy store where #ffdb4a — a warm marigold — is the primary voltage, appearing in badges, sale callouts, and accent elements against a canvas of #ffffff and soft grays like #f5f5f5 and #f7f7f7. The brand uses Exo 2 and Quicksand (both found on the live site) for a geometric, friendly, slightly technical feel that matches the "brain" in the name — clean sans-serif letterforms with subtle rounded terminals. Product cards sit on white with #eeeeee hairlines and use #27a8e0 (a bright cyan) as a secondary accent for interactive elements like "Add to Cart" buttons and category links. The palette is unusually broad for a toy brand: alongside the expected primary and secondary, there are distinct semantic colors (#3c763d for success, #a94442 for errors, #8a6d3b for warnings) suggesting a mature e-commerce system with clear feedback states. Navigation uses a dark bar at #404041 with white text, while the search bar and utility icons float on white. The overall mood is energetic but not chaotic — the marigold and cyan provide pops of color against an otherwise restrained gray-and-white system, letting the toys themselves (and their bright product photography) be the real visual heroes. Rounded corners are moderate ({rounded.sm}–{rounded.md}), avoiding the extreme pill shapes of lifestyle brands in favor of a more structured, trustworthy feel.

colors:
  primary: "#ffdb4a"
  primary-active: "#e6c542"
  primary-disabled: "#fff0b3"
  ink: "#404041"
  body: "#58595b"
  muted: "#777777"
  muted-soft: "#9d9d9d"
  hairline: "#eeeeee"
  hairline-soft: "#f5f5f5"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#404041"
  accent-cyan: "#27a8e0"
  accent-cyan-active: "#007eb2"
  success: "#3c763d"
  success-bg: "#dff0d8"
  error: "#a94442"
  error-bg: "#f2dede"
  warning: "#8a6d3b"
  warning-bg: "#fcf8e3"
  info: "#31708f"
  info-bg: "#d9edf7"
  nav-bg: "#404041"
  nav-text: "#ffffff"
  sale-badge: "#dc143c"
  star-rating: "#ffdb4a"

typography:
  display-xl:
    fontFamily: "'Exo 2', 'Quicksand', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Exo 2', 'Quicksand', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Exo 2', 'Quicksand', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Exo 2', 'Quicksand', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Exo 2', 'Quicksand', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Quicksand', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Quicksand', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Quicksand', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Quicksand', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Exo 2', 'Quicksand', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Exo 2', 'Quicksand', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Exo 2', 'Quicksand', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'Quicksand', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Exo 2', 'Quicksand', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 10px
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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.hairline}"
  button-accent:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-active:
    backgroundColor: "{colors.accent-cyan-active}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.accent-cyan}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.accent-cyan}"
  text-input-error:
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link:
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-link-active:
    textColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
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
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    color: "{colors.ink}"
  product-card-rating:
    color: "{colors.star-rating}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  new-badge:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
    textTransform: uppercase
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  alert-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.success}"
  alert-error:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.error}"
  alert-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.warning}"
  alert-info:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.info}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.info}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, using the marigold `{colors.primary}` on a white or light gray background. Text is `{colors.on-primary}` (#404041 dark gray) for strong contrast. On hover, shifts to `{colors.primary-active}` (#e6c542). Disabled state uses `{colors.primary-disabled}` (#fff0b3) with muted text. Height is 44px with `{rounded.sm}` corners.

**`button-secondary`** — An outlined variant with white background, `{colors.ink}` text, and a 2px `{colors.hairline}` border. Used for "Learn More" or "View Details" actions alongside primary buttons. Hover state darkens the border to `{colors.muted}`.

**`button-accent`** — Cyan variant using `{colors.accent-cyan}` (#27a8e0) background with white text. Used for "Add to Cart" and other purchase-adjacent actions. Active state shifts to `{colors.accent-cyan-active}` (#007eb2).

**`button-ghost`** — Transparent background with cyan text, used for text links that need button-like sizing (e.g., "Clear filters", "See all"). Hover adds a subtle `{colors.surface-soft}` background.

### Navigation
**`nav-bar`** — A dark bar at `{colors.nav-bg}` (#404041) with white text, 56px tall. Links use `{typography.nav-link}` (Exo 2, 14px, uppercase, 600 weight, 0.5px letter spacing). Active link or hover uses `{colors.primary}` (#ffdb4a) as the text color. The nav contains category dropdowns, a logo, and utility icons (search, account, cart).

**`search-bar`** — A pill-shaped input (`{rounded.full}`) on white background with a 1px `{colors.hairline}` border. 40px tall, uses `{typography.body-md}`. On focus, the border changes to `{colors.accent-cyan}`. Often placed inside the nav bar or as a prominent hero element.

### Cards
**`product-card`** — White card with `{rounded.md}` (10px) corners and `{spacing.base}` padding. Contains a product image (with `{rounded.sm}`), title in `{typography.title-sm}`, price in bold `{typography.body-md}`, and star rating in `{colors.star-rating}` (#ffdb4a). Cards sit on `{colors.surface-soft}` (#f7f7f7) backgrounds in grid layouts.

**`category-chip`** — Pill-shaped filter chips (`{rounded.full}`) on `{colors.surface-soft}` background with `{typography.button-sm}`. Active state uses `{colors.primary}` background with `{colors.on-primary}` text. Used in category strips and filter bars.

### Badges
**`sale-badge`** — A small red badge (`{colors.sale-badge}` #dc143c) with white text, `{rounded.xs}` (4px), using uppercase `{typography.badge}`. Positioned on the top corner of product card images.

**`new-badge`** — Cyan badge (`{colors.accent-cyan}`) with white text, same sizing as sale badge. Used for new arrivals or featured items.

### Forms
**`text-input`** — Standard input field with white background, `{colors.hairline}` border, `{rounded.sm}`, and 44px height. Focus state uses a 2px `{colors.accent-cyan}` border. Error state uses a 2px `{colors.error}` (#a94442) border with `{colors.error-bg}` background.

### Alerts
**`alert-success`**, **`alert-error`**, **`alert-warning`**, **`alert-info`** — Four semantic alert variants using the extracted Bootstrap-style colors. Each has a light background, matching text color, `{rounded.sm}`, and a 1px border of the corresponding color. Used for cart messages, form validation, and informational banners.

### Footer
**`footer`** — Dark background (`{colors.ink}` #404041) with `{colors.muted-soft}` (#9d9d9d) text. Section headings use `{colors.canvas}` white with `{typography.title-sm}` and uppercase transformation. Links use `{typography.link}`. Padding is `{spacing.xxl}` top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1–2 columns). Nav bar collapses to hamburger menu. Search bar moves below nav or into a slide-out panel. Category chips stack vertically or scroll horizontally. Hero banner reduces padding to `{spacing.lg}`. |
| Tablet | 744–1128px | Two-column product grid. Nav bar shows top-level categories with dropdowns on hover. Search bar remains in nav. Footer columns stack to 2 rows. |
| Desktop | 1128–1440px | Three- to four-column product grid. Full nav bar with all categories visible. Hero banner at full `{spacing.section}` padding. Sidebar filters visible on category pages. |
| Wide | > 1440px | Max-width container (typically 1440px) centered. Product grid can expand to 5 columns. Hero banner may include full-width imagery. |

### Touch Targets
- All buttons and interactive elements minimum 44px height (buttons, inputs, chips).
- Nav links and icon buttons minimum 40px touch area.
- Category chips minimum 32px height with 16px horizontal padding.
- Product card tap targets (title, price, add-to-cart) spaced at least `{spacing.sm}` apart.

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px.
- Sidebar filters collapse to a "Filter" button that opens a modal or drawer on mobile.
- Footer link columns collapse from 4 columns to 2 columns on tablet, to a single vertical stack on mobile.
- Product image galleries collapse from thumbnail strip to single-image swipe on mobile.
- Category chip strips collapse from horizontal wrap to horizontal scroll with fade indicators on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors are heavily weighted toward Bootstrap framework defaults (alert colors, button blues, grays) — the brand's true palette may include more distinctive hues not captured in the extraction. The marigold (#ffdb4a) and cyan (#27a8e0) are the most distinctive signals.
- Font weights beyond what's declared in extracted CSS are inferred — Exo 2 and Quicksand are confirmed on the live site, but exact weight usage (e.g., 300 vs 400 for body, 600 vs 700 for headings) may vary.
- Hover and focus states for most components are inferred from common patterns; exact extracted values for `:hover`, `:focus`, `:active` are not available.
- Dark mode is not present on the live site; no dark mode tokens are defined.
- Sub-brand or seasonal palette variations (holiday, clearance, new-arrival) are not captured.
- Exact spacing values (padding, margin, gap) are estimated from common e-commerce patterns; the brand may use a different scale.
- Animation and transition timing (ease, duration) are not extracted.
- Iconography style (line vs filled, stroke weight) is not documented.
- Product card hover states (shadow, scale, border change) are not extracted.
- Checkout flow styling (Shopify Pay, Klarna, Afterpay widgets) may introduce additional colors not in the brand palette.
