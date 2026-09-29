---
version: alpha
name: "Mack Weldon"
source_url: "https://mackweldon.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  National2Condensed headlines compress Mack Weldon's editorial voice into tight, uppercase stacks — a typographic choice that reads more like a sportswear magazine spread than a product page, and signals the brand's conviction that disciplined hierarchy is more persuasive than hero imagery alone. The primary anchor is #001237, a navy so deep it approaches black, used for every primary button, the global nav bar, and any CTA that demands authority. Warm sand-beige enters at #dfd5c4 and #d1c3b2, surfacing in loyalty-tier backgrounds, editorial callout modules, and seasonal campaign backdrops — a counterweight that prevents the palette from reading as corporate-cold. Forest green #1f3521 handles the Weldon Blue membership program and select performance-certification badges, holding enough chromatic distance from the navy to mark tier status without visual conflict. Interactive actions — link underlines, form focus rings, add-to-cart confirmations — pivot to #0074e0, a crisp mid-blue that lifts clearly off the dark brand palette. Gray steps are unusually fine-grained: #303030 and #2d2d2d carry secondary text and hard dividers; #e0e0e0, #ebebeb, #eaeaea, and #f7f7f7 subdivide the light canvas into drawer surfaces, card tints, and skeleton states. Buttons use `{rounded.none}` or `{rounded.xs}` — there are no soft corners anywhere in the UI, reflecting a precision-over-approachability philosophy that runs through every grid edge. UntitledSans handles all running body copy and UI labels in a clean grotesque register, letting the condensed display stack carry the brand's editorial weight while prose stays legible and unobtrusive. Product cards are deliberately spare: clean aspect-ratio containers, a hover-swap for the alternate colorway, and a compact badge row for technical callouts like "Silver Fabric" or "18-Hour." On desktop, sections open wide with full-bleed imagery and the condensed type at scale; on mobile the grid collapses to single-column while National2Condensed headlines hold brand voice at 32–40px.

colors:
  primary: "#001237"
  primary-hover: "#0a1e45"
  primary-active: "#000d25"
  primary-disabled: "#6b7280"
  interactive: "#0074e0"
  interactive-hover: "#005bb5"
  interactive-disabled: "#aaaaaa"
  ink: "#303030"
  body: "#2d2d2d"
  muted: "#707070"
  muted-soft: "#aaaaaa"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  border-mid: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#f3f3f3"
  surface-hover: "#ebebeb"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sand: "#dfd5c4"
  sand-deep: "#d1c3b2"
  forest: "#1f3521"
  on-forest: "#ffffff"
  error: "#d12121"
  error-dark: "#c70000"
  copper: "#cc6328"

typography:
  display-xl:
    fontFamily: "National2Condensed, 'Arial Narrow', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "National2Condensed, 'Arial Narrow', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.3px
    textTransform: uppercase
  display-md:
    fontFamily: "National2Condensed, 'Arial Narrow', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
    textTransform: uppercase
  display-sm:
    fontFamily: "National2Condensed, 'Arial Narrow', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0
    textTransform: uppercase
  title-lg:
    fontFamily: "UntitledSans, Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "UntitledSans, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "UntitledSans, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  body-md:
    fontFamily: "UntitledSans, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "UntitledSans, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "UntitledSans, Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-caps:
    fontFamily: "UntitledSans, Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "UntitledSans, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  button-sm:
    fontFamily: "UntitledSans, Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  nav-link:
    fontFamily: "UntitledSans, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "UntitledSans, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "UntitledSans, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0

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
    padding: "14px 24px"
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "13px 23px"
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "13px 0"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-promo:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    badgeSlot: true
  product-card-name:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  hero-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: "480px"
  hero-sand:
    backgroundColor: "{colors.sand}"
    textColor: "{colors.primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: "480px"
  editorial-callout:
    backgroundColor: "{colors.sand}"
    textColor: "{colors.primary}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl}"
  performance-badge:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-forest}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  weldon-blue-badge:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-forest}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.primary}"
    borderInactive: "1px solid {colors.hairline}"
    gap: "{spacing.sm}"
  size-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    height: 40px
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    soldOutTextColor: "{colors.muted-soft}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderLeft: "1px solid {colors.hairline}"
    width: "400px"
    headlineTypography: "{typography.title-md}"
  loyalty-tier-card:
    backgroundColor: "{colors.sand}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.sand-deep}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    headlineTypography: "{typography.label-caps}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Solid #001237 navy fill, no border-radius, all-caps UntitledSans at 14px/600 weight with 0.06em tracking. The zero-radius hard edge is intentional and appears on every primary action in the system — add to cart, checkout, and account creation alike. Hover darkens to #0a1e45; disabled uses #6b7280 so the shape persists without affordance.

**`button-secondary`** — Canvas fill with a 1px #001237 stroke and matching navy text. On hover the button inverts to the filled primary state, giving a clean toggle feel without animation complexity. Height and padding mirror `button-primary` so the two can sit side-by-side without vertical misalignment.

**`button-ghost`** — Transparent background with #303030 ink text, used for secondary inline actions (size guides, learn-more links, filter toggles) where a bordered button would add visual weight. No radius, matching uppercase letter-spacing.

### Text Input

**`text-input`** — Zero-radius rectangle, 1px #e0e0e0 border at rest, shifts to 1px #001237 on focus with no glow or shadow. Placeholder text uses #707070 muted. Height 48px matches button height so inline form rows (email capture, promo code) align without flex hacks.

### Navigation

**`nav-bar`** — White canvas, 60px tall, 1px #e0e0e0 bottom border. Logo sits left; primary nav links in 14px/500 UntitledSans center or left-aligned; cart, account, and search icons right. The nav carries a `nav-bar-promo` strip above it — solid #001237 with white caption text centered at 36px height — for free-shipping thresholds or sale announcements.

### Product Card

**`product-card`** — Hard edges throughout, 3:4 image container with a hover swap to the alternate colorway shot. Name uses `title-sm` (14px/600), price uses `price-sm` (14px/500). A `product-card-badge` slot at the image top-left holds flat #001237 panels for "NEW", "BEST SELLER", or sale callouts in 11px all-caps. The card carries no drop shadow or card stroke — products are differentiated by image and copy, not frame chrome.

### Hero

**`hero-dark`** — Full-bleed section on #001237 canvas, white text. Headline in `display-xl` (National2Condensed, 56px, uppercase) stacked above a `body-md` subtitle and a `button-primary`. On desktop the text block sits left-aligned over a right-bleed photograph; on mobile the image stacks below the text block. **`hero-sand`** swaps the background to #dfd5c4 with #001237 text — used for lifestyle editorial campaigns and membership program feature rows.

### Editorial Callout

**`editorial-callout`** — Sand background (#dfd5c4) with navy text, `display-md` headline and `body-md` paragraph, 48px padding all sides. Used for feature storytelling sections (fabric tech explainers, "Why Mack Weldon" modules) between product grids. No border, no radius, full column width.

### Performance & Loyalty Badges

**`performance-badge`** and **`weldon-blue-badge`** — Both use #1f3521 forest fill with white label-caps text (11px, 0.08em spacing, uppercase). Performance badges call out fabric certifications ("Silver Technology," "18-Hour Shirt"); Weldon Blue badges signal loyalty-program benefits. The forest green provides categorical separation from the primary navy at a glance.

### Color Swatch & Size Button

**`color-swatch`** — 24px circles with `{rounded.full}`, 8px gap. Active state draws a 2px #001237 ring; inactive uses 1px #e0e0e0. Sold-out swatches receive a diagonal strike. **`size-button`** is a flat 40px rectangle (no radius), resting with #e0e0e0 border and ink text; selected inverts to #001237 fill with white text; sold-out keeps its shape with #aaaaaa text and no hover affordance.

### Cart Drawer

**`cart-drawer`** — 400px wide panel sliding in from the right, white background, 1px #e0e0e0 left border. No shadow layer — the border alone creates the edge. Item rows follow the `product-card` pattern at reduced scale; a sticky footer holds the order total and the `button-primary` checkout CTA.

### Loyalty Tier Card

**`loyalty-tier-card`** — #dfd5c4 sand panel with a 1px #d1c3b2 border, 24px padding, no radius. Headline in `display-sm` (National2Condensed, 24px, uppercase), body in `body-sm`. Used in the Weldon Blue membership section to present tier names (Blue, Gold, Platinum) with their associated perks.

### Footer

**`footer`** — Full-width #001237 navy footer with white text throughout. Column headers in `label-caps` (11px, uppercase, 0.08em tracking); links in `body-sm` (14px/400). Four-column layout on desktop collapses to a single accordion on mobile. Social icons and legal copy run in a sub-footer row at 12px caption scale.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; National2Condensed display at 32–36px; nav collapses to hamburger + logo + cart icons; `hero-dark` text stacks above image; `cart-drawer` becomes full-width bottom sheet; size/color selectors expand to full row width |
| Tablet | 744–1128px | Two-column product grid; nav links visible with condensed labels; hero image and text side-by-side at 50/50 split; `editorial-callout` padding reduces to `{spacing.xl}` |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with hover mega-menus; hero text block left at ~40% with right-bleed image; `display-xl` at full 56px |
| Wide | > 1440px | Max-width container ~1440px centered; product grid caps at four columns; hero image full-bleed behind a max-width text column |

### Touch Targets

- All interactive buttons and inputs maintain 48px minimum height
- Color swatches padded to 40px touch area despite 24px visual size
- Size buttons at 40px height with `{spacing.sm}` gap between items
- Nav icons (cart, account, search) hit 44px tap target via padding

### Collapsing Strategy

- Navigation collapses hamburger-first; promo bar persists until 375px breakpoint
- Product filters move from left sidebar (desktop) to a full-screen drawer (mobile)
- Footer four-column layout collapses to single-column accordion with `{colors.hairline}` dividers
- `editorial-callout` padding scales from 48px (desktop) to 24px (mobile)
- Hero image drops below text block on mobile; text block takes `{colors.primary}` background fill for legibility

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button border-radius value not confirmed from CSS extraction — `{rounded.none}` assumed based on brand aesthetic; may be 2px (`{rounded.xs}`) in practice
- National2Condensed and UntitledSans are licensed custom fonts; exact weight variants (300/400/500/700) and webfont loading strategy not extracted
- Mega-menu structure, animation timing, and hover panel layout not captured
- Mobile nav drawer background color and transition curve not confirmed
- Specific spacing grid (8px base vs 4px base) not confirmed from extraction — 8px-based `spacing` scale assumed
- Weldon Blue loyalty tier names, color assignments per tier (Blue/Gold/Platinum), and specific badge variants not extracted from live site
- Product image hover behavior (fade vs slide swap) not confirmed
- Swatches: exact sold-out treatment (diagonal line vs opacity vs cross) not observed
- `copper: "#cc6328"` appears in the extracted palette but its usage context (sale callouts? seasonal campaign?) is not confirmed
