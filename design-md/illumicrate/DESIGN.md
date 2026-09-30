---
version: alpha
name: "Illumicrate"
source_url: "https://www.illumicrate.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A gilded, bibliophilic subscription brand where the primary voltage is not a single hex but a duet — the deep, almost-ink black of #1c1c1c against the warm gold of #fada4a, a pairing that reads as both premium and magical. The palette draws from the alchemy of a book's edge: #f2a63b (a secondary amber), #700f5f (a crushed-velvet plum), and #f3a4bb (a blush pink) appear as accent badges, foil-stamped details, and exclusive-edition treatments. The canvas is #f4f4f6, a soft off-white that avoids the sterile glare of pure white, while #e5e5eb and #d3d4dd serve as hairline borders and muted dividers. Type is set in Beirut Display for headlines — a serif with a theatrical, almost editorial weight — paired with Labil Grotesk for body and UI, a clean sans-serif that keeps the reading experience grounded. The brand's signature design move is the foil-stamped badge: a small, rounded rectangle (`{rounded.sm}`) in gold or plum, carrying a single word like "EXCLUSIVE" or "SIGNED" in uppercase, applied to product cards and hero banners. The overall mood is that of a curated library — dark shelves (`{colors.ink}`), warm lamp-light (`{colors.primary}`), and the tactile promise of a hand-picked monthly delivery. There is no hard corner on a button (`{rounded.sm}`), but the typography retains a sharp, authoritative serif for display, creating a deliberate tension between softness and tradition.

colors:
  primary: "#fada4a"
  primary-active: "#f2a63b"
  primary-disabled: "#e5e5eb"
  ink: "#1c1c1c"
  body: "#272d45"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#d3d4dd"
  hairline-soft: "#e5e5eb"
  canvas: "#f4f4f6"
  surface-soft: "#f7f7f8"
  surface-card: "#ffffff"
  on-primary: "#1c1c1c"
  accent-plum: "#700f5f"
  accent-blush: "#f3a4bb"
  accent-amber: "#f2a63b"
  badge-gold: "#fada4a"
  badge-plum: "#700f5f"
  badge-amber: "#f2a63b"
  error: "#c01616"
  success: "#0b853e"
  star-rating: "#fada4a"

typography:
  display-xl:
    fontFamily: "'Beirut Display', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Beirut Display', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Beirut Display', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Beirut Display', Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Labil Grotesk', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Labil Grotesk', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Labil Grotesk', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Labil Grotesk', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Labil Grotesk', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Labil Grotesk', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'Labil Grotesk', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Labil Grotesk', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Labil Grotesk', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.3px
  link:
    fontFamily: "'Labil Grotesk', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Labil Grotesk', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
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
    textColor: "{colors.muted}"
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
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-gold:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-badge:
    backgroundColor: "{colors.badge-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-plum:
    backgroundColor: "{colors.badge-plum}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-accent:
    backgroundColor: "{colors.accent-plum}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 12px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.primary}"
  badge-exclusive:
    backgroundColor: "{colors.badge-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-signed:
    backgroundColor: "{colors.badge-plum}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  subscription-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  subscription-card-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "2px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with gold (#fada4a) and black text. Used for "Subscribe Now", "Add to Cart", and "Join Waitlist". On hover, shifts to amber (#f2a63b). Disabled state uses the muted gray #e5e5eb with muted text. Height is 44px with 12px/24px padding and 8px corner radius.

**`button-secondary`** — An outlined variant on a white or soft canvas background, with a 1px hairline border (#d3d4dd). Active state swaps the border to ink (#1c1c1c). Used for "Learn More" and "View Details" actions.

**`button-tertiary-text`** — A text-only button with no background or border. Used for "Cancel" or "Back to Browsing" links within modals or forms. Inherits the ink color and button-md typography.

**`button-pill-gold`** — A fully rounded pill button in gold, used for promotional badges or "Shop Now" links on hero banners. Uses button-sm typography and 8px/20px padding.

### Cards
**`product-card`** — A white card with 8px rounded corners, no padding on the container (padding is applied to child elements). The image area has rounded top corners (8px 8px 0 0). Badges (gold, plum, or amber) sit over the image in the top-left corner with 4px corner radius and uppercase 10px type. Title uses title-sm, price uses body-md with xs/base/base padding.

**`subscription-card`** — A larger card with 12px rounded corners and 24px padding, used for plan selection. Active state has a 2px gold border. Contains plan name, price, features list, and a CTA button.

### Navigation
**`top-nav`** — A 72px tall bar with soft canvas background and a 1px bottom border in hairline-soft (#e5e5eb). Nav links are uppercase, 14px, weight 600, with 0.5px letter spacing. Active link has a 2px gold underline. Inactive links are muted (#676986).

**`nav-link-active`** — Bold ink color with a 2px gold bottom border. Used for the current page or section.

**`nav-link-inactive`** — Muted gray (#676986) with no underline. Hover state transitions to ink.

### Forms
**`search-bar`** — A 44px tall input with 8px rounded corners, 1px hairline border, and 10px/16px padding. On focus, the border switches to ink (#1c1c1c). Uses body-sm typography.

**`quantity-selector`** — A 40px tall input with 8px rounded corners, 1px hairline border, and 8px/12px padding. Used for cart quantity adjustments. Contains increment/decrement buttons on either side.

### Badges
**`badge-exclusive`** — Gold background (#fada4a) with black text. Used for "EXCLUSIVE" or "SPECIAL EDITION" labels on product cards and hero banners.

**`badge-signed`** — Plum background (#700f5f) with white text. Used for "SIGNED" or "AUTHORED" editions.

**`badge-limited`** — Amber background (#f2a63b) with black text. Used for "LIMITED" or "LAST CHANCE" urgency labels.

### Hero
**`hero-banner`** — A full-width section with deep ink (#1c1c1c) background and white text. Uses display-xl typography (36px Beirut Display). Padding is 64px top/bottom and 32px left/right. Contains a headline, optional subheadline, and a gold accent badge.

**`hero-banner-accent`** — A small plum badge (#700f5f) with white text, 4px/12px padding, and 4px rounded corners. Used to highlight a key detail like "MONTHLY BOX" or "NEW RELEASE".

### Footer
**`footer`** — A full-width dark section with ink background and white text. Links are muted-soft (#9a9db1) and turn gold on hover. Contains newsletter signup, navigation links, and social icons.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger; product cards stack vertically; hero banner reduces to 48px padding; badges scale to 8px font; search bar becomes full-width |
| Tablet | 744–1128px | Two-column product grid; top-nav shows 4-5 links; hero banner uses 56px padding; subscription cards display in 2 columns |
| Desktop | 1128–1440px | Three-column product grid; full top-nav visible; hero banner uses 64px padding; subscription cards in 3 columns; search bar is 320px max-width |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero banner uses 80px padding; subscription cards in 4 columns |

### Touch Targets
- All buttons and interactive elements are minimum 44px height (WCAG 2.1 compliant)
- Icon buttons are 36px x 36px on mobile, 40px x 40px on desktop
- Nav links have 48px tap area (padding + link height)
- Quantity selector buttons are 40px x 40px
- Product card images are tappable with minimum 120px height

### Collapsing Strategy
- Top-nav collapses to hamburger menu at < 744px; menu slides in from the right
- Product grid collapses from 4 columns to 3 to 2 to 1 as viewport shrinks
- Subscription cards collapse from 4 columns to 3 to 2 to 1
- Hero banner text reduces from display-xl (36px) to display-lg (28px) on mobile
- Footer links collapse into a single column on mobile
- Search bar expands to full width on mobile, collapses to icon-only on very small screens (< 400px)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components are inferred from common patterns; exact transition durations and easing curves not extracted
- Error styling (input validation, form errors) not observed; error color (#c01616) is an estimate from extracted hexes
- Dark mode not present on the live site; no dark palette tokens available
- Sub-brand palettes (e.g., Illumicrate vs. Illumicrate YA vs. Illumicrate Adult) not distinguishable from extracted data
- Font weights for Beirut Display and Labil Grotesk are estimated based on common usage; exact weight values not extracted
- Letter-spacing values for display typography are estimated from common editorial serif usage
- Border radius values are estimated from extracted CSS; exact values may vary by component
- Active/disabled states for buttons are inferred; exact color values not extracted
- Star rating size (16px) is an estimate; exact dimensions not observed
- Quantity selector increment/decrement button styles not extracted
- Modal, overlay, and drawer component styles not observed
- Loading states (skeleton screens, spinners) not extracted
- Animation and transition specifications (duration, easing, keyframes) not available
