---
version: alpha
name: "IXXI"
source_url: "https://www.ixxiyourworld.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Each IXXI order arrives not as a single print but as a grid of individually cut rectangular panels that interlock by hand into a wall-scale image — the modular assembly system is the product, and every UI decision flows from that fact. Deep slate-navy (#0f172a) anchors both the primary brand action and the darkest ink on the page, creating a surface that steps back cleanly to let full-bleed photography and curated artwork read at maximum saturation. DM Serif Display pulls display headings into an editorial register — bracketed serifs at low weight read gallery wall, not e-commerce drop-down — while Futura PT handles all transactional copy with geometric discipline: navigation labels, size callouts, and uppercase button text tracked at +0.08em. That two-voice type system — serif editorial above, geometric utility below — carries IXXI's dual identity as art publisher and personalisation tool simultaneously, without either voice overpowering the artwork itself.

  The panel-builder interface is where IXXI diverges structurally from a standard print shop. A configuration canvas maps the user's uploaded photograph across a live grid of rectangular tiles sized in centimetres, with thin `{colors.panel-border}` lines marking every seam so the customer can see exactly how the physical assembly will look before committing. `{rounded.none}` governs the entire builder — flat corners on every tile, every crop thumbnail, every dimension chip — treating the image as an object that runs to the edge with no radius softening the illusion. Product cards in the catalogue maintain the same corner discipline: rectangular crops, Futura PT captions in `{colors.muted}` at 12 px below the image, and a hover state that insets a 2 px `{colors.primary}` border into the frame rather than lifting a shadow.

  Spacing throughout is generous: `{spacing.section}` (64 px) between editorial zones, `{spacing.xl}` (32 px) between product rows, `{spacing.xxl}` vertical padding on hero blocks. The canvas stays white (`{colors.canvas}`) with `{colors.surface-soft}` appearing only in filter sidebars, input fields, and the builder background — every other surface passes maximum contrast to the photography. CTAs use `{rounded.xs}` for the subtlest possible softening that still signals interactivity without compromising the grid-first corner logic that runs through every other touchpoint.

colors:
  primary: "#0f172a"
  primary-active: "#1e293b"
  primary-disabled: "#94a3b8"
  ink: "#0f172a"
  body: "#334155"
  muted: "#64748b"
  hairline: "#e2e8f0"
  hairline-soft: "#f1f5f9"
  canvas: "#ffffff"
  surface-soft: "#f8fafc"
  surface-card: "#ffffff"
  panel-border: "#cbd5e1"
  on-primary: "#ffffff"
  on-muted: "#475569"
  error: "#dc2626"

typography:
  display-xl:
    fontFamily: "'dm-serif-display', 'Adjusted Times New Roman Fallback', Georgia, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'dm-serif-display', 'Adjusted Times New Roman Fallback', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'dm-serif-display', 'Adjusted Times New Roman Fallback', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'futura-pt', 'Adjusted Arial Fallback', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'futura-pt', 'Adjusted Arial Fallback', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.04em
  body-md:
    fontFamily: "'futura-pt', 'Adjusted Arial Fallback', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'futura-pt', 'Adjusted Arial Fallback', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'futura-pt', 'Adjusted Arial Fallback', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  label-caps:
    fontFamily: "'futura-pt', 'Adjusted Arial Fallback', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'futura-pt', 'Adjusted Arial Fallback', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'futura-pt', 'Adjusted Arial Fallback', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.10em
    textTransform: uppercase
  nav-link:
    fontFamily: "'futura-pt', 'Adjusted Arial Fallback', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.06em
  price-display:
    fontFamily: "'futura-pt', 'Adjusted Arial Fallback', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0

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
    padding: "14px 28px"
    height: 48px
    states:
      hover:
        backgroundColor: "{colors.primary-active}"
      disabled:
        backgroundColor: "{colors.primary-disabled}"
        textColor: "{colors.on-primary}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "13px 27px"
    height: 48px
    border: "1px solid {colors.ink}"
    states:
      hover:
        backgroundColor: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "8px 0"
    borderBottom: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.display-sm}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.body-sm}"
    titleColor: "{colors.ink}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    priceTypography: "{typography.title-sm}"
    priceColor: "{colors.ink}"
    padding: "0 0 {spacing.md} 0"
    gap: "{spacing.sm}"
    states:
      hover:
        borderInset: "2px solid {colors.primary}"
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
    layout: "50/50 split, copy left, image right"
    gap: "{spacing.xl}"
  panel-builder-canvas:
    backgroundColor: "{colors.surface-soft}"
    gridLineColor: "{colors.panel-border}"
    gridLineWidth: 1px
    tileBackground: "{colors.canvas}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    dimensionLabelTypography: "{typography.caption}"
    dimensionLabelColor: "{colors.muted}"
  panel-tile:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.panel-border}"
    borderWidth: 1px
    rounded: "{rounded.none}"
    selectedBorderColor: "{colors.primary}"
    selectedBorderWidth: 2px
  size-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
    activeBorderColor: "{colors.primary}"
    activeBorderWidth: 2px
    inactiveBorderColor: "{colors.hairline}"
  photo-upload-zone:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    borderStyle: dashed
    borderWidth: 2px
    rounded: "{rounded.none}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.muted}"
    ctaTypography: "{typography.button-md}"
    ctaColor: "{colors.primary}"
    minHeight: 240px
    padding: "{spacing.xxl}"
  collection-filter:
    backgroundColor: "{colors.canvas}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    activeTypography: "{typography.title-sm}"
    activeColor: "{colors.ink}"
    labelTypography: "{typography.label-caps}"
    labelColor: "{colors.muted}"
    borderRight: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    width: 240px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.primary-disabled}"
    bodyTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-caps}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Full slate-navy (#0f172a) fill with white Futura PT uppercase text tracked at 0.08em, 48 px tall, `{rounded.xs}` corners — four pixels of radius, the minimum that reads as interactive without undermining the grid-corner logic everywhere else. Hover state deepens to `{colors.primary-active}` (#1e293b); disabled swaps in `{colors.primary-disabled}` as the fill while keeping white text opacity at 100 %. The uppercase tracking aligns button copy with the label-caps convention used in filter headings and size chips, so CTA text and UI metadata share the same visual register.

**`button-secondary`** — White fill with a 1 px `{colors.ink}` outline border, matching uppercase type, same 48 px height. Hover lifts the background to `{colors.surface-soft}` rather than darkening the border, keeping focus on the outline as the persistent identifier. Used alongside `button-primary` in split CTA pairs on the hero block and within the panel-builder step flow.

**`button-ghost`** — Transparent fill, bottom-edge underline only (1 px `{colors.ink}`), no box border or radius. Deployed for lower-hierarchy actions such as "View All" at the foot of collection grids and "Learn More" within editorial content blocks. The underline convention reinforces the flat-grid aesthetic while still marking the element as interactive.

### Text Input

**`text-input`** — Zero border-radius, 48 px tall, with a 1 px `{colors.hairline}` border that sharpens to `{colors.primary}` on focus with no animation — a direct state switch matching the panel grid's binary active/inactive logic. Placeholder text in `{colors.muted}` at `{typography.body-md}`. Used across search, email capture, coupon fields, and the dimension entry fields inside the panel builder where width and height are specified in centimetres.

### Navigation

**`nav-bar`** — White background, 64 px tall, with a 1 px `{colors.hairline}` bottom rule. The IXXI wordmark renders in `{typography.display-sm}` DM Serif Display — the serif logo sits inside a geometric navigation rail, creating the same editorial-versus-utility contrast as the hero typography pair. Navigation links use `{typography.nav-link}` Futura PT at weight 500 with 0.06em tracking. Cart, account, and language icons sit right-aligned. Product category flyouts expand as a simple `{colors.surface-card}` panel below the bar — no mega-menu, no illustrated tiles, just a clean list so the nav never competes with product imagery.

### Product Card

**`product-card`** — Zero-radius rectangle, 3:4 image crop that treats photography as the primary object edge to edge. Title in `{typography.body-sm}` and price in `{typography.title-sm}` sit directly below the image with `{spacing.sm}` gap, both left-aligned. On hover, a 2 px `{colors.primary}` border insets inside the image frame — no drop shadow, no background lift — so the hover state is a frame drawn around the art rather than elevation of the card. Sale badges (`badge-sale`) appear top-left in flat navy with white label-caps text; new-arrival badges (`badge-new`) use the light-bordered variant to distinguish priority without introducing a third brand color.

### Hero

**`hero-editorial`** — Full-width 50/50 split: DM Serif Display headline in `{typography.display-xl}` (56 px, weight 400) left-aligned in the copy column, large lifestyle or product photograph filling the right column. `{spacing.section}` (64 px) padding top and bottom on the copy column. A `button-primary` CTA and a `button-ghost` secondary sit below the subhead in `{typography.body-md}`. The right image panel bleeds to the edge of the viewport with no margin, maximising the art's visual weight. On mobile, image stacks above the headline and the copy column goes full-width.

### Panel Builder Canvas

**`panel-builder-canvas`** — The central interactive feature: a `{colors.surface-soft}` background hosting a tiled grid where each `panel-tile` carries a segment of the user's image. `{colors.panel-border}` grid lines mark every seam at 1 px so the assembly logic is legible before purchase. Tile count, total dimensions, and estimated price update in real-time below the canvas in `{typography.caption}` at `{colors.muted}`. `{rounded.none}` governs every element of the builder — tiles, the outer canvas frame, and the control panel — so the builder reads as a drafting tool, not a consumer form. Zoom controls (plus/minus) appear as flat icon buttons at the canvas corner.

### Panel Tile

**`panel-tile`** — Individual rectangular cells within the builder canvas. `{colors.canvas}` background, 1 px `{colors.panel-border}` border, no radius. Selected or active tiles replace the default border with a 2 px `{colors.primary}` inset, marking which segment the user has tapped without lifting the tile out of the grid plane. At small canvas zoom levels the tap target is padded internally to maintain 44 × 44 px minimum interaction area.

### Size Selector

**`size-selector`** — Flat rectangular chips displaying dimension options (e.g. "30 × 40 CM") in `{typography.label-caps}`. Active chip uses a 2 px `{colors.primary}` border; inactive chips fall back to `{colors.hairline}`. No border-radius on either state — the chip shape deliberately rhymes with the panel tile geometry. Groups of chips are arranged horizontally with `{spacing.sm}` gap, wrapping on narrow viewports.

### Photo Upload Zone

**`photo-upload-zone`** — Dashed 2 px `{colors.hairline}` border on a `{colors.surface-soft}` fill, no radius, minimum 240 px tall. Centre-aligned upload icon and `{typography.body-sm}` instruction copy in `{colors.muted}` explain accepted formats and minimum resolution. Below the icon, a `{typography.button-md}` "Upload your photo" text in `{colors.primary}` acts as the primary trigger — clicking anywhere in the zone fires the file picker. Drag-over state replaces the dashed border with a solid 2 px `{colors.primary}` outline and lightens the fill to `{colors.hairline-soft}`.

### Collection Filter

**`collection-filter`** — A 240 px left sidebar with a 1 px `{colors.hairline}` right border. Section headings (Colour, Style, Format) in `{typography.label-caps}` at `{colors.muted}` separate filter groups. Individual options in `{typography.body-sm}` at `{colors.body}` switch to `{typography.title-sm}` weight when selected — the weight change signals active state without introducing a check-mark glyph or colour swatch, keeping the sidebar visually quiet. At tablet width the sidebar compresses to a horizontal chip rail above the product grid; at mobile it becomes a bottom-sheet triggered by a "Filter & Sort" button.

### Badges

**`badge-sale`** — Flat `{colors.primary}` fill, `{colors.on-primary}` text, `{typography.label-caps}`, zero radius, 4 px × 8 px padding. Sits top-left of product card images. **`badge-new`** — `{colors.surface-soft}` fill with a 1 px `{colors.hairline}` border and `{colors.body}` text using the same label-caps type; the lighter treatment avoids equal-weight competition with sale urgency. Both badges use no radius to maintain grid fidelity.

### Footer

**`footer`** — Full slate-navy (`{colors.primary}`) background, white body text in `{typography.body-sm}`, column headings in `{typography.label-caps}` tracking at 0.12em. Link text uses `{colors.primary-disabled}` (#94a3b8) — the lightened slate reads clearly against the dark fill without needing a contrasting accent hue. Newsletter email field inverts the standard `text-input`: white border on the dark ground, placeholder in `{colors.primary-disabled}`. `{spacing.section}` top and bottom padding gives the footer the same vertical breath as the hero.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero image stacks above headline; panel builder collapses to full-width canvas with sticky bottom control bar; nav collapses to hamburger; filter sidebar becomes bottom-sheet drawer; product grid is 1 column |
| Tablet | 744–1128px | Two-column product grid; hero becomes 60/40 copy-left split; panel builder shows canvas above controls in a stacked panel; collection filter shows as horizontal chip rail above grid |
| Desktop | 1128–1440px | Three-column product grid; hero is 50/50 split; panel builder is side-by-side (canvas left, dimension controls right); filter sidebar always-visible at 240px wide; nav links fully expanded |
| Wide | > 1440px | Four-column product grid; hero content max-width capped at 1440px and centred; panel builder canvas expands to fill available width; footer columns expand to five |

### Touch Targets
- All buttons and inputs maintain 48 px minimum height
- Panel tiles padded internally to 44 × 44 px tap target regardless of canvas zoom level
- Size selector chips minimum 44 px tall on mobile
- Nav hamburger icon has 48 × 48 px tap region including invisible padding
- Photo upload zone full area is tappable (no small hit-target sub-element)

### Collapsing Strategy
- Panel builder: canvas scales proportionally via CSS transform; dimension controls collapse to a sticky bottom bar at mobile with up-arrow expand affordance
- Collection filter collapses to a single "Filter & Sort" `button-secondary` at < 744px; tapping opens a full-screen bottom-sheet overlay
- Product grid: 4 → 3 → 2 → 1 columns across Wide → Desktop → Tablet → Mobile
- Hero headline scales: `{typography.display-xl}` (56 px) at Desktop/Wide → `{typography.display-md}` (36 px) at Tablet → `{typography.display-sm}` (24 px) at Mobile
- Footer: five-column grid collapses to two columns on Tablet, single accordion on Mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex value (#0f172a) was successfully extracted from the live site; the full palette — including accent colors, hover states, promotional colors, and any warm or illustrative tones used in editorial content — is inferred from the dark-slate anchor and standard print-shop conventions
- It is unknown whether IXXI uses any brand accent color (warm tone, highlight, or category-family color) beyond the slate-navy and neutral system defined here
- futura-pt and dm-serif-display are confirmed as loaded typefaces but specific weight variant counts, optical sizes in use, and whether an italic cut of dm-serif-display is deployed could not be verified
- Button and chip border-radius values are inferred from the grid/modular-panel aesthetic; `{rounded.xs}` may be `{rounded.none}` throughout if the brand is fully corner-strict
- Mobile navigation pattern (hamburger flyout vs. bottom tab bar) and whether a search overlay or inline search is used could not be confirmed
- Dark-mode or high-contrast variant, if any, was not detectable from extraction
- Exact panel-builder interaction details — zoom gesture support, drag-to-reposition, per-tile brightness/contrast controls — are assumed from category conventions and not verified from extraction data
