---
version: alpha
name: "Mugsy Jeans"
source_url: "https://mugsyjeans.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  An electric blue (#3366ff) CTA button sitting on a near-white field is Mugsy's first visual declaration — a denim brand that treats stretchability as a performance specification rather than a fabric footnote, and the interface encodes that logic at every layer. The type stack leads with Hind, a compressed humanist sans-serif that reads hard-working rather than aspirational, running tight negative letter-spacing on display-xl headlines and a comfortable 1.5 line-height through body copy. Fire-engine red (#fc0000) intercepts the scroll at sale callouts and urgency triggers; saturated yellow (#ffd200) badges frame bestsellers and new-arrival signals in a register closer to a streetwear drop calendar than department-store signage. Beneath this high-contrast CTA layer the page breathes in pale surface tones — #f4f4f6 cards on #f7f7f8 backgrounds — while muted blue-gray (#676986) handles secondary labels in sizing grids and filter menus without competing with the product imagery. A dark navy (#272d45) grounds both the announcement bar at the top and the footer at the bottom, anchoring the scroll with consistent brand gravity. The {rounded.full} pill shape appears on promotional badges exclusively — sale chips, bestseller tags, new-arrival flags — never on primary action buttons, which hold at {rounded.sm} to signal utility over softness. Color swatches mirror the pill logic with fully circular dots, while size swatches stay rectangular, reinforcing the brand's functional register. Full-width hero sections run edge-to-edge photography against dark overlays with no softening radius at the viewport break, keeping the performance-brand energy intact from first impression through checkout.

colors:
  primary: "#3366ff"
  primary-active: "#2267d8"
  primary-disabled: "#a8bfff"
  ink: "#202020"
  body: "#1f2937"
  muted: "#676986"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#f7f7f8"
  surface-subtle: "#f4f4f6"
  on-primary: "#ffffff"
  sale-red: "#fc0000"
  sale-red-dark: "#b32c2e"
  badge-yellow: "#ffd200"
  badge-mint: "#b2f9e9"
  success: "#22c55e"
  warning: "#f59e0b"
  info-blue: "#38bdf8"
  dark-navy: "#272d45"
  dark-alt: "#2c3e50"
  scrim: "#202020"

typography:
  display-xl:
    fontFamily: "'Hind', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Hind', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Hind', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Hind', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Hind', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Hind', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Hind', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Hind', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge-label:
    fontFamily: "'Hind', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Hind', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Hind', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Hind', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Hind', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'Hind', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "'Hind', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
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
    border: "2px solid {colors.ink}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  button-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.dark-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageBorderRadius: "{rounded.xs}"
    padding: "{spacing.md}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
  sale-badge:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  bestseller-badge:
    backgroundColor: "{colors.badge-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  new-badge:
    backgroundColor: "{colors.badge-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  promo-chip:
    backgroundColor: "{colors.badge-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 14px
  price-sale-display:
    salePriceColor: "{colors.sale-red}"
    comparePriceColor: "{colors.muted}"
    salePriceTypography: "{typography.price-sale}"
    comparePriceTypography: "{typography.price-compare}"
    compareTextDecoration: line-through
  hero-section:
    backgroundColor: "{colors.dark-navy}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-md}"
    minHeight: 560px
    paddingX: "{spacing.xl}"
    paddingY: "{spacing.section}"
  size-swatch:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.ink}"
    selectedBackgroundColor: "{colors.ink}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 36px
    minWidth: 44px
    padding: 0 8px
  color-swatch:
    borderColor: "{colors.hairline-soft}"
    selectedBorderColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 28px
    width: 28px
  rating-stars:
    activeColor: "{colors.badge-yellow}"
    inactiveColor: "{colors.hairline}"
    typography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.dark-navy}"
    textColor: "{colors.on-primary}"
    linkColor: "#dbdde4"
    dividerColor: "#272d45"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    overlayColor: "{colors.scrim}"
    overlayOpacity: 0.5
    titleTypography: "{typography.title-md}"
    lineItemTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"

## Components

### Buttons

**`button-primary`** — The primary action surface runs `{colors.primary}` (#3366ff), an electric blue that treats add-to-cart and checkout with the same urgency as a performance spec callout. Active state darkens to `{colors.primary-active}` (#2267d8); disabled washes to `{colors.primary-disabled}` (#a8bfff) with white label retained. The uppercase `{typography.button-md}` treatment at 0.5px tracking gives it the weight of a technical label rather than a soft consumer invite.

**`button-secondary`** — White canvas fill with a solid 2px ink border, same uppercase `{typography.button-md}` as primary. Used for secondary CTAs like "View All", "Learn More", or quiz-entry prompts where the primary blue would compete.

**`button-sale`** — Fire-engine red (#fc0000) reserve deployed exclusively for sale-event CTAs, clearance triggers, and limited-run urgency states. Shares identical padding, height, and `{rounded.sm}` radius as `button-primary` to prevent layout shift on swap between sale and non-sale states.

**`button-ghost`** — Transparent fill with a 1px `{colors.primary}` border, used for tertiary actions like "View Details" on hover states or non-critical navigation nudges. Smaller `{typography.button-sm}` scale keeps visual weight low.

### Navigation

**`nav-bar`** — White canvas, 64px height, `{colors.hairline}` bottom border. Logo left; main categories in `{typography.nav-link}` uppercase 14px/600. Sits beneath the `announcement-bar`, which runs the full width in `{colors.dark-navy}` (#272d45) with white 12px caption text cycling free-shipping thresholds and promotional codes.

### Product Cards

**`product-card`** — Minimal card with `{rounded.xs}` image corners on `{colors.surface-card}` (#f7f7f8) background. Product title renders in `{typography.title-sm}`; price in `{typography.price}`. Up to three badge slots stack in the top-left corner of the product image: sale (red), bestseller (yellow), or new-arrival (mint). Color swatches appear below the image as 28px circular dots before the add-to-cart button.

### Badges

**`sale-badge`** — `{colors.sale-red}` (#fc0000) pill using `{rounded.full}`, all-caps 11px `{typography.badge-label}`. Appears both on PLP card image overlays and PDP header sections.

**`bestseller-badge`** — `{colors.badge-yellow}` (#ffd200) pill with `{colors.ink}` text at the same geometry as sale-badge. Provides social-proof anchoring on high-velocity SKUs.

**`new-badge`** — `{colors.badge-mint}` (#b2f9e9) pill with ink text. Marks seasonal drops and new colorway introductions without the urgency of the red/yellow palette.

### Hero Section

**`hero-section`** — Full-viewport-width panel, typically dark-navy (#272d45) or full-bleed photography with a dark overlay. `{typography.display-xl}` headline in white, `{typography.body-md}` subtitle, and a `button-primary` or `button-sale` CTA left-aligned or centered depending on campaign. Hard edge at viewport break — no radius, no soft vignette — consistent with the brand's performance register.

### Product Detail Swatches

**`size-swatch`** — Rectangular chip, minimum 44px touch width, 36px height. Default state: white background, `{colors.hairline}` border. Selected: inverted to `{colors.ink}` fill with white text. Sold-out sizes receive a muted treatment; confirmed with a diagonal line or grayed label.

**`color-swatch`** — 28px circular dot ({rounded.full}) with a thin `{colors.hairline-soft}` default ring that tightens to `{colors.ink}` on selection.

### Price Display

**`price-sale-display`** — Sale price renders in `{colors.sale-red}` using `{typography.price-sale}`; the original compare-at price sits beside it in `{colors.muted}` with line-through decoration via `{typography.price-compare}`. Both appear inline at the same vertical baseline.

### Cart Drawer

**`cart-drawer`** — Right-side sliding panel on `{colors.canvas}`, title in `{typography.title-md}`, line items in `{typography.body-sm}` and `{typography.price}`. Behind the open drawer, a `{colors.scrim}` overlay at 50% opacity dims the PDP without a hard black blackout.

### Footer

**`footer`** — Dark navy (#272d45) background mirroring the announcement bar, creating visual bookends on the page scroll. Column headings in `{typography.title-sm}` white; body links in slightly softened #dbdde4 for legibility without full contrast.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column PLP grid; nav collapses to hamburger drawer; hero stacks text vertically over full-bleed image; CTA buttons go full-width; size/color swatches scroll horizontally |
| Tablet | 744–1128px | 2-column PLP grid; nav may show top-level categories inline with a dropdown trigger; hero switches to side-by-side split layout |
| Desktop | 1128–1440px | 3–4 column PLP grid; full horizontal nav with hover dropdowns; hero runs full-bleed with left-aligned text overlay and constrained max-width content column |
| Wide | > 1440px | Content max-width caps around 1440px with auto horizontal margins; hero image bleeds to viewport edge while text column holds at grid width |

### Touch Targets

- All buttons minimum 44px height
- Size swatches minimum 44px touch width × 36px height
- Color swatches padded to 40px tap zone despite 28px visual size
- Nav links 44px tap zone in mobile hamburger drawer
- Add-to-cart on mobile is full-width, 48px height
- Badge chips not interactive; no minimum required

### Collapsing Strategy

- Primary nav: hamburger side drawer on mobile; horizontal link row with dropdowns on desktop
- Filters: bottom-sheet or full-screen drawer on mobile; sticky left sidebar on desktop PLP
- Product image gallery: single swipeable carousel on mobile; thumbnail rail + main image on desktop
- Announcement bar: single static or rotating message on mobile; same on desktop with potential multi-message carousel
- Size guide: modal overlay on all breakpoints, triggered from size-swatch row

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface confirmed — Hind appears in the extracted font stack but is a standard Google Font; display-weight optical sizing and whether Mugsy uses a licensed or subset variant is unconfirmed
- Exact button border-radius not extractable; `{rounded.sm}` (8px) inferred from the brand's utilitarian aesthetic
- Nav dropdown and mega-menu internal color treatment not captured
- Hover and focus state colors for links, nav items, and swatches not extracted
- Mobile drawer overlay scrim exact opacity value not confirmed
- Whether `{colors.info-blue}` (#38bdf8) and `{colors.success}` (#22c55e) surface as in-page status indicators or only as Shopify system/admin defaults is uncertain
- Exact hero section text alignment (centered vs. left) varies by campaign and could not be pinned from static extraction
- Dark-mode support not confirmed; all tokens assume light-mode baseline
