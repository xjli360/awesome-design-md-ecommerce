---
version: alpha
name: "Susan Caplan"
source_url: "https://www.susancaplan.co.uk"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Archive-catalog gray — a tonal stack running from #f5f5f5 through #dfdfdf to #bbbbbb — wraps every Susan Caplan product page like acid-free tissue, a deliberate restraint that cedes all visual authority to signed vintage pieces by Chanel, Dior, and Miriam Haskell. Against this studied pallor, lacquer-bright #ff2626 lands with the force of a price sticker in a Portobello Road stall: it activates every primary CTA, every SALE flag, every Add to Bag moment. Warm #f49a13 amber plays second voltage for discount markers and promotional banners, giving sale events a jeweller's warmth rather than a supermarket blare. Gill Sans — the quintessentially British humanist face that has lettered Underground signs and Penguin paperback spines for nearly a century — carries display headings and collection titles; Cabin handles subheadings and button labels; Lato provides the utilitarian workhorse at body scale. The system runs hard corners throughout — {rounded.none} on primary buttons, product cards, and input fields — a formal archival posture that deliberately distances the site from the rounded-edge warmth of fast-fashion contemporaries. Navigation is disciplined: a single-row bar in {colors.canvas} with uppercase-tracked category links and no mega-menu theatrics, trusting that collectors know what they are looking for. Photography sits on near-white ({colors.surface-soft}) fields without lifestyle staging; each brooch, clip earring, and parure is treated as a collectible object to be examined rather than an accessory to be coveted. An announcement bar in {colors.ink} anchors every page with shipping thresholds, its white-on-near-black the only high-contrast moment the layout permits outside of CTA buttons. The dark footer mirrors that inversion — ink ground, muted link labels — completing a site that reads as auction-house catalogue rather than high-street scroll.

colors:
  primary: "#ff2626"
  primary-active: "#c62828"
  primary-disabled: "#f9b5b5"
  accent-amber: "#f49a13"
  ink: "#141416"
  body: "#121212"
  muted: "#bbbbbb"
  hairline: "#dedede"
  hairline-soft: "#dfdfdf"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link-blue: "#286ef8"

typography:
  display-xl:
    fontFamily: "'Gill Sans', 'Gill Sans MT', Calibri, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.06em
  display-md:
    fontFamily: "'Gill Sans', 'Gill Sans MT', Calibri, sans-serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.03em
  display-sm:
    fontFamily: "'Gill Sans', 'Gill Sans MT', Calibri, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-md:
    fontFamily: "Cabin, 'Gill Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.01em
  title-sm:
    fontFamily: "Cabin, 'Gill Sans', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  body-md:
    fontFamily: "Lato, Cabin, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Lato, Cabin, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Lato, Cabin, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  button-md:
    fontFamily: "Cabin, 'Gill Sans', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "Cabin, 'Gill Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "Cabin, 'Gill Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.1em
    textTransform: uppercase
  price-display:
    fontFamily: "Cabin, 'Gill Sans', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "Cabin, 'Gill Sans', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  announcement:
    fontFamily: "Lato, Cabin, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.05em

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
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    logoHeight: 40px
    position: sticky
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.announcement}"
    height: 38px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageBg: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    designerTypography: "{typography.caption}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
    imageHoverScale: 1.03
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    position: "top-left"
  new-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    position: "top-left"
  price-tag:
    regularPriceTypography: "{typography.price-display}"
    regularPriceColor: "{colors.ink}"
    salePriceTypography: "{typography.price-sale}"
    salePriceColor: "{colors.primary}"
    originalPriceColor: "{colors.muted}"
    strikethrough: true
  collection-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.muted}"
  category-filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: "8px 16px"
    height: 36px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-md}"
    minHeight: 480px
  search-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.ink}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 44px
    submitButtonBg: "{colors.ink}"
    submitButtonColor: "{colors.canvas}"
  wishlist-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    activeTextColor: "{colors.primary}"
    iconSize: 20px
    rounded: "{rounded.none}"
  qty-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    buttonSize: 40px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    copyrightTypography: "{typography.caption}"
    borderTop: none
    columns: 4

## Components

### Buttons

**`button-primary`** — A hard-cornered ({rounded.none}) red block in #ff2626 at 48px tall with 32px horizontal padding and 13px uppercase Cabin at 0.12em tracking. The squared geometry signals archival authority rather than friendly invitation. Active state drops to #c62828 with no transition animation; disabled washes to #f9b5b5 — the only soft moment in the button system. Used on Add to Bag, Checkout, and every primary collection CTA.

**`button-secondary`** — Canvas fill with a 1px solid #141416 border, matching primary dimensions exactly. On hover the fill inverts hard to ink with canvas text — a swap, not a fade. Appears on wishlist flows, View More in editorial contexts, and secondary filter submission.

**`button-ghost`** — Transparent, no border, ink text, same uppercase Cabin tracking as the rest of the button family. Renders as an inline link-button for Read More copy, filter resets, and account navigation where a bordered button would overweight the surrounding text.

### Text Input and Search

**`text-input`** — Zero-radius field at 48px tall with a single 1px hairline border (#dedede) that sharpens to #141416 on focus. No box-shadow, no fill change on interaction — the field remains canvas-white throughout. Placeholder renders in #bbbbbb. Aligns optically with primary buttons when placed in horizontal form rows on checkout.

**`search-bar`** — Full-width zero-radius input with an attached ink-coloured submit icon block flush against the right edge, forming a single unbroken rectangle — archival card-index aesthetics applied to site search. On focus, the outer border advances to #141416 matching the text-input convention.

### Navigation

**`nav-bar`** — Single 64px horizontal bar in canvas white, 1px hairline bottom border. Logo left-aligned at 40px height; primary category links in uppercase Cabin 12px with 0.1em tracking positioned centre or right. Utility icons (search, account, bag) right-aligned at 44px touch targets. Bar is sticky on scroll with no hide/reveal animation.

**`announcement-bar`** — 38px ink (#141416) strip fixed at the very top of the page in white Lato 13px, 0.05em tracking, centred. Carries shipping thresholds, new arrivals alerts, or editorial messaging. Single line on desktop without marquee scroll.

### Product Card

**`product-card`** — Clean vertical stack with zero rounding on every edge. Product image fills the full card width against a #f5f5f5 field; below it, the designer label renders in caption-scale Lato (12px), the piece name in small uppercase Cabin ({typography.title-sm}), and the price in 18px Cabin bold. Sale prices appear in #ff2626 with the original price struck through in muted gray. Hover produces a contained image scale of 1.03 — no border change, no shadow lift — so the grid reads as a flat index surface.

**`sale-badge`** / **`new-badge`** — Flat rectangular chips flush against the top-left corner of the product image. SALE on #ff2626; NEW ARRIVAL or JUST IN on #141416. Both render at 11px uppercase Cabin with 0.1em tracking, 4px top / 8px side padding — legible but subordinate to the jewellery image behind them.

### Price

**`price-tag`** — Regular price at 18px Cabin bold in #141416. Sale state: sale price in #ff2626 bold, original price struck through in #bbbbbb, rendered side by side with {spacing.xs} between. The red sale colour is the same token as primary CTAs, reinforcing the urgency pairing throughout the commerce flow.

### Collection and Filters

**`collection-heading`** — 26px Gill Sans at weight 400, 0.03em tracking, ink colour. A 1px hairline underline separates heading from the product grid below. Title case rather than uppercase — at display scale Gill Sans carries sufficient weight without the capitalisation formality used on nav links.

**`category-filter-pill`** — Square-cornered chips at 36px height using 12px uppercase Cabin, hairline border on surface-soft fill. Active state: hard ink fill, canvas text, no radius change. Multiple selections stack horizontally on desktop in a wrapping row; on mobile this row becomes independently scrollable.

**`breadcrumb`** — Caption-scale Lato in #bbbbbb with a "/" separator in the same muted colour. Active (current page) label steps to #141416. No truncation on desktop; on mobile the deepest two levels are retained and ancestors collapsed.

### Hero

**`hero-banner`** — Full-width editorial block at minimum 480px tall on desktop. Background is typically #f5f5f5 or a full-bleed product still; no dark overlay is applied — photography is selected for intrinsic contrast. Headline in Gill Sans display-xl (40px, weight 300, 0.06em tracking) positions above a body-md subtitle in Lato. A single primary button or ghost link completes the CTA zone. Text block is left-aligned rather than centred, evoking a printed catalogue spread.

### Footer

**`footer`** — Four-column dark reversal: #141416 ground, #f5f5f5 body text, #bbbbbb link labels that advance to canvas white on hover. Column headings in 12px uppercase Cabin ({typography.title-sm}). Copyright and legal links at caption scale. The darkness provides visual punctuation at the end of the scroll, echoing the announcement bar above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + bag icon; announcement bar wraps to two lines if needed; category filters convert to horizontal scrollable chip row; hero min-height reduces to 280px |
| Tablet | 744–1128px | Two-column product grid; nav retains top bar with abbreviated category labels; hero at 380px min-height; filter pills remain horizontal row |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with all category labels visible; hero at 480px min-height; filter sidebar or top row visible |
| Wide | > 1440px | Grid max-width constrained to ~1400px, centred with equal gutters; hero image scales with viewport while text block holds a fixed left inset |

### Touch Targets

- Primary and secondary buttons minimum 48px height throughout
- Nav icon buttons (search, bag, account) minimum 44×44px tap target
- Category filter pills minimum 40px height on mobile
- Wishlist icon buttons minimum 44×44px regardless of displayed icon size
- Full product card area is tappable on mobile — no separate tap target needed

### Collapsing Strategy

- Desktop category nav → mobile hamburger drawer with accordion category groups
- Utility icons (search, wishlist) remain exposed on mobile; account collapses into hamburger drawer
- Announcement bar: single static line on desktop, wraps gracefully on mobile at reduced font size (11px)
- Footer: four columns on desktop → two on tablet → single stacked accordion on mobile
- Filter row: sidebar or inline row on desktop → horizontally scrollable chip strip on mobile, with a floating "Filter" button to open a drawer

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `primary-disabled: "#f9b5b5"` is derived by lightening the extracted primary, not directly extracted from the live site
- Canvas white (#ffffff) is inferred as the base background; the extractor did not surface it — it may be a browser or Shopify CSS default
- `link-blue: "#286ef8"` is likely a Shopify framework utility default rather than a Susan Caplan brand colour; treat as utility-only and do not elevate it to primary actions
- Exact nav bar height, logo aspect ratio, and sticky-scroll behaviour were not confirmable from the extracted hints
- Whether Gill Sans is served as a web font or relies on system fallback (Calibri on Windows, macOS Gill Sans) is unknown; the stack reflects the extracted font-family list
- Specific hover animation timing (image scale transition duration) is inferred from Shopify convention, not extracted
- `accent-amber: "#f49a13"` usage contexts (price badges, promo banners, or seasonal overlays) could not be precisely mapped without deeper page inspection
- No dark-mode variant was detected in the extraction
- Icon system style (stroke weight, filled vs outline) and SVG asset details were not extractable from the hints provided
