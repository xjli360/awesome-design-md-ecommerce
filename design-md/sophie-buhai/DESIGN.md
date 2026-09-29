---
version: alpha
name: "Sophie Buhai"
source_url: "https://www.sophiebuhai.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Two weights of Univers LT Pro — 55Roman for body and navigation, 65Bold for display and labels — are the entire typographic system on a site that refuses decorative variation. The palette compresses to four neutrals: #121212 at deepest ink, #222222 as both primary action color and body text, #dedede for hairlines and disabled states, #eeeeee lifting surfaces the barest step above white canvas. The compression is structural rather than accidental — gold vermeil and oxidized sterling read as chromatic events precisely because the digital ground surrenders all color to the object. The brand name appears centered in the nav, rendered in the same Univers 65Bold used for category headings, distinguished by letter-spacing and weight rather than a custom logotype; Sophie Buhai treats the typeface as house identity, which means the typographic logic runs unbroken from logo to footnote. Primary CTAs are hard-cornered filled rectangles at {rounded.none} — no border-radius anywhere on the page — so the button reads as an architectural slab rather than a soft web affordance. Letter-spacing operates aggressively in the uppercase register: navigation and button labels track at 0.10–0.15em, approximating the compressed density of a printed jewelry catalog. Product cards are square-crop photography on white ground, price and name set in a tight two-line column below, with no hover animation beyond a mild opacity fade lasting 0.3s; the quietness forces attention onto the form of the piece rather than the interface framing it. Editorial sections alternate full-bleed campaign imagery — one model, one jewel, maximum negative space — with structured product grids, creating rhythm through scale contrast rather than color contrast. Every component reaches for a single distinguishing variable: weight, or spacing, or tracking, never all three simultaneously. The formal economy mirrors the jewelry itself: everything resolved to the minimum necessary structure.

colors:
  primary: "#222222"
  primary-active: "#121212"
  primary-disabled: "#dedede"
  ink: "#121212"
  body: "#222222"
  muted: "#888888"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  overlay-scrim: "rgba(18,18,18,0.48)"

typography:
  display-xl:
    fontFamily: "'UniversLTPro-65Bold', 'Univers LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'UniversLTPro-65Bold', 'Univers LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'UniversLTPro-65Bold', 'Univers LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.12em
    textTransform: uppercase
  body-md:
    fontFamily: "'UniversLTPro-55Roman', 'Univers LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'UniversLTPro-55Roman', 'Univers LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'UniversLTPro-55Roman', 'Univers LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.05em
  button-md:
    fontFamily: "'UniversLTPro-55Roman', 'Univers LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-label:
    fontFamily: "'UniversLTPro-55Roman', 'Univers LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.10em
    textTransform: uppercase
  logo-display:
    fontFamily: "'UniversLTPro-65Bold', 'Univers LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.15em
    textTransform: uppercase
  price-md:
    fontFamily: "'UniversLTPro-55Roman', 'Univers LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  announcement-text:
    fontFamily: "'UniversLTPro-55Roman', 'Univers LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.08em

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
    padding: 14px 32px
    height: 44px
    border: none
    transition: background-color 0.2s ease
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 44px
    border: "1px solid {colors.ink}"
    transition: background-color 0.2s ease
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    borderTop: none
    borderLeft: none
    borderRight: none
    borderBottom: "1px solid {colors.hairline}"
    padding: 10px 0px
    height: 40px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    borderBottomColor: "{colors.ink}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    logoTypography: "{typography.logo-display}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.xl}"
    logoAlignment: center
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.announcement-text}"
    height: 36px
    textAlign: center
    padding: "0 {spacing.base}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: 1/1
    rounded: "{rounded.none}"
    imageGap: "{spacing.sm}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price-md}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.body}"
    padding: 0
  product-card-hover:
    imageOpacity: 0.88
    transition: opacity 0.3s ease
  product-grid:
    backgroundColor: "{colors.canvas}"
    columns: 3
    gap: "{spacing.xl}"
    padding: "0 {spacing.xl}"
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    imageLayout: full-bleed
    overlayScrim: "{colors.overlay-scrim}"
    headingTypography: "{typography.display-xl}"
    headingColor: "{colors.canvas}"
    textAlignment: center
    minHeight: 80vh
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    descriptionColor: "{colors.muted}"
    padding: "{spacing.xxl} {spacing.xl} {spacing.lg}"
    textAlign: center
  product-image-gallery:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: 1/1
    rounded: "{rounded.none}"
    thumbnailSize: 64px
    thumbnailGap: "{spacing.xs}"
    thumbnailBorderActive: "2px solid {colors.ink}"
    thumbnailBorderInactive: "1px solid {colors.hairline}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    height: 40px
    minWidth: 40px
    selectedBorderColor: "{colors.ink}"
    selectedBorderWidth: 2px
  material-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "3px {spacing.sm}"
    display: inline-block
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    gap: "{spacing.xs}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.title-md}"
    itemTitleTypography: "{typography.body-md}"
    itemPriceTypography: "{typography.price-md}"
    borderLeft: "1px solid {colors.hairline}"
    width: 380px
    padding: "{spacing.xl}"
  newsletter-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    inputBorderBottom: "1px solid {colors.hairline}"
    inputTypography: "{typography.body-md}"
    inputHeight: 40px
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonTypography: "{typography.button-md}"
    buttonHeight: 40px
    padding: "{spacing.xxl} {spacing.xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-md}"
    linkColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
    columnGap: "{spacing.xxl}"

## Components

### Buttons
**`button-primary`** — Flat near-black rectangle at {rounded.none} and 44px height, carrying uppercase Univers 55Roman at 11px tracked to 0.12em. Hover deepens from #222222 to #121212 over 0.2s; the shift is intentionally subtle because the geometry has already communicated authority. Disabled state fills with #dedede and white text, retreating from the eye rather than drawing attention with a separate visual treatment.

**`button-secondary`** — Same hard-cornered geometry as `button-primary`, white fill with 1px #121212 border and matching typography. Hover fills the background with #eeeeee, reading as engagement without weight. Used for secondary actions — editorial "Shop Now" links, wishlist CTAs, and navigational prompts adjacent to the primary add-to-cart flow.

### Navigation
**`nav-bar`** — Minimal horizontal bar at 56px with the brand name centered in 13px Univers 65Bold tracked to 0.15em. Navigation links flank the logo at left and right in 11px uppercase Univers 55Roman, creating a typographic bracket rather than a left-anchored list. A 1px #dedede hairline closes the bar against the page below. No hover flyout animations or mega-menus — subcategory links surface in a lean dropdown that inherits the nav's own typographic register.

**`announcement-bar`** — Full-width #121212 field at 36px sitting above the nav, the only surface on the site where color inverts: Univers 55Roman in white against deep black. Carries single-line messages (free shipping thresholds, new arrivals) without introducing a third hue into the palette.

### Product Presentation
**`product-card`** — Square-aspect image at zero padding, followed immediately by a two-line text block: product name in 14px Univers 55Roman and price in 13px with slight 0.02em tracking. No badge, no overlay, no hover card — only an opacity fade to 0.88 at 0.3s. The restraint ensures the jewelry photograph is never upstaged by interface chrome.

**`product-grid`** — Three-column grid at 32px gap with horizontal padding matching the nav's own edge rhythm. Columns step to two on tablet and one on mobile. The generous gap between pieces creates breathing room without the page reading as sparse.

**`hero-editorial`** — Full-bleed campaign image filling at least 80vh, with centered heading in 40px Univers 65Bold overlaid on a translucent dark scrim. Follows gallery-poster logic: one image, one statement, one CTA. The scrim uses {colors.overlay-scrim} rather than a solid mask to preserve the photograph's texture beneath the type.

**`collection-header`** — Centered title in 24px Univers 65Bold above a one- to two-sentence description in 14px Univers 55Roman at #888888. Provides editorial framing for collection index pages without competing visually with the product grid immediately below.

**`product-image-gallery`** — Square primary image with a horizontal strip of 64px thumbnails below, each separated by {spacing.xs}. The selected thumbnail promotes its border from 1px #dedede to 2px #121212 — weight shift as selection signal, consistent with the size-selector convention.

### Forms and Inputs
**`text-input`** — Bottom-border-only field: no surrounding box, just a 1px #dedede underline that focuses to #121212. The convention strips all rectangular scaffolding from the form surface, leaving search and email fields as typographic lines rather than containers. Placeholder text renders in #888888.

**`newsletter-section`** — #eeeeee-surface band with uppercase Univers 65Bold heading at 13px, short supporting body in 12px Univers 55Roman, and an inline input-plus-button row. The button height matches the input height exactly at 40px, creating a flush horizontal register. Padding at {spacing.xxl} top and bottom gives the section editorial weight without a background color shift.

### Supporting Components
**`size-selector`** — Square 40×40px tappable cells with no border-radius and 1px #dedede border at rest. Selected state promotes the border to 2px #121212, using weight rather than fill color as the confirmation signal. Serves ring size and bracelet length selectors consistently.

**`material-tag`** — Inline {rounded.none} chip on #eeeeee fill in 11px Univers 55Roman at #888888. Appears on product detail pages as metadata: "14k gold vermeil", "sterling silver oxidized". Muted text keeps it subordinate to the product title and price rather than reading as a marketing badge.

**`cart-drawer`** — 380px panel sliding from the right, white background with a single 1px #dedede left border. Header in uppercase Univers 65Bold at 13px, line items in 14px Univers 55Roman with price in 13px price-md. Padding at {spacing.xl} on all sides. No box-shadow — the hairline border alone separates the drawer from page content.

**`footer`** — Canvas background with 1px #dedede top border and four-column link grid. Column headers in 13px uppercase Univers 65Bold, links in 12px Univers 55Roman. No background tint or enclosing box; the footer reads as a natural extension of the page grid rather than a visual foot-block. Column gap at {spacing.xxl} mirrors the editorial breathing room above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger icon with full-height slide-in drawer; hero heading scales to display-md (24px); horizontal padding compresses to {spacing.base} |
| Tablet | 744–1128px | Two-column product grid; full nav labels remain visible; collection-header padding reduces to {spacing.lg} vertical |
| Desktop | 1128–1440px | Three-column product grid; max-content width 1280px centered; nav-bar holds at 56px height; cart-drawer at 380px |
| Wide | > 1440px | Grid locks at 1280px max-width with auto side margins; hero and editorial imagery scale to full viewport width behind the centered content column |

### Touch Targets
- All buttons are minimum 44px height to meet iOS and Android tap-target minimums
- Size-selector cells expand their tap area to 44×44px on mobile without changing visual size
- Nav icons in collapsed mobile state render at 44×44px touch region regardless of visual glyph size
- Product card tap region covers full card width including the text block below the image thumbnail

### Collapsing Strategy
- Navigation collapses to a hamburger icon at mobile; drawer slides in full-height with nav-label typography stacked vertically and the logo displayed at the top
- Product grid steps 3 → 2 → 1 at Desktop → Tablet → Mobile breakpoints
- Hero heading scales from display-xl (40px) to display-md (24px) on mobile; full-bleed image persists across all breakpoints
- Collection header centered-text stack persists; padding compresses from {spacing.xxl} to {spacing.lg} at mobile
- Footer four-column layout collapses to two columns on tablet and a stacked accordion on mobile, retaining the weight-differentiated heading/link hierarchy within each accordion item

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only four hex values were extracted (#222222, #dedede, #eeeeee, #121212); white canvas (#ffffff) is inferred as standard Shopify default but was not confirmed as a literal extracted value
- Muted gray (#888888) and overlay-scrim are approximated from the extracted neutral ladder; actual computed values were not available
- No warm metallic or gold accent color was confirmed — it is plausible the site uses a subtle gold (#c9a96e or similar) for hover links or material callouts that did not surface in extraction
- Exact font sizes, line-heights, and letter-spacing values on the live site could not be verified via static extraction; values above are inferred from Univers LT Pro conventional usage at this brand archetype
- Hover transition durations and easing curves are approximated; actual site values were not extractable
- Cart, wishlist, and account icon styles (filled vs. outline, stroke weight, size) could not be confirmed
- Mobile nav drawer background and transition direction (slide-in vs. fade) could not be verified
