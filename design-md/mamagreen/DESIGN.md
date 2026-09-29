---
version: alpha
name: "Mamagreen"
source_url: "https://www.mamagreen.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Mamagreen arrives at luxury through restraint — a near-black charcoal grid (#222222, #444444) anchors the neutral field, and the site's only true color voltage, a deep ocean teal at #1d4354, surfaces where authority is required: primary CTAs, nav anchors, and product-color selectors. A warm terracotta (#cc6055) provides the counter-note, appearing in accent badges and hover treatments rather than competing for dominance, evoking the sun-baked stone patios the furniture is built to occupy. The overall effect reads as a system designed for photography to win: quiet type on near-white canvas (#fcfbfe) gives product imagery — teak grain, powder-coated aluminum, woven rope — full atmospheric control. Montserrat carries all typographic weight, from wide-tracked display headings at 48px down to tightly set all-caps captions. At display scale, letter-spacing opens to 3px, echoing the deliberate negative space in the furniture's frame geometry; button labels are uppercase with 2px tracking, treating each word as a precision mark. Body type stays conservative at 16px / 1.6 line-height, legible against the pale canvas. There are no serif detours, no decorative contrast pairings — just one geometric sans held at different weights, mirroring the brand's philosophy of a single material executed flawlessly rather than a catalogue of options. Corner radii sit almost entirely at {rounded.none}. Product cards, nav bars, and interactive buttons all use sharp corners; only material swatches break to {rounded.full} to mirror the circular profile of fabric samples and finish dots. This is a brand that sells objects with precise machined silhouettes — any softness in the UI would betray the aesthetic. Spacing is generous throughout: section breaks open at 64px, cards carry substantial internal padding, and the grid never crowds. On category landings, products present two-up at desktop, allowing each piece room to breathe as it would on an actual terrace. A pale lavender-gray (#e9e6ed, #cfc8d8) appears in filter panels and secondary surface areas — a warmer alternative to flat white that subtly references the diffuse light of overcast northern European mornings, the origin context for much of the collection's design language. WooCommerce plugin colors contaminate the extracted palette but represent no brand tokens.

colors:
  primary: "#1d4354"
  primary-active: "#163240"
  primary-disabled: "#7a9caa"
  accent: "#cc6055"
  accent-hover: "#b84f45"
  ink: "#222222"
  body: "#444444"
  muted: "#777777"
  muted-soft: "#aaaaaa"
  hairline: "#d3d3d3"
  hairline-soft: "#eeeeee"
  canvas: "#fcfbfe"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-warm: "#e9e6ed"
  surface-warm-deep: "#cfc8d8"
  stone: "#c1bdb3"
  on-primary: "#ffffff"
  on-accent: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: 3px
  display-md:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 1.5px
  display-sm:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 1px
  title-md:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
  caption-upper:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 2px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.5px
  price:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  label-upper:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 2px
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
    padding: 14px 32px
    height: 48px
    border: none
  button-primary-hover:
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
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 13px 24px
    height: 48px
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-accent-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoHeight: 36px
    padding: "0 {spacing.xl}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    columnGap: "{spacing.xl}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    padding: "10px {spacing.base}"
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/3"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    border: "1px solid {colors.hairline-soft}"
    hoverBorder: "1px solid {colors.stone}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    overlayColor: "{colors.ink}"
    overlayOpacity: 0.32
  hero-light:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  collection-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  category-filter-tab:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.none}"
    padding: "{spacing.base} {spacing.xl}"
    borderBottom: "2px solid transparent"
  category-filter-tab-active:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.primary}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.none}"
    padding: "{spacing.base} {spacing.xl}"
    borderBottom: "2px solid {colors.primary}"
  product-detail-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    priceTypography: "{typography.price}"
    bodyTypography: "{typography.body-md}"
    labelTypography: "{typography.label-upper}"
    labelColor: "{colors.muted}"
    padding: "{spacing.xl}"
    rounded: "{rounded.none}"
  material-swatch:
    size: 32px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderSelected: "2px solid {colors.primary}"
    gap: "{spacing.sm}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    gap: "{spacing.sm}"
  section-heading:
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    textAlign: center
    paddingBottom: "{spacing.xl}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.xxl} 0"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-warm}"
    linkColor: "{colors.stone}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.caption-upper}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: "none"

## Components

### Buttons

**`button-primary`** — Sharp-cornered ({rounded.none}), ocean-teal (#1d4354) fill with all-caps Montserrat at 13px / 2px letter-spacing, conveying precision rather than friendliness. On hover it deepens to `primary-active` (#163240); disabled state fades to the desaturated `primary-disabled` (#7a9caa). Minimum height 48px with generous side padding (32px) keeps the label readable without crowding.

**`button-secondary`** — Same sharp geometry as primary, but reversed: white/canvas fill with a 1px teal border and teal label. Hover tightens the border to `primary-active` and shifts background to `surface-soft`. Used for secondary CTAs like "Request a Quote" or "Download Catalogue" adjacent to a dark hero CTA.

**`button-ghost`** — Transparent fill, hairline border (#d3d3d3), ink text. Appears for low-emphasis actions such as pagination, filter resets, and ancillary nav links where the teal would overpower surrounding content.

**`button-accent`** — Terracotta fill (#cc6055) with white text; hover deepens to `accent-hover` (#b84f45). Reserved for promotional moments — seasonal sale banners, limited-edition collection launches — so the color retains its visual charge. Never used as a standard product CTA.

### Navigation

**`nav-bar`** — 72px tall, canvas background with a single hairline-soft bottom rule. Montserrat 13px / 500 weight for all nav links, with the brand logo centered or left-aligned at 36px height. No background on scroll — stays transparent to photography. Top of the stack is the `promo-banner`, a 40px teal strip with all-caps caption announcing delivery lead times or current promotions.

**`nav-dropdown`** — Opens on hover beneath the relevant nav item; canvas background, hairline border on three sides (no top border), generous 24px internal padding arranged in labeled columns. Link text uses `body-sm` Montserrat at 400 weight. No flyout animations — the brand's precision aesthetic favors immediate, mechanical reveal over playful transitions.

### Product Cards

**`product-card`** — Square-cornered card with a 4:3 image crop showing the full piece in situ or on a neutral stone surface. Title in `title-sm` (16px / 600), price below in `price-sm` (16px / 600), material shorthand in `caption` with `muted` text color. On hover, the hairline-soft border steps to `stone` (#c1bdb3) and the image may reveal a second lifestyle shot. No add-to-cart button on the card — Mamagreen's luxury positioning routes through the product detail page.

**`product-detail-panel`** — Right-side panel on desktop PDP, full-width stack on mobile. Headline in `display-sm` (24px), price in `price` (22px / 700), section labels (Materials, Dimensions, Lead Time) in `label-upper` (10px / 700 / uppercase / 2px tracking) with `muted` color. Material swatches are 32px circles (`rounded.full`) with a 2px teal ring on selection. No accordion — all specification content is visible, reflecting that buyers are making large, deliberate purchases.

### Hero

**`hero-banner`** — Full-bleed, minimum 560px tall, primary teal (#1d4354) as background or a dark photographic overlay at 32% opacity. Headline in `display-xl` (48px / 700 / 3px tracking), subhead in `body-md`. CTA is `button-primary` reversed to white when placed over the teal field. Used for category header moments — "Dining Sets", "Lounge", "Accessories".

**`hero-light`** — A lower-contrast alternative on `surface-warm` (#e9e6ed) background for mid-page editorial breaks. Headline in `display-md`, subhead in `body-md` with `body` color. Typically pairs with a flanking product image rather than a full bleed, giving the section a split editorial quality.

### Badges and Labels

**`collection-badge`** — Terracotta fill, white all-caps caption at 11px / 1.5px tracking, zero radius. Applied to product card image corners for seasonal collections or finish exclusives. Kept to one badge per card maximum.

**`new-badge`** — Same geometry as `collection-badge` but teal fill. Marks newly released pieces within an existing collection. The color distinction between teal (new) and terracotta (collection-limited) creates a legible badge vocabulary without extra shape variation.

### Filters and Navigation Rails

**`category-filter-tab`** — Horizontal tab row on `surface-warm` background, all-caps `caption-upper` in muted gray. Active state shifts text to teal with a 2px teal bottom border — a minimal underline indicator that reads as deliberate selection, not hover state. Sits below the hero on collection pages and above the product grid.

### Utility

**`breadcrumb`** — Caption-weight Montserrat (12px / 500) in muted gray, slash-separated, rightmost item in ink. Low visual weight — purely navigational, never competes with product content above or below.

**`material-swatch`** — 32px circular swatches (the one place `rounded.full` appears on interactive elements), grouped with 8px gap. Unselected state has a transparent 2px border; selected gains a 2px teal ring. Swatch colors are literal material finishes — teak, charcoal, sand, slate — not brand palette.

**`section-heading`** — Centered `display-md` headline with an optional `body-md` subhead below in `body` color. Used to open each collection block on the homepage and category pages. Consistent 32px padding below separates it from the product grid.

**`footer`** — Dark ink (#222222) background carrying the brand into negative space. Column headings in `caption-upper` (stone-tinted), links in `body-sm` at `stone` (#c1bdb3) color, hover shifting to canvas white. Four columns at desktop: Collections, Company, Support, and a newsletter signup using `text-input` on a dark field (border shifts to `hairline` against the dark ground). No gradient, no decorative rules — the footer earns its weight through generous top/bottom padding at 64px.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero drops to 420px min-height; display-xl scales to 32px; nav collapses to hamburger drawer; promo-banner text truncates to one line; footer columns stack vertically |
| Tablet | 744–1128px | Two-column product grid; hero retains full bleed at 480px; nav shows primary links, secondary items in overflow drawer; category-filter-tabs scroll horizontally |
| Desktop | 1128–1440px | Two-up product grid (generous gutters) or three-up for accessories; nav fully expanded with dropdown panels; hero at full 560px; product-detail-panel floats right at ~480px wide |
| Wide | > 1440px | Grid centers at max-width 1440px with equal side margins; hero image extends edge-to-edge behind a centered content column; section-heading remains max-width 800px for line-length control |

### Touch Targets

- All interactive buttons and filter tabs minimum 48px tall
- Material swatches 32px diameter — increase touch hit-area with 8px invisible padding ring on mobile
- Nav links in mobile drawer minimum 48px height per item
- Breadcrumb links padded to 44px height on mobile despite small visual footprint

### Collapsing Strategy

- Primary nav collapses to hamburger at tablet breakpoint; drawer slides from left, overlaying content with a muted scrim
- Category filter tabs convert from a horizontal strip to a scrollable horizontal rail at mobile; active tab scrolls into view on load
- Product detail panel stacks below product images on mobile and tablet; sticky "Add to Quote" CTA bar anchors at viewport bottom on mobile
- Footer four-column grid collapses to two columns at tablet, single column at mobile with accordion-style section expansion for link lists
- Hero subhead text hidden at mobile below 375px viewport width to preserve headline legibility

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color tag extracted; cannot confirm if teal (#1d4354) or a lighter variant is the intended browser chrome accent
- Montserrat confirmed present in font stacks but specific weight files loaded (400, 600, 700 vs. full variable font) are unconfirmed — fallback to Helvetica/Arial may shift kerning at display sizes
- Many extracted hex values (#720eec, #7f54b3, #1e85be, #8fae1b, #7ad03a, #b81c23, #de8604, #aa0000, #ffba00) are standard WooCommerce plugin UI colors and are excluded from brand tokens; this contamination reduces confidence in the full palette extraction
- Exact hover/transition behavior on product cards (second image reveal, zoom, video autoplay) not observed
- Mobile navigation pattern (drawer vs. overlay vs. full-screen) unconfirmed; drawer assumed from common WooCommerce patterns
- Filter sidebar vs. horizontal rail layout on collection pages unverified at tablet
- Icon style (stroke weight, filled vs. outline) for nav and UI icons not extractable — FontAwesome is present but specific subset and style unknown
- Product card grid column count at desktop (2-up vs. 3-up for dining sets vs. accessories) not confirmed
- Custom checkout or quote-request flow styling not observed; Mamagreen likely uses a trade/project inquiry model rather than standard cart-checkout
