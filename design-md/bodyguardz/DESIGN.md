---
version: alpha
name: "BodyGuardz"
source_url: "https://www.bodyguardz.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A protective brand that wraps its products in a palette of muted coastal grays (#859eab, #668796) and a warm, peachy canvas (#fff5ed), creating a visual atmosphere that feels more like a trusted gear shop than a phone-accessory store. The brand's primary voltage comes from the soft sage-steel #859eab — a color that appears nowhere in the generic web palette and signals a deliberate departure from the black-and-neon conventions of the protection category. Typography runs on Jost and Modern Gothic, two faces that bring a clean, slightly architectural modernism to product names and navigation. Buttons use {rounded.sm} corners and sit on the sage primary, while the search bar and product cards adopt {rounded.md} for a friendly but not pillowy feel. The site's Shopify foundation is visible in the checkout-widget colors that pepper the extracted palette (#0062cc, #1e7e34, #d39e00), but the brand's own voice lives in the contrast between #1a1a1a ink on #fff5ed canvas — a warm, approachable reading experience that makes drop-test ratings and military-grade claims feel less clinical. The footer and secondary surfaces use #f2f2f2, keeping the overall weight light and airy, while the meta theme-color of #ffffff ensures the browser chrome disappears into the brand's white frame.

colors:
  primary: "#859eab"
  primary-active: "#668796"
  primary-disabled: "#c8d5dc"
  ink: "#1a1a1a"
  body: "#241f21"
  muted: "#7c8d8f"
  muted-soft: "#a8b8ba"
  hairline: "#dae0e5"
  hairline-soft: "#e4e9e9"
  canvas: "#fff5ed"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#fff5ed"
  accent-sage: "#859eab"
  accent-steel: "#668796"
  error: "#bd2130"
  success: "#1e7e34"
  warning: "#d39e00"
  info: "#117a8b"

typography:
  display-xl:
    fontFamily: "'Jost', 'Modern Gothic', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Jost', 'Modern Gothic', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Jost', 'Modern Gothic', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Jost', 'Modern Gothic', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'CircularProWeb', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'CircularProWeb', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'CircularProWeb', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Jost', 'Modern Gothic', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Jost', 'Modern Gothic', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  link:
    fontFamily: "'CircularProWeb', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Jost', 'Modern Gothic', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Jost', 'Modern Gothic', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase

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
    padding: 12px 24px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    backgroundColor: "{colors.surface-soft}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.primary}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 52px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.link}"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  rating-stars:
    color: "{colors.warning}"
    size: 16px
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
    border: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Shop Now", and "Get Protected" actions. Rendered on the sage #859eab background with white text and {rounded.sm} corners, it carries the brand's full weight. On hover, it shifts to the deeper steel #668796 (`button-primary-active`). The disabled state fades to a muted sage #c8d5dc, signaling unavailability without visual noise.

**`button-secondary`** — A bordered alternative for secondary actions like "Learn More" or "Compare Models". Uses the warm canvas background with ink text and a hairline border. On active state, the border swaps to the primary sage, creating a subtle brand cue without overwhelming the layout.

**`button-ghost`** — A text-only variant for tertiary actions like "Cancel" or "View Details". Uses the primary sage as text color on a transparent background, keeping the interface clean while maintaining brand consistency.

### Cards
**`product-card`** — The primary product display unit, a white card with {rounded.md} corners and base padding. Product images sit inside with {rounded.sm} corners, creating a nested softness. Badges like "NEW" or "SALE" float at the top-left using `product-card-badge` or `badge-sale`/`badge-new`, rendered in the brand's uppercase condensed style. The card carries no shadow by default, relying on the white surface against the warm canvas for separation.

### Navigation
**`nav-bar`** — A 72px fixed-height bar on the warm canvas background, separated from content by a soft hairline. Navigation links use Jost at 15px with 0.2px letter-spacing, giving a slightly spaced, modern feel. The active state underlines with a 2px primary sage line, a restrained indicator that doesn't compete with product imagery. On mobile, the nav collapses into a hamburger menu with a full-height drawer.

### Forms
**`text-input`** — Standard input fields with white background, ink text, and a hairline border. On focus, the border thickens to 2px and adopts the primary sage, providing clear focus indication without relying on colored shadows or outlines. Placeholder text uses the muted-soft gray, keeping the form readable but uncluttered.

### Footer
**`footer`** — A full-width section on the soft surface (#f2f2f2) with muted text for links and body copy. Links are set in CircularProWeb at 14px, and hover to ink color. The footer uses section-level padding (64px top/bottom) with generous left/right spacing, creating a calm, spacious end to the page.

### Badges
**`badge-sale`** and **`badge-new`** — Small, uppercase, bold labels that sit on product cards. Sale uses the error red (#bd2130), new uses success green (#1e7e34), both with white text and {rounded.xs} corners. The 11px font with 0.5px letter-spacing ensures they're readable at small sizes without dominating the card.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, nav collapses to hamburger, hero padding reduced to 32px, buttons become full-width, font sizes scale down one step |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, hero maintains section padding, search bar remains visible |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, hero at full section padding, search bar with expanded width |
| Wide | > 1440px | Max-width container at 1440px, centered content, product grid can show four columns, hero text scales to display-xl |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Product card tap targets (add to cart, quick view) are at least 48px tall
- Nav links on mobile drawer have 48px touch targets
- Search bar maintains 48px height across all breakpoints

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product filters collapse to a "Filter" button with modal overlay on mobile
- Footer link columns collapse to accordion-style sections on mobile
- Hero image and text stack vertically below 744px
- Multi-column product grids reduce to single column on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is heavily polluted with Shopify checkout-widget colors (#0062cc, #1e7e34, #117a8b, #d39e00, #bd2130, #dae0e5, #1d2124, #b3d7ff, #004085, #383d41, #155724, #0c5460, #856404, #721c24, #818182, #1b1e21, #f6f7f7, #e4e9e9, #444e50, #17405c, #9fcdff, #c8cbcf) and stock-image dominant tones. The true brand palette likely centers on #859eab, #668796, #fff5ed, #f2f2f2, #1a1a1a, and #241f21 — the remaining colors should be treated as system defaults until confirmed by design files.
- Font stack is inferred from extracted declarations; Jost and Modern Gothic appear as distinct brand choices alongside the system CircularProWeb. Exact font weights and sizes for each typography token are estimated based on common DTC patterns and should be verified against the live site's computed styles.
- Hover states for buttons and links are inferred from common patterns; exact color transitions and timing are unknown.
- Error states for forms (validation, error messages) are not captured; the error red #bd2130 is a Shopify default and may differ from the brand's actual error styling.
- Dark mode is not present in the extracted data; the brand may not support it.
- Sub-brand or product-line-specific palettes (e.g., for "Pure" vs "Pro" product lines) are not captured.
- The meta theme-color of #ffffff suggests the brand prefers a white browser chrome, but this may vary by page or section.
