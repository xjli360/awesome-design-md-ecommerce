---
version: alpha
name: "Gymshark"
source_url: "https://gymshark.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Near-black at #121212 is Gymshark's deliberate ground — a canvas that makes athlete photography glow and the brand-blue (#007db5) arrive like a voltage spike rather than a web color. Montserrat carries every display weight: compressed letter-spacing on hero headlines, all-caps labels on category callouts, oversized numerals on sale countdowns — the type behaves like functional training equipment, no curves where straight lines will do. Roboto steps in for body copy and fine legal text, a utilitarian anchor that keeps Montserrat's assertiveness from tipping into noise. The storefront strips typical DTC warmth entirely — no rounded-corner friendliness, no pastel accent palette, no lifestyle illustration. Product grids sit flat to the grid with near-zero border-radius, and the always-dark UI reads as competitive infrastructure rather than a consumer aesthetic choice. Primary blue (#007db5) surfaces with discipline: add-to-bag buttons, email capture CTAs, loyalty enrollment — never as decoration or hover tint. Community proof is built into the layout architecture: athlete ambassador rows, macro statistics ("14M+ strong"), and social-content embeds are structural content, not social plugs bolted on at the end. The mega-menu carries sport and gender filters deep enough to need department-store navigation logic. Size-guide and fit-finder tools slide in as overlay drawers, preserving product-page context while adding decision support without a full page transition. The `{rounded.none}` posture runs almost everywhere — buttons, inputs, cards — making the rare `{rounded.xs}` treatment on loyalty badges feel like a deliberate softening rather than a default. The overall register is assertive without noise: every typographic decision runs tight tracking and controlled weight, saying performance without writing the word.

colors:
  primary: "#007db5"
  primary-active: "#005f8a"
  primary-disabled: "#004d70"
  primary-hover: "#0090cc"
  ink: "#ffffff"
  body: "#dedede"
  muted: "#888888"
  hairline: "#2d2d2d"
  hairline-soft: "#222222"
  canvas: "#121212"
  canvas-pure: "#000000"
  surface-soft: "#1a1a1a"
  surface-card: "#1e1e1e"
  surface-raised: "#252525"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale-badge: "#c0392b"
  sale-badge-text: "#ffffff"
  loyalty-gold: "#c9a84c"
  success: "#27ae60"
  error: "#e74c3c"
  scrim: "rgba(0,0,0,0.7)"

typography:
  display-xl:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: -1px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  body-md:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.1px
  category-label:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  stat-display:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 48px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -1px
  button-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  nav-label:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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
    rounded: "{rounded.none}"
    padding: 14px 24px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    opacity: 0.5
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 23px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoMaxHeight: 28px
  nav-mega-menu:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    columnHeaderTypography: "{typography.nav-label}"
    padding: "{spacing.xl} {spacing.xxl}"
    borderTop: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.category-label}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    padding: "{spacing.sm}"
    badgePosition: top-left
  product-card-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.xs}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-md}"
    minHeight: 600px
    overlayColor: "{colors.scrim}"
    textAlign: left
    padding: "{spacing.xxl} {spacing.section}"
  collection-filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline}"
    activeTextColor: "{colors.ink}"
    activeBorderColor: "{colors.primary}"
    height: 48px
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.ink}"
    unavailableTextColor: "{colors.muted}"
    unavailableTextDecoration: line-through
    height: 48px
  size-guide-drawer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    headingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    borderLeft: "1px solid {colors.hairline}"
    width: 400px
    padding: "{spacing.xl}"
  loyalty-badge:
    backgroundColor: "{colors.loyalty-gold}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  ambassador-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.title-md}"
    sportTypography: "{typography.category-label}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
  stat-block:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    numberTypography: "{typography.stat-display}"
    labelTypography: "{typography.category-label}"
    labelColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.canvas-pure}"
    textColor: "{colors.muted}"
    headingTypography: "{typography.category-label}"
    linkTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline-soft}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons
**`button-primary`** — Flat Gymshark-blue (#007db5) rectangle with zero border-radius and all-caps Montserrat at 14px/700/1px tracking. The sharp geometry is load-bearing: it signals urgency and function over warmth. Hover lifts to `{colors.primary-hover}`, active darkens to `{colors.primary-active}`, and disabled drops to 50% opacity over `{colors.primary-disabled}` — states are unambiguous without animation delay.

**`button-secondary`** — Transparent fill with a 1px `{colors.ink}` border (white) and white text on dark surfaces. Used for secondary actions such as "View All" below product grids or "Learn More" on ambassador sections. The border-forward treatment keeps the button visible without competing with the primary CTA.

**`button-ghost`** — No border, no fill, `{colors.body}` text at 14px. Reserved for low-stakes actions — "Skip" in quiz flows, "Continue Shopping" in the cart drawer — where the UI needs a tap target without visual weight.

### Text Input
**`text-input`** — Dark `{colors.surface-soft}` fill (#1a1a1a) with zero rounding and a `{colors.hairline}` border. Placeholder text renders in `{colors.muted}`. On focus, the border snaps immediately to `{colors.primary}` blue — no fade, consistent with the brand's hard-edge directness. The full-width email capture row pairs this input with a `button-primary` flush to its right edge, both at 48px height.

### Navigation
**`nav-bar`** — 60px dark bar pinned to the top of the viewport, carrying the Gymshark logo (≤28px tall), sport and gender top-level links in `{typography.nav-link}`, and icon controls for search, bag count, and account. A hairline bottom border separates it from the page without introducing a lifted-card effect. The announcement bar sits above and is persistent across all pages.

**`announcement-bar`** — 36px solid primary-blue (#007db5) strip above the nav, running `{typography.category-label}` in white. Reserved exclusively for conversion-critical messaging: discount codes, shipping thresholds, and countdown tickers. Nothing decorative occupies this real estate.

**`nav-mega-menu`** — Full-width panel in `{colors.surface-card}` dropping below the nav on hover. Organized in 4–6 columns with `{typography.nav-label}` section headers and `{typography.nav-link}` item links. Primary axes are sport, gender, fit, and collection. A featured image column on the far right highlights a current campaign drop, functioning as passive marketing within the navigation itself.

### Product Card
**`product-card`** — Sits on `{colors.surface-card}` at a 4:5 image ratio with no radius on the image block. Product name runs in `{typography.title-sm}` and price in `{typography.price-display}` below the image with `{spacing.sm}` internal padding. "SALE" badges render in `{colors.sale-badge}` red and "NEW" in `{colors.primary}` blue using `{typography.badge}`, top-left corner. On hover, a secondary colorway image cross-fades in — the only animation on the card, kept to 200ms.

**`product-card-badge`** — Zero-radius chip in red or blue depending on type. "SALE", "NEW", "BESTSELLER" at 11px uppercase Montserrat. Sits inside the image frame at the top-left corner with minimal padding, never breaking the grid edge.

### Size Selector
**`size-selector`** — Square tiles at 48px height arranged in a horizontal wrap, 1px hairline border default. Selected state upgrades border to 1px `{colors.ink}` (white). Unavailable sizes render in `{colors.muted}` with `line-through` decoration and remain tappable — clicking triggers a notify-me flow rather than a dead state.

### Hero Section
**`hero-section`** — Full-bleed photography with a `{colors.scrim}` overlay at 40% opacity for legibility. Headline runs `{typography.display-xl}` — 56px Montserrat 800, uppercase, −1px tracking. Supporting body copy in `{typography.body-md}` (Roboto 400) sits below, followed by a `button-primary` CTA with `{spacing.lg}` vertical gap. Text alignment defaults left on desktop and centers on mobile. Minimum height 600px; on mobile the image crops to portrait.

### Size Guide Drawer
**`size-guide-drawer`** — 400px panel sliding in from the right, `{colors.surface-card}` background. Heading in `{typography.display-sm}`, measurement tables and fit notes in `{typography.body-sm}`. Used for size guides, model measurement references, and fit-finder quiz results. Does not navigate away from the product page; a scrim covers the product detail behind it.

### Ambassador Card
**`ambassador-card`** — 3:4 portrait image, no radius. Athlete name in `{typography.title-md}` and sport specialism in `{typography.category-label}` (uppercase, tracked) sit below the image frame. Used in 4–6 column grids on the athlete roster page and in horizontal carousels embedded in sport-specific collection pages.

### Stat Block
**`stat-block`** — Full-width section on `{colors.canvas}`, displaying macro community metrics such as "14M+ strong". Number in `{typography.stat-display}` (48px Montserrat 800), descriptor label in `{typography.category-label}` colored in `{colors.muted}`. Three to four stats run side by side on desktop in equal-width columns.

### Collection Filter Bar
**`collection-filter-bar`** — Sticky horizontal bar below the nav on collection pages. Filter categories (Sport, Gender, Fit, Color, Size) render in `{typography.title-sm}` as horizontal chips with 48px touch height. The active filter gains a bottom border in `{colors.primary}` blue. At mobile breakpoints the bar becomes a horizontally scrollable row with no wrapping.

### Loyalty Badge
**`loyalty-badge`** — Small gold (#c9a84c) chip with a 2px `{rounded.xs}` radius — the only instance of rounding in the system outside full-circle icons. Used to mark loyalty-exclusive pricing, early-access drops, and member-only colorways. Appears on product cards, product detail pages, and the account dashboard.

### Footer
**`footer`** — Pure-black (#000000) background with a 1px `{colors.hairline-soft}` top border separating it from the canvas. Column headers in `{typography.category-label}` (uppercase, 11px, muted). Links in `{typography.body-sm}` (Roboto, 14px, muted). Newsletter capture uses the standard text-input component in a full-width row. Payment badges and legal links run in a sub-footer strip below the link columns.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero text centers and image crops to portrait; nav collapses to hamburger + bag icon; announcement bar shows one rotating message |
| Tablet | 744–1128px | 2-column product grid; mega-menu replaced with full-screen slide-in drawer nav; hero switches to 4:5 portrait crop; filter bar scrolls horizontally |
| Desktop | 1128–1440px | 4-column product grid; full mega-menu panel on hover; hero runs 16:9 landscape at full bleed; size-guide opens as right-side drawer |
| Wide | > 1440px | Max-width container at 1440px centered; side gutters appear flanking the hero image; product grid stays at 4 columns with increased card spacing |

### Touch Targets
- All buttons minimum 48px height with 44px minimum horizontal tap area
- Size selector tiles minimum 48×48px; unavailable tiles remain tappable for notify-me flow
- Nav icons (search, bag, account) maintain 44×44px tap targets at mobile breakpoints
- Collection filter chips minimum 40px height inside horizontally scrollable row

### Collapsing Strategy
- Desktop mega-menu collapses to a full-screen overlay drawer nav at tablet and below; sport/gender filters become accordion sections within the drawer
- Announcement bar condenses to a single rotating ticker on mobile from a static message on desktop
- Hero CTA stacks below the headline vertically on mobile; side-by-side text layouts only appear at desktop
- Ambassador grid collapses from 6-column to 2-column at tablet, to a horizontally scrollable strip on mobile
- Stat block collapses from 4-column to 2-column at tablet, to single stacked column at mobile
- Size-guide drawer becomes a full-height bottom sheet on mobile instead of a right-side panel

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only three hex values extracted (#dedede, #007db5, #121212); all secondary surface tones (#1a1a1a, #1e1e1e, #252525), scrim, badge colors, and loyalty gold are logically derived — not extracted from the live site
- Exact font weights and letter-spacing values for Montserrat display treatments are estimated from brand conventions; live CSS was not directly accessible at extraction time
- Nav height (60px) and announcement-bar height (36px) are approximated; Gymshark has shipped multiple nav redesigns
- Sale badge red (#c0392b) is derived, not extracted
- Loyalty program gold (#c9a84c) is inferred from Gymshark Lifting Club brand assets, not extracted from the Shopify storefront
- Product card hover timing (colorway crossfade duration, easing curve) not captured
- Icon set stroke weight and style (outlined vs. filled) not determinable from color extraction
- Dark/light mode toggle not observed; system assumed always-dark with no light-mode variant
