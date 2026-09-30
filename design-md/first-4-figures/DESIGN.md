---
version: alpha
name: "First 4 Figures"
source_url: "https://www.first4figures.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A collector's stage where premium resin and polystone statues are presented against a deep, almost theatrical darkness — #0f0f0f and #1d1d1d dominate the canvas, pushing the product photography into high-contrast spotlight. The brand's single voltage of accent color is #0693e3, a cool cyan-blue that appears on primary CTAs, navigation highlights, and the signature "Pre-order" badge, cutting through the monochrome like a museum label in a dim gallery. Typography runs Montserrat at clean, moderate weights — display headlines sit at 500–600 weight rather than heavy bold, letting the sculptural detail of each collectible do the rhetorical work. Product cards use soft corners (`{rounded.md}` ~12px) and generous padding (`{spacing.lg}` 24px) to frame each statue as an art object, while the persistent top nav stays fixed in #191919 with white text, creating a reliable anchor. The checkout flow introduces a secondary accent in #4d5bcd (a subdued indigo) for progress indicators and secondary actions, and a restrained red #ae2828 for sold-out or low-stock warnings. The overall mood is one of hushed intensity — the site treats every figure as a limited-edition artifact, and the design system exists to step back and let the collectible command attention.

colors:
  primary: "#0693e3"
  primary-active: "#0578c0"
  primary-disabled: "#7ab8e8"
  ink: "#0f0f0f"
  body: "#1d1d1d"
  muted: "#555555"
  muted-soft: "#777777"
  hairline: "#313131"
  hairline-soft: "#d9d9d9"
  canvas: "#f6f1f1"
  surface-soft: "#202020"
  surface-card: "#191919"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-indigo: "#4d5bcd"
  accent-red: "#ae2828"
  accent-orange: "#ec523e"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Work Sans', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Work Sans', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Work Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Work Sans', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Work Sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Work Sans', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Work Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Work Sans', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Montserrat', 'Work Sans', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Work Sans', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Work Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Montserrat', 'Work Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Montserrat', 'Work Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Work Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px

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
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 36px
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
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
    color: "{colors.primary}"
    marginTop: "{spacing.xs}"
  badge-preorder:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-sold-out:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-low-stock:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.on-primary}"
    marginBottom: "{spacing.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Pre-order Now", and "View Details". Rendered in the signature cyan #0693e3 with white text and a subtle 8px corner radius. On hover, shifts to a deeper #0578c0. Disabled state uses a desaturated #7ab8e8 to indicate inactivity without visual noise.

**`button-secondary`** — An outlined variant for less prominent actions like "Learn More" or "View Gallery". Uses the dark card surface #191919 as background with a 1px hairline border (#313131) and white text. Maintains the same 44px height and 12px horizontal padding as the primary button for alignment in forms.

**`button-tertiary-text`** — A text-only button for inline actions such as "Clear filters" or "Cancel". Uses transparent background with the primary cyan text color, matching the button-md typography.

**`button-pill-primary`** — A compact, fully rounded variant used for filter chips, category tags, and quick-select options. Smaller padding (8px 20px) and button-sm typography keep it unobtrusive while maintaining brand presence.

### Navigation
**`top-nav`** — A fixed header bar at 64px height, rendered in pure black (#0f0f0f) with white navigation links. The logo sits left-aligned, with primary navigation items (Shop, Pre-orders, About) centered or right-aligned. Active links shift to the primary cyan, creating a clear wayfinding signal.

**`nav-link-active`** — Uses the brand cyan for the currently active section, maintaining the same 14px/500 weight typography as inactive links for consistency.

**`nav-link-inactive`** — White text on the dark nav background, with a subtle hover state that may introduce a light opacity shift or underline.

### Product Cards
**`product-card`** — The core content container for collectible listings. Uses the dark card surface (#191919) with 12px rounded corners and 16px internal padding. Each card frames a product image with a subtle corner radius on the image itself, followed by the title in title-sm weight and the price in primary cyan.

**`badge-preorder`** — A compact label pinned to the top-left of product cards or hero images, signaling upcoming releases. Uses the primary cyan background with uppercase badge typography and 4px corners.

**`badge-sold-out`** — A red (#ae2828) badge for items no longer available, using the same structural dimensions as the preorder badge but with urgent color signaling.

**`badge-low-stock`** — An orange (#ec523e) badge for limited availability, creating a three-tier badge system (cyan = available/preorder, red = sold out, orange = low stock).

### Forms & Inputs
**`search-bar`** — A dark-themed search input with #191919 background, 1px #313131 border, and 8px rounded corners. White text at body-sm size, with placeholder text in muted gray (#555555). The 40px height keeps it compact for the nav bar or dedicated search page.

### Footer
**`footer`** — A full-width dark section (#0f0f0f) with muted gray (#777777) body text. Section headings use title-sm in white, with link items in the muted gray. Padding of 48px top/bottom and 16px sides provides breathing room for multi-column layouts (About, Support, Legal, Social links).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1–2 cards), hamburger menu replaces top nav links, search bar collapses to icon-only, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, top nav shows limited links (Shop, Pre-orders), search bar remains full-width but condensed |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links, search bar in nav, footer in 3–4 columns |
| Wide | > 1440px | Four-column product grid, max-width container (~1440px) centers content, additional whitespace on sides |

### Touch Targets
- All buttons and clickable elements maintain minimum 44px height for touch accessibility
- Icon buttons use 36px circular targets with adequate padding
- Navigation links have minimum 40px tap area
- Product card CTAs are full-width on mobile for easy tapping

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with slide-out drawer for full navigation
- Product filters collapse to a "Filter" button that opens a modal overlay on mobile
- Footer multi-column layout collapses to single-column stacked layout below 744px
- Search bar collapses to a search icon that expands to full-width input on tap (mobile)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors are heavily skewed toward dark grays and blacks (#0f0f0f, #1d1d1d, #191919, #202020, #313131) with a single distinctive cyan (#0693e3) — the palette appears intentionally monochrome with one accent, but hover/active/focus states for secondary elements are inferred
- No extracted hover states for buttons, links, or cards — primary-active and primary-disabled are estimated based on common darkening/desaturation patterns
- Font stack includes Montserrat and Work Sans as primary options, but exact hierarchy (headline vs. body) is inferred from common usage — Work Sans may be used for specific sub-sections
- No extracted data for error states, form validation styling, or loading indicators
- Shopify platform suggests possible checkout overrides (Shopify Pay buttons, Klarna badges) that may introduce colors not in the brand system — these have been excluded
- No extracted data for dark mode (site appears to already use a dark theme as default)
- Sub-brand or collection-specific palettes (e.g., limited edition statues with unique color treatments) could not be determined
- Animation durations, easing curves, and micro-interaction details are not available from static extraction
