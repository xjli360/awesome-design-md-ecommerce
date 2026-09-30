---
version: alpha
name: "Arbelos Films"
source_url: "https://arbelosfilms.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, scholarly blue — #1561a8 — anchors a site that feels more like a university press catalog than a movie distributor’s storefront. The palette is built on a narrow band of navy and slate (#003388, #005a87, #006ba1) against a near-white canvas (#f8f9f9), with the occasional jolt of cyan (#34e2e4) or purple (#4721fb) reserved for badges and accent elements. Typography runs Arial and Helvetica at modest sizes — no display faces, no variable fonts, no theatrical weight jumps. The grid is tight and text-heavy: film titles, director names, and release dates stack in compact rows with minimal imagery, trusting the strength of the catalog over hero photography. Buttons use {rounded.sm} corners and solid fills, while the search bar adopts {rounded.full} pill shapes — a rare moment of softness in an otherwise rectilinear system. The overall effect is archival and authoritative, a design that treats film as text worth studying rather than spectacle worth consuming.

colors:
  primary: "#1561a8"
  primary-active: "#005a87"
  primary-disabled: "#7c7c7c"
  ink: "#111111"
  body: "#222222"
  muted: "#444444"
  muted-soft: "#777777"
  hairline: "#d6d6d6"
  hairline-soft: "#e9e9e9"
  canvas: "#f8f9f9"
  surface-soft: "#ededed"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#34e2e4"
  accent-purple: "#4721fb"
  accent-magenta: "#ab1dfe"
  badge-new: "#00d084"
  badge-sale: "#0693e3"
  star-rating: "#313131"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 16px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.primary-disabled}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "2/3"
  badge:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
  filter-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.xxl} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Pre-order", and "Subscribe". Solid navy fill on {colors.primary} with white text, {rounded.sm} corners, and a compact 44px height. On hover and active, shifts to {colors.primary-active} (#005a87) for a darker, more grounded state. Disabled state uses {colors.primary-disabled} (#7c7c7c) to signal unavailability without ambiguity.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Learn More". White background with a 2px {colors.primary} border and matching text. Active state darkens the border and text to {colors.primary-active}. Used alongside primary buttons in product listings and hero sections.

**`button-tertiary`** — A text-only button for minimal interactions like "Cancel" or "Clear filters". Transparent background, {colors.primary} text, no border. Relies on the brand blue alone for affordance, keeping the interface clean in dense catalog views.

**`button-pill`** — A smaller, fully rounded button for compact contexts like "Shop Now" badges or quick-add actions. Uses {rounded.full} for a pill shape, {typography.button-sm} at 13px, and a shorter 36px height. Appears in product cards and promotional strips.

### Navigation
**`nav-bar`** — A fixed 64px header with white background and a subtle bottom border ({colors.hairline}). Navigation links use {typography.nav-link} at 15px semibold. Active links gain a 2px bottom border in {colors.primary} and matching text color. Hover state shifts text to {colors.primary} without the underline, keeping the bar clean and scholarly.

**`nav-link-active`** — The active state for top-level navigation items. Uses {colors.primary} text and a 2px solid bottom border in the same blue. No background fill — the brand trusts color and line to indicate location.

### Cards
**`product-card`** — The core content container for film listings. White background, 1px soft border ({colors.hairline-soft}), {rounded.sm} corners, and 16px padding. On hover, the border shifts to {colors.primary} and a subtle box shadow appears — a restrained interaction that rewards exploration without overwhelming the catalog grid. The image area uses a 2:3 aspect ratio ({rounded.xs}) to match standard poster dimensions.

### Forms
**`text-input`** — Standard input fields for search, newsletter signup, and checkout forms. White background, 1px {colors.hairline} border, {rounded.sm} corners, and 48px height. On focus, the border thickens to 2px and turns {colors.primary}. Error state uses a 2px {colors.primary-disabled} border — a muted but clear signal.

**`search-bar`** — A dedicated search input with {rounded.full} pill shape, distinguishing it from standard form fields. White background, 1px {colors.hairline} border, 48px height. Focus state mirrors the text-input pattern with a 2px {colors.primary} border. The pill shape is the site's only fully rounded element, creating a subtle visual anchor for the primary discovery action.

### Badges
**`badge`** — Small uppercase labels for film metadata (format, year, region). Default uses {colors.accent-cyan} (#34e2e4) background with dark text. Variants include `badge-new` with green (#00d084) for new releases and `badge-sale` with blue (#0693e3) for promotions. All use {typography.badge} at 11px bold, uppercase, with {rounded.xs} corners and minimal padding.

### Filters
**`filter-tag`** — Pill-shaped filter chips for browsing by genre, director, or format. Soft gray background ({colors.surface-soft}) with muted text. Active state fills with {colors.primary} and white text. 32px height keeps them compact in a horizontal scroll strip.

### Footer
**`footer`** — A dark footer section on {colors.ink} (#111111) with white text. Links use {colors.muted-soft} (#777777) and shift to white on hover. Padding uses {spacing.section} (64px) top and bottom for breathing room. The footer contains legal text, social links, and a newsletter signup — all in {typography.body-sm}.

### Hero
**`hero-section`** — A full-width dark hero area for featured films or collections. {colors.ink} background with white text. The title uses {typography.display-xl} at 28px bold, while the subtitle drops to {typography.body-md} in {colors.muted-soft}. Padding is generous at {spacing.xxl} (48px) vertical and {spacing.lg} (24px) horizontal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid, nav collapses to hamburger, product cards stack full-width, hero padding reduces to {spacing.lg} |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, search bar moves to header, filter tags wrap to two rows |
| Desktop | 1128–1440px | Three-column product grid, full nav with dropdowns, hero uses 60/40 text-to-image split, filter strip scrolls horizontally |
| Wide | > 1440px | Max-width container at 1440px, four-column product grid, hero image expands to fill, additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements maintain minimum 44x44px touch target (WCAG 2.1 compliant)
- Filter tags at 32px height are paired with 8px gap to prevent mis-taps
- Search bar at 48px height provides ample touch area
- Nav links in mobile hamburger menu expand to full-width 48px tap targets

### Collapsing Strategy
- Navigation collapses to hamburger menu below 744px, with slide-in drawer
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows
- Hero section stacks vertically on mobile (text above image)
- Filter strip becomes a horizontal scrollable row on mobile, hiding overflow
- Footer links collapse to a single column below 744px
- Search bar moves from hero to sticky header on mobile for persistent access

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted color list is heavily weighted toward generic web blues and grays — the brand's true primary (#1561a8) is the most distinctive blue, but there may be additional brand-specific accent colors not captured (e.g., a signature yellow or red for sale badges)
- No font-family declarations beyond system stacks (Arial, Helvetica, Times New Roman) — the brand may use a custom or licensed typeface not detectable from HTML/CSS extraction
- Hover and focus states for buttons and inputs are inferred from common patterns, not extracted from live CSS
- Error, success, and warning form states are not confirmed — only error border color is estimated
- Dark mode is not detected; the site appears to use light mode exclusively
- Sub-brand or collection-specific color palettes (e.g., for "Arbelos Classics" or "Arbelos Restorations") are not captured
- Animation and transition durations/timing functions are unknown
- Icon set and illustration style are not documented
- Mobile navigation drawer behavior (slide-in vs. overlay) is assumed from common patterns
- Checkout flow components (cart, payment forms) are not extracted — may use Shopify or third-party widgets with separate styling
