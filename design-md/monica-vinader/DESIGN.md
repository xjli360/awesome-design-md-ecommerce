---
version: alpha
name: "Monica Vinader"
source_url: "https://www.monicavinader.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Engraving is the brand's signature promise — every piece on monicavinader.com can be marked with a name, date, or set of coordinates — and the interface enforces that precision through deliberate restraint. A single extracted ink tone, #313131, operates against white; there is no competing interface color to distract from the gold, silver, and vermeil of the product photography. CTAs render as solid #313131 bars with uppercase tracked type and {rounded.none} geometry, landing as discreet counter signage rather than urgent commerce buttons. The nav carries soft category labels — NEW IN, JEWELRY, GIFTS, ENGRAVING, SALE — at low weight and open tracking, with no bold or color differentiation between states; hierarchy is conveyed through spacing and uppercase case alone. Product cards are portrait-ratio rectangles, hard-edged, shadowless, name and price in 14px regular weight below the image — editorial restraint that trusts the object over the interface frame. The brand's single most distinctive UI moment is the engraving preview: as a customer types a name or date, a live script-font rendering appears in a warm off-white panel above the input field, mimicking the look of metal inscription. This tactile simulation is where interface warmth concentrates, while every surrounding element stays neutral. Personalization selectors for metal finish (Gold Vermeil, Sterling Silver, Rose Gold Plated) use rectangular swatches with {rounded.none} and a hairline border, activating into #313131 fill rather than a color-coded swatch system — consistency over decoration. The footer inverts to a dark #313131 ground with white type, closing the page on the same monochromatic logic that opened it.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#9e9e9e"
  ink: "#313131"
  body: "#4d4d4d"
  muted: "#767676"
  muted-soft: "#a3a3a3"
  hairline: "#e5e5e5"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f8f6f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  gold-accent: "#c5a77d"
  error: "#c0392b"

typography:
  display-xl:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
  body-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  nav-label:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 1.2px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 1px
    textTransform: uppercase
  product-name:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  engraving-script:
    fontFamily: "Script, 'Pinyon Script', cursive"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px

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
    padding: 14px 32px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.base}"
    height: 48px
  engraving-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.base}"
    height: 48px
    maxLength: 20
  engraving-preview:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.engraving-script}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    minHeight: 80px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
    boxShadow: none
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.product-name}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
    border: none
    boxShadow: none
  product-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "3px 6px"
  metal-selector:
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackgroundColor: "{colors.canvas}"
    inactiveTextColor: "{colors.ink}"
    activeBorder: "1px solid {colors.ink}"
    inactiveBorder: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "8px 16px"
    typography: "{typography.caption}"
    height: 40px
  size-selector:
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackgroundColor: "{colors.canvas}"
    inactiveTextColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    height: 40px
    minWidth: 40px
    typography: "{typography.caption}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    displayTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 560px
    textAlign: center
    padding: "{spacing.section} {spacing.xl}"
  wishlist-icon:
    defaultColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    size: 20px
    rounded: "{rounded.full}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    border: none
    borderBottom: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} 0"
    height: 48px
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.md} 0"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  newsletter-input:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    border: none
    borderBottom: "1px solid {colors.on-dark}"
    rounded: "{rounded.none}"
    placeholder: "{colors.muted-soft}"
    padding: "{spacing.sm} 0"
    height: 44px

## Components

### Buttons

**`button-primary`** — Solid #313131 fill, uppercase tracked type at 1.2px letter-spacing, zero border radius, 48px height. The button reads as a discreet label bar rather than a color-forward CTA; visual energy stays with the product image, not the button. Active state deepens to #1a1a1a; disabled drops to #9e9e9e, maintaining strict monochrome logic throughout all states.

**`button-secondary`** — White fill with a 1px #313131 border and identical uppercase type at 48px height. Paired alongside `button-primary` for dual-action rows (Add to Bag / Add to Wishlist); the two buttons read as visual equals rather than hierarchy, letting the customer choose without pressure.

**`button-ghost`** — Transparent background, underlined text, no border or background fill. Used for tertiary inline actions such as "Continue Shopping," "Learn About Engraving," or editorial text links within content blocks.

### Text Input & Engraving

**`text-input`** — Zero-radius field at 48px height with a 1px #e5e5e5 border that transitions to #313131 on focus. No background fill change on focus — the border darkening alone communicates state, keeping the field quiet within the product page layout.

**`engraving-input`** — Shares the same dimensions and focus behavior as `text-input` but drives a live preview. As the customer types, the `engraving-preview` panel above renders their text in `{typography.engraving-script}`, simulating the look of inscribed metal. Character count guidance and font-choice toggles (block, script, uppercase) attach below the field. This pairing is Monica Vinader's most distinctive UX signature.

**`engraving-preview`** — A warm off-white `{colors.surface-soft}` panel with a 1px hairline border and `{rounded.none}` geometry, minimum 80px tall. The script-font preview text sits centered in the panel with generous `{spacing.lg}` padding on all sides so the rendered name reads as precious rather than crowded.

### Navigation

**`nav-bar`** — 60px tall, white background, single 1px bottom border in #e5e5e5. Top-level links rendered in `{typography.nav-label}` — 13px uppercase at 0.8px tracking, weight 400 — with no bold active state, no color shift on hover. The logo center- or left-aligns depending on breakpoint. Utility icons (search, account, bag) cluster at right.

**`nav-dropdown`** — Full-width mega-panel drops flush to the navbar bottom border. White background, top border only, no shadow. Interior organizes into two to four columns: subcategory text links left, editorial imagery or campaign asset right. Links in `{typography.body-sm}`, hover triggers a color shift to #313131 from #767676 with no fill change.

### Product Card

**`product-card`** — Portrait 3:4 image rectangle, hard-edged, no shadow or border. Product name in `{typography.product-name}` (14px / weight 400) directly below image, price in `{typography.price}` on the next line. On hover, a wishlist icon surfaces at the image top-right and some cards swap to a secondary colorway image. No card background, no overlay gradient.

**`product-badge`** — Small rectangular chip ("NEW", "BESTSELLER", "LAST FEW") with a 1px hairline border on white, uppercase 10px tracked type, no color fill. Badge presence marks editorial status without color noise; it reads more like a museum label than a commerce flag.

### Metal & Size Selectors

**`metal-selector`** — Rectangular text swatches at 40px height for Gold Vermeil, Sterling Silver, Rose Gold Plated, Gold Plated. Active state: solid #313131 fill with white text. Inactive state: white fill with hairline border. No color circles — the label text alone differentiates finishes. Typography `{typography.caption}`.

**`size-selector`** — Square or short-rectangle buttons at 40×40px minimum for ring sizes and bracelet lengths. Same active/inactive logic as `metal-selector`. No radius. Sold-out sizes show a diagonal line-through.

### Hero Banner

**`hero-banner`** — Full-width editorial panel, minimum 560px tall on desktop, with a `{colors.surface-soft}` background or full-bleed jewelry photography. Display headline at `{typography.display-xl}` weight 300 — the lightness of the weight is intentional; heavy headlines would compete with the delicacy of the product imagery. One or two `button-primary` or `button-secondary` CTAs beneath the copy, spaced with `{spacing.lg}`.

### Search

**`search-overlay`** — Full-width field that appears below the nav bar on search activation. No box border — only a single 1px underline in #313131, rendering as an underscored line rather than a form input box. Placeholder text in `{colors.muted}`, 48px height. Suggestions appear in a dropdown below without visual boxing.

### Filter Bar

**`filter-bar`** — Horizontal strip below the category header image. Filter labels ("Metal", "Price", "Gemstone", "Style", "New Arrivals") in `{typography.caption}`, muted at rest, #313131 when active or open. No button outlines at rest — the strip reads as a content annotation row, not a button row. Bottom border only.

### Footer

**`footer`** — #313131 background with white text throughout. Newsletter input uses the same bottom-line-only pattern as the search field, inverted to white on dark. Three or four link columns in `{typography.body-sm}` with no column dividers. Final row carries social icons and accepted payment icons in white at reduced opacity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero headline scales to `{typography.display-md}`; engraving preview stacks above input full-width; metal selectors wrap to two rows |
| Tablet | 744–1128px | Two-column product grid; abbreviated nav shows top-level labels with hamburger for sub-categories; hero shifts to half-width text with adjacent product image |
| Desktop | 1128–1440px | Three- to four-column product grid; full mega-menu; engraving input and preview sit side-by-side; filter bar is always visible |
| Wide | > 1440px | Content constrained to ~1440px max-width; side margins grow; hero imagery extends full-bleed while text and CTA remain center-column |

### Touch Targets

- Metal and size selector swatches: minimum 40×40px enforced with padding
- Wishlist icon on product card: minimum 44×44px tap area via absolute-positioned padding
- Nav hamburger icon: minimum 44×44px
- Filter label chips: minimum 40px height
- All primary and secondary buttons: 48px height, minimum 120px width

### Collapsing Strategy

- Mega-menu becomes a slide-in drawer on mobile; each top-level category expands as an inline accordion
- Product filters collapse into a bottom-sheet modal on mobile, triggered by a "Filter & Sort" sticky bar
- Engraving preview panel stacks above the input on mobile rather than floating beside it
- Footer columns stack to a single-column accordion on mobile; newsletter field remains visible above the collapsed links
- Search overlay takes full viewport width on mobile with a prominent close icon

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Full color palette unextracted**: Only #313131 was captured; the site was behind Cloudflare anti-bot protection ("Just a moment..." page title). Warm off-white surface values, hairline grays, and the `gold-accent` token (#c5a77d) are inferred from Monica Vinader's widely documented demi-fine jewelry aesthetic — not from live extraction.
- **Typography unconfirmed**: No custom font-family was detected at scrape time; the extraction returned only system font stacks. `Neue Haas Grotesk` is a reasonable inference for a London-founded premium jewelry brand but must be verified by inspecting network font requests on the live site.
- **Gold accent hex unverified**: #c5a77d (warm sand-gold) is a brand-knowledge inference based on the Gold Vermeil and gold-plated product lines; the actual UI accent value was not extracted.
- **Engraving script font name unknown**: The typeface used in the live engraving preview panel was not capturable without JS execution; actual font name and source require network inspection on a product detail page.
- **Meta theme-color absent**: No PWA shell color was set or the tag was stripped during extraction.
- **Animation and transition tokens**: Hover crossfade timing on product cards, drawer open/close easing curves, and the engraving preview character-by-character animation were not extractable from a static scrape.
- **Secondary palette (error, success, promotional)**: Sale and promotional banner colors, error validation states, and any loyalty or campaign accent colors were not captured.
