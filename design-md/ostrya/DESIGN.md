---
version: alpha
name: "Ostrya"
source_url: "https://ostryaequipment.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A dark, weather-bitten canvas for outdoor equipment, where #1c1b1b ink swallows most of the screen and #4469af — a cold, alpine blue — cuts through as the single primary voltage. The site reads like a field notebook: body text in Open Sans at 16px sits on #f2f2f2 surface-soft panels, while #363636 muted text and #d9d9d9 hairline strokes keep hierarchy crisp without shouting. Product imagery dominates — the brand trusts full-bleed hero shots of tents and packs against #121212 backgrounds, letting gear speak over copy. Buttons carry {rounded.sm} corners and the primary blue (#4469af) flips to #c8232c (a sharp red) for sale badges and urgency markers, a two-tone system that feels like trail signage. The typography stack leans on Unica77LLWeb-Regular for display — a clean, Swiss-inspired sans that avoids outdoor-brand cliché — with monospace for technical specs. There is no gradient, no glassmorphism, no decorative flourish; every pixel earns its place through utility. The footer collapses into a single column of #a1a1a1 links on #1c1b1b, and the cart drawer uses #ff2626 for remove actions, a red that matches the urgency of a forgotten stove. This is a system built for people who read weather reports and pack by weight — not for browsing.

colors:
  primary: "#4469af"
  primary-active: "#286ef8"
  primary-disabled: "#a1a1a1"
  ink: "#1c1b1b"
  body: "#363636"
  muted: "#696969"
  muted-soft: "#a1a1a1"
  hairline: "#d9d9d9"
  hairline-soft: "#e2e2e2"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-badge: "#c8232c"
  sale-badge-text: "#ffffff"
  danger: "#ff2626"
  danger-soft: "#ffdede"
  accent-yellow: "#fff300"
  accent-green: "#307a07"
  accent-green-soft: "#d2e4c4"
  social-blue: "#00aced"
  social-blue-soft: "#4fc3f7"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Unica77LLWeb-Regular', 'Unica77LLSub-Regular', 'Open Sans', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Unica77LLWeb-Regular', 'Unica77LLSub-Regular', 'Open Sans', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  monospace:
    fontFamily: "Consolas, 'Liberation Mono', Menlo, Monaco, 'SF Mono', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

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
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
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
    border: "2px solid {colors.danger}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    objectFit: "cover"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "0 {spacing.base} {spacing.base}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    minHeight: "480px"
  hero-overlay:
    backgroundColor: "rgba(28, 27, 27, 0.4)"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  social-icon:
    color: "{colors.social-blue}"
    size: "24px"
  social-icon-hover:
    color: "{colors.social-blue-soft}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 36px
  cart-item-remove:
    color: "{colors.danger}"
    typography: "{typography.caption}"
    cursor: "pointer"
  cart-item-remove-hover:
    color: "{colors.sale-badge}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and primary form submissions. Renders as a solid #4469af rectangle with white uppercase text at 14px/600 weight. On hover, shifts to #286ef8; disabled state drops to #a1a1a1. All variants share {rounded.sm} and 44px height.

**`button-secondary`** — Outline variant for secondary actions like "View Details" or "Continue Shopping". White background with a 2px #1c1b1b border and matching ink text. Active state fills to #f2f2f2 surface-soft. Maintains the same 44px height and uppercase typography as primary.

**`button-danger`** — Destructive action button for cart removals and account deletions. Uses #ff2626 fill with white text, matching the urgency red found in cart remove links. Shares same dimensions and typography as primary.

### Cards
**`product-card`** — The core product display unit, a white card with {rounded.md} corners and no border — relies on shadow from surrounding layout. Contains a full-width product image with top-rounded corners, a title in 16px/600 Open Sans, and a price in 16px/400 body weight. Sale items overlay a {colors.sale-badge} badge in the top-left corner.

### Navigation
**`nav-bar`** — Fixed top navigation at 72px height with a white background and a single #d9d9d9 hairline bottom border. Links render in 14px/600 uppercase Open Sans. On scroll, gains a subtle box-shadow. The logo sits left-aligned; primary nav links center; utility links (search, cart, account) right-align.

**`search-bar`** — A pill-shaped input with {rounded.full} and a 1px #d9d9d9 border. On focus, the border thickens to 2px and shifts to #4469af. Uses 16px body text for query entry. Sits in the nav bar on desktop; expands to full-width on mobile.

### Forms
**`text-input`** — Standard form input with white background, 1px #d9d9d9 border, and {rounded.sm} corners. Focus state swaps to a 2px #4469af border. Error state uses a 2px #ff2626 border. Height is 48px with 12px/16px padding for comfortable touch targets.

### Footer
**`footer`** — Full-width dark section on #1c1b1b background with #a1a1a1 link text. Links hover to white. Content stacks in a single column on mobile, multi-column on desktop. Includes social icons in #00aced with hover shift to #4fc3f7.

### Badges & Tags
**`sale-badge`** — Small #c8232c rectangle with white uppercase 11px/700 text, {rounded.xs} corners, and 2px/8px padding. Overlaid on product card images for sale items. The red matches the urgency accent found in cart remove actions.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; footer stacks vertically; search bar expands full-width below nav; hero text reduces to 24px |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; footer splits into two columns; hero maintains 36px display |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; footer in four columns; hero at full height with 36px display |
| Wide | > 1440px | Max-width container at 1440px; product grid can show four columns; hero scales proportionally |

### Touch Targets
- All buttons and interactive elements minimum 44px height (WCAG AAA compliant)
- Text inputs at 48px height for comfortable touch entry
- Nav links have minimum 44px tap area even when text is smaller
- Cart quantity selectors at 36px height — borderline, but consistent with compact cart layout
- Social icons at 24px with 44px tap padding

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product grid reduces from 3 columns to 2 at tablet, 1 at mobile
- Footer column count drops from 4 to 2 at tablet, 1 at mobile
- Hero overlay text reduces font size below 744px
- Search bar moves from nav bar to full-width below nav on mobile
- Accordion-style product details replace tabbed layout below 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components were inferred from common patterns; extracted CSS may not reflect exact brand implementations
- Error state styling for forms (colors, icons, messaging) was not reliably extracted from the live site
- Dark mode preferences or alternate color schemes were not detected
- Sub-brand or seasonal color palettes (e.g., limited edition collections) are not represented
- Animation durations, easing curves, and transition properties were not extracted
- The extracted hex list includes many grays and blues that may be Shopify defaults or stock image tones — the true brand palette may be narrower than listed
- Specific font weights for Unica77LLWeb-Regular beyond 400 were not confirmed; all display text assumes weight 400
- Product card shadow depth and spread values were not extractable from static CSS
- Checkout flow styling (Shopify checkout override) was not analyzed
- Mobile navigation drawer animation and overlay behavior were not captured
- The #c62828 and #cb2b2b reds in the extracted list may be alternate sale/danger variants but their usage context is unclear
- #e4c4c4 and #c0c0c0 may be legacy or unused colors — included in extraction but not assigned to components
