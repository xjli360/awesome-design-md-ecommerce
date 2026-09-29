---
version: alpha
name: "Formlabs"
source_url: "https://www.formlabs.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Part numbers and resin-type codes render in Consolas and Menlo — Formlabs is one of the few hardware brands that elevates monospace into the product interface rather than confining it to documentation. Against that technical register, the primary palette is engineering-blue (#0762c8) deepened to navy (#003594) in hover and active states, punctuated by an aggressive #ff5a00 orange reserved for high-urgency CTAs and new-product badges. The canvas reads warm rather than clinical: #fefdf9 instead of pure white, with surface cards on #f3f3f3 and soft dividers at #ddd9cf — a deliberate counter-weight to the cold precision-instrument expectation of a professional 3D printer brand. Buttons are rectangular or near-rectangular (`{rounded.xs}`), signaling a hardware-spec aesthetic instead of the consumer-friendly pill radii that SaaS tools default to. Photography leans on studio-lit grey fields at #e0e0e0 and #d0d0ce, and product cards surface amber (#e1a200) for availability notices and material-compatibility callouts. The typographic scale runs Roboto at restrained weights: 48px headers at weight 700 read declarative rather than loud — engineering confidence over marketing bravado. Error and warning states split cleanly: #bd3500 burnt-orange for errors (distinct from both primary blue and accent orange), #e1a200 amber for cautions, maintaining a legible triage hierarchy across multi-step print-configuration screens. The dual-register system — Roboto for editorial copy, Consolas/Menlo for data fields — is the single clearest signal that this is a precision professional tool, not a consumer gadget.

colors:
  primary: "#0762c8"
  primary-hover: "#2763c1"
  primary-active: "#003594"
  primary-disabled: "#82afe3"
  accent-orange: "#ff5a00"
  accent-amber: "#e1a200"
  accent-blue-light: "#5db5ff"
  accent-sky: "#2299dd"
  error: "#bd3500"
  info: "#1082f0"
  ink: "#1f1f1f"
  body: "#4b5563"
  muted: "#63666a"
  muted-light: "#9ca3af"
  hairline: "#e0e0e0"
  hairline-warm: "#ddd9cf"
  hairline-soft: "#e5e7eb"
  canvas: "#fefdf9"
  surface-soft: "#f6f6f6"
  surface-card: "#f3f3f3"
  surface-warm: "#f3f0e9"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  deep-navy: "#003594"
  near-black: "#111110"
  warm-black: "#232018"

typography:
  display-xl:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  mono-data:
    fontFamily: "Consolas, 'Courier New', 'Liberation Mono', Menlo, Monaco, SFMono-Regular, ui-monospace, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  mono-label:
    fontFamily: "Consolas, 'Courier New', 'Liberation Mono', Menlo, Monaco, SFMono-Regular, ui-monospace, monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  label-caps:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase

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
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-orange-cta:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    padding: 10px 14px
    height: 44px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    height: 44px
    padding: "0 {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  notification-banner:
    backgroundColor: "{colors.deep-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero-section:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.accent-orange}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    padding: "{spacing.section} 0"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    valueTypography: "{typography.mono-data}"
    labelTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
  badge-material:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.mono-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-availability:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.warm-black}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-new:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  part-number-label:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.mono-label}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "2px 6px"
  material-selector:
    backgroundColor: "{colors.surface-card}"
    selectedBorder: "2px solid {colors.primary}"
    defaultBorder: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    codeTypography: "{typography.mono-label}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
  print-progress-bar:
    trackColor: "{colors.hairline}"
    fillColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.warm-black}"
    textColor: "{colors.on-dark}"
    bodyTypography: "{typography.body-sm}"
    linkTypography: "{typography.nav-link}"
    separatorColor: "{colors.deep-navy}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Engineering-blue (#0762c8) with a tight `{rounded.xs}` (2px) corner radius, communicating precision over approachability. Hover deepens to `{colors.primary-hover}` (#2763c1); pressed state drops to deep navy `{colors.primary-active}` (#003594). Disabled state washes to `{colors.primary-disabled}` (#82afe3) without changing geometry — the shape stays authoritative even when inactive.

**`button-secondary`** — Outlined variant with #0762c8 text and border on warm-canvas background. Shares the 44px height and `{rounded.xs}` radius as the primary, ensuring visual alignment in side-by-side CTA pairs on product and pricing pages.

**`button-ghost`** — Tertiary neutral button for "Learn More," filter resets, and secondary nav actions. Hairline-border on transparent background; text in `{colors.ink}`. Visually recessive against both white and surface-card contexts.

**`button-orange-cta`** — The `{colors.accent-orange}` (#ff5a00) variant is reserved for hero sections, product launch banners, and promotional blocks where dark backgrounds demand a high-contrast call to action. Identical geometry to primary; intentionally limited to one per major section to preserve its urgency signal.

### Form Inputs

**`text-input`** — Warm-canvas fill, hairline border, 2px `{colors.primary}` focus ring. The 44px height matches button height for clean form layouts on configuration and checkout flows. Fields accepting serial numbers, part IDs, or print-job names swap in `{typography.mono-data}` programmatically.

**`search-bar`** — Surface-soft background distinguishes it visually from the white nav. Focus state surfaces a `{colors.primary}` border. Used in global nav and product-listing filters.

### Navigation

**`nav-bar`** — 64px tall, `{colors.canvas}` background with a subtle `{colors.hairline-soft}` bottom border. Product categories, materials, and software links render in `{typography.nav-link}` (Roboto 500 at 14px). Wordmark anchors left; account and cart icons anchor right with 44px tap targets.

**`notification-banner`** — Full-width deep-navy (#003594) strip above the nav for firmware update notices, regional shipping alerts, and event announcements. White `{typography.body-sm}` with an optional dismiss control on the trailing edge.

### Product Display

**`product-card`** — Surface-card (#f3f3f3) fill with hairline border and `{rounded.sm}` (4px) corners. Printer name in `{typography.title-md}` (Roboto 600 at 20px); material compatibility and layer resolution in `{typography.body-sm}`. A `badge-material` chip in the upper-right corner carries the resin product line code in monospace uppercase.

**`spec-table`** — The component that most clearly separates Formlabs from consumer-brand design: a two-column table where left-column labels use `{typography.body-sm}` (Roboto) and right-column values use `{typography.mono-data}` (Consolas 13px). Header rows use `{colors.surface-soft}` fill. This component anchors printer detail pages listing build volume, XY resolution, and compatible resin families.

**`part-number-label`** — Inline chip for SKUs, cartridge codes, and serial identifiers. `{typography.mono-label}` (Consolas 11px uppercase), surface-soft background, hairline border. Appears inside spec tables, order confirmations, and material-selector panels.

### Status & Feedback

**`badge-material`** — Blue chip identifying resin product lines (e.g., RIGID 10K, CASTABLE WAX) in monospace uppercase. Appears on product cards and inside material-selector tiles.

**`badge-availability`** — Amber (#e1a200) chip for stock and shipping notices. Warm-black text on amber ensures contrast without black harshness; deliberately calm against the assertive orange and blue.

**`badge-new`** — Orange (#ff5a00) chip for newly launched products or material introductions. High-contrast, intentionally scarce — one per page maximum.

**`print-progress-bar`** — A 4px-tall hairline track filled with `{colors.primary}` blue, `{rounded.full}` pill ends. Used on dashboard and order-status pages to show print completion. Non-interactive on mobile; scrub control appears on desktop only.

### Layout

**`hero-section`** — Full-width near-black (#111110) background with `{typography.display-xl}` Roboto in white. CTAs use `{colors.accent-orange}` against dark for maximum contrast. `{spacing.section}` (64px) vertical padding top and bottom; photography or 3D render bleeds to right half on desktop, collapses behind text on mobile.

**`material-selector`** — Grid of surface-card tiles, each with a monospace code label, thumbnail swatch, and a short description. Selected state applies a 2px `{colors.primary}` border. Used in the print-configuration wizard and the resin shop to guide material choice.

**`footer`** — Warm-black (#232018) background with white link columns in `{typography.nav-link}` and body copy in `{typography.body-sm}`. Deep-navy (#003594) horizontal rules divide Product, Software, and Support column groups. Contact details render in `{typography.mono-data}` to hold the technical register through to the page bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces horizontal links; hero drops from display-xl to display-md; spec-table reflows to stacked label-above-value definition list; horizontal padding collapses to 16px |
| Tablet | 744–1128px | Two-column product grid; nav consolidates secondary links into a "More" dropdown; hero maintains two-column text + image split |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with all categories visible; hero full-bleed background with left-aligned text in max-width container |
| Wide | > 1440px | Content max-width capped at ~1280px and centered; hero background extends edge-to-edge; spec-table gains optional third comparison column for side-by-side printer models |

### Touch Targets
- All buttons, nav links, and material-selector tiles minimum 44×44px
- Badge chips on mobile expand to 8px vertical padding for reliable thumb tap
- Dismiss/close icons on notification banners minimum 32×32px tap zone
- Form inputs minimum 44px height on all breakpoints

### Collapsing Strategy
- Horizontal nav collapses to hamburger below 744px; sub-menus become full-screen slide-in drawers
- Spec-tables reflow to single-column definition-list format below 744px (label above value, mono values left-aligned)
- Material-selector grid: 4 columns → 2 columns → 1 column at mobile
- Hero image moves to background on mobile; appears as foreground split panel at tablet and above
- Footer column groups stack vertically at mobile with accordion expand per group
- Notification banners persist as single-line strip at mobile; text truncates with "…" and links to a detail page

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface confirmed — Roboto inferred from extracted font stack; Formlabs may license a proprietary display face not captured by CSS sampling
- Exact button border-radius not confirmed from source CSS; 2px (xs) assumed from observed angular aesthetic
- Icon system not extractable — Formlabs uses a custom SVG glyph set for product categories, material types, and printer states; stroke weight and grid size unknown
- Dark-mode and dashboard-specific tokens not captured; the PreForm print-preparation software and Dashboard app likely carry a separate dark-surface palette
- Exact nav height not confirmed; 64px estimated from standard B2B hardware norms
- Animation and transition timing not extracted — print-progress fill animation and configuration-wizard step transitions unspecced
- Material-selector thumbnail aspect ratio and image dimensions not confirmed
- The warm off-white canvas (#fefdf9) vs pure white (#ffffff) split-point not confirmed — which surfaces use which is inferred from the extracted palette ordering
