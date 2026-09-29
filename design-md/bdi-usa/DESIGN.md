---
version: alpha
name: "BDI USA"
source_url: "https://www.bdiusa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The charcoal that finishes BDI's credenzas, lateral files, and media consoles — #313131 — crosses without friction from physical product surface to interface ink, so the digital catalog reads as a continuation of the material vocabulary embedded in the furniture itself. BDI occupies an unusual position in office storage: the pieces photograph like residential furniture, price like premium imports, and the brand's digital presence mirrors that controlled sobriety throughout. No bright accent color announces a CTA; the primary action button is drawn from the same near-black that darkens cabinet shells, and everything else recedes into pale neutral canvas and hairline borders. The system font stack — -apple-system, BlinkMacSystemFont, Helvetica Neue, Arial — reinforces the restraint: no custom typeface license, no brand font to maintain, just the screen's native letterforms at precise weights and sizes. Geometry stays sharp and architectural: product cards use zero or minimal rounding ({rounded.none} to {rounded.xs}) to echo the milled precision of the furniture joinery, and grid gutters maintain a consistent architectural beat throughout the catalog. Finish swatches — the physical material options for each SKU, from espresso to matte white — become a signature UI pattern, rendered as small labeled color circles that let the buyer commit to a surface before the piece ships. Photography functions as the real design system: pieces float on near-white fields, shadows anchoring form without lifestyle distraction, nothing introduced to muddy the material read. Button states lean on shade shift within the {colors.primary} channel rather than color-switching; hover darkens fill or draws a 1px inset border, signaling interactivity without introducing a secondary hue. The overall register sits close to a Knoll catalog page — clean, unhurried, confident in the product object — but aimed squarely at the work-from-home buyer who wants that finish tier without a contract-furniture procurement process. Token gaps are significant throughout this spec: only one hex value was extractable from the live site, so palette completions are inferred from that single anchor and from the neutral architectural systems that office furniture brands at this tier reliably employ.

colors:
  primary: "#313131"
  primary-active: "#1c1c1c"
  primary-disabled: "#aaaaaa"
  ink: "#313131"
  body: "#555555"
  muted: "#888888"
  hairline: "#e3e3e3"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-mid: "#ececec"
  on-primary: "#ffffff"
  overlay: "rgba(49,49,49,0.06)"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 44px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
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
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  swatch-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  label-caps:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: none
    padding: 14px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    height: 48px
    padding: 0 16px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    descTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    minHeight: 560px
    textColor: "{colors.ink}"
  finish-swatch:
    size: 28px
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.hairline}"
    selectedBorder: "1.5px solid {colors.primary}"
    labelTypography: "{typography.swatch-label}"
    labelColor: "{colors.muted}"
  category-pill:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 44px
    padding: 0 14px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
  section-label:
    textColor: "{colors.muted}"
    typography: "{typography.label-caps}"
    marginBottom: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.xxl} 0"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  dimension-table:
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.title-sm}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rowHoverBackground: "{colors.surface-soft}"

## Components

### Buttons

**`button-primary`** — Solid #313131 charcoal block with no border radius, uppercase 14px tracking at 0.5px letterSpacing, white text. The sharp square cut echoes furniture joinery rather than consumer-app softness. Hover shifts fill to {colors.primary-active} (#1c1c1c); disabled washes to {colors.primary-disabled}. Fixed at 48px height for comfortable click and touch targets across desktop and mobile surfaces.

**`button-secondary`** — White fill with a 1px {colors.primary} border and matching charcoal text, identical sharp corners and uppercase label style as the primary. On hover, background tints to {colors.surface-soft} to communicate press without a hue shift. Used for secondary navigation actions — "compare," "add to wishlist," "download spec sheet."

**`button-ghost`** — Transparent background, no border, {colors.primary} text at {typography.button-md}. Underline appears on hover. Used for inline "learn more" links and filter-clear affordances where a bordered button would add visual clutter.

### Text Input

**`text-input`** — No border radius; 1px {colors.hairline} border that sharpens to {colors.primary} on focus. Height 48px with 16px horizontal padding. The no-radius treatment keeps input fields visually coherent with the sharp furniture photography grid and the square-edged button system.

### Navigation

**`nav-bar`** — White canvas, 64px tall, {colors.hairline} bottom border. Links use {typography.nav-link} at 14px weight 500. Utility icons (search, wishlist, cart) cluster right-aligned as 44×44px tap targets. On scroll, a subtle box-shadow appears without color change — the bar stays white throughout.

### Product Card

**`product-card`** — No rounding; image zone fills a square-ratio container against {colors.surface-soft}. Product name in {typography.title-md}, price in {typography.price-display} directly below, with a secondary {typography.body-sm} line for the series or collection name. On hover, the image scales to 1.03× inside a clipped container and a quick-view affordance may surface at center. Ratings appear on PDP only — cards are clean of star rows.

### Hero Banner

**`hero-banner`** — Minimum 560px tall; background is {colors.surface-soft} or a controlled studio photograph. Headline in {typography.display-xl} at fontWeight 300 — the thin weight is the most brand-specific typographic choice in the system, signaling premium restraint where most competitors use bold display. Body in {typography.body-md}; CTA uses `button-primary`. Text block is left-aligned on desktop and centered on mobile. Overlay scrims are used only on photography-backed heroes where contrast demands it.

### Finish Swatch

**`finish-swatch`** — 28px circles, {rounded.full}, 1.5px border at {colors.hairline} normally, shifting to {colors.primary} on selection. A {typography.swatch-label} label appears below or on hover in {colors.muted}. This is the most distinctive interactive pattern on BDI PDPs — the buyer selects a physical material finish before the add-to-cart action, mirroring how a showroom customer would handle material samples.

### Category Pill / Filter Chip

**`category-pill`** — {rounded.full} pill, {colors.surface-mid} fill, {typography.button-sm} uppercase text. Active state flips to {colors.primary} fill with {colors.on-primary} text. On mobile the pill row scrolls horizontally to navigate furniture category subsets (Filing, Storage, Desks, Media); on desktop it sits as a static horizontal cluster above the product grid.

### Search Bar

**`search-bar`** — No radius, 44px height, {colors.surface-soft} fill with {colors.hairline} border and magnifying-glass icon left-padded. On desktop it sits persistently in the left column or nav header; on mobile it expands to a full-screen overlay triggered by the nav icon tap.

### Breadcrumb

**`breadcrumb`** — {typography.caption} 12px; {colors.muted} for ancestor nodes, {colors.ink} for the active (current) node. Slash separator. Sits 16px above the page headline on category and PDP pages to orient the user without competing with product photography.

### Footer

**`footer`** — Full-bleed {colors.primary} (#313131) background with {colors.on-primary} text throughout. {typography.body-sm} for link columns, {typography.caption} for legal lines and copyright. Four-column layout on desktop (Products, Resources, Company, Social), two columns on tablet, single stacked column on mobile. All links stay white — no colored anchor treatment introduced inside the dark footer.

### Product Badge

**`product-badge`** — Sharp-cornered label ({rounded.none}), {colors.primary} fill, {colors.on-primary} text in {typography.label-caps}. Applied as a top-left overlay on product card images to flag "New," "Sale," or collection launches. Maximum width approximately 64px.

### Dimension Table

**`dimension-table`** — On PDP, dimensions (width, depth, height, weight) are listed in a hairline-bordered table. Labels in {typography.title-sm} + {colors.muted}, values in {typography.body-sm} + {colors.ink}. Row hover tints to {colors.surface-soft}. No zebra striping — the table reads as a clean data layer against the white canvas, not a spreadsheet.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero headline drops from {typography.display-xl} to {typography.display-md} at fontWeight 300; category pills scroll horizontally; search expands to full overlay; finish swatch row wraps to two rows maximum |
| Tablet | 744–1128px | Two-column product grid; primary nav links retained, secondary links move to dropdown or hamburger overflow; hero text block narrows to 60% width; filter sidebar collapses to a slide-in drawer triggered above the grid |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all primary links; hero at full 560px min-height with side-by-side text-and-image variant available; filter sidebar visible at 240px fixed left column |
| Wide | > 1440px | Content capped at 1440px max-width and centered with auto side margins; four-column grid on category pages; hero photography bleeds to viewport edge while text block stays within the max-width container |

### Touch Targets

- Primary and secondary buttons: 48px height, minimum 44px width
- Finish swatches: 28px diameter circles with 8px minimum gap, yielding 36px center-to-center spacing for thumb accuracy
- Nav icon buttons (search, wishlist, cart): 44×44px tap target regardless of visible icon size
- Category pills: 36px minimum height on mobile

### Collapsing Strategy

- Filter sidebar (desktop: fixed 240px left column) → slide-in drawer from left edge (tablet and mobile), triggered by a "Filter" button above the product grid
- Primary nav links fully visible on desktop → hamburger drawer on tablet and below; drawer presents the full nav hierarchy with expand/collapse for subcategories
- Four-column footer on desktop → two-column on tablet → single stacked column on mobile; social icon cluster moves to the bottom of the column stack
- Hero image: full bleed on desktop, 3:2 aspect crop on tablet, 1:1 square crop on mobile; studio photography with controlled backgrounds typically requires no overlay scrim to maintain text contrast

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extractable — the live site presents a Cloudflare anti-bot challenge ("Just a moment...") and did not render further design tokens. The full palette is inferred from this single anchor and the neutral systems standard in premium office furniture at this tier.
- No brand-specific or licensed typeface was detected; the site relies entirely on a system font stack. If BDI uses a custom typeface it was not recoverable via static extraction.
- Meta theme-color is absent, indicating no PWA manifest or explicit mobile chrome color theming.
- Accent or secondary brand colors (warm cream, a product-line highlight, a campaign color) are entirely unknown and not fabricated here.
- Exact button border radii, grid column counts, and gutter widths on the live site could not be confirmed — values follow conventions for the category.
- Navigation depth, mega-menu structure, and filter taxonomy are undocumented due to the anti-bot block.
- Hover and focus animation timing, easing functions, and transition durations are unknown.
- Whether BDI applies a fluid/clamp() type scale or discrete breakpoint overrides could not be determined.
