---
version: alpha
name: "Satechi"
source_url: "https://www.satechi.net"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A dark, precision-oriented electronics accessories brand that builds its entire visual identity around the tension between #222021 (near-black ink) and #f55a19 (a scorched-orange accent that reads like anodized aluminum catching light). The brand's product photography — aluminum docks, USB-C hubs, mechanical keyboards — is the real typography; the actual type system is a restrained sans-serif that stays out of the way, with body copy at 14–16px and display rarely exceeding 24px. Every product card uses a soft #f5f2ef canvas that mimics the warm neutral of brushed aluminum, while CTAs pulse in #f55a19 with {rounded.sm} corners that echo the chamfered edges of the hardware itself. The nav bar sits at 64px, dark (#222021) with white text, a clean horizontal strip that signals industrial confidence. Badges for "NEW" or "SALE" appear in #e22120 (a cooler red than the orange primary) or #00eab6 (a mint accent used sparingly for compatibility badges). The checkout flow introduces #4e34e0 (a deep violet) for payment buttons — a deliberate shift that separates transaction from browsing. There is no gradient, no drop-shadow excess, no decorative illustration; the brand trusts hard edges, generous whitespace, and the material truth of its products.

colors:
  primary: "#f55a19"
  primary-active: "#d94a0f"
  primary-disabled: "#f5a07a"
  ink: "#222021"
  body: "#4c4c4c"
  muted: "#6d6d6d"
  muted-soft: "#919090"
  hairline: "#dedede"
  hairline-soft: "#e5e5eb"
  canvas: "#ffffff"
  surface-soft: "#f5f2ef"
  surface-card: "#fafafa"
  surface-dark: "#1b1c21"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-red: "#e22120"
  accent-mint: "#00eab6"
  accent-violet: "#4e34e0"
  accent-blue: "#1878b9"
  badge-new: "#e22120"
  badge-sale: "#e22120"
  badge-compatibility: "#00eab6"
  footer-bg: "#272d45"
  footer-text: "#cfc6bf"
  scrim: "#0a0a0a"

typography:
  display-xl:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  badge:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    border: "1px solid {colors.muted}"
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-checkout:
    backgroundColor: "{colors.accent-violet}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-bar-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.on-dark}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted-soft}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-mint:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-violet:
    backgroundColor: "{colors.accent-violet}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.lg} 0"
  section-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    padding: "0 0 {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. Uses the brand's scorched-orange (#f55a19) on a white background with uppercase 14px/600 weight type. Corners are minimally rounded at {rounded.sm} (4px), echoing the chamfered edges of Satechi's aluminum products. On hover, the background deepens to #d94a0f (`{colors.primary-active}`). When disabled, it fades to a pale peach (`{colors.primary-disabled}`) with reduced opacity.

**`button-secondary`** — An outlined variant for secondary actions. White background with a 1px `{colors.hairline}` border and `{colors.ink}` text. On hover, the background shifts to `{colors.surface-soft}` and the border to `{colors.muted}`. Used for "Learn More" or "View Details" links.

**`button-dark`** — Used on light backgrounds or within hero sections that need a dark anchor. `{colors.ink}` background with white text. Appears in product detail "Add to Cart" when the primary orange would compete with other orange elements.

**`button-checkout`** — A distinct deep violet (`{colors.accent-violet}`) button reserved for the checkout flow. Slightly taller (48px) with more horizontal padding (32px) to signal finality and importance. This color shift deliberately separates the transaction moment from the browsing experience.

### Cards
**`product-card`** — A clean, minimal card with a white background (`{colors.surface-card}`) and {rounded.md} (8px) corners. The product image fills the top of the card with no padding; title and price sit below with `{spacing.sm}` padding on the sides. No drop shadow — the card relies on the contrast between the white surface and the `{colors.surface-soft}` page background. Badges overlay the top-left of the image area.

**`product-card-badge`** — Small uppercase labels (10px/700 weight) that sit at the top-left of product images. Red (`{colors.badge-new}`) for "NEW" or "SALE" items, mint (`{colors.accent-mint}`) for compatibility badges like "USB-C" or "M4 Chip", and violet (`{colors.accent-violet}`) for exclusive or limited-edition tags.

### Navigation
**`nav-bar`** — A fixed 64px dark bar (`{colors.ink}`) with white uppercase nav links at 13px/500 weight. The Satechi logo sits left-aligned in white. Links have 8px vertical and 16px horizontal padding. The active link or hover state shifts to `{colors.primary}`. On mobile, the nav collapses into a hamburger menu with a slide-out drawer.

### Forms
**`text-input`** — Standard input fields with a white background, 1px `{colors.hairline}` border, and {rounded.sm} corners. On focus, the border switches to `{colors.primary}`. Height is 44px with 12px vertical and 16px horizontal padding. Used in search, newsletter signup, and checkout forms.

**`select-input`** — Matches the text-input styling but includes a custom dropdown arrow. Used for product filtering (category, sort by) and address forms.

### Footer
**`footer`** — A deep navy section (`{colors.footer-bg}`) with warm gray text (`{colors.footer-text}`). Links are 14px/400 weight and shift to white on hover. The footer contains columns for product categories, support links, company info, and social icons. Padding is `{spacing.xxl}` vertical and `{spacing.lg}` horizontal.

### Hero
**`hero-section`** — Full-width dark section (`{colors.ink}`) with white heading text and muted gray subtitle. Used for featured product launches and seasonal campaigns. The heading uses `{typography.display-xl}` (28px/700 weight) and the subtitle uses `{typography.body-md}` in `{colors.muted-soft}`. Background may include a subtle product image or pattern overlay.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; hero padding reduces to 32px; footer columns stack vertically; search bar moves to drawer |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards in 2-column grid; hero padding at 48px; footer in 2-column layout |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-4 column grid; hero at full padding (64px); footer in 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero content centered with max-width 1200px |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav links have 48px touch targets (8px padding on 32px text height)
- Product card tap targets are the full card area
- Search bar has 48px height for easy tapping

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Product grid collapses from 4 columns → 2 columns → 1 column
- Footer columns collapse from 4 → 2 → 1
- Hero content padding reduces by 50% on mobile
- Search bar moves from inline to a slide-out drawer on mobile
- Product filters collapse into a "Filter" button that opens a modal on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font-family declarations were limited to "inherit" and widget-specific fonts (oke-widget-icons). The actual brand typeface could not be reliably extracted — the system likely uses system-ui stack or a custom font loaded via Shopify theme settings. The typography block uses "inherit" as a placeholder; a real implementation should verify the actual font family.
- Hover and active states for most components were inferred from common patterns rather than extracted from the live site.
- Error state styling (form validation, error messages) was not visible during extraction.
- Dark mode preferences or alternate color schemes were not detected.
- The extracted hex list includes many grays and neutrals that may be Shopify theme defaults rather than intentional brand colors. The distinctive colors (#f55a19, #4e34e0, #00eab6, #e22120) are confidently brand-specific.
- Product card hover effects (scale, shadow, border) were not extractable from static analysis.
- Loading states and skeleton screens were not observed.
- Animation durations and easing curves were not captured.
- The checkout flow colors (#4e34e0) may be from a Shopify payment app rather than the brand itself — use with caution outside checkout context.
- Social icon colors in the extracted list may not be brand colors.
