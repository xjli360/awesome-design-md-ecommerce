---
version: alpha
name: "Renegade Game Studios"
source_url: "https://renegadegamestudios.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A board game publisher whose visual identity leans into the dark, saturated end of the tabletop spectrum — deep ink (#1a1a2e) as the default canvas, with primary voltage supplied by a vivid cobalt (#1990c6) that reads as both approachable and competitive. The site trusts high-contrast product photography against near-black backgrounds, letting box art and component shots do the heavy lifting over decorative illustration. Typography runs a clean sans-serif stack at moderate weights — display sizes hover around 28–32px in weight 600, never competing with the game imagery for attention. Navigation is lean: a single row of game-series dropdowns, a search icon, and a cart badge, all sitting on the dark canvas without a visible hairline separator. Buttons use the cobalt primary with white text and a modest {rounded.sm} corner, while product cards adopt a slightly lighter surface (#16213e) to lift the box art without breaking the dark envelope. The overall effect is a storefront that feels like a game table at dusk — focused, slightly dramatic, and built to let the product speak.

colors:
  primary: "#1990c6"
  primary-active: "#1473a0"
  primary-disabled: "#4a8ba8"
  ink: "#1a1a2e"
  body: "#e0e0e0"
  muted: "#8899aa"
  muted-soft: "#556677"
  hairline: "#2a2a3e"
  hairline-soft: "#222233"
  canvas: "#1a1a2e"
  surface-soft: "#16213e"
  surface-card: "#16213e"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-gold: "#d4a843"
  accent-red: "#c0392b"
  accent-green: "#27ae60"
  star-rating: "#d4a843"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.25px
  badge:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  link:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.25px

rounded:
  none: 0px
  xs: 2px
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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-icon-square:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-dropdown-trigger:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
    rounded: "{rounded.sm}"
  nav-dropdown-menu:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 8px 0
  search-icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
    padding: 0 6px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-rating:
    color: "{colors.star-rating}"
    typography: "{typography.caption}"
    padding: "0 {spacing.base} {spacing.base}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  section-header:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.display-md}"
    padding: "{spacing.xl} 0 {spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.body}"
  badge-new:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-in-stock:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  filter-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    padding: "0 8px"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand cobalt {colors.primary} with white text. Used for "Add to Cart", "Pre-Order", and "Shop Now" actions. On hover, shifts to {colors.primary-active} for a darker, more committed state. Disabled state uses {colors.primary-disabled} to signal inactivity without losing brand recognition.

**`button-secondary`** — An outlined-style button on the dark canvas, using {colors.surface-card} background with {colors.primary} text. Appears in filter bars, "Learn More" links, and secondary purchase paths. Maintains the same 44px height and {rounded.sm} corners as the primary for visual consistency.

**`button-tertiary-text`** — A text-only button with no background, used for "Cancel", "Clear Filters", and "View All" links within content sections. Relies on {colors.primary} for color to remain clickable without competing with primary CTAs.

**`button-icon-square`** — A compact square button for icon-only actions like search, menu toggle, and social links. Uses {colors.surface-card} background and {colors.body} text, with a 40px square footprint and {rounded.sm} corners.

### Navigation
**`top-nav`** — A fixed-height 64px bar on the dark {colors.canvas} background. Contains game-series dropdown triggers, a search icon button, and a cart badge. No visible bottom border — the nav floats on the dark canvas without a hairline separator.

**`nav-dropdown-trigger`** — A text label with a small chevron icon, styled in {typography.nav-link}. On hover, reveals the dropdown menu. Padding of 8px 12px keeps the click target comfortable.

**`nav-dropdown-menu`** — A flyout panel with {colors.surface-card} background, {rounded.md} corners, and 8px vertical padding. Contains game series links in {typography.body-sm}. Appears below the trigger with no offset gap.

**`search-icon-button`** — A 40px square icon button in the top nav. On click, expands into a full search overlay or inline input. Transparent background keeps it integrated with the nav bar.

**`cart-badge`** — A small pill-shaped indicator showing item count, positioned on the cart icon. Uses {colors.primary} background with white text in {typography.badge} (11px uppercase). Minimum 20px width ensures single-digit counts look centered.

### Cards
**`product-card`** — A dark card on {colors.surface-card} background with {rounded.md} corners and zero internal padding. The card itself is a container — all spacing comes from child elements. Box art fills the top with rounded top corners, then title, price, and rating stack below.

**`product-card-image`** — The top region of the product card, with rounded corners only at the top ({rounded.md} top-left and top-right). The image fills full width with no padding, letting the box art bleed edge-to-edge.

**`product-card-title`** — Game title in {typography.title-sm} (14px, weight 600), padded with {spacing.sm} top and {spacing.base} sides. Keeps the name close to the image while leaving breathing room.

**`product-card-price`** — Price displayed in {typography.body-md} with {colors.primary} color for visual emphasis. Padded with {spacing.base} on sides and bottom.

**`product-card-rating`** — Star rating and review count in {typography.caption}, using {colors.star-rating} (gold) for the stars. Padded with {spacing.base} on sides and bottom.

### Forms
**`text-input`** — A standard text input on {colors.surface-card} background with a 1px {colors.hairline} border. On focus, the border switches to {colors.primary} for clear active state. 44px height matches button height for form alignment.

**`select-dropdown`** — A styled select element matching the text input in height, padding, and border treatment. Uses {colors.surface-card} background with {colors.body} text in {typography.body-sm}.

**`quantity-selector`** — A compact 40px-high control for adjusting item quantities in the cart. Uses {colors.surface-card} background with {rounded.sm} corners. Contains minus/plus buttons flanking the current value.

### Badges
**`badge-new`** — A gold badge on {colors.accent-gold} background with dark text, used for "New Release" tags on game cards. Small {rounded.xs} corners and tight 2px 8px padding keep it unobtrusive.

**`badge-sale`** — A red badge on {colors.accent-red} background with white text, used for "Sale" or "Clearance" indicators. Same sizing as the new badge for visual consistency.

**`badge-in-stock`** — A green badge on {colors.accent-green} background with white text, used for availability indicators on product detail pages.

### Filters
**`filter-chip`** — A pill-shaped filter option in {rounded.full} with {colors.surface-card} background and {colors.body} text. Used in category and game-series filter bars. Active state switches to {colors.primary} background with white text.

**`filter-chip-active`** — The selected state of a filter chip, using {colors.primary} background for clear visual distinction from inactive chips.

### Hero
**`hero-section`** — The full-width hero area on the homepage, using the dark {colors.canvas} background with large display typography. Contains a headline, optional subheading, and a hero CTA button. Padding of {spacing.section} top/bottom and {spacing.lg} sides.

**`hero-cta`** — A larger variant of the primary button for hero sections, with 14px 32px padding and 48px height for greater visual weight. Uses the same {colors.primary} background and {rounded.sm} corners.

### Footer
**`footer`** — A full-width footer on the deepest {colors.ink} background with {colors.muted} text. Contains link columns, social icons, and legal text. Padding of {spacing.xxl} top/bottom and {spacing.lg} sides.

**`footer-link`** — Standard footer link in {colors.muted} with {typography.link}. On hover, shifts to {colors.body} for readability.

### Dividers and Loading
**`divider`** — A 1px horizontal rule in {colors.hairline} for separating content sections. Used between product cards, in dropdown menus, and in the footer.

**`divider-soft`** — A subtler 1px rule in {colors.hairline-soft} for lighter visual separation within cards or sidebars.

**`loading-spinner`** — A 24px spinning indicator in {colors.primary} for async content loading. Used on product listing pages and during checkout transitions.

**`tooltip`** — A small dark tooltip on {colors.ink} background with {colors.body} text in {typography.caption}. {rounded.sm} corners and 4px 8px padding for compact information display.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card wide), hamburger menu replaces top nav dropdowns, hero section reduces to 48px padding, filter chips stack vertically, footer collapses to single column |
| Tablet | 744–1128px | Two-column product grid (2 cards wide), top nav dropdowns remain but with reduced padding, hero section at 56px padding, filter chips wrap in a 2-row strip |
| Desktop | 1128–1440px | Three-column product grid (3 cards wide), full top nav with dropdowns, hero section at 64px padding, filter chips in a single horizontal row |
| Wide | > 1440px | Four-column product grid (4 cards wide), max-width container at 1440px, hero section at 80px padding, additional whitespace around product cards |

### Touch Targets
- All interactive elements (buttons, links, chips) maintain a minimum 44px height for touch accessibility
- Icon buttons are 40px × 40px, meeting the 44px touch target with 2px internal padding
- Filter chips are 32px tall — below the 44px recommendation, but acceptable for desktop filter bars where precision is higher
- Cart badge is 20px tall — a known accessibility gap, mitigated by the parent icon button providing the touch target
- Dropdown triggers have 8px 12px padding, creating a ~30px × 40px touch area on mobile

### Collapsing Strategy
- Top nav dropdowns collapse into a hamburger menu on mobile (< 744px), with the menu panel sliding in from the left
- Product grid collapses from 4 columns (wide) → 3 (desktop) → 2 (tablet) → 1 (mobile)
- Hero section padding reduces from 80px (wide) to 48px (mobile), with text size dropping from {typography.display-lg} to {typography.display-md}
- Filter chips collapse from a single horizontal row (desktop) to a vertical stack (mobile) with a "Filters" toggle button
- Footer link columns collapse from 4 columns (desktop) to a single vertical list (mobile) with expandable section headers
- Search expands from an icon button to a full-width input bar on mobile, overlaying the top nav

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted hex colors were available from the live site — the color palette above is inferred from the brand's visual identity (dark canvas, cobalt accent) and common tabletop game publisher conventions. True brand colors should be verified against the live site's CSS.
- No font-family declarations were extracted — the typography stack uses Inter as a reasonable sans-serif choice for a modern board game publisher. The actual brand font may differ.
- Hover and focus states for most components are not confirmed from live data — the active/disabled variants provided are best guesses based on common dark-theme patterns.
- Error styling for form inputs (validation errors, error messages) is not documented — the text-input focus state is provided, but error borders and helper text styling need verification.
- Dark mode is not applicable — the site already uses a dark canvas as its default theme.
- Sub-brand or game-series-specific color variations (e.g., special edition badges, franchise-specific accents) are not captured.
- Animation and transition timings (hover fade, dropdown slide, modal entrance) are not specified — the site likely uses 150–300ms ease transitions, but exact values need extraction.
- The star rating color ({colors.accent-gold}) is an assumption — actual rating stars may use a different gold or yellow.
- The footer link hover color ({colors.body}) is a reasonable guess — the actual hover state may use {colors.primary} or another accent.
- The loading spinner size and color are not confirmed — 24px and {colors.primary} are common patterns for dark-themed sites.
- Tooltip positioning (top, bottom, with arrow) and animation are not documented.
