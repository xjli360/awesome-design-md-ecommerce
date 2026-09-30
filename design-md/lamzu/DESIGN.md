---
version: alpha
name: "Lamzu"
source_url: "https://lamzu.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-octane gaming peripherals brand that uses #039aff as its primary voltage — an electric cyan-blue that reads more like a neon tube sign than a conventional brand color, appearing on every primary CTA, product-highlight badge, and the site's meta theme-color bar. The palette is otherwise aggressively monochromatic: #141414, #121212, and #323232 for backgrounds and ink, with #444444 and #dedede for body and muted text, creating a dark-mode-first canvas that lets the cyan-blue pop like a laser sight. Red accents (#d21625) appear sparingly on sale badges and limited-edition markers, while #ffff00 (a pure yellow) surfaces on discount callouts, giving the brand a three-color accent system that feels arcade-born. Typography runs on Poppins at 500–700 weight for display and body, with Prompt used for select hero headlines — both geometric sans-serifs that carry the precision of esports overlays. Buttons use {rounded.sm} corners (8px) rather than pill shapes, a deliberate choice that signals performance over friendliness; product cards adopt {rounded.md} (12px) for a slightly softer containment. The nav bar is a fixed 64px strip of #121212 with cyan underline indicators, and the footer collapses into a dense, link-heavy grid on #141414. Every surface is matte — no gradients, no glassmorphism, no decorative flourishes — just raw contrast between near-black backgrounds and the cyan signal.

colors:
  primary: "#039aff"
  primary-active: "#0280d4"
  primary-disabled: "#7fcbff"
  ink: "#121212"
  body: "#444444"
  muted: "#969595"
  muted-soft: "#989898"
  hairline: "#323232"
  hairline-soft: "#444444"
  canvas: "#141414"
  surface-soft: "#1a1a1a"
  surface-card: "#1e1e1e"
  on-primary: "#ffffff"
  accent-red: "#d21625"
  accent-yellow: "#ffff00"
  badge-sale: "#d21625"
  badge-new: "#039aff"
  badge-discount: "#ffff00"
  star-rating: "#ffff00"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Prompt', Poppins, 'Segoe UI', Roboto, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Prompt', Poppins, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
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
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
  button-pill-cyan:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    border: "1px solid {colors.primary}"
  icon-button-circle:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.primary}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-discount:
    backgroundColor: "{colors.badge-discount}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 14px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.accent-red}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  checkbox:
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    checkedBackground: "{colors.primary}"
    checkedBorder: "2px solid {colors.primary}"
  radio:
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.full}"
    checkedBorder: "2px solid {colors.primary}"
    checkedDot: "{colors.primary}"
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    toggleActive: "{colors.primary}"
    knobColor: "{colors.on-primary}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary action button across the site, filled with {colors.primary} cyan and white text using {typography.button-md}. On hover, it shifts to {colors.primary-active} (#0280d4) for a slightly deeper blue. Disabled state uses {colors.primary-disabled} (#7fcbff) to indicate non-interactivity while preserving brand recognition.

**`button-secondary`** — An outlined variant with transparent background, {colors.primary} text, and a 2px solid border in the same cyan. On hover or active, it fills with {colors.primary} and white text, matching the primary button's active state. Used for secondary CTAs like "Learn More" or "Compare."

**`button-tertiary-text`** — A text-only button with no background or border, using {colors.primary} text. Hover state shifts to {colors.primary-active}. Used for inline actions like "View Details" or "Cancel."

**`button-pill-cyan`** — A fully rounded pill variant of the primary button, using {typography.button-sm} for tighter spacing. Used for filter tags, category toggles, and compact CTAs. The outline variant (`button-pill-outline`) swaps to transparent background with a 1px cyan border.

**`icon-button-circle`** — A 40px circular button with {colors.surface-card} background and a {colors.primary} icon. Used for cart, search, and menu toggles in the nav bar. Hover state adds a subtle {colors.primary} border.

### Navigation
**`top-nav`** — A fixed 64px bar on {colors.ink} (#121212) background, containing the logo, nav links, and icon buttons. Nav links use {typography.nav-link} in uppercase with 0.5px letter-spacing. Active links display a 2px {colors.primary} underline indicator. The nav collapses to a hamburger menu on mobile.

**`nav-link-active`** — Active navigation link styled with {colors.primary} text and a 2px bottom border in the same cyan. Inactive links (`nav-link-inactive`) use {colors.muted} (#969595) text with no underline.

### Cards
**`product-card`** — A product listing card on {colors.surface-card} (#1e1e1e) background with {rounded.md} corners and {spacing.base} padding. On hover, a 1px {colors.primary} border appears. The title uses {typography.title-sm} in white, while the price is rendered in {colors.primary} using {typography.body-md}. Badges overlay at the top-left corner.

**`product-card-title`** — Product name styled with {typography.title-sm} and white text for maximum contrast against the dark card background.

**`product-card-price`** — Price display in {colors.primary} cyan using {typography.body-md}, making the cost a visual highlight on the card.

### Badges
**`badge-sale`** — A small uppercase badge on {colors.accent-red} (#d21625) background with white text, {rounded.xs} corners, and 2px/8px padding. Used for sale indicators.

**`badge-new`** — Same structure as sale badge but on {colors.primary} (#039aff) background. Used for new product markers.

**`badge-discount`** — A yellow badge on {colors.accent-yellow} (#ffff00) with dark text ({colors.ink}), used for discount percentage callouts like "-30%."

### Hero
**`hero-section`** — Full-width hero area on {colors.canvas} (#141414) background with {typography.display-xl} headlines in white. Padding is {spacing.section} (64px) vertically and {spacing.lg} horizontally. The primary CTA (`hero-cta`) is a larger 48px-tall button with 14px/32px padding.

### Footer
**`footer`** — A dense link grid on {colors.canvas} (#141414) with {spacing.xxl} vertical padding. Links use {typography.link} in {colors.muted} (#969595), shifting to {colors.primary} on hover. Section headings use {typography.title-sm} in white.

### Forms
**`text-input`** — Standard text input on {colors.surface-card} with {rounded.sm} corners, 1px {colors.hairline} border, and {typography.body-sm} text. Focus state swaps the border to {colors.primary}. Error state uses {colors.accent-red} border.

**`select-dropdown`** — Dropdown select styled identically to text inputs, with {colors.surface-card} background and {colors.hairline} border.

**`checkbox`** — Square checkbox with 2px {colors.hairline} border and {rounded.xs} corners. Checked state fills with {colors.primary} and uses a white checkmark.

**`radio`** — Circular radio button with 2px {colors.hairline} border. Checked state shows a {colors.primary} outer ring with a solid dot of the same color.

**`toggle`** — Pill-shaped toggle switch, 24px tall, with {colors.hairline} background. Active state fills with {colors.primary}, and the knob is white.

**`divider`** — A 1px horizontal line in {colors.hairline} (#323232), used between sections and list items.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked hero with centered text, footer collapses to single column, badges stack vertically |
| Tablet | 744–1128px | Two-column product grid, expanded nav with dropdowns, hero maintains full-width but reduces headline to {typography.display-lg}, footer uses 2-column grid |
| Desktop | 1128–1440px | Three-column product grid, full nav bar visible, hero uses {typography.display-xl}, footer uses 4-column grid, search bar expands |
| Wide | > 1440px | Max-width container at 1440px, four-column product grid, hero has larger padding, footer uses 4-column grid with wider spacing |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Icon buttons are 40px circles, exceeding the 44px recommendation for critical actions.
- Nav links have 48px tap targets on mobile through increased padding.
- Product cards have 100% width tap targets on mobile.

### Collapsing Strategy
- Top nav collapses to a hamburger menu below 744px, with a slide-out drawer for navigation links.
- Product grid collapses from 4 columns (wide) to 1 column (mobile), with 2 columns at tablet.
- Footer link columns collapse from 4 to 1, stacking vertically on mobile.
- Hero section reduces headline size and centers content on mobile.
- Badges on product cards stack vertically on mobile to avoid overlap.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors are heavily weighted toward dark-mode defaults and may include Shopify checkout widget colors (Klarna, Afterpay) that are not part of the brand palette. The distinctive cyan (#039aff), red (#d21625), and yellow (#ffff00) are confirmed brand accents.
- Font-family declarations were limited to Poppins, Prompt, and generic fallbacks. Exact font weights and sizes for all typography tokens are inferred from common gaming-peripheral design patterns and may not match the live site exactly.
- Hover, focus, and active states for all components are inferred from the primary color and standard interaction patterns; actual extracted data was not available.
- Error, success, and warning form states beyond the red error border are not confirmed.
- Dark mode is the default (and only observed) theme; no light mode palette was extracted.
- Sub-brand or limited-edition color palettes (e.g., for special edition mice) are not captured.
- Animation durations, easing curves, and transition properties were not extracted.
- Dropdown menus, tooltips, modals, and toast notifications were not observed in the extracted data.
- The exact Shopify theme structure may introduce additional components (cart drawer, product variant selector) not documented here.
