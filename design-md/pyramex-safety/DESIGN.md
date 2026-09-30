---
version: alpha
name: "Pyramex Safety"
source_url: "https://www.pyramexsafety.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Conduit ITC Std sets the typographic register before any product loads: narrow, upright, squared at the terminals, the face reads like safety-placard lettering pressed into a digital grid — the opposite of the smooth rounded letterforms that consumer gear brands favor. The palette the live server delivers is deliberately stripped: an off-white field at #f7f7f7 (`{colors.surface-soft}`), mid-gray body text at #444444 (`{colors.body}`), and a hard black (#000000, `{colors.ink}`) that functions as both meta theme-color and primary UI anchor. No brand accent color surfaced in extraction — high-visibility yellows, oranges, and reflective silvers live only inside product photography, which carries every chromatic duty while the surrounding shell stays achromatic.

  The three Conduit cuts — conduititcstdbold, conduititcstdmedium, conduititcstdmediumitalic — map directly onto three editorial registers: assertive category headers and hero callouts get the bold cut at large display sizes; product specs, nav links, and form labels fall to medium weight; promotional asides and pull-quotes flex into medium-italic for angled energy without switching families. This mono-family discipline signals the brand treats its typographic voice as a structural identity asset.

  Corner radii stay nearly flat — `{rounded.xs}` at 2px on cards and inputs, `{rounded.sm}` at 4px on CTA buttons — reinforcing an industrial authority that refuses consumer-friendly softness. The combination of sharp corners, bold condensed type, and a high-contrast #000000/#e5e5e5 skeleton means the brand reads equally well in a printed safety data sheet and a digital product grid. Category filters, compliance badges (ANSI Z87.1, EN166, OSHA certification marks), and technical spec tables dominate the component vocabulary: this is a site built for procurement buyers reading certification ratings, not lifestyle browsers scanning editorial photography. Spacing is generous vertically — hero and section blocks breathe at `{spacing.section}` — but horizontal density is high, packing product grids tightly to maximize SKU visibility per viewport on a Shopify-hosted catalog.

colors:
  primary: "#000000"
  primary-active: "#333333"
  primary-disabled: "#e5e5e5"
  ink: "#000000"
  body: "#444444"
  muted: "#888888"
  hairline: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Conduit ITC Std', conduititcstdbold, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Conduit ITC Std', conduititcstdbold, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  display-italic:
    fontFamily: "'Conduit ITC Std', conduititcstdmediumitalic, sans-serif"
    fontSize: 28px
    fontWeight: 500
    fontStyle: italic
    lineHeight: 1.15
    letterSpacing: 0
  title-md:
    fontFamily: "'Conduit ITC Std', conduititcstdmedium, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Conduit ITC Std', conduititcstdmedium, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', Roboto, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', Roboto, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Conduit ITC Std', conduititcstdbold, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Conduit ITC Std', conduititcstdbold, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.17
    letterSpacing: 0.75px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Conduit ITC Std', conduititcstdmedium, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.25px
  spec-label:
    fontFamily: "'Conduit ITC Std', conduititcstdmedium, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.75px
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
    padding: 12px 24px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
  nav-bar-top-strip:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-italic}"
    padding: "{spacing.section} 0"
    overlayOpacity: 0.55
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    searchIconColor: "{colors.body}"
  compliance-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    border: none
  category-filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 6px 12px
  category-filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  safety-spec-row:
    borderBottom: "1px solid {colors.hairline}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    padding: "{spacing.sm} 0"
  footer:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons
**`button-primary`** — Solid black fill with white Conduit Bold uppercase text at 14px/1px letter-spacing, 4px radius, 44px tall. Active state darkens to #333333; disabled state drops to #e5e5e5 fill with muted text. The uppercase Conduit treatment at small size reads like a stenciled instruction rather than a consumer CTA.

**`button-secondary`** — White fill with a solid black 1px border and black uppercase Conduit text. Pairs with `button-primary` on light canvas backgrounds without competing for visual hierarchy.

**`button-ghost`** — Transparent background with hairline border and small Conduit Bold uppercase text at 12px. Used for low-priority actions — "View All", "Compare", export links — inside product cards and filter panels where visual weight must stay low.

### Navigation
**`nav-bar`** — Full-width black bar at 64px height with white Conduit medium nav links. A narrow utility strip (`nav-bar-top-strip`) sits above it at 36px in dark gray (#333333), carrying shipping notices, distributor login links, or regional messages. Nav links rely on the condensed typeface rather than wide spacing to stay scannable at high horizontal density. On mobile the top-level links collapse to a full-height hamburger drawer with the same black-on-white inversion.

### Search
**`search-bar`** — Off-white (#f7f7f7) background with a hairline border, 2px radius, and DM Sans placeholder text. A dark search icon anchors one end. No pill shape or rounded treatment — the bar is a functional utility strip, not a brand design moment. Can appear inline in the nav or as a full-width row on category entry pages.

### Product Card
**`product-card`** — White card with a hairline 1px border and 2px radius. Product image fills a 4:3 region at the top; model number, short name, and category tag in Conduit medium `title-sm` below; supplemental spec details in `body-sm` DM Sans. No price is shown on catalog cards in the default layout, reflecting a B2B/wholesale model. A `compliance-badge` overlays the image corner when an ANSI or EN certification applies.

### Compliance Badges
**`compliance-badge`** — Small black sharp-cornered label (`{rounded.none}`) with white Conduit `spec-label` uppercase text. Carries certification strings: "ANSI Z87.1+", "EN166", "OSHA Compliant", "NFPA 70E". Positioned as an absolute overlay on product imagery or as an inline tag row on product detail pages. Zero radius is intentional — it reads as an official mark, not a decorative chip.

### Category Filters
**`category-filter-chip`** — Soft gray fill (#f7f7f7) with hairline border and 2px radius, `body-sm` DM Sans text. Active chip inverts to black fill with white text, mirroring the primary button language. Filter rows appear as a horizontal scrolling strip on mobile; a sidebar column on desktop.

### Safety Spec Rows
**`safety-spec-row`** — Borderless table rows separated by hairline bottom dividers. Spec labels (e.g. "Lens Material", "Impact Rating", "Frame Color") render in uppercase Conduit `spec-label` at muted gray; values render in `body-sm` DM Sans at ink. Compact vertical padding (`{spacing.sm}` top and bottom) keeps dense specification grids scannable without wasted whitespace.

### Hero
**`hero`** — Full-bleed image with a 55% black overlay. Headline in `display-xl` Conduit Bold white at 52px; product family tagline or secondary statement in `display-italic` Conduit medium-italic at 28px. `button-primary` floats below on the left. Minimum 200px tall on mobile; desktop stretches to 480–600px depending on campaign.

### Footer
**`footer`** — Dark gray (#333333) background with white `body-sm` links organized in 4–5 column groups. Column headings in `title-sm` Conduit medium. Certification logos (CE, OSHA, ANSI) and social icons appear in a bottom sub-row separated by a hairline. Full-width layout collapses to stacked accordions on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, nav collapses to hamburger drawer, filter chips scroll horizontally, hero shrinks to 200px tall, category headings scale to `display-md` (32px) |
| Tablet | 744–1128px | 2–3 column product grid, nav shows top-level links with overflow menu, hero at 360px, filter panel shifts to horizontal strip above grid |
| Desktop | 1128–1440px | 4-column product grid, full horizontal nav with mega-menu dropdowns, hero at 480px, sidebar filter column visible alongside results |
| Wide | > 1440px | Max-width container (~1400px) centered with wider margins, 4–5 column grid, hero at 560px |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Filter chips maintain 44px tap height via vertical padding adjustments
- Compliance badge overlays are decorative and exempt from touch-target sizing
- Nav hamburger icon sized to 44×44px hit area regardless of visible icon size
- Spec row tap targets expand to 44px height on mobile for filter interactions

### Collapsing Strategy
- Navigation: horizontal mega-menu → hamburger drawer (full-height overlay, black background, white Conduit links)
- Filter panel: sidebar column → horizontal scrolling chip strip → collapsible accordion drawer
- Product grid: 4-col → 3-col → 2-col → 1-col across breakpoints
- Hero headline: `display-xl` at 52px scales to `display-md` at 32px on mobile
- Spec table rows collapse to stacked label/value pairs on mobile viewports
- Footer: 4-column grid → 2-column → stacked accordions with expand/collapse behavior
- Top utility strip hides on mobile to preserve nav height budget

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only three neutral hex values extracted (#e5e5e5, #f7f7f7, #444444); brand accent colors — safety yellow, hi-vis orange, warning red — did not surface and appear to load via JS or exist solely within image assets rather than CSS custom properties
- `colors.primary-active` (#333333) and `colors.muted` (#888888) are logically derived from the extracted gray range, not directly captured
- Whether Pyramex uses a high-visibility yellow primary CTA (common in PPE branding) or maintains black as the sole primary action color could not be confirmed from extraction
- Exact font-size scales and spacing tokens for Conduit ITC Std headings are estimated; no explicit CSS scale or design-token file was captured
- Product pricing display model (B2B login-gated MSRP vs. public pricing) is unclear from site extraction alone
- Animation and transition values for mega-menu dropdowns, drawer overlays, and filter panel open/close were not captured
- Exact Shopify theme grid gutter widths and responsive breakpoint pixel values were not extractable
- Whether a secondary accent color (e.g. a Pyramex red or orange for clearance/new badges) exists in the full design system is unknown
