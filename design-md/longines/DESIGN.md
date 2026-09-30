---
version: alpha
name: "Longines"
source_url: "https://www.longines.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The winged hourglass stamped on every Longines dial since 1889 doubles as a design philosophy — precision housed inside a silhouette so spare it approaches abstraction. On screen the same economy holds: a white canvas ({colors.canvas}) stretches to the viewport edge and the signature red (#BF1B2C) deploys only at counted pressure points — the primary CTA fill, the logo's outer border accent, the thin rule beneath an active category tab — never as ambient wash or atmospheric fill. Display type defaults to a classical serif, evoking the engraved lettering found on a watch caseback rather than a screen-native grotesque; body copy shifts to a neutral sans-serif so long-form readability stays unforced. Longines occupies a precise niche between haute horlogerie and aspirational luxury, and the component system reflects that calibration: corners barely register ({rounded.xs} at 2px), hero images run cinematically full-bleed and unhurried, and gold (#B8966C) surfaces only in material selectors and price readouts, never as a brand color spread broadly. Product cards behave like museum frames — white ground, centered watch photography, a minimum of metadata beneath — while the model selector for case diameter and strap material reads as a printed specification table rather than a style configurator. Filter and navigation overlays are quiet and quickly dismissed; the search field expands on focus from a single understated icon. Every interactive decision is soft but definitive, echoing the haptic precision of a correctly regulated crown. The overall register is that of an atelier catalogue: scroll depth, hero pacing, and whitespace allocations operate at a cadence slower than typical e-commerce convention, trusting photography to carry the selling weight and reserving brand red for the one moment a visitor needs to act.

colors:
  primary: "#BF1B2C"
  primary-active: "#991522"
  primary-disabled: "#E9A9AF"
  accent-gold: "#B8966C"
  ink: "#1A1A1A"
  body: "#3D3D3D"
  muted: "#6E6E6E"
  hairline: "#D9D9D9"
  hairline-soft: "#EFEFEF"
  canvas: "#FFFFFF"
  surface-soft: "#F5F4F2"
  surface-card: "#FFFFFF"
  surface-dark: "#1A1A1A"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.02em
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 34px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.02em
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.01em
  title-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  title-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
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
    letterSpacing: 0.03em
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  price-display:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.01em
  label-xs:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.14em
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  base: 24px
  lg: 32px
  xl: 48px
  xxl: 64px
  section: 96px

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
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
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
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.on-dark}"
    padding: 13px 31px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
    activeIndicatorColor: "{colors.primary}"
    scrollShadow: "0 2px 12px rgba(0,0,0,0.08)"
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.section}"
    borderTop: "1px solid {colors.hairline}"
    columnHeadTypography: "{typography.label-xs}"
    columnHeadColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspect: "1 / 1"
    padding: "{spacing.xl}"
    collectionTypography: "{typography.caption}"
    collectionColor: "{colors.muted}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    hoverElevation: "box-shadow: 0 4px 16px rgba(0,0,0,0.08)"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    ctaComponent: "button-ghost"
    imageBleed: full-viewport
    overlayColor: "rgba(0,0,0,0.30)"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xxl}"
    contentAlign: bottom-left
  collection-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-md}"
    ctaColor: "{colors.primary}"
    padding: "{spacing.section}"
    imageAspect: "3 / 4"
    layout: alternating-image-text
  model-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.label-xs}"
    labelColor: "{colors.muted}"
    swatchSize: 28px
    swatchBorderActive: "2px solid {colors.ink}"
    swatchBorderInactive: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    pillPaddingActive: "4px 14px"
  watch-specs-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    dividerColor: "{colors.hairline}"
    paddingVertical: "{spacing.xl}"
    paddingHorizontal: "{spacing.xxl}"
  price-tag:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
    currencyColor: "{colors.muted}"
    taxNoteTypography: "{typography.caption}"
    taxNoteColor: "{colors.muted}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    padding: "{spacing.sm} 0"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.label-xs}"
    headingColor: "{colors.primary}"
    dividerColor: "rgba(255,255,255,0.12)"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Filled with Longines red (#BF1B2C), sharp corners ({rounded.none}), uppercase tracked lettering via {typography.button-md}, and a 48px hit area. Hover darkens to the primary-active shade (#991522) without transition delay — the brand favors crisp state changes over animated transitions. The disabled state renders a muted rose ({colors.primary-disabled}); the button stays fully opaque rather than fading to ghost.

**`button-secondary`** — White canvas with a 1px {colors.ink} border and matching uppercase treatment. Appears alongside button-primary on product detail pages and as the lone CTA in editorial collection strips where the primary slot is already saturated by imagery. Active state inverts: ink background, white text.

**`button-ghost`** — Transparent fill, 1px white border, white {typography.button-md} label. Used exclusively over full-bleed dark hero panels where the brand red would be absorbed by photographic backgrounds. Never appears on light-canvas surfaces.

### Navigation

**`nav-bar`** — A 72px white bar with a 1px hairline bottom border. The winged-hourglass wordmark sits left-aligned; the right cluster carries bag count, search icon, and language/region selector. Center links are {typography.nav-link} uppercase with no underline default; on hover a 2px {colors.primary} rule appears beneath the active item and a full-width mega-menu drops below. On scroll the bar acquires a soft drop-shadow to maintain separation from page content.

**`nav-mega-menu`** — Full-width overlay descending flush below the nav bar on category hover. Laid out in three to four columns; column headings use {typography.label-xs} in {colors.primary}, links beneath in {typography.body-sm}. The rightmost column hosts a campaign image or new-arrival editorial tile. Background is pure {colors.canvas} with a 1px {colors.hairline} top border; no overlay scrim behind it on desktop.

### Inputs

**`text-input`** — Zero border radius ({rounded.none}), 1px {colors.hairline} border sharpening to 1px {colors.ink} on focus. Placeholder in {colors.muted}. Appears in the search overlay (which expands from an icon trigger to a centered full-width input) and the footer newsletter form. No filled or floating-label variant — the label sits above the field as a static {typography.label-xs} string.

### Product Card

**`product-card`** — White card, flush edges, internal padding of {spacing.xl}. Watch image centered at 1:1 aspect ratio with generous breathing room above and below. Collection name in {typography.caption} uppercase {colors.muted} sits above; model name in {typography.title-sm} and price in {typography.price-display} appear below. On hover a subtle elevation shadow (0 4px 16px rgba 8%) lifts the card — no color change, no border reveal. No inline "Add to Cart" on listing pages; clicking routes to the PDP.

### Hero Banner

**`hero-banner`** — Full-viewport-width cinematic panel with a 30% black overlay scrim. Headline in {typography.display-xl} white, subhead in {typography.display-sm} white, followed by a single `button-ghost` CTA. Content aligns bottom-left on desktop, shifts to center-bottom on mobile for thumb ergonomics. Image never crops at a hard rule — the overlay grades naturally from the photography. Aspect on mobile collapses to approximately 3:4.

### Collection Strip

**`collection-strip`** — Alternating image-left / image-right editorial modules used for collection storytelling below the hero. Image column at 3:4 aspect, text column alongside with {typography.display-md} headline, {typography.body-md} body, and a text-link CTA rendered in {colors.primary} using {typography.button-md}. Padding is {spacing.section} on all sides; the alternating rhythm prevents the page from reading as a simple product grid.

### Model Selector

**`model-selector`** — A specification-table-style variant picker for case diameter (displayed in millimeters) and strap/bracelet material. Diameter options appear as small text pills with sharp corners and a 1px {colors.hairline} border; the active pill switches to a 2px {colors.ink} border with no background fill change. Material swatches are 28×28px circles with the same border logic. No {rounded.full} treatment — the selector stays sharp-cornered, consistent with the rest of the component library. Section label above each group uses {typography.label-xs} in {colors.muted}.

### Watch Specs Panel

**`watch-specs-panel`** — A definition-list panel on {colors.surface-soft} presenting movement type, power reserve, water resistance, case dimensions, and crystal material. Labels in {typography.caption} {colors.muted}, values in {typography.body-sm} {colors.ink}, rows separated by 1px {colors.hairline} dividers. Vertical padding {spacing.xl}, horizontal {spacing.xxl}. Appears below the model selector on the PDP, before the long-form description.

### Price Tag

**`price-tag`** — Price value in {typography.price-display} {colors.ink}; currency symbol rendered at a slightly smaller size in {colors.muted}. Tax notation (e.g., "incl. VAT") in {typography.caption} {colors.muted} sits on a second line. No strike-through, no badge surround — price reads as editorial metadata rather than a commercial claim.

### Footer

**`footer`** — Full-width dark panel ({colors.surface-dark}) with white text. Column headings in {typography.label-xs} {colors.primary}, links in {typography.body-sm} white, shifting to {colors.primary} on hover. Social icons as small outlined circles. The winged-hourglass wordmark appears in white at the bottom-center above legal copy. A newsletter email input spans the top row at full width on mobile. Dividers between columns are rgba white at 12% opacity rather than a solid hairline.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero collapses to 3:4 aspect; nav becomes left-slide hamburger drawer with accordion categories; product grid 1-up; specs panel becomes single-column definition list |
| Tablet | 744–1128px | 2-column product grid; hero at 16:9; nav bar retains all primary links; mega-menu opens as full-width overlay |
| Desktop | 1128–1440px | 3-column product grid; hero full-viewport; mega-menu at full width; specs panel sits beside product image in a two-column PDP layout |
| Wide | > 1440px | Max-width container centered at 1440px; hero image scales to fill; lateral padding increases proportionally; content columns held at 1440px cap |

### Touch Targets
- All interactive elements hold a minimum 44×44px touch target on mobile, including swatch circles and nav icons
- The search icon tap region extends 8px beyond the visible glyph on all sides
- Model-selector diameter pills expand to at least 44px tall on screens narrower than 744px
- Footer links gain {spacing.xs} additional vertical padding on touch viewports to reduce mis-tap rate

### Collapsing Strategy
- Navigation collapses to a hamburger icon below 744px; the drawer slides from the left and presents all collection categories as an accordion, each expanding to its sub-links
- Mega-menu columns compress to a single scrollable list inside the mobile drawer; campaign image tile is hidden
- Collection strips reflow from side-by-side to stacked (image above, text below) below 744px; alternating layout is abandoned at this breakpoint
- Watch specs panel transitions from a two-column grid to a single-column definition list on mobile
- Hero CTA button shifts from bottom-left to center-bottom on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site (likely loaded via JavaScript or behind bot-detection); all palette values are estimated from widely observable Longines brand materials and may deviate from exact production tokens
- No font families were extracted; actual Longines web fonts are almost certainly a custom or licensed typeface — the serif/sans-serif stacks above are fallback approximations only
- Exact button and input border-radius values not confirmed; {rounded.none} is an inference from the brand's precision-instrument aesthetic
- Meta theme-color absent; mobile browser chrome color unverified
- Animation easing curves, transition durations, and parallax scroll behavior not captured
- Exact grid gutter widths and column counts on desktop and tablet not confirmed from extraction
- Longines operates locale-specific storefronts (CH, US, EU, Asia-Pacific); component details such as currency display, tax notation, and size-table conventions may vary by region
- Accent gold value (#B8966C) is estimated from photographed marketing materials; actual swatch hex may differ
