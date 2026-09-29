---
version: alpha
name: "DC Vintage Watches"
source_url: "https://www.dcvintagewatches.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Electric blue (#116dff) is an unusual choice for a vintage watch dealer — it lands with the precision of a dive bezel luminous indicator, not the expected brown leather or aged brass of the industry's default palette. Against #151414 near-black, every primary CTA and interactive element reads with instrument-face clarity: the active state charges forward while the dark ground recedes exactly as a watch dial uses contrast to communicate without a second glance. The typeface Madefor — a geometric sans with calibrated stroke-to-counter ratios — carries display headings at 700 weight where its sharp-shouldered letterforms share something with quality dial typography: deliberate, unfussy, built to be read at a glance. The palette extends into a full condition vocabulary beyond the blue-and-black spine: deep garnet (#9c2426) marks sold badges and urgent price alerts; forest green (#0d4f3d) signals verified provenance and authentication certificates; warm amber (#d49341) traces gold-case references and gilt-dial catalogue entries, each colour doing the semantic work of a physical label in a dealer's tray. A long grayscale ramp — from #383838 body text through #767574 muted captions to #e0dfdf hairlines — gives the catalogue grid tonal range to carry dense listings without fatigue. Card surfaces pull a barely-perceptible blue tint (#f5f7ff) from the primary ramp, so white space stays within the brand system rather than drifting neutral. Rounded corners hold at 8px across inputs and chips, 12px on cards — restrained, like the case finishing of a well-made watch: clean breaks, no frippery. The collector's intelligence is respected at every scroll depth: specifications render in monospaced precision, provenance details surface at caption scale, and the hierarchy never forces a knowledgeable buyer to hunt for the information that matters.

colors:
  primary: "#116dff"
  primary-active: "#0f2ccf"
  primary-hover: "#2f5dff"
  primary-soft: "#597dff"
  primary-disabled: "#d5dfff"
  primary-tint: "#eaefff"
  primary-surface: "#f5f7ff"
  accent-red: "#9c2426"
  accent-red-mid: "#df3336"
  accent-red-light: "#f4b8b9"
  accent-red-surface: "#fcebeb"
  accent-green: "#0d4f3d"
  accent-green-mid: "#4b916d"
  accent-green-light: "#bde2a7"
  accent-green-surface: "#effae5"
  accent-gold: "#d49341"
  ink: "#151414"
  body: "#383838"
  muted: "#767574"
  muted-soft: "#a8a6a5"
  hairline: "#e0dfdf"
  hairline-soft: "#f1f0ef"
  canvas: "#ffffff"
  surface-soft: "#f1f0ef"
  surface-card: "#f5f7ff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  price-display:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  label-caps:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  spec-mono:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
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
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1.5px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 20px
  button-ghost-hover:
    backgroundColor: "{colors.primary-tint}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1.5px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1.5px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    rounded: "{rounded.md}"
    padding: 10px 16px
    height: 48px
    iconColor: "{colors.muted}"
    iconFocusColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    activeColor: "{colors.primary}"
    hoverColor: "{colors.primary-hover}"
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    imageRatio: 1/1
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    padding: "{spacing.base}"
    shadow: "0 2px 8px rgba(21,20,20,0.07)"
    hoverShadow: "0 6px 20px rgba(17,109,255,0.12)"
    hoverBorder: "1px solid {colors.primary-disabled}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    subheadingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.sm}"
    minHeight: 480px
    padding: "{spacing.section}"
  condition-badge:
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
    mint-backgroundColor: "{colors.accent-green-surface}"
    mint-textColor: "{colors.accent-green}"
    mint-border: "1px solid {colors.accent-green-light}"
    excellent-backgroundColor: "{colors.primary-surface}"
    excellent-textColor: "{colors.primary-active}"
    excellent-border: "1px solid {colors.primary-disabled}"
    good-backgroundColor: "{colors.surface-soft}"
    good-textColor: "{colors.body}"
    good-border: "1px solid {colors.hairline}"
    sold-backgroundColor: "{colors.accent-red-surface}"
    sold-textColor: "{colors.accent-red}"
    sold-border: "1px solid {colors.accent-red-light}"
  provenance-badge:
    backgroundColor: "{colors.accent-green-surface}"
    textColor: "{colors.accent-green}"
    border: "1px solid {colors.accent-green-light}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
    iconSize: 14px
  price-alert-badge:
    backgroundColor: "{colors.accent-red-surface}"
    textColor: "{colors.accent-red-mid}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  gold-reference-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent-gold}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary-tint}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-soft}"
    rounded: "{rounded.full}"
  watch-spec-table:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.spec-mono}"
    valueColor: "{colors.body}"
    rowPadding: "{spacing.md} {spacing.base}"
    alternateRowColor: "{colors.surface-soft}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.primary-soft}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    padding: "{spacing.section} 0"
    borderTop: "1px solid {colors.body}"

## Components

### Buttons

**`button-primary`** — Solid #116dff fill with white text at Madefor 15px/600, 44px height, 8px radius. Hover shifts fill to #2f5dff; active presses to #0f2ccf; disabled renders in #d5dfff. Padding is 12px vertical, 24px horizontal.

**`button-secondary`** — White background with a 1.5px #e0dfdf hairline border and ink text at matching 44px height. On hover the surface shifts to #f1f0ef and the border darkens to #a8a6a5. Paired with primary to offer a parallel action without competing for focus.

**`button-ghost`** — Transparent background, #116dff text, no border. Used for in-context navigation and lower-priority listing actions. Hover fills #eaefff tint behind the text to confirm target area without structural weight.

### Search Bar

**`search-bar`** — 48px input on a 12px radius with #f1f0ef fill and 1.5px hairline border. A muted search icon (#767574) sits left-inset; on focus, both border and icon shift to #116dff. The taller height and softer fill distinguish it from standard text inputs as the catalogue navigation centrepiece.

### Navigation

**`nav-bar`** — White 64px bar with a single 1px #e0dfdf bottom border. Madefor 14px/500 nav links in ink; active and hover states shift to #116dff. Brand wordmark sits left-aligned; search, account, and enquiry controls cluster right. State changes are typographic only — no dropdown shadow fills or background planes.

### Product Cards

**`product-card`** — White card on 12px radius with 1px hairline border and a 2px/8px-blur ink shadow at 7% opacity. Watch photographs render 1:1 square. Title uses Madefor 15px/600 in ink; price renders at 24px/700. Maker, reference number, and year sit below price in 12px/500 muted caption. On hover the shadow expands to 6px/20px at 12% primary-blue tint opacity and the border shifts to #d5dfff, giving the card a blue-lit lift without displacement.

### Condition Badges

**`condition-badge`** — Four-state system in all-caps 11px/700 Madefor at 1px letter-spacing. Mint: #effae5 fill, #0d4f3d text, #bde2a7 border. Excellent: #f5f7ff fill, #0f2ccf text, #d5dfff border. Good: #f1f0ef fill, #383838 text, #e0dfdf border. Sold: #fcebeb fill, #9c2426 text, #f4b8b9 border. All states use 4px radius and 3px×8px padding to sit inline on a card without displacing adjacent elements.

### Provenance Badge

**`provenance-badge`** — Green-tinted label (#effae5 fill, #0d4f3d text, #bde2a7 border) at 12px/500 caption with a 14px verified-tick icon inset left. Wider than condition badges at 4px×10px padding, marking it as a trust signal rather than a classification label.

### Price Alert Badge

**`price-alert-badge`** — Compact crimson-surface label (#fcebeb fill, #df3336 text) in all-caps 11px/700 for recent price reductions or timed availability. Shares 4px radius with condition badges to preserve badge-language consistency across card layouts.

### Gold Reference Tag

**`gold-reference-tag`** — Warm amber text (#d49341) on #f1f0ef surface with #e0dfdf border, in all-caps 11px/700 Madefor. Applied to gold-case or gilt-dial reference entries. The amber reads as a material signal rather than a brand-arbitrary accent.

### Filter Chips

**`filter-chip`** — Full-radius pills at Madefor 13px/600, #f1f0ef fill, 1px hairline border. Active state transitions to #eaefff fill, #0f2ccf text, #597dff border — a contained blue shift that echoes the primary without hardening to a button. Used across brand, condition, decade, and movement-type filters.

### Watch Spec Table

**`watch-spec-table`** — Two-column block: left column in 12px/500 muted (#767574) labels, right column in monospaced 13px (#383838) values. Alternating rows use #f1f0ef fill for separation without inner borders. Full-width hairline dividers cap the top and bottom. Standard fields: reference, case diameter, movement, water resistance, provenance.

### Footer

**`footer`** — #151414 near-black background with white headings at Madefor 15px/600 and #a8a6a5 body links at 14px/400. Link hover shifts to #597dff, threading the primary blue against the dark ground. A single 1px #383838 top border separates footer from catalogue content. Section padding 64px top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter chips collapse to a scrollable horizontal rail; nav-bar hides category links behind a hamburger; hero min-height reduces to 320px |
| Tablet | 744–1128px | Two-column product grid; filter chips visible in a left sidebar at ≥ 768px; nav-bar shows 3–4 primary category links |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar; hero expands to 480px; spec tables render inline beside watch imagery |
| Wide | > 1440px | Four-column grid; content max-width caps at 1440px with symmetric margins; hero image bleeds edge-to-edge behind a constrained text column |

### Touch Targets

- All interactive elements maintain a minimum 44×44px touch target on mobile
- Filter chips expand vertical padding to 10px on mobile to compensate for narrow pill widths
- Card tap targets cover the full card surface including image, title, and price regions
- Product image carousels use 48px-high swipe zones at left and right edges

### Collapsing Strategy

- Primary navigation collapses to hamburger at < 744px; the drawer uses #151414 dark background with full-width ink-white link rows
- Filter sidebar collapses to a bottom-sheet modal on mobile, triggered by a sticky #116dff "Filter" button
- Watch spec table stacks label and value into a single column at < 480px with 12px vertical row padding
- Condition and provenance badges remain inline at all breakpoints; font size does not reduce below 10px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Custom font "Madefor" appears in the CSS stack but no @font-face source URL was captured; it may be served from a CDN not reachable during static extraction
- Japanese font stack (Hiragino Kaku Gothic Pro, Meiryo) present but no JP-locale page routes or language toggle observed — unclear whether site actively serves Japanese content or inherited these from a framework default
- Gold reference tag surface and border colors use #f1f0ef and #e0dfdf from the extracted neutral ramp rather than a dedicated amber-tint surface, as no light amber tones appeared in extraction
- Exact box-shadow values for product cards not extracted — values inferred from catalogue conventions at this density
- No meta theme-color defined; mobile browser chrome colour unspecified
- Dark-mode token set not observed; all extracted colours suggest a light-canvas-first system — dark mode support unknown
- Hover and transition animation durations not captured; 150–200ms ease assumed from category conventions
- Nav dropdown or mega-menu structure, if any, not visible from static extraction
