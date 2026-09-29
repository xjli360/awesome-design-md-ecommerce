---
version: alpha
name: "Ana Luisa"
source_url: "https://analuisa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  "Your Jewelry Uniform" is the thesis, not a tagline — it positions Ana Luisa as a daily-wear category rather than occasion jewelry, and every design decision reinforces that logic. The site runs on a warm ivory canvas (#fffbf3, deepening to #fbf7ec on card surfaces), against which the primary action color — a brick-kiln red (#bb1b01) — reads as editorial rather than commercial, closer to a magazine's accent ink than a typical e-commerce CTA. A custom extended serif, AwesomeSerif-SemBdExtraTall, carries all display roles at strikingly tall proportions; it is paired with Rigatoni for secondary headlines and Mulish (a humanist sans) for all running prose, producing a deliberate contrast between editorial declaration and readable utility. Warm stone neutrals thread through the system — sand (#dbd6ce), blush sand (#e4e1db), soft peach (#ffddce) — avoiding the sterile white-and-silver palette common to the jewelry category. Rounded tokens lean generous: {rounded.full} pills on primary CTAs, {rounded.md} on product cards, reading as approachable and modern without the hard-edge geometry of luxury or the bubble softness of DTC skincare. The dark olive-charcoal ink (#43443f) keeps body copy slightly warmer than pure black, and a deep burgundy (#8a152a) activates as the pressed-state complement to the brick primary. Promotional chips and price badges inherit the soft peach (#ffddce) rather than a clinical yellow or urgent red, ensuring that even scarcity signals stay within the warm editorial palette. Quick-add overlays and drawer-based cart interactions suggest a mobile-first construction, with generous touch targets and sticky nav architecture that positions the cart icon as the primary conversion funnel. No gradients, no neon — the sophistication is delivered through palette restraint and the confident vertically-stretched geometry of the custom display faces.

colors:
  primary: "#bb1b01"
  primary-active: "#8a152a"
  primary-disabled: "#ffddce"
  ink: "#43443f"
  body: "#4a4a4a"
  muted: "#747571"
  stone: "#898786"
  dark-muted: "#585858"
  hairline: "#dbd6ce"
  hairline-soft: "#e4e1db"
  canvas: "#fffbf3"
  surface-soft: "#f8f5f1"
  surface-card: "#fbf7ec"
  on-primary: "#ffffff"
  warm-sand: "#dbd6ce"
  soft-peach: "#ffddce"
  blush-sand: "#e4e1db"
  success: "#26c653"

typography:
  display-xl:
    fontFamily: "'AwesomeSerif-SemBdExtraTall', serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'AwesomeSerif-SemBdExtraTall', serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Rigatoni', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Mulish', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Mulish', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "'Mulish', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "'Mulish', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Mulish', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Mulish', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  price-display:
    fontFamily: "'Mulish', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Mulish', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-label:
    fontFamily: "'Mulish', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  button-md:
    fontFamily: "'Mulish', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Mulish', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  promo-tag:
    fontFamily: "'Mulish', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px

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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.stone}"
  text-input-focus:
    border: "1px solid {colors.ink}"
    backgroundColor: "{colors.canvas}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    position: sticky
    top: 0
    zIndex: 100
  nav-logo:
    fontFamily: "'AwesomeSerif-SemBdExtraTall', serif"
    fontSize: 22px
    fontWeight: 600
    color: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    overflow: hidden
    padding: "{spacing.sm}"
  product-card-title:
    typography: "{typography.body-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    color: "{colors.ink}"
  product-card-price-sale:
    color: "{colors.primary}"
  product-card-price-original:
    color: "{colors.muted}"
    textDecoration: line-through
  quick-add-overlay:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    position: absolute
    bottom: 0
    width: 100%
    height: 40px
    opacity: 0
    hoverOpacity: 1
    transition: "opacity 200ms ease"
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-bestseller:
    backgroundColor: "{colors.soft-peach}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  promo-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.promo-tag}"
    height: 36px
    textAlign: center
  hero-editorial:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.display-md}"
    subtitleColor: "{colors.muted}"
    padding: "{spacing.section} 0"
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 8px 16px
    height: 36px
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
  swatch-circle:
    width: 20px
    height: 20px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
  swatch-circle-active:
    border: "2px solid {colors.ink}"
    outline: "2px solid {colors.canvas}"
  email-signup:
    backgroundColor: "{colors.warm-sand}"
    inputBackgroundColor: "{colors.canvas}"
    inputTypography: "{typography.body-md}"
    inputRounded: "{rounded.full}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonTypography: "{typography.button-md}"
    buttonRounded: "{rounded.full}"
    padding: "{spacing.xxl} {spacing.lg}"
  pdp-image-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    thumbnailRounded: "{rounded.sm}"
    thumbnailBorderActive: "2px solid {colors.ink}"
  pdp-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    height: 56px
    width: 100%
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    borderLeft: "1px solid {colors.hairline}"
    width: 400px
  toast-notification:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-primary}"
    linkColor: "{colors.stone}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons
**`button-primary`** — A pill-shaped brick-red (#bb1b01) button using uppercase Mulish at 14px/700 with 0.5px letter-spacing. At 48px tall with 28px horizontal padding, it anchors add-to-cart, email signup, and checkout flows. On press it deepens to the burgundy active state (#8a152a); when disabled it renders in soft peach with muted text, remaining distinguishable without projecting urgency.

**`button-secondary`** — A transparent pill with a 1.5px ink border, matching height and typography to `button-primary`. Used for secondary actions like "View All" and "Save to Wishlist" where brick-red would compete with adjacent primary CTAs.

**`button-ghost`** — Transparent with no border, muted gray text. Handles low-priority actions like cancel, back navigation, and pagination controls without adding visual weight.

### Text Input
**`text-input`** — A softly rounded (8px) 48px-tall field with a 1px sand hairline border and warm canvas fill. Stone-gray placeholder text (#898786) guides without distracting. On focus the border firms to ink (#43443f) with no colored ring, keeping the interaction layer tonally consistent with the overall palette.

### Navigation
**`nav-bar`** — Sticky at 64px, warm ivory background separated from content by a 1px sand border. The logo uses AwesomeSerif-SemBdExtraTall at 22px as the primary typographic signal. Navigation links use Mulish 600/14px; icons for search, wishlist, and cart are the secondary mobile targets. On mobile the link row collapses entirely, leaving only the logo and icon cluster.

### Product Cards
**`product-card`** — 12px-rounded warm ivory card. Imagery fills the upper field; below, the product name renders in `body-sm` and price in `price-display`. Sale prices activate in brick-red; original prices gain a line-through in muted gray. On desktop hover, the `quick-add-overlay` fades in at the card base.

**`quick-add-overlay`** — A full-width absolute ink panel (40px) at the card bottom that transitions from opacity 0 to 1 over 200ms ease on hover. Lets shoppers add to cart without navigating to the PDP, essential for the jewelry-uniform browsing model where quantity and variety are expected.

### Badges
**`badge-new`** — Ink background, white uppercase caption, 4px radius. **`badge-sale`** — Brick-red background, white text — matches the primary CTA color to reinforce discount urgency. **`badge-bestseller`** — Soft peach (#ffddce) background with ink text, the warmest treatment; distinguishes popularity from promotional urgency without reaching for a competitive color.

### Hero
**`hero-editorial`** — A full-width warm-surface section with the headline in AwesomeSerif-SemBdExtraTall at 56px and the subtitle in Rigatoni at 28px. Generous section padding on both axes enforces the unhurried, editorial-spread register appropriate for the "jewelry uniform" positioning.

### Filters
**`filter-pill`** — Compact 36px round pills with a 1px hairline border and caption typography. Inactive state: ivory background, ink text. Active state: ink background, white text (see `filter-pill-active`). Used across category browsing, metal, and stone filter interfaces. On mobile these scroll horizontally or collapse to a bottom drawer.

### Color Swatches
**`swatch-circle`** — 20px filled circles with a 2px transparent border. The active state adds a 2px ink ring plus a 2px canvas gap between the ring and the swatch surface, producing a floating-ring selection indicator that reads clearly at small sizes across gold, silver, and rose-gold fills.

### Email Signup
**`email-signup`** — Contained on a warm sand panel (#dbd6ce) to lift it off the ivory page. Pairs a full-pill canvas input with a full-pill brick-red submit button, maintaining CTA language consistency. The sand enclosure creates a visual boundary without a hard border rule.

### PDP Gallery
**`pdp-image-gallery`** — Warm surface-soft background with md-rounded main image and sm-rounded thumbnails. The active thumbnail receives a 2px ink border, repeating the swatch-circle selection vocabulary so both gestures feel like the same design system.

**`pdp-add-to-cart`** — Full-width pill at 56px (4px taller than standard) to increase visual weight at the purchase decision moment. Brick-red/white treatment identical to `button-primary` but scaled for the PDP conversion role.

### Cart Drawer
**`cart-drawer`** — A 400px slide-in panel from the right edge with a single 1px hairline left border. The warm ivory background keeps the drawer tonally continuous with the page, avoiding a high-contrast "pop" that would feel jarring in a warm editorial environment.

### Toast Notification
**`toast-notification`** — Ink background with white Mulish body-sm, 8px radius. Appears bottom-right on add-to-cart and wishlist actions. The dark treatment ensures legibility against the warm ivory page without requiring a separate colored success variant.

### Promotional Banner
**`promo-banner`** — A 36px ink-background top bar with white promo-tag typography, sitting above the nav. Used for shipping thresholds, sale countdowns, and launch announcements. Expected to collapse or become scrollable on mobile to preserve viewport real estate.

### Footer
**`footer`** — Full ink background with white heading text (Mulish 700/14px) and stone-gray link text (#898786) creating a quiet hierarchy. Generous vertical padding for breathing room; link columns expected to stack with accordion expand on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces link row; hero scales to display-lg (40px); filter pills scroll horizontally or collapse to bottom drawer |
| Tablet | 744–1128px | Two-column product grid; nav links visible at reduced spacing; hero maintains display-xl; PDP gallery in side-by-side layout |
| Desktop | 1128–1440px | Three- or four-column product grid; hover quick-add enabled; cart drawer at full 400px; filter pills inline |
| Wide | > 1440px | Max-width container (~1440px) centered with growing side margins; four-column grid maintained; hero padding increases |

### Touch Targets
- All tappable controls (buttons, filter pills, nav icons) minimum 44×44px hit area
- Swatch circles expand hit target to 36×36px via padding despite 20px visual diameter
- Cart, wishlist, and hamburger nav icons padded to 48×48px touch region in mobile nav bar
- Quick-add CTA height of 40px meets minimum; on mobile it may be replaced by a persistent add-to-cart button on the card

### Collapsing Strategy
- Promo banner collapses after first scroll on mobile to recover viewport space; remains sticky on desktop
- Nav links collapse to a slide-in hamburger drawer below tablet breakpoint; cart icon persists in top-right at all sizes
- Product filters collapse to a slide-up bottom sheet on mobile instead of inline pill row
- PDP gallery switches from vertical thumbnail rail to horizontal swipe carousel on mobile
- Footer link groups stack vertically with accordion expand per section on mobile
- Email signup module stacks input and button vertically on mobile, both stretching full width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- AwesomeSerif-SemBdExtraTall weight and width variants not confirmed — only the SemiBold ExtraTall cut was detected; lighter or narrower cuts for subheadings are not confirmed
- Rigatoni licensing, foundry, and available weight range not confirmed; role inferred from font name, category, and position as secondary display face
- Exact product-card image aspect ratio not extracted — 3:4 portrait assumed based on jewelry category convention
- Animation easing curves and duration tokens beyond the inferred 200ms ease on quick-add not extracted from the live site
- Nav height in scrolled/compressed sticky state not confirmed; 64px reflects the expanded state
- Dark mode or high-contrast mode palette not present — all tokens assume the warm ivory light mode
- #007aff is iOS system blue (link default) and #26c653 is system green (likely success state); neither is confirmed as a brand-owned palette choice
- Monospace font stack (Consolas, Menlo, Monaco, etc.) appears to be system/code defaults with no confirmed brand-facing use case
- Exact grid gutter widths and max container width not extracted; values in Responsive Behavior section are inferred from category conventions
