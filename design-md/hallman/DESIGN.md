---
version: alpha
name: "Hallman"
source_url: "https://www.hallmanindustries.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Gold hardware glints against matte black steel — that single material pairing drives every pixel of Hallman's digital presence the way it drives their physical ranges. The site opens into darkness: a near-black canvas (`{colors.canvas-dark}`) lets full-bleed lifestyle photography of colored ranges command the viewport, then yields to a clean white surface (`{colors.canvas}`) for spec grids and configurator panels. Primary actions carry a warm antiqued gold (`{colors.primary}`, #b8965a) lifted straight from the brass trim on their appliance knobs and handles — not a decorative flourish but a literal product-truth translated into interface. Typography stays authoritative without shouting: a geometric sans-serif in weight 500–700 at generous sizes for display headings, dropped to 400 for body copy, with tight letter-spacing that echoes machined precision. Corners are kept almost perfectly square (`{rounded.xs}` on cards, `{rounded.none}` on hero imagery) because the product language is slabs, edges, cast-iron gratings — softness would contradict what's being sold. Spacing is architectural: `{spacing.section}` gaps between content bands give each range finish its own breathing room, mimicking a showroom floor rather than a catalog page. The product card component pairs a dominant swatch circle with a cropped beauty shot, foregrounding color choice as the primary purchase decision. Navigation is minimal — five or six top-level links in uppercase micro-labels, reinforcing the idea that Hallman's catalog is curated, not sprawling. A sticky configurator bar appears on product pages, holding finish, size, and fuel-type selectors in a single row with the gold CTA anchored right, ensuring the build-your-range flow never scrolls out of reach.

colors:
  primary: "#b8965a"
  primary-active: "#9e7d45"
  primary-disabled: "#d9c9a8"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#717171"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  canvas-dark: "#0d0d0d"
  surface-soft: "#f5f5f3"
  surface-card: "#ffffff"
  surface-dark: "#1c1c1c"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-dark-muted: "#a0a0a0"
  accent-navy: "#1e2d3b"
  accent-red: "#8b2020"
  accent-ivory: "#f4f0e8"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 1px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.8px
    textTransform: uppercase
  price:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.7
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: 2px solid {colors.ink}
  button-secondary-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: 2px solid {colors.on-dark}
  button-configurator:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 40px
    height: 56px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.primary}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline-soft}
  nav-bar-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: none
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    imageAspectRatio: 4:3
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
  hero-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 85vh
    contentMaxWidth: 560px
    overlayGradient: "linear-gradient(to right, rgba(0,0,0,0.7) 0%, transparent 60%)"
  color-swatch:
    rounded: "{rounded.full}"
    size: 36px
    border: 2px solid {colors.hairline}
    selectedBorder: 2px solid {colors.primary}
    spacing: "{spacing.sm}"
  configurator-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    height: 80px
    padding: "{spacing.lg}"
    borderTop: 1px solid {colors.hairline-soft}
    position: sticky
    bottom: 0
    boxShadow: "0 -4px 24px rgba(0,0,0,0.08)"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    rowPadding: "{spacing.base}"
    rowBorder: 1px solid {colors.hairline-soft}
  finish-badge:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  collection-grid:
    columns: 3
    gap: "{spacing.lg}"
    itemRounded: "{rounded.xs}"
    itemBackgroundColor: "{colors.surface-soft}"
  footer:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark-muted}"
    linkColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  announcement-bar:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center

---

## Components

### Buttons

**`button-primary`** — A warm gold rectangle with sharp `{rounded.xs}` corners and uppercase tracking. The gold reads as premium hardware, not generic accent. On hover, darkens to `{colors.primary-active}`; disabled state fades to `{colors.primary-disabled}` with reduced opacity. Used for all conversion-critical actions: "Add to Cart," "Build Your Range," "Request Quote."

**`button-secondary`** — Transparent fill with a 2px ink border, maintaining the same rectangular geometry. On dark backgrounds, switches to white border via `button-secondary-dark`. Used for secondary navigation actions like "View All Finishes" or "Compare Models."

**`button-configurator`** — An oversized variant of button-primary (56px tall) used exclusively in the sticky configurator bar. The extra height and larger type ensure it remains the dominant tap target when surrounded by select dropdowns.

### Navigation

**`nav-bar`** — A 72px white bar with uppercase geometric sans links spaced generously. Transitions to `nav-bar-dark` (solid black, no border) when overlaying hero imagery. Logo sits left, navigation center-aligned, cart/account icons right. On scroll past hero, snaps back to white variant with a subtle bottom hairline.

**`announcement-bar`** — A 40px navy strip above the nav carrying promotional copy (free shipping thresholds, lead times). Text is centered caption-weight, white on dark navy.

### Product Display

**`product-card`** — A quiet card with `{colors.surface-soft}` background, minimal corner rounding, and generous internal padding. The product image dominates at 4:3, with title below in `{typography.title-sm}` and price in bold `{typography.price}`. No border — the background tint separates it from the white canvas. Hover lifts the card with a subtle box-shadow.

**`color-swatch`** — Circular swatches (`{rounded.full}`) representing available range finishes. Selected state gains a gold border matching `{colors.primary}`. Arranged in a horizontal row with `{spacing.sm}` gaps inside product cards and the configurator.

**`configurator-bar`** — A sticky bottom panel that holds finish, size, and fuel-type selectors alongside the primary CTA. White background, top hairline, and soft upward shadow create hierarchy without heaviness. On mobile, collapses to a floating gold button with a slide-up sheet for options.

### Hero & Layout

**`hero-dark`** — Full-viewport dark section with a left-aligned gradient overlay ensuring text legibility over lifestyle photography. Heading in `{typography.display-xl}` white, body copy in `{typography.body-md}` at reduced opacity, single gold CTA below. Content constrained to 560px max-width left column while imagery bleeds right.

**`collection-grid`** — A three-column grid of range categories (Pro, Classico, Bold series). Each cell uses `{colors.surface-soft}` fill with `{rounded.xs}` corners, product image centered, series name below.

### Specs & Details

**`spec-table`** — Alternating-row specification table with uppercase bold labels (BTU output, dimensions, certifications) in `{typography.spec-label}` and values in `{typography.body-sm}`. Rows separated by soft hairlines. No zebra striping — the label weight alone creates scan-ability.

**`finish-badge`** — A compact navy pill labeling special finishes or limited editions. Uppercase caption text on dark background, positioned over product card imagery or inline with configurator options.

### Footer

**`footer`** — Dark canvas matching the hero sections, creating a bookend effect. Muted body text with brighter white link color on hover. Four-column layout: product categories, support, company, and a newsletter signup using `text-input` adapted for dark backgrounds.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero text stacks above image; configurator bar collapses to floating gold CTA with bottom-sheet selectors; nav becomes hamburger menu; collection grid drops to 1 column; spec table becomes stacked label/value pairs |
| Tablet | 744–1128px | Two-column product grid; configurator bar shows all selectors inline; hero maintains overlay but at 70vh; footer collapses to 2 columns |
| Desktop | 1128–1440px | Full three-column grids; sticky configurator bar; nav fully expanded; hero at 85vh with side-by-side text and image |
| Wide | > 1440px | Content max-width capped at 1440px with centered layout; additional whitespace on flanks; hero image scales to cover |

### Touch Targets
- All interactive elements maintain 48px minimum touch height on mobile
- Color swatches expand to 44px on touch devices with increased gap spacing
- Configurator selects use native mobile dropdowns below 744px
- Bottom-sheet modals include a 56px drag handle zone

### Collapsing Strategy
- Navigation links collapse into a full-screen dark overlay menu with stacked links at `{typography.title-md}` size
- Product spec tables reflow from two-column key/value to stacked blocks
- Collection grid items become horizontal scrolling cards on mobile
- Footer columns stack vertically with accordion toggles for each section
- Announcement bar text truncates with ellipsis; swipe for full message on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors could be extracted from the live site — colors above are based on widely-documented Hallman brand identity (gold hardware, dark/light contrast) but have not been verified against current CSS variables
- No font-family stacks were extracted — Montserrat is used as a reasonable geometric sans-serif stand-in based on the brand's visual weight and style; actual webfont may differ
- No meta theme-color found; mobile browser chrome color is unknown
- Platform could not be confirmed (not Shopify); CMS and framework are unidentified, meaning component naming conventions may not align with the actual implementation
- Exact border-radius values, spacing scale, and animation/transition durations could not be measured from extraction
- Dark-mode or alternate theme behavior is unknown — the dark canvas sections may be fixed rather than theme-toggled
- Icon system (line weights, size grid, stroke vs. fill) could not be determined
