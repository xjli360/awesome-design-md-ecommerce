---
version: alpha
name: "Duesenberg"
source_url: "https://www.duesenberg.de"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The parchment warmth of #e4e2d5 anchors a site that would rather whisper Duisburg workshop than broadcast e-commerce — a cream ground that reads more like an aged guitar catalog than a contemporary DTC storefront. Duesenberg's instruments draw from the same 1930s-to-1950s American visual grammar as the automobiles that lend the brand its name: binding details, bound headstocks, sparkle finishes. Digitally, that heritage surfaces in the restraint of an almost entirely system-font type stack — no custom display typeface claims the foreground; the guitars themselves provide the visual energy. Primary interactions run through an assertive #0062cc, a blue inherited from Bootstrap's utility layer rather than a bespoke brand color, which puts CTA work in serviceable hands without upstaging product photography. Dark near-blacks (#1d2124, #1b1e21) anchor footers and immersive hero sections, creating the shadow-box context that vintage instrument photography demands. Spec data renders in monospace via Consolas or Courier New — a legible nod to the technical precision that German manufacturing implies. Rounded corners stay conservative: {rounded.xs} on buttons and inputs keeps UI geometry squared-off, matching the angular cutaways and binding edges of the instruments themselves. Guitar model names carry the brand's real typographic personality — typically set large, tight-tracked, with enough weight to feel structural rather than decorative. The extracted palette's Bootstrap-pattern secondary colors (success greens, warning ambers, danger reds) appear to drive badge and alert states rather than brand expression, meaning the site's true visual identity rests almost entirely on photography and hardware chrome, with typography and color playing a supporting structural role.

colors:
  primary: "#0062cc"
  primary-active: "#004085"
  primary-disabled: "#b8daff"
  ink: "#1d2124"
  body: "#383d41"
  muted: "#545b62"
  hairline: "#c8cbcf"
  canvas: "#e4e2d5"
  surface-soft: "#dae0e5"
  surface-card: "#ffffff"
  surface-mid: "#ececf6"
  on-primary: "#ffffff"
  on-dark: "#e4e2d5"
  near-black: "#1b1e21"
  link: "#9fcdff"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.6px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  series-tag:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.1px
  spec-label:
    fontFamily: "Consolas, 'Courier New', 'Liberation Mono', Menlo, Monaco, SFMono-Regular, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.3px

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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
  button-secondary-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    border: "2px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    shadow: "0 2px 8px rgba(0,0,0,0.08)"
    padding: "{spacing.base}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    overlayOpacity: 0.55
    minHeight: 520px
    titleTypography: "{typography.display-xl}"
    rounded: "{rounded.none}"
  guitar-model-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  series-label:
    textColor: "{colors.muted}"
    typography: "{typography.series-tag}"
    backgroundColor: transparent
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    rowAlternate: "{colors.canvas}"
  finish-chip:
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    size: 32px
    activeBorderColor: "{colors.primary}"
    activeBorderWidth: 2px
  dealer-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    metaTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.link}"
    headingTypography: "{typography.title-sm}"
  artist-signature-card:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    labelTypography: "{typography.series-tag}"
    nameTypography: "{typography.title-md}"

## Components

### Buttons
**`button-primary`** — Solid #0062cc fill, white text, 44px tall with {rounded.xs} corners and 12px/24px padding. Darkens to #004085 on active/hover press. Used for "Add to Cart," "Contact Dealer," and primary checkout actions across product and contact pages. The disabled state fades fill to #b8daff and should suppress pointer events entirely.

**`button-secondary`** — Transparent background with a 2px solid #0062cc border and matching text color, sharing the {rounded.xs} geometry and 44px height of the primary. Used for secondary actions such as "Download Spec Sheet" or "View Full Series" where hierarchy must defer to the primary CTA. On dark hero backgrounds, swap to `button-secondary-dark` which reverses to #e4e2d5 border and text.

### Nav Bar
**`nav-bar`** — 64px tall bar sitting on the warm #e4e2d5 canvas, separated from page content by a 1px #c8cbcf hairline. Navigation links use {typography.nav-link} at weight 500; the Duesenberg wordmark anchors the left. Series categories (Guitars, Artists, Dealers, About) fan right with a dropdown revealing model families. On scroll past the hero, the bar may invert to the near-black (#1b1e21) background with {colors.on-dark} text.

### Product Card
**`product-card`** — White (#ffffff) surface card at {rounded.sm} with a 0 2px 8px shadow that lifts instruments off the warm cream background. Guitar name renders in {typography.title-md}, model series in {typography.caption} uppercase. The card hosts a dominant product image at roughly a 3:4 aspect ratio above a minimal text block containing price and a primary CTA button.

### Hero Banner
**`hero-banner`** — Full-width dark backdrop (#1d2124) or photography panel with a 0.55 overlay, minimum 520px tall, delivering the brand's primary visual statement. Title text uses {typography.display-xl} in {colors.on-dark}, reinforcing the parchment-to-dark contrast motif. A single CTA button sits beneath the headline, typically `button-secondary-dark` so it reads light on dark without blue-on-blue collision.

### Guitar Model Badge
**`guitar-model-badge`** — Compact #0062cc tile at {rounded.xs} with 4px/10px padding. Denotes series affiliation — Starplayer, Bonneville, Gran Majesto — directly on product cards and listing pages in {typography.caption} weight. Keeps labels concise, maximum two words, so multiple badges can stack without crowding.

### Series Label
**`series-label`** — Uppercase {typography.series-tag} in {colors.muted} with 1.5px letter-spacing, placed above product names to establish model-family context before the specific guitar title asserts itself. No background or border — purely typographic hierarchy, rendered transparently over any surface.

### Spec Table
**`spec-table`** — Zero-radius table with alternating {colors.canvas} and {colors.surface-soft} rows, organizing scale length, pickup configuration, hardware finish, nut width, and country of manufacture. Label column renders in {typography.spec-label} monospace; value column in {typography.body-sm}. No rounded corners — the squared geometry echoes instrument body edges.

### Finish Chip
**`finish-chip`** — 32px circular swatch ({rounded.full}) with a 1px {colors.hairline} border showing available guitar finish options. Clicking a chip updates the product hero image to the selected colorway. Active state applies a 2px {colors.primary} ring with 2px offset to signal selection without covering the swatch color.

### Dealer Card
**`dealer-card`** — White card at {rounded.sm} with a 1px {colors.hairline} border, listing dealer name in {typography.title-sm}, address and phone in {typography.body-sm}, and city/region in {typography.caption} muted. Used in the dealer-locator flow alongside a map panel, with distance displayed as a right-aligned caption.

### Artist Signature Card
**`artist-signature-card`** — Dark #1d2124 card at {rounded.sm} presenting endorsed artist name in {typography.title-md} in {colors.on-dark}, with the associated signature model referenced below in {typography.series-tag}. Photography of the artist or their guitar anchors the card at full bleed within the rounded boundary.

### Footer
**`footer`** — Full-bleed {colors.near-black} section with {typography.body-sm} text in {colors.on-dark} and links in {colors.link}. Organized into columns: Guitar Series, Artists, Support, Dealers, Company. Bottom row carries the made-in-Germany note and legal links in {typography.caption}.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav collapses all series links to accordion; hero min-height drops to 320px; spec table scrolls horizontally; finish chips enlarge tap area to 44px |
| Tablet | 744-1128px | Two-column product grid; nav stays visible with primary links only, no megamenu; hero at 420px |
| Desktop | 1128-1440px | Three-column product grid; full nav with dropdowns; hero at 520px; spec table fixed-width alongside a sticky buy-panel |
| Wide | > 1440px | Max-width container (~1380px) centered; product grid may extend to four columns; footer columns widen with additional gutter whitespace |

### Touch Targets
- All buttons minimum 44px tall
- Finish chip swatches padded to minimum 44px touch area despite 32px visual diameter
- Nav links minimum 44px tap height on mobile
- Dealer locator cards full-width tap targets on mobile with padding inside the card boundary

### Collapsing Strategy
- Navigation collapses to hamburger icon below 744px; series megamenu becomes a stacked accordion
- Spec tables switch to horizontal scroll at mobile breakpoint rather than collapsing columns
- Footer columns stack vertically on mobile, two-up on tablet, four-up on desktop
- Artist signature cards collapse from horizontal to vertical stack below 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand font detected; the site appears to use system font stack throughout. Duesenberg's print and packaging identity may use a custom display typeface not web-served.
- Extracted palette is heavily Bootstrap 4 utility-derived — success greens (#1e7e34, #155724), danger reds (#bd2130, #721c24), warning ambers (#d39e00, #856404), info teals (#117a8b, #0c5460). Only #e4e2d5 (warm cream) is clearly brand-specific rather than a Bootstrap default. True brand accent colors may live in photography or print assets only.
- Meta theme-color is absent; no mobile browser chrome color is defined.
- No logo SVG or wordmark color values extractable from CSS.
- Product photography color grading — the primary visual identity carrier for instrument brands — is not capturable from static CSS extraction.
- Art deco decorative motifs or vintage ornamental elements referenced in Duesenberg's physical brand identity are absent from the extracted digital palette and cannot be reliably specified here.
- No animation, transition-duration, or easing curve data extracted.
- Dealer-locator map tile styling and custom marker colors not inspectable from static extraction.
- Active/hover state contrast ratios unverified against WCAG 2.1 AA due to incomplete state color extraction.
