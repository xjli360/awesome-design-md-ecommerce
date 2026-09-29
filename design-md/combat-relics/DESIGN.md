---
version: alpha
name: "Combat Relics"
source_url: "https://www.combat-relics.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The page title announces "original historical antiques" and the design hierarchy earns that claim — a parchment-warm canvas (#f1f0ef) conditions the eye for objects that predate the website by eighty years. Combat Relics is a specialist dealer in WWI and WWII militaria: helmets, medals, insignia, field equipment, and documents recovered from European battlefields and private estate collections. Its color system anchors on near-black (#080808, #151414) and a gradient of warm neutrals (#383838, #525150, #767574) that reads as photographic — the palette of archival print, acid-free tissue, and aged steel. The decisive accent is dark crimson (#9c2426), the color of campaign ribbons and regimental dress uniforms, reserved for primary CTAs and price highlights against fields of neutral gray without competing with merchandise photography. Military forest green (#0d4f3d) surfaces as a structural secondary color, referencing field equipment and mid-century olive drab; a softer sage (#4b916d) serves secondary badges and category chips. The olive-gray #5f6360 bridges the two families as a reliable mid-surface. Type mixes classical and utilitarian registers — Times New Roman carries display headings with a document-archive authority, while Open Sans handles body copy and utility labels at 14–16px. Corners stay sharp or barely softened ({rounded.xs} at most on cards), because pill-shaped buttons would feel anachronistic against bullet-struck steel and hand-stamped identity discs. Spacing is generous on product detail pages, giving provenance text and condition notes the room a museum placard earns. Product cards lift with a measured drop shadow on hover, mimicking the physical act of picking up an item to examine it. Several extracted blue values (#116dff through the #acbeff–#d5dfff ramp) are Wix platform UI colors and are excluded from brand tokens.

colors:
  primary: "#9c2426"
  primary-active: "#7a1b1d"
  primary-disabled: "#f4b8b9"
  primary-muted: "#df3336"
  military-green: "#0d4f3d"
  military-green-mid: "#4b916d"
  military-green-light: "#97c693"
  olive: "#5f6360"
  ink: "#080808"
  ink-secondary: "#151414"
  body: "#383838"
  mid: "#525150"
  muted: "#767574"
  muted-soft: "#a8a6a5"
  hairline: "#e0dfdf"
  hairline-soft: "#f1f0ef"
  canvas: "#f1f0ef"
  surface-soft: "#e0dfdf"
  surface-card: "#ffffff"
  surface-dark: "#151414"
  on-primary: "#ffffff"
  on-dark: "#f1f0ef"
  alert: "#ff4040"

typography:
  display-xl:
    fontFamily: "'Times New Roman', Times, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Times New Roman', Times, serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Times New Roman', Times, serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  body-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  label:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  era-tag:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price-display:
    fontFamily: "'Times New Roman', Times, serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  provenance-text:
    fontFamily: "'Times New Roman', Times, serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
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
    padding: "12px 24px"
    height: 44px
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    height: 44px
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.ink}"
    padding: "11px 23px"
    height: 44px
  button-green:
    backgroundColor: "{colors.military-green}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "12px 24px"
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1.5px solid {colors.primary}"
    padding: "10px 14px"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "2px solid {colors.primary}"
  nav-link:
    textColor: "{colors.on-dark}"
    hoverTextColor: "{colors.primary-muted}"
    typography: "{typography.nav-link}"
  category-nav:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    activeTextColor: "{colors.primary}"
    activeBorderBottom: "2px solid {colors.primary}"
    padding: "0 {spacing.lg}"
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    hoverBoxShadow: "0 4px 16px rgba(8,8,8,0.18)"
    imageAspectRatio: "4/3"
    imageBackgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.primary}"
  era-badge:
    backgroundColor: "{colors.military-green}"
    textColor: "{colors.on-dark}"
    typography: "{typography.era-tag}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  country-badge:
    backgroundColor: "{colors.olive}"
    textColor: "{colors.on-dark}"
    typography: "{typography.era-tag}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  condition-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
    borderLeft: "3px solid {colors.primary}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    overlayColor: "rgba(8,8,8,0.55)"
    minHeight: 480px
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    subtitleTextColor: "{colors.muted-soft}"
  provenance-block:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.provenance-text}"
    border: "1px solid {colors.hairline}"
    borderLeft: "4px solid {colors.military-green}"
    padding: "{spacing.lg}"
    rounded: "{rounded.none}"
  price-block:
    typography: "{typography.price-display}"
    textColor: "{colors.primary}"
    strikethroughColor: "{colors.muted}"
    strikethroughTypography: "{typography.body-md}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1.5px solid {colors.primary}"
    rounded: "{rounded.xs}"
    height: 40px
    padding: "0 {spacing.base}"
  detail-section-header:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.hairline}"
    paddingBottom: "{spacing.sm}"
    marginBottom: "{spacing.base}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Dark crimson (#9c2426) fill with white text, 44px tall, {rounded.xs} corners, and {typography.button-md} with 0.5px letter-spacing. Hover deepens to {colors.primary-active} (#7a1b1d) without an animation curve — a direct, non-decorative state change suited to serious commerce. The disabled state fades to the {colors.primary-disabled} blush, keeping the shape readable while communicating unavailability. This button handles "Add to Cart," "Make Offer," and "Contact About This Item."

**`button-secondary`** — Transparent background with a 1.5px {colors.ink} outline, matching height and {typography.button-md}. Used for secondary actions like "Ask a Question" or "Save to Watchlist" alongside a crimson primary. On hover the border shifts to {colors.primary}, pulling attention without filling.

**`button-green`** — Military green (#0d4f3d) fill variant reserved for confirmatory or navigation actions where the green's historical association (field gear, maps, uniforms) reinforces the merchandise context — typically "Browse Category" or "View All German Items."

### Text Input & Search
**`text-input`** — White surface, {rounded.xs} corners, neutral {colors.hairline} border at rest, sharpening to a 1.5px crimson border on focus. Height and padding match the 44px button standard so inline form rows align without adjustment.

**`search-bar`** — A compact 40px variant of the text input intended for the header or above product grids. A magnifying-glass icon sits inside the right edge. Focus state applies the 1.5px crimson border; placeholder text sits in {colors.muted} to keep the dark nav context readable.

### Navigation
**`nav-bar`** — Near-black (#151414) header with a 2px crimson bottom border that marks the brand boundary between header and content, echoing the regimental-stripe vocabulary of the merchandise. Links use {typography.nav-link} in {colors.on-dark}; hover shifts text to {colors.primary-muted} red. The dark header anchors all scroll positions with visual weight.

**`category-nav`** — A secondary navigation stripe on {colors.canvas} directly below the main header, 44px tall. Active categories underline in 2px crimson with {colors.primary} text; inactive labels use {colors.body} gray. Typical categories include era (WWI / WWII), national origin, and item type (Headgear, Medals, Documents, Edged Weapons).

### Product Card
**`product-card`** — White card, 1px {colors.hairline} border, {rounded.xs} corner, no elevation at rest. On hover the card lifts to a `0 4px 16px` shadow — a gesture that reads as physically handling the item. The image area sits on a {colors.surface-soft} background to cushion photography with uneven cropping. Era and country badges overlap the image corner in stacked rows; condition badge sits below the image. Title renders in {typography.title-md} ink; price in {typography.price-display} crimson.

### Badges
**`era-badge`** — Small all-caps {typography.era-tag} chips in military green (#0d4f3d) marking WWI, WWII, or inter-war period. {rounded.xs} corners; no softening.

**`country-badge`** — Same shape and scale as the era badge but in {colors.olive} (#5f6360), distinguishing national origin (German, American, British, French, etc.) from temporal period.

**`condition-badge`** — A left-border accent (3px {colors.primary} crimson) on a {colors.surface-soft} chip, {typography.label} uppercase. Grades run from "Poor" through "Good," "Very Good," "Fine," to "Mint." The vertical crimson stripe gives a quick-scan quality signal without competing with the price.

### Hero Banner
**`hero-banner`** — Full-width dark section with a 55% black overlay over battlefield or collection photography, ensuring {typography.display-xl} (Times New Roman, 36px) reads cleanly over varied image tones. Minimum 480px tall. A single {colors.primary} `button-primary` sits below a two-line headline with an optional subtitle in {colors.muted-soft}. The overlay doubles as a desaturation layer, preventing any one photo from dominating the brand palette.

### Provenance Block
**`provenance-block`** — A left-bordered text panel (4px {colors.military-green} left edge) on warm {colors.canvas}, set in {typography.provenance-text} (Times New Roman, 15px, 1.75 line-height). Used on product detail pages for item history, recovery location, and previous ownership notes. The serif type and open line-height give it a written-document quality distinct from the utility grid around it.

### Detail Section Header
**`detail-section-header`** — {typography.display-sm} (Times New Roman, 20px bold) over a 2px {colors.hairline} bottom rule, spacing items like "Description," "Provenance," "Shipping," and "Similar Items" on the PDP. The serif weight and rule together communicate section hierarchy without decorative dividers.

### Footer
**`footer`** — Near-black (#151414) with a 3px crimson top border echoing the nav-bar's bottom border, bookending every page in brand crimson. Links in {colors.muted-soft} gray lighten to {colors.on-dark} on hover. {typography.body-sm} at generous line-height. Typical columns include category links, policies, about, and contact.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with slide-out drawer on {colors.surface-dark}; hero drops to 320px min-height; provenance block scrolls below the image stack |
| Tablet | 744–1128px | Two-column product grid; category nav converts to horizontal scroll strip; hero at 400px; PDP stacks image above details |
| Desktop | 1128–1440px | Three-column product grid; PDP splits 55/45 image-left details-right; full category nav visible with no overflow |
| Wide | > 1440px | Content caps at 1440px max-width; optional four-column grid; lateral padding expands to {spacing.section} per side |

### Touch Targets
- All buttons minimum 44px height
- Badge tap targets expand to 36px minimum height on mobile via vertical padding
- Nav links in mobile drawer use 48px row height with a 1px {colors.hairline} bottom rule between items
- Condition and era badges on mobile product cards maintain 32px min-height for reliable tap registration

### Collapsing Strategy
- Dark nav-bar collapses to a hamburger icon at < 744px; the 2px crimson bottom border persists on the mobile header
- Category nav converts to a horizontally scrollable chip row at tablet and below; chips maintain {rounded.xs} shape
- Era, country, and condition badges stack vertically beneath the product image on mobile instead of floating over the image corner
- Provenance block moves below product images on mobile and tablet; on desktop it occupies a right-column panel or full-width below the image gallery
- Hero subtitle text is hidden on mobile to preserve headline impact at reduced viewport width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Most extracted blue values (#116dff, #3899ec, #0f2ccf, #2f5dff, #597dff and the #acbeff–#f5f7ff ramp) are Wix platform component colors, not brand design tokens; they were excluded from all token definitions
- `wf_d68200ba897e4768b5e0bb319` is a Wix font bundle hash — the exact typeface inside it could not be determined from extraction; Times New Roman and Open Sans are inferred from the `times new roman` and `open sans` stack entries
- No meta theme-color was set, so the true primary accent color cannot be confirmed via that signal; crimson (#9c2426) is inferred from distinctiveness and category fit
- Logo file, wordmark font, and brand guidelines were not accessible; logo typography treatment and any custom logotype are unknown
- Exact product grid gutter widths, PDP layout breakpoints, and checkout flow styling were not extractable
- Hover transition durations and easing curves were not captured; the card lift shadow is inferred from standard e-commerce UX conventions
- Pricing display conventions (whether sold items show strikethrough, whether currency formatting includes decimals) could not be confirmed
