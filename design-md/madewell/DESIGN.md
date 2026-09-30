---
version: alpha
name: "Madewell"
source_url: "https://madewell.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The near-square corner on a Madewell primary button — {rounded.xs}, just 2px of radius — is the first structural tell: a brand anchored in selvedge denim and workwear heritage treats softened edges as decoration it doesn't need. The palette is almost entirely warm neutrals — a slightly creamy canvas (#FAFAF8) as the page base, near-black (#1A1A1A) for primary CTAs and body ink — with one chromatic departure: a muted selvedge-indigo (#4A6080) that surfaces in hover accents and collection spotlights, present enough to signal the denim identity without performing it. Display headlines run in an editorial serif at light-to-regular weight (400–500), making category headers read like spreads from a worn paperback rather than retail signage; UI labels, filter text, and prices drop into a clean geometric sans with consistent tracking. Product photography is the real visual currency: grid-card images sit flush to card edges with no border-radius ({rounded.none}), letting raw hem detail and lived-in fabric texture own the full frame. Spacing follows an 8pt rhythm — {spacing.lg} (24px) inside product cards, {spacing.section} (64px) between editorial modules — giving the page an unhurried cadence that reads more like a catalog than a conversion funnel. Sale indicators and clearance callouts arrive in a single accent red (#C0392B), the only warm hue in the system, preserving its urgency rather than distributing it across decorative chrome. The footer inverts the palette — warm cream text ({colors.on-dark}) on dark charcoal (#2A2A2A) — signaling a transition from commerce to brand narrative; it holds email capture, social links, and a small-caps navigation grid. Every hover, focus, and disabled state functions in grayscale: the visual logic trusts that indigo-washed denim and raw cotton are the only accents the brand requires.

colors:
  primary: "#1A1A1A"
  primary-active: "#000000"
  primary-disabled: "#9A9A9A"
  accent-indigo: "#4A6080"
  accent-indigo-hover: "#3A5070"
  sale-red: "#C0392B"
  ink: "#1A1A1A"
  body: "#3A3A3A"
  muted: "#767676"
  hairline: "#E0DFDB"
  hairline-soft: "#EEEDE9"
  canvas: "#FAFAF8"
  surface-soft: "#F5F3EF"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  footer-bg: "#2A2A2A"
  on-dark: "#F5F3EF"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-caps:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.06em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.06em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  filter-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
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
    rounded: "{rounded.xs}"
    padding: "14px 24px"
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.ink}"
    padding: "13px 23px"
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    height: 48px
    padding: "0 {spacing.base}"
  text-input-error:
    border: "1px solid {colors.sale-red}"
    textColor: "{colors.sale-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    logoAlignment: center
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
    imageRounded: "{rounded.none}"
  promo-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-caps}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageRounded: "{rounded.none}"
    titleTypography: "{typography.body-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.body}"
    priceSaleColor: "{colors.sale-red}"
    swatchGap: "{spacing.xs}"
    padding: "{spacing.sm} 0"
  sale-badge:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-caps}"
    rounded: "{rounded.none}"
    padding: "3px {spacing.sm}"
  new-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-caps}"
    rounded: "{rounded.none}"
    padding: "3px {spacing.sm}"
  color-swatch-dot:
    width: 16px
    height: 16px
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    borderSelected: "2px solid {colors.ink}"
    gap: "{spacing.xs}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    borderUnavailable: "1px solid {colors.hairline-soft}"
    textColorUnavailable: "{colors.primary-disabled}"
    width: 44px
    height: 44px
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.on-primary}"
    subTypography: "{typography.body-md}"
    imageRounded: "{rounded.none}"
    ctaStyle: button-primary
    textAlignment: center
    overlayOpacity: 0.18
  filter-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.filter-label}"
    borderRight: "1px solid {colors.hairline}"
    headerTypography: "{typography.caption-caps}"
    width: 280px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    gap: "{spacing.sm}"
  category-tile:
    imageRounded: "{rounded.none}"
    labelTypography: "{typography.display-sm}"
    labelColor: "{colors.on-primary}"
    overlayOpacity: 0.10
    hoverOverlayOpacity: 0.22
    hoverImageScale: 1.03
    hoverTransition: "300ms ease"
  footer-band:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    linkTypography: "{typography.caption}"
    padding: "{spacing.xxl} 0"
    gridColumns: 4

## Components

### Buttons

**`button-primary`** — A filled near-black (#1A1A1A) rectangle with {rounded.xs} (2px) corners, uppercase letter-spaced button-md type, and a fixed 48px height. Hover tightens to pure black (button-primary-active); disabled bleaches to warm gray (#9A9A9A) at the same geometry. The uppercase setting and 0.06em tracking give CTAs dry, editorial authority — no pulse animation, no shadow elevation on hover, just the color shift.

**`button-secondary`** — Transparent fill with a 1.5px ink border and identical uppercase button-md type, 48px tall. Hover inverts to the filled primary appearance — a clean binary flip with no intermediate state. Used for secondary actions like "Add to Wishlist" and "View Details" when a primary action already anchors the view.

**`button-text`** — Inline underlined body-sm, no border or fill. Carries tertiary actions in product descriptions, account management flows, and return policy references. The underline is the only affordance — consistent with the brand's low-decoration UI philosophy.

### Text Input

**`text-input`** — Flat 1px hairline border at rest, sharpening to ink on focus; {rounded.xs} corners, 48px tall. Placeholder text renders in muted ({colors.muted}); the label sits above the field in body-sm. Error state swaps the border to sale-red and tints the label message to match. No box shadow, no glow ring — the field sits flush on canvas without elevation.

### Navigation

**`nav-bar`** — 56px tall, canvas background, hairline bottom border. Logo centers in the horizontal axis; account, search, and bag icons cluster to the right at 44×44px minimum tap areas; top-level category links distribute left or center depending on count. nav-link type is 13px/500 weight with 0.02em tracking. The bar remains fixed on scroll with no additional shadow — the hairline border is the sole vertical separator.

**`nav-dropdown`** — Full-width editorial panel below the nav-bar, triggered on hover. Canvas fill, hairline top border, two-to-four-column grid inside: editorial campaign image flush left ({rounded.none}), category sub-links in body-sm columns, a featured product tile at right. No page scrim or overlay — the dropdown sits above content without dimming it.

**`promo-banner`** — 36px strip pinned above the nav-bar in surface-soft (#F5F3EF), promotional copy in caption-caps (11px, uppercase, 0.08em tracking), centered. No dismiss icon in the default single-message state; a left/right chevron pair appears when multiple promos rotate. Background stays within the warm-neutral register — never red or ink, which are reserved for higher-urgency signals.

### Product Card

**`product-card`** — Photography fills the full card width at zero border-radius ({rounded.none}), preserving the raw, unframed quality of editorial denim imagery. Below the image: product name in body-sm ({colors.ink}), price in price-display ({colors.body}), sale price in sale-red with the original struck through in muted. Color swatch dots are 16px circles ({rounded.full}) with a hairline border at rest and a 2px ink ring when selected, arranged in a horizontal row with {spacing.xs} gaps. On hover, a quick-add button (button-primary, 40px height) appears absolutely positioned at the card bottom.

### Badges

**`sale-badge`** — Zero-radius rectangle ({rounded.none}) in sale-red (#C0392B) with on-primary text in caption-caps, pinned to the top-left corner of the product image. No drop shadow or border. The flat, hard-edged badge reads as matter-of-fact rather than promotional — one instance of the only warm hue in the system.

**`new-badge`** — Same geometry and type style as sale-badge, filled with ink (#1A1A1A). Stacks below the sale-badge if both conditions apply, or appears alone for new-arrival products.

### Size Selector

**`size-selector`** — 44×44px squares with {rounded.none}, 1px hairline border at rest, switching to 1px ink border on selection. Unavailable sizes receive a CSS diagonal strikethrough line and hairline-soft border with disabled text color (#9A9A9A). The size grid auto-flows left-to-right, wrapping at container width, with {spacing.xs} between cells. No background fill change on hover — border weight is the only active signal.

### Filter Drawer

**`filter-drawer`** — 280px side panel entering from the left on desktop, hairline right border, canvas fill. Filter group titles render in caption-caps (11px uppercase), individual options in filter-label (13px/400). Accordion sections animate height on expand/collapse. Applied filter count appears as a small ink-fill badge next to the group title. A "Clear All" button-text appears at the top of the drawer when any filters are active.

### Hero Editorial

**`hero-editorial`** — Full-bleed image with an 18% dark overlay concentrated at the lower third. Headline in display-xl (40px serif, 400 weight) centered and in on-primary; a single button-primary sits {spacing.lg} (24px) below it. On mobile, the image crops to a 4:5 ratio, headline drops to display-md (28px), and padding tightens. No carousel auto-play in the default hero — a static editorial frame is preferred over motion.

### Category Tile

**`category-tile`** — Square or portrait editorial image at {rounded.none}, carrying the category name in display-sm (22px serif) bottom-anchored with a 10% overlay. Hover scales the image to 1.03 over 300ms ease and deepens the overlay to 22%, maintaining text legibility without a separate text background. Used in homepage 3- or 4-column category navigation grids.

### Footer

**`footer-band`** — Dark charcoal (#2A2A2A) background reversing the page polarity, on-dark text (#F5F3EF, warm cream). Four-column grid: brand sub-navigation in caption, email capture using the text-input style with an inline button-primary submit, social icon links, and legal/copyright in caption at 60% opacity. Hover states on footer links use on-dark at 80% opacity — no separate accent color introduced in this layer.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero crops to 4:5 portrait with display-md headline; nav-bar collapses to hamburger + centered logo + bag; filter drawer becomes full-width bottom sheet; promo-banner single line with ellipsis overflow |
| Tablet | 744–1128px | 2-column product grid; nav shows top-level categories inline, sub-navigation in hamburger accordion; filter drawer is modal overlay; hero full-width at maintained aspect ratio |
| Desktop | 1128–1440px | 3-column product grid; full nav-bar with hover mega-dropdown; filter sidebar in-page at 280px; hero at full bleed; promo-banner shows full message |
| Wide | > 1440px | 4-column product grid; max-width container (1440px) centered on canvas; hero image capped at 680px max-height; footer grid stays 4-column |

### Touch Targets

- All buttons minimum 48×48px tap area
- Size selector cells 44×44px visible; tight grids add invisible 8px padding halo to meet 44px minimum
- Nav icons (bag, account, search) 44×44px minimum
- Color swatches 16×16px visual; 36×36px touch target via padding expansion
- Filter accordion rows minimum 44px tall with full-width tap area
- Breadcrumb links minimum 36px tall

### Collapsing Strategy

- Primary navigation collapses to hamburger below 1128px; mega-dropdown becomes stacked accordion inside the drawer
- Product grid steps 4→3→2→1 columns at 1440→1128→744→375px breakpoints
- Footer 4-column grid collapses to 2-column at tablet, 1-column at mobile; email capture floats to top of the mobile footer stack
- Promo-banner hides overflow text with ellipsis at mobile; left/right chevron rotation used only when multiple promos are configured
- Hero text repositions to bottom-aligned at mobile to avoid placement over complex image regions; overlay opacity increases slightly for contrast safety

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted (site returned HTTP 403 / "Access Denied"); all palette values are inferred from widely observed Madewell brand documentation — treat as approximate and verify against live CSS custom properties or computed styles
- No font stacks were extracted; display typography uses Georgia as a system-serif placeholder — Madewell likely uses a licensed editorial serif (possibly Tiempos Text, Canela, or equivalent); inspect computed font-family on headings before implementation
- Meta theme-color unavailable; mobile browser chrome color is unspecified
- Exact button border-radius unconfirmed; 2px ({rounded.xs}) is inferred from visual analysis suggesting near-square corners
- Accent indigo (#4A6080) is a brand-knowledge inference from the denim heritage; the precise production hex for link hover states and collection accents needs live extraction
- Dark-mode or high-contrast variant is unknown; this spec assumes light-mode only
- Exact nav-bar height (56px) is an estimate; verify against live layout measurements
- Wishlist icon-button style not fully specified; assumed as ink-stroke heart on transparent background, no fill, 44×44px tap target
- Animation durations and easing curves for hover states, dropdown appearance, and filter drawer are estimated at common defaults (200–300ms ease); extract from computed transitions on live site
