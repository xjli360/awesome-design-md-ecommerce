---
version: alpha
name: "Tom Anderson"
source_url: "https://www.andersonguitars.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Anderson Guitarworks photographs its instruments against near-black (#040404) studio voids, a choice that makes each guitar's grain and finish the only light source on the page. The palette runs on two axes: a cold midnight navy (#112233) holds navigation and structural anchors while a thinly deployed guitar-lacquer red (#cc3b3b, intensified to #bd0000 on active states) fires only at the sharpest moments — a CTA fill, a sale badge, an image-viewer selection ring. The surrounding field is almost exclusively neutral — #aaaaaa on dark surfaces, #eeeeee on light — keeping all spectral attention on instrument photography. Custom display work uses Clarkson for headlines, a serif-adjacent display face that carries old-world luthier weight without period-room stiffness; Josefin Sans handles mid-weight subheads and navigation where geometric regularity fits technical specs and model names; Oswald covers uppercase labels, badges, and specification tables where compressed condensed weight reads at a glance. Body copy runs Arial/Helvetica Neue — utility-grade, intentionally invisible. Corner radii are kept minimal throughout: product cards use {rounded.none}, CTAs are equally sharp, reinforcing the precision-machined quality claim. Spacing is generous in hero sections — full {spacing.section} gaps before spec blocks — compressing to tight {spacing.md} and {spacing.sm} grids inside model comparison tables. The site reads less like retail and more like a catalog issued by a workshop: every layout decision defers to the guitar.

colors:
  primary: "#112233"
  primary-active: "#112255"
  primary-disabled: "#aaaaaa"
  accent: "#cc3b3b"
  accent-deep: "#bd0000"
  accent-muted: "#e99292"
  ink: "#111111"
  body: "#272727"
  muted: "#aaaaaa"
  hairline: "#e1e1e1"
  hairline-dark: "#3e3e3e"
  canvas: "#fafafa"
  surface-soft: "#f5f5f5"
  surface-card: "#f7f7f7"
  surface-dark: "#1e1e1e"
  surface-hero: "#040404"
  on-primary: "#f5f5f5"
  on-dark: "#eeeeee"

typography:
  display-xl:
    fontFamily: "'Clarkson', 'Josefin Sans', Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1px
  display-md:
    fontFamily: "'Clarkson', 'Josefin Sans', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Josefin Sans', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  title-md:
    fontFamily: "'Josefin Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  title-sm:
    fontFamily: "'Josefin Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  label-caps:
    fontFamily: "'Oswald', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Oswald', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'Oswald', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  body-md:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Josefin Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Josefin Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Josefin Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1px
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
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.accent-deep}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.on-dark}"
    padding: 13px 27px
    height: 48px
  button-secondary-light:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: none
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1px solid {colors.primary}"
  text-input-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-dark}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1px solid {colors.accent}"
  nav-bar:
    backgroundColor: "{colors.surface-hero}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-dark}"
    logoColor: "{colors.on-dark}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
    hoverBorder: "1px solid {colors.primary}"
  hero-section:
    backgroundColor: "{colors.surface-hero}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    paddingY: "{spacing.section}"
    overlayColor: "rgba(4,4,4,0.55)"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    headerBackgroundColor: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.label-caps}"
    cellTypography: "{typography.spec-label}"
    cellTextColor: "{colors.body}"
    rowAltBackground: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
  model-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  finish-swatch:
    size: 32px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selectedBorder: "2px solid {colors.primary}"
    hoverBorder: "2px solid {colors.muted}"
  configurator-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    sectionLabelTypography: "{typography.label-caps}"
    optionTypography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
  guitar-image-viewer:
    backgroundColor: "{colors.surface-hero}"
    thumbnailBorder: "1px solid {colors.hairline-dark}"
    thumbnailSelectedBorder: "2px solid {colors.accent}"
    rounded: "{rounded.none}"
  search-overlay:
    backgroundColor: "{colors.surface-hero}"
    textColor: "{colors.on-dark}"
    inputBackgroundColor: "{colors.surface-dark}"
    inputTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-dark}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.label-caps}"
    borderTop: "1px solid {colors.hairline-dark}"
    paddingY: "{spacing.section}"

## Components

### Buttons
**`button-primary`** — Sharp-cornered (`{rounded.none}`) CTAs in guitar-lacquer red (`{colors.accent}`, #cc3b3b) that read against both dark hero canvases and light spec pages. Uppercase Josefin Sans (`{typography.button-md}`, 1.5px letter-spacing) reinforces the machined-tool aesthetic; hover state deepens to `{colors.accent-deep}` (#bd0000). Disabled state mutes to `{colors.primary-disabled}` (#aaaaaa) at full opacity.

**`button-secondary`** — Outline-only, no fill; 1px border and text inherit the surface's text color — `{colors.on-dark}` on dark backgrounds, `{colors.ink}` via `button-secondary-light` on light pages. Same uppercase Josefin Sans typography and zero radius as primary, making the two visually twinned and differentiated only by fill versus outline.

**`button-ghost`** — Text-only in accent red (`{colors.accent}`) with no border or padding, used inside configurator panels and spec tables for secondary actions like "View Full Specs" or "Compare Models."

### Navigation
**`nav-bar`** — Full-width near-black (`{colors.surface-hero}`, #040404) bar, 72px tall with a `{colors.hairline-dark}` bottom edge, nearly invisible against dark hero photography. Links use `{typography.nav-link}` — 14px Josefin Sans, 1px letter-spacing, uppercase. Logo reverses to `{colors.on-dark}`. No blur, no translucency; fully opaque black at all scroll positions.

### Product Card
**`product-card`** — Zero-radius card on `{colors.surface-card}` (#f7f7f7) with a thin `{colors.hairline}` border that sharpens to `{colors.primary}` navy on hover, surfacing the brand color only at interaction. Title in `{typography.title-md}` (Josefin Sans 600); price in `{typography.price-display}` (Oswald 28px). The 4:3 image frame shows guitars straight-on or slightly angled against near-black studio backgrounds, directly importing the hero palette into the grid.

### Hero Section
**`hero-section`** — Near-black (`{colors.surface-hero}`, #040404) full-bleed panels with guitar photography behind a dark scrim. Headline in `{typography.display-xl}` (Clarkson 700, 56px, −1px tracking); subhead in `{typography.display-sm}` (Josefin Sans 600, 24px). Vertical padding uses `{spacing.section}` on both axes. CTA buttons sit below the subhead in a horizontal stack: primary in `{colors.accent}`, secondary as outline white.

### Spec Table
**`spec-table`** — Multi-column table on `{colors.surface-soft}` with a `{colors.primary}` (#112233) navy header row reversing text in `{typography.label-caps}` (Oswald uppercase, 12px, 1.5px tracking). Data cells use `{typography.spec-label}` (Oswald 13px, `{colors.body}`). Alternating rows fall on `{colors.canvas}` for readability across long specification lists — scale length, nut width, fret count, pickup configuration, and finish.

### Model Badge
**`model-badge`** — Flat red (`{colors.accent}`) rectangle at `{rounded.none}` placed over product listing card images to flag limited editions, new models, or custom-shop pieces. Typography in `{typography.label-caps}` — Oswald uppercase. No drop shadow; the red block reads as a physical label, not a UI affordance.

### Finish Swatch
**`finish-swatch`** — 32px circular swatches (`{rounded.full}`) for selecting guitar finish on configurator and product detail pages. Transparent border at rest; `{colors.muted}` ring on hover; 2px `{colors.primary}` (#112233) navy ring on selected state, which separates cleanly from any finish color.

### Configurator Panel
**`configurator-panel`** — Light background (`{colors.surface-soft}`) panel with section labels in `{typography.label-caps}` and options in `{typography.title-sm}` (Josefin Sans 600, 14px). `{rounded.none}` throughout, `{spacing.xl}` internal padding, `{colors.hairline}`-bordered. Finish swatches, pickup selectors, and hardware options stack vertically with `{spacing.lg}` between groups.

### Guitar Image Viewer
**`guitar-image-viewer`** — Near-black (`{colors.surface-hero}`) main image frame with a thumbnail strip below. Thumbnails carry a `{colors.hairline-dark}` default border; the selected thumbnail activates a 2px `{colors.accent}` red border. Zero radius on both main frame and thumbnails — the entire viewer reads as a precision inspection window.

### Search Overlay
**`search-overlay`** — Full-screen near-black layer (`{colors.surface-hero}`) with a centered input on `{colors.surface-dark}` background. Input text in `{typography.body-md}`, `{colors.hairline-dark}` border, no radius. Results surface as product cards on the dark ground.

### Footer
**`footer`** — Dark surface (`{colors.surface-dark}`, #1e1e1e) with `{colors.hairline-dark}` top border. Section labels in `{typography.label-caps}` (Oswald uppercase, `{colors.on-dark}`); links in `{typography.body-sm}` at `{colors.muted}` (#aaaaaa), hovering to `{colors.on-dark}`. Vertical padding at `{spacing.section}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero headline drops to `display-md` (Clarkson 36px); configurator panel moves below guitar image viewer; spec table scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; nav shows abbreviated model category labels; configurator panel slides up as a bottom drawer; hero at `display-xl` with reduced side padding |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdown model categories; configurator panel docks right alongside the guitar image viewer; hero full-width at `{spacing.section}` padding |
| Wide | > 1440px | Content column max-width ~1400px centered; dark side rails frame the column; hero photography scales to fill with controlled crop anchors |

### Touch Targets
- All buttons minimum 48px height
- Finish swatches 40px effective tap area (32px visual + 4px padding ring)
- Nav hamburger icon minimum 44×44px
- Product cards fully tappable with no dead zones inside the card boundary
- Configurator option rows minimum 44px height with full-row tap area

### Collapsing Strategy
- Desktop three-column product grid → Tablet two-column → Mobile one-column
- Desktop side-by-side configurator (image left, panel right) → Mobile stacked (image top, panel below)
- Desktop full nav with dropdowns → Tablet abbreviated category nav → Mobile off-canvas drawer
- Spec tables add horizontal scroll on Mobile rather than reflowing, to avoid data truncation
- Footer four-column link grid collapses to single-column accordion on Mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color set; whether nav uses a CSS variable or hard-coded #040404 is unconfirmed
- Clarkson is a custom or licensed display face — weight variants and optical sizes not fully verified from extraction
- Exact nav height (72px used here) not captured; may shift when a promotional announcement banner is present
- No confirmed grid gutter values or max content-width breakpoint
- Hover and focus-ring color for interactive elements not extracted — `{colors.primary}` navy assumed from brand hue
- Animation easing curves and transition durations not available from extraction
- Custom font loading method for Clarkson (self-hosted vs. Typekit/Adobe Fonts) not confirmed
- Exact Josefin Sans and Oswald weight subsets loaded per context not fully mapped
- No pricing or cart UI color data captured — accent red assumed for add-to-cart from CTA convention
