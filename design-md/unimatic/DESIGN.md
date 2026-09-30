---
version: alpha
name: "Unimatic"
source_url: "https://www.unimaticwatches.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Forty watches. That's often the total production run for a Unimatic model—a number that appears on the dial itself, not buried in marketing copy. The site delivers exactly that constraint aesthetic: near-black canvas (#111111), Aktiv Grotesk Thin stretched across hero widths at {typography.display-xl} scale, and a ruthless economy of color where #eeeeee body text on dark ground does most of the communicative work. The extracted palette skews heavily toward darks (#1e1e1e, #313131, #32373c) with neutral grays (#646464, #555555, #444444) for secondary hierarchy, and a single accent—#003388, a deep naval blue that reads more ink than accent, appropriate for an Italian brand that names its models with military reference codes (U1-S for subaqueo, U3-D for diver). Aktiv Grotesk runs the full weight range from thin display headlines to regular body copy, giving the type system tonal range without switching families. There are no rounded corners worth speaking of—every surface is {rounded.none}, flush to the grid; the language is utilitarian, not friendly. Photography drives the product experience: watches photographed against matte surfaces, technical detail shots, wrist context images. The model-code tag—U1, U3, U5 prefixed designations—functions as the brand's primary navigational language, and the edition-number component (e.g. "12/50") carries aspirational weight out of proportion to its size. A site-wide dark mode isn't a style choice but a structural one: these instruments were designed in low-light operational conditions, and the digital environment reflects that.

colors:
  primary: "#003388"
  primary-active: "#002266"
  primary-disabled: "#32373c"
  ink: "#eeeeee"
  body: "#646464"
  muted: "#555555"
  hairline: "#32373c"
  canvas: "#111111"
  surface-soft: "#1e1e1e"
  surface-card: "#313131"
  on-primary: "#eeeeee"
  on-dark: "#eeeeee"
  mid-gray: "#444444"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'aktiv-grotesk-thin', 'aktiv-grotesk', sans-serif"
    fontSize: 72px
    fontWeight: 100
    lineHeight: 1.0
    letterSpacing: -2px
  display-lg:
    fontFamily: "'aktiv-grotesk-thin', 'aktiv-grotesk', sans-serif"
    fontSize: 48px
    fontWeight: 100
    lineHeight: 1.05
    letterSpacing: -1.5px
  display-md:
    fontFamily: "'aktiv-grotesk', sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  title-md:
    fontFamily: "'aktiv-grotesk', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "'aktiv-grotesk', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  body-md:
    fontFamily: "'aktiv-grotesk', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'aktiv-grotesk', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'aktiv-grotesk', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  model-code:
    fontFamily: "'aktiv-grotesk', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 2px
    textTransform: uppercase
  edition-number:
    fontFamily: "'aktiv-grotesk-thin', 'aktiv-grotesk', sans-serif"
    fontSize: 13px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 1px
  button-md:
    fontFamily: "'aktiv-grotesk', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 2px
    textTransform: uppercase
  nav-item:
    fontFamily: "'aktiv-grotesk', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 1.5px
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 44px
    border: "1px solid {colors.ink}"
  button-primary-hover:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.primary-disabled}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-item}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    imageAspectRatio: "1/1"
  product-card-label:
    typography: "{typography.model-code}"
    textColor: "{colors.body}"
  product-card-name:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-edition:
    typography: "{typography.edition-number}"
    textColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    minHeight: 90vh
    layout: full-bleed
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subline:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: 480px
  edition-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.edition-number}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    border: "1px solid {colors.hairline}"
  edition-badge-soldout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.edition-number}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    border: "1px solid {colors.hairline}"
  model-tag:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.model-code}"
    rounded: "{rounded.none}"
    padding: "0"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    rowPadding: "12px 16px"
  spec-table-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  spec-table-value:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  collection-filter:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.model-code}"
    rounded: "{rounded.none}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  collection-filter-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — A stark rectangle of #eeeeee fill on #111111 ground, zero radius, uppercase Aktiv Grotesk at 12px with 2px letter-spacing. The hover state inverts: transparent fill with a matching {colors.ink} border, turning the button into an outline on hover—the brand's single interaction flourish. Disabled state falls to {colors.primary-disabled} fill with {colors.muted} text, communicating unavailability without any softening of geometry.

**`button-secondary`** — Transparent fill, 1px {colors.hairline} border, same uppercase type and flush geometry as primary. Used alongside primary in quantity-select and wishlist contexts; hover sharpens the border to full {colors.ink} intensity with a {colors.surface-soft} background fill.

### Text Input

**`text-input`** — Flush rectangle ({rounded.none}), {colors.surface-soft} fill, 1px {colors.hairline} border. Labels sit above in {typography.model-code} styling—all-caps, wide-tracked—consistent with the brand's preference for uppercase labeling throughout. Focus state tightens the border to full {colors.ink} weight with no glow or shadow. Placeholder text renders in {colors.muted}.

### Navigation

**`nav-bar`** — 64px tall, {colors.canvas} background, 1px {colors.hairline} bottom border. Logo mark sits left; navigation links in {typography.nav-item} (12px uppercase, 1.5px tracking) are clustered right with cart icon. No dropdown mega-menu at any breakpoint; collections navigate via direct links or a full-width off-canvas drawer on mobile.

### Product Card

**`product-card`** — Sharp-cornered ({rounded.none}) cell on {colors.surface-soft}. Square image crop dominates the upper portion. Below: a {typography.model-code} model tag in {colors.body} (e.g. "U1-S"), the full product name in {typography.title-md} in {colors.ink}, then edition status in {typography.edition-number} and {colors.muted}—"12 / 50" or sold-out state. Price is typically deemphasized or revealed only on PDP; scarcity signaling through edition numbers carries more visual weight.

### Hero

**`hero`** — Full-bleed, minimum 90vh, {colors.canvas} or photographic background. Headline in {typography.display-xl} (72px thin, −2px tracking) in {colors.ink}, stacked above a {typography.body-md} descriptor paragraph maxed at 480px wide. CTA button sits {spacing.xl} below. On photographic heroes the headline may overlay the image in {colors.on-dark} with no scrim—confidence in image contrast over legibility safety nets.

### Edition Badge

**`edition-badge`** — Small rectangular chip ({rounded.none}), 1px {colors.hairline} border, {typography.edition-number} in {colors.body}. Appears on both collection grid cards and the PDP to surface print-run size and remaining stock. When inventory reaches zero, the badge switches to {colors.muted} text and renders "SOLD OUT" rather than a fraction.

### Model Tag

**`model-tag`** — Inline text label, no background, no border, no padding. Carries the model reference code (U1-S, U3-D, U5-S) in {typography.model-code}—11px, 600 weight, 2px letter-spacing, uppercase—rendered in {colors.muted}. Functions as the secondary classification system beneath product names across all collection and search views, mapping the brand's own internal taxonomy directly to the UI.

### Spec Table

**`spec-table`** — Two-column definition list on {colors.surface-soft}, no outer radius, 1px {colors.hairline} row dividers. Left column: {typography.caption} labels in {colors.muted} (e.g. "CASE DIAMETER", "WATER RESISTANCE", "MOVEMENT"). Right column: {typography.body-sm} values in {colors.ink}. Sits below the fold on PDPs to communicate technical specifications without competing with imagery above.

### Collection Filter

**`collection-filter`** — A horizontal row of filter chips in {typography.model-code} casing. Inactive: transparent fill, 1px {colors.hairline} border, {colors.body} text. Active: {colors.ink} fill, matching border, {colors.canvas} text—the same inversion logic as the primary button, keeping the interaction vocabulary coherent. Filters map to model series (U1, U3, U5) or material and colorway attributes.

### Footer

**`footer`** — {colors.surface-soft} background, 1px {colors.hairline} top border. {typography.caption} throughout in {colors.muted}. Four columns on desktop: brand info, collections, stockists, legal. Newsletter input uses the inline text-input pattern with an adjacent submit button. Social links rendered as text labels rather than icons only, consistent with the typographic-first identity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero headline drops to {typography.display-lg}; spec table single-column label-above-value stacking |
| Tablet | 744–1128px | Two-column product grid; nav bar retains text links; hero stays full-bleed at display-lg scale |
| Desktop | 1128–1440px | Three-column product grid; full nav exposed; hero headline at full {typography.display-xl} |
| Wide | > 1440px | Grid max-width constrained to ~1280px centered; side margins grow; type scale unchanged |

### Touch Targets

- All interactive buttons minimum 44px tall matching defined component height
- Filter chips expand to 44px touch height on mobile via increased vertical padding
- Nav links inside hamburger drawer minimum 48px row height
- Cart, close, and icon controls minimum 44×44px hit area
- Product card entire surface is tappable, not just title or image

### Collapsing Strategy

- Navigation: full text links → full-width off-canvas drawer; no intermediate hamburger-with-dropdown
- Hero CTA: stacks below headline text on mobile, no horizontal arrangement at any breakpoint
- Spec table: two-column → single-column label-above-value stack below 744px
- Footer: four columns → two columns at tablet → single-column accordion stack on mobile
- Product grid: 3-col → 2-col → 1-col; image fills full card width at all breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list contains a large proportion of WordPress Gutenberg block-editor defaults (#00d084, #0693e3, #7a00df, #34e2e4, #4721fb, #ab1dfe, #faaca8, #dad0ec, #fafae1, #67a671, #fdd79a, #31cdcf, etc.)—these are almost certainly editor UI artifacts, not brand palette entries; actual brand colors are likely confined to the dark neutrals (#111111, #1e1e1e, #313131, #32373c) and possibly #003388
- No meta theme-color extracted, which would have confirmed the intended primary canvas color with certainty
- Whether #003388 is a deliberate brand accent or an incidental link/focus default is unconfirmed; it is retained as primary accent because it is the most distinctive non-neutral in the extracted set
- Aktiv Grotesk is served via Adobe Fonts/Typekit—actual CSS weight values and font-family declarations in production may differ from the extracted stack names
- Price display conventions, sale badge styling, and back-in-stock notification patterns not confirmed from extraction
- Mobile nav drawer animation style, overlay opacity, and item hierarchy not detectable from static analysis
- Custom scroll behavior or cursor treatments common in independent watch micro-brands not detected in extraction
