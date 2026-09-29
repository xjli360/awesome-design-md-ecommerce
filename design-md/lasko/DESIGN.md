---
version: alpha
name: "Lasko"
source_url: "https://www.lasko.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every component on Lasko.com resolves toward function: the deep housing-navy at #171f32 anchors navigation and primary typography, the brand blue #0058a8 — locked in as the meta theme-color — handles interactive trust signals and primary CTAs, and the coral at #e25e49, warm as a resistive heating coil, punctuates promotions, urgency tags, and key conversion moments. Type runs on Assistant, a humanist sans-serif with open apertures that read cleanly at 14px body copy and scale to bold 40px hero displays without losing mechanical clarity; weight discipline is strict at 700 for headlines, 600 for subheadings, and 400 for body — no intermediate values, giving the page a hierarchy that mirrors the structured logic of a BTU rating table. Color economy is equally spare: the gray spectrum from warm off-white at #e8e8e1 through mid-grays at #f3f3f3 and #ebebeb down to hairline at #dedede forms a layered surface system in which product cards emerge from their ground in soft relief, framed by {rounded.sm} corners that signal appliance-grade construction rather than lifestyle softness. The nav bar and footer share the same #171f32 deep navy field, reversed-out white typography creating visual bookends around every page. Two accent colors earn semantic roles: the green at #00a47c marks energy-efficiency callouts and certification badges — a regulatory signal rendered in color — while the blue-slate at #334fb4 provides a middle hover-state between brand blue and deep navy without requiring custom tints. Promotional pressure channels exclusively through the coral at #e25e49: sale ribbons, urgency banners, and limited-time labels run this one warm tone against a cool-dominant palette, creating a heat-map of commercial intent across the full catalog grid.

colors:
  primary: "#0058a8"
  primary-active: "#002144"
  primary-disabled: "#acacaf"
  accent: "#e25e49"
  accent-active: "#c94535"
  eco: "#00a47c"
  navy-deep: "#171f32"
  navy-mid: "#334fb4"
  ink: "#121212"
  body: "#31373d"
  charcoal: "#3d4246"
  muted: "#acacaf"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#fafafa"
  surface-soft: "#f3f3f3"
  surface-card: "#f8f8f8"
  surface-warm: "#e8e8e1"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-accent: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Assistant', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Assistant', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Assistant', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Assistant', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Assistant', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Assistant', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Assistant', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  button-md:
    fontFamily: "'Assistant', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Assistant', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Assistant', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Assistant', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  spec-label:
    fontFamily: "'Assistant', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1px
  promo-tag:
    fontFamily: "'Assistant', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"

  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    opacity: 0.6

  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px

  button-accent-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"

  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 48px

  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: none

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 48px

  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    iconColor: "{colors.charcoal}"

  nav-bar:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px

  nav-bar-utility:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
    imageRounded: "{rounded.xs}"

  hero-banner:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    accentColor: "{colors.accent}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 480px

  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    borderActive: "2px solid {colors.primary}"
    textColorActive: "{colors.primary}"

  eco-badge:
    backgroundColor: "{colors.eco}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px

  sale-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px

  promo-ribbon:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.promo-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 10px

  spec-row:
    backgroundColor: "transparent"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} 0"

  rating-stars:
    activeColor: "{colors.accent}"
    inactiveColor: "{colors.hairline}"
    typography: "{typography.caption}"
    countColor: "{colors.muted}"

  feature-icon-card:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    iconColor: "{colors.primary}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "4px solid {colors.primary}"
    padding: "{spacing.xxl} 0"


## Components

### Buttons

**`button-primary`** — The main action button runs Lasko brand blue (#0058a8) on a 48px-tall container with {rounded.sm} corners. Hover state advances to the blue-slate #334fb4; press state deepens to the dark navy #002144 (primary-active). Applied to "Add to Cart," "Shop Now," and category-landing CTAs — wherever the primary conversion action lives.

**`button-accent`** — Coral (#e25e49) variant reserved for promotional and urgency-driven contexts: sale events, seasonal clearance, bundle promotions, and limited-time offer banners. Shares the 48px height and {rounded.sm} radius of the primary button but signals commercial urgency rather than product trust. Press state moves to #c94535.

**`button-secondary`** — Transparent fill with a 2px solid primary-blue border and matching text. Used for secondary actions — "Learn More," "Compare Models," "View All" — placed adjacent to a primary or accent button. Height matches at 48px; padding reduces to 10px 22px to account for border width.

**`button-ghost`** — No border, no background, body-colored text at {typography.button-sm}. Lowest-hierarchy action, used for tertiary links inside product cards or collapsed filter panels.

### Inputs

**`text-input`** — 48px height, {rounded.sm} corners, 1px hairline border at rest. Focus transitions to 2px solid #0058a8. Placeholder text in muted gray (#acacaf). Applied across account forms, checkout fields, and filter panel inputs.

**`search-bar`** — Full-pill ({rounded.full}) search input at 48px height. Focus ring is 2px solid primary; a search icon in charcoal (#3d4246) sits left-inset; a clear button appears on input. Used in the main navigation search experience, which typically overlays the full viewport on mobile.

### Navigation

**`nav-bar`** — Top navigation bar on a deep navy canvas (#171f32), 64px tall, with reversed-out white typography at {typography.nav-link}. No bottom border — the color transition to the page surface is the separator. Hover states on nav links use underline or subtle opacity shift rather than background fill.

**`nav-bar-utility`** — A 36px announcement strip immediately above the main nav, filled with brand blue (#0058a8). Carries shipping thresholds, promotional headlines, or site-wide alerts in {typography.caption} white text. Hidden on mobile, with its message surfaced inside the hamburger drawer footer.

### Product Card

**`product-card`** — 1px hairline-soft bordered card on {colors.surface-card}, {rounded.sm} corners, {spacing.base} internal padding. Product title at {typography.title-sm} in ink; price at {typography.price-display} in ink. Rating stars use coral (#e25e49) for filled state and hairline gray for empty, with review count in muted gray at {typography.caption}. Sale badges and eco badges stack on the upper-left corner of the product image. Card lifts on hover via a subtle box-shadow shift.

### Hero Banner

**`hero-banner`** — Full-bleed navy (#171f32) field, minimum 480px tall, with reversed-out white headline at {typography.display-xl} and supporting copy at {typography.display-sm}. The CTA button inside hero sections defaults to button-accent (coral) to create thermal contrast against the cold navy ground. Product photography sits right-aligned at desktop widths and collapses to a centered inset on mobile.

### Badges and Tags

**`eco-badge`** — Green (#00a47c) rectangular badge, {rounded.xs} corners, {typography.badge} weight. Applied to products with Energy Star certification or low-watt operation claims. Renders at approximately 24px height.

**`sale-badge`** — Compact coral badge at {typography.badge} without uppercase transform. Appears inside product cards adjacent to the price, confirming discounted status without the urgency weight of a promo ribbon.

**`promo-ribbon`** — Coral (#e25e49) all-caps uppercase tag using {typography.promo-tag} with 0.4px letter-spacing. Applied to product image overlays or card headers during sale events, seasonal campaigns, or bundle promotions.

### Specification Row

**`spec-row`** — Two-column row, label in muted gray at {typography.spec-label} and value in ink at {typography.body-sm}, separated by a hairline-soft bottom border. Assembles into a spec table for CFM, BTU, ASHRAE rating, wattage, and coverage area. Zero border-radius; no card wrapper — the row itself is the unit.

### Feature Icon Card

**`feature-icon-card`** — Warm off-white background (#e8e8e1) with {rounded.md} corners and {spacing.lg} padding. Carries a primary-blue icon glyph, title at {typography.title-sm}, and supporting text at {typography.body-sm}. Used in "Why Lasko" and product-feature sections on category landing pages to contrast the gray-heavy catalog grid.

### Footer

**`footer`** — Deep navy ground (#171f32) matching the nav bar, closing the page with visual symmetry. A 4px solid primary-blue top border separates footer from the page content area. Link columns run {typography.body-sm} in on-dark white; column headings run {typography.title-sm} at bold weight. Padding at {spacing.xxl} top and bottom.

### Rating Stars

**`rating-stars`** — Coral (#e25e49) filled stars, hairline gray empty stars. Review count inline to the right in muted gray at {typography.caption}. Compact arrangement directly below product title on cards and atop the PDP.

### Category Chips

**`category-chip`** — Soft gray ({colors.surface-soft}) pill chip, {rounded.full} radius. Active state gains a 2px primary-blue border and shifts text to primary blue. Used in PLP filter bars for product type selection: Tower Fans, Box Fans, Portable AC, Window AC, Heaters, Air Purifiers.


## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen navy drawer; search expands to a full-viewport overlay; hero min-height drops to 320px; spec tables scroll horizontally; utility strip hidden |
| Tablet | 744–1128px | Two-column product grid; nav shows primary categories with overflow "More" dropdown; hero scales to 400px; category chips collapse into a horizontal scroll strip |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with mega-menu dropdowns; hero at full 480px; sidebar filter panel on PLP; utility strip visible |
| Wide | > 1440px | Content max-width ~1440px centered; hero background extends edge-to-edge while text column stays capped; four-column product grid; generous whitespace margins |

### Touch Targets
- All interactive elements maintain a minimum 44×44px touch area on mobile via padding expansion
- Category chip pills carry 8px vertical padding to ensure 40px+ tap height
- Rating star tap zone extends to 44px height via invisible hit-area padding
- Nav hamburger button renders at 48×48px

### Collapsing Strategy
- Primary nav collapses to hamburger at < 744px; drawer uses full navy (#171f32) background with stacked nav-link items and the utility strip message in footer position
- Utility strip (nav-bar-utility) hidden on mobile to preserve vertical viewport space
- Product spec rows remain single-column at all breakpoints; no truncation applied — content scrolls
- Promo ribbons persist on mobile at reduced font size (10px) to maintain promotional hierarchy over card images
- Feature icon cards reflow from three-column to single-column on mobile; padding reduces to {spacing.base}


## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected; all type renders in Assistant (Google Fonts), which may be a framework default — a licensed display typeface may exist but was not detectable from page extraction
- Exact CSS border-radius values not extractable; {rounded.sm} (8px) and {rounded.xs} (4px) are inferred from visual inspection and Shopify theme defaults
- Mega-menu structure, hover animation timing curves, and dropdown shadow depth not captured
- Exact button height and internal padding specs inferred from Shopify theme standards — may vary per template zone
- Product image aspect ratio enforcement and focal-point crop rules not extracted
- Star rating display format (integer count vs. aggregate decimal score) not confirmed
- Mobile navigation drawer animation style and backdrop behavior not captured
- Dark mode support not confirmed; no prefers-color-scheme tokens or alternate palette detected in extraction
- #007aff appears in extracted colors but its UI role (possibly a system link override or iOS scroll-indicator artifact) is ambiguous and was excluded from the token set
