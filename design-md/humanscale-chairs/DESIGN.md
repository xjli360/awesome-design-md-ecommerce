---
version: alpha
name: "Humanscale (Chairs)"
source_url: "https://www.humanscale.com/products/seating"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every Humanscale seating page opens with a near-silent palette — deep graphite (#1d1d1b) on white (#ffffff), no accent voltage, no promotional red — because the brand's authority derives from precision tolerances and load ratings rather than from color psychology. The chairs themselves carry all the visual energy: the sinuous carbon-fiber shell of the Freedom Headrest, the gossamer mesh of the Liberty, and the folding geometry of the Diffrient Smart act as the primary graphic system. Typography runs at tight tracking and light weight — display lines sit at fontWeight 300, not 700, behaving more like engineering documentation than retail copy; certifications, material grades, and weight capacities share the same visual register as the product name and price. Rounded tokens stay minimal — {rounded.xs} on swatches and inputs, {rounded.none} for every button — because Humanscale's product geometry is rectilinear and precise, not pillow-soft. Product configuration panels, where users select fabric families, base finishes, and armrest grades, are the most functionally dense moments on the page; they use a compact swatch grid with tight {spacing.sm} gutters and a hard outline on the selected state rather than a color fill. The navigation system expands via a horizontal mega-menu organized by product category, leaning on {colors.ink} type against {colors.canvas} with a single underline rule as the only active indicator. CTA copy reads as directives — Configure, Request a Quote, Find a Dealer — transactional language suited to the B2B procurement context where facilities managers and corporate buyers, not impulsive individual shoppers, often finalize the purchase. Surface colors grade from {colors.canvas} through {colors.surface-soft} using luminance steps small enough that section breaks feel structural rather than decorative. The overall grammar is German functionalist: every element earns its presence by doing work, and the system's extreme restraint is its most legible brand signal.

colors:
  primary: "#1d1d1b"
  primary-active: "#000000"
  primary-disabled: "#b0b0b0"
  ink: "#1d1d1b"
  body: "#3d3d3d"
  muted: "#767676"
  muted-soft: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  surface-mid: "#eeeeee"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#c0392b"
  swatch-selected-outline: "#1d1d1b"

typography:
  display-xl:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.02em
  body-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  label-caps:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  spec-value:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    padding: "12px 24px"
    height: 44px
    border: "1px solid {colors.primary}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary-disabled}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "11px 23px"
    height: 44px
    border: "1px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "11px 0px"
    borderBottom: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "10px 12px"
    height: 44px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.error}"
    textColor: "{colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "10px 12px"
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 28px
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "{spacing.xl} {spacing.xxl}"
    borderTop: "1px solid {colors.hairline}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.08)"
    sectionLabelTypography: "{typography.label-caps}"
    sectionLabelColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.10)"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "{spacing.section} {spacing.xxl}"
    minHeight: 520px
  hero-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
    minHeight: 520px
  spec-table:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.label-caps}"
    valueTypography: "{typography.spec-value}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rowPadding: "{spacing.sm} {spacing.base}"
    alternateRowBg: "{colors.surface-soft}"
  swatch-selector:
    size: 28px
    gap: "{spacing.xs}"
    selectedOutline: "2px solid {colors.swatch-selected-outline}"
    selectedOutlineOffset: 2px
    rounded: "{rounded.none}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
  configuration-panel:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.xl}"
    gap: "{spacing.lg}"
    borderTop: "1px solid {colors.hairline}"
    sectionLabelTypography: "{typography.label-caps}"
    sectionLabelColor: "{colors.muted}"
  badge-award:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  sustainability-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xxl}"
    borderTop: "1px solid {colors.hairline}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    gap: "{spacing.xs}"
  filter-tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
    border: "1px solid {colors.hairline}"
    activeBackground: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.ink}"
  pagination:
    textColor: "{colors.ink}"
    activeBackground: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    size: 36px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    padding: "{spacing.xxl}"
    columnGap: "{spacing.xl}"

## Components

### Buttons

**`button-primary`** — A fully square-cornered (`{rounded.none}`) dark-charcoal fill button with uppercase, moderately tracked letter-spacing copy that reads as a directive rather than an invitation. Hover and press state deepens to pure black (`{colors.primary-active}`); disabled fades the fill to `{colors.primary-disabled}` while the uppercase label persists. A matching 1px border ensures the button reads at identical optical weight in both dark and light layout contexts.

**`button-secondary`** — Canvas fill with a 1px `{colors.ink}` perimeter outline, matching the primary's exact height and uppercase type treatment. Active state shifts the background to `{colors.surface-soft}` to signal press without reversing color polarity. Used for secondary actions in configuration panels, quote flows, and dealer-finder CTAs.

**`button-ghost`** — Transparent background with no surrounding border; only a bottom underline rule at `{colors.ink}` anchors the label visually. Applied for in-context text links that carry enough weight to act as navigation cues — "View All Finishes," "Download Spec Sheet," "See Full Dimensions."

### Text Input

**`text-input`** — Zero-radius input box with a 1px `{colors.hairline}` border that sharpens to a full `{colors.ink}` rule on focus. No inner shadow, no glow ring — the fieldset reads like a dimension box on a technical drawing. Error state swaps border and label text to `{colors.error}`. The `select-input` variant follows identical sizing and border rules with a custom SVG chevron replacing the native arrow.

### Navigation

**`nav-bar`** — 64px-tall white bar, bottom-bordered at `{colors.hairline}`. The Humanscale wordmark sits left at 28px height; product category links in `{typography.nav-link}` run to the right. On hover, a `nav-mega-menu` drops full-width below the bar, organized by product family with thumbnail imagery, `{typography.label-caps}` section headers in `{colors.muted}`, and 1px `{colors.hairline}` column separators. The mega-menu carries no fill color other than `{colors.canvas}`, making its boundaries defined entirely by the top border rule and a diffuse drop shadow.

### Product Card

**`product-card`** — Square-cornered card with a `{colors.surface-soft}` image field that occupies the top two-thirds. Product name renders in `{typography.title-md}` and a one-line range descriptor in `{typography.caption}` at `{colors.muted}`. No badge overlays, no price display — pricing routes exclusively through configure or quote CTAs. Hover state lifts the card with a contained `box-shadow` to signal interactivity without changing background color.

### Hero Banner

**`hero-banner`** — Full-width section on `{colors.surface-soft}` with a `{typography.display-xl}` headline at fontWeight 300. The light-weight display at large scale is the brand's primary typographic signature: authority through precision rather than mass. A `hero-dark` variant inverts the field to `{colors.ink}` with `{colors.on-dark}` text, deployed for product-launch announcements, award callouts, and campaign-specific landing sections.

### Spec Table

**`spec-table`** — Two-column key-value table with labels in `{typography.label-caps}` at `{colors.muted}` and values in `{typography.spec-value}` at `{colors.ink}`. Alternating rows use `{colors.surface-soft}` to maintain scanability without a dividing line per row. This component is the densest information surface in the Humanscale system and its most differentiated: weight capacity, seat-height range, back-angle adjustment, certifications, and material composition all live at equal typographic weight, signaling that every specification carries equal importance.

### Swatch Selector & Configuration Panel

**`swatch-selector`** — 28×28px square swatches (no radius) in a tight grid with `{spacing.xs}` gaps. Selected state applies a 2px `{colors.swatch-selected-outline}` outline with 2px offset — no fill indicator, no checkmark, just a hard perimeter rule that mirrors the border vocabulary used throughout the system. A `{typography.caption}` label in `{colors.muted}` below the grid names the currently selected option. The **`configuration-panel`** wraps groups of swatch selectors, dropdown `select-input` controls, and quantity inputs in a `{colors.surface-soft}` container, using `{typography.label-caps}` headers to separate fabric family, base finish, armrest type, and caster selection.

### Filter Tags

**`filter-tag`** — Square-cornered compact pills used in the seating-grid filter bar. Default state is outlined on white canvas; active flips to solid `{colors.ink}` fill with `{colors.on-primary}` text — the same polarity inversion as the primary/secondary button pair, keeping the filter system typologically consistent with page-level CTAs.

### Award Badge

**`badge-award`** — Flat `{colors.surface-mid}` rectangle with `{typography.caption}` text in `{colors.muted}`. Used inline near product names or in a horizontal strip below the hero to surface certifications (BIFMA, Cradle to Cradle, GREENGUARD) without interrupting the rectilinear product image.

### Footer

**`footer`** — Full-width `{colors.ink}` field acting as a hard visual stop after the white body. Column headers in `{colors.on-dark}`, link text in `{colors.muted-soft}`. Dense multi-column layout covers product lines, support resources, sustainability commitments, and corporate information. The dark footer is the only place on the page where the brand's primary surface color inverts, reinforcing its role as a terminal anchor rather than a decorative band.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-height drawer; hero reduces to 320px min-height; configuration panel becomes full-width bottom sheet |
| Tablet | 744–1128px | Two-column product grid; mega-menu persists horizontally but truncates to fewer columns; spec table remains full-width; hero at 420px |
| Desktop | 1128–1440px | Three-column product grid; full mega-menu with image thumbnails; hero at 520px; configuration panel floats as right-rail sidebar beside product image |
| Wide | > 1440px | Content max-width 1400px centered; four-column grid option; hero scales to full viewport minus nav; footer columns expand to 5 |

### Touch Targets

- All buttons, filter tags, and swatch selectors minimum 44×44px tap zone
- Swatch selectors rendered at 28px visual size with transparent padding to reach 44px tap area
- Nav drawer links at minimum 48px row height on mobile
- Pagination controls maintain 44px minimum regardless of visual circle size
- Spec table rows padded to 44px height on mobile for accessible tap targets on expandable rows

### Collapsing Strategy

- Mega-menu collapses to an accordion-style drawer inside the mobile hamburger panel, with `{typography.label-caps}` section headers as expand triggers
- Spec table collapses to stacked label-above-value pairs (label in `{typography.label-caps}`, value in `{typography.spec-value}`) below 744px
- Configuration panel moves from desktop right-rail to a bottom-anchored slide-up sheet on mobile, triggered by a sticky "Configure" button fixed above the viewport bottom edge
- Product hero image and configuration panel stack vertically on tablet; side-by-side at 50/50 split on desktop
- Footer transitions from 4-column to 2-column at tablet breakpoint, then single-column at mobile with each section collapsed behind an accordion toggle

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site (JS-loaded design tokens or anti-bot protection returned nothing); all palette values are derived from widely-observable Humanscale brand characteristics and must be verified against production CSS before committing to implementation
- Font family was not extracted; "Neue Haas Grotesk" is inferred from brand precedent and widely-referenced design comparables — verify the actual webfont name, file format, and weight axes in production stylesheet
- No `meta theme-color` tag was present; primary charcoal `#1d1d1b` is an estimate based on observable brand ink and should be confirmed
- Button radius is set to `{rounded.none}` based on the brand's rectilinear product aesthetic — some interactive micro-components may use `{rounded.xs}` (2px); verify in production
- Pricing display pattern not confirmed (quote-only vs. direct list price vs. dealer-gated); `configuration-panel` CTA routing and any price-display typography may need adjustment
- Animation and transition timing entirely absent from extraction; 200ms ease assumed for hover state transitions — verify production motion specs
- Dark-mode or high-contrast variant support unknown; no evidence either way from available data
