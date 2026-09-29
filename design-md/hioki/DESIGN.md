---
version: alpha
name: "Hioki"
source_url: "https://www.hioki.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Red sits at the tip of every Hioki instrument — the jaw of a clamp meter, the shroud of a probe, the LED power indicator — and the same calibrated voltage translates into the digital brand as a single decisive vermillion (#e8001c) that functions more like a warning light than a decorative accent. The brand operates at the intersection of Japanese precision engineering and international technical authority: a white canvas (#ffffff) held to strict editorial discipline, with near-black ink (#1a1a1a) carrying data-dense specifications and a cool gray hierarchy handling everything secondary. There is no ornamentation — no gradient wash, no illustrative warmth. The geometry is sharp: hard corners dominate product tables and data cards, softened only slightly on interactive controls (`{rounded.sm}`) so that the interface reads as a calibrated instrument rather than a consumer app. Photography leans on close-cropped instrument shots on neutral backgrounds, communicating precision through clarity rather than lifestyle staging. Navigation carries a measured, menu-heavy structure with deep product categorization — oscilloscopes, power analyzers, LCR meters, clamp sensors — organized with the same logical taxonomy that appears in a product datasheet. CTAs like "Download" and "Request a Quote" sit in contained rectangular buttons with clear contrast, never pill-shaped, never rounded to softness. Typographic sizing is conservative and legible: display lines run at modest weights to prioritize scanability of model numbers and technical specs over brand expressiveness. The footer is expansive and information-dense, reflecting the expectations of an engineering audience who reads documentation rather than scrolls social feeds. Every spatial decision — from the tightly-controlled `{spacing.base}` grid to the hairline table borders at `{colors.hairline}` — signals that Hioki is built for people who measure things for a living, and who expect the tools they use to behave like instruments.

colors:
  primary: "#e8001c"
  primary-active: "#b80016"
  primary-disabled: "#f4808e"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-mid: "#f0f0f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#0066cc"
  link-hover: "#004499"
  alert-warn: "#f5a623"
  alert-error: "#e8001c"

typography:
  display-xl:
    fontFamily: "'Noto Sans JP', 'Hiragino Kaku Gothic ProN', 'Meiryo', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Noto Sans JP', 'Hiragino Kaku Gothic ProN', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Noto Sans JP', 'Hiragino Kaku Gothic ProN', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Noto Sans JP', 'Hiragino Kaku Gothic ProN', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  title-sm:
    fontFamily: "'Noto Sans JP', 'Hiragino Kaku Gothic ProN', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "'Noto Sans JP', 'Hiragino Kaku Gothic ProN', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Noto Sans JP', 'Hiragino Kaku Gothic ProN', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'Noto Sans JP', 'Hiragino Kaku Gothic ProN', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  spec-label:
    fontFamily: "Consolas, 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.3px
  model-number:
    fontFamily: "Consolas, 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "'Noto Sans JP', 'Hiragino Kaku Gothic ProN', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Noto Sans JP', 'Hiragino Kaku Gothic ProN', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Noto Sans JP', 'Hiragino Kaku Gothic ProN', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Noto Sans JP', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.primary}"
    padding: 9px 19px
    height: 40px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1.5px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    borderBottom: "1px solid {colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    paddingX: "{spacing.xl}"
  nav-bar-top-strip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 32px
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    shadow: "0 4px 16px rgba(0,0,0,0.10)"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    height: 40px
    iconColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    imageBackground: "{colors.surface-soft}"
    modelNumberTypography: "{typography.model-number}"
    titleTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"
  product-card-hover:
    border: "1px solid {colors.muted}"
    shadow: "0 2px 12px rgba(0,0,0,0.08)"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
    paddingY: "{spacing.xxl}"
    accentBar: "4px solid {colors.primary}"
  category-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 6px"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.title-sm}"
    cellTextColor: "{colors.body}"
    cellTypography: "{typography.spec-label}"
    border: "1px solid {colors.hairline}"
    rowBorderBottom: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.none}"
  download-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    iconColor: "{colors.primary}"
    labelTypography: "{typography.body-sm}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"
  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackgroundColor: "{colors.canvas}"
    inactiveTextColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 32px
    width: 32px
    typography: "{typography.button-sm}"
  footer:
    backgroundColor: "#222222"
    textColor: "{colors.on-dark}"
    linkColor: "#aaaaaa"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    paddingY: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — A rectangular, hard-cornered CTA in Hioki red (#e8001c) at 40px height with 10px vertical and 20px horizontal padding. Used for primary actions like "Add to Cart," "Request Quote," or "Download Datasheet." On hover, deepens to `{colors.primary-active}` (#b80016); disabled state washes to `{colors.primary-disabled}`. No pill rounding — the `{rounded.sm}` 4px corner is the maximum softness applied to any button in the system.

**`button-secondary`** — White fill with a 1.5px red border and red text, maintaining the brand accent while reducing visual weight. Used adjacent to primary actions (e.g., "Compare" or "View Details"). Hover shifts fill to `{colors.surface-soft}` to confirm interactivity without losing the red outline logic.

**`button-ghost`** — Transparent with a single bottom border in `{colors.muted}`, functioning as an inline text-link-style action. Used for secondary navigation within content blocks and "See all" prompts in product category grids.

### Navigation

**`nav-bar`** — A 60px white bar with a 1px `{colors.hairline}` bottom border. The Hioki logo anchors left; product category dropdowns and utility links (Support, Distributors, Region) sit right. A `nav-bar-top-strip` at 32px in near-black carries the region/language selector and a direct path to the corporate investor relations portal — typical of Japanese B2B brands that serve both engineering buyers and institutional stakeholders.

**`nav-mega-menu`** — Full-width dropdown panels organized by product family (Electrical Safety, Power Measurement, Data Acquisition, etc.) with sub-categories and featured product thumbnails. No rounded corners; `box-shadow: 0 4px 16px rgba(0,0,0,0.10)` lifts it from the page. Typography stays at `{typography.body-sm}` to accommodate the density of a deep product catalog.

### Product Card

**`product-card`** — Zero-radius border card with a 1px `{colors.hairline}` rule and a light `{colors.surface-soft}` image field that floats the instrument photograph on neutral ground. The model number renders in `{typography.model-number}` (monospace, tracked) to distinguish the alphanumeric product ID (e.g., "PW6001") from the prose title. On hover, the border darkens and a subtle shadow lifts the card. Category and "New" badges in `{colors.primary}` pin to the image corner.

### Hero Banner

**`hero-banner`** — Full-bleed dark panel in `{colors.ink}` with a 4px `{colors.primary}` top accent bar. Headline in `{typography.display-xl}` white, body in `{typography.body-md}` at reduced opacity. Used for campaign landing sections and trade-show spotlight announcements. Never lifestyle photography — instrument detail shots or abstract measurement data visualizations only.

### Spec Table

**`spec-table`** — The workhorse component for product detail pages. A zero-radius HTML table with a `{colors.surface-soft}` header row and alternating `{colors.hairline-soft}` row separators. Header labels use `{typography.title-sm}`; cell content uses `{typography.spec-label}` in monospace for measurement values (Ω, V, Hz, A) to maintain column alignment. No zebra striping beyond the hairline separator — keeps reading clean at dense row counts.

### Download Card

**`download-card`** — Light surface card with a red file-type icon (PDF, ZIP) left-aligned and the document title in `{typography.body-sm}`. Used in Support and Documentation pages for datasheets, instruction manuals, and application guides. Clicking the entire card triggers the download — no separate button required.

### Search Bar

**`search-bar`** — A contained `{rounded.sm}` input sitting in `{colors.surface-soft}`, bordered in `{colors.hairline}`. On focus, border shifts to `{colors.primary}` to signal active state. A magnifier icon in `{colors.muted}` sits right-inset. Used sitewide in the top-right utility cluster and as a full-width element on the product search landing page.

### Badges

**`category-badge`** and **`new-badge`** — Small, uppercase, 2px-radius chips in `{colors.primary}` white text. `category-badge` labels the product type (Power Meter, Data Logger) on cards and listing rows. `new-badge` marks recently launched instruments and is identical in construction, differing only in label text.

### Footer

**`footer`** — Dark (#222222) with a 3px `{colors.primary}` top rule as a brand terminator. Four columns cover Products, Support, Company, and Regional Resources. Links render at `#aaaaaa` and lift to white on hover. The footer carries ISO certification marks, RoHS compliance icons, and regional headquarters addresses — all expected by an engineering audience conducting vendor qualification.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger menu replaces horizontal nav. Product grid collapses to single column. Spec tables scroll horizontally. Hero banner reduces to 320px height. Download cards stack vertically. |
| Tablet | 744–1128px | Two-column product grid. Mega-menu condenses to accordion drawers. Hero maintains dual-column text + image layout. Breadcrumb truncates to last two segments. |
| Desktop | 1128–1440px | Three to four-column product grid. Full mega-menu panel. Spec table visible without scroll. Hero banner at full 480px with side-by-side CTA cluster. |
| Wide | > 1440px | Max content width caps at 1400px, centered. Nav and hero maintain proportions. Product grid holds at four columns; whitespace widens in `{spacing.section}` rhythm. |

### Touch Targets

- All interactive buttons minimum 40px height, primary CTA 44px on mobile
- Nav hamburger tap target 48×48px
- Product card full-card tap area, no isolated button required
- Download card full-area tap triggers download
- Pagination controls minimum 40px square on mobile

### Collapsing Strategy

- Mega-menu collapses to accordion-style slide panels inside hamburger drawer on mobile and tablet
- Spec tables gain horizontal scroll container with sticky first column (parameter name) at mobile breakpoint
- Footer four-column grid collapses to two columns on tablet, single column on mobile
- Top strip (region/language bar) hides below 744px; region selector moves into hamburger drawer
- Hero headline scales from `{typography.display-xl}` (36px) down to `{typography.display-md}` (24px) at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site (JS-loaded design tokens or anti-bot protection); all palette values derive from Hioki's publicly visible brand materials and general corporate identity knowledge — treat as best estimates requiring validation against the actual site
- No font-family stacks were captured; typography assignments use a plausible Japanese-brand sans-serif stack (Noto Sans JP + system fallbacks) consistent with the brand's Japanese origin and international technical audience, but the actual webfont may differ
- Meta theme-color is absent, so mobile browser chrome tinting cannot be confirmed
- Exact button border-radius, shadow values, and spacing rhythms are inferred from instrument-brand norms rather than measured from the live DOM
- Animation and transition timing (hover speed, dropdown easing) are not documented; likely conservative (150–200ms ease) for a professional/technical brand but unconfirmed
- Dark mode support unknown — no evidence of a color-scheme toggle in available metadata
- Hioki operates separate regional sites (Japan, Americas, Europe, Asia); design tokens may vary by locale
