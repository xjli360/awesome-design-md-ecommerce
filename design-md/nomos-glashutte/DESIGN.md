---
version: alpha
name: "Nomos Glashütte"
source_url: "https://www.nomos-glashuette.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every Nomos Glashütte dial carries a printed minute track governed by tolerances measured in microns — the same precision discipline shapes their digital presence. The site anchors to a deep cobalt (#003399) borrowed directly from the Atlantic and Metro Neomatik oceanic collections; against the near-white canvas layers (#f6f6f6, #fafafa, #f8f8f8) it reads as technical authority without aggression. Gotham Narrow — the compressed, rationalist grotesque — carries every headline and navigation label, its tight apertures echoing the thin hands and applied indices of the Tangente and Orion families. The narrow variant is deliberate: it lets long German compound words — Glashütter, Uhrenmacher, Schaltradchronograph — sit in single-line headers without wrapping.

  Secondary accents include a warm antiquarian gold (#af8649) for crown imagery and movement-plate callouts, a cool sage tint (#d4e2e2) for configurator chip highlights, and a near-natural linen (#edeae3, #f1f1ef) that surfaces in editorial zones to signal craft without gilding it. Alert states split between a decisive carmine (#d0021b) for errors and a mid-forest green (#19ac4c) for availability — both held to single-use discipline that prevents the minimal layout from fragmenting into a status dashboard.

  Corners are nearly absent: the UI runs on zero-radius containers throughout, matching the flat-bezel case profiles of the watches themselves. Section rhythm uses generous vertical spacing — 64px breaks, 48px between content clusters — so each product image performs as photography rather than as a merchandising tile. The product card floats against `{colors.surface-soft}` with a single `{colors.hairline}` border replacing the shadow-box convention used by most luxury e-commerce. The watch configurator — material selector, strap picker, dial preview — sits in a two-column lockup at desktop, collapsing to a single stacked scroll on mobile, using `{colors.accent-teal}` chips to mark the active configuration state.

  Interstate Gravur (`interstate_gravur_v01regular`) appears in isolated contexts — movement-plate engravings, serial-number stamps — functioning as a reference to Glashütte's horological documentation tradition rather than as a UI typeface. A reader who notices it has been shown, without being told, that the brand builds its own calibres.

colors:
  primary: "#003399"
  primary-active: "#002277"
  primary-disabled: "#99aedd"
  ink: "#111111"
  body: "#1e1e1e"
  muted: "#8c8c8c"
  muted-soft: "#a0a0a0"
  hairline: "#e2e2e2"
  hairline-light: "#ededed"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-warm: "#f1f1ef"
  surface-linen: "#edeae3"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  accent-gold: "#af8649"
  accent-teal: "#d4e2e2"
  accent-teal-dark: "#007862"
  alert-error: "#d0021b"
  alert-error-mid: "#e72645"
  alert-error-light: "#fbeff1"
  alert-success: "#19ac4c"
  alert-success-dark: "#0d7932"
  alert-success-light: "#e7fff1"
  scrim: "#111111"

typography:
  display-xl:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', 'Gotham A', 'Gotham B', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', 'Gotham A', 'Gotham B', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.13
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.3px
  caption-tabular:
    fontFamily: "'Gotham Narrow Tabular A', 'Gotham Narrow Tabular B', 'Gotham Narrow A', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  label-sm:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.5px
  price-display:
    fontFamily: "'Gotham Narrow Tabular A', 'Gotham Narrow Tabular B', 'Gotham Narrow A', monospace"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  gravur-accent:
    fontFamily: "interstate_gravur_v01regular, 'Gotham Narrow A', monospace"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.4
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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 32px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 31px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 31px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1/1"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
  collection-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.primary}"
    activeBorder: "2px solid {colors.primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
  hero-full:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 600px
    overlay: "rgba(17,17,17,0.35)"
  watch-configurator:
    backgroundColor: "{colors.canvas}"
    sectionLabelTypography: "{typography.label-sm}"
    sectionLabelColor: "{colors.muted}"
    rounded: "{rounded.none}"
  configurator-chip:
    backgroundColor: "{colors.canvas}"
    activeBackgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    activeTextColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: 6px 14px
    height: 44px
  movement-badge:
    backgroundColor: "{colors.surface-linen}"
    textColor: "{colors.body}"
    accentColor: "{colors.accent-gold}"
    accentRule: "2px solid {colors.accent-gold}"
    typography: "{typography.gravur-accent}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  availability-tag:
    inStockColor: "{colors.alert-success}"
    inStockBackgroundColor: "{colors.alert-success-light}"
    outOfStockColor: "{colors.alert-error}"
    outOfStockBackgroundColor: "{colors.alert-error-light}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  price-display-block:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
    installmentColor: "{colors.muted}"
    installmentTypography: "{typography.caption}"
  editorial-pull-quote:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    accentRule: "3px solid {colors.accent-gold}"
    padding: "{spacing.xl} {spacing.xxl}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    iconColor: "{colors.muted}"
    iconFocusColor: "{colors.primary}"
    border: "none"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 44px
  collection-grid:
    columns: 3
    gap: "{spacing.lg}"
    mobileColumns: 1
    tabletColumns: 2
    backgroundColor: "{colors.canvas}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    mutedTextColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    borderTop: none

## Components

### Buttons

**`button-primary`** — The cobalt fill (#003399) with all-caps Gotham Narrow at 14px and 1px letter-spacing is how Nomos marks every decisive CTA, from "In den Warenkorb" to "Discover Collection." The zero-radius edge is non-negotiable; it matches the flat-bezel profile of the watches. On `:active` the fill shifts to `{colors.primary-active}`; disabled state renders at `{colors.primary-disabled}`, a washed lavender that preserves the button's shape without inviting a click.

**`button-secondary`** — White fill with a 1px cobalt border and cobalt text, used for secondary actions in configurator panels and modal footers. The outlined treatment gives visual parity to paired primary/secondary button rows without fighting for dominance.

**`button-ghost`** — Transparent background, `{colors.hairline}` border, `{colors.ink}` text. Appears in editorial contexts — article footers, brand-story pages — where cobalt would dominate surrounding photography.

### Navigation

**`nav-bar`** — A 64px horizontal strip at `{colors.canvas}` with a single `{colors.hairline}` bottom border and no shadow or blur. Links use `{typography.nav-link}` at 0.5px letter-spacing — quiet enough that the Nomos logotype reads as the dominant element. Flyout sub-menus expand as full-width panels anchored below the nav rail, letting collection imagery serve as the flyout's primary content rather than a list of links.

### Product Cards

**`product-card`** — The watch face renders on white, bounded by a single `{colors.hairline}` rule — no radius, no drop shadow. Model name sits in `{typography.title-md}`; price occupies `{typography.price-display}` using the Gotham Narrow Tabular cut so euro signs and numerals align across multi-column grid rows. On hover the image translates 4px upward with a 200ms ease; no border-color change.

### Watch Configurator

**`watch-configurator`** — Occupies the right column at desktop alongside a static product image. Option sets render as `configurator-chip` rows: flat zero-radius chips in `{colors.canvas}` with `{colors.hairline}` borders at rest, toggling to `{colors.accent-teal}` fill with `{colors.primary}` border and text on selection. Material, dial, and strap groupings are separated by `{typography.label-sm}` headings in `{colors.muted}` gray.

### Movement Badge

**`movement-badge`** — A horizontal linen-tinted strip (`{colors.surface-linen}`) running beneath the product title on the PDP. Movement calibre, power reserve, and water-resistance rating render in `{typography.gravur-accent}` — the `interstate_gravur_v01regular` stencil face — with a fine `{colors.accent-gold}` rule above the strip. This is the only zone on the product page where the gravur face appears; its containment keeps the effect legible as a deliberate reference, not a typeface choice.

### Availability Tag

**`availability-tag`** — A small inline chip: forest green on pale green (`{colors.alert-success}` / `{colors.alert-success-light}`) for in stock; carmine on blush (`{colors.alert-error}` / `{colors.alert-error-light}`) for unavailable. Both use `{typography.label-sm}` uppercase at `{rounded.xs}` — the single concession to rounded corners in an otherwise flat interface, kept small enough (2px) to read as practical rather than decorative.

### Editorial Pull Quote

**`editorial-pull-quote`** — Used in brand-story and craft-editorial pages: a `{colors.surface-warm}` field with a 3px `{colors.accent-gold}` left rule and a large `{typography.display-sm}` quotation. Padding is `{spacing.xl}` vertical and `{spacing.xxl}` horizontal, giving the text room to breathe against the ivory-tinted ground without touching the page edge.

### Search

**`search-bar`** — A flat `{colors.surface-soft}` field with no border at rest and a `1px solid {colors.primary}` border on focus. Occupies full viewport width on mobile and a fixed 320px slot in the nav at desktop. The search icon transitions from `{colors.muted}` to `{colors.primary}` on focus.

### Footer

**`footer`** — Reverses to `{colors.ink}` with `{colors.canvas}` type. Four link columns (Watches, Brand, Service, Legal) use `{typography.caption}` at modest vertical spacing. The Glashütte address block renders in `{colors.muted}`, signaling that it is present for compliance, not hierarchy. No top border — the transition from page body to footer is marked solely by the background reversal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column collection grid; nav collapses to hamburger with full-screen overlay; configurator stacks below product image; hero becomes full-bleed portrait crop |
| Tablet | 744–1128px | Two-column collection grid; nav retains top bar but drops sub-labels; configurator remains two-column at wider tablet sizes |
| Desktop | 1128–1440px | Three-column collection grid; full flyout navigation; two-column configurator lockup; editorial pull quotes constrained to 60% page width |
| Wide | > 1440px | Max-width container (~1440px) centered with extended whitespace gutters; hero image gains subtle parallax offset |

### Touch Targets

- All interactive elements minimum 44×44px
- Configurator chips enforce 44px height with `{spacing.base}` horizontal padding
- Mobile nav items expand to full-width rows with 48px tap height
- Footer links padded to 40px tap height despite smaller caption type

### Collapsing Strategy

- Primary nav: hamburger icon below 744px; reveals full-screen overlay with collection links and a featured watch image
- Product grid: 3-col → 2-col → 1-col as viewport narrows through breakpoints
- Configurator: side-by-side at ≥ 1128px; stacked (image above, selectors below) below 1128px
- Footer columns: 4-col → 2-col → 1-col with accordion collapse at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `primary-active` and `primary-disabled` hex values are derived — exact design-system tokens not extractable from live CSS
- Hover-state colors for buttons and text links not captured; values estimated from lightness shifts on primary
- Font weight range for Gotham Narrow not confirmed; whether Light (100/200) and Book (400) are both loaded is unknown
- Nav flyout animation duration and easing curve not captured
- Configurator dial preview behavior (live-render vs. static image swap on selection) not confirmed
- Exact grid gutter values per breakpoint not extracted
- Checkout and account-area flows not crawled; form field error states in those contexts unknown
- `interstate_gravur_v01regular` placement is inferred from font-stack presence; all specific usage contexts may not be captured
- Dark-mode or alternate theme variants not detected, but may exist for campaign landing pages
