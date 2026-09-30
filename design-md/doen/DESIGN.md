---
version: alpha
name: "Doen"
source_url: "https://shopdoen.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The circumflex over the O in DÔEN is the brand's first typographic signal — an insistence on marking a familiar thing with something the eye doesn't expect, a precision that runs through every surface choice thereafter. The canvas is #f6f2e6, a warm parchment that reads as aged paper rather than a neutral web default, setting the entire shop inside a world that feels analog and archival rather than digital-first. Against it, primary text and CTA color is #333230, a near-black with enough brown warmth to read as ink on real paper rather than a CSS color chip. Snell Roundhand script carries the brand's most intimate voice — campaign headline accents, seasonal collection introductions — and never drops into UI chrome; it remains strictly an editorial register. Founders Caslon Roman and Italic form the editorial spine, sizing down to 14px for product captions and opening to 28–48px for seasonal display. Carta Nueva handles the largest display scale and the wordmark itself. Masqualero and Romaine appear as secondary display variants in lookbook contexts. Helvetica Neue and Inter absorb all utility UI — the brand maintains a sharp wall between editorial type and system type, never letting the two registers bleed. Color language is restrained and warm throughout: three surface temperatures layer the depth — parchment (#f6f2e6) as canvas, deeper warm taupe (#e6dccd) as card surface and hover register, and warm mid-gray (#8c897d) as the muted text value, all with the same earthy temperature rather than cooling toward neutral gray. An amber (#f59e0b) provides the single saturation note, appearing in editorial accent and footer link hover states. A blue (#334fb4) serves anchor link treatment in a controlled context. Radii are near-zero throughout: `{rounded.xs}` at most on form inputs, `{rounded.none}` on imagery and buttons — the aesthetic is flat-plane and print-adjacent. Product cards are portrait-dominant, photography-first, with Caslon captions below rather than overlaid. Navigation is a lean single bar: centered wordmark flanked by tracked uppercase categoricals. Mobile renders as a single-column editorial scroll — no carousel pagination, no mega-menu, just a vertical publication rhythm carried through to the smallest screen.

colors:
  primary: "#333230"
  primary-active: "#141414"
  primary-disabled: "#8c897d"
  ink: "#232323"
  body: "#545454"
  muted: "#77787b"
  muted-soft: "#b4b4b4"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#f6f2e6"
  surface-soft: "#f3f3f3"
  surface-card: "#fefefe"
  surface-parchment: "#e6dccd"
  on-primary: "#f6f2e6"
  on-dark: "#f6f2e6"
  accent-amber: "#f59e0b"
  accent-amber-bright: "#fbbf24"
  link: "#334fb4"
  scrim: "#141414"

typography:
  display-xl:
    fontFamily: "'Carta Nueva', 'Founders Caslon', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Carta Nueva', 'Founders Caslon', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Founders Caslon', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: -0.2px
  display-script:
    fontFamily: "'Snell Roundhand', 'Snell Roundhand Script', cursive"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Founders Caslon', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  body-md:
    fontFamily: "'Founders Caslon', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Founders Caslon', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.09em
    textTransform: uppercase
  caption-serif:
    fontFamily: "'Founders Caslon', Georgia, serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-wordmark:
    fontFamily: "'Carta Nueva', 'Founders Caslon', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.05em

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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 31px
    height: 44px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 0
    borderBottom: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    wordmarkTypography: "{typography.nav-wordmark}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.caption-serif}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.body}"
    hoverSurface: "{colors.surface-parchment}"
    gapSpacing: "{spacing.sm}"
  hero-editorial:
    backgroundColor: "{colors.primary}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.on-dark}"
    scriptAccentTypography: "{typography.display-script}"
    scriptAccentColor: "{colors.on-dark}"
    ctaTypography: "{typography.button-md}"
    minHeight: 90vh
  campaign-script-accent:
    fontStyle: "{typography.display-script}"
    textColor: "{colors.primary}"
    backgroundColor: "transparent"
    paddingTop: "{spacing.lg}"
    paddingBottom: "{spacing.lg}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.primary}"
    selectedBackground: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    unavailableStrikeColor: "{colors.hairline}"
    height: 40px
    minWidth: 40px
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.primary}"
    borderOffset: 2px
  newsletter-form:
    backgroundColor: "{colors.surface-parchment}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    inputBackgroundColor: "{colors.canvas}"
    inputBorder: "1px solid {colors.hairline}"
    inputTypography: "{typography.body-md}"
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitTypography: "{typography.button-md}"
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.accent-amber}"
    paddingVertical: "{spacing.xxl}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 44px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  tag-chip:
    backgroundColor: "{colors.surface-parchment}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 4px 12px

## Components

### Buttons
**`button-primary`** — A flat ink block with zero border radius, tracked uppercase Helvetica Neue at 12px, 0.12em letter-spacing. The #333230 background with parchment text (#f6f2e6) reads as a letterpress impression rather than a digital affordance. Active state deepens to #141414; disabled holds the warm gray (#8c897d) rather than collapsing to a cold neutral, preserving temperature even when inactive. Min height 44px for accessibility despite the visually compressed type.

**`button-secondary`** — Ghost treatment: transparent fill, 1px solid #333230 border, identical uppercase type. Hover inverts to filled primary. Used for secondary page actions — "View All," "Add to Wishlist" — wherever a full button block would feel too heavy against the parchment ground.

**`button-ghost`** — Inline text link with a 1px bottom border, no background, no box. Used within editorial copy sections where a button rectangle would interrupt the layout's print-adjacent rhythm. The underline is the only affordance signal.

### Text Inputs
**`text-input`** — Flat-sided with a single 1px hairline (#dedede) border at all sides and no rounding. Focus upgrades the border to 1px solid primary — no glow, no box-shadow. The input inherits the canvas parchment background so form fields feel continuous with the page rather than isolated white boxes.

### Navigation
**`nav-bar`** — A 56px bar on parchment canvas. The DÔEN wordmark in Carta Nueva sits centered at 20px with 0.05em letter-spacing. Category links (Dresses, Tops, Bottoms, etc.) run in 11px tracked uppercase Helvetica Neue; on tablet and up these flank the wordmark horizontally, on mobile the bar reduces to logo-only with a hamburger. A hairline bottom border separates the bar from page content. Cart count, search, and account icons occupy the far right at 44×44px touch targets.

### Product Card
**`product-card`** — Portrait 3:4 photography, full-bleed, zero rounding, no drop shadow, no border. A secondary editorial image may swap in on hover via an opacity crossfade. Title in Founders Caslon 14px runs beneath the image; price in 12px caption-serif beneath that. The gutter between cards is `{spacing.sm}` on mobile, expanding to `{spacing.base}`–`{spacing.lg}` on wider grids. The entire card feels like a catalogue page cut into a grid.

### Hero Editorial
**`hero-editorial`** — Full-viewport-height imagery with the Carta Nueva headline overlaid at display-xl (48px, –0.5px tracking). A Snell Roundhand script accent in display-script (40px) occupies a secondary line beneath the headline, carrying the seasonal collection name or campaign tagline. A single button-md CTA sits centered near the lower third. On mobile the type stack repositions below a square-cropped image rather than overlaying it.

### Campaign Script Accent
**`campaign-script-accent`** — A standalone Snell Roundhand element used outside the hero in editorial content rows and collection introductions. Never appears in navigation, forms, or UI chrome — strictly a layout accent. Set in primary dark on parchment, sized 36–48px depending on context, with `{spacing.lg}` vertical padding above and below to preserve the open-page feeling.

### Size Selector
**`size-selector`** — Flat square tiles with hairline borders, 40×40px minimum. Selected state inverts to filled primary (#333230) with parchment text. Unavailable sizes carry a diagonal strike-through line in hairline gray; the tile itself stays visible rather than vanishing. No border radius — the tiles match the button's flat-plane logic exactly.

### Newsletter Form
**`newsletter-form`** — A full-width section with surface-parchment (#e6dccd) background, one temperature step warmer than canvas. Headline in Founders Caslon display-md. The email input and submit button use standard flat styles: no rounding, 1px hairline border on input, filled primary submit. Vertical padding at 48px gives the module the breathing room of a print advertisement rather than a squeezed signup bar.

### Footer
**`footer`** — Rendered on the primary dark (#333230), creating a dense page terminus that reads as the back cover of a lookbook. Link columns in 11px uppercase Helvetica Neue in parchment (#f6f2e6); hover state shifts link color to amber (#f59e0b), the one place that accent color serves navigation. Social icons sit alongside the newsletter prompt in a horizontal lockup. On mobile, columns collapse to a stacked accordion with hairline separators.

### Color Swatch
**`color-swatch`** — 20px circles, the only element that uses `{rounded.full}`. Selected state shows a 2px primary border with a 2px offset gap, producing a ring-selection halo. No border on unselected. Tap target expands to 32×32px via transparent padding beyond the visible diameter.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to centered wordmark + hamburger drawer; hero image crops square with type block below; display-xl scales to display-lg (36px); footer columns stack to accordion |
| Tablet | 744–1128px | Two-column product grid; full horizontal nav with abbreviated category labels; hero at full viewport height; editorial split sections use 50/50 image+text |
| Desktop | 1128–1440px | Three- or four-column product grid; complete nav with all categories; campaign script accents display at full 40px; asymmetric editorial layouts (60/40) available |
| Wide | > 1440px | Content max-width ~1440px centered with auto margins; hero imagery bleeds edge-to-edge while text block constrains to ~720px reading width; product grid may expand to five columns |

### Touch Targets
- All buttons maintain 44px minimum height regardless of visual label size
- Size selector tiles are minimum 40×40px with tap target padding beyond the visible hairline border
- Nav icons (cart, search, hamburger) have 44×44px touch regions
- Color swatches expand tap target to 32×32px despite the 20px visual circle
- Footer accordion headers are minimum 48px tall

### Collapsing Strategy
- Category navigation collapses to a full-screen left drawer on mobile; drawer background uses surface-parchment (#e6dccd) to maintain the warm palette even off-canvas
- Product filters shift from a horizontal filter-bar to a bottom sheet modal triggered by a flat uppercase "Filter" button
- Editorial two-column splits reflow to single column with image above text, maintaining the editorial sequence
- Script headline accents reduce from 40px to 28px on mobile to prevent overflow while preserving Snell Roundhand; they do not fall back to sans-serif
- The nav wordmark drops from 20px to 16px on mobile to accommodate icon targets on either side

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact weights for Carta Nueva, Masqualero, and Romaine are not extractable; 400 (regular) assumed for all three — confirm if bold variants exist
- The amber values (#f59e0b, #fbbf24) appear in the extracted palette but their precise role — sale price, editorial accent, hover only, badge fill — could not be confirmed and is inferred from common brand practice
- The blue (#334fb4) appears in the extracted palette; whether it is a standard anchor link color or a campaign-period accent could not be confirmed from extraction alone
- Exact nav height is estimated at 56px from Shopify fashion theme conventions; the true computed height may differ by a few pixels
- Motion and transition tokens (hover fade duration, image crossfade timing, drawer animation) are not extractable and are not defined here
- Whether Snell Roundhand is served as a web font or exists only in static imagery and SVG exports is unconfirmed; the file assumes web font delivery
- Dark-mode variant is unknown; no dark-specific overrides are defined
- Exact product-card hover behavior (image swap vs. overlay scrim vs. both) is inferred from documented brand practice rather than confirmed by extraction
