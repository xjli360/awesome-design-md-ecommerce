---
version: alpha
name: "Accu-Scope"
source_url: "https://www.accu-scope.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Poppins at weight 600 carries model names and category headers with the same stroke-width consistency you'd want in a well-calibrated reticle — geometric, unambiguous, impossible to misread at small sizes on a product comparison grid. The palette is a three-tier blue architecture: #1863dc operates as the sovereign primary across CTAs, active nav states, and section accent rules; #02609b (`{colors.ocean}`) deepens link hover and dropdown contexts; #003388 (`{colors.navy}`) brackets the composition by anchoring both the hero overlay and the footer, giving each page a clear open-and-close in institutional navy. Canvas holds at #fdfdfd rather than full white, reducing eye fatigue on catalog pages dense with specification text and accessory matrices. The only warm interruption in the cool blue-and-slate system is #fac917 (`{colors.accent-gold}`), reserved for promotional ribbons and sale callout badges — just enough warmth to mark a price event without softening the scientific credibility of the surrounding interface. Button corners sit at 4px (`{rounded.xs}`), a deliberate rejection of pill geometries; the tight radius signals precision-instrument discipline appropriate for a company whose product tolerances are measured in microns. Monospace Courier appears only inside model-code chips and technical specification rows, drawing a legible boundary between marketing copy set in Poppins and the part-number or objective-specification data beneath — two typographic registers that serve entirely different reading modes. Gray infrastructure runs through five stops — hairlines at #d5d5d5, mid-surfaces at #ebebeb, soft fills at #f4f4f4, near-white card fills at #f8f8f8, and body text at #404040 — distributing catalog density across compound, stereo, digital, and fluorescence microscope lines without grid collapse. Footer text links step down to #abb8c3 (`{colors.footer-link}`), a cool slate that bridges the navy background and on-primary white without introducing a third accent temperature. FontAwesome handles all interactive icons, standardizing the interaction vocabulary across the WooCommerce-based catalog and eliminating custom SVG maintenance overhead.

colors:
  primary: "#1863dc"
  primary-hover: "#0056a7"
  primary-active: "#003388"
  primary-disabled: "#abb8c3"
  ocean: "#02609b"
  navy: "#003388"
  ink: "#1a1a1a"
  body: "#404040"
  muted: "#6d6d6d"
  muted-soft: "#747474"
  hairline: "#d5d5d5"
  hairline-soft: "#eeeeee"
  canvas: "#fdfdfd"
  surface-soft: "#f4f4f4"
  surface-card: "#f8f8f8"
  surface-mid: "#ebebeb"
  on-primary: "#ffffff"
  accent-gold: "#fac917"
  footer-link: "#abb8c3"
  error: "#cf2e2e"

typography:
  display-xl:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  spec-label:
    fontFamily: "'Courier', 'Courier 10 Pitch', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.5px
  model-code:
    fontFamily: "'Courier', 'Courier 10 Pitch', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.8px

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
    padding: 12px 28px
    height: 44px
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
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-hover}"
    border: "1px solid {colors.primary-hover}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocused: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocused: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 68px
    borderBottom: "1px solid {colors.hairline}"
    linkHoverColor: "{colors.primary}"
    linkActiveColor: "{colors.primary}"
    linkActiveWeight: 600
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.title-md}"
    priceColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 16px
    imageBackground: "{colors.canvas}"
    imageRounded: "{rounded.xs}"
  hero:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    overlayColor: "{colors.navy}"
    overlayOpacity: 0.6
    padding: 64px 48px
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
  category-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  sale-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
    fontWeight: 700
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.title-sm}"
    headerTextColor: "{colors.ink}"
    cellTypography: "{typography.spec-label}"
    cellTextColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    alternateRowBackground: "{colors.surface-soft}"
    padding: 10px 16px
  model-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ocean}"
    typography: "{typography.model-code}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    linkHoverColor: "{colors.primary}"
  section-header:
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    accentBorderLeft: "3px solid {colors.primary}"
    paddingLeft: 12px
    marginBottom: 24px
  filter-sidebar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    headingTypography: "{typography.title-sm}"
    checkboxAccentColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.footer-link}"
    linkHoverColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingTextColor: "{colors.on-primary}"
    padding: 48px 64px
    borderTop: "3px solid {colors.primary}"
  alert-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderLeft: "4px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 12px 16px
  pagination:
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackground: "{colors.canvas}"
    inactiveTextColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    height: 36px
    width: 36px

## Components

### Buttons

**`button-primary`** — The royal-blue `#1863dc` fill with `{rounded.xs}` 4px corners is the primary purchase action, used for "Add to Cart," "Request a Quote," and "Buy Now." Hover transitions to `{colors.primary-hover}` (#0056a7); active state presses to `{colors.primary-active}` (#003388). Disabled state applies `{colors.primary-disabled}` (#abb8c3) fill and removes pointer events.

**`button-secondary`** — A white-fill, `{colors.primary}`-bordered outline button at the same 44px height as primary, used for "View Details," "Download PDF," and "Compare." Hover shifts both border and text to `{colors.primary-hover}` and fills with `{colors.surface-soft}` to signal readiness without competing with primary CTAs. Never used directly adjacent to primary on the same row — the two button types always have contextual separation.

**`button-ghost`** — Plain text link treatment in `{colors.primary}` with an underline, no background, no border. Reserved for secondary navigational actions in product cards (e.g., "View Accessories," "See All Models") where a bordered button would overcrowd the grid cell.

### Text Input & Search

**`text-input`** — A 42px-tall `{rounded.xs}` field with a `{colors.hairline}` 1px border that upgrades to 2px `{colors.primary}` on focus, providing clear keyboard-navigation feedback in catalog filter panels. Placeholder text renders in `{colors.muted}` Poppins 15px; typed input in `{colors.ink}` at the same scale.

**`search-bar`** — Slightly taller at 44px with `{rounded.sm}` corners (8px), used in the site-wide header. A FontAwesome search glyph in `{colors.muted}` sits left-inset; on focus, the border animates to 2px `{colors.primary}`. Predictive results drop in a `{colors.canvas}` panel with `{colors.hairline}` separators, `{typography.body-sm}` type, and `{rounded.sm}` card rounding.

### Navigation

**`nav-bar`** — A `{colors.canvas}` bar at 68px height, separated from page content by a single `{colors.hairline}` bottom border. Navigation links run in `{typography.nav-link}` Poppins 14px weight 500; active link and hover states shift to `{colors.primary}` with no underline or background fill. The logo and primary CTA button anchor left and right respectively, keeping the microscope category links centered at moderate viewport widths.

### Product Card

**`product-card`** — A `{colors.surface-card}` (#f8f8f8) fill with a `{colors.hairline}` 1px border and `{rounded.sm}` 8px corner radius. The product image occupies the top portion against a `{colors.canvas}` background, isolating the instrument against a clean white; below, `{typography.title-sm}` Poppins 600 carries the model name, `{typography.body-sm}` describes the use case in one line, and price in `{typography.title-md}` renders in `{colors.primary}` to draw the eye. A `{category-badge}` chip overlays the image top-left when a new model designation applies, and a `{sale-badge}` in `{colors.accent-gold}` (#fac917) overlays when a sale price is active.

### Hero

**`hero`** — A full-width banner with a `{colors.navy}` (#003388) overlay at 60% opacity over product photography, establishing the institutional authority that dominates the top of department and homepage views. Headline copy renders in `{typography.display-xl}` Poppins 700 white, subhead in `{typography.body-md}` white at reduced opacity (85%), and the primary CTA button sits beneath with a `{colors.primary}` fill — the one blue-on-navy moment that works because #1863dc is bright enough to clear against the dark navy base.

### Badges

**`category-badge`** — A compact `{colors.primary}` (#1863dc) pill with white `{typography.caption}` 12px text and `{rounded.xs}` corners, applied directly over product images to mark microscope category ("Compound," "Stereo," "Digital"). Never stacked more than one per image card.

**`sale-badge`** — Identical geometry to `{category-badge}` but filled with `{colors.accent-gold}` (#fac917) and inked in `{colors.ink}` at weight 700 — the only moment warm color enters the palette. Appears exclusively on cards with a price reduction and functions as a visual temperature interrupt to route eyes through the catalog grid.

### Spec Table

**`spec-table`** — The workhorse component for objective configuration, magnification ranges, illumination types, and accessory compatibility. Headers in `{colors.surface-soft}` with `{typography.title-sm}` Poppins 600; data cells in `{typography.spec-label}` Courier monospace at 12px, 0.5px letter-spacing — creating a readable instrument-datasheet register distinct from surrounding marketing copy. Alternating rows use `{colors.surface-soft}` to segment dense multi-row comparisons without heavy borders.

### Model Chip

**`model-chip`** — An inline `{colors.surface-soft}` chip with `{colors.ocean}` (#02609b) text in `{typography.model-code}` Courier, a `{colors.hairline}` 1px border, and `{rounded.xs}` corners. Used inline within product titles and breadcrumbs to surface part numbers (e.g., "EXC-400") without breaking reading flow. The ocean color links these chips visually to the primary blue family while distinguishing them from clickable `{colors.primary}` elements.

### Breadcrumb

**`breadcrumb`** — `{typography.caption}` Poppins 12px in `{colors.muted}` (#6d6d6d), with FontAwesome chevron separators in `{colors.hairline}`. The active (current page) crumb renders in `{colors.ink}` at the same size — no bold, no color change beyond darkening. Links hover to `{colors.primary}`.

### Filter Sidebar

**`filter-sidebar`** — A `{colors.surface-soft}` panel with `{rounded.sm}` rounding and a `{colors.hairline}` border, holding category checkboxes, price range inputs, and application-use toggles. Section headings in `{typography.title-sm}`; filter labels in `{typography.body-sm}`. Checkbox accent renders in `{colors.primary}` — the one brand-blue touch inside an otherwise neutral utility panel.

### Section Header

**`section-header`** — A left `{colors.primary}` 3px vertical accent rule at 12px left padding separates major catalog sections ("Featured Microscopes," "By Application," "New Arrivals") from body content. Heading in `{typography.display-sm}` Poppins 600 `{colors.ink}`, 24px bottom margin before the grid starts.

### Alert Banner

**`alert-banner`** — A `{colors.surface-soft}` strip with a 4px `{colors.primary}` left border and no rounding, spanning the content column. Used for shipping lead-time notices and product availability updates. Body text in `{typography.body-sm}` `{colors.ink}`.

### Footer

**`footer`** — The `{colors.navy}` (#003388) fill with a 3px `{colors.primary}` top border creates a clear page-end bracket. Column headings in `{typography.title-sm}` Poppins 600 white; body links in `{typography.body-sm}` at `{colors.footer-link}` (#abb8c3), upgrading to white on hover. Bottom strip carries copyright and legal links at `{typography.caption}` scale against the same navy background.

### Pagination

**`pagination`** — Square 36×36 chips with `{rounded.xs}` corners; active page fills `{colors.primary}` with white `{typography.button-sm}` numeral; inactive pages are `{colors.canvas}` with a `{colors.hairline}` border and `{colors.body}` text. Prev/Next controls use FontAwesome chevrons at the same chip height.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav bar collapses to hamburger + logo; search expands to full-width strip; hero headline steps down from display-xl (36px) to display-md (28px); filter sidebar becomes a bottom-sheet drawer; spec tables scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; top nav shows logo + search + hamburger; hero at full height with reduced padding (32px vertical); filter sidebar collapses to horizontal chip strip above the grid |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with all category links visible; filter sidebar as persistent left panel; spec tables fully visible without scroll |
| Wide | > 1440px | Max content width capped at 1400px with auto side margins; four-column grid on category landing pages; hero image expands edge-to-edge behind fixed max-width text overlay |

### Touch Targets

- All buttons minimum 44px tall on mobile
- Pagination chips expand to 44×44px on touch viewports
- Category filter checkboxes minimum 44px tap target via padding extension
- Nav hamburger icon 44×44px hit area
- Product card entire surface is a link target on mobile, not just the title text

### Collapsing Strategy

- Primary nav: logo + search + cart icon remain; category links move to hamburger drawer at < 1128px
- Filter sidebar: collapses to horizontal scrollable chip row at < 1128px; moves into a bottom-sheet modal at < 744px
- Spec table: horizontal scroll container at < 744px with sticky first column (specification name) for readability
- Hero subhead: hidden on mobile viewports < 414px to reduce vertical hero height
- Footer columns: four-column layout stacks to two columns at tablet, single column at mobile with accordion-style section expand

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `#7f54b3` (WooCommerce purple) and `#f78da7` (pink) appear in extraction but are almost certainly WordPress Gutenberg block editor palette entries, not brand assets — excluded from tokens
- `#cf2e2e` similarly is a Gutenberg default red; included only as `{colors.error}` since error-red semantics are plausible regardless of origin
- Exact Poppins weight and size used for product category mega-menu items not confirmed — inferred from nav-link scale
- Animation timing and easing curves (hover transitions, drawer open) not extractable from static scrape
- Whether Poppins loads from Google Fonts CDN or is self-hosted — cannot determine from extraction
- Mobile-specific type scale overrides not confirmed; all mobile sizes are inferred reductions
- Exact spacing grid inside the comparison table component (column widths, min-widths) not extracted
- Hero imagery art direction (product photography vs lifestyle vs illustrated diagrams) not confirmed from static data
- Form validation states beyond error (warning, success) color assignments not confirmed
