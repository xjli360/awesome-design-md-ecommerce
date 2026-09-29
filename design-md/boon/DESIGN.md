---
version: alpha
name: "Boon"
source_url: "https://www.booninc.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The grass countertop drying rack — rows of flexible green pegs that look more like a lawn than kitchen equipment — established Boon's design language before any screen ever loaded: everyday baby utility reimagined as something you'd actually want to leave on your counter. That same impulse governs the digital surface: a single saturated orange (#f78f1e) carries every CTA, price callout, and promo strip while a warm cream canvas (#fbf8e7) and a disciplined range of cool neutrals (#636466, #757575, #e5e5e5) hold everything else in reserve. The brand doesn't apologize for color — it also keeps a teal (#00c2c7), a signal red (#f94436), and a golden yellow (#ffbb49) in rotation for product and promotional moments — but orange is the organizing voltage, the one hue that tells parents exactly where to press.

  Type runs in Jost, a geometric sans that sits between the looseness of a rounded display face and the austerity of a Swiss grotesque. At display scale it's set at weights 600–700 rather than the heavy 800+ that other infant brands use to project authority; Boon trusts color and product photography to carry that load instead. Body copy drops to 400 weight at 16px with a 1.6 line-height, making dishwasher-safe specs and feature callouts scannable at pace. Button labels and filter tags use uppercase tracking at modest letter-spacing, giving the UI a clean industrial quality without reading cold.

  Corner radii lean soft but stop short of pill: product cards use `{rounded.md}` (12px), primary buttons `{rounded.sm}` (8px), and filter chips `{rounded.full}` for a slightly more playful register. The warm cream surface (#fbf8e7) surfaces behind editorial blocks — gift guides, seasonal collections, feature stories — providing a second canvas temperature that's perceptibly warmer than white without announcing itself. Spacing is generous throughout: section breaks at 64px give each product category room to breathe, and the 72px nav height signals a brand that is not trying to compress its presence into the smallest possible header. The overall effect is a storefront built by people who have actually wrestled a bottle brush under a faucet at 2 a.m.: direct, color-forward, and entirely uninterested in looking cute.

colors:
  primary: "#f78f1e"
  primary-active: "#d97210"
  primary-disabled: "#fcd5a0"
  accent-teal: "#00c2c7"
  accent-red: "#f94436"
  accent-blue: "#007dc6"
  accent-yellow: "#ffbb49"
  accent-coral: "#e95144"
  ink: "#212121"
  body: "#444444"
  muted: "#757575"
  muted-soft: "#8f8f8f"
  hairline: "#e5e5e5"
  hairline-soft: "#f2f2f2"
  canvas: "#ffffff"
  surface-warm: "#fbf8e7"
  surface-soft: "#f6f6f6"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "rgba(0,0,0,0.4)"

typography:
  display-xl:
    fontFamily: "'Jost', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Jost', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Jost', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Jost', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Jost', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Jost', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Jost', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Jost', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.6px
    textTransform: uppercase
  label-uppercase:
    fontFamily: "'Jost', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Jost', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'Jost', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
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
    border: "2px solid {colors.ink}"
    padding: 12px 26px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  promo-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  hero-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
    imagePosition: right
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
    imageRounded: "{rounded.md}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    hoverShadow: "0 4px 16px rgba(0,0,0,0.10)"
  age-badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  new-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
    padding: 6px 14px
  category-section-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    accentBorder: "3px solid {colors.primary}"
    paddingBottom: "{spacing.sm}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    overlayColor: "{colors.scrim}"
    roundedLeft: "{rounded.lg}"
    width: 420px
    ctaComponent: "button-primary"
    headerTypography: "{typography.title-md}"
    itemTitleTypography: "{typography.body-sm}"
    totalTypography: "{typography.price-display}"
  editorial-card:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    headingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.label-uppercase}"
    headingColor: "{colors.muted-soft}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The orange (#f78f1e) primary button is the single loudest element on any page, carrying add-to-cart, checkout, and primary form submissions. It sits at 48px height with uppercase Jost at 15px/600 weight and 0.8px letter-spacing, giving it a confident industrial quality. On `:hover` the background shifts to `{colors.primary-active}` (#d97210); the disabled state mutes to `{colors.primary-disabled}` (#fcd5a0) with unchanged text. Corner radius stays at `{rounded.sm}` (8px) — soft enough to feel approachable, square enough to read as a control rather than a pill.

**`button-secondary`** — White fill with a 2px ink (#212121) border and matching uppercase label. Occupies the same 48px height as primary but signals a lower-commitment action: "View Details," "Learn More," "Add to Wishlist." On `:hover` the border color swaps to `{colors.primary}` orange to maintain visual continuity with the primary hierarchy.

**`button-ghost`** — Transparent background, orange text, no border. Used for tertiary text-link actions inside cards and modals where a full button would crowd the layout. Underline appears on hover.

---

### Navigation

**`nav-bar`** — 72px fixed bar on white canvas with a `{colors.hairline}` bottom border (1px). The Boon wordmark renders in `{colors.primary}` orange at the left. Center hosts top-level category links in Jost 15px/500. Right side carries search, wishlist, and cart icon buttons. A `{colors.promo-strip}` (orange, 40px) sits immediately above the nav, carrying free-shipping thresholds and promo codes in Jost caption text.

---

### Product Card

**`product-card`** — Rendered on `{colors.surface-card}` (#f2f2f2) with `{rounded.md}` (12px) corners and a matching image crop. Title uses `{typography.title-sm}` (Jost 16px/600); price uses `{typography.price-display}` (Jost 20px/700). Badge chips (age range, SALE, NEW) stack at the top-left corner of the image — teal for age, red for sale, yellow for new. Card lifts with a subtle box-shadow on hover. Add-to-cart button appears on hover overlay using `button-primary` at reduced padding.

---

### Badges

**`age-badge`** — Teal (#00c2c7) pill-adjacent chip (xs radius, 4px) in uppercase Jost 11px/700. Encodes "0–6M", "6–18M", "2–4Y" age ranges — the primary navigation affordance Boon uses to help parents self-select quickly.

**`sale-badge`** — Signal red (#f94436), same form factor. Appears on product cards, category pages, and inside the cart.

**`new-badge`** — Golden yellow (#ffbb49) with ink text for contrast. Signals recent launches without the urgency connotation of red.

---

### Hero Banner

**`hero-banner`** — Full-bleed section on `{colors.surface-warm}` (#fbf8e7) cream. Headline in `{typography.display-xl}` (Jost 48px/700), body in `{typography.body-md}`. Primary CTA sits left-aligned below the body copy. Product or lifestyle photography fills the right column on desktop, stacks above the copy on mobile. The warm cream background distinguishes hero and editorial moments from the cooler white of product-listing pages.

---

### Filters

**`filter-chip`** / **`filter-chip-active`** — Pill-shaped (`{rounded.full}`) category and attribute filters. Inactive state: `{colors.surface-soft}` fill, `{colors.hairline}` border, `{colors.body}` text. Active state inverts to `{colors.ink}` fill with `{colors.on-dark}` text — a strong binary toggle that makes selection state legible at a glance without relying on color alone.

---

### Cart Drawer

**`cart-drawer`** — 420px overlay sliding from the right edge. Left edge rounded at `{rounded.lg}` (20px). Background `{colors.canvas}` white; header line in `{typography.title-md}`; item titles in `{typography.body-sm}`; order total in `{typography.price-display}`. Checkout CTA is a full-width `button-primary`. Overlay scrim uses `{colors.scrim}` (rgba black at 40%).

---

### Editorial Card

**`editorial-card`** — Warm cream (#fbf8e7) surface with `{rounded.md}` corners and generous `{spacing.xl}` padding. Used in gift guides, blog previews, and feature callouts. Heading in `{typography.display-sm}`; body in `{typography.body-sm}`. No border — the warm background alone defines the card boundary against the white canvas.

---

### Footer

**`footer`** — Ink-dark (#212121) background with white text. Section headings in `{typography.label-uppercase}` (Jost 11px/700, 1.2px tracking, muted-soft color) to organize columns. Links in `{typography.body-sm}` white. The orange primary does not appear in the footer — no CTA competes with the bottom navigation links.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + cart icon; hero image stacks above headline; promo strip wraps to two lines if needed; filter chips scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + condensed links + icons; hero goes 50/50 split; cart drawer narrows to 360px |
| Desktop | 1128–1440px | Three-column product grid; full nav with all category links visible; hero banner at full `{spacing.section}` vertical padding |
| Wide | > 1440px | Content max-width capped at 1440px and centered; hero image scales proportionally; grid stays three columns; additional editorial cards appear in homepage layout |

### Touch Targets

- All interactive controls (buttons, chips, icon buttons) maintain minimum 44×44px touch target
- Filter chips use 6px top/bottom padding to meet height on mobile even when text is small
- Cart and wishlist icon buttons in nav are padded to 48px hit area regardless of icon size
- Age-badge and sale-badge chips on product cards are display-only on mobile; tap target is the card itself

### Collapsing Strategy

- Top promo strip persists across all breakpoints but reduces to a single line of 11px caption text on mobile
- Category navigation moves into a full-screen drawer on mobile with all top-level links expanded as an accordion
- Hero banner switches from two-column to single-column at 744px, image stacking above headline
- Product filter panel collapses from sidebar (desktop) to horizontal scroll chips (tablet/mobile)
- Footer column layout shifts from four columns (desktop) to two (tablet) to single stacked (mobile)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color was set, so the exact intended browser chrome accent color is inferred from the dominant orange rather than confirmed
- Precise button border-radius values could not be measured from the live site; `{rounded.sm}` (8px) is estimated from visual inspection
- Exact nav height (72px) and promo strip height (40px) are estimated; the site was not Shopify and no CSS variables were exposed
- Hover and focus state colors for secondary and ghost buttons are inferred; no design tokens or CSS custom properties were extractable
- Font weight scale for Jost is estimated (400/500/600/700) based on the variable-font range Jost supports; exact weights used at each level were not confirmed
- Animation/transition durations (card hover lift, drawer slide, filter chip toggle) are not captured
- Mobile navigation drawer visual treatment (background, animation direction, close affordance) could not be confirmed from static extraction
- Exact image aspect ratio used in product cards (likely 1:1 or 4:3) was not confirmed
