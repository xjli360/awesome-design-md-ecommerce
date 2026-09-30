---
version: alpha
name: "Maingear"
source_url: "https://www.maingearpc.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A void-black viewport forces a single spectral slash of red — #e5222a — to carry every interactive decision on the page, and that constraint defines everything downstream. Pre-built gaming towers and custom-configured rigs are photographed against negative space so complete that the chassis geometry reads like industrial sculpture rather than retail merchandise. Display type runs wide, condensed, and heavy — suggesting the typographic tradition of motorsport and aerospace spec sheets rather than the rounded, approachable geometry of consumer electronics — and model names like "VYBE", "RUSH", and "ELEMENT" appear at display-xl scale functioning closer to part numbers than marketing headlines. Hard corners ({rounded.none}) appear everywhere structural: build-config tables, spec cells, hero staging, form fields. Only logistics badges — "IN STOCK", "SHIPS TODAY" — earn a modest {rounded.xs} to signal their secondary, informational status.

  The canvas resolves to near-void (#0d0d0d) rather than white, making the site feel more like a configuration terminal than a storefront. Spacing is technically dense: spec rows breathe at tight {spacing.sm}–{spacing.md} rhythm while section breaks open to {spacing.section} gulfs that let chassis photography assert itself. CTA buttons are flat, wide, and uppercase — the interaction language of BIOS screens and control panels — never the pill-shaped softness of D2C consumer goods. Secondary buttons invert to transparent with a red border so the dark field bleeds through, reinforcing depth rather than surface as Maingear's native medium. The accent (#e5222a) appears at full saturation only on interactive elements and active states — never diluted to a tint, never used as a fill — which keeps its signal value intact against an environment with almost no competing brightness.

  Below the hero, commerce converts to a near-technical register: spec badges cluster in rows of four to six chips, each stamping GPU, RAM, and storage values in a monospace-adjacent face. The configurator panel — CPU tier, GPU family, RAM density, storage — operates like a structured form rather than a guided wizard, with active selections marked by a border upgrade from hairline gray to primary red rather than a checkbox glyph or highlight fill. The footer condenses every product line, configurator entry point, warranty clause, and social handle into a dense dark grid, treating discovery as a technical index rather than a brand narrative.

colors:
  primary: "#e5222a"
  primary-active: "#c01820"
  primary-disabled: "#7a1014"
  primary-ghost-border: "#e5222a"
  ink: "#ffffff"
  body: "#cccccc"
  muted: "#888888"
  hairline: "#2e2e2e"
  canvas: "#0d0d0d"
  surface-soft: "#141414"
  surface-card: "#1a1a1a"
  surface-raised: "#222222"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  badge-stock: "#1a7a2e"
  badge-stock-text: "#ffffff"
  badge-sale: "#e5222a"
  badge-sale-text: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Barlow Condensed', 'Oswald', Arial Narrow, sans-serif"
    fontSize: 72px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -2px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Barlow Condensed', 'Oswald', Arial Narrow, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Barlow Condensed', 'Oswald', Arial Narrow, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
    textTransform: uppercase
  title-md:
    fontFamily: "'Barlow', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Barlow', 'Open Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  body-md:
    fontFamily: "'Barlow', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Barlow', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-mono:
    fontFamily: "'IBM Plex Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Barlow Condensed', 'Barlow', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Barlow Condensed', 'Barlow', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Barlow', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  price-display:
    fontFamily: "'Barlow Condensed', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px

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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    opacity: 0.5
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary-ghost-border}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    subTextColor: "{colors.muted}"
    typography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    imageAspect: "4/3"
  product-card-hover:
    border: "1px solid {colors.primary}"
    backgroundColor: "{colors.surface-card}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    overlayGradient: "linear-gradient(90deg, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.3) 60%, transparent 100%)"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    paddingY: "{spacing.section}"
    minHeight: 560px
  spec-badge:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.body}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.spec-mono}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  stock-badge:
    backgroundColor: "{colors.badge-stock}"
    textColor: "{colors.badge-stock-text}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  sale-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.badge-sale-text}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  config-table:
    backgroundColor: "{colors.surface-soft}"
    rowBorderColor: "{colors.hairline}"
    labelTypography: "{typography.body-sm}"
    valueTypography: "{typography.spec-mono}"
    accentRowBorderLeft: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  configurator-panel:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    height: 40px
    textAlign: center
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    activeBorderBottom: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Flat, zero-radius red (#e5222a) slab with all-caps condensed lettering at 1.5px tracking. On hover it transitions to `primary-active` (#c01820) with no easing delay — the interaction pattern mimics a physical key press rather than a soft UI affordance. Disabled state uses `primary-disabled` at half opacity, ensuring it reads as deliberately inactive rather than accidentally invisible against the dark canvas. Width typically locks to a fixed value (180–220px) rather than shrinking to content, giving CTA rows visual weight parity across product cards.

**`button-secondary`** — Transparent fill with a 1px `primary-ghost-border` red edge and white uppercase label; the dark canvas bleeds through, giving the button a bordered-void look. On hover, `surface-soft` fills in — just enough brightness shift to confirm the state without breaking the dark-field illusion. Used paired alongside `button-primary` in hero and product detail layouts, always at the same height (48px) so the two buttons optically match.

**`button-ghost`** — Hairline-bordered utility button with `muted` text; used for tertiary actions like "Compare" or "Add to Wishlist" on product cards where the primary CTA is already present. Never uses red — keeps the accent reserved for decisive, transactional moments.

### Text Input

**`text-input`** — Near-black fill (`surface-soft`) with a 1px `hairline` border and zero border-radius that extends the angular design language from buttons into form fields. Focus replaces the border color with `primary` red rather than adding an outer glow, maintaining the flat surface read. Placeholder text sits in `muted` (#888888) against the dark fill; typed text in `ink` (#ffffff) creates an immediate, high-contrast confirmation of input.

### Navigation

**`nav-bar`** — 64px dark bar flush with the `canvas`; product categories ("DESKTOPS", "LAPTOPS", "CUSTOMIZE", "ACCESSORIES") at `nav-link` weight with no persistent underline — hover triggers a bottom border in `primary` red. Logo anchors the left; cart, search, and account icons cluster right as SVG glyphs. On scroll past the hero, a 1px `hairline` bottom border separates the bar from the page surface below it.

**`nav-dropdown`** — Dark panel (`surface-card`, 1px `hairline` border, no rounding) that opens below the nav on category hover. Product sub-lines and featured pre-built systems appear in a two-column grid with small preview images. No drop shadow — the panel edge defines the boundary against the dark background.

### Product Card

**`product-card`** — Dark card (`surface-card`, 1px `hairline` border) that upgrades its border to 1px `primary` red on hover. Product image fills the upper 4:3 zone; model name at `title-sm`, price at `price-display` (28px condensed), and a `button-primary` CTA anchor the lower section. `stock-badge` and `sale-badge` chips overlay the image at top-left corner at `caption` scale. Zero border-radius throughout; the card reads as a panel from a dashboard, not a marketplace tile.

### Hero

**`hero`** — Full-bleed chassis photography with a left-anchored gradient scrim (`rgba(0,0,0,0.85)` fading to transparent at 60%) that ensures headline legibility without boxing the image. Model name in `display-xl` (72px, uppercase, −2px tracking) and a single `button-primary` CTA sit in the left column at `section` vertical padding. Background position anchors the chassis at center-right so the product occupies the unobscured right half of the frame. Minimum height 560px; expands to 640px on wide viewports.

### Spec Badge

**`spec-badge`** — Small horizontal chip (`surface-raised`, 1px `hairline` border, zero radius) with a `caption` label above a `spec-mono` value. Used in clusters of four to six across product card footers and product detail pages — GPU model, RAM size, storage type, display spec — giving at-a-glance hardware comparison without requiring the user to open a full spec sheet. Chips wrap to two rows on card widths below 280px.

### Configurator Panel

**`configurator-panel`** — The commerce core of the Maingear experience; each hardware tier (CPU, GPU, RAM, storage, cooling, OS) gets a card panel with a `title-md` section header and a list of radio-style option rows. Active selection upgrades the panel border from 1px `hairline` to 1px `primary` red. Option rows show the part name at `body-sm` and the price delta (e.g. "+$200") at `body-sm` `muted` — the configurator reads as a structured technical form, not a guided wizard.

### Config Table

**`config-table`** — Striped two-column spec readout used in product detail summaries and comparison views. Label column in `body-sm` at `muted` color; value column in `spec-mono` for character-level alignment across rows. The currently highlighted row gets a 2px left-side border in `primary` — a single column of red in an otherwise monochrome table, functioning like a cursor indicator.

### Promo Banner

**`promo-banner`** — Full-width 40px red strip pinned above the nav bar for time-sensitive messaging ("FREE SHIPPING OVER $99", "LABOR DAY SALE — UP TO $400 OFF"). Typography at `button-sm` uppercase. No close affordance — the banner is editorial broadcast, not a dismissible notification. On mobile it wraps to two lines and grows height to fit.

### Category Tab

**`category-tab`** — Horizontal tab strip used to filter product listings by tier ("ALL", "ENTRY", "MID-RANGE", "ENTHUSIAST", "ULTIMATE"). Active state: `ink` white text plus a 2px `primary` bottom border. Inactive: `muted` text, no border. No background fill change on any state — the active indicator is purely the bottom edge, consistent with the flat-surface design language.

### Footer

**`footer`** — Four-column dark grid (`surface-soft`, 1px `hairline` top border) with `caption` heading labels and `body-sm` link lists. Social icons appear beneath the last column or in a dedicated fifth column. Copyright and legal links run at `body-sm` in `muted` along the bottom edge. No decorative graphics or gradients — the footer is a technical index, not a brand story closer.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero headline drops to `display-md` (32px); nav collapses to hamburger with slide-out drawer; product cards stack full-width; configurator panels become accordion rows; spec badges reduce to 3 chips |
| Tablet | 744–1128px | Two-column product grid; hero maintains left-text / right-image split with tighter padding; top nav shows primary categories only, secondary nav in drawer; configurator panels stack vertically |
| Desktop | 1128–1440px | Three-column product grid; configurator splits into left-panel options and right-panel sticky summary; full horizontal nav with dropdowns; `display-xl` headlines at full 72px |
| Wide | > 1440px | Content max-width caps at 1440px and centers; hero padding expands to `{spacing.section}` × 2; four-column product grid available for listing pages |

### Touch Targets

- All buttons and nav links maintain a minimum 44px tap height on mobile
- Configurator option rows expand to 52px tap height on touch devices to accommodate radio-style selection
- Product card CTA buttons span full card width on mobile for maximum tap area
- Spec badge chips maintain 36px min height on touch viewports with increased horizontal padding

### Collapsing Strategy

- Nav collapses to hamburger icon at < 744px; cart and search icons remain persistent in the top bar
- Promo banner wraps to two lines on mobile rather than hiding — logistics messaging is purchase-critical
- Config table collapses to single-column key → value rows with `{spacing.sm}` row gap; left accent border moves to a top accent border on mobile
- Spec badge clusters reduce from 6 chips to 4 on tablet, 3 on mobile (GPU, RAM, storage prioritized)
- Category tab strip becomes horizontally scrollable with soft fade mask at < 744px — no wrapping or line break

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All colors are brand-knowledge estimates; no hex values were extracted.** The site returned no color tokens from automated extraction (likely JS-rendered token system or anti-bot protection). Primary red (#e5222a) is based on widely visible Maingear brand assets and marketing materials; exact swatch must be verified against live CSS custom properties or official brand guidelines.
- **Font families not extracted.** No font-family stack was detected. Typography uses Barlow Condensed / Barlow as plausible replacements consistent with the condensed-display gaming aesthetic; actual typefaces may differ.
- **No meta theme-color tag detected.** Cannot confirm the canonical accent via this secondary signal.
- **No Shopify platform confirmed.** Commerce infrastructure (cart, configurator, checkout) may involve custom or headless implementation; component states here model surface appearance only, not checkout or compatibility validation logic.
- **Configurator flow depth unknown.** Maingear's custom PC builder involves multi-step compatibility checking; the `configurator-panel` component models visual states only, not conflict UX, part availability gates, or price recalculation behavior.
- **Dark-mode assumption unverified.** Always-dark treatment assumed based on category norms; a light-mode or adaptive-mode variant may exist and was not confirmed or ruled out by extraction.
- **Icon set, illustration style, and animation timings** could not be characterized from extraction data.
