---
version: alpha
name: "B&K Precision"
source_url: "https://www.bkprecision.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Amber needles on a dark panel — that is the visual logic threading through B&K Precision's digital language. The #f4b153 signal amber lifts against deep instrument teal (#325d75) the way a moving needle catches the eye against a dark bezel, and the pairing gives measurement product pages a legibility that polished B2B sites usually sacrifice for style. Typography falls back entirely to the operating system's monospace stack — Consolas, Menlo, Monaco, Courier New — an unselfconscious choice that reads, in context, as precision: specification tables, frequency ranges, and resistance tolerances rendered in the same fixed-width glyphs a lab notebook uses. Where marketing copy needs warmth, Georgia and Cambria carry the prose. Corner geometry is straight-cornered or barely radiused ({rounded.xs}), matching the physical form language of rack-mounted instruments and bench power supplies. Navigation sits in a dark #1f2937 shell that references instrument chassis rather than consumer SaaS chrome; product subcategory chips in muted #698796 act as secondary wayfinding without competing with the amber accent. Search is foregrounded — locating a specific model by specification is the dominant user job, and the search bar occupies the full utility row of the nav at desktop widths. Density sits higher than most electronics sites: more product links per viewport, a narrower vertical rhythm, data-forward cards that surface parameter ranges before lifestyle imagery. Hairlines at #e5e7eb separate catalog columns with the same economy a data sheet uses between rows. The site's overall refusal to adopt a custom display typeface is itself a design statement — engineers who trust instruments that don't waste material on ornamentation will trust a catalog that doesn't either.

colors:
  primary: "#2299dd"
  primary-active: "#1d4ed8"
  primary-disabled: "#698796"
  accent: "#f4b153"
  accent-active: "#c78f3a"
  accent-disabled: "#f4d4a1"
  precision-teal: "#325d75"
  teal-muted: "#698796"
  ink: "#111827"
  body: "#374151"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#e5e7eb"
  hairline-soft: "#f3f4f6"
  border: "#d1d5db"
  canvas: "#ffffff"
  surface-soft: "#f3f4f6"
  surface-card: "#ffffff"
  surface-dark: "#1f2937"
  on-primary: "#ffffff"
  on-accent: "#111827"
  on-dark: "#ffffff"
  data-blue: "#007df6"

typography:
  display-xl:
    fontFamily: "Georgia, Cambria, 'Times New Roman', Times, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, Cambria, 'Times New Roman', Times, serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "Georgia, Cambria, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  mono-data:
    fontFamily: "Consolas, 'Andale Mono', 'Courier New', Courier, Monaco, Menlo, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  mono-label:
    fontFamily: "Consolas, 'Andale Mono', 'Courier New', Courier, Monaco, Menlo, monospace"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.6px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  category-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
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
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 42px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.accent-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.precision-teal}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 42px
    border: "1.5px solid {colors.precision-teal}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: none
  button-teal:
    backgroundColor: "{colors.precision-teal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 42px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    typography: "{typography.body-sm}"
    focusBorderColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    height: 44px
    typography: "{typography.body-sm}"
    iconColor: "{colors.muted}"
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-bar-top:
    backgroundColor: "{colors.precision-teal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    subtitleTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBg: "{colors.surface-soft}"
    headerTextColor: "{colors.body}"
    headerTypography: "{typography.mono-label}"
    cellTypography: "{typography.mono-data}"
    cellTextColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rowAlternateBg: "{colors.surface-soft}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.teal-muted}"
    typography: "{typography.category-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
    border: "1px solid {colors.hairline}"
  category-chip-active:
    backgroundColor: "{colors.precision-teal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.category-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    accentColor: "{colors.accent}"
    minHeight: 360px
    padding: "{spacing.section} {spacing.xl}"
  model-badge:
    backgroundColor: "{colors.precision-teal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.mono-label}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  data-readout:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.accent}"
    typography: "{typography.mono-data}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.teal-muted}"
  product-page-sidebar:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.muted-soft}"
    headingColor: "{colors.on-dark}"
    headingTypography: "{typography.title-md}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.accent}"
    borderTopColor: "{colors.precision-teal}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Amber fill (`{colors.accent}` #f4b153) on a {rounded.xs} corner with dark `{colors.on-accent}` text at `{typography.button-md}`. The amber choice echoes analog instrument indicator lamps and meter needles rather than adopting the generic corporate blue used for links elsewhere on the page. Hover darkens to `{colors.accent-active}` (#c78f3a); disabled state drains to `{colors.accent-disabled}` to preserve the amber hue family without suggesting interactivity.

**`button-secondary`** — White `{colors.canvas}` fill with a 1.5px `{colors.precision-teal}` border and matching text. Holds the same {rounded.xs} geometry and 42px height as primary. Used for secondary actions on product detail pages: "Download Datasheet", "Add to Compare", "Request Quote".

**`button-ghost`** — Transparent background, `{colors.primary}` blue text, no border. Used inline in navigation dropdowns, table footers, and link-style CTAs embedded in body copy.

**`button-teal`** — Deep `{colors.precision-teal}` (#325d75) fill with `{colors.on-dark}` white text. Functions as a page-level secondary CTA distinct from the amber primary; typically reserved for "Contact Sales" and account-level actions in the nav utility bar.

### Text Input & Search

**`text-input`** — 1px `{colors.border}` outline, white `{colors.canvas}` fill, {rounded.xs} corner, 40px height. Focus ring transitions border to `{colors.primary}` blue with no fill shift — contrast comes from border color change alone. `{typography.body-sm}` in system sans-serif renders both label and value.

**`search-bar`** — Wider variant of the text input at 44px height with a leading magnifier icon in `{colors.muted}`. Given B&K's deep catalog spanning thousands of SKUs across fifteen-plus product families, search is the primary navigation mode; at desktop widths the bar spans the full utility strip of the nav bar.

### Navigation

**`nav-bar`** — Dark `{colors.surface-dark}` (#1f2937) main bar at 56px, `{typography.nav-link}` in `{colors.on-dark}` white. The dark chassis references the physical form of bench instruments rather than consumer SaaS chrome. A secondary utility strip `nav-bar-top` at 36px in `{colors.precision-teal}` carries account links, distributor locator, and region/language selector in `{typography.caption}`.

### Product Card

**`product-card`** — 1px `{colors.hairline}` border, {rounded.xs} corners, `{colors.surface-soft}` image well. A `model-badge` in teal renders the alphanumeric model number above the product title. Key specification ranges (e.g., "0–30 V / 0–5 A") render in `{typography.mono-data}` directly beneath the model name, giving the card data-sheet energy before the user clicks through. Primary CTA is a `button-primary` amber control anchored to the card bottom edge.

### Spec Table

**`spec-table`** — The most brand-characteristic component on B&K's site. Column headers use `{typography.mono-label}` (monospace, uppercase, letter-spaced) against `{colors.surface-soft}`; cell values use `{typography.mono-data}` in `{colors.ink}`. Alternating rows between white and `{colors.surface-soft}` provide scan-line legibility for long parameter lists. Renders measurement range, accuracy class, resolution, input impedance, and interface rows. Printed datasheets and on-screen spec tables share an intentionally unified visual grammar.

### Category Chip

**`category-chip`** — Small uppercase label in `{typography.category-label}`, `{colors.teal-muted}` text on `{colors.surface-soft}` with 1px `{colors.hairline}` border and {rounded.xs} corners. Active/selected state fills with `{colors.precision-teal}` and switches text to `{colors.on-dark}`. Used for product family filtering: Oscilloscopes, Power Supplies, Digital Multimeters, Calibrators, LCR Meters, etc.

### Hero Banner

**`hero-banner`** — Full-width `{colors.surface-dark}` panel with `{typography.display-xl}` headline in `{colors.on-dark}` white. Accent rule or inline callout text in `{colors.accent}` amber. Product photography sits right-aligned, typically showing instrument front panels lit to reveal amber LED readouts — reinforcing the signal-amber color language in literal context. Minimum 360px height with `{spacing.section}` vertical padding.

### Data Readout

**`data-readout`** — A dark `{colors.surface-dark}` cell with `{colors.accent}` amber `{typography.mono-data}` text, mimicking an instrument LED or LCD display. Used on product detail pages to show representative measurement values (e.g., "0.000 V", "±0.05%", "20 MHz"). Thin 1px `{colors.teal-muted}` border. The component is purely decorative/illustrative — it does not receive user input.

### Model Badge

**`model-badge`** — Zero-radius (`{rounded.none}`) rectangle in `{colors.precision-teal}` with `{colors.on-dark}` `{typography.mono-label}` text. Renders the alphanumeric model identifier (e.g., "BK1685B", "2831E") above the product title in cards and search results. The hard corner mirrors the mechanical aesthetic of instrument labeling.

### Footer

**`footer`** — `{colors.surface-dark}` fill with a `{colors.precision-teal}` top border as a structural rule. Section headings in `{typography.title-md}` `{colors.on-dark}`; links in `{typography.body-sm}` `{colors.muted-soft}` that brightens to `{colors.accent}` amber on hover. Columns cover: Products, Support & Downloads, Company, and Distributors / Where to Buy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen drawer over `{colors.surface-dark}`; search bar full-width below nav strip; spec tables scroll horizontally with sticky first column; hero reduces to 240px min-height; category chips hidden behind "Filter" toggle |
| Tablet | 744–1128px | 2-column product grid; top utility bar collapses to icon-only; category chip row scrolls horizontally as a strip; product detail sidebar moves below the image gallery |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with mega-menu dropdowns; product detail uses 2-column layout (images left, specs and CTA right); spec table fully visible without scroll |
| Wide | > 1440px | Max content width ~1320px centered with auto margins; hero image scales with right-aligned product art; section padding expands via `{spacing.section}`; product grid stays at 4 columns |

### Touch Targets

- Minimum 44×44px on all interactive controls at mobile widths
- Category chips expand to `{spacing.sm}` vertical padding on mobile to meet tap target height
- `model-badge` tap target extended via parent card hit area — badge itself renders at its natural height
- Nav drawer links minimum 48px row height with full-width tap region
- Spec table row height increased to 44px on touch viewports for accessible row selection

### Collapsing Strategy

- Mega-menu dropdowns → full-screen overlay drawer at < 1128px
- Product subcategory chip row → horizontal scroll strip at tablet; "Filter" toggle accordion at mobile
- Spec table → horizontal scroll with sticky first column (parameter name) at < 744px
- Product detail sidebar (datasheet downloads, accessories, related models) → accordion below product images at mobile
- Top utility bar (account, distributor, region) → icon-only at tablet, folds into nav drawer at mobile
- Footer columns → single accordion stack at mobile, 2-column grid at tablet

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom web font detected — the entire extracted font stack is system monospace (Consolas, Menlo, Monaco, Courier New, Andale Mono) and system serif (Georgia, Cambria). May indicate fonts load via JavaScript after extraction, or that the site deliberately uses system fonts. No brand typeface can be confirmed.
- No `theme-color` meta tag present; the brand blue between `#2299dd` and `#2563eb` is ambiguous — `#2299dd` appears to be a custom brand value while `#2563eb` is stock Tailwind blue-600.
- The extracted palette contains many Tailwind CSS framework defaults (#6b7280, #9ca3af, #e5e7eb, #374151, #4b5563, #6366f1, #4f46e5, #c7d2fe, #1e3a8a) — actual custom brand tokens may be a smaller subset of the full list.
- Non-Shopify site with no e-commerce UI evidence in extraction; cart, checkout, pricing display, and quantity-selector components cannot be specified.
- Dark mode tokens not observed; site appears to operate as light-mode only.
- Exact mega-menu structure, product family taxonomy depth, and subcategory labeling not derivable from color/font hints alone.
- Animation timing, easing curves, and transition durations not available from static extraction.
- Icon set (product category glyphs, UI icons) not identifiable from extraction.
