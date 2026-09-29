---
version: alpha
name: "Ohaus"
source_url: "https://www.ohaus.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Calibration certificates, GLP/GMP compliance stamps, and class-E weight traceability chains — OHAUS treats every product page with the same documentary rigour a metrologist brings to a reference standard. The homepage arranges product families the way a lab manual arranges protocols: by application discipline, load capacity, and measurement readability rather than by marketing narrative. The single color reliably extractable from the live site — #eeeeee, the confirmed surface tone — sets the entire register: the flat, neutral gray of brushed aluminum panel or a poured epoxy countertop, neither warm nor sterile, just stable and functional. Everything else in the palette is subordinate to that baseline.

  No brand web font was capturable at extraction time; FontAwesome (an icon library) was the only font-family detected, indicating the brand's actual typefaces load via JS. What the page structure reveals is a typographic hierarchy built for specification scanning rather than emotional persuasion: model designations, maximum capacities, and tolerance figures demand that numbers be readable under lab lighting at arm's length. A monospace scale handles numeric spec values throughout product detail pages, visually separating measurement data from prose descriptions. Display type runs at modest weights — the brand earns authority through specification depth, not typographic muscle.

  The primary brand blue — conservatively estimated at #004B8D from publicly visible OHAUS catalog covers and trade materials — anchors all primary CTAs, active nav states, and focus rings. Corners are nearly square at the button level (4px radius) and softly rounded at the card level (8px), a geometry that reads as precise and deliberate rather than friendly. The spec-table component is arguably the most load-bearing UI surface on the site: dense two-column rows of tolerance, repeatability, and environmental rating data that a purchasing engineer or lab manager reads before a product image. Red appears in sub-brand badge work and regulatory warning indicators, kept narrow in scope so it retains signal value. The `{colors.surface-soft}` #eeeeee tone repeats as the hero band background, section dividers, and the header row of every spec table, giving the site a low-contrast but coherent visual anchor.

colors:
  primary: "#004B8D"
  primary-active: "#003570"
  primary-disabled: "#99BFD8"
  ink: "#1A1A1A"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#DDDDDD"
  canvas: "#FFFFFF"
  surface-soft: "#EEEEEE"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  accent-red: "#C8102E"
  accent-red-light: "#FDECEA"
  success: "#16A34A"
  warning: "#F59E0B"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  part-number:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0

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
    height: 44px
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 44px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
  nav-top-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    iconColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    imageAspect: "4/3"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} 0"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    valueTypography: "{typography.spec-label}"
    labelTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    rowPaddingY: "{spacing.sm}"
  product-badge-cert:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-badge-new:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  part-number-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.part-number}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons
**`button-primary`** — A 44px-tall, nearly square-cornered (`{rounded.sm}`, 4px) CTA filled with `{colors.primary}` blue and white text in `{typography.button-md}` at 600 weight. The geometry signals precision and restraint rather than consumer friendliness — there is no pill shape anywhere in the primary action flow. Active state deepens to `{colors.primary-active}`; disabled state fades the fill to `{colors.primary-disabled}` while retaining white text.

**`button-secondary`** — Outlined sibling at the same height and corner radius, with a 1px `{colors.primary}` border and matching blue label on a white ground. Used for parallel actions — "Compare Models," "Download Datasheet," "Add to Quote Cart" — that sit alongside but defer to the primary conversion CTA without visual noise.

**`button-text`** — Inline `{colors.primary}` link-style button with no background or border, in `{typography.button-sm}`. Appears in dense spec tables, breadcrumb contexts, and accordion triggers where a bordered button would overwhelm the surrounding data layout.

### Inputs
**`text-input`** — Clean 44px rectangle with a 1px `{colors.hairline}` resting border sharpening to `{colors.primary}` on focus, `{rounded.sm}` corners. Placeholder renders in `{colors.muted}`. Used for search queries, capacity-range filter fields, and quote-request form entries throughout the catalogue.

**`search-bar`** — Extends `text-input` with a magnifier glyph (FontAwesome) in `{colors.muted}` on the trailing edge. Filters the product catalogue by model name, part number, or application keyword. On desktop the bar is persistent in the nav zone; on mobile it expands from an icon tap.

### Navigation
**`nav-top-strip`** — A 36px utility banner in `{colors.primary}` carrying quick-links (Support, Find a Dealer, Where to Buy, Login) in `{typography.caption}` on `{colors.on-primary}`. This is the single most visible expression of the brand's primary blue across the page load — functional rather than decorative. Collapses entirely at the mobile breakpoint.

**`nav-bar`** — 64px white bar with a 1px `{colors.hairline}` bottom border. OHAUS logo sits left; product-family mega-menu links center; search icon, region selector, and account icon anchor the right. `{typography.nav-link}` at 500 weight keeps the menu legible without asserting itself over product imagery.

**`breadcrumb`** — Compact trail in `{typography.caption}`, `{colors.muted}` for ancestor crumbs, `{colors.ink}` for the active (current) page. Slash separator in `{colors.hairline}`. Positioned immediately below the nav bar on product family and product detail pages, essential wayfinding in a deep catalogue hierarchy.

### Cards
**`product-card`** — White (`{colors.surface-card}`) card with a 1px `{colors.hairline}` border, `{rounded.md}` corners, and `{spacing.base}` padding. Product image occupies the top half at 4:3 aspect. Below: model name in `{typography.title-md}`, part number in `{typography.part-number}` (monospace, uppercase, spaced), a one-line specification callout (maximum capacity or readability) in `{typography.body-sm}`, and a `{colors.primary}` "View Details" button-text link or full `button-primary` anchoring the card footer. Certification and recency badges (`product-badge-cert`, `product-badge-new`) overlay the image corner.

**`category-tile`** — A `{colors.surface-soft}` (#eeeeee) tile with `{rounded.md}` radius, centered product-family icon (FontAwesome or product SVG), and label in `{typography.title-sm}`. Border transitions from `{colors.hairline}` to `{colors.primary}` on hover, providing a clear affordance. Used on the homepage and product-family landing pages to present eight to twelve measurement disciplines at a glance.

### Spec Table
**`spec-table`** — The load-bearing UI surface on every product detail page. A two-column table: labels in `{typography.body-sm}`, values in `{typography.spec-label}` (monospace, 13px, 0.2px letter-spacing) so numeric measurement data is visually distinct from prose descriptions. The header row ("Specifications") uses `{colors.surface-soft}` fill. Every data row carries a 1px `{colors.hairline}` bottom border with `{spacing.sm}` vertical padding. A purchasing engineer or lab manager reads this table before the hero image.

### Badges
**`product-badge-cert`** — Small rectangular tag in `{colors.surface-soft}` with `{colors.muted}` text and a 1px `{colors.hairline}` border. Carries certification stamps — ISO, NTEP, OIML, CE — as terse uppercase abbreviations in `{typography.caption}`. Multiple badges stack horizontally below the part number on product cards and detail pages.

**`product-badge-new`** — Same geometry as the cert badge but filled with `{colors.accent-red}` and `{colors.on-primary}` text. Marks newly released models in the catalogue. Kept narrow in deployment so the red retains signal value; it appears on the image corner, not repeated in the card body.

**`part-number-tag`** — Monospaced capsule in `{colors.surface-soft}` with `{colors.muted-soft}` text, in `{typography.part-number}` (uppercase, 0.5px letter-spacing). Renders the model/SKU string immediately below the product title throughout search results and category grids so engineers can identify parts without reading prose.

### Hero
**`hero`** — Full-width `{colors.surface-soft}` band — the one confirmed site color — carrying headline in `{typography.display-xl}` and a short descriptor in `{typography.body-md}`. No image overlay on the headline; product photo or family render sits right-column in a two-column layout on desktop. Primary CTA is `button-primary`. Avoids stock lifestyle photography in favor of clean product renders against neutral backgrounds, consistent with the precision-equipment context.

### Footer
**`footer`** — Dark (`{colors.ink}`) full-width band with four to five link columns covering Products, Support, About, Resources, and Legal. Link text uses `{colors.surface-soft}` for contrast. Bottom bar carries copyright, region/language selector, and social icons. Typography throughout in `{typography.body-sm}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; `nav-top-strip` hidden; hamburger nav drawer; hero stacks image below headline; `spec-table` scrolls horizontally; category tiles stack 2×N |
| Tablet | 744–1128px | Two-column product grid; main nav condenses to icon+label bar; category tiles shift to 3-column row; hero remains two-column but image scales down |
| Desktop | 1128–1440px | Three- or four-column product grid; full mega-menu with product-family columns; two-column hero; `spec-table` full-width with label and value columns side by side |
| Wide | > 1440px | Content max-width ~1400px centered; grid stays four columns; hero gains increased horizontal padding; no new columns added |

### Touch Targets
- All interactive buttons minimum 44px tall, enforced by `height: 44px` on `button-primary` and `text-input`
- `nav-bar` links carry 44px minimum tap zone even when visual label height is smaller
- Full `product-card` surface area is tappable; secondary actions (compare, quick-view) surface on explicit tap rather than hover
- `category-tile` entire bounding box is a single link — no sub-targets on mobile
- Badge overlays are non-interactive; they do not need minimum tap sizing

### Collapsing Strategy
- `nav-top-strip` collapses first at mobile breakpoint; utility links move into the hamburger drawer
- Mega-menu folds to a stacked accordion drawer triggered by hamburger icon; product families expand individually
- Hero two-column layout stacks vertically; product image moves below the headline and CTA
- `spec-table` acquires `overflow-x: auto` wrapper rather than truncating measurement values — numeric precision must not be cut off
- Product grid steps from four → two → one column at Desktop → Tablet → Mobile
- Footer link columns stack vertically on mobile with expand/collapse disclosure toggles per section

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#eeeeee) was reliably extracted from the live site; the entire palette beyond surface-soft is estimated from publicly visible OHAUS catalog covers, trade materials, and product photography — production tokens may differ
- Primary brand blue (#004B8D) is a conservative estimate from documented visual materials; the exact production hex is unconfirmed
- Accent red (#C8102E) appears in OHAUS sub-brand and product-line materials but was not confirmed from live site extraction
- No brand web font was captured — FontAwesome (icon library) was the only font-family detected; body, display, and UI typefaces load via JS and could not be identified; system font stack used as a safe fallback throughout
- No meta theme-color was set on the page, removing a common shortcut to the primary brand color
- Navigation depth and mega-menu taxonomy (number of product-family columns, sub-category structure) inferred from page title patterns; live DOM structure was not captured
- Exact corner radii in production may differ from the `{rounded.sm}` (4px) and `{rounded.md}` (8px) estimates, which are based on the precision-instrument aesthetic convention rather than extraction
- Icon glyph set beyond FontAwesome — product-category illustrations, certification logos — not characterized
- Regional e-commerce flow (quote cart, dealer-finder, configurator) UI patterns were not observed at extraction time
