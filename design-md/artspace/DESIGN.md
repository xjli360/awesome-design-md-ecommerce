---
version: alpha
name: "Artspace"
source_url: "https://www.artspace.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Golden amber (#ffc800) as a primary CTA color is an unusual choice for an art marketplace — it reads more like a traffic placard than a gallery wall — yet against near-black (#231f20) and clinical white it functions as a decisive lot-number stamp that snaps every "Buy Now" or "Make Offer" out of the editorial field. Artspace pairs this high-contrast voltage with Akzidenz-Grotesk Next in three widths of compression: the condensed variant packs artist names and edition metadata into tight uppercase stacks; the extended variant stretches campaign headlines across the full grid; the standard and Pro weights handle body and UI copy without ornament. The result is a typographic register borrowed from print art catalogs and auction supplements — hard left-aligned columns, condensed-uppercase category labels, price displayed in bold medium weight as a first-class UI element rather than a whispered afterthought. A bright secondary yellow (#f6e70f) surfaces on sale flags and special-edition markers, while teal (#088f87) carries editorial accent roles — featured-artist callouts, curated-collection banners — giving the otherwise binary black-and-amber palette a third dimension without softening the institutional tone. Cards sit on pale gray (#f0f0f0, #dedede) surfaces with minimal border radius — {rounded.xs} to {rounded.sm} — keeping the image plane sovereign. The platform is Shopify, but Artspace templates push well past default: multi-image artwork viewers, artist-biography modules, edition-count trackers (e.g. "Print 12 of 150"), and certificate-of-authenticity copy all run inline with the purchase flow, collapsing the distance between gallery wall text and the checkout button. Navigation reads institutional: a spare top bar in #231f20 with amber hover states and a single search affordance that expands to a full-screen overlay. The Phaidon parent-brand DNA shows in the footer — dense editorial link columns in caption-weight Akzidenz, structured like the back matter of an art monograph.

colors:
  primary: "#ffc800"
  primary-active: "#e6a800"
  primary-disabled: "#ffe480"
  primary-bright: "#f6e70f"
  ink: "#231f20"
  ink-deep: "#121212"
  body: "#3a3535"
  muted: "#888888"
  hairline: "#dedede"
  hairline-mid: "#cfcfcf"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  surface-pale: "#bad2df"
  on-primary: "#231f20"
  accent-teal: "#088f87"

typography:
  display-xl:
    fontFamily: "'akzidenz-grotesk-next-extend', 'akzidenz-grotesk-next', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'akzidenz-grotesk-next-extend', 'akzidenz-grotesk-next', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'akzidenz-grotesk-next', 'akzidenz-grotesk-next-pro', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.16
    letterSpacing: 0
  artist-name:
    fontFamily: "'akzidenz-grotesk-next-conden', 'akzidenz-grotesk-next', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  title-md:
    fontFamily: "'akzidenz-grotesk-next', 'akzidenz-grotesk-next-pro', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.28
    letterSpacing: 0
  title-sm:
    fontFamily: "'akzidenz-grotesk-next', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price-display:
    fontFamily: "'akzidenz-grotesk-next', 'akzidenz-grotesk-next-pro', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  body-md:
    fontFamily: "'akzidenz-grotesk-next', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'akzidenz-grotesk-next', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'akzidenz-grotesk-next', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  category-label:
    fontFamily: "'akzidenz-grotesk-next-conden', 'akzidenz-grotesk-next', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  edition-counter:
    fontFamily: "'akzidenz-grotesk-next-conden', 'akzidenz-grotesk-next', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'akzidenz-grotesk-next', 'akzidenz-grotesk-next-pro', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.75px
    textTransform: uppercase
  button-sm:
    fontFamily: "'akzidenz-grotesk-next', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.75px
    textTransform: uppercase
  nav-link:
    fontFamily: "'akzidenz-grotesk-next', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.canvas}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 60px
    hoverTextColor: "{colors.primary}"
    borderBottom: none
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    padding: 8px
    artistNameTypography: "{typography.artist-name}"
    artistNameColor: "{colors.ink}"
    titleTypography: "{typography.body-sm}"
    titleColor: "{colors.body}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    editionTypography: "{typography.edition-counter}"
    editionColor: "{colors.muted}"
    hoverEffect: "image scale 1.03"
  artwork-detail-module:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    artistTypography: "{typography.artist-name}"
    editionTypography: "{typography.edition-counter}"
    editionColor: "{colors.muted}"
    buyButtonVariant: "button-primary"
    offerButtonVariant: "button-secondary"
    padding: 32px 48px
  price-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  sale-badge:
    backgroundColor: "{colors.primary-bright}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  edition-counter-badge:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.edition-counter}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.category-label}"
    rounded: "{rounded.xs}"
    padding: 4px 12px
  featured-banner:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.category-label}"
    padding: 8px 16px
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    minHeight: 520px
    ctaVariant: "button-primary"
    overlayOpacity: 0.55
  search-overlay:
    backgroundColor: "{colors.canvas}"
    inputTypography: "{typography.display-sm}"
    inputBorderBottom: "2px solid {colors.ink}"
    rounded: "{rounded.none}"
    backdropColor: "rgba(35, 31, 32, 0.85)"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.caption}"
    headingTypography: "{typography.category-label}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.primary}"
    columns: 4
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — Amber (#ffc800) fill with near-black (#231f20) on-primary text and zero border radius; the flat silhouette reads as a hard institutional stamp rather than a consumer CTA. Uppercase tracking in weight-700 Akzidenz gives it the authority of a lot label. Active state shifts to #e6a800; disabled state bleaches to #ffe480 at reduced opacity.

**`button-secondary`** — White fill with a 1px solid ink border, same uppercase button-md typography, same flat corners. On hover it inverts to ink-fill / white-text, maintaining the high-contrast binary schema. Used for "Make Offer," "Save," and secondary navigation actions.

**`button-ghost`** — White outline variant for placement on the hero overlay or dark editorial banners. Follows the same inversion pattern as button-secondary but starts from a transparent base, preserving image legibility behind the CTA.

### Text Input

**`text-input`** — Square-cornered field with a 1px hairline border that upgrades to 1px ink on focus. No shadow, no soft radius. Height of 48px matches buttons for grid regularity across form rows. Placeholder text in muted at body-sm scale.

### Navigation

**`nav-bar`** — 60px bar in ink (#231f20) with white text and amber (#ffc800) hover states. Logo lockup runs in white Akzidenz; primary nav links use nav-link typography with generous horizontal spacing. A persistent search icon at the right edge triggers the `search-overlay`. On mobile the bar collapses to wordmark plus hamburger.

### Product Card

**`product-card`** — Zero-radius card on white or #f0f0f0 surface. Image occupies a 4:5 aspect ratio with a subtle scale on hover. Below the image: artist name in condensed uppercase (artist-name typography, ink), artwork title in body-sm (body color), edition count in edition-counter typography (muted), and price in price-display weight (ink). An amber `price-badge` overlays the image corner for time-limited or reduced-price works; a `sale-badge` in #f6e70f distinguishes reduced editions.

### Artwork Detail Module

**`artwork-detail-module`** — The right-hand purchase panel in the PDP two-column layout. Price in price-display weight is the first visual anchor, immediately followed by an `edition-counter-badge` and a stacked two-button group: `button-primary` ("Buy Now") above `button-secondary` ("Make Offer"). Artist name in uppercase condensed above the title, wall text in body-md, and certificate-of-authenticity copy in caption-weight below a hairline rule.

### Badges

**`price-badge`** — Amber fill, on-primary text, zero radius, uppercase button-sm. Overlays the image corner on product cards to signal a specific price point or availability tier.

**`sale-badge`** — Bright yellow (#f6e70f) fill, same structure. Distinguishes sale or reduced-price editions from standard inventory; the two yellows read as a deliberate hierarchy rather than a palette accident.

**`edition-counter-badge`** — Transparent fill with 1px hairline border, muted text, condensed uppercase. Renders edition data ("12 of 150 remaining") inline with the price stack on the PDP.

**`category-chip`** — Small uppercase condensed label on soft-gray (#f0f0f0), {rounded.xs}. Used for filtering browse grids by medium (Photography, Painting, Prints), period, or price tier.

### Featured Banner

**`featured-banner`** — Full-width teal (#088f87) strip in white condensed-uppercase type. Breaks the black-and-amber schema to signal editorial curation — "Artist of the Week," "Phaidon Picks," "New Arrivals." Sits as a section divider between product grid modules rather than at page top.

### Hero

**`hero`** — Full-bleed photography or video with a 0.55-opacity ink overlay. Headline in display-xl (extended variant, white), subhead in display-sm, and a `button-primary` CTA anchored bottom-left. Minimum 520px height; no radius anywhere in the module.

### Search Overlay

**`search-overlay`** — Full-viewport white takeover. A single large input at display-sm scale uses a 2px solid ink underline rather than a boxed border, prioritizing the editorial feel over form convention. Results populate below in product-card density. Backdrop uses rgba(35, 31, 32, 0.85) before the panel is fully loaded.

### Footer

**`footer`** — Four-column link grid on ink (#231f20) background, capped by a 3px amber top border that echoes the primary action color as a structural delimiter. Column headings in category-label typography (white condensed uppercase); link body in caption scale (hairline-gray, amber on hover). Phaidon and partner logos sit in the bottom row at reduced-opacity white.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + slide-in drawer; hero stacks text above cropped image; artwork detail module scrolls below full-bleed image; sticky 80px buy-bar pins to viewport bottom |
| Tablet | 744–1128px | Two-column product grid; nav shows primary links plus hamburger for secondary categories; hero maintains overlay at reduced type scale |
| Desktop | 1128–1440px | Three- to four-column product grid; full horizontal nav; artwork PDP runs two-column (image left, detail panel right) |
| Wide | > 1440px | Max-width container centers at ~1440px; hero image bleeds to viewport edge; footer columns gain proportional breathing room |

### Touch Targets

- All buttons and nav links maintain a minimum 44×44px tap area regardless of visual size
- Product cards use a full-image tap zone; the artist-name link is a separate, secondary tap target
- Category chips floor at 36px height with {spacing.sm} horizontal padding
- "Buy Now" and "Make Offer" buttons hold 48px height on mobile — no reduction for space savings
- Hamburger icon minimum 44×44px with no overlap into adjacent logo zone

### Collapsing Strategy

- Top nav loses secondary category links first; hamburger reveals full taxonomy in a stacked full-height drawer
- Product grid steps 4 → 3 → 2 → 1 column as viewport narrows through breakpoints
- Featured banners remain full-width at all breakpoints; headline scales from display-md to title-md on mobile
- Footer transitions from 4-column to 2-column to single-column accordion pattern on mobile
- Artwork detail buy-panel becomes a sticky bottom strip on mobile, with price and primary CTA always visible without scrolling

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Border radius values not directly confirmed from CSS extraction; {rounded.none} and {rounded.xs} inferred from editorial art-gallery convention and flat visual appearance of extracted screenshots
- Muted text color (#888888) was absent from the extracted palette; derived as a reasonable mid-gray placeholder — actual value may differ
- Role of #bad2df (soft blue) is ambiguous; could be decorative illustration tinting, a partner-brand badge, or subcategory highlight — no confirmed component context extracted
- Exact hover/focus state colors for inputs and secondary nav links not confirmed from live extraction
- Animation and transition timing (hover fade duration, overlay entrance) not extractable from static extraction
- Mobile navigation pattern (hamburger drawer vs. tabbed bottom bar) not confirmed from extraction
- Desktop grid gutter width and max-content-width values not extracted; 24px gutters at 1440px max assumed from convention
- Dark-mode or high-contrast variant not confirmed; extracted palette is entirely light-canvas-oriented
- Exact Akzidenz-Grotesk Next license weights and whether "Pro" includes optical sizes beyond standard is not confirmed; extended and condensed sub-families assumed available as loaded font stacks suggest all variants are active
