---
version: alpha
name: "X-Chair"
source_url: "https://www.xchair.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Exo2 at display weight has the visual signature of a cockpit instrument label — geometric, open-apertured, with a slightly aeronautical condensed texture that places X-Chair in the "performance tool" category rather than lifestyle furniture. The brand's palette is built almost entirely from eight interlocking grays (#e2e2e2, #e0e0e0, #dedede, #d9d9d9, #c7c7c7, #c4c4c4, #bfc0c0, #939393) that create a tiered surface system — each layer a half-stop darker than the last, giving product photography maximum breathing room without reaching for decorative color. Into this grayscale architecture, a single chromatic force — #ea212e — governs every primary CTA, sale badge, and urgency callout with deliberate precision. The dark navy #2d3142 and slate-steel #4f5d75 appear in technical trust blocks: ergonomic specification tables, warranty terms, certification seals — copy that must read as engineered rather than sold. Component rounding is restrained: button corners sit at `{rounded.xs}`, card containers at `{rounded.sm}`, never approaching the soft pill shapes of lifestyle brands. The sage note in #ced7cf surfaces in specific product colorway contexts — a quiet departure that signals the chair exists beyond its signature black-and-gray world. Baskerville provides editorial counterpoint in testimonial headlines and long-form copy blocks, a serif intrusion that creates brief warmth inside an otherwise systematic sans-serif architecture. Navigation runs Exo2-SemiBold with wide tracking at 13–14px, echoing the precision of technical instrument manuals. The overall effect is a brand that earns credibility through typographic and chromatic restraint, letting the single red voltage land with maximum force when it finally appears on screen.

colors:
  primary: "#ea212e"
  primary-hover: "#d41928"
  primary-active: "#c41a26"
  primary-disabled: "#f4a0a5"
  navy: "#2d3142"
  steel: "#4f5d75"
  slate: "#67758b"
  sage: "#ced7cf"
  ink: "#0b0b0b"
  body: "#4d4d4d"
  muted: "#717171"
  muted-soft: "#939393"
  hairline: "#e2e2e2"
  hairline-mid: "#d9d9d9"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#f0f0f0"
  surface-mid: "#e2e2e2"
  surface-strong: "#c7c7c7"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Exo 2', 'Exo2-Bold', Arial, Helvetica, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Exo 2', 'Exo2-Bold', Arial, Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Exo 2', 'Exo2-SemiBold', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Exo 2', 'Exo2-SemiBold', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Exo 2', 'Exo2-SemiBold', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Exo 2', 'Exo2-Medium', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Exo 2', 'Exo2-Regular', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Exo 2', 'Exo2-Regular', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Exo 2', 'Exo2-Regular', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-lg:
    fontFamily: "'Exo 2', 'Exo2-Bold', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  button-md:
    fontFamily: "'Exo 2', 'Exo2-Bold', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Exo 2', 'Exo2-Bold', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Exo 2', 'Exo2-SemiBold', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.04em
  label-sm:
    fontFamily: "'Exo 2', 'Exo2-Medium', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.06em
    textTransform: uppercase
  editorial-serif:
    fontFamily: "Baskerville, 'Baskerville Old Face', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: -0.1px
  spec-mono:
    fontFamily: "monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

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
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 52px
    border: none
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 52px
    border: "2px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.ink}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.navy}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoWidth: 140px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    shadow: "0 8px 24px rgba(0,0,0,0.10)"
  promo-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    height: 36px
    padding: "0 {spacing.base}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    imageBackground: "{colors.surface-card}"
    padding: "{spacing.base}"
    shadow: none
  product-card-hover:
    border: "1px solid {colors.steel}"
    shadow: "0 4px 16px rgba(45,49,66,0.10)"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-bestseller:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.body}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaStyle: "button-primary"
    minHeight: 560px
    overlayOpacity: 0.45
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
  product-configurator:
    backgroundColor: "{colors.canvas}"
    sectionLabelTypography: "{typography.label-sm}"
    optionLabelTypography: "{typography.body-sm}"
    activeOptionBorder: "2px solid {colors.primary}"
    inactiveOptionBorder: "1px solid {colors.hairline}"
    swatchSize: 32px
    swatchRounded: "{rounded.full}"
    containerBorder: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
  color-swatch:
    size: 28px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderSelected: "2px solid {colors.primary}"
    gap: "{spacing.sm}"
  sticky-atc:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.title-sm}"
    ctaStyle: "button-primary"
    height: 68px
    zIndex: 100
  trust-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.navy}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.navy}"
    headerTextColor: "{colors.on-dark}"
    headerTypography: "{typography.label-sm}"
    rowTypography: "{typography.body-sm}"
    altRowBackgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    bodyTypography: "{typography.body-md}"
    headlineTypography: "{typography.editorial-serif}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    accentBorder: "3px solid {colors.primary}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    linkColor: "#c7c7c7"
    headingTypography: "{typography.label-sm}"
    linkTypography: "{typography.body-sm}"
    borderTop: none

## Components

### Buttons

**`button-primary`** — The brand's only chromatic force: #ea212e fill, white Exo2-Bold uppercase at 16px with 0.06em tracking, clipped at `{rounded.xs}` (2px) corners that refuse any softness. Hover transitions to `{colors.primary-hover}` (#d41928); active state deepens to `{colors.primary-active}` (#c41a26). Disabled renders in `{colors.primary-disabled}` — a desaturated blush — keeping the shape legible without competing with live CTAs on the page.

**`button-secondary`** — `{colors.canvas}` fill bounded by a 2px `{colors.ink}` border, matching uppercase Exo2-Bold at 14px. Hover fills with `{colors.surface-soft}` while the ink border holds, signaling state change without introducing color. Used alongside the primary CTA for actions like "Compare" or "View Details."

**`button-ghost`** — Transparent background, `{colors.primary}` red text with underline. Appears inline in editorial zones — "See all reviews," "Read the full story" — where a full button shape would crowd the layout.

### Navigation

**`nav-bar`** — 72px fixed header on `{colors.canvas}` with a `{colors.hairline}` bottom border. Logo anchors left at 140px; center cluster holds category links in `{typography.nav-link}` (Exo2-SemiBold, 14px, 0.04em tracking); right cluster carries search, account, and cart icons. Hover over a category link drops a `nav-dropdown` panel with `{rounded.sm}` corners and a low navy-tinted shadow.

**`promo-bar`** — 36px announcement strip in `{colors.primary}` red, positioned above the nav. White `{typography.label-sm}` uppercase text carries shipping thresholds or promotional codes. The red-on-red stacking with the primary CTA is intentional pressure — the page opens with urgency before the user has scrolled.

### Product Cards

**`product-card`** — White canvas with a 1px `{colors.hairline}` border and `{rounded.sm}` corners. Product image renders on a `{colors.surface-card}` (#f0f0f0) field. Title in `{typography.title-sm}`, price in `{typography.title-md}`. Hover upgrades the border to `{colors.steel}` with a shallow `rgba(45,49,66,0.10)` shadow. Absolute-positioned `badge-sale` or `badge-new` strips anchor to the top-left of the image zone with `{rounded.none}` — frameless rectangles that maximize the urgency signal.

**`badge-sale`** — Flat `{colors.primary}` with no radius. The hardest chromatic element on the card surface, deliberately raw-edged.

**`badge-bestseller`** — Same flat geometry in `{colors.surface-mid}` with `{colors.body}` text. A subdued social-proof mark that doesn't compete with the sale badge.

### Product Configurator

**`product-configurator`** — X-Chair's signature customization panel: fabric/color, lumbar type, headrest, and add-ons each occupy a labeled section in `{typography.label-sm}` uppercase. Color selections use `color-swatch` circles (28px, `{rounded.full}`) with a 2px `{colors.primary}` outline on the selected state. Non-color option tiles are `{rounded.xs}` bordered rectangles that transition from a `{colors.hairline}` to a `{colors.primary}` border on selection. The entire panel sits in a `{rounded.sm}` container with a `{colors.hairline-soft}` boundary, contained and systematic.

**`color-swatch`** — 28px circles with `{rounded.full}`, a 2px transparent border at rest that resolves to `{colors.primary}` red on selection. Gap between swatches is `{spacing.sm}`. The swatch set can include the `{colors.sage}` (#ced7cf) colorway among standard blacks, grays, and fabric options.

**`sticky-atc`** — Sticky add-to-cart bar that activates after the main product CTA scrolls out of viewport. 68px tall, `{colors.canvas}` background, `{colors.hairline}` top border. Left side shows chair name and selected configuration in `{typography.title-sm}`; right side holds the `button-primary` CTA. z-index 100.

### Trust and Specification

**`trust-bar`** — Full-width band in `{colors.surface-soft}`, with icon+label groups distributed evenly across the row. Icons tinted `{colors.navy}`. Labels in `{typography.body-sm}`. Carries warranty duration, weight capacity, BIFMA and CE certification callouts. Appears directly below the hero and again below the primary product description.

**`spec-table`** — Data-dense table with a `{colors.navy}` header row in white `{typography.label-sm}`. Body rows alternate between `{colors.canvas}` and `{colors.surface-soft}`. Cells hold weight capacity, adjustability ranges, and material breakdowns. Container is `{rounded.sm}` with 1px `{colors.hairline}` cell borders; column values may use `{typography.spec-mono}` for numeric precision.

### Editorial

**`testimonial-card`** — `{colors.surface-soft}` background, `{rounded.sm}` corners. A 3px `{colors.primary}` left border marks the entry edge — the one place red appears not as a CTA but as editorial punctuation. Headline renders in `{typography.editorial-serif}` (Baskerville, 28px), the only serif moment in the product interface. Quote body in `{typography.body-md}`, padding `{spacing.xl}`.

### Footer

**`footer`** — Full `{colors.navy}` (#2d3142) background, a hard visual cut from the canvas content above — no top border, no gradient transition. Column headings in `{typography.label-sm}` uppercase white. Links in `{typography.body-sm}` at #c7c7c7 — dimmed, not pure white, preserving hierarchy within the dark zone. Social icons and legal links anchor at the base row.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; `promo-bar` truncates to single offer line; `product-configurator` opens as bottom sheet; `sticky-atc` CTA goes full-width; hero height reduces to 320px |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links only, mega-menu sub-items omitted; configurator runs full-width below product images; `trust-bar` wraps to 2×2 icon grid |
| Desktop | 1128–1440px | Three-column product grid; full mega-menu on hover; configurator appears as side panel alongside images; hero at full 560px min-height |
| Wide | > 1440px | Max-width container capped at 1440px centered; four-column grid for accessories; hero image bleeds full-width behind the capped content zone |

### Touch Targets

- All interactive controls minimum 44×44px on mobile
- `color-swatch` expands from 28px to 36px on mobile viewports
- Nav hamburger icon tap zone 44×44px
- `sticky-atc` CTA button runs full-width on mobile, minimum 52px height
- Dropdown accordion headings in mobile nav drawer minimum 48px tall

### Collapsing Strategy

- Mega-menu → single-depth accordion inside hamburger drawer at mobile
- Horizontal `trust-bar` icon row → 2×2 grid at tablet, stacked single-column list at mobile
- `spec-table` → horizontally scrollable container below 744px, no content truncation
- `product-configurator` → inline stacked sections at tablet, bottom sheet drawer at mobile
- Footer multi-column grid → stacked accordion with collapsed section headings at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No `meta theme-color` extracted; browser chrome accent color undefined
- `primary-hover` (#d41928) and `primary-active` (#c41a26) are computed estimates from the extracted #ea212e — live Shopify CSS may define distinct values
- Button border-radius not directly measurable from static extraction; `{rounded.xs}` (2px) inferred from the industrial aesthetic
- Baskerville usage context inferred from font-stack presence; specific component placement rules not confirmed from live DOM
- `#ced7cf` sage color confirmed in palette extraction but specific component assignments (product colorway swatch vs. UI element) unverified
- Icon library and glyph set not identified — SVG assets inaccessible via static extraction
- Animation timings, easing curves, and transition durations not captured
- `promo-bar` scroll behavior (sticky vs. dismissible on scroll) unconfirmed
- Mobile nav drawer nesting depth and animation style unconfirmed
- Dark mode support status unknown
