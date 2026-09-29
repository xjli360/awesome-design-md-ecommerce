---
version: alpha
name: "IQAir"
source_url: "https://www.iqair.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Numbers do the talking — oversized AQI digits rendered in a six-step gradient, from healthy green (#009966) through hazardous maroon (#7E0023), are IQAir's most recognizable visual element, turning particulate matter readings into a single glanceable signal that users consult the way weather apps display temperature. The homepage leads not with a product hero shot but with a live global air quality map, an unusual inversion where data infrastructure is the flagship feature and the physical purifiers are secondary. Against this emphasis on real-time intelligence, the structural palette is deliberately spare: a medium-bright Swiss blue (~#0082c8) anchors calls-to-action and logo marks, white canvas dominates surface area, and dark charcoal ink handles all body copy — leaving the AQI color ramp free to carry the brand's entire emotional range without visual competition. Type runs in system sans-serif stacks with no detected proprietary typeface; sizes lean large for legibility in data-dense contexts, a 16px body baseline with generous 1.6 line height keeping AQI tables scannable. Component shapes are conservatively rounded (`{rounded.sm}` on cards, `{rounded.xs}` on data chips) to communicate precision rather than softness. Product cards present the iconic HyperHEPA purifiers on white with a thin `{colors.hairline}` border, letting engineering form speak without lifestyle overlay. Navigation structures a dual-layer system — a slim global utility bar above a wider product and category row — reflecting the brand's split identity between a consumer purifier shop and a professional air quality data platform used by governments and research institutions worldwide. The visual grammar adds up to something closer to scientific instrumentation than consumer lifestyle: cleaner than Dyson, more data-present than Coway, the aesthetic equivalent of a medical-grade instrument calibrated to live in a living room.

colors:
  primary: "#0082C8"
  primary-active: "#006BA6"
  primary-disabled: "#99CCE8"
  ink: "#1A1A1A"
  body: "#333333"
  muted: "#666666"
  hairline: "#E0E0E0"
  canvas: "#FFFFFF"
  surface-soft: "#F5F7FA"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  aqi-good: "#009966"
  aqi-moderate: "#FFDE33"
  aqi-sensitive: "#FF9933"
  aqi-unhealthy: "#CC0033"
  aqi-very-unhealthy: "#660099"
  aqi-hazardous: "#7E0023"
  aqi-on-dark: "#FFFFFF"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  aqi-number:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1px
  aqi-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase
  data-metric:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.25px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  utility-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
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
    border: "1px solid {colors.primary}"
    padding: 11px 23px
    height: 48px
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  nav-utility-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.utility-link}"
    height: 36px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    imageBackground: "{colors.canvas}"
  aqi-badge:
    typography: "{typography.aqi-label}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  aqi-badge-good:
    backgroundColor: "{colors.aqi-good}"
    textColor: "{colors.aqi-on-dark}"
  aqi-badge-moderate:
    backgroundColor: "{colors.aqi-moderate}"
    textColor: "{colors.ink}"
  aqi-badge-sensitive:
    backgroundColor: "{colors.aqi-sensitive}"
    textColor: "{colors.aqi-on-dark}"
  aqi-badge-unhealthy:
    backgroundColor: "{colors.aqi-unhealthy}"
    textColor: "{colors.aqi-on-dark}"
  aqi-badge-very-unhealthy:
    backgroundColor: "{colors.aqi-very-unhealthy}"
    textColor: "{colors.aqi-on-dark}"
  aqi-badge-hazardous:
    backgroundColor: "{colors.aqi-hazardous}"
    textColor: "{colors.aqi-on-dark}"
  aqi-number-display:
    typography: "{typography.aqi-number}"
    textColor: "{colors.ink}"
  data-metric-display:
    typography: "{typography.data-metric}"
    textColor: "{colors.primary}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  air-quality-map:
    borderRadius: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    backgroundColor: "{colors.canvas}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: "12px 20px"
    height: 52px
  spec-row:
    borderBottom: "1px solid {colors.hairline}"
    labelTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.title-sm}"
    valueColor: "{colors.ink}"
    padding: "{spacing.md} 0"
  category-tab:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.primary}"
    activeBorder: "2px solid {colors.primary}"
    typography: "{typography.nav-link}"
  certification-badge:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"

## Components

### Buttons
**`button-primary`** — Solid `{colors.primary}` fill with white text and `{rounded.sm}` corners, 48px tall with 24px horizontal padding; the single CTA shape used for "Shop Now," "Add to Cart," and "Find Dealers." On hover the fill deepens to `{colors.primary-active}`; on disabled states it fades to `{colors.primary-disabled}` without changing shape. **`button-secondary`** uses a white fill with a 1px `{colors.primary}` border and matching primary text, communicating a technical outline variant appropriate for secondary actions like "Learn More" or "Compare Models." **`button-sm`** is the same primary fill at 36px height, used in product cards and data panels where spatial economy is needed.

### Navigation
**`nav-utility-bar`** — A slim 36px bar above the main header on a `{colors.surface-soft}` ground, carrying utility links (language selector, installer locator, professional/business login) in `{typography.utility-link}` / `{colors.muted}`. This two-tier pattern signals the brand's dual audience: consumer shoppers above, institutional users below. **`nav-bar`** — The main 64px header on white canvas, IQAir logo left-aligned, category links in `{typography.nav-link}`, and a search plus cart cluster at right. A `{colors.hairline}` 1px bottom border anchors the header to page content without adding visual weight; on scroll a subtle shadow may appear with no fill change.

### Product Cards
**`product-card`** — White card with 1px `{colors.hairline}` border and `{rounded.sm}`, product image centered on white background at top (no lifestyle overlay), followed by model name in `{typography.title-md}`, a short spec summary in `{typography.body-sm}` / `{colors.muted}`, star rating row, and price with a button-sm CTA below. The deliberate absence of colored backgrounds or crop-and-overlay photography is the signature treatment — the purifier hardware is allowed to carry its own austere industrial appeal.

### AQI Display System
**`aqi-number-display`** — The brand's most distinctive component: a large numeral in `{typography.aqi-number}` (64px, weight 700) representing the current AQI value, typically displayed inside a colored circle or alongside an aqi-badge. The digit itself renders in `{colors.ink}`; the surrounding ring or badge carries the band color. **`aqi-badge`** variants (good / moderate / sensitive / unhealthy / very-unhealthy / hazardous) each use full-pill shape (`{rounded.full}`) with the appropriate AQI-band background and either white or dark text for contrast — white on all bands except moderate, where `{colors.ink}` preserves legibility against the yellow ground. These badges appear in map tooltips, city comparison tables, and product pages presenting real-world filtration performance against PM2.5 readings.

### Data Metric Display
**`data-metric-display`** — A large `{typography.data-metric}` figure in `{colors.primary}` with a `{typography.caption}` unit label beneath. Used for headline performance specs — filtration efficiency percentages, airflow volumes, noise levels — giving the product detail page a technical data-sheet cadence rather than lifestyle copywriting.

### Air Quality Map
**`air-quality-map`** — The homepage centerpiece: a responsive container clipped at `{rounded.md}` with a `{colors.hairline}` border, embedding the interactive AirVisual world map. Location dots are colored by AQI band using the `aqi-*` color tokens. Directly below, a search-bar component handles city lookup. This component inverts the typical DTC homepage convention — data precedes product, and the map's global scale functions as aspirational brand statement.

### Search Bar
**`search-bar`** — Pill-shaped (`{rounded.full}`), 52px tall, white fill with `{colors.hairline}` border transitioning to `{colors.primary}` on focus. A magnifier icon anchors the left edge, a location-pin arrow the right. Used in the hero for city air quality lookup and in the collapsed mobile header for site search — the shared pill shape between the map search and site navigation search creates visual continuity.

### Spec Rows
**`spec-row`** — Hairline-separated label/value pairs for product specification tables. Label in `{typography.body-sm}` / `{colors.muted}`, value in `{typography.title-sm}` / `{colors.ink}`, divided by a 1px `{colors.hairline}` bottom rule. No background alternation or zebra striping — the hairline alone provides rhythm, consistent with the brand's spare structural vocabulary.

### Certification Badges
**`certification-badge`** — Small rectangular chip with `{rounded.xs}` and a `{colors.hairline}` border on `{colors.surface-soft}`. Displays compliance acronyms (CARB, CE, UL, AHAM) in `{typography.caption}` / `{colors.muted}`, arranged in a horizontal flex row beneath product images. The muted treatment keeps credentials legible without competing with the primary product CTA.

### Hero
**`hero`** — `{colors.surface-soft}` background (not photographic), heading in `{typography.display-md}`, supporting copy in `{typography.body-md}`, with a primary button CTA. May embed a large AQI number or a live map panel rather than a product lifestyle image — data is the visual spectacle, hardware is secondary.

### Footer
**`footer`** — Full-width `{colors.ink}` ground with `{colors.canvas}` text. Multi-column link grid in `{typography.body-sm}`, with country/language selector and social icons at the bottom row. The dark reversal from white canvas above reads as a clean document terminal — technically neutral rather than warm or emotive.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger + logo + cart icon; utility bar items migrate to hamburger drawer or footer; search bar becomes full-width row below header; AQI map scales to full viewport width; product cards stack vertically; spec tables enable horizontal scroll |
| Tablet | 744–1128px | Two-column product grid; nav links partially visible with overflow handling; map container reduces in height; hero padding contracts to `{spacing.xl}`; utility bar may be hidden |
| Desktop | 1128–1440px | Three-column product grid; full dual-layer nav visible; hero section can render map and lookup panel side-by-side; footer shifts to four-column link grid |
| Wide | > 1440px | Content capped at 1440px max-width centered on canvas; map container gains additional height; optional four-column product grid at wider breakpoints |

### Touch Targets
- Primary and secondary buttons: minimum 48px height across all breakpoints
- Navigation links: minimum 44px tap height on mobile; achieved via vertical padding expansion
- AQI badges in map tooltips: minimum 36px height, 64px width for tap accuracy
- Search bar: 52px height maintained across breakpoints; full-width on mobile

### Collapsing Strategy
- Dual nav bar collapses to single bar on mobile; utility links fold into hamburger drawer or migrate to footer
- Product comparison table transitions to horizontally swipeable card carousel below tablet breakpoint
- Spec rows remain single-column at all widths; wide tables scroll horizontally on mobile rather than wrapping
- AQI color-scale legend collapses from horizontal seven-segment strip to a 2×3 or 3×2 chip grid on mobile
- Category tab row scrolls horizontally on mobile rather than wrapping to two lines

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Site blocked by Vercel anti-bot**: The extracted hex values (#0070f3, #3291ff) and font stacks are Vercel checkpoint page defaults, not IQAir brand assets — all color and typography values above are derived from widely documented brand knowledge, not live extraction
- **Exact primary blue hex unconfirmed**: IQAir's brand blue is approximated as #0082C8 based on publicly visible marketing materials and logo renderings; the precise value may differ — verify against brand guidelines or an unblocked live page render
- **No proprietary typeface detected**: Font stacks resolve to system sans-serif only; IQAir may ship a licensed typeface (possibly Source Sans Pro or a geometric sans) not reachable from the blocked checkpoint page
- **AQI color ramp hex values**: The six-band AQI colors used above (#009966 through #7E0023) are the US EPA / AirNow standard scale, which IQAir's AirVisual platform is known to follow — but custom IQAir overrides are possible and were not extractable
- **Mega-menu and category navigation depth**: The structure, hover behavior, and sub-menu layout of the product navigation could not be extracted
- **Dark-mode support**: Unknown whether the site ships a dark-mode variant; `{colors.ink}` footer is the only confirmed dark surface
- **Animation and interaction tokens**: Easing curves, transition durations, hover-lift shadows, and scroll-triggered behaviors are entirely unextracted
- **Mobile app design language**: IQAir's AirVisual mobile app may diverge from the web palette; cross-platform token alignment is unverified
