---
version: alpha
name: "Pwnage"
source_url: "https://pwnage.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A performance-gaming brand that signals its precision through a high-voltage blue (#3561ff) — the meta theme-color and the single electric accent that charges every primary button, link, and badge across a near-monochrome canvas of deep charcoal (#232527, #1c1d1f) and cool white (#fafdff). The brand lives in a world of soft surfaces: cards and buttons carry gentle radii ({rounded.sm}–{rounded.md}), while the typography runs Outfit at clean weights — display heads sit at 500–600 rather than the aggressive 700+ common in gaming, suggesting a mature, tool-like confidence. A secondary accent of vivid cyan (#1dfef2) and a warning yellow (#ffd900) appear sparingly, reserved for stock indicators and sale flags. The extracted palette reveals a heavy reliance on near-blacks (#252525, #121212) and cool grays (#e9ecee, #d3d7d9, #8d9398) that frame product photography — mice, keyboards, and accessories — as the hero. The brand's voice is technical but not cold: the blue (#3561ff) is the same shade used in engineering schematics and precision instruments, and the layout leans on generous whitespace and centered product grids rather than dense, information-heavy modules. The single most distinctive design move is the pairing of a bright, saturated primary with a near-black body — a high-contrast system that reads as both premium and functional, closer to tool design than esports spectacle.

colors:
  primary: "#3561ff"
  primary-active: "#2b6ae0"
  primary-disabled: "#899df1"
  ink: "#232527"
  body: "#1c1d1f"
  muted: "#8d9398"
  muted-soft: "#d3d7d9"
  hairline: "#dedede"
  hairline-soft: "#e9ecee"
  canvas: "#fafdff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#1dfef2"
  accent-yellow: "#ffd900"
  accent-purple: "#8500ff"
  error: "#ff3939"
  surface-dark: "#252525"
  surface-darker: "#121212"
  surface-charcoal: "#232527"

typography:
  display-xl:
    fontFamily: "'Outfit', -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Outfit', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Outfit', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Outfit', -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Outfit', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Outfit', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Outfit', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Outfit', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Outfit', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Outfit', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Outfit', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Outfit', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Outfit', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Outfit', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Outfit', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
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
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.error}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
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
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-sold-out:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  badge-new:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-preorder:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  icon-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 0 0 16px 0

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, filled with the brand's electric blue (#3561ff) and white text. Used for "Add to Cart", "Pre-Order", and primary checkout flows. On hover, shifts to a deeper blue (#2b6ae0). Disabled state uses a muted blue (#899df1) with reduced opacity feel.

**`button-secondary`** — A white-filled button with dark text for secondary actions like "View Details" or "Learn More". The outline variant uses a transparent background with a dark border, maintaining the same 44px height and {rounded.sm} corners for visual consistency.

**`button-ghost`** — A text-only button with no background, using the primary blue for text color. Used for "Cancel", "Clear Filters", and inline actions where a full button would be too heavy.

**`button-pill-primary`** — A compact, fully rounded variant of the primary button, used for filter tags, category pills, and small CTAs. The pill shape ({rounded.full}) distinguishes it from the standard {rounded.sm} primary button.

### Cards
**`product-card`** — The core product display unit, a white card with {rounded.md} corners containing a product image, title, price, and optional badges. The image area uses the same corner radius, creating a clean, contained visual. Cards sit on a soft gray surface (#f6f6f6) or white canvas, with consistent spacing between grid items.

**`product-card-badge`** — Small, uppercase labels overlaid on product images. Yellow (#ffd900) for sale items, cyan (#1dfef2) for new arrivals, purple (#8500ff) for pre-orders. Each uses {rounded.xs} and tight padding to sit unobtrusively in the top-left corner of the product image.

### Navigation
**`nav-bar`** — A fixed 64px header on white background, containing the logo, product category links in uppercase Outfit 500, a search icon, and a cart icon. Active nav links use the primary blue; inactive links use muted gray (#8d9398). On scroll, a subtle hairline (#dedede) appears at the bottom.

**`nav-link-active` / `nav-link-inactive`** — Uppercase navigation links with 0.2px letter spacing. Active state uses primary blue (#3561ff) with no underline or background — the color alone signals the current section.

### Forms
**`text-input`** — Standard input fields with white background, dark text, and {rounded.sm} corners. Focus state adds a primary blue border. Error state uses red (#ff3939) for the border and text. Height is consistent at 44px to match button height for aligned form rows.

**`quantity-selector`** — A compact input group for adjusting product quantities, with minus/plus buttons flanking a centered number. Uses {rounded.sm} and matches the 40px height of icon buttons for inline alignment.

### Search
**`search-bar`** — A fully rounded search input ({rounded.full}) with a magnifying glass icon, placeholder text, and a 48px height. Used in the mobile menu and on search-focused pages. The pill shape distinguishes it from standard text inputs and signals a more casual, exploratory interaction.

### Footer
**`footer`** — A dark section using the brand's near-black (#232527) as background with white text. Links use the muted gray (#d3d7d9) for a softer contrast. The footer contains columns for product categories, support links, and social icons, with generous padding ({spacing.section}) top and bottom.

### Badges
**`badge-new`** — Cyan (#1dfef2) background with dark text, used to flag newly released products. The high-contrast cyan stands out against both white and dark surfaces, creating a "fresh" visual signal.

**`badge-sale`** — Yellow (#ffd900) background with dark text, used for discounted items. The warm yellow creates urgency without the aggression of red.

**`badge-preorder`** — Purple (#8500ff) background with white text, used for upcoming products available for pre-order. The purple sits between the primary blue and accent cyan in the brand's accent hierarchy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces top nav, search bar collapses to icon, footer stacks vertically, hero section reduces padding to {spacing.xl} |
| Tablet | 744–1128px | Two-column product grid, top nav shows limited links with "More" dropdown, search bar remains full-width in header, footer displays two-column layout |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all category links, search bar integrated into header, footer shows four-column layout |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centers content, hero section uses larger display-xl type, additional whitespace around product cards |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Icon buttons use 40px diameter circles with 24px icons inside
- Nav links have 48px tap targets (padding extends beyond text)
- Product card CTAs are full-width on mobile for easy tapping

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Footer collapses from 4 columns to stacked single column below 744px
- Hero section reduces type size from display-xl to display-lg on tablet, display-md on mobile
- Search bar collapses to icon-only trigger on mobile, expanding to full-width overlay on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were inferred from the extracted palette; actual transition durations and shadow values are unknown
- Error state styling (red #ff3939) was extracted but form validation patterns (success states, helper text, character counts) are not documented
- The extracted color list includes many near-blacks and grays that may represent Shopify theme defaults rather than intentional brand choices — the true brand palette may be more limited
- Dark mode styling is not present in the extracted data; the brand may not support it
- Typography scale (font sizes, weights, line heights) was estimated from the single extracted font-family (Outfit) and common gaming-brand patterns; actual values may differ
- Component spacing (padding, margins) was inferred from common e-commerce patterns and may not match the live site exactly
- The accent colors (cyan #1dfef2, yellow #ffd900, purple #8500ff) were extracted but their exact usage contexts (which badge types, hover states, etc.) are speculative
- No animation or transition timing data was extracted
- The brand's icon system (cart, search, hamburger, social icons) is not documented — only the container styles are captured
- Product card hover states (elevation, border changes) are unknown
- The checkout flow uses Shopify's default styling, which may differ from the brand's design system
