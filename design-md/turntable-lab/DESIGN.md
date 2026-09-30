---
version: alpha
name: "Turntable Lab"
source_url: "https://www.turntablelab.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Bebas Neue runs at full condensed compression across every display headline — a font borrowed from crate dividers and record-store signage — sitting on a near-black vinyl slab (#121212) that never lightens to true white on any primary surface. The electric cobalt #3245ff handles every interactive state: the add-to-cart button, hovered nav links, active filters. It reads against the dark canvas without softening, which gives the site a tension closer to a record sleeve than a boutique shop. The body font switches to Instrument Sans, a contemporary geometric that keeps the reading layer legible without fighting the display muscle overhead. A third axis — Inconsolata, a monospace slab — handles catalog metadata: track listings, stock codes, technical audio specs. Together the three-font system maps cleanly onto three modes of content: headline (Bebas Neue), editorial (Instrument Sans), data (Inconsolata). Buttons, cards, inputs, and section dividers carry `{rounded.none}` throughout — no softened corner anywhere, the same flat geometry as a record sleeve cut to dimension. The accent palette is unusually wide for an audio shop: amber #f7a504, red #de0f2b, purple #7f5fca, yellow #ffcb42, and a range of greens (#478947 through #02642f) are all present, functioning as genre color codes and inventory-status badges rather than brand expression. The light neutrals — #e3e4ec, #f0f0f0, #f7f7f7 — exist almost exclusively as text-on-dark surfaces or faint dividers, since the site lives primarily in dark mode. Spacing is generous in the catalog grid but tight inside product cards, squeezing maximum vinyl into a finite screen.

colors:
  primary: "#3245ff"
  primary-active: "#1a2ee0"
  primary-hover: "#4a5aff"
  primary-disabled: "#3245ff66"
  accent-amber: "#f7a504"
  accent-red: "#de0f2b"
  accent-purple: "#7f5fca"
  accent-yellow: "#ffcb42"
  accent-green: "#478947"
  accent-green-mid: "#0ea352"
  accent-green-bright: "#17c266"
  accent-green-deep: "#02642f"
  sale-red: "#d02f2e"
  ink: "#e3e4ec"
  ink-strong: "#f0f0f0"
  ink-muted: "#737373"
  body: "#d0d0d8"
  muted: "#4f4f4f"
  hairline: "#303030"
  hairline-soft: "#242424"
  canvas: "#121212"
  surface-soft: "#050505"
  surface-card: "#242424"
  surface-mid: "#303030"
  on-primary: "#ffffff"
  on-dark: "#f0f0f0"

typography:
  display-xl:
    fontFamily: "'Bebas Neue', Impact, 'Arial Narrow', sans-serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: 1px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Bebas Neue', Impact, 'Arial Narrow', sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Bebas Neue', Impact, 'Arial Narrow', sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.5px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Bebas Neue', Impact, 'Arial Narrow', sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.3px
    textTransform: uppercase
  title-md:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  catalog-meta:
    fontFamily: "'Inconsolata', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  catalog-label:
    fontFamily: "'Inconsolata', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Inconsolata', 'Courier New', monospace"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-lg:
    fontFamily: "'Inconsolata', 'Courier New', monospace"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  badge-label:
    fontFamily: "'Inconsolata', 'Courier New', monospace"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Bebas Neue', Impact, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Bebas Neue', Impact, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 10px
  xl: 16px
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
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink-strong}"
    border: "1px solid {colors.ink-muted}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    width: "100%"
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 40px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "none"
    height: 36px
    placeholderColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    imageAspectRatio: "1:1"
    gap: "{spacing.xs}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink-strong}"
  product-card-artist:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink-muted}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-meta:
    typography: "{typography.catalog-meta}"
    textColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-strong}"
    minHeight: 480px
    padding: "{spacing.xxl} {spacing.section}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink-strong}"
  hero-subhead:
    typography: "{typography.body-md}"
    textColor: "{colors.ink-muted}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink-strong}"
    borderBottom: "2px solid {colors.primary}"
    paddingBottom: "{spacing.sm}"
    marginBottom: "{spacing.lg}"
  genre-badge:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  sale-badge:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  in-stock-badge:
    backgroundColor: "{colors.accent-green-mid}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  pre-order-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "#000000"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  catalog-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.catalog-meta}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} {spacing.base}"
    hoverBackgroundColor: "{colors.surface-card}"
  catalog-row-id:
    typography: "{typography.catalog-label}"
    textColor: "{colors.ink-muted}"
    width: 80px
  catalog-row-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  filter-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.catalog-label}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    border: "1px solid {colors.hairline}"
  filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-heading:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink-strong}"

## Components

### Buttons
**`button-primary`** — A flat, zero-radius block button using Bebas Neue at 16px with 1.5px letter-spacing, background #3245ff on white text. The hard square corners are load-bearing: they echo the geometry of printed sleeve art and physical record formats, keeping the site's aesthetic coherent between the physical and digital. Hover shifts to #4a5aff, active state drops to #1a2ee0, and disabled renders at 40% opacity of the primary blue.

**`button-secondary`** — Transparent background with a 1px solid hairline border (#303030), Bebas Neue label in #e3e4ec. Hover fills with surface-card (#242424) to acknowledge the interaction without competing with primary actions. Used for secondary navigation triggers, "View All" shelf links, and format selectors.

**`add-to-cart`** — Full-width variant of the primary button at 48px height, always spanning the full product card width. This maximizes the tap target on mobile and creates a uniform grid register across catalog layouts. Shares all state variants with `button-primary`.

**`button-ghost`** — No background, no border, muted ink (#4f4f4f), Bebas Neue at 13px. Reserved for tertiary actions: "Remove from wishlist", "See all", inline footer links. Never used near primary CTAs to avoid dilution.

### Text Inputs
**`text-input`** — Zero-radius input on surface-card (#242424), 1px solid hairline border at rest. Focus state replaces the hairline with the primary #3245ff border, no box-shadow or glow. Placeholder text in muted (#4f4f4f). Height 40px matches the compact density of catalog rows.

**`nav-search`** — An abbreviated inline search field living in the top navigation bar. No visible border, surface-card background, Instrument Sans body-sm. Expands on focus; the Inconsolata typeface is applied to any autocomplete results to maintain the data-layer visual register.

### Navigation
**`nav-bar`** — 56px tall, canvas black (#121212) background with a 1px bottom border in #303030. Links use Instrument Sans 13px medium at default ink (#e3e4ec); the active category link fires in primary #3245ff. The site logo occupies the left anchor as a Bebas Neue wordmark. Right side houses search, cart icon, and account.

### Product Cards
**`product-card`** — Zero-radius cards on surface-card (#242424), 8px internal padding. The square product image bleeds to the card edges. Below the image: artist name in body-sm muted ink, album/product title in title-sm strong ink, catalog label and format in catalog-meta (Inconsolata), price in the price token (Inconsolata bold 16px). Badge overlays (genre, sale, new, in-stock) sit at the top-left corner of the image.

### Badge System
The badge system is the widest-palette element on the site, doubling as both genre tagging and inventory signaling. **`sale-badge`** fires in #d02f2e. **`new-badge`** uses primary #3245ff. **`in-stock-badge`** renders in #0ea352. **`pre-order-badge`** uses amber #f7a504 on black text for contrast. **`genre-badge`** uses surface-mid (#303030) with standard ink. All badges share Inconsolata uppercase at 10px with 1px letter-spacing and a 2px radius — the only rounded element in the system.

### Catalog Row
**`catalog-row`** — A list-mode alternative to the card grid, evoking a physical record bin index. Each row is full-width, separated by a hairline-soft divider (#242424). A catalog ID in Inconsolata uppercase occupies an 80px left gutter; artist and title follow in Instrument Sans; price sits right-aligned in the price token. Hover fills the row with surface-card (#242424). Useful for "New This Week" and staff-pick lists where album context matters more than imagery.

### Section Headers
**`section-header`** — Bebas Neue display-md (32px uppercase) in strong ink (#f0f0f0), with a 2px primary-blue underline rule (#3245ff) that extends to the container edge. This is the primary wayfinding element between catalog sections — New Arrivals, Staff Picks, Used, Gear — and the only place the primary blue appears as a decorative element rather than an interactive one.

### Filter Pills
**`filter-pill`** — Inconsolata uppercase catalog-label at 10px, surface-card background, 1px hairline border, 2px radius. Active state fills with primary #3245ff and drops the border. Used horizontally across format (LP / 12" / 7" / Cassette / CD), condition (New / Used), and genre filter rows above catalog grids.

### Hero
**`hero`** — Full-width dark canvas section at minimum 480px tall. The headline uses display-xl Bebas Neue (72px) in strong ink. Subheadline drops to Instrument Sans body-md at muted ink. The CTA uses the hero-cta variant at 14px/32px padding, matching the flat zero-radius block pattern throughout. Backgrounds alternate between near-black solid fills and full-bleed record sleeve imagery.

### Footer
**`footer`** — Surface-soft (#050505) background, a step darker than the canvas, with a single top hairline. Section headings use display-sm Bebas Neue (22px) in strong ink. Link columns use body-sm Instrument Sans at muted ink (#737373). Social icon links render as 32×32px zero-radius icon blocks with hairline borders.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column catalog grid; nav collapses to hamburger icon and fullscreen drawer; hero headline drops to display-lg (48px); filter pills scroll horizontally in a single row; add-to-cart always full-width |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories only, no secondary dropdowns; hero at display-xl with reduced vertical padding; catalog row mode hidden |
| Desktop | 1128–1440px | Four-column catalog grid; full nav with category dropdowns; hero at full display-xl; catalog row list-mode toggle available |
| Wide | > 1440px | Grid holds at four columns; max-width container centers at 1440px; outer gutters widen rather than adding more columns |

### Touch Targets
- All interactive buttons minimum 44px tall
- Filter pills pad to 44px height on mobile via increased vertical padding
- Product cards use the full card surface as a tap target, not just the title text
- Nav hamburger icon occupies a 44×44px touch zone
- Badge overlays on product images do not intercept card taps

### Collapsing Strategy
- Category nav collapses to a fullscreen slide-in drawer on mobile, triggered by a hamburger in the nav-bar
- Genre and format filter sidebar collapses to a bottom-sheet modal on mobile and tablet
- Catalog row list mode is hidden below 1128px; card grid is the only view on mobile and tablet
- Section headers reduce from display-md to display-sm (22px Bebas Neue) on mobile
- Footer columns stack to two on tablet, single column on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color was set; the dark canvas assumption (#121212) is inferred from the dominant extracted colors, not confirmed from a theme declaration
- Specific color-to-genre mappings are unknown — the accent palette (amber, red, purple, yellow, greens) is present in extraction but which hue maps to which genre or format type could not be determined
- Hover and focus states for nav links are estimated; primary #3245ff as the active/hover color is inferred from interactive-element context rather than directly observed
- Exact product grid column counts and gutter widths were not measured; four-column desktop assumption follows common vinyl shop patterns
- Icon library (format icons, turntable glyphs, genre pictograms, player controls) was not captured in extraction
- Animation timing for cart drawer, filter sheet, and hover transitions was not extracted
- Wishlist and comparison feature UI patterns, if any, are unknown
- Mobile nav drawer visual design (background, animation direction, close affordance) is unknown beyond the hamburger trigger
