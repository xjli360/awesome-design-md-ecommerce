---
version: alpha
name: "Supreme"
source_url: "https://supremenewyork.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The red box sits flush against a white ground — no radius, no gradient, no shadow — and that binary graphic logic propagates through every surface on supremenewyork.com. A single voltage color, #ec1324 (the box logo red, in continuous use since 1994), appears on the primary call-to-action and nowhere else; the entire surrounding system is white (#ffffff), near-white (#f2f2f2), black, and a hairline-thin gray border that seems almost accidental. Drop culture is encoded in the layout itself: Thursday releases are rendered as a stark 4-column product manifest, not a lifestyle catalog — no editorial interstitials, no recommendation carousels, no promotional badges beyond a plain-text "NEW" label at the edge of the listing. Typography at the logo inherits from Barbara Kruger via Futura Heavy Oblique; the site's body and navigation run on a tightly tracked sans-serif at small sizes that reads as authority through minimalism rather than spectacle. `{rounded.none}` governs every interactive surface — every card edge, every button, every input field is a hard right angle. Spacing follows the same logic: the canvas is generous in emptiness but compressed within the product grid, so the tension between white space and density is the primary compositional gesture. Navigation collapses to a single shallow band — category links reading left to right, cart count in plain numerals on the right, no mega-menu, no promotional header strip. Sold-out states appear as direct text labels beside or below the size selector, not as disabled button styles, which preserves the aesthetic purity of the button at the cost of conventional visual feedback. The experience is deliberately anti-comfort in conventional UX terms: no upsell mechanics, no loyalty prompts, no personalization surface. The scarcity mechanism is the UI.

colors:
  primary: "#ec1324"
  primary-active: "#c20f1e"
  primary-disabled: "#f5a0a7"
  ink: "#000000"
  body: "#1a1a1a"
  muted: "#767676"
  hairline: "#dedede"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sold-out-label: "#767676"
  new-label: "#ec1324"
  scrim: "#000000"

typography:
  logo-display:
    fontFamily: "Futura, 'Futura PT', 'Century Gothic', sans-serif"
    fontSize: 24px
    fontWeight: 900
    fontStyle: italic
    lineHeight: 1.0
    letterSpacing: 0.02em
    textTransform: uppercase
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.05em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.03em
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.04em
  product-name:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
    textTransform: uppercase
  price-display:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  label-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.1em
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
    rounded: "{rounded.none}"
    padding: 10px 16px
    height: 40px
    border: none
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 9px 15px
    height: 40px
    border: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 8px 10px
    height: 36px
    focusBorder: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 44px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.base}"
  category-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    activeTextColor: "{colors.primary}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xs} 0"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageBorder: "1px solid {colors.hairline-soft}"
    nameTypography: "{typography.product-name}"
    priceTypography: "{typography.price-display}"
    gap: "{spacing.xs}"
    padding: "{spacing.sm} 0"
  product-grid:
    columns: 4
    gap: "{spacing.sm}"
    padding: "{spacing.base}"
    backgroundColor: "{colors.canvas}"
  hero-drop-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xl} {spacing.section}"
    rounded: "{rounded.none}"
  announcement-strip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-sm}"
    height: 32px
    padding: "0 {spacing.base}"
  new-badge:
    backgroundColor: "{colors.new-label}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: "2px {spacing.xs}"
  sold-out-label:
    textColor: "{colors.sold-out-label}"
    typography: "{typography.label-sm}"
    backgroundColor: transparent
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 6px 10px
    selectedBorder: "1px solid {colors.ink}"
    soldOutOpacity: 0.35
  drop-date-label:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    backgroundColor: transparent
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "6px {spacing.sm}"
    height: 32px
  product-detail-title:
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    marginBottom: "{spacing.sm}"
  logo-box:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.logo-display}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  cart-count:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    backgroundColor: transparent
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.base}"
    linkColor: "{colors.ink}"

## Components

### Buttons

**`button-primary`** — A flat, zero-radius rectangle filled with Supreme red (#ec1324) and white uppercase text at 14px/700 weight with 0.08em tracking. Label convention is all-caps ("ADD TO CART"); the button typically spans the container width on product detail pages and sits directly below the size selector. Active state deepens the fill to #c20f1e; disabled state renders the fill in a pale pink (#f5a0a7) with no label change. No shadow, no hover fill shift — cursor change is the only hover affordance.

**`button-secondary`** — Identical geometry and typography to `button-primary` but with a white fill and a 1px solid black border. Used for secondary actions such as "Find a Store" or size-guide triggers. Hard corners throughout; border remains at full ink weight on hover.

### Navigation

**`nav-bar`** — A 44px-tall single-row band on a white ground, divided from content by a 1px hairline. The left anchor is the `logo-box` (red fill, white Futura Oblique); category links extend right in 13px regular-weight sans-serif with slight tracking; a plain numeral cart count sits at the far right. No dropdown, no mega-menu, no promotional strip — all navigation is flat and link-driven, routing to category listing pages.

**`category-nav`** — A secondary link row beneath the main bar listing seasonal categories (Tops, Jackets, Pants, Hats, Accessories, Skate, etc.). The active category shifts to primary red (#ec1324); all others remain ink black. A 1px hairline separates it from the product grid below. On mobile it becomes a horizontally scrollable strip with the same flat link style.

### Product Grid

**`product-card`** — The image fills the card area with a faint hairline border on all sides. Beneath the image: product name in 11px uppercase tracked sans-serif, price in the same scale at regular weight, both left-aligned with minimal gap. No hover overlay or quick-add affordance — the entire card is a single tap/click target to the PDP. Sold-out items display a "SOLD OUT" text label in muted gray (#767676) rather than image dimming or badge overlays.

**`product-grid`** — A strict 4-column manifest at 8px gap with 16px padding from the viewport edge. No featured large tiles, no editorial breaks between drops — every SKU occupies identical space. The uniformity is intentional: the grid reads as inventory, not aspiration.

**`new-badge`** — A small, hard-cornered red slab reading "NEW" in 10px white uppercase at 700 weight with wide tracking. Positioned above or beside the product name with 2px vertical and 4px horizontal padding. Zero border radius; no shadow or outline.

### Drop / Release

**`hero-drop-banner`** — A full-bleed red (#ec1324) block spanning viewport width, deployed for weekly drop announcements. White display-xl text states the drop date and season name. No photography, no sub-copy beyond the essential date — the negative space within the red ground is the composition.

**`drop-date-label`** — Small caption-weight text in muted gray (#767676) indicating drop day and time. Appears inline below a product name or adjacent to a collection header. No background or container.

**`announcement-strip`** — A 32px black band above the nav bar delivering short system messages (drop times, store hours, shipping notices) in 10px white uppercase with wide tracking. Full-bleed, no dismiss control.

### Product Detail

**`size-selector`** — A horizontal row of flat, square-edged buttons, one per available size. The selected size receives a 1px solid black border as its only differentiation; unselected sizes have a hairline border. Sold-out sizes render at 35% opacity, sometimes with a diagonal strikethrough, rather than being hidden or fully disabled.

**`sold-out-label`** — Plain-text in muted gray (#767676) with no container, no badge, no icon. Appears directly beside or below the size selector to communicate stock status without disrupting the visual order of the page.

**`product-detail-title`** — Product name in 14px uppercase 700-weight sans-serif at 0.05em tracking, followed immediately by the price at the same size in regular weight. No separator element between name and price; the weight contrast alone creates hierarchy.

### Structural

**`logo-box`** — The hard red rectangle enclosing "Supreme" in white Futura Heavy Oblique. Hard corners on all four sides; zero border radius; the geometric absoluteness of the box is the brand's most recognized graphic fact and must never receive radius treatment.

**`search-input`** — A compact 32px-tall flat input on the surface-soft (#f2f2f2) background, 1px hairline border, no border radius. Triggered from a nav icon; expands inline or as a full-width overlay. Placeholder text in muted gray.

**`footer`** — White ground with a 1px hairline top border. Left-aligned link clusters in 11px caption-weight muted text, covering Shipping, Returns, Stores, and legal copy. No promotional material, no email capture, no social icons in the primary footer region.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Product grid collapses to 2 columns; category nav becomes horizontal scroll or hidden behind a toggle; nav bar retains logo-box and cart count only; announcement strip persists |
| Tablet | 744–1128px | Product grid at 3 columns; category nav persists as scrollable single row; hero banner scales down vertically; nav link labels visible |
| Desktop | 1128–1440px | 4-column product grid at full density; complete single-row nav with all category links; hero banner full-bleed |
| Wide | > 1440px | Content and grid cap at ~1440px max-width, centered on the canvas; hero banner fills full viewport width behind a max-width content container |

### Touch Targets

- "Add to Cart" button spans full container width on mobile, minimum 44px tall
- Size selector buttons expand to a minimum 44×44px tap area on mobile via padding
- Nav links receive minimum 44px tap height via vertical padding extension
- Entire product card (image + label area) is one tap target routing to PDP
- Logo box tap target extends to full nav height for ergonomic accuracy

### Collapsing Strategy

- Primary nav collapses at mobile breakpoint; logo-box and cart count remain visible at all widths
- Category sub-nav converts to a horizontally scrollable flat-link strip on mobile — no pills, no rounded containers, underline active state only
- Product grid holds at 2 columns on mobile; 1-column is never used (density is part of the brand expression)
- Footer link columns stack vertically at mobile, maintaining the same caption-size muted style
- Hero drop banner reduces vertical height on mobile but remains full-bleed and full-red

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex value extracted from the live site (#f2f2f2, the meta theme-color); all other palette values including the primary red (#ec1324) are derived from widely documented Supreme brand identity, not from live extraction
- Exact primary red hex unconfirmed by extraction: Supreme's red is universally documented as a pure or near-pure red; #ec1324 is a widely cited approximation but the precise rendered value was not captured
- No font-family stacks detected from the live site; typography assignments (Futura for the logo mark, Helvetica Neue for UI text) are based on brand-knowledge and are unverified against actual computed styles
- Supreme's site is likely behind anti-bot protection and loads design tokens via JavaScript, preventing reliable CSS extraction
- No spacing, sizing, or border-width tokens were extracted; all component dimensions are estimated from visual brand references
- Dark mode behavior unknown; the brand appears to operate exclusively in light mode
- Animation timing, transition curves, and scroll behavior not captured
- The exact weight and tracking values used in production navigation and product labels could not be confirmed
