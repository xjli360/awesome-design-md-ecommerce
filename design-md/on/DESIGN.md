---
version: alpha
name: "On"
source_url: "https://www.on-running.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A crisp, high-contrast performance brand where a single electric blue — #2f7efe — acts as the system’s primary voltage, appearing on CTAs, navigation accents, and product highlights against a predominantly white canvas (#ffffff) and a secondary off-white surface (#f7f7f7). The brand’s typographic voice is built on a custom family called “On” (with “On Mono” and “On Semi Mono” variants) paired with “Suisse Works” for editorial weight, creating a distinctively Swiss, technical feel that mirrors the company’s Zurich roots. The extracted palette reveals a surprising breadth: a safety red (#ed0000) used sparingly for sale badges or error states, a warm terracotta (#e15f14) that appears on lifestyle product accents, and a muted sage (#e2fbb1) that suggests an unexpected environmental or sustainability cue. The dominant gray scale runs from near-black (#151522) through charcoal (#4d4d4d) to warm stone (#dad8d2), giving the system a serious, engineered tone. Buttons use {rounded.sm} (8px) corners — not pill-shaped — reinforcing a precision aesthetic over friendliness. The top navigation is a thin, 64px strip with a transparent background that becomes white on scroll, and the search icon is a simple outlined loop rather than a filled orb. Product cards use {rounded.md} (12px) with a subtle shadow, and the hero section typically features full-bleed video or high-speed photography with a gradient overlay from {colors.ink} at 40% opacity. The brand’s signature move is the “On dot” — a small circular badge in {colors.primary} that appears on new arrivals and limited editions, and the CloudTec sole pattern is echoed in a repeating geometric motif used as a background texture on category pages. The checkout flow introduces Shopify Pay’s blue and Klarna’s pink, but the brand’s own palette remains rigorously restrained: three accent colors, one primary, and a warm-neutral gray scale.

colors:
  primary: "#2f7efe"
  primary-active: "#1a5fd4"
  primary-disabled: "#a3c5ff"
  ink: "#151522"
  body: "#4d4d4d"
  muted: "#7a7a7a"
  muted-soft: "#a0a0a0"
  hairline: "#dad8d2"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-warm: "#f0eceb"
  surface-warm-alt: "#faf7f6"
  on-primary: "#ffffff"
  accent-red: "#ed0000"
  accent-terracotta: "#e15f14"
  accent-sage: "#e2fbb1"
  charcoal: "#494740"
  scrim: "#151522"

typography:
  display-xl:
    fontFamily: "'On', 'Suisse Works', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'On', 'Suisse Works', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'On', 'Suisse Works', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'On', 'Suisse Works', -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'On', 'Suisse Works', -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'On', 'Suisse Works', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'On', 'Suisse Works', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'On', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'On', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'On', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "'On', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.17
    letterSpacing: 0
  badge:
    fontFamily: "'On Mono', 'On', -apple-system, system-ui, monospace"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'On Semi Mono', 'On', -apple-system, system-ui, monospace"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'On', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'On', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'On', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'On', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.1px

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
    height: 48px
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
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-tertiary-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-accent-terracotta:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  top-nav:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  top-nav-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: "0 1px 3px rgba(21, 21, 34, 0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 2px 8px rgba(21, 21, 34, 0.06)"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    boxShadow: "0 4px 16px rgba(21, 21, 34, 0.1)"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sage:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    height: "calc(100vh - 64px)"
    minHeight: 600px
  hero-overlay:
    background: "linear-gradient(180deg, rgba(21,21,34,0.4) 0%, rgba(21,21,34,0.1) 50%, rgba(21,21,34,0.6) 100%)"
  hero-cta:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 52px
  hero-cta-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: 24px
  category-card-hover:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-red}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 40px 12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-body:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  dot-badge:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 8px
    width: 8px
  dot-badge-red:
    backgroundColor: "{colors.accent-red}"
    rounded: "{rounded.full}"
    height: 8px
    width: 8px
  loading-spinner:
    color: "{colors.primary}"
    height: 24px
    width: 24px
  skeleton-loader:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.xs}"
    height: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for “Add to Cart,” “Shop Now,” and “Explore” actions. Rendered in {colors.primary} (#2f7efe) with white text and {rounded.sm} (8px) corners. On hover, shifts to {colors.primary-active} (#1a5fd4); disabled state uses {colors.primary-disabled} (#a3c5ff). Height is 48px with 12px vertical and 24px horizontal padding. The button uses {typography.button-md} (15px, weight 600) with 0.2px letter spacing for a precise, engineered feel.

**`button-secondary`** — An outlined alternative for secondary actions like “Learn More” or “View Details.” Uses a white background with a 2px solid {colors.ink} border. On hover, the background fills with {colors.surface-soft} (#f7f7f7). Same height and typography as the primary button, but with 11px vertical padding to account for the border.

**`button-tertiary-text`** — A text-only link styled as a button, used for “Sign In,” “Track Order,” and “Size Guide” actions. Appears in {colors.primary} with no background or border. On hover, shifts to {colors.primary-active}. Padding is 12px vertical with no horizontal padding, allowing it to sit inline with other elements.

**`button-accent-red`** and **`button-accent-terracotta`** — Smaller, high-visibility buttons used for sale items and limited editions. The red variant ({colors.accent-red} #ed0000) signals discounts or clearance; the terracotta variant ({colors.accent-terracotta} #e15f14) is used for seasonal or lifestyle collections. Both use {typography.button-sm} (13px, weight 600) and are 36px tall with 8px vertical padding.

### Navigation
**`top-nav`** — A 64px transparent navigation bar that becomes white on scroll with a subtle shadow. The logo sits left-aligned, with nav links in {typography.nav-link} (14px, weight 500, 0.1px letter spacing). Active and hover states shift link color to {colors.primary}. The search icon is a simple outlined loop, and the cart icon includes a {colors.primary} dot badge for item count. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

### Product Cards
**`product-card`** — A white card with {rounded.md} (12px) corners and a subtle shadow (0 2px 8px rgba(21,21,34,0.06)). On hover, the shadow deepens to 0 4px 16px. The card contains a product image (typically 4:5 ratio), a title in {typography.title-sm}, a price in {typography.body-md}, and optional badges. Badges appear in the top-left corner and use {typography.badge} (11px, uppercase, monospace) with 2px horizontal padding.

**`product-card-badge`** — Standard badge in {colors.primary} for “New” or “Limited Edition.” **`product-card-badge-red`** uses {colors.accent-red} for “Sale” or “Final Sale.” **`product-card-badge-sage`** uses {colors.accent-sage} (#e2fbb1) with dark text for sustainability-related tags like “Recycled Materials” or “Carbon Neutral.”

### Hero Section
**`hero-section`** — A full-viewport-height section (minus the 64px nav) with a minimum height of 600px. The background is typically a full-bleed video or high-speed photograph overlaid with a gradient from {colors.ink} at 40% opacity. Text appears in white using {typography.display-xl} (48px, weight 700). The hero CTA is a white button with dark text that shifts to {colors.surface-soft} on hover.

### Forms
**`text-input`** — A standard input field with a 1px {colors.hairline} border and {rounded.sm} corners. On focus, the border becomes 2px solid {colors.primary}. Error state uses a 2px {colors.accent-red} border. Height is 48px with 12px vertical padding. Used for search, email signup, and checkout fields.

**`select-input`** — Similar to text-input but includes a 40px right padding for the dropdown arrow. Used for size selection, sorting, and filter dropdowns.

**`quantity-selector`** — A compact 40px-tall input with increment/decrement buttons on either side. Used on product detail pages and cart.

### Footer
**`footer`** — A dark section with {colors.ink} background and white text. Contains columns for customer service, about, and social links. Links use {typography.link} (14px, weight 400) and shift to {colors.primary} on hover. Section headings use {typography.title-sm} (16px, weight 500). Padding is {spacing.section} (64px) vertical and {spacing.lg} (24px) horizontal.

### Miscellaneous
**`dot-badge`** — A small 8px circle in {colors.primary} used for notification indicators, new item markers, and step indicators in checkout. **`dot-badge-red`** uses {colors.accent-red} for urgent notifications.

**`loading-spinner`** — A 24px spinning circle in {colors.primary}, used during product loading and checkout processing.

**`skeleton-loader`** — A 16px-tall placeholder bar with {colors.hairline-soft} background and {rounded.xs} corners, used for content loading states.

**`accordion-header`** and **`accordion-body`** — Used on product detail pages for “Details,” “Shipping,” and “Returns” sections. Headers are clickable with no background, using {typography.title-sm} and 16px vertical padding. Bodies reveal with a smooth height animation and use {typography.body-sm} in {colors.body}.

**`divider`** and **`divider-soft`** — 1px horizontal rules used to separate sections. The standard divider uses {colors.hairline} (#dad8d2); the soft variant uses {colors.hairline-soft} (#e5e5e5) for less visual weight.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to {typography.display-md} (28px); buttons become full-width; footer stacks into single column; search bar moves to full-width below nav |
| Tablet | 744–1128px | Two-column product grid; nav links condensed to icons for search and cart; hero maintains full height but text reduces to {typography.display-lg} (36px); footer uses two-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero at full height with {typography.display-xl}; footer uses four-column layout; product detail page shows two-column layout (image left, details right) |
| Wide | > 1440px | Max-width container at 1440px with centered content; product grid expands to four columns; hero maintains full viewport height; additional whitespace on left and right of nav |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px on mobile to meet WCAG touch target guidelines
- Icon buttons are 40px × 40px with 8px internal padding
- Product card tap targets extend to the full card area
- Accordion headers have 44px minimum tap height
- Quantity selector buttons are 40px × 40px

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px; the menu overlay includes all primary links, search, and account options
- Product filters collapse into a “Filter” button that opens a bottom sheet on mobile
- Footer columns collapse into accordion sections on mobile, with the first column (brand info) always visible
- Product detail accordions (Details, Shipping, Returns) are collapsed by default on all breakpoints
- Hero section reduces text size and may crop video to 16:9 aspect ratio on mobile
- Product image galleries collapse from thumbnails to dot indicators on mobile
- Size selector switches from a horizontal row to a scrollable horizontal list on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product-card-badge variants (red, sage) could not be reliably extracted; assumed to maintain the same background color with a slight opacity shift
- Error styling for form inputs beyond the border color (e.g., error message typography, icon placement) was not observed
- Dark mode palette is not present on the live site; no dark-mode tokens are defined
- Sub-brand palettes (e.g., On x Loewe, On x Post Archive Faction) may introduce additional accent colors not captured in the extraction
- The exact font-weight values for “On” and “Suisse Works” are inferred from common web usage; the brand may use variable font weights that differ from the static values listed
- Animation durations and easing curves (e.g., hover transitions, accordion expand, skeleton loading) were not extracted
- Focus-visible ring styles (color, width, offset) for keyboard navigation are not documented
- The “On Mono” and “On Semi Mono” font families may have specific tracking or letter-spacing values for code-like display that were not observed
- Checkout flow introduces third-party payment widget colors (Shopify Pay blue, Klarna pink, Afterpay black) that are not part of the brand’s core palette
- Social media icon colors (Instagram gradient, YouTube red, Twitter blue) appear in the footer but are not brand tokens
- The extracted color list included #e5e5e5 (a generic light gray) and #f5f5f5 (another near-white); these may be framework defaults rather than intentional brand colors
- Stock photography may introduce dominant tones (e.g., green grass, blue sky) that inflate the color extraction; the sage (#e2fbb1) and terracotta (#e15f14) are the most distinctive non-generic colors in the list
- The brand’s signature CloudTec sole pattern used as a background texture could not be captured as a design token
- Video poster frames and gradient overlay percentages in the hero section are estimated based on common patterns
