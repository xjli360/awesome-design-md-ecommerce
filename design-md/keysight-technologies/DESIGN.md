---
version: alpha
name: "Keysight Technologies"
source_url: "https://www.keysight.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Oscilloscope bandwidth at 110 GHz and network analyzer dynamic range at 120 dB set the engineering stakes at Keysight Technologies, and the same demand for zero ambiguity propagates through the brand's visual grammar. A single corporate blue (#0071B8) carries every primary CTA, product-family header, active link state, and search-submit control — it is the only expressive color in a system otherwise built from navy ({colors.surface-dark}), near-white surfaces ({colors.surface-soft}), and neutral grays. Corner radii are minimal throughout: {rounded.xs} on buttons and inputs, {rounded.sm} on cards — the vocabulary of an instrument panel rather than a consumer storefront. Navigation is structured like a test system menu, with deep mega-menus organized by measurement discipline (oscilloscopes, network analyzers, signal generators, software) rather than by marketing category, reflecting a user base that arrives already knowing what measurement problem it needs to solve. Typography runs clean sans-serif at modest weights — 600 for headings, 400 for body — serving engineers who are reading spec values and comparing channel counts rather than responding to editorial voice. A teal accent ({colors.accent-teal}) marks application-domain intersections — 5G, aerospace, semiconductor, automotive — as pill-shaped badges on product cards and solution tiles, giving buyers a categorical filter cue at a glance. Dark navy hero banners ground the heaviest landing pages, transitioning via directional gradient to product photography on the right half. The spec comparison table is a first-class UI component — monospace data cells, sticky first column, {colors.surface-dark} header — designed for engineers evaluating 20-plus parameters side by side. Resource tiles (datasheets, application notes, configuration guides) use a muted {colors.surface-soft} fill with a blue file icon, making the download CTA immediately legible inside dense resource libraries. The system reserves design energy entirely for navigability and information density, with no ornamental elements anywhere in the component vocabulary.

colors:
  primary: "#0071B8"
  primary-active: "#005C97"
  primary-hover: "#0080CC"
  primary-disabled: "#99C9E4"
  ink: "#1D1D1B"
  body: "#3C3C3C"
  muted: "#6B6B6B"
  muted-soft: "#9B9B9B"
  hairline: "#D8D8D8"
  hairline-soft: "#EBEBEB"
  canvas: "#FFFFFF"
  surface-soft: "#F4F7FB"
  surface-card: "#FFFFFF"
  surface-mid: "#E8EEF4"
  surface-dark: "#002A4A"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  accent-teal: "#00B5CC"
  accent-teal-muted: "#E0F6FA"
  success: "#00875A"
  warning: "#FF8C00"
  error: "#C62828"
  table-row-alt: "#F9FAFB"
  link: "#0071B8"
  link-hover: "#005C97"

typography:
  display-xl:
    fontFamily: "'Neue Helvetica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Neue Helvetica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Neue Helvetica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Neue Helvetica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Neue Helvetica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Neue Helvetica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Neue Helvetica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Neue Helvetica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Neue Helvetica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-label:
    fontFamily: "'Neue Helvetica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.45
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Neue Helvetica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'Neue Helvetica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Neue Helvetica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  spec-data:
    fontFamily: "'Roboto Mono', 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  badge:
    fontFamily: "'Neue Helvetica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.4px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 12px
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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: "1.5px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1.5px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 16px
    height: 40px
    border: none
  button-ghost-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoAreaWidth: 160px
    megaMenuBackground: "{colors.canvas}"
    megaMenuBorder: "1px solid {colors.hairline-soft}"
    megaMenuShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    shadow: none
    shadowHover: "0 2px 12px rgba(0,0,0,0.10)"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
    overlayGradient: "linear-gradient(90deg, {colors.surface-dark} 55%, transparent 100%)"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 48px
    border: "2px solid {colors.primary}"
    borderFocus: "2px solid {colors.primary-active}"
    iconColor: "{colors.primary}"
    submitBackground: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitRounded: "{rounded.sm}"
  solution-badge:
    backgroundColor: "{colors.accent-teal-muted}"
    textColor: "{colors.accent-teal}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
    border: "1px solid {colors.accent-teal}"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-dark}"
    headerTextColor: "{colors.on-dark}"
    headerTypography: "{typography.title-sm}"
    rowTextColor: "{colors.body}"
    rowTypography: "{typography.spec-data}"
    rowAltBackground: "{colors.table-row-alt}"
    rowBorder: "1px solid {colors.hairline-soft}"
    cellPadding: "10px {spacing.base}"
    rounded: "{rounded.none}"
    stickyFirstColumn: true
  download-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    iconColor: "{colors.primary}"
    ctaTypography: "{typography.button-sm}"
    ctaColor: "{colors.primary}"
    ctaColorHover: "{colors.primary-active}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.title-sm}"
    checkmarkColor: "{colors.primary}"
    borderRight: "1px solid {colors.hairline}"
    activeChipBackground: "{colors.surface-mid}"
    activeChipTextColor: "{colors.primary}"
    activeChipRounded: "{rounded.full}"
  solution-tile:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderHover: "1px solid {colors.primary}"
    iconColor: "{colors.primary}"
    padding: "{spacing.xl}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  section-divider:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    headlineColor: "{colors.surface-dark}"
    accentBar: "4px solid {colors.primary}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Filled #0071B8 with white label at `{typography.button-md}` (600 weight, 15px) and a 40px height with minimal `{rounded.xs}` (2px) corners. Hover shifts to `{colors.primary-hover}`, active darkens to `{colors.primary-active}`, disabled renders at the pale `{colors.primary-disabled}` with `cursor: not-allowed`. No pill shapes appear anywhere in the button vocabulary — the hard corner is load-bearing to the precision aesthetic.

**`button-secondary`** — White fill with a 1.5px `{colors.primary}` border and blue label at the same `{typography.button-md}` scale. Hover fills `{colors.surface-soft}` and deepens both border and label to `{colors.primary-active}`. Paired with `button-primary` on product and solution pages — primary anchors "Configure / Buy" and secondary anchors "Download Datasheet / Learn More".

**`button-ghost`** — Transparent background, no border, blue text. Used for inline text-level actions within dense layouts like filter sidebars and spec tables. Hover reveals a subtle `{colors.surface-soft}` fill to confirm interactivity without adding visual weight to already-dense data views.

### Navigation

**`nav-bar`** — 64px white bar with a 1px `{colors.hairline}` bottom rule. Logo reserves 160px on the left; primary product-family links sit center using `{typography.nav-link}` (500 weight); search, account, and cart icons anchor the right. On hover, mega-menu panels drop below the bar on a white background with a `0 4px 16px rgba(0,0,0,0.12)` shadow — columns inside organize sub-categories by measurement type and frequency range, not by brand priority. No rounded corners on any nav surface.

### Product Cards

**`product-card`** — White card with 1px `{colors.hairline}` border and `{rounded.sm}` (4px) corners. Product renders on a `{colors.surface-soft}` image swatch in the upper section; title at `{typography.title-md}`, model number and key spec line at `{typography.body-sm}`. On hover, a `0 2px 12px rgba(0,0,0,0.10)` shadow lifts the card without shifting it. Solution badges from `solution-badge` may appear on the card to signal application-domain intersections (5G, aerospace, semiconductor).

### Search

**`search-bar`** — The primary discovery path for a catalog spanning thousands of instruments and accessories. Rendered at 48px height with a heavier 2px `{colors.primary}` border that signals its primacy on product-finder and category-listing pages. A filled blue submit button is flush to the right end; focus state holds the same border color so the bar remains stable on both white and `{colors.surface-soft}` backgrounds. Autocomplete suggestions appear in a white dropdown with 1px `{colors.hairline-soft}` borders.

### Spec Table

**`spec-table`** — An engineering-grade comparison component that is a first-class UI citizen on product and product-family pages. Header row fills `{colors.surface-dark}` with white `{typography.title-sm}` labels. Body rows alternate between `{colors.canvas}` and `{colors.table-row-alt}`, with 1px `{colors.hairline-soft}` row separators. Cell data uses `{typography.spec-data}` (monospace, 13px) to align numeric values in columns cleanly across bandwidth, dynamic range, frequency range, and input impedance fields. The first column is sticky on horizontal scroll; no rounded corners anywhere on the table.

### Download Card

**`download-card`** — Light `{colors.surface-soft}` tile used in resource libraries (application notes, white papers, datasheets, configuration guides). A file-type icon in `{colors.primary}` appears on the left; title at `{typography.body-sm}` and a "Download PDF" link at `{typography.button-sm}` sit to the right. On hover, icon and link deepen to `{colors.primary-active}`. Used in grid layouts of 3–4 columns on resource-center pages.

### Filter Sidebar

**`filter-sidebar`** — Left-rail component on product-listing and resource pages. Section labels at `{typography.title-sm}`, checkbox items at `{typography.body-sm}` with `{colors.primary}` check marks. Active filter selections become dismissible chips in `{colors.surface-mid}` fill with `{colors.primary}` text at `{rounded.full}`, displayed in an "Applied Filters" strip above the result grid. The sidebar sits on `{colors.canvas}` with a 1px `{colors.hairline}` right border separating it from the grid — no fill of its own.

### Hero Banner

**`hero-banner`** — Full-width `{colors.surface-dark}` (#002A4A) section with a left-aligned content column at roughly 50% width. Headline at `{typography.display-xl}` (white), subhead at `{typography.display-sm}`, body copy at `{typography.body-md}`. A directional gradient (`linear-gradient(90deg, {colors.surface-dark} 55%, transparent)`) transitions to an instrument or application photograph on the right half. Primary CTA uses the `button-primary` fill; a secondary CTA on dark backgrounds uses a white-border, white-label variant of `button-secondary`.

### Solution Badges

**`solution-badge`** — Pill-shaped tags (`{rounded.full}`) in `{colors.accent-teal-muted}` fill with `{colors.accent-teal}` text and a 1px teal border. Applied to product cards, solution tiles, and application-note cards to signal intersection with a test domain. `{typography.badge}` (11px, 700 weight, uppercase, 0.4px tracking) keeps the label legible at small card sizes. `new-badge` uses the same pill geometry in solid `{colors.primary}` for newly released instruments.

### Solution Tile

**`solution-tile`** — `{colors.surface-mid}` tile with `{rounded.sm}` corners, used on solution-area landing pages (5G / IoT / Aerospace / Automotive). Title at `{typography.display-sm}`, body at `{typography.body-sm}`, a blue icon at top. Border lifts to `{colors.primary}` on hover with no other movement. Padding at `{spacing.xl}` gives the tile space proportional to the icon + headline + body stack inside.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces mega-menus with accordion expansion; search bar full-width below header strip; spec tables scroll horizontally with sticky first column; filter sidebar collapses to a bottom-sheet modal triggered by a fixed "Filter & Sort" bar; hero headline steps down to `{typography.display-md}` |
| Tablet | 744–1128px | Two-column product grid; nav collapses to icon-only top row with product-family text hidden; search bar remains in header; filter sidebar visible as a 200px left rail; hero content narrows to 65% width |
| Desktop | 1128–1440px | Three or four-column product grid; full mega-menu nav; 240px filter sidebar; spec table shows 5–6 visible columns; hero image fully visible with directional gradient |
| Wide | > 1440px | Content max-width 1440px centered; hero padding increases to `{spacing.section}` vertical; product grid can render up to five columns on category pages; mega-menu columns expand to wider gutters with more sub-category visibility |

### Touch Targets

- All buttons and nav items maintain a minimum 44×44px tap area, even when visual size is smaller
- Filter checkboxes use 20×20px visual elements inside 44px tall touch rows
- Product card entire surface is tappable on mobile, not just the CTA
- Breadcrumb links expand to full-height row tap targets on mobile
- Mega-menu accordion handles have 48px minimum height on touch devices

### Collapsing Strategy

- Mega-menu collapses to a hamburger drawer with accordion expansion; product-family top-level items always visible, sub-categories expand in place
- Spec table columns collapse progressively — least-differentiating specs hide first; key specs (frequency range, bandwidth, channel count, dynamic range) remain visible at all breakpoints
- Filter sidebar becomes a full-height bottom sheet on mobile, triggered by a persistent "Filter & Sort" bar fixed at the viewport bottom
- Hero banner reflows from side-by-side to stacked on mobile: image crops to 16:9 above the content block; gradient is removed
- Download card grid collapses from 4-column to 2-column at tablet, 1-column at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No colors extracted** — the live site returned "Access Denied" to the crawler. All hex values are derived from widely documented Keysight visual identity materials and brand knowledge, not from direct CSS extraction. Verify against official Keysight brand guidelines before production use.
- **No font stacks extracted** — the `Neue Helvetica` / `Helvetica Neue` stack is inferred from the brand's enterprise design tradition; the actual licensed typeface name, weights, and loading mechanism should be confirmed from Keysight's internal brand kit or rendered stylesheet.
- **Corner radii unconfirmed** — `{rounded.xs}` (2px) and `{rounded.sm}` (4px) are inferred from enterprise-tech conventions; actual values may differ from the live site.
- **Mega-menu taxonomy** — product category groupings are inferred from publicly documented Keysight product families; actual column structure and sub-category labels should be reviewed against the live navigation.
- **Icon library unspecified** — navigation glyphs, solution-area icons, and file-type icons are referenced by behavior but not catalogued; the actual icon set (SVG library, icon font, or design-system component name) is unknown.
- **Product configurator components** — Keysight uses an option-code configurator flow for instrument ordering; those components (option selector, part-number builder, lead-time display) are unspecified here due to extraction failure.
- **Dark-mode palette absent** — no dark-mode variant could be derived; it is unknown whether Keysight's application pages (PathWave software, online licenses) carry a separate dark-mode token set.
- **E-commerce / quoting flow** — pricing display, "Add to Cart," request-a-quote, and multi-unit ordering components are not defined due to lack of extraction data.
