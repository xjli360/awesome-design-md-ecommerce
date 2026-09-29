---
version: alpha
name: "Mount-It!"
source_url: "https://mount-it.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The surprise in Mount-It!'s extracted palette is not the commanding steel-blue navy (#154775) anchoring every primary CTA and navigation bar, but the warm amber-browns — raw sienna (#964b00), teak (#774d3b), cognac (#7a6c60) — that surface throughout product imagery and discount-tier callouts. This is a brand that sells precision-machined aluminum monitor arms, yet its color world reads like a craftsman's workshop: cool authority at the top, warm wood-tone depth wherever the human hand appears in product staging. That tension is resolved by a shared neutrality — charcoal (#282a2c) for near-black ink, chalky off-whites (#f5f5f7, #f3f3f3) for surface and canvas — keeping the palette cohesive without forcing either register to recede.

  Nunito Sans is an unusual choice for a B2B-adjacent hardware category. The rounded, humanist letterforms that make it comfortable in consumer wellness or education software here read as an accessibility signal: this is not industrial procurement software, it is a consumer who assembled their first standing desk and is ready to go further. Display headings sit at weight 800 and 28–40px, asserting product authority; body copy relaxes to weight 400 at a generous 1.6 line-height, inviting the spec-reading shopper to slow down and compare load ratings.

  Corner radii stay purposefully modest — `{rounded.sm}` (8px) on buttons and product cards, `{rounded.xs}` on badges — except in the search bar, which goes full-pill `{rounded.full}` in the pattern common to Shopify-native storefronts. The navy navigation bar carries no visible border-bottom; the background color alone creates the structural break, making the header feel engineered rather than decorated.

  The promo-pink (#f79ac2) appearing in the discount badge layer is the sharpest departure from the otherwise industrial tone: a single soft voltage, used at badge scale to flag clearance or seasonal offers, that does not appear as a primary surface anywhere. Together with the amber (#eab95b) savings chips and burnt-orange (#e6822e) promotional stripe, Mount-It! operates a layered discount-communication system — three distinct hues signaling three discount tiers — that competes for attention without undermining the navy-white authority of the main storefront.

colors:
  primary: "#154775"
  primary-active: "#0e3358"
  primary-disabled: "#7a9cba"
  accent-blue: "#52a2d8"
  accent-amber: "#eab95b"
  accent-orange: "#e6822e"
  sale-brown: "#964b00"
  promo-pink: "#f79ac2"
  error: "#be1414"
  ink: "#282a2c"
  body: "#4a4e52"
  muted: "#7a6c60"
  muted-warm: "#705f53"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  hairline-strong: "#a9aaab"
  canvas: "#ffffff"
  surface-soft: "#f5f5f7"
  surface-card: "#f3f3f3"
  surface-warm: "#faf5eb"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', Arial, -apple-system, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.32
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  price-display:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: -0.2px
  price-sm:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.36
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
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    border: "2px solid {colors.primary-active}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    focusBorder: "2px solid {colors.accent-blue}"
    errorBorder: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    logoHeight: 36px
  nav-top-stripe:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    imageBackground: "{colors.surface-soft}"
    overflow: hidden
    hoverShadow: "0 4px 20px rgba(21,71,117,0.12)"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.primary}"
  product-card-price-compare:
    typography: "{typography.price-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-promo:
    backgroundColor: "{colors.promo-pink}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-savings:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
    minHeight: 480px
    ctaButton: button-primary
  promo-stripe:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    fontWeight: 600
    height: 36px
    textAlign: center
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    iconColor: "{colors.muted}"
    focusBorder: "1px solid {colors.accent-blue}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  trust-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline-strong}"
    activeColor: "{colors.ink}"
  spec-table:
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.title-sm}"
    headerTextColor: "{colors.ink}"
    rowTypography: "{typography.body-sm}"
    rowTextColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    stripeBackground: "{colors.canvas}"
    rounded: "{rounded.sm}"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    height: 44px
    buttonColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.accent-blue}"
    mutedTextColor: "{colors.muted-warm}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — The primary action button runs a deep navy (#154775) fill on white text at `{rounded.sm}` (8px), 48px tall. The 14px top/bottom padding and 28px side padding give it a proportional heft suited to hardware CTA copy like "Add to Cart" and "Shop Now." On hover, the background drops to `{colors.primary-active}` (#0e3358); on disabled state, the fill lightens to `{colors.primary-disabled}` (#7a9cba) at full opacity so the button footprint remains legible in the layout without a cursor pointer.

**`button-secondary`** — A 2px navy border on white with navy text creates a contained outline button that pairs with the primary at equal 48px height. Hover shifts the fill to `{colors.surface-soft}` and tightens the border to `{colors.primary-active}`, keeping visual hierarchy clear when both buttons share a product-detail row.

**`button-ghost`** — Transparent background, `{colors.primary}` text, underline decoration. Used for lower-priority actions like "View full specs" or "Compare" within product cards and spec tables.

### Navigation

**`nav-top-stripe`** — A 36px announcement bar in `{colors.primary-active}` (#0e3358) sits above the main nav, used for shipping thresholds and promotional codes. Body copy is `{typography.caption}` in white, centered. This stripe collapses to hidden on mobile.

**`nav-bar`** — A 64px navy header using `{colors.primary}` as the background with white nav-link text at 14px/600 weight. No bottom border; the color break is structural. The desktop layout distributes category links (Monitor Mounts, Desk Mounts, TV Mounts, Standing Desks) across the center with a search icon and cart on the right. Dropdown menus (`nav-dropdown`) surface on a white card with a soft box-shadow.

### Product Cards

**`product-card`** — White card with a 1px `{colors.hairline}` border and `{rounded.sm}` radius. Product images sit on a `{colors.surface-soft}` (#f5f5f7) image panel; on hover, a `box-shadow: 0 4px 20px rgba(21,71,117,0.12)` elevation lifts the card. Badges layer over the image's top-left corner. Price displays at `{typography.price-display}` in `{colors.primary}`; a compare-at price in struck-through `{colors.muted}` sits inline to the right.

### Badges

**`badge-sale`** — Red (#be1414) fill on white text, 11px/700 uppercase. Flags items with a list-price discount. **`badge-new`** — Navy fill, same type. **`badge-promo`** — `{colors.promo-pink}` (#f79ac2) with ink text for limited promotions. **`badge-savings`** — `{colors.accent-amber}` (#eab95b) with ink text for bundle-savings or coupon callouts. The four badge types operate at `{rounded.xs}` (4px) so they read as labels rather than pills.

### Hero Banner

**`hero-banner`** — Full-bleed navy section at 480px minimum height. Heading in `{typography.display-xl}` (40px/800) on white, body copy in `{typography.body-md}`, and a `button-primary` CTA. Right half typically contains a product lifestyle image cropped to bleed edge. On tablet, copy left-aligns at 50% width; on mobile, stacks with image above.

### Search Bar

**`search-bar`** — The one full-pill element in the system (`{rounded.full}`), 44px tall, sitting inside the nav or as a hero overlay. The pill form signals "entry point" against the otherwise rectilinear card-and-button language of the page. A search icon in `{colors.muted}` sits left of the placeholder text; on focus, the border shifts to `{colors.accent-blue}` (#52a2d8).

### Filter Chips & Trust Badges

**`filter-chip`** / **`filter-chip-active`** — Used in the product-listing sidebar and horizontal scroll bar on mobile to filter by mount type, compatibility, and load capacity. Inactive chips use `{colors.surface-soft}` fill; active chips invert to navy fill and white text, both at `{rounded.full}`.

**`trust-badge`** — Warm-cream (`{colors.surface-warm}`, #faf5eb) cards with a primary-colored icon and `{typography.body-sm}` body text. Displayed as a 3- or 4-up row beneath the add-to-cart block on product detail pages, covering free shipping, warranty, and return policy. The warm cream anchors the domestic-workshop warmth visible elsewhere in the palette.

### Spec Table & Quantity Stepper

**`spec-table`** — Two-column key/value table with a `{colors.surface-soft}` header row and alternating white rows. Used on product detail pages for load capacity, VESA compatibility, tilt range, and cable management specs.

**`quantity-stepper`** — Inline –/+ stepper at 44px height with a `{colors.hairline}` border and `{rounded.sm}`, matching input field geometry so the PDP form row reads as a cohesive unit.

### Promotional Stripe

**`promo-stripe`** — 36px banner in `{colors.accent-orange}` (#e6822e) that can replace or layer beneath the top stripe for sitewide sale events. Text is `{colors.ink}` at `{typography.body-sm}` weight 600 for contrast on the warm orange.

### Footer

**`footer`** — Dark charcoal (#282a2c) background with a 3px navy (`{colors.primary}`) top border as the only decorative element. Link columns in `{typography.body-sm}`; heading labels in `{typography.title-sm}` white. Inline links use `{colors.accent-blue}` (#52a2d8) for legibility on the dark ground. Bottom strip contains legal copy in `{colors.muted-warm}` at `{typography.caption}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; `nav-top-stripe` hidden; hamburger nav replaces category links; filter chips scroll horizontally; hero copy stacks beneath product image; footer columns collapse to single accordion |
| Tablet | 744–1128px | 2-column product grid; nav links visible but condensed; hero splits 50/50 text and image; filter chips shift to collapsible drawer |
| Desktop | 1128–1440px | 3–4 column product grid with persistent left-rail filter sidebar; full nav with dropdown menus; hero at full 480px height |
| Wide | > 1440px | Content max-width ~1400px centered with equal side margins; grid stays at 4 columns; hero image expands to fill bleed |

### Touch Targets

- All interactive buttons and filter chips minimum 44px tall
- Quantity stepper buttons minimum 44×44px tappable area regardless of visual size
- Nav hamburger icon minimum 44px touch target
- Badge elements non-interactive; no minimum enforced

### Collapsing Strategy

- Category navigation collapses to hamburger at < 744px; mega-dropdown panels become full-screen slide-in sheets
- Product filter sidebar hidden by default on mobile/tablet, triggered by "Filter" button as a bottom sheet
- `nav-top-stripe` and `promo-stripe` merge into a single announcement strip on mobile to preserve vertical space
- Trust badges collapse from 4-up row to 2-up at tablet, 1-up stacked at mobile
- Spec table remains visible on all breakpoints; scrolls horizontally if column content overflows on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Nunito Sans font weight availability not confirmed from CSS inspection; weight 800 assumed from Nunito Sans variable range but may render as 700 on older delivery stacks
- Specific border-radius values for nav dropdown and modal overlays not extracted; `{rounded.sm}` assumed by analogy with card and button radii
- Cart drawer and checkout color states not captured; `{colors.primary}` assumed for checkout CTA continuity
- Icon set style (filled vs. outlined, stroke weight) not extractable from hex or font data; likely a generic line-icon set
- Hover and focus animation durations not confirmed; standard 150–200ms ease-in-out assumed
- Mobile nav mega-menu structure not confirmed; assumed slide-in sheet based on Shopify theme conventions
- `sale-brown` (#964b00) role is inferred from palette position; may be category-specific (clearance section background) rather than a UI component token
