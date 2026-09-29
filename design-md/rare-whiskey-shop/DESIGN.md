---
version: alpha
name: "The Rare Whiskey Shop"
source_url: "https://therarewhiskeyshop.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every bottle at The Rare Whiskey Shop arrives framed by a near-black cellar ground — #0e1311, three degrees below the #111111 site theme-color hint, a darkness that reads as vault rather than dark mode. Against that depth a single electric teal (#11b1a7) carries every interactive surface: add-to-cart buttons, hovered nav links, active filter chips, search submission, account actions, and in-stock availability indicators. The contrast is severe by design — a cold neon signal over stored bourbon, the digital equivalent of a single inspection lamp in a bonded warehouse. Two typefaces divide the page into editorial and commerce registers: Tenor Sans, a text-weight serif with long open ascenders, names bottles at 52px with near-zero tracking so that "Pappy Van Winkle 23-Year" carries auction-catalog authority; Outfit, a geometric sans with condensed proportions, covers all UI chrome — navigation links, filter labels, uppercase CTA caps, form fields — keeping every bottle name from reading like a menu item. A full amber gradient family codes the liquid itself: from warm gold (#ffb846) through burnt sienna (#e16f27) to deep copper (#d05b2e), the pour-spectrum appears in tasting-note color bands, pour-line decorative elements, and rating bar fills. Coral (#e7656e) and red-orange (#ff4f33) handle low-stock and alert callouts; deep crimson (#c20000) overlays sold-out bottles with a subdued warning register. Body copy runs in #e8e8e1, a warm near-ivory that reads like aged paper rather than a clinical screen — a temperature match for the bourbon context. Surface depth steps through dark registers — #1c1d1d for secondary panels, #231f20 for product cards, #2b2b2b for elevated controls and whiskey badge borders — each step barely perceptible in isolation but collectively giving the layout dimension without breaking the vault aesthetic. Buttons and cards share {rounded.sm} corners throughout; only pill-shaped collection-filter tags and review score chips reach {rounded.full}; everywhere else geometry holds close to rectilinear, echoing the hard edges of distillery label printing.

colors:
  primary: "#11b1a7"
  primary-active: "#18c1b6"
  primary-disabled: "#1c5f5b"
  teal-soft: "#5ddab1"
  whiskey-amber: "#ffb846"
  whiskey-orange: "#f48120"
  whiskey-warm: "#e16f27"
  whiskey-copper: "#d05b2e"
  coral: "#e7656e"
  danger: "#ff4f33"
  deep-red: "#c20000"
  payment-amex: "#006fcf"
  ink: "#f5f5f5"
  body: "#e8e8e1"
  muted: "#9a9a94"
  hairline: "#2b2b2b"
  canvas: "#0e1311"
  surface-soft: "#1c1d1d"
  surface-card: "#231f20"
  surface-elevated: "#2b2b2b"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Tenor Sans', Georgia, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.01em
  display-md:
    fontFamily: "'Tenor Sans', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.01em
  display-sm:
    fontFamily: "'Tenor Sans', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.01em
  title-md:
    fontFamily: "'Outfit', system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  button-md:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.04em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.04em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.02em
  price-display:
    fontFamily: "'Tenor Sans', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  label-caps:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.08em
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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    borderColor: "{colors.primary}"
    borderWidth: 1px
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    outlineWidth: 2px
    outlineColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottomColor: "{colors.hairline}"
    borderBottomWidth: 1px
    activeLinkColor: "{colors.primary}"
    logoTypography: "{typography.display-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
    nameTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    hoverBorderColor: "{colors.primary}"
    hoverBorderWidth: 1px
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 600px
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
    overlayColor: "rgba(14, 19, 17, 0.6)"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
    salePriceColor: "{colors.coral}"
    originalPriceColor: "{colors.muted}"
    currencyFontSize: 18px
  whiskey-badge:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.whiskey-amber}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    borderColor: "{colors.whiskey-amber}"
    borderWidth: 1px
  age-statement:
    textColor: "{colors.whiskey-amber}"
    typography: "{typography.display-sm}"
    backgroundColor: transparent
  collection-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  review-badge:
    backgroundColor: "{colors.teal-soft}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  stock-alert:
    backgroundColor: "rgba(194, 0, 0, 0.12)"
    textColor: "{colors.deep-red}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    borderColor: "{colors.deep-red}"
    borderWidth: 1px
  amber-rating-bar:
    fillColor: "{colors.whiskey-amber}"
    trackColor: "{colors.surface-elevated}"
    height: 4px
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.xl}"
    borderTopColor: "{colors.hairline}"
    borderTopWidth: 1px

## Components

### Buttons

**`button-primary`** — Filled teal (#11b1a7) on the near-black canvas, 48px tall at {rounded.sm} with uppercase Outfit at 15px/600 weight and 0.04em tracking. Hover brightens to the active teal (#18c1b6); disabled drops to a dark muted teal (#1c5f5b) with subdued text. Used exclusively for primary purchase actions: "Add to Cart", "Buy Now", "Reserve Allocation", "Notify Me When Available".

**`button-secondary`** — Transparent background with a 1px teal (#11b1a7) border and teal text on dark ground. Same 48px height and {rounded.sm} radius as the primary. Used for secondary product actions: "Add to Wishlist", "View Details", and filter resets where a ghosted border feels appropriate alongside a filled sibling.

**`button-ghost`** — No border, no background fill, ink text (#f5f5f5) in Outfit 13px/600 caps at {rounded.xs}. Used for inline navigation controls, "View All" links that need button semantics, and modal dismissals.

### Form Inputs

**`text-input`** — Dark panel surface (#1c1d1d) with 1px #2b2b2b border and {rounded.xs} radius. Placeholder text in muted (#9a9a94), entered value in ink (#f5f5f5). On focus, a 2px solid teal (#11b1a7) outline replaces the hairline border, carrying the primary brand voltage into keyboard navigation. Height 48px to match button height for side-by-side search rows.

### Navigation

**`nav-bar`** — Full-width at 72px tall, canvas (#0e1311) background with a 1px #2b2b2b bottom border. Brand name rendered in Tenor Sans at display-sm scale. Nav links in Outfit 14px/500 with teal (#11b1a7) on hover and active states. Cart icon shows a teal-filled count badge on {rounded.full}. The bar stays affixed at the top on scroll.

### Products

**`product-card`** — #231f20 surface at {rounded.sm} with 16px internal padding. Bottle photography fills a 3:4 aspect ratio container occupying the upper portion of the card. Bottle name in Outfit 18px/600 below the image, price in Tenor Sans 28px beneath that. On hover, a 1px teal border traces the full card perimeter. A `whiskey-badge` showing age statement or distillery sits top-left over the photograph.

**`price-display`** — Tenor Sans 28px/400 in ink (#f5f5f5). When a sale price is present, the new price renders in coral (#e7656e) and the original price in muted (#9a9a94) with strikethrough. Currency symbol drops to 18px inline with the mantissa.

**`whiskey-badge`** — Compact pill on {rounded.xs} with #2b2b2b fill and 1px #ffb846 amber border. Label text in Outfit caps 11px/700 at 0.08em tracking, amber (#ffb846) colored. Used for age statements (e.g., "23 Year"), distillery abbreviations, cask type, bottling lot, and proof designations on product cards and detail pages.

**`age-statement`** — Tenor Sans 24px/400 in whiskey-amber (#ffb846), no background. Appears as an editorial overlay on bottle hero images and as a standalone display element within the product detail pane, giving the age statement the same visual register as a label cartouche.

**`collection-filter`** — {rounded.full} pill, #1c1d1d default fill with #e8e8e1 body text in 12px caption type. Active state fills solid teal (#11b1a7) and switches text to white. Used across distillery, region, age range, proof, and availability filter rows. Filters horizontally scroll on mobile without wrapping.

**`review-badge`** — {rounded.full} pill in teal-soft mint (#5ddab1) with near-black (#0e1311) canvas text in Outfit caps 11px. Displays aggregate review scores pulled from Reviews.io. The mint-on-black provides clear contrast without overlapping with the primary teal reserved for purchase CTAs.

**`stock-alert`** — Translucent crimson background (rgba(194, 0, 0, 0.12)) with deep-red (#c20000) text and matching 1px border at {rounded.xs}. Triggers for "Only 2 Remaining", "Sold Out", and allocation-limit notices. Occupies a fixed position below the price row on product detail pages.

**`amber-rating-bar`** — 4px-tall horizontal track at {rounded.full}. Fill color is whiskey-amber (#ffb846); empty track is surface-elevated (#2b2b2b). Used in tasting-note breakdowns and aggregate score visualizations on product detail and collection pages.

**`hero-banner`** — Full-viewport section with 600px minimum height. Canvas background (#0e1311) with a rgba(14, 19, 17, 0.6) overlay when full-bleed bottle photography is placed behind content. Headline in Tenor Sans 52px with a single button-primary CTA. 64px vertical padding at each edge. Feature collections use this component with amber-toned photography of rare bottles on dark felt or oak surfaces.

**`footer`** — #1c1d1d background with a 1px #2b2b2b top border. Body-sm Outfit text in #e8e8e1, anchor links in teal (#11b1a7). 48px vertical padding. Structured in four columns: Shop by Category, About, Customer Support, and Social/Newsletter. Newsletter input field uses the `text-input` component inline with a `button-primary` at reduced width.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero headline drops to 32px Tenor Sans; filter row becomes horizontal scroll strip; price and add-to-cart stack vertically on product detail; whiskey-badge repositions below bottle name |
| Tablet | 744–1128px | Two-column product grid; top nav links visible up to four items; hero retains 52px headline; filters wrap in two rows; product detail shifts to two-column layout |
| Desktop | 1128–1440px | Three- to four-column product grid; full 72px nav bar; hero at full 600px minimum height; left-sidebar filter panel on collection pages; bottle detail at 60/40 image/info split |
| Wide | > 1440px | Content centers at 1440px max-width with full-bleed background; hero photography expands edge-to-edge; product grid holds four columns with wider gutters |

### Touch Targets
- All buttons minimum 48px tall and 48px wide
- Collection-filter pills minimum 40px tall on mobile
- Product card tap region covers full card face including image area
- Cart, search, and account icons in nav bar minimum 44×44px hit area
- Whiskey-badge and stock-alert tap areas padded to 36px minimum height on mobile

### Collapsing Strategy
- Top navigation collapses to hamburger drawer + centered logo + cart icon below 744px; drawer slides in from left over a dark scrim
- Filter panel transitions from persistent left sidebar (desktop) to bottom-anchored drawer triggered by a "Filter" pill button (mobile)
- Age-statement overlay and whiskey-badge stack below the product name on small viewports rather than overlaying the image
- Hero text block moves to a semi-transparent panel pinned to the bottom of the banner image on mobile for readability over photography
- Footer columns stack single-column below 744px with 32px gap between sections

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Muted text color (#9a9a94) is derived from the palette temperature range, not directly extracted; actual in-use value may differ
- Exact font-weight variations for Tenor Sans beyond weight 400 not confirmed; the typeface is typically single-weight, so 400 is assumed throughout
- Hover and active border hex for button-secondary not directly extracted; derived from primary token (#11b1a7)
- Review star color not confirmed from extraction; assumed to follow whiskey-amber (#ffb846) given palette context
- Exact product grid column breakpoints not extracted; standard Shopify Dawn/Debut responsive breakpoints assumed
- Icon set or SVG library (navigation icons, cart glyph, search icon) not identifiable from extraction
- Specific Shopify section schema structure and metafield keys for age statement and distillery data not extracted
- Payment badge colors beyond American Express blue (#006fcf) not confirmed; additional payment icons (Visa, Mastercard) likely present but hex values not in extraction
- Exact letter-spacing and size for Tenor Sans display-xl on mobile not confirmed; breakpoint scaling is estimated
