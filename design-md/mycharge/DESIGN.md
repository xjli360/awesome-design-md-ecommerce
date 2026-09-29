---
version: alpha
name: "MyCharge"
source_url: "https://www.mycharge.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Electric cyan (#32b6f3) pulses through MyCharge's interface like a charging indicator hitting 100% — every primary CTA, product badge, and feature icon carries that vivid energy signature against a deep navy canvas (#2a3048) that doubles as the meta theme-color and hero backdrop. The typographic system pairs CocoSharp for display headlines — geometric, squared-off letterforms that mirror the hard edges of a power bank housing — with Figtree as the workhorse body face, its open counters and generous x-height keeping spec tables and mAh ratings scannable at `{typography.body-sm}`. Product cards sit on near-white surfaces (`{colors.surface-card}`) with `{rounded.md}` corners, giving each portable charger its own clean pedestal while mint-green badges (`{colors.accent-mint}`) flag "fully charged" states and pale yellow callouts (`{colors.accent-yellow}`) mark limited-time bundles. Navigation lives in that navy band at 64px height, white type at `{typography.nav-link}` weight 600, with the logo wordmark set in Futura-Book at a deliberate tracking that separates "my" from "Charge" without a visible space. Buttons are decisive — `{rounded.sm}` rectangles, never pills — sized at 48px height with 14px vertical padding, communicating the same no-nonsense industrial confidence as the products themselves. The spacing system breathes at `{spacing.lg}` between content blocks and `{spacing.section}` above fold breaks, preventing the dense technical specifications (watt-hours, port counts, cable types) from overwhelming the visual hierarchy. A secondary blue (#48a0e0) appears in hover states and informational icons, while the near-black ink (#121212) grounds long-form copy. The overall impression is a hardware brand that borrowed its palette from the glow of lithium cells — cool, saturated, unapologetically technical.

colors:
  primary: "#32b6f3"
  primary-active: "#00afec"
  primary-disabled: "#609edb"
  navy: "#2a3048"
  navy-light: "#54575a"
  ink: "#121212"
  body: "#303030"
  muted: "#616161"
  muted-soft: "#8a8a8a"
  hairline: "#dedede"
  hairline-soft: "#f1f1f1"
  border-mid: "#adb2b6"
  canvas: "#fefefe"
  surface-soft: "#f3f3f3"
  surface-card: "#fefefe"
  surface-dark: "#171717"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-navy: "#ffffff"
  accent-mint: "#cdfee1"
  accent-yellow: "#ffef9d"
  accent-yellow-dark: "#4f4700"
  success: "#24b263"
  success-deep: "#29845a"
  mid-blue: "#48a0e0"
  lavender: "#ebe9f1"

typography:
  display-xl:
    fontFamily: "'CocoSharp', 'Futura-Book', -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'CocoSharp', 'Futura-Book', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'CocoSharp', 'Futura-Book', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'CocoSharp', 'Futura-Book', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Figtree', 'CocoSharp', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', 'CocoSharp', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'CocoSharp', 'Figtree', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'CocoSharp', 'Figtree', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-value:
    fontFamily: "'CocoSharp', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  logo:
    fontFamily: "'Futura-Book', 'CocoSharp', sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 1.5px

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
  hero: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.ink}
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-navy:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 18px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.primary}
  text-input-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.navy-light}
    focusBorder: 1px solid {colors.primary}
  nav-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 {spacing.xl}
  nav-bar-scrolled:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.nav-link}"
    height: 56px
    boxShadow: 0 2px 8px rgba(0,0,0,0.15)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: 0 1px 4px rgba(0,0,0,0.06)
    hoverBoxShadow: 0 4px 16px rgba(0,0,0,0.1)
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    aspectRatio: 1 / 1
    padding: "{spacing.lg}"
  hero-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.display-xl}"
    padding: "{spacing.hero} {spacing.xl}"
    minHeight: 520px
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.hero} {spacing.xl}"
    minHeight: 480px
  spec-badge:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.success-deep}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  spec-badge-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.accent-yellow-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  spec-stat:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  charging-indicator:
    backgroundColor: "{colors.surface-dark}"
    fillColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 8px
  feature-icon-circle:
    backgroundColor: "{colors.lavender}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 56px
    width: 56px
  comparison-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    border: 1px solid {colors.hairline}
    cellPadding: "{spacing.md} {spacing.base}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.mid-blue}"
    padding: "{spacing.section} {spacing.xl}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    padding: 0 {spacing.base}
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    boxShadow: 0 8px 32px rgba(0,0,0,0.12)
    padding: "{spacing.lg}"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    separatorColor: "{colors.border-mid}"

---

## Components

### Buttons

**`button-primary`** — Electric cyan (#32b6f3) fill with white text set in CocoSharp 600 weight at 15px. Corners at `{rounded.sm}` (8px) keep the shape industrial and squared-off, matching the geometry of the products. On hover, background transitions to `{colors.primary-active}` (#00afec) with a subtle 150ms ease. Disabled state shifts to a desaturated blue (#609edb) at reduced opacity. Height fixed at 48px across all viewports.

**`button-secondary`** — White fill with a 2px ink-black border and dark text. On hover, the fill inverts to `{colors.ink}` with white text, creating a definitive click-state. Used for "Add to Cart" secondary actions and comparison triggers where the cyan primary would compete with product imagery.

**`button-navy`** — Deep navy (#2a3048) fill used exclusively in the hero and footer contexts where the primary cyan would clash with photography overlays. Same 48px height and `{rounded.sm}` corners as primary.

**`button-sm`** — Compact 36px-height variant with `{rounded.xs}` corners, used inside product cards for quick-add actions and filter chips.

### Navigation

**`nav-bar`** — Fixed navy (#2a3048) bar at 64px height. Logo sits left in Futura-Book with 1.5px letter-spacing. Navigation links in Figtree 600 weight are centered, with a hover underline animation (2px cyan line sliding in from left). On scroll, height compresses to 56px with a drop shadow for depth. Mobile collapses to a hamburger with a full-screen navy overlay.

**`announcement-bar`** — Sits above nav at 40px height with cyan background and white caption text. Used for shipping thresholds and promotions. Dismissible with an × icon that persists state in localStorage.

### Product Cards

**`product-card`** — White surface with 12px radius and a subtle 1px box-shadow at rest. Image area uses `{colors.surface-soft}` background with the product centered at 80% width and square aspect ratio. On hover, shadow deepens to 16px blur and the card translates -2px on Y axis. Title in `{typography.title-md}`, price in `{typography.title-sm}`, and mAh spec in `{typography.caption}` with the spec-label style.

**`product-card-image`** — The contained image zone within the card uses `{colors.surface-soft}` as its backdrop to ensure product shots (often on transparent PNGs) render against a consistent neutral tone rather than pure white.

### Spec & Feature Blocks

**`spec-stat`** — Rounded container (`{rounded.md}`) on soft-gray background displaying a single key metric (e.g., "10,000 mAh", "20W", "2 Ports"). The label sits above in uppercase 12px Figtree at 700 weight with 0.5px tracking, the value below in CocoSharp 24px bold. Used in 3-up or 4-up grids on product detail pages.

**`spec-badge`** — Compact mint-green chip for status indicators: "Fast Charge", "USB-C", "Built-in Cable". Green text on `{colors.accent-mint}` background with `{rounded.xs}` corners.

**`spec-badge-yellow`** — Yellow variant for promotional flags: "Best Seller", "New", "Limited". Dark olive text on pale yellow.

**`feature-icon-circle`** — 56px lavender circle with a centered cyan icon (24px). Used in feature grids to illustrate capabilities like wireless charging, passthrough, or weather resistance.

### Hero

**`hero-banner`** — Full-width navy section with minimum 520px height. Display text in CocoSharp at `{typography.display-xl}` (48px) weight 700, left-aligned with a max-width of 600px. Product photography floats right or bleeds to edge. CTA button uses `button-primary` positioned below the headline with `{spacing.lg}` gap. Subtle gradient overlay (navy to transparent) protects text legibility over imagery.

**`hero-banner-light`** — Soft-gray variant for secondary hero placements (category pages, landing pages) with dark text and no overlay.

### Charging Indicator

**`charging-indicator`** — Horizontal progress bar on dark background, 8px height with `{rounded.full}` ends. Fill color is `{colors.primary}` with an animated pulse glow at the leading edge. Used on product pages to visually represent charge capacity relative to device charges ("charges iPhone 3x").

### Comparison Table

**`comparison-table`** — Bordered table with `{rounded.md}` outer radius and 1px hairline cell borders. Header row in `{typography.title-sm}` with sticky positioning. Cell padding at 12px/16px. Checkmarks use `{colors.success}`, missing features show a muted dash. Used to compare charger models side-by-side.

### Footer

**`footer`** — Dark surface (#171717) with white body text and `{colors.mid-blue}` links. Four-column grid on desktop (Products, Support, Company, Social) collapsing to accordion on mobile. Newsletter signup input uses `text-input-dark` variant. Bottom bar with copyright in `{typography.caption-sm}`.

### Search & Breadcrumbs

**`search-overlay`** — Modal overlay with white background, 12px radius, and deep shadow. Input auto-focuses with cyan border on focus. Results appear as a list with product thumbnails (40px), title, and price. Triggered by magnifying glass icon in nav.

**`breadcrumb`** — Horizontal trail in `{typography.body-sm}` with muted text, forward-slash separators in `{colors.border-mid}`, and the current page in `{colors.ink}`. Padding uses `{spacing.md}` vertical.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, nav collapses to hamburger menu, hero text drops to `{typography.display-md}` (28px), spec-stats stack 2-up, comparison table horizontally scrolls, footer columns become accordions |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed spacing, hero image scales to 50% width, spec-stats remain 3-up, footer shifts to 2×2 grid |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links and search visible, hero at full 520px height with side-by-side text/image, all components at default sizing |
| Wide | > 1440px | Content max-width caps at 1440px and centers, product grid expands to four columns, hero gains extra horizontal padding, section spacing increases to 96px |

### Touch Targets

- All interactive elements maintain 44px minimum touch target on mobile, even when visually smaller
- Product card tap zones extend to full card area (not just image or title)
- Nav hamburger icon padded to 48×48px hit area
- Spec badges in product detail are non-interactive; feature-icon-circles link to feature sections with 56px target

### Collapsing Strategy

- Navigation: full horizontal links → condensed links (tablet) → hamburger with full-screen overlay (mobile)
- Product grid: 4-col → 3-col → 2-col → 1-col, maintaining card aspect ratios
- Spec-stat grids: 4-up → 3-up → 2-up, never 1-up (minimum two stats side-by-side for comparison value)
- Hero: side-by-side layout → stacked (image above, text below) at tablet breakpoint
- Comparison table: fixed layout → horizontal scroll with sticky first column on mobile
- Footer: 4-column grid → 2×2 (tablet) → single-column accordions (mobile)

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font weights for CocoSharp variants could not be confirmed — the font may ship as discrete files (Light, Regular, Bold) rather than variable weight; assumed 600/700 based on visual density
- Futura-Book usage appears limited to the logo lockup; full fallback stack and alternate weights not observed
- Icon system (line weight, grid size, icon font vs. SVG sprite) not determinable from color/font extraction alone
- Exact box-shadow values on product cards and search overlay are approximations — live site likely uses Shopify theme variables
- Motion/animation timing (hover transitions, page transitions, loading states) not captured in static extraction
- Whether the mint-green (#cdfee1) and yellow (#ffef9d) badges are hardcoded or generated from a configurable tag system is unclear
- Dark mode or reduced-motion preferences not observed in extracted data
- Exact max-width constraint for content area (estimated 1440px from common Shopify patterns) not directly confirmed
