---
version: alpha
name: "Casio"
source_url: "https://www.casio.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Forty years of LCD panel engineering left Casio's visual language shaped by the segmented digit — the seven-bar display that renders every numeral readable at arm's length under fluorescent light. That commitment to legibility under adverse conditions carries directly into the digital interface: a #cc0000 brand red concentrates every primary CTA onto a single high-energy frequency against white product fields, borrowing the hard contrast that makes a quartz display readable in direct sunlight. The nav band runs near-black (#0a0a0a), partitioning catalogue-brand authority from the white product-browsing space below — a structural device common in Japanese consumer electronics where the header functions as a second brand lockup, not merely a link cluster.

  The product range spans from ¥1,000 F-91W units to ¥300,000 MR-G titanium pieces, which means the UI must anchor specification trust as firmly as it carries aspirational photography. Body copy and labels sit at weight 600–700 at smaller sizes — heavier than a fashion brand would ever deploy — signaling that model numbers and module counts deserve the same hierarchy as hero headlines. Product cards carry a strict white surface, no decorative gradients, and grid-aligned spec rows beneath each watch thumbnail: a visual argument that the catalog is a reference tool, not a mood board.

  G-Shock receives its own sub-brand treatment: yellow (#f5c300) enters the system only in G-Shock landing contexts, appearing on filter badges and series header bands, never bleeding into the general catalog. Baby-G draws on lighter pastels and Pro Trek carries muted olive, but sub-brand accent containment means a single component library serves radically different registers without rebuilding tokens. Buttons sit on {rounded.none} by default on desktop product pages — a flat-rectangle heritage from hardware specification sheets — while mobile CTAs relax to {rounded.xs} to meet minimum touch-target guidance. The overall impression is of a global catalog built on a specification-first hierarchy, where every visual choice must justify itself against the legibility standard of a 1983 databank wristwatch.

colors:
  primary: "#cc0000"
  primary-active: "#a30000"
  primary-disabled: "#f0a0a0"
  gshock-accent: "#f5c300"
  gshock-accent-active: "#d4a600"
  nav-dark: "#0a0a0a"
  ink: "#111111"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-gshock: "#000000"
  badge-new: "#cc0000"
  badge-limited: "#0a0a0a"

typography:
  display-xl:
    fontFamily: "'Noto Sans JP', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Noto Sans JP', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Noto Sans JP', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Noto Sans JP', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Noto Sans JP', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Noto Sans JP', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Noto Sans JP', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Noto Sans JP', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Noto Sans JP', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Noto Sans JP', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Noto Sans JP', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0
  spec-label:
    fontFamily: "'Noto Sans JP', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  model-number:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  price:
    fontFamily: "'Noto Sans JP', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 11px 23px
    height: 44px
  button-gshock:
    backgroundColor: "{colors.gshock-accent}"
    textColor: "{colors.on-gshock}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    padding: 10px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    imageAspectRatio: "1 / 1"
    padding: "{spacing.base}"
    modelNumberTypography: "{typography.model-number}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
  product-spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    rowBorder: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-dark}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  gshock-series-header:
    backgroundColor: "{colors.gshock-accent}"
    textColor: "{colors.on-gshock}"
    typography: "{typography.display-md}"
    padding: "{spacing.xl} {spacing.section}"
  hero-banner:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
  filter-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.title-sm}"
    optionTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  series-tab:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    activeTextColor: "{colors.primary}"
    activeBorder: "2px solid {colors.primary}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — A flat rectangle with no border-radius, #cc0000 fill, and white text at weight 600 and 0.5px letter-spacing. Hover darkens to `primary-active` (#a30000); disabled state fades to a light rose (#f0a0a0) while preserving white text. At 44px height the button meets minimum touch-target spec without the rounded padding common in fashion-oriented stores.

**`button-secondary`** — White fill with a 1px solid #111111 border; same flat-rectangle profile as the primary. Used for secondary catalog actions like "Compare" and "Save to Wishlist" where the primary CTA must dominate visually on cluttered spec pages.

**`button-gshock`** — G-Shock sub-brand CTA using the #f5c300 yellow on black text. Appears exclusively inside G-Shock series landing pages and product detail pages; its presence signals a sub-brand context switch to the user. Never rendered alongside a standard red primary button on the same screen.

### Navigation

**`nav-bar`** — A near-black (#0a0a0a) full-width band at 60px height carrying the Casio wordmark on the left, product-line mega-menu triggers in the center, and search/account icons on the right. Text renders in white at 14px weight 500, with no active underline on hover — only the dropdown mega-menu appears. The hard color contrast against the white content field below makes the nav feel more like a product header than a standard site chrome.

**`nav-mega-menu`** — A white fly-out panel triggered on hover over product lines (Watches, Calculators, Musical Instruments, etc.), with a 1px hairline border and generous `{spacing.lg}` internal padding. Series thumbnails appear in a 4–6 column grid alongside text links to sub-categories; the mega-menu deliberately surfaces product photography rather than hiding it in text hierarchies.

### Product Card

**`product-card`** — White surface, no radius, 1px hairline border, and a square 1:1 image crop. The model number appears beneath the image in `{typography.model-number}` (monospace, 12px), followed by the descriptive name in `{typography.title-sm}` and the price in `{typography.price}` (700 weight, 20px). Badge overlays for NEW or LIMITED use uppercase spec-label typography pinned to the top-left corner of the image.

**`product-spec-table`** — A two-column definition table that appears on product detail pages below the main image gallery. Labels use `{typography.spec-label}` (11px, uppercase, 0.8px tracking) in the left column; values use `{typography.body-sm}` right-aligned. Rows sit on `{colors.surface-soft}` with 1px hairline separators, communicating that specifications are structured data, not marketing copy.

### Badges

**`badge-new`** — Red fill (#cc0000), white uppercase text at 11px weight 700, no border-radius, 3px vertical and 8px horizontal padding. Appears as a corner chip on product card images. **`badge-limited`** — Same geometry with near-black fill (#0a0a0a) and white text, used for limited-edition releases where red is reserved for the newness signal.

### G-Shock Series Header

**`gshock-series-header`** — A full-bleed yellow (#f5c300) band used as the landing-page masthead for G-Shock series pages. The series name renders in `{typography.display-md}` at weight 700 in black (#000000), with generous `{spacing.xl}` vertical padding. The band's purpose is to make the sub-brand context unambiguous at first scroll, replacing the standard dark hero used for the general catalog.

### Hero Banner

**`hero-banner`** — Near-black background with a full-bleed product photograph, minimum 480px height. Headline uses `{typography.display-xl}` at weight 700 in white; supporting copy uses `{typography.body-md}` at weight 400. A red primary button anchors the bottom-left of the text block. Dark hero + white text + red CTA is the default treatment for new product launches and seasonal campaigns.

### Filter Panel

**`filter-panel`** — A left-rail panel on desktop catalog pages, white background with 1px hairline border, no border-radius. Filter group labels use `{typography.title-sm}` (weight 600) as section headers; individual options use `{typography.body-sm}` with checkbox inputs. Active filter chips appear above the product grid as removable tags using the same flat-rectangle language as buttons.

### Series Tabs

**`series-tab`** — Horizontal tab strip used within product lines (e.g. G-Shock series: Master of G, Analog-Digital, Skeleton). Inactive tabs carry ink text on white with no border; active tab shows a 2px red bottom border with `{colors.primary}` text. No border-radius anywhere in the strip, consistent with the flat-rectangle system.

### Footer

**`footer`** — Full-width near-black band mirroring the nav. Links render in `{typography.body-sm}` at white with no underline until hover. Organized in multi-column link groups (Products, Support, Corporate, Social) above a legal strip with copyright and region-selector controls. The dark footer + dark nav creates a consistent brand frame around white product content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with slide-in drawer; filter panel becomes bottom sheet; sticky "Add to Cart" bar fixed above browser chrome; series tabs collapse to horizontal scroll |
| Tablet | 744–1128px | 2-column product grid; filter sidebar persists as collapsible left rail; nav mega-menu replaced by accordion in drawer; hero banner reduces to 360px height |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with hover mega-menu; visible filter panel; spec table shifts to 2-column layout beside image gallery |
| Wide | > 1440px | 4–5 column product grid; max-width container (~1400px) centered; hero banners full-bleed behind contained text block; footer link columns spread to 6 |

### Touch Targets

- All buttons minimum 44×44px on mobile
- Filter checkboxes padded to 44px tap height with invisible hit area extension
- Series tabs minimum 44px height with full-width tap zones
- Product cards are full-surface tappable with no nested interactive elements competing for the tap

### Collapsing Strategy

- Mega-menu collapses to categorized accordion inside the hamburger drawer
- Spec tables stack into single-column definition lists on mobile
- Filter panel becomes a "Filter & Sort" bottom sheet with apply/clear CTAs
- Secondary nav links (Support, Corporate) collapse to a footer accordion on mobile
- Price and model number remain visible on card at all breakpoints; only secondary metadata (series name, short description) truncates

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors extracted — site returned 403 Access Denied; all color values derived from widely-documented Casio brand references (red CTAs, black nav) and should be verified against live assets
- No font families extracted — typography stack uses Noto Sans JP as a reasonable inference for a Japanese-origin brand with multilingual catalog requirements; actual font may differ (possibly a custom or licensed typeface)
- Sub-brand color values for Baby-G (pastel pink/mint) and Pro Trek (muted olive) not specified — only G-Shock yellow included; those sub-brand tokens should be added once verified
- Exact nav height, hero minimum height, and card border-radius values are inferred from category conventions rather than measured from live DOM
- Dark-mode or regional site variants (casio.com/jp vs /us) may use different token values not covered here
- Promotional color system (sale red vs badge red) may be distinct tokens on the live site; treated as a single `{colors.primary}` here
