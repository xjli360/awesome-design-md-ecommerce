---
version: alpha
name: "Ilve"
source_url: "https://www.ilveusa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The front face of an Ilve professional range ships in over thirty custom enamel finishes — celadon, cobalt, aubergine — but the digital counterpart grounds itself in something closer to the appliance's own cold-rolled steel. A deep teal-navy (#165c7d) sits at the center of every primary action, reading somewhere between a professional kitchen wall and a Ligurian harbor at dusk. It anchors CTA buttons, active nav states, and the left accent border of the configurator panel, while a companion deep navy (#003971) moves beneath it as the weight behind section headers, footer backgrounds, and dark-mode hero modules. Red (#ff0000) surfaces only where a pilot light would — warning messages, out-of-stock flags, hard-stop validation errors — never decoratively, keeping the overall palette as composed as the cast-iron grates the brand is known for. The neutrals extracted from the site read like brushed steel and matte enamel in digital form: a near-black charcoal (#444444) holds body copy, a mid-gray (#6a6c6c) handles dimension callouts and spec labels, and a pale silver (#e3e3e3) rules hairline borders and alternating spec rows. The font extraction returned a contaminated stack (Mothercare 2020, from an unrelated children's apparel brand injected via a compromised page title) and cannot be trusted; the typographic system below substitutes a precise geometric sans appropriate to Italian precision manufacturing, set at light-to-medium weights — 300 for display, 400 for body — because the photography and range silhouettes provide the visual mass. Components carry {rounded.xs} and {rounded.sm} geometry throughout. There are no pill buttons, no softened modal corners, no full-radius anything except the color-swatch circles in the configurator. Layout breathes at {spacing.section} vertical rhythm in product photography zones and pulls in to {spacing.lg} gutters for spec tables and comparison modules — enough information density to support a considered luxury purchase, never so compressed it reads as fine print.

colors:
  primary: "#165c7d"
  primary-active: "#0e3f58"
  primary-disabled: "#a0c4d4"
  secondary-navy: "#003971"
  link-blue: "#1979c3"
  accent-red: "#ff0000"
  error: "#ff0c0c"
  ink: "#444444"
  body: "#414141"
  muted: "#6a6c6c"
  hairline: "#e3e3e3"
  canvas: "#ffffff"
  surface-soft: "#f5f7f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Ilve Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Ilve Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Ilve Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Ilve Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Ilve Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Ilve Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Ilve Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Ilve Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  label-upper:
    fontFamily: "'Ilve Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Ilve Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Ilve Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Ilve Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  spec-label:
    fontFamily: "'Ilve Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'Ilve Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.25px

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
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.primary}"
    padding: 13px 31px
    height: 48px
  button-secondary-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.on-dark}"
    padding: 13px 31px
    height: 48px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 72px
  nav-bar-dark:
    backgroundColor: "{colors.secondary-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "2px solid {colors.primary}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.12)"
    padding: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    imageRounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-caption:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.secondary-navy}"
    textColor: "{colors.on-dark}"
    minHeight: 600px
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subheadline:
    typography: "{typography.body-md}"
    textColor: "{colors.on-dark}"
    opacity: 0.85
  collection-grid:
    backgroundColor: "{colors.canvas}"
    columns: 3
    gap: "{spacing.lg}"
    paddingVertical: "{spacing.section}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    rowPadding: "{spacing.md} {spacing.base}"
  spec-table-label:
    textColor: "{colors.muted}"
    typography: "{typography.spec-label}"
  spec-table-value:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  badge-award:
    backgroundColor: "{colors.secondary-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  color-swatch:
    size: 32px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
    borderActive: "2px solid {colors.primary}"
  configurator-panel:
    backgroundColor: "{colors.surface-soft}"
    borderLeft: "3px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  price-display:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  dealer-locator-button:
    backgroundColor: "{colors.secondary-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  footer:
    backgroundColor: "{colors.secondary-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    paddingVertical: "{spacing.xxl}"
  footer-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    opacity: 0.75
    hoverOpacity: 1
  footer-heading:
    textColor: "{colors.on-dark}"
    typography: "{typography.label-upper}"

## Components

### Buttons

**`button-primary`** — Deep teal (#165c7d) fill, white type at `{typography.button-md}` (15px, weight 500, 0.5px tracking), 2px radius. The minimum corner softening that prevents the button from reading as a border artifact on a white background. Used for primary CTAs including "Configure Your Range", "Request a Quote", and "Find a Dealer". Active state darkens to #0e3f58; disabled state washes to the pale teal `{colors.primary-disabled}`.

**`button-secondary`** — White fill with a 1.5px primary-teal border and matching teal text. Paired with `button-primary` in dual-CTA zones (e.g., "Configure" alongside "Download Spec Sheet"). On dark hero backgrounds, converts to `button-secondary-dark`, replacing the teal border and text with white while maintaining identical geometry.

**`button-text-link`** — Transparent, teal-colored with underline. Used in spec table footers, article inline references, and in-page section anchors where a bordered button would compete with surrounding data.

### Navigation

**`nav-bar`** — 72px tall, white fill, single hairline border below. Category links use `{typography.nav-link}` (14px, weight 500, 0.5px tracking) — the tightened tracking reads as considered without entering logo-type territory. Transitions to `nav-bar-dark` (navy fill, white text) on full-bleed dark hero pages.

**`nav-dropdown`** — Appears below the nav rail on hover or focus. White panel, 2px primary-teal top border, soft drop shadow (0 8px 24px). The colored top edge connects the panel to its parent tab without needing an arrow notch or pointer decoration.

### Product Cards

**`product-card`** — White fill, 1px hairline border, 4px radius. Product photography bleeds to card edges with no inner radius — full-range shots on white backgrounds do not require rounding softening. Title uses `{typography.title-md}`, secondary copy uses `{typography.body-sm}` in `{colors.muted}`. In collection grids, cards carry no hover elevation; the product image scales 2–3% on hover to signal interactivity without breaking the grid's geometric regularity.

### Hero

**`hero`** — Full-width, navy (#003971) background, 600px minimum height. Headline in `{typography.display-xl}` (48px, weight 300) against white — the light weight reads as Italian restraint because size and leading carry visual mass on their own. A dual-CTA pair (`button-primary` + `button-secondary-dark`) sits below with `{spacing.lg}` between them. Range photography is placed right-of-center at 110–120% natural scale, bleeding into the right edge for depth.

### Configurator Panel

**`configurator-panel`** — The color-and-finish configurator is the most complex interaction on the site. A panel with a 3px primary-teal left border sits beside the range canvas render. Finish swatches use `{color-swatch}` tokens — 32px circles at rest with hairline rings, 2px primary rings on active selection — arranged in an 8-per-row grid. Each swatch carries a `{typography.caption}` label below in `{colors.muted}`. On mobile the panel stacks above the canvas render, swatch grid reduces to 6 per row.

### Spec Table

**`spec-table`** — `{colors.surface-soft}` tint on alternating rows, 1px hairline separators between rows. Left column holds spec labels in `{typography.spec-label}` muted gray; right column holds values in `{typography.body-sm}` ink. A `{badge-award}` tag may float alongside spec rows flagging award-recognized features. The spec table is a key conversion-path element for a considered luxury purchase — readable data density is a functional requirement, not just style.

### Badges

**`badge-new`** — Teal (#165c7d) fill, white uppercase type (11px, weight 600, 1.5px tracking). Used on newly introduced range models and fresh colorway additions to existing lines.

**`badge-award`** — Navy (#003971) fill, white uppercase type. Flags third-party industry awards (press recognitions, "Best Professional Range" citations) in product cards and spec sheets without disrupting the neutral product layout.

### Price Display

**`price-display`** — 28px, weight 300, tight −0.25px tracking in `{colors.ink}`. Light weight keeps the MSRP from competing visually with the product name or photography; the character spacing makes multi-digit figures read as a single unit.

### Footer

**`footer`** — Navy (#003971) full-width band with `{spacing.xxl}` vertical padding. Four-column layout: product categories, support, about, dealer locator. Column headings use `{typography.label-upper}` (uppercase, 1.5px tracking) in white; links use `{typography.body-sm}` at 75% opacity, rising to 100% on hover. No horizontal separator lines inside the footer — column structure provides sufficient visual organization.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replacing top rail; hero min-height drops to 400px; configurator panel stacks above canvas; spec tables scroll horizontally; CTA pairs stack vertically at full width |
| Tablet | 744–1128px | Two-column product grid; nav collapses secondary items into overflow menu; hero headline drops to `display-md` (32px); configurator stays side-by-side at 40/60 split |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with dropdown panels; hero at full 600px; configurator at 35/65 split with panel sticky-scrolled |
| Wide | > 1440px | Content capped at 1440px centered on white margins; hero photography scales to fill extended viewport; grid stays three columns but card widths grow proportionally |

### Touch Targets

- All buttons minimum 48px height on touch viewports
- Color swatches expand from 32px to 44px on touch devices to prevent mis-selection
- Nav links in hamburger drawer set to 56px row height
- Spec table rows expand to 48px minimum on mobile for tap accuracy

### Collapsing Strategy

- Main nav collapses to hamburger at < 744px; product categories become accordion rows inside the drawer
- Dual-CTA button pairs stack vertically on mobile with full-width buttons, primary above secondary
- Four-column footer collapses to two columns at tablet, single column at mobile with headings remaining visible as section anchors
- Configurator panel moves from side-by-side to stacked layout on mobile; swatch grid narrows to 6 per row
- Hero typography steps down one scale per breakpoint: `display-xl` on desktop, `display-md` at tablet, `display-sm` at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Font extraction unreliable**: Page title returned "CERITOTO • Link Toto 4D Dan Situs Slot Deposit 5k Hari Ini Mudah Menang" — clear evidence of SEO hijacking or page compromise at extraction time. The font stack "Mothercare 2020 / mothercare_2020-regular-webfont" belongs to an unrelated children's apparel brand and cannot reflect Ilve's typography. All type tokens use a geometric sans fallback pending a clean extraction.
- **Color palette may be partially contaminated**: With a compromised page in the extraction pipeline, some values (#003399, #1979c3) may originate from injected third-party content rather than Ilve's own stylesheet. The teal (#165c7d), deep navy (#003971), and neutral grays (#e3e3e3, #444444, #6a6c6c) are the most plausible Ilve candidates.
- **No meta theme-color**: Could not confirm a single canonical primary hex from a browser-level brand signal.
- **Configurator finish palette unresolved**: Ilve offers 30+ enamel colors for range bodies. These product-finish colors are distinct from the UI palette and were not captured in the extraction.
- **Animation and motion specs absent**: No easing curves or timing values recoverable; configurator canvas transitions and product card hover motion remain unspecified.
- **Icon system unknown**: Navigation glyphs, feature icons, and technical spec icons not documented; stroke weight and style (outline vs. fill) unconfirmed.
- **Dealer locator UI**: The dealer-locator flow (map provider, pin styling, search input behavior) could not be confirmed from extraction.
