---
version: alpha
name: "PRS Guitars"
source_url: "https://www.prsguitars.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Figured maple grain — quilted, flamed, or simply straight — runs through every visual decision PRS Guitars makes: product photography occupies most of the canvas at large viewport widths, letting wood figure and candy finishes (Aquableux, Faded Whale Blue, Trampas Green) carry the brand's color story rather than UI chrome. The design system lives in dark charcoal space, with #313131 establishing the dominant surface register across nav, footer, and page fills. Against that ground, warm gold (#c9a84c) functions as the single activation signal — appearing on primary CTAs, hover states, and the thin rule that separates guitar series sections. Typography runs almost entirely in system-stack sans-serif at modest weight, trusting the photography to carry visual interest; headlines lean into negative letterSpacing at large sizes for compressed elegance, while spec tables and series labels use uppercase tracking to organize dense product data. PRS operates four product tiers — SE (offshore, entry), S2 (domestic budget), USA Core, and Private Stock (bespoke, 4–6 week build) — and the design differentiates them with badge hierarchy: Private Stock receives charcoal-fill with gold text, a deliberate inversion that signals the tier sits outside ordinary hierarchy. The fretboard bird inlay, rendered in photography across product cards and guitar-detail pages, is the brand's most recognizable recurring visual element — reproduced in abalone, mother-of-pearl, and wood inlay finishes. Finish-swatch carousels replace traditional color pickers: circular swatches (~40px) arranged horizontally beneath a product photo let shoppers preview finish options, each swatch carrying an active ring in {colors.primary} rather than a checkbox. Corner radii throughout are minimal-to-zero ({rounded.none} on most interactive elements), reinforcing the precision-manufacturing associations of a brand whose tolerances are measured in thousandths of an inch. Padding is generous at wide viewports, condensing to a single-column guitar grid at mobile.

colors:
  primary: "#c9a84c"
  primary-active: "#a8883a"
  primary-disabled: "#5c4e23"
  ink: "#f0ece4"
  body: "#c4bdb5"
  muted: "#7a7268"
  hairline: "#383432"
  canvas: "#0f0e0d"
  surface-soft: "#1a1918"
  surface-card: "#222120"
  charcoal: "#313131"
  on-primary: "#0a0a09"
  on-dark: "#f0ece4"
  overlay: "#000000"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.05
    letterSpacing: -1px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0
  series-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.15em
    textTransform: uppercase
  price-display:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 11px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 11px 31px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/3"
    imageFit: cover
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
    seriesBadgePosition: top-left
  hero-fullbleed:
    backgroundColor: "{colors.canvas}"
    minHeight: "90vh"
    overlayColor: "rgba(0,0,0,0.45)"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.body}"
    textAlign: left
    padding: "0 {spacing.xxl}"
  series-badge:
    se:
      backgroundColor: "{colors.surface-card}"
      textColor: "{colors.body}"
    s2:
      backgroundColor: "{colors.charcoal}"
      textColor: "{colors.ink}"
    usa:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
    private-stock:
      backgroundColor: "{colors.charcoal}"
      textColor: "{colors.primary}"
    typography: "{typography.series-label}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  finish-swatch:
    size: 40px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
    activeBorder: "2px solid {colors.primary}"
    activeScale: 1.1
    gap: "{spacing.sm}"
    tooltipTypography: "{typography.caption}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    alternateRowBackground: "{colors.canvas}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.body}"
    rowBorder: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.base}"
  model-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 8px 16px
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "#0a0a09"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.primary}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"
    logoColor: "{colors.primary}"

## Components

### Buttons

**`button-primary`** — Gold (#c9a84c) fill on a sharp-cornered rectangle with all-caps type tracking at 0.08em. At rest the label is near-black on gold; `:hover` deepens to `primary-active` (#a8883a); `:disabled` drops to a near-invisible charcoal fill with `{colors.muted}` label. Used exclusively for primary purchase, "Add to Cart," and configurator submission actions — never for nav or filters.

**`button-secondary`** — Transparent fill with a 1px gold border and gold label text. Mirrors primary dimensions but visually recedes behind product photography; used for "Learn More," "Compare Models," and artist-page secondary CTAs.

**`button-ghost`** — Transparent fill with a 1px `{colors.hairline}` border and `{colors.ink}` label. Functions as a tertiary action within spec sidebars, configuration panels, and filter drawers where gold would compete with the photography.

### Navigation

**`nav-bar`** — Fixed to the top at 72px, filled with `{colors.canvas}` (near-black), separated from page content by a 1px `{colors.hairline}` border. The PRS wordmark at left renders in `{colors.primary}` gold. Category links (Guitars, Amps, Effects, Accessories, Artists) run in `{typography.nav-link}` — 14px weight 500. Search and cart icons anchor the right edge at 44×44px touch targets. On mobile, all categories collapse to a hamburger drawer that slides in from the left at full height.

### Product Cards

**`product-card`** — Dark rectangle (`{colors.surface-card}`) with a 4:3 image well covering the full card width. Guitar model name in `{typography.title-md}`, MSRP in `{typography.price-display}` (serif 24px, weight 400) below. A `series-badge` chip overlays the top-left corner of the image. The card border is 1px `{colors.hairline}` at rest; on hover it transitions to 1px `{colors.primary}` with no elevation change — the brand avoids shadows in favor of border-color state changes. A `finish-swatch` row appears beneath the price when multiple finishes exist.

### Hero

**`hero-fullbleed`** — Full-bleed guitar photography with a ~45% dark overlay (`rgba(0,0,0,0.45)`), minimum 90vh. Headline in `{typography.display-xl}` (56px, weight 300 serif, letterSpacing −1px) sits lower-left; body copy in `{typography.body-md}` rendered in `{colors.body}`. A `button-primary` CTA anchors the bottom-left cluster. On mobile, image pans to center and the headline scales to approximately 32px with the CTA stacked below.

### Series Badges

**`series-badge`** — Small all-caps chips (`{typography.series-label}`: 10px, weight 700, letterSpacing 0.15em) overlaid at the top-left of product card images. SE uses `{colors.surface-card}` fill with `{colors.body}` text — visually quiet, signaling the entry point. S2 uses `{colors.charcoal}` (#313131) with `{colors.ink}`. USA Core inverts to `{colors.primary}` gold fill with dark text, marking the domestic-made threshold. Private Stock uses `{colors.charcoal}` fill with `{colors.primary}` gold text — a deliberate reversal that distinguishes the ultra-premium tier from the gold-filled USA badge rather than escalating it.

### Finish Swatches

**`finish-swatch`** — 40px circular swatches arranged horizontally at `{spacing.sm}` gaps beneath a product photo. Inactive swatches carry a 2px `{colors.hairline}` ring; the active swatch upgrades to a 2px `{colors.primary}` ring and scales 10%. For figured and burst finishes, the swatch renders a cropped photograph of the actual top wood rather than a flat color. A `{typography.caption}` tooltip displays the finish name on hover or long-press.

### Spec Table

**`spec-table`** — Two-column alternating-row table for individual model pages. Left column: spec label in `{typography.spec-label}` rendered in `{colors.muted}`. Right column: spec value in `{typography.body-sm}` in `{colors.body}`. Rows alternate between `{colors.surface-soft}` and `{colors.canvas}` for scanability across long spec lists (body wood, neck profile, scale length, fret count, nut width, pickup type, controls, hardware finish). Row padding is `{spacing.md}` vertical by `{spacing.base}` horizontal.

### Model Selector

**`model-selector`** — A compact horizontal strip of sibling model names (e.g., Custom 24 / Custom 22 / Custom 24-08) at the top of series landing pages. Each segment is a borderless rectangle with a 1px `{colors.hairline}` outline; the active segment fills with `{colors.primary}` and labels in `{colors.on-primary}`. Selection routes the page to the chosen model without a full reload. On mobile, the strip scrolls horizontally when segments overflow.

### Footer

**`footer`** — Near-black (#0a0a09) background with four link columns (Guitars, Support, Artists, Company) in `{typography.body-sm}` / `{colors.muted}`. Link hover promotes color to `{colors.primary}` with no underline. A gold PRS wordmark in `{colors.primary}` sits centered above the column grid. Social icons and a legal/privacy strip run below the columns at `{typography.caption}` size. A 1px `{colors.hairline}` rule separates the footer from the last page section.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline scales to ~32px; nav collapses to hamburger drawer; finish swatches scroll horizontally; spec table renders as labeled rows |
| Tablet | 744–1128px | Two-column product grid; hero retains full-bleed, CTA moves below headline block; model selector scrolls horizontally |
| Desktop | 1128–1440px | Three-column product grid; nav fully expanded; hero minimum 90vh with lower-left text cluster |
| Wide | > 1440px | Grid and content capped at 1440px max-width and centered; hero image scales to cover remaining viewport width |

### Touch Targets

- All buttons minimum 48px tall
- Nav hamburger and icon buttons minimum 44×44px
- Finish swatches 40px diameter with 8px gap between (48px effective tap zone)
- Model selector segments minimum 44px tall on mobile
- Footer links minimum 44px vertical tap zone with `{spacing.xs}` padding

### Collapsing Strategy

- Primary nav categories collapse into a full-height left-side slide-over drawer on mobile; subcategories expand in-place within the drawer
- Spec table collapses to a single scrollable column with left-justified label/value pairs stacked vertically
- Finish swatch row becomes a horizontally scrolling strip with visible overflow fade at the trailing edge
- Footer four-column link grid collapses to a single stacked accordion on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site is behind Cloudflare anti-bot protection ("Just a moment..." title); only one hex color (#313131 charcoal) was reliably extracted
- No custom brand fonts detected — only system font stacks found; PRS may use licensed display or text typefaces not visible during extraction
- Primary accent color (#c9a84c warm gold) is inferred from brand knowledge, not extracted; the real production value may differ
- No meta theme-color was set; dark-mode canvas and surface values are estimated from the #313131 anchor
- Desktop navigation structure (mega-menu flyout vs. simple dropdown) could not be confirmed
- Hover and transition timing values (easing curves, duration) are entirely unextracted
- Private Stock configurator UI patterns (material selection, inlay chooser, finish builder) are not captured here
- Pricing format, currency-locale conventions, and MAP policy display patterns were not available for extraction
