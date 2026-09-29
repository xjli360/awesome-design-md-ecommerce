---
version: alpha
name: "Breitling"
source_url: "https://www.breitling.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The #ffc72c amber on Breitling's primary CTAs has a direct lineage to aviation instrument panels — the high-contrast warm tone that pilots learned to trust at a glance under cockpit glare. Against the brand's signature deep navy (#072c54) and near-black (#09091a) backgrounds, the amber reads less like a marketing choice and more like a functional signal, which is precisely the effect Breitling has maintained since its AOPA partnership in the 1950s. The site carries this instrument logic throughout: dark surfaces dominate hero and collection pages, navigation anchors at depth (#0e2240), and text content pools into off-white (#fafafa) rather than pure white, keeping the register cool and legible without clinical sterility.

  Typography operates on a proprietary hierarchy. BreitlingFont handles display and headline work — its proportions carry mechanical weight without resorting to condensed letterforms. Moderat, a geometric grotesque, handles body and UI text at sizes that read cleanly against both the dark navy canvas and lighter product-detail surfaces. Italian Plate appears in labeling contexts — reference numbers, technical specifications, collection identifiers — where its industrial mono-spaced register signals precision. Two engraving variants (Block and Cursive) serve ceremonial moments: personalization flows, limited-edition callouts, and the watch-dial reproduction micro-details that Breitling renders in product close-ups.

  Spacing is generous by luxury standards, with section breaks at {spacing.section} and wide padding in product cards that mirrors the physical space a watch occupies on a showcase table. Corners are almost entirely square — the only softening appears at {rounded.xs} on form inputs and {rounded.sm} on cards; pill shapes do not appear in the standard component library. This near-total absence of rounding is a design declaration: Breitling builds instruments, not lifestyle accessories, and every hard corner reinforces that claim. The #007aff link blue appears only in system-level utility contexts — account flows, legal text — and never intrudes on the primary brand register.

colors:
  primary: "#ffc72c"
  primary-active: "#e6a800"
  primary-disabled: "#ffeaa3"
  ink: "#09091a"
  body: "#222222"
  muted: "#7a7a7a"
  muted-light: "#4f4f4f"
  hairline: "#d5d5d5"
  hairline-soft: "#ebebeb"
  canvas: "#fafafa"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#09091a"
  on-dark: "#fafafa"
  navy: "#072c54"
  navy-deep: "#0e2240"
  obsidian: "#09091a"
  charcoal: "#111820"
  link: "#007aff"

typography:
  display-xl:
    fontFamily: "BreitlingFont, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.07
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "BreitlingFont, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-md:
    fontFamily: "BreitlingFont, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "BreitlingFont, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "Moderat, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Moderat, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Moderat, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Moderat, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Moderat, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  tech-label:
    fontFamily: "Italian Plate, monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.08em
    textTransform: uppercase
  ref-number:
    fontFamily: "Italian Plate, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0.04em
  engraving-block:
    fontFamily: "Engraving Block, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.06em
  engraving-cursive:
    fontFamily: "Engraving Cursive, cursive"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Moderat, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.06em
    textTransform: uppercase
  button-sm:
    fontFamily: "Moderat, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "Moderat, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.04em

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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: none
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    imageAspect: "1/1"
    titleTypography: "{typography.title-md}"
    refTypography: "{typography.ref-number}"
    priceTypography: "{typography.title-sm}"
    border: "1px solid {colors.hairline-soft}"
  hero-banner:
    backgroundColor: "{colors.obsidian}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 100vh
    overlayOpacity: 0.45
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    activeTextColor: "{colors.ink}"
    activeBorder: "2px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  watch-badge:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.tech-label}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  watch-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.tech-label}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    labelTypography: "{typography.tech-label}"
    valueTypography: "{typography.body-sm}"
    rowBorder: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  personalization-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    cursiveTypography: "{typography.engraving-cursive}"
    blockTypography: "{typography.engraving-block}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid rgba(255,255,255,0.12)"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The amber (#ffc72c) CTA button renders with square corners (`{rounded.none}`) and near-black text (`{colors.on-primary}`), maintaining visibility against both dark hero backgrounds and lighter product-detail canvases. The uppercase tracking in `{typography.button-md}` keeps it in the instrument-readout register that runs across the brand. On `:active`, background deepens to `{colors.primary-active}` (#e6a800); disabled state uses `{colors.primary-disabled}` with `{colors.muted}` text.

**`button-secondary`** — Transparent ghost button with a single-pixel border and `{colors.on-dark}` text, used exclusively on dark backgrounds (`{colors.navy}`, `{colors.obsidian}`). Padding mirrors `button-primary` exactly so stacked CTAs align optically. Focus state promotes the border to full white; there is no fill on hover.

**`button-ghost`** — Borderless text-only variant in `{colors.on-dark}`, used for lower-hierarchy actions within dark sections: filter resets, "View All" overflow links, and secondary configurator steps.

### Text Input

**`text-input`** — A near-frameless input: transparent background, thin `{colors.hairline}` border at 1px. Focus promotes the border to `{colors.ink}`. The 2px corner radius (`{rounded.xs}`) is the smallest visible softening in the entire UI — present mainly to prevent rendering artifacts. Input text runs in `{typography.body-md}` (Moderat). Used in search, newsletter capture, and configurator forms.

### Navigation

**`nav-bar`** — A 72px dark navy (`{colors.navy-deep}`) bar carrying the wordmark left, collection mega-menu center, and account/search icons right. Links use `{typography.nav-link}` in `{colors.on-dark}`. On scroll past the hero threshold, a subtle drop shadow appears without any color change — preserving the dark chromatic continuity at all scroll positions. At mobile breakpoints (< 744px), the center menu collapses to a hamburger icon that triggers a full-height drawer overlay.

### Product Card

**`product-card`** — White card with a 4px corner softening (`{rounded.sm}`), a square 1:1 watch image occupying the full card width, model name in `{typography.title-md}`, reference number in `{typography.ref-number}` (Italian Plate), and price in `{typography.title-sm}`. A thin `{colors.hairline-soft}` border defines the card edge against the canvas. On hover, the card elevates with a box-shadow increase; no fill or color changes occur. Collection badges sit as absolute overlays in the top-left corner of the image zone.

### Hero Banner

**`hero-banner`** — Full-viewport dark hero (`min-height: 100vh`) over an `{colors.obsidian}` base with a 45% opacity scrim on video or photographic assets. Headline in `{typography.display-xl}` in `{colors.on-dark}`, body copy in `{typography.body-md}`. The amber CTA (`button-primary`) sits 32px below body copy. On mobile, the headline drops to `{typography.display-md}` and the CTA button becomes full-width. Video loops silently; poster frame is served for reduced-motion and low-bandwidth contexts.

### Collection Filter

**`collection-filter`** — Horizontal filter strip on `{colors.canvas}`, each chip in `{typography.body-sm}` with `{colors.body}` text. The active chip carries a 2px bottom border in `{colors.ink}` rather than a filled or rounded pill — an uncommon choice that keeps the filter row visually weightless. Chips are strictly rectangular (`{rounded.none}`). On mobile, the strip becomes a horizontally-scrollable single row with no line wrapping.

### Watch Badges

**`watch-badge`** — Dark navy (`{colors.navy}`) label in `{typography.tech-label}` (Italian Plate uppercase) for collection identifiers (e.g., "NAVITIMER", "SUPEROCEAN"). **`watch-badge-new`** swaps the background to `{colors.primary}` amber with `{colors.on-primary}` text for new-release or limited-edition callouts. Both variants are square-cornered (`{rounded.none}`) and function as absolute overlays on the product card image.

### Specification Table

**`spec-table`** — Two-column key-value table for technical specifications: case diameter, movement caliber, power reserve, water resistance rating. Labels render in `{typography.tech-label}` (`{colors.muted}`); values in `{typography.body-sm}` (`{colors.ink}`). Row separators use `{colors.hairline}`. The table does not collapse into an accordion on mobile — it reflows to a single stacked column with the label above the value, preserving scannable precision data.

### Personalization Panel

**`personalization-panel`** — Light-surface panel (`{colors.surface-soft}`) for the watch engraving configurator. Preview text renders in `{typography.engraving-cursive}` or `{typography.engraving-block}` depending on the user's selected engraving style. This is the only context in which the engraving typefaces appear anywhere in the UI; their presence in the font stack is entirely scoped to this component. The panel is padded generously at `{spacing.xl}` to give the rendered engraving preview room to breathe.

### Footer

**`footer`** — Full-width deep navy (`{colors.navy-deep}`) footer. Column links use `{typography.body-sm}` in `{colors.on-dark}`. A faint rule (`rgba(255,255,255,0.12)`) separates the footer from the final content section above it. At desktop the footer mirrors the mega-menu's column grouping; on mobile the columns collapse to tap-to-expand accordions divided by `{colors.hairline}` rows.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger nav replaces mega-menu; hero headline drops to `{typography.display-md}`; product grid 1-column; CTA buttons full-width; spec table single-column stacked; filter strip horizontally scrollable |
| Tablet | 744–1128px | 2-column product grid; mega-menu replaced by slide-in drawer overlay; hero text at `{typography.display-lg}`; personalization panel stacks vertically |
| Desktop | 1128–1440px | Full mega-menu visible; 3–4 column product grid; hero full viewport with copy and image side-by-side |
| Wide | > 1440px | Content max-width 1440px, centered with equal gutters; hero background video bleeds edge-to-edge; product grid caps at 4 columns |

### Touch Targets

- Minimum 44×44px tap target for all interactive elements
- Nav icon buttons expand tap zones to 48px via padding without changing visual size
- Collection filter chips maintain 40px minimum height on mobile
- Entire product card surface is tappable; no separate "View Details" link is needed
- Engraving style selector radio controls use 48px touch targets

### Collapsing Strategy

- Mega-menu collapses to a full-height drawer overlay on mobile and tablet, sliding in from the left
- Collection filter chips collapse from a multi-row grid to a single horizontally-scrollable row below 744px
- Footer columns collapse to tap-to-expand accordions at mobile breakpoint
- Product configurator panels stack vertically on mobile: watch preview image anchors top, option selectors scroll below it
- Hero video pauses and is replaced by a static poster image in reduced-motion and low-bandwidth contexts

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact BreitlingFont metrics (x-height, cap ratio, optical sizes) are not extractable from the font-family stack string alone — display sizes estimated from visual patterns
- Moderat weight range in active use is approximate: 400 and 500 are confirmed; 300 (light) and 600 (semibold) may be present in sub-components
- Italian Plate variant (No. 1 vs No. 2) is not determinable from the CSS identifier `__italianPlate_843ea1`
- Engraving font sizes in the configurator panel could not be directly measured; values are estimated at 14–16px
- Hover and transition animation timing functions (easing curves, durations) were not captured — assumed 200–300ms ease-out
- Exact mega-menu layout (column count, featured image placement, grouping logic per collection) not confirmed from extraction
- Box-shadow token values for card hover state and sticky nav scroll state are absent — not extractable from hex color scan
- Dark-mode variant presence or absence is unconfirmed; no `prefers-color-scheme` tokens were detected
