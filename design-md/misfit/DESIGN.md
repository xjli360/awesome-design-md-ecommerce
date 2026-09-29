---
version: alpha
name: "Misfit"
source_url: "https://www.misfit.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every hero frame renders hardware against pure darkness — an absolute near-black (#0a0a0a) that dissolves product edges and makes an aluminum Shine disc or Vapor bezel appear self-luminous rather than lit from outside. Type stays skeletal: display headings rarely cross 500 weight, treating the white-on-black contrast as the entire statement rather than typographic muscle. The brand's geometry is circular everywhere it matters — watch faces, tracker discs, product thumbnails — and that circle logic bleeds into UI as `{rounded.full}` pill buttons and circular icon badges. Navigation reads like a product catalog rather than a feature list: a minimal horizontal bar, wordmark anchored left, three or four destination links right, no mega-menu, no promotional banners crowding the header. The palette runs close to monochrome with a single cool-cyan accent (`#00b8d9`) reserved for primary CTAs and active-state underlines, a choice that reads as precision engineering rather than brand color play. Product cards float on `{colors.surface-card}` (#1a1a1a) with no visible border — separation comes from the depth delta between card and canvas, not from hairlines. Spacing is generous on desktop, with section padding that mirrors the breathing room around a physical product on a shelf rather than the compressed grid of a deal-driven retailer. The Misfit brand sits at the intersection of fitness tracking and fashion accessory, and the UI encodes that duality: spec tables and metric dashboards use the same restrained type scale as editorial hero copy, so the page never feels like it switches between gadget store and lifestyle magazine. Because no color or font tokens could be extracted from the live site (likely JS-loaded or behind anti-bot), the palette and typography below are inferred from Fossil Group brand history, archived Misfit product pages, and the documented visual language of Misfit Vapor and Shine product lines — treat all values as approximate and verify against computed styles before production use.

colors:
  primary: "#00b8d9"
  primary-active: "#0096b4"
  primary-disabled: "#003f4d"
  ink: "#f5f5f7"
  body: "#c7c7cc"
  muted: "#8e8e93"
  hairline: "#2c2c2e"
  hairline-soft: "#1c1c1e"
  canvas: "#0a0a0f"
  surface-soft: "#111115"
  surface-card: "#1a1a1f"
  surface-raised: "#222228"
  on-primary: "#000000"
  on-dark: "#f5f5f7"
  accent-gold: "#c9a84c"
  accent-rose: "#c06b78"
  success: "#34c759"
  error: "#ff453a"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'SF Pro Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.07
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'SF Pro Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.8px
  display-md:
    fontFamily: "'SF Pro Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.21
    letterSpacing: -0.4px
  display-sm:
    fontFamily: "'SF Pro Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 21px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'SF Pro Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.41
    letterSpacing: -0.2px
  title-sm:
    fontFamily: "'SF Pro Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.46
    letterSpacing: -0.1px
  body-md:
    fontFamily: "'SF Pro Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.58
    letterSpacing: -0.1px
  body-sm:
    fontFamily: "'SF Pro Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'SF Pro Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-strong:
    fontFamily: "'SF Pro Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  overline:
    fontFamily: "'SF Pro Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 1.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'SF Pro Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 17px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: -0.1px
  button-sm:
    fontFamily: "'SF Pro Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.28
    letterSpacing: 0
  nav-link:
    fontFamily: "'SF Pro Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.28
    letterSpacing: 0
  spec-label:
    fontFamily: "'SF Pro Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
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
  hero: 120px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 50px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 13px 27px
    height: 50px
  button-secondary-hover:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    paddingX: "{spacing.xl}"
    borderBottom: "1px solid {colors.hairline-soft}"
    backdropFilter: "blur(20px)"
    position: sticky
  nav-wordmark:
    fontFamily: "'SF Pro Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    letterSpacing: 2px
    textTransform: uppercase
    textColor: "{colors.ink}"
  hero-full-bleed:
    backgroundColor: "{colors.canvas}"
    minHeight: "100vh"
    layout: centered
    paddingTop: "{spacing.hero}"
    paddingBottom: "{spacing.hero}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadlineTypography: "{typography.display-md}"
    subheadlineColor: "{colors.body}"
    ctaMarginTop: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    overflow: hidden
    padding: "{spacing.lg}"
    imageAspectRatio: "1:1"
    nameTypography: "{typography.title-md}"
    nameColor: "{colors.ink}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.body}"
    hoverTransform: "translateY(-4px)"
    hoverTransition: "0.25s ease"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  color-swatch-picker:
    size: 24px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.ink}"
    borderInactive: "2px solid transparent"
    gap: "{spacing.sm}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    rowPadding: "12px 16px"
    dividerColor: "{colors.hairline}"
  feature-icon-row:
    iconSize: 32px
    iconColor: "{colors.primary}"
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xxl}"
    labelTypography: "{typography.title-sm}"
    labelColor: "{colors.ink}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
  comparison-table:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    headerTypography: "{typography.title-sm}"
    headerColor: "{colors.ink}"
    headerBg: "{colors.surface-raised}"
    cellTypography: "{typography.body-sm}"
    cellColor: "{colors.body}"
    checkColor: "{colors.primary}"
    borderColor: "{colors.hairline}"
  app-store-badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "10px 16px"
    iconSize: 24px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkColor: "{colors.body}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.body-sm}"
    paddingY: "{spacing.xxl}"
    borderTop: "1px solid {colors.hairline}"
    columnGap: "{spacing.xxl}"

## Components

### Buttons
**`button-primary`** — Full-pill geometry (`{rounded.full}`) in Misfit cyan (`{colors.primary}`) with black text, 50px tall, 28px horizontal padding. Active state compresses to `{colors.primary-active}`; disabled collapses to `{colors.primary-disabled}` with muted label. The pill form connects visually to the circular watch-face motif that defines the hardware product line.

**`button-secondary`** — Same pill radius with transparent fill, `{colors.hairline}` 1px border, and `{colors.ink}` text. Hover floods the interior with `{colors.surface-raised}` without changing the border — a low-flash shift that keeps dark-mode contrast stable. Used alongside primary for "Buy" + "Learn more" pairings on product pages.

**`button-ghost`** — Transparent background, `{colors.primary}` text, no border, no radius. Used for inline text-link CTAs in spec sections and editorial paragraphs where a boxed button would interrupt reading flow.

### Text Input
**`text-input`** — `{colors.surface-card}` fill with a `{colors.hairline}` border, slight `{rounded.sm}`, and 48px height. Placeholder text renders in `{colors.muted}`. On focus, the border swaps to `{colors.primary}` — no glow, no shadow — consistent with the brand's preference for precise rather than atmospheric feedback. Used in newsletter sign-up, account login, and app-download email-entry flows.

### Navigation
**`nav-bar`** — 60px sticky header at `{colors.canvas}` with a `{colors.hairline-soft}` bottom rule and `backdrop-filter: blur(20px)` for scroll legibility. Wordmark sits left in `{typography.nav-wordmark}` (all-caps, tracked at 2px). Three to four destination links in `{typography.nav-link}` sit right, separated by `{spacing.xl}` gaps. No hamburger on desktop; on mobile the links collapse into a drawer triggered by a minimal 24px icon button.

### Hero
**`hero-full-bleed`** — Full-viewport dark canvas (`{colors.canvas}`) with centered product shot and headline in `{typography.display-xl}` at weight 300. The lightweight display type against absolute black is the hero's whole argument — no overlays, no gradient scrims, no supporting body text except a brief descriptor in `{typography.display-md}` and a primary CTA pill below. Section-level vertical padding (`{spacing.hero}`) gives the hardware image room to read as an object rather than a screenshot.

### Product Card
**`product-card`** — `{colors.surface-card}` fill, `{rounded.lg}` corners, no border. The depth separation from `{colors.canvas}` replaces explicit stroke. Square image region (1:1) fills the top; name in `{typography.title-md}` and price in `{typography.body-md}` sit below with `{spacing.lg}` padding on all sides. Hover applies a 4px upward translate over 0.25s ease — gentle kinetic feedback without color change. Optional `product-card-badge` overlays the image corner for "New" or colorway labels.

### Color Swatch Picker
**`color-swatch-picker`** — 24px circles in `{rounded.full}`, spaced `{spacing.sm}` apart. Selected state shows a 2px `{colors.ink}` ring via `border`; unselected has a transparent border that preserves layout stability. Used on product detail pages to switch between finishes (black, silver, rose gold). No tooltip, no label — the swatch color is the label.

### Spec Table
**`spec-table`** — `{colors.surface-soft}` background in `{rounded.md}` container. Each row pairs a `{typography.spec-label}` label (uppercase, muted) with a `{typography.body-sm}` value in `{colors.ink}`, divided by `{colors.hairline}` rules. Used for battery life, water resistance, connectivity, and compatibility rows on every product page. No zebra striping — row distinction comes from the label/value typographic contrast.

### Feature Icon Row
**`feature-icon-row`** — Three- or four-column grid on desktop, single-column on mobile. Each cell: 32px `{colors.primary}` icon above `{typography.title-sm}` label and `{typography.caption}` descriptor. The cell itself sits in a `{colors.surface-card}` tile with `{rounded.xl}` and generous `{spacing.xxl}` internal padding — making each feature feel spatially equivalent to a product card rather than a footnote bullet.

### Comparison Table
**`comparison-table`** — Full-width responsive table in `{colors.surface-card}` with `{rounded.lg}`. Header row uses `{colors.surface-raised}` background and `{typography.title-sm}`. Checkmarks render in `{colors.primary}`; absence uses an em-dash in `{colors.muted}`. Dividers are `{colors.hairline}`. Used on category pages to compare Misfit models against each other rather than against competitors.

### App Store Badge
**`app-store-badge`** — Small inline component with 24px platform icon (Apple/Google) and label in `{typography.caption-strong}`. `{colors.surface-card}` fill, `{colors.hairline}` border, `{rounded.sm}`. Placed in the footer and on product pages beneath app-connectivity feature callouts.

### Footer
**`footer`** — `{colors.surface-soft}` background with a `{colors.hairline}` top rule. Links in `{typography.body-sm}` at `{colors.body}`; secondary text in `{colors.muted}`. Columns spaced by `{spacing.xxl}` horizontally; section-level vertical padding. Social icons render as 20px monochrome glyphs, not colored platform logos — consistent with the dark monochrome palette.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav links collapse to slide-in drawer; hero headline drops to `{typography.display-md}`; hero padding reduces to `{spacing.xl}`; spec table becomes full-width with stacked rows |
| Tablet | 744–1128px | Two-column product grid; nav shows wordmark + icon-only drawer trigger; hero at `{typography.display-lg}`; feature icon row at two columns |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav link row visible; hero headline at `{typography.display-xl}`; feature icon row at four columns; comparison table fully visible |
| Wide | > 1440px | Max-width container at 1340px centered; hero image scales to fill remaining horizontal space; footer switches to five-column layout |

### Touch Targets
- All interactive elements minimum 44×44px on mobile, matching Apple HIG and Android Material minimums
- Color swatch circles expand from 24px to 36px on mobile via padding increase (visual size unchanged)
- Nav drawer links receive 56px row height with full-width tap area
- Product card entire surface is tappable — not just the image or title

### Collapsing Strategy
- Feature icon row: 4-col → 2-col → 1-col
- Product grid: 4-col → 2-col → 1-col, maintaining card proportions
- Comparison table: scrollable horizontally on mobile behind sticky first column (model name)
- Spec table rows stack label above value on viewports narrower than 480px
- Hero text alignment switches from centered to left-aligned on mobile to avoid orphan words at narrow widths
- Footer columns stack vertically in two groups (navigation links, legal/social) on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All hex colors are inferred from brand memory** (Fossil Group archived materials, Misfit Vapor/Shine product pages); live site returned no extractable color tokens — likely JS-injected or behind anti-bot protection. Verify every color against DevTools computed styles before production use.
- **Font stack is inferred** — no `font-family` declarations were extracted from the live site. SF Pro Display/Text is a plausible stand-in for a clean Apple-adjacent geometric sans; the actual typeface may differ entirely.
- **Primary accent color unconfirmed** — `#00b8d9` is consistent with Misfit Vapor marketing materials but is not a formally documented brand color. Could be a deeper navy, pure white-only accent, or a Fossil Group shared color.
- **Accent-gold and accent-rose** are product-finish colors (Misfit Shine in rose gold/gold editions), not confirmed digital UI palette members.
- **No `meta theme-color`** detected — mobile browser chrome color unknown.
- **Current site status unclear** — Misfit.com may redirect to Fossil.com or show a holding page post-2021 product discontinuations; if so, this spec describes the brand at peak product-line activity rather than the current live state.
- **Animation/motion tokens** not specified — no evidence from extraction for transition durations, easing curves, or scroll-animation preferences.
- **Icon system unknown** — circular icon style inferred from hardware design language; actual UI icon library (custom, Material, SF Symbols) not confirmed.
