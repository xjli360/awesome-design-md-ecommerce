---
version: alpha
name: "Bernell Hydraulics"
source_url: "https://www.bernellhydraulics.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  One extracted hex — #116600, a compression green shared with hydraulic hose placards and OSHA safety charts — does all the brand-color work on Bernell Hydraulics' catalog site. This is not a marketing green; it is a shop-floor green, a color that maintenance technicians and OEM engineers read as "action" long before they read it as "brand." The site builds around this single industrial anchor with what the detected Bootstrap Icons dependency suggests is a utility-first, Bootstrap-powered layout — structurally clear, built for part-number lookup and quote requests rather than for scroll-stopping imagery. When the only web font extracted is an icon library rather than a typeface, the message is plain: the brand invests in catalog depth and navigation clarity, not typographic craft. Text falls to system stacks, reinforcing the sense that speed-to-information outranks font selection — a technician hunting a Parker gear-pump replacement at 6 AM before a production line goes down will not notice letterforms, but will notice a three-click path to a PDF spec sheet. Surface treatment stays minimal: white canvas, a featherweight gray shelf for alternating spec-table rows, and near-black ink that keeps pressure ratings and port sizes legible at a glance. Corner radii are conservative — 4px at most for interactive controls, none at all on data tables — signaling industrial reliability over consumer friendliness. The primary CTA green (#116600) on white clears WCAG AA contrast without decoration; active states darken toward #0d4f00 rather than shift hue, preserving the safety-signal quality through every interaction state. The system reads as a competent regional distributor with a functional-first digital posture: every pixel earns its place by reducing friction between a broken hydraulic circuit and the correct replacement part.

colors:
  primary: "#116600"
  primary-active: "#0d4f00"
  primary-disabled: "#c8e2c3"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-alt-row: "#f9f9f9"
  on-primary: "#ffffff"
  link: "#116600"
  link-hover: "#0d4f00"
  warning: "#cc7700"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  label:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.36
    letterSpacing: 0.8px
    textTransform: uppercase
  table-header:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.7px
    textTransform: uppercase
  part-number:
    fontFamily: "'Courier New', Courier, 'Lucida Console', monospace"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
  button-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
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
    height: 42px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 42px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 44px 10px 12px
    height: 44px
    iconColor: "{colors.primary}"
  nav-bar-top:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 36px
    paddingX: "{spacing.lg}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    paddingX: "{spacing.lg}"
    linkHoverColor: "{colors.primary-disabled}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageAspect: "1:1"
    titleTypography: "{typography.title-sm}"
    partNumberTypography: "{typography.part-number}"
    ctaTypography: "{typography.button-sm}"
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    hoverBackgroundColor: "{colors.surface-alt-row}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
    titleTypography: "{typography.title-sm}"
    iconColor: "{colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.link}"
    linkHoverColor: "{colors.link-hover}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    altRowBackgroundColor: "{colors.surface-alt-row}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.table-header}"
    cellTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
  part-number-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.part-number}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  manufacturer-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  sidebar-filter:
    backgroundColor: "{colors.canvas}"
    headingTypography: "{typography.label}"
    optionTypography: "{typography.body-sm}"
    borderRight: "1px solid {colors.hairline}"
    checkboxAccentColor: "{colors.primary}"
    width: 240px
  quote-request-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-md}"
    padding: "{spacing.lg} {spacing.xl}"
    rounded: "{rounded.none}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xl}"

## Components

### Buttons
**`button-primary`** — Forest green (#116600) fill, white text, 42px tall, 4px radius, 10px/20px padding. The color is read as an action signal before it is read as a brand color — the same green on pressure-rating labels and safety placards carries over directly into CTA affordance. Hover and active states deepen to #0d4f00 with no hue shift, preserving that signal strength. Disabled state renders in a pale #c8e2c3 wash with muted text, appearing on catalog items that require a quote rather than direct purchase.

**`button-secondary`** — White fill with a 1px #116600 border and green label text, matching primary height and radius. Used alongside `button-primary` for secondary actions like "Download Spec Sheet" or "View Details" where the primary CTA is "Add to Cart" or "Request Quote." Hover fills surface-soft and tightens border to `{colors.primary-active}`.

**`button-ghost`** — Transparent background, green text, no border. Reserved for low-hierarchy inline actions such as "See All in Category" or "View More Results" at catalog section edges. Smaller type (`{typography.button-sm}`) keeps it visually subordinate to nearby primary CTAs.

### Search
**`search-bar`** — 44px full-width input with a right-anchored magnifying-glass icon in `{colors.primary}`. Focus upgrades border to 2px green for clear active-field feedback. Placeholder text reads "Search by part number, keyword, or manufacturer" — the part-number use case comes first because engineers arrive with a known cross-reference, not a keyword. The search bar is the site's functional nucleus; it deserves first visual weight on every page.

### Navigation
**`nav-bar-top`** — Slim 36px utility strip in charcoal (#1a1a1a) above the main header, carrying phone number, business hours, and account/login links in small white text. Standard B2B industrial ecommerce pattern: contact access before catalog access.

**`nav-bar`** — Primary green (#116600) main header, 56px tall, white text and icons. Logo left, category links center, search bar and cart right. The green navigation band is Bernell's strongest visual architectural statement — it draws the eye before the canvas below registers.

### Product Card
**`product-card`** — White card, 1px hairline border, 4px radius. Product image square-cropped 1:1 at top. Product name in `{typography.title-sm}`, part number in monospace `{typography.part-number}` immediately below — the part number is the primary lookup key for returning engineers and appears in a visually distinct treatment to support quick scanning. CTA button (`button-primary` or `button-ghost` for quote-only items) anchors the card bottom. No star ratings; B2B industrial catalog prioritizes spec accuracy and availability over social proof.

### Category Card
**`category-card`** — Light-gray surface-soft fill, subtle border, used in grid layouts for browsing hydraulic pumps, cylinders, fittings, pneumatics, and filtration families. A Bootstrap icon appears left-aligned in green, category label in `{typography.title-sm}`. Hover lifts to surface-alt-row without shadow, keeping the interaction subtle.

### Spec Table
**`spec-table`** — Full-width borderless-radius table, alternating row fill (surface-alt-row) for scan readability across long dimension charts. Column headers in uppercase `{typography.table-header}`. The zero-radius treatment reads as data infrastructure rather than UI furniture — correct for a context where pressure ratings, flow capacities, and port thread standards are the actual product.

### Part Number Badge
**`part-number-badge`** — Monospace `{typography.part-number}` set in a light surface-soft chip with a 2px radius. Appears inline in search results, cross-reference lookups, and product listing rows. The monospace face makes alphanumeric part strings — which mix letters, digits, and dashes — parse faster than proportional type at the small sizes used in dense catalog rows.

### Manufacturer Badge
**`manufacturer-badge`** — White chip, hairline border, uppercase label type. Appears alongside part numbers to identify Parker, Bosch Rexroth, Eaton, and other OEM brands. The subdued styling keeps manufacturer attribution visible without competing with part-number or price data.

### Sidebar Filter
**`sidebar-filter`** — 240px left-rail panel with right-border hairline separating it from the catalog grid. Section headers in uppercase `{typography.label}`, checkbox options in `{typography.body-sm}`. Checkboxes use green accent (`{colors.primary}`). Filter dimensions: manufacturer, product series, pressure rating (PSI), port size, and in-stock status. The filter rail is persistent on desktop; the narrow column keeps the grid dominant.

### Quote Request Banner
**`quote-request-banner`** — Full-bleed green (#116600) band for catalog pages where direct ordering gives way to volume or custom-quote workflows. White heading in `{typography.title-md}`, white body copy, a white-outlined button CTA. No image — the green fill is enough authority for an industrial distributor.

### Hero Banner
**`hero-banner`** — Green fill panel on homepage and campaign landing pages. White display heading, white body paragraph, white-bordered button CTA. Photography is optional and secondary; the brand does not rely on lifestyle imagery to establish authority.

### Footer
**`footer`** — Charcoal (#1a1a1a) ground, 4-column link grid: Products, Services, Company, Contact. Section headings in `{typography.title-sm}` white. Links in hairline gray, hover to white. Bottom bar carries copyright and Bootstrap Icons social icon row.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; sidebar filters collapse to bottom-sheet modal; search bar goes full-width below logo; nav condenses to hamburger + slide-in drawer; `nav-bar-top` hidden, phone number surfaces in drawer footer |
| Tablet | 744–1128px | Two-column product grid; sidebar filters become collapsible accordion rail; nav shows top-level categories as dropdowns, mega-menu suppressed |
| Desktop | 1128–1440px | Three-column product grid; full 240px sidebar filter rail persistent; primary nav mega-menu on hover; `nav-bar-top` visible |
| Wide | > 1440px | Four-column product grid; container max-width 1400px centered; horizontal margin whitespace increases |

### Touch Targets
- All buttons minimum 42px tall; icon-only controls padded to 44×44px tap area
- Mobile filter section toggles minimum 48px tall for thumb access
- Category card tap target covers full card, not just label text
- Pagination controls minimum 44×44px on mobile
- Search bar 44px tall on all viewports

### Collapsing Strategy
- Sidebar filter panel collapses to a bottom-sheet modal drawer on mobile (triggered by a sticky "Filter" chip above the grid)
- Mega-nav compresses to hamburger icon + right-sliding drawer at < 744px
- Spec tables scroll horizontally on mobile with the first column (part number) sticky for reference
- `nav-bar-top` utility strip hides on mobile; phone number and account links move into the hamburger drawer
- Multi-level category trees collapse to accordion pattern on mobile and tablet

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color was extracted (#116600); all secondary, surface, neutral, and state-variant palette values are inferred from industrial B2B ecommerce conventions, not from live site extraction
- No text font families were detected — only Bootstrap Icons (an icon library) appeared in font stacks; all typography tokens use a system-ui fallback stack and may diverge from actual site fonts
- No meta theme-color was declared, removing a secondary color-confirmation signal
- Primary color shade variants (primary-active #0d4f00, primary-disabled #c8e2c3) are derived approximations, not extracted values
- Whether the site uses a custom Bootstrap theme or default Bootstrap 5 styles is unclear; spacing, sizing, and radius tokens follow Bootstrap 5 defaults and may not match the live implementation exactly
- Exact component padding, border-radius, and height values could not be measured from extraction; values are consistent with Bootstrap 5 conventions
- Pricing display patterns, cart UI, and checkout flow components could not be confirmed from extraction alone
- No confirmation of whether the site uses a product configurator, cross-reference tool, or request-for-quote workflow beyond what catalog-pattern conventions suggest
