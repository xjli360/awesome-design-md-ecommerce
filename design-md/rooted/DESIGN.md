---
version: alpha
name: "Rooted"
source_url: "https://heyrooted.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Electric chartreuse (#ccff00) bursting against deep forest green (#134431) — the palette reads like new growth punching through canopy shade, and that tension drives every surface on the Rooted storefront. GT Walsheim carries the type system in two cuts: a rounded geometric heading weight that feels approachable at 32–48px display sizes, and a lighter body weight that keeps long plant-care descriptions scannable without drifting into clinical sans-serif territory. The canvas sits at a warm parchment (#fafaef) rather than pure white, giving photography of soil, terracotta, and foliage a grounded warmth that sterile #fff would bleach out. Cards and product tiles use `{rounded.md}` corners with generous `{spacing.lg}` gutters, letting each plant breathe inside its frame — the layout never crowds. CTAs punch in that lime accent on the dark green ground, a combination with enough contrast to pass WCAG AA at `{typography.button-md}` size while still feeling organic rather than corporate. A secondary palette of earthy neutrals — warm beige (#f1ece8), pale sage (#e7ecd6), and a soft green-cream (#eef4db) — tiles across category banners, subscription plan cards, and seasonal campaign modules, reinforcing the botanical identity without leaning on leaf illustrations. Navigation holds steady in the darkest green (#15271a), nearly black but warm enough to avoid the harshness of pure #000. Accent flashes of burnt orange (#ff5400) mark sale badges and urgency indicators, while a surprise lavender (#aaa3fd) and dusty rose (#e19c9c) surface in seasonal collection headers and gift-card modules, proving the system can flex beyond its green core without losing coherence. Subscription is the commercial engine — plan-selector components, frequency toggles, and delivery-schedule cards all carry first-class design treatment with distinct surface colors and clear hierarchy. The overall impression is a nursery counter transplanted into a browser: soil-stained, sun-lit, and alive.

colors:
  primary: "#134431"
  primary-active: "#0e3325"
  primary-disabled: "#134431aa"
  accent: "#ccff00"
  accent-active: "#b8e600"
  accent-disabled: "#ccff0066"
  alert: "#d51010"
  alert-soft: "#e19c9c"
  orange: "#ff5400"
  lavender: "#aaa3fd"
  ink: "#15271a"
  body: "#121212"
  muted: "#6b6b6b"
  hairline: "#dedede"
  canvas: "#fafaef"
  surface-soft: "#f1ece8"
  surface-card: "#ffffff"
  surface-sage: "#e7ecd6"
  surface-green: "#eef4db"
  on-primary: "#ccff00"
  on-accent: "#134431"
  on-dark: "#fafaef"

typography:
  display-xl:
    fontFamily: "'GTWalsheimHeading', 'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'GTWalsheimHeading', 'Assistant', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'GTWalsheimHeading', 'Assistant', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'GTWalsheimHeading', 'Assistant', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'GTWalsheimHeading', 'Assistant', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'GTWalsheimHeading', 'Assistant', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'GTWalsheimBody', 'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'GTWalsheimBody', 'Assistant', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'GTWalsheimBody', 'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'GTWalsheimBody', 'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'GTWalsheimBody', 'Assistant', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'GTWalsheimBody', 'Assistant', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'GTWalsheimHeading', 'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'GTWalsheimHeading', 'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'GTWalsheimBody', 'Assistant', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  uppercase-tag:
    fontFamily: "'GTWalsheimBody', 'Assistant', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'GTWalsheimHeading', 'Assistant', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'GTWalsheimBody', 'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  price-lg:
    fontFamily: "'GTWalsheimHeading', 'Assistant', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-md:
    fontFamily: "'GTWalsheimBody', 'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0

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
    typography: "{typography.button-lg}"
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    opacity: 0.6
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  button-accent-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 13px 24px
    height: 48px
    borderWidth: 2px
    borderColor: "{colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
  text-input-error:
    borderColor: "{colors.alert}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 24px
  nav-bar-scrolled:
    backgroundColor: "{colors.primary}"
    backdropFilter: none
    boxShadow: "0 2px 8px rgba(19,68,49,0.15)"
  announcement-bar:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.caption}"
    height: 36px
    padding: 8px 16px
  hero-split:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-lg}"
    ctaComponent: button-accent
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 560px
    imagePosition: right
    imageFit: cover
  hero-full-bleed:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-lg}"
    overlay: "linear-gradient(to right, rgba(21,39,26,0.75) 0%, transparent 60%)"
    minHeight: 640px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm}"
    imageRatio: "4:5"
    imageRounded: "{rounded.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-md}"
    hoverTransform: "translateY(-2px)"
    hoverShadow: "0 8px 24px rgba(19,68,49,0.1)"
  product-card-badge:
    backgroundColor: "{colors.orange}"
    textColor: "{colors.on-dark}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-badge-new:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  subscription-plan-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    borderWidth: 2px
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-lg}"
    bodyTypography: "{typography.body-sm}"
  subscription-plan-card-selected:
    borderColor: "{colors.primary}"
    backgroundColor: "{colors.surface-green}"
  frequency-toggle:
    backgroundColor: "{colors.surface-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 4px
    height: 40px
  frequency-toggle-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  collection-banner:
    backgroundColor: "{colors.surface-sage}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl} {spacing.lg}"
  collection-banner-seasonal:
    backgroundColor: "{colors.lavender}"
    textColor: "{colors.on-dark}"
  collection-banner-gift:
    backgroundColor: "{colors.alert-soft}"
    textColor: "{colors.ink}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  plant-care-badge:
    backgroundColor: "{colors.surface-green}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 4px 10px
  trust-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    iconSize: 24px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.link}"
    padding: "{spacing.section} {spacing.lg}"
  footer-newsletter:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    inputBackgroundColor: "rgba(255,255,255,0.15)"
    inputTextColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 420px
    headerTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    footerBackgroundColor: "{colors.surface-soft}"
  cart-line-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageSize: 80px
    imageRounded: "{rounded.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-md}"
  quantity-stepper:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 32px
    buttonWidth: 32px
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-lg}"
    resultTypography: "{typography.body-md}"
    scrimColor: "rgba(18,18,18,0.5)"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
---

## Components

### Buttons

**`button-primary`** — Deep forest green (#134431) fill with chartreuse (#ccff00) text, `{rounded.md}` corners, and `{typography.button-lg}` weight. On hover the background darkens to `{colors.primary-active}`, and a subtle `translateY(-1px)` lift gives tactile feedback. Disabled state drops to 60% opacity with no pointer events.

**`button-accent`** — Inverts the primary relationship: chartreuse fill with dark green text. Used for hero CTAs and subscription commit actions where the button needs to pop against a dark green background. Active state shifts to `{colors.accent-active}`, a slightly deeper lime.

**`button-secondary`** — Transparent with a 2px `{colors.primary}` border and green text. On hover the fill floods to `{colors.primary}` and text flips to `{colors.on-primary}`, creating a smooth ink-wash transition. Used for secondary actions like "View All" links and alternative plan selections.

**`button-tertiary`** — Text-only with an underline, no background or border. Reserved for inline actions like "Learn more" and "View care guide" where a full button would feel heavy.

### Navigation

**`nav-bar`** — Full-width deep green bar at 64px height, anchoring the brand's forest identity at the top of every page. Logo sits left, nav links center in `{typography.nav-link}`, and cart/account icons sit right. On scroll, a subtle `box-shadow` appears to separate the nav from content beneath.

**`announcement-bar`** — Chartreuse strip above the nav, 36px tall, carrying rotating promotional messages (free shipping thresholds, seasonal sales, subscription offers) in `{typography.caption}` dark-green text. High-contrast pairing ensures readability at small sizes.

### Product Cards

**`product-card`** — White card with `{rounded.md}` corners housing a 4:5 ratio plant photograph with `{rounded.sm}` inner radius. Title in `{typography.title-sm}`, price in `{typography.price-md}`. On hover, the card lifts 2px with a soft green-tinted shadow, inviting interaction. Quick-add overlay appears on hover for desktop, showing a compact "Add to cart" button.

**`product-card-badge`** — Burnt orange (#ff5400) pill with white uppercase text for "SALE" and limited-stock indicators. Positioned absolutely in the top-left corner of the product image. A `badge-new` variant uses chartreuse with dark green text for new arrivals.

### Subscription Components

**`subscription-plan-card`** — White card with `{rounded.lg}` corners, 2px hairline border, and generous `{spacing.lg}` internal padding. Plan name in `{typography.title-md}`, price in large `{typography.price-lg}`, and feature list in `{typography.body-sm}`. When selected, the border thickens to `{colors.primary}` and the background shifts to `{colors.surface-green}`, a pale botanical green that signals activation without overwhelming.

**`frequency-toggle`** — Pill-shaped segmented control (`{rounded.full}`) sitting on a sage background (`{colors.surface-sage}`). The active segment fills with `{colors.primary}` and flips text to chartreuse. Used to switch between weekly, biweekly, and monthly delivery frequencies.

### Collection & Category

**`collection-banner`** — Full-width rounded banner (`{rounded.lg}`) in `{colors.surface-sage}` that introduces a plant category with display typography and optional body text. Seasonal variants swap to `{colors.lavender}` for spring/summer collections and `{colors.alert-soft}` for gift-oriented collections, expanding the palette without breaking the system.

**`category-pill`** — Horizontally scrollable filter chips in `{rounded.full}` capsules. Inactive pills sit on `{colors.surface-soft}` with dark text; active pills fill with `{colors.primary}` and flip to chartreuse text. Used for filtering by plant type, light requirements, and difficulty level.

### Plant Care

**`plant-care-badge`** — Small informational badges in `{colors.surface-green}` with forest-green text, `{rounded.sm}` corners. Displayed on product detail pages to indicate light level, water frequency, and pet safety. Icon + label pattern at `{typography.caption}` size.

### Trust & Social Proof

**`trust-bar`** — Horizontal strip in `{colors.surface-soft}` running across the page below the hero, displaying 3-4 trust signals (number of plants shipped, customer rating, sustainable packaging claim) with 24px icons and `{typography.body-sm}` text.

### Cart

**`cart-drawer`** — Slide-in panel from the right, 420px wide on desktop, full-width on mobile. White background with a sticky header (`{typography.title-md}`) and a sticky footer on `{colors.surface-soft}` containing the subtotal and checkout CTA. Line items stack vertically with 80px square product thumbnails.

**`quantity-stepper`** — Compact −/+/count control at 32px height with `{rounded.sm}` corners on a `{colors.surface-soft}` background. Minus and plus buttons are 32px square touch targets.

### Search

**`search-overlay`** — Modal overlay with a dark scrim, centered search panel with `{rounded.lg}` corners. Large input field in `{typography.body-lg}` with no border, just a bottom hairline. Results stream below as the user types, showing product image, title, and price in a compact list format.

### Footer

**`footer`** — Dark green-black (#15271a) full-width block with link columns in `{typography.link}`, a newsletter signup module in `{colors.primary}` with a translucent input field, and social icons. Bottom bar carries legal links and payment icons at `{typography.caption-sm}` size.

**`footer-newsletter`** — Inset module within the footer, `{colors.primary}` background with `{rounded.md}` corners. Heading in `{typography.title-md}` with chartreuse text, email input with translucent white background, and a chartreuse submit button.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2-up cards). Hero stacks vertically — image above, text below. Nav collapses to hamburger menu with full-screen green overlay. Cart drawer becomes full-width bottom sheet. Category pills scroll horizontally. Subscription cards stack vertically. Display type scales to 32px. |
| Tablet | 744–1128px | Two-column product grid (3-up cards). Hero maintains split layout at reduced image ratio. Nav shows abbreviated link set with overflow into hamburger. Cart drawer stays at 420px. Collection banners reduce padding. |
| Desktop | 1128–1440px | Three- to four-column product grid. Full nav with all links visible. Hero split at ~50/50 ratio. Subscription plan cards sit side by side (up to 3). Cart drawer at 420px. Hover states activate on product cards. |
| Wide | > 1440px | Content max-width clamps at 1440px and centers. Product grid holds 4-up. Hero image can extend beyond content max-width for full-bleed effect. Generous section spacing at `{spacing.section}` or larger. |

### Touch Targets
- All interactive elements maintain 44px minimum touch target on mobile, even when visually smaller
- Category pills and frequency toggles have 12px horizontal gap to prevent mis-taps
- Quantity stepper buttons expand to 44px on mobile despite 32px visual size
- Cart line-item swipe-to-delete zone spans full row height

### Collapsing Strategy
- Product grid: 4-col → 3-col → 2-col → 2-col (never single-column cards)
- Footer link columns: 4-col → 2×2 grid → single accordion stack
- Subscription plan cards: horizontal row → vertical stack with the recommended plan first
- Trust bar icons: horizontal row → 2×2 grid on mobile
- Collection banner: horizontal text + image → stacked image-first on mobile
- Announcement bar: marquee scroll on mobile when text exceeds viewport width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- GT Walsheim exact font weights and OpenType feature settings could not be confirmed from extraction alone — the heading and body cuts may share a single variable font file with different weight ranges
- Exact border-radius values on product cards and buttons are inferred from visual style; the live site may use slightly different values (e.g., 10px vs 12px)
- Transition/animation durations and easing curves were not extracted — hover lifts, drawer slides, and overlay fades need manual measurement
- The lavender (#aaa3fd) and dusty rose (#e19c9c) appear in limited contexts and may be seasonal; their permanence in the design system is uncertain
- Mobile nav overlay behavior (animation direction, backdrop treatment, menu item spacing) was not captured
- Favicon and Open Graph image colors were not cross-referenced against the palette
- No meta theme-color was set, so mobile browser chrome color is uncontrolled
- Subscription flow micro-interactions (plan selection animation, frequency toggle slide, delivery calendar UI) need further inspection
- Dark mode treatment is absent from the live site — no prefers-color-scheme tokens were detected
