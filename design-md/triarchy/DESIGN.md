---
version: alpha
name: "Triarchy"
source_url: "https://triarchy.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Triarchy runs #108474 — a deep, almost medicinal teal — as its lone chromatic anchor in an otherwise near-achromatic field: near-black ink at #121212, warm off-whites at #f9fafb and #fafafa, and a graduated stack of neutral grays (#eeeeee, #dedede, #e9e9e9) that carry every hairline and surface. The teal choice is precise — it straddles ocean and earth without defaulting to the clichéd forest green of generic eco-branding — and pairs with a dark forest olive (#30402d) for editorial panels and product-context moments where sustainability messaging needs more ground. A chrome yellow (#fbcd0a) fires as a rare spike: sale badges, notification dots, the one place urgency is permitted to interrupt the restrained palette.

  Typography is an unusually ambitious three-family system for a DTC denim brand. Baskerville handles display headlines — its serifs borrow fashion-editorial credibility, positioning garment craft within a heritage register that denim-as-luxury demands. Nunito Sans runs body copy and navigation at 14–16px; its slightly rounded terminals soften what would otherwise be a severe achromatic palette without softening the brand voice. Poppins takes button labels and UI controls, its geometric neutrality keeping brand type from bleeding into functional type. Each family has a clear register with no overlap.

  Surfaces are cool and pale — the canvas reads #f9fafb rather than pure white, keeping product photography from fighting a glaring ground. Hairlines (#eeeeee, #dedede) are frequent and light; card backgrounds lift only slightly from the canvas. Corner radii are deliberately minimal: no pill shapes, no playful rounding anywhere outside filter chips. Primary buttons sit at a flat 4px radius; product cards read as near-flat rectangles. The overall impression is stripped and garment-industry adjacent — tactility lives in the photography and material storytelling, not in decorative UI chrome. Full-bleed editorial imagery with Baskerville reversed white over dark scrim panels alternates with pale PDP surfaces engineered for maximum legibility at checkout.

colors:
  primary: "#108474"
  primary-active: "#0c6b5e"
  primary-disabled: "#a0d4cc"
  accent-yellow: "#fbcd0a"
  accent-red: "#f5383e"
  forest: "#30402d"
  ink: "#121212"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#acacac"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  hairline-strong: "#bbbbbb"
  canvas: "#f9fafb"
  canvas-alt: "#fafafa"
  surface-soft: "#f2f2f2"
  surface-card: "#e9e9e9"
  surface-muted: "#f9f9f9"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "Baskerville, 'Baskerville Old Face', 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Baskerville, 'Baskerville Old Face', 'Times New Roman', serif"
    fontSize: 38px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Baskerville, 'Baskerville Old Face', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.30
    letterSpacing: 1.2px
    textTransform: uppercase
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-uppercase:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "Poppins, 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "Poppins, 'Nunito Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  price-display:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0

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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoAlignment: center
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas-alt}"
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    height: 40px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.sm}"
    hoverEffect: image-swap
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  sustainability-tag:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: 3px 10px
  hero-banner:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 80vh
    contentAlignment: center
    overlayOpacity: 0.35
    ctaComponent: button-primary
  editorial-panel:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  size-selector:
    defaultBackground: "{colors.canvas}"
    defaultBorder: "1px solid {colors.hairline}"
    defaultTextColor: "{colors.ink}"
    selectedBackground: "{colors.ink}"
    selectedTextColor: "{colors.on-dark}"
    unavailableTextColor: "{colors.muted-soft}"
    unavailableDecoration: line-through
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    size: 44px
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.ink}"
    defaultBorder: "1px solid {colors.hairline}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    selectedBackground: "{colors.ink}"
    selectedTextColor: "{colors.on-dark}"
    padding: 8px 16px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.hairline-strong}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Filled teal (#108474) with white uppercase Poppins labels at 14px / 0.8px tracking. Height is 48px with 28px horizontal padding and a flat 4px radius — no pill, no playful curvature. Hover darkens to `{colors.primary-active}` (#0c6b5e); disabled state fades to `{colors.primary-disabled}`. The uppercase tracking gives CTAs fashion-label weight without requiring heavy type.

**`button-secondary`** — Transparent fill with a 1px #121212 border and ink-colored uppercase label. Identical height and geometry to primary so the pair stacks or sits side-by-side without visual imbalance. Used for secondary purchase actions and "learn more" moments alongside a filled primary.

**`button-ghost`** — Transparent with a 1px `{colors.primary}` teal border and teal label. Appears on sustainability-adjacent CTAs — material-sourcing callouts, recycling program links — where teal brand signal is appropriate but a filled button would overstate urgency.

### Navigation
**`nav-bar`** — 64px tall, canvas (#f9fafb) ground, centered wordmark, hairline-soft bottom separator. Navigation links in Nunito Sans 14px/600 with 0.3px tracking. On scroll, background transitions to `{colors.canvas-alt}` (#fafafa). The announcement bar always sits above the nav in primary teal with reversed white uppercase copy — typically a sustainability certification callout or free-shipping threshold.

**`announcement-bar`** — Primary teal (#108474) ground, white label-uppercase Nunito Sans, 40px fixed height. Rotates between sustainability certifications (B Corp, WRAP, water-savings data) and promotional shipping thresholds.

### Product Card
**`product-card`** — Near-flat rectangle, no border-radius. A 3:4 portrait image dominates; hovering swaps to a secondary lifestyle or texture shot. Title in Nunito Sans 600 at 16px below the image; price in price-display scale. `{colors.accent-yellow}` (#fbcd0a) SALE badges sit top-left; teal sustainability tags sit top-right when applicable. No card shadow — spacing handles depth. The card reads as a clean garment hang-tag analogue.

**`product-card-badge`** — Chrome yellow (#fbcd0a) fill with #121212 ink text, 2px radius, uppercase 11px Nunito Sans at 1.2px tracking. Keeps promotional urgency legible without colliding with the teal primary.

**`sustainability-tag`** — Primary teal fill, white label-uppercase caption. Applied to products meeting Triarchy's environmental criteria — specific water-saving figures, recycled fiber content. Sits top-right corner of product imagery as a stamp rather than a ribbon.

### Hero
**`hero-banner`** — Full-bleed, minimum 80vh, dark scrim at 35% opacity over brand photography. Display headline in Baskerville at 52px/400 weight centered over the image — the low weight at that scale creates editorial calm rather than urgency. A single `button-primary` CTA sits below the headline. The near-black (#121212) scrim makes the reversed white type work across any photography without per-image adjustment.

**`editorial-panel`** — Dark forest green (#30402d) fill used in full-width editorial sections between collection grids. Baskerville display-md (28px/400) headline over Nunito Sans body-sm body copy, both reversed white. No border-radius. Typically paired with a half-panel product photograph or a close-up fabric detail crop.

### Size & Color Selectors
**`size-selector`** — 44×44px square tiles, no border-radius, 1px hairline border in default state. Selected tiles flip to filled #121212 with white text. Unavailable sizes render the label in muted-soft (#acacac) with line-through decoration — no diagonal overlay graphic. Stacks inline on PDP, collapses to a `<select>` dropdown below 400px viewport width.

**`color-swatch`** — 24px circle, 1px hairline default border, 2px ink border when selected. A tooltip surfaces the colorway name on hover. Arranged in a horizontal row below size tiles on the PDP.

### Filtering
**`filter-chip`** — Pill-shaped (`{rounded.full}`) with a 1px hairline border and Nunito Sans body-sm label. Selected state inverts to filled #121212 with white text. Scrolls horizontally across the top of collection pages on all viewports. The pill is the one exception to the brand's corner-averse geometry — it signals selectability distinctly from the flat button and card shapes surrounding it.

### Forms
**`text-input`** — Canvas fill (#f9fafb), 1px hairline border, 4px radius, 48px height matching button height. Focus border upgrades to 1px primary teal (#108474). Placeholder text in muted (#7b7b7b). Used in newsletter capture, site search, and all checkout fields. Pairs with `button-primary` as a search-bar unit in the nav drawer.

### Footer
**`footer`** — Near-black (#121212) fill. Column headings in title-sm (uppercase Nunito Sans 11px, 1.2px tracking). Body links in hairline-soft (#eeeeee) body-sm. Typically four columns: Shop, Responsibility, About, Account. Collapses into tap-to-expand accordions on mobile with the same ink fill and reversed white type.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; size selector collapses to `<select>` dropdown; nav collapses to hamburger drawer; hero headline drops to display-lg (38px); filter chips scroll horizontally; footer columns become accordions |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links only, no mega-menu; hero maintains full-bleed 80vh; PDP shifts to 50/50 image–details split |
| Desktop | 1128–1440px | Three-column product grid; full nav with category dropdowns; editorial panels use 60/40 or 50/50 splits; PDP shows sticky details panel right of image carousel |
| Wide | > 1440px | Four-column product grid; hero headline upgrades to display-xl (52px); content width caps at 1440px with symmetric side padding; editorial panels constrained to max-width container |

### Touch Targets
- All interactive elements minimum 44×44px on mobile viewports
- Size selector tiles expand to 48px touch target on mobile
- Filter chips maintain 40px minimum height in horizontal scroll container
- Nav drawer links rendered at 56px row height for comfortable tap
- Color swatches expand to 32px diameter on touch viewports

### Collapsing Strategy
- Primary nav collapses to hamburger at < 744px; announcement bar remains above the hamburger header at all breakpoints
- Footer accordion activates below 744px; each column heading is a tap-to-expand section with chevron indicator
- Size selector degrades to a native `<select>` element below 400px viewport width
- Filter chips transition from a horizontal scroll row to a slide-in left drawer on mobile
- Breadcrumbs truncate to Home > [current page] on mobile, suppressing intermediate category levels

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.
- No custom brand typeface confirmed; Baskerville may be used as a web-safe approximation of a licensed editorial serif loaded via Shopify theme assets not captured in static extraction
- Poppins presence may be partially or wholly from third-party review widget injections (JudgeMe) rather than core brand UI — verify button typography against live DOM computed styles
- No explicit dark-mode palette detected; dark (#121212) surfaces in hero and footer are editorial choices, not a system dark theme token set
- Interaction easing curves, transition durations, and hover animation timing not extractable from static hints — 200ms ease-out assumed throughout
- Icon set style (stroke weight, corner treatment, glyph library) not captured; likely a custom SVG set or thin-weight stroke library
- Exact column-count and gutter-width values per breakpoint unconfirmed from extraction
- Navigation dropdown architecture (mega-menu with imagery vs. simple flyout) unconfirmed
- Specific Baskerville weight and style variants (italic usage, bold availability) not confirmed from extraction
