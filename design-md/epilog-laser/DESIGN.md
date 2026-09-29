---
version: alpha
name: "Epilog Laser"
source_url: "https://www.epiloglaser.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Machine photography dominates every page — the Fusion Edge, Zing, and MUSE series are lit against near-black slate (#2b2e38) in hero sections that feel closer to darkroom exposures than lifestyle marketing. That darkness is the canvas; the brand's voltage arrives in sky-blue (#6dcff6 and its deeper cousins #085e91 and #005689), colors that echo both the visible spectrum of a CO₂ laser beam and the clean-room palette of precision manufacturing. Epilog runs the entire site on Arial with no custom typeface and no web-font payload, trusting machine specs, cut-speed charts, and wattage comparisons to carry authority over typographic gesture. The system-font stack is a deliberate B2B signal: this brand sells to shop owners and engineers who scan spec tables before they read headlines.

  Red (#dd3737) is deliberately narrow in application — safety callouts, urgent badges, and nothing else. It never bleeds into general marketing surface, keeping the overall read disciplined rather than promotional. Deep blues (#005689, #085e91) anchor navigation and primary CTAs; the lighter sky accent (#6dcff6) lifts hero gradients and series identification badges. Corner radii stay minimal throughout, barely above square ({rounded.xs} to {rounded.sm}), matching the machined-metal aesthetic of the hardware itself. Section spacing runs wide — Epilog separates product families, application galleries, and spec blocks with room enough that the page breathes despite its dense technical content. A note on the extracted palette: many colorful hex values (#ff6900, #fcb900, #9b51e0, and others) appear to be WordPress Gutenberg editor swatch artifacts rather than brand tokens and have been excluded; the true brand vocabulary is the blue-slate-red triad defined here.

colors:
  primary: "#085e91"
  primary-light: "#6dcff6"
  primary-lighter: "#8de0ff"
  primary-dark: "#005689"
  primary-active: "#1e77a6"
  primary-disabled: "#abb8c3"
  accent-sky: "#6dcff6"
  danger: "#dd3737"
  danger-dark: "#cf2e2e"
  danger-deep: "#571313"
  ink: "#2b2e38"
  body: "#32373c"
  muted: "#555555"
  muted-soft: "#95979c"
  hairline: "#abb8c3"
  canvas: "#ffffff"
  surface-dark: "#2b2e38"
  surface-charcoal: "#32373c"
  surface-soft: "#f5f7fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica CY', 'Nimbus Sans L', sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, 'Helvetica CY', 'Nimbus Sans L', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Arial, 'Helvetica CY', 'Nimbus Sans L', sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "Arial, 'Helvetica CY', 'Nimbus Sans L', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica CY', 'Nimbus Sans L', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica CY', 'Nimbus Sans L', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica CY', 'Nimbus Sans L', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica CY', 'Nimbus Sans L', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica CY', 'Nimbus Sans L', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "Arial, 'Helvetica CY', 'Nimbus Sans L', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica CY', 'Nimbus Sans L', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Arial, 'Helvetica CY', 'Nimbus Sans L', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "Arial, 'Helvetica CY', 'Nimbus Sans L', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.1px
  table-header:
    fontFamily: "Arial, 'Helvetica CY', 'Nimbus Sans L', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.6px
    textTransform: uppercase
  table-cell:
    fontFamily: "Arial, 'Helvetica CY', 'Nimbus Sans L', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
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
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 26px
    height: 44px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 26px
    height: 44px
  button-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "none"
  nav-dropdown:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    hoverBackgroundColor: "{colors.primary-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    shadow: "0 2px 8px rgba(0,0,0,0.08)"
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    accentColor: "{colors.accent-sky}"
    minHeight: 520px
    padding: "{spacing.section} {spacing.xl}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.table-header}"
    cellTypography: "{typography.table-cell}"
    cellTextColor: "{colors.body}"
    rowAlternateBackground: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
  machine-series-badge:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-dark}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  feature-callout:
    backgroundColor: "{colors.surface-soft}"
    borderLeft: "4px solid {colors.primary}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.title-md}"
    padding: "{spacing.lg}"
    rounded: "{rounded.xs}"
  alert-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
  application-card:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    overlayColor: "rgba(43,46,56,0.78)"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    aspectRatio: "4/3"
  demo-request-form:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.primary-light}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "2px solid {colors.primary}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Industrial blue (#085e91) fill, white bold 15px Arial, {rounded.xs} corners that match the machined-edge aesthetic throughout. Hover shifts to `{colors.primary-active}` (#1e77a6); disabled fades to `{colors.primary-disabled}` (#abb8c3). Primary CTAs are "Request a Demo", "Get a Quote", and "Configure Your Laser" — conversion-focused and consistently above the fold on every product page.

**`button-secondary`** — Transparent background with a 2px solid `{colors.primary}` border and matching ink. Used alongside `button-primary` for secondary actions: "Download Brochure", "View Accessories", "Compare Models". Hover fills to `{colors.primary}` with white text.

**`button-ghost`** — White border and white text, used exclusively on `{colors.surface-dark}` hero backgrounds where a second CTA (e.g., "Watch Demo Video") accompanies a primary action without competing for attention.

**`button-danger`** — `{colors.danger}` (#dd3737) fill, reserved for support and safety documentation contexts. Never appears on general product marketing surfaces.

### Text Input

**`text-input`** — White field, 1px `{colors.hairline}` border that activates to `{colors.primary}` blue on focus, {rounded.xs} corners. Height 42px keeps it near the 44px touch minimum. Used in quote forms, dealer-locator search, and newsletter capture. Placeholder in `{colors.muted-soft}` (#95979c).

### Navigation

**`nav-bar`** — Full-width dark slate (#2b2e38) at 60px height, no border-bottom needed since the stark contrast against the white page body acts as the separator. Bold 14px Arial links in white, organized by machine series (Fusion Edge, MUSE, Zing) and use-case categories. Logo left, "Contact" and "Request Demo" anchor right — the latter rendered as a compact `button-primary` in the nav rail. Mega-menus drop on hover with machine thumbnails and spec highlights inline.

**`nav-dropdown`** — Extends the nav's dark slate, hover rows highlight to `{colors.primary-dark}` (#005689). Typography at `{typography.body-sm}` with machine family sub-groupings. Mega-menus show a thumbnail grid of machines at left and application categories at right.

### Product Card

**`product-card`** — White surface, 1px `{colors.hairline}` border, `{rounded.xs}` corners, and a shallow drop shadow. Machine name in `{typography.title-md}` (18px bold), model descriptor in `{typography.body-sm}`. A `machine-series-badge` (sky-blue pill) sits top-left naming the product line. Card footer shows wattage range and work area in `{typography.spec-label}` uppercase; a `button-primary` at the card bottom drives to the model detail page.

### Hero

**`hero-dark`** — Full-width dark slate (#2b2e38) section with machine photography right-aligned or centered. Headline in `{typography.display-xl}` (42px bold white); subhead in `{typography.body-md}` white at 85% opacity. A sky-blue (#6dcff6) gradient stripe or glow accent echoes the laser-beam motif at the right edge. Min-height 520px on desktop. CTA row stacks `button-primary` ("Request a Demo") beside `button-ghost` ("Watch in Action").

### Spec Table

**`spec-table`** — The site's primary conversion tool for comparing laser models. Header row in `{colors.primary}` fill with white `{typography.table-header}` uppercase labels. Body rows alternate between white and `{colors.surface-soft}`. No corner radius ({rounded.none}) — edges stay hard and grid-like, matching engineering documentation conventions. A checkbox row above the table lets users select 2–3 machines for a highlighted side-by-side column comparison.

### Machine Series Badge

**`machine-series-badge`** — Compact sky-blue pill (`{colors.primary-light}` bg, `{colors.primary-dark}` text) in `{typography.spec-label}` uppercase at {rounded.xs}. Labels product series (FUSION EDGE, MUSE FIBER, ZING 24) on cards, hero sections, and inline spec callouts. Stays informational — never uses danger red.

### Feature Callout

**`feature-callout`** — Soft-grey (`{colors.surface-soft}`) block with a 4px left border in `{colors.primary}`. Label in `{typography.spec-label}` uppercase, value in `{typography.title-md}` bold dark ink. Used in machine detail pages to surface key specs: MAX WORK AREA, LASER POWER (WATTS), MAX RESOLUTION (DPI). Typically a grid of 3–4 callouts immediately below the hero, before the full spec table.

### Application Card

**`application-card`** — Dark-background photo tile showing engraved trophies, cut acrylic, marked aerospace components. Dark overlay (`rgba(43,46,56,0.78)`) over the photo with title text in white `{typography.title-sm}`. 4/3 aspect ratio; hover lifts the overlay opacity to reveal a one-line descriptor. Grid of 6–8 tiles spans the applications gallery section.

### Demo Request Form

**`demo-request-form`** — Soft-grey (`{colors.surface-soft}`) padded container with a 1px `{colors.hairline}` border and `{rounded.sm}`. Heading in `{typography.display-md}` (26px bold); supporting copy in `{typography.body-md}`. Fields: name, company name, email, phone, machine interest (dropdown). Single full-width `button-primary` at the bottom. All fields visible at once — no progressive disclosure — matching the expectations of B2B buyers who want to indicate intent in one pass.

### Footer

**`footer`** — Dark slate matching the nav, separated from the page body by a 2px `{colors.primary}` top border that visually closes the product loop. Four-column grid: Products, Industries, Resources, Company. Column headings in `{typography.title-sm}` bold white; links in `{colors.primary-light}` (#6dcff6) for legibility on dark. Bottom bar: copyright, privacy policy, terms in `{colors.muted-soft}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger drawer with accordion product series; hero stacks to single column (headline above image); spec table horizontally scrollable with fixed first column; feature callouts stack 1-column; product cards full-width vertical list |
| Tablet | 744–1128px | 2-column product card grid; hero maintains side-by-side at reduced padding; spec table shows 3 columns with horizontal scroll; nav shows top-level links with tap-to-expand mega-menu |
| Desktop | 1128–1440px | Full mega-nav; 3-column product grid; hero at full 520px min-height; all spec table columns visible; feature callouts in 4-column row |
| Wide | > 1440px | Content container max-width 1280px centered; hero background extends edge-to-edge; application card grid expands to 4 columns |

### Touch Targets
- All buttons minimum 44px height — `button-primary`, `button-secondary`, `button-ghost` all set to `height: 44px`
- Nav drawer links at 48px row height on mobile
- Spec table rows at minimum 44px height when used as interactive model selectors
- Form fields at 42px height (within 2px of minimum; acceptable with label tap area above)
- Product cards tap-target covers the entire card surface, not just the headline link

### Collapsing Strategy
- Mega-nav collapses to hamburger at < 744px; machine series exposed as accordion items inside the slide-in drawer
- Hero two-column layout (text left, machine image right) collapses to stacked single column; image moves below headline on mobile
- Feature callout grid: 4-col → 2-col at tablet → 1-col at mobile
- Spec table: first column (model name) fixed, remaining columns scroll horizontally on < 744px; a "Compare" button condenses to icon-only on mobile
- Application card grid: 4-col (Wide) → 3-col (Desktop) → 2-col (Tablet) → 1-col (Mobile)
- Footer four-column grid: 2-col at tablet; accordion (all closed by default) at mobile to reduce scroll depth

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected — the site runs Arial / Helvetica CY / Nimbus Sans L system fonts entirely; type scale values above are inferred from B2B industrial site conventions rather than extracted computed styles
- Many extracted hex values (#ff6900, #fcb900, #7bdcb5, #00d084, #9b51e0, #8ed1fc, #0693e3, #81c784, #66bb6a, and others) are standard WordPress Gutenberg editor palette swatches, not Epilog brand tokens; they have been excluded
- No meta theme-color present in the page head — primary color assignment relies on blue-tone frequency and dominance in the extracted palette
- Icon set not confirmed — Epilog likely uses custom machine-diagram SVGs and industry-specific icons; no specific icon library (Font Awesome, Heroicons, etc.) identified
- Hover transition durations and easing curves not extractable from static snapshot; nav and card hover states above are assumed from standard industrial B2B patterns
- Dark mode support unknown — the site appears to use a fixed dark header/footer pattern with a white body canvas rather than a system-level dark/light toggle
- Product configurator UI (if present) uses dynamic components whose exact styling was not captured in static extraction
