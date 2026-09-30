---
version: alpha
name: "Brew"
source_url: "https://www.brewwatches.com"
captured_at: "2026-09-28T04:53:12.448075+00:00"
evidence_status: "historical_partial_css_evidence"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Midnight navy `#00052c` anchors the entire visual system the way lacquer grounds a dial — total absorption, zero warmth, every accent made to read brighter against it. Brew Watch Co. runs Barlow Condensed for all display and heading type, a choice that carries deliberate resonance: the condensed letterforms echo the economy of instrument-panel printing that dial typography borrowed from aviation gauges before condensed type became a branding trend. Display headlines sit tight, tracking pulled in, giving model names the same compressed authority as a reference number stamped on a case back. Instrument Sans handles body and UI copy — a clean, contemporary counterpart that reads efficiently at small sizes without competing with the headline level's compressed drama.

  The tonal palette splits into three registers: deep-navy ground (`#00052c`, `#272d45`) for dark surfaces and anchoring text; a family of cool near-whites (`#f9fafb`, `#f4f4f6`, `#f3f3f3`) for the primary canvas; and a band of blue-tinged neutrals (`#676986`, `#9a9db1`, `#dbdde4`) that handle secondary text, hairlines, and placeholder copy without ever sliding warm. Teal `#0e7a82` arrives as a secondary accent — calibrated, not loud — and its lighter sibling `#9fcacd` provides hover states and footer link color. `#d02e2e` shows up as a sharp-red signal for errors, sale markers, and the occasional dial-color badge, echoing the red 12 o'clock position found on field-watch dials.

  Geometry stays near-square throughout. Buttons, filter chips, and spec cells use `{rounded.sm}` or `{rounded.none}`, never the full-radius pill that reads as cosmetic softness. This keeps the interface feeling closer to a product configurator than a lifestyle shop — useful, angular, exact. Collection pages rely on dense grid photography rather than decorative UI chrome, trusting steel and brass to carry the brand statement.

colors:
  primary: "#00052c"
  primary-active: "#000b5f"
  primary-disabled: "#676986"
  ink: "#0b0b0b"
  body: "#272d45"
  muted: "#9a9db1"
  muted-strong: "#737373"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5eb"
  canvas: "#f9fafb"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#f3f3f3"
  accent-teal: "#0e7a82"
  accent-teal-light: "#9fcacd"
  accent-teal-dark: "#0c6b72"
  accent-red: "#d02e2e"
  mid-navy: "#2c3e50"
  scrim: "#00052c"

typography:
  display-xl:
    fontFamily: "'Barlow Condensed', sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Barlow Condensed', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.3px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Barlow Condensed', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.2px
    textTransform: uppercase
  title-md:
    fontFamily: "'Barlow Condensed', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "'Barlow Condensed', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0
  label-caps:
    fontFamily: "'Barlow Condensed', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Barlow Condensed', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Barlow Condensed', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 1.2px
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
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-secondary-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 60px
    logoTypography: "{typography.display-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageRounded: "{rounded.none}"
    nameTypography: "{typography.title-md}"
    nameColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    collectionLabelTypography: "{typography.label-caps}"
    collectionLabelColor: "{colors.muted}"
    subtitleColor: "{colors.muted}"
    padding: "{spacing.md}"
    imageAspectRatio: "1:1"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadOpacity: 0.75
    ctaComponent: "button-secondary-on-dark"
    minHeight: 520px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  collection-filter-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 32px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.primary}"
  watch-spec-table:
    backgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.label-caps}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    rowBorderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    selectedBorder: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    width: 56px
    height: 44px
  teal-accent-badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    linkHoverColor: "{colors.accent-teal-light}"
    headingTypography: "{typography.label-caps}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.mid-navy}"
  search-overlay:
    scrimBackgroundColor: "{colors.scrim}"
    scrimOpacity: 0.75
    panelBackgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    rounded: "{rounded.none}"

## Components

### Buttons

**`button-primary`** — Midnight-navy `#00052c` fill carrying uppercase Barlow Condensed tracked at 1.5px; the compressed letterforms and tight uppercase give it more visual weight than its 44px height suggests. Active state deepens to `{colors.primary-active}` `#000b5f`; disabled drops to muted `{colors.primary-disabled}` `#676986`. Corners sit at `{rounded.sm}` — just enough to file the edge without softening the impression.

**`button-secondary`** — Transparent ground with a 1px `{colors.primary}` border and matching text, using the same uppercase Barlow Condensed as the primary. On dark surfaces (hero, footer) the variant `button-secondary-on-dark` inverts both border and text to `{colors.on-primary}`. No fill change on hover — border and text simply gain opacity.

### Text Input

**`text-input`** — `{colors.canvas}` background, 1px `{colors.hairline}` border, no decorative chrome. Focus state replaces the hairline with a 2px `{colors.primary}` outline, anchoring keyboard navigation in the same navy identity as the primary button. Placeholder text in `{colors.muted}` blue-gray keeps the field readable but unobtrusive.

### Navigation

**`nav-bar`** — Canvas-white bar with a thin `{colors.hairline}` bottom rule separating it from page content. Logo renders in Barlow Condensed `{typography.display-sm}` weight 600 flush-left; navigation links use Instrument Sans `{typography.nav-link}` right of center. Cart, search, and account icons align far right with 44px tap areas. On scroll the bar gains a subtle `{colors.hairline-soft}` box-shadow without color change.

### Product Card

**`product-card`** — Square photography with zero border-radius (`{rounded.none}`) matching the rectilinear language of watch case profiles against plain studio backgrounds. Below the image: model name in Barlow Condensed `{typography.title-md}`, collection label in uppercase `{typography.label-caps}` at `{colors.muted}`, and price in `{typography.price-display}` at `{colors.primary}` navy. No shadow or card border — visual separation comes from grid gap and the `{colors.surface-soft}` page ground.

### Hero

**`hero`** — Full-width `{colors.primary}` field with headline in `{typography.display-xl}` uppercase Barlow Condensed, white. Supporting copy in `{typography.body-md}` Instrument Sans at 75% opacity. CTA uses `button-secondary-on-dark`. Minimum height 520px; on mobile crops to 400px with a centered text column overlay.

### Announcement Bar

**`announcement-bar`** — Single-rule strip at the very top of the page in `{colors.primary}` with `{colors.on-primary}` copy in `{typography.caption}`. Typically carries free-shipping thresholds or limited-launch notices. 36px height; text centered.

### Collection Filter Tag

**`collection-filter-tag`** — Compact uppercase chips for filtering by dial color, movement type, and case material. Resting: `{colors.surface-soft}` fill, 1px `{colors.hairline}` border, `{colors.body}` text. Active: `{colors.primary}` fill, `{colors.on-primary}` text, matching navy border. Corner at `{rounded.xs}` — 2px, nearly square.

### Watch Spec Table

**`watch-spec-table`** — Two-column key/value grid sitting in the product detail page below the description block. Labels in `{typography.label-caps}` at `{colors.muted}` blue-gray; values in `{typography.body-sm}` at `{colors.ink}`. `{colors.hairline}` horizontal rules divide rows; no outer card border or elevation — the table sits flush in the page. Fields typically include case diameter, thickness, lug-to-lug, crystal, movement, water resistance, and strap width.

### Size Selector

**`size-selector`** — Square tiles (56 × 44px) displaying case diameter in millimeters in `{typography.button-sm}` uppercase. Unselected: `{colors.canvas}` ground, 1px `{colors.hairline}` border, `{colors.body}` text. Selected: `{colors.primary}` fill, `{colors.on-primary}` text, matched navy border. `{rounded.none}` keeps geometry hard-edged — the tiles read as objects, not pills.

### Teal Accent Badge

**`teal-accent-badge`** — Small inline label for "New", "Limited Edition", or dial-colorway callouts. `{colors.accent-teal}` `#0e7a82` fill, `{colors.canvas}` text in uppercase `{typography.label-caps}`. `{rounded.xs}` corner. The teal sits distinctly apart from the navy vocabulary, functioning as a genuine signal rather than ambient brand color.

### Footer

**`footer`** — Deep `{colors.primary}` ground matching the hero and announcement bar, unified with the dark anchors of the page. Column headings in `{typography.label-caps}` uppercase `{colors.on-primary}`; body links in `{typography.body-sm}` at `{colors.on-primary}` with `{colors.accent-teal-light}` hover. Social icons row above the legal line. A `{colors.mid-navy}` top border separates it from the page body.

### Search Overlay

**`search-overlay`** — Triggered from the nav search icon. A `{colors.scrim}` overlay at 75% opacity drops behind a full-width input panel on `{colors.canvas}`. Input text in `{typography.body-md}` Instrument Sans; results list uses `{typography.body-sm}` with `{typography.label-caps}` category headers. `{rounded.none}` throughout — the panel reads as a viewport layer, not a floated modal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav opens a left-slide drawer over navy scrim; hero crops to 400px with centered text; spec table scrolls horizontally; filter chips become a horizontal scroll strip |
| Tablet | 744–1128px | Two-column product grid; full nav links visible but condensed; hero splits to text-left / image-right layout at 50/50 |
| Desktop | 1128–1440px | Three or four-column product grid; full nav with hover dropdowns; hero full-bleed with centered or left-offset text overlay |
| Wide | > 1440px | Max-width container (~1440px) centered; side gutters fill with `{colors.canvas}`; grid holds at four columns |

### Touch Targets
- All buttons minimum 44 × 44px; size-selector tiles exactly 56 × 44px
- Nav icon areas padded to 44 × 44px regardless of icon rendered size
- Filter chip minimum height 36px with 12px horizontal padding on mobile
- Footer links minimum 44px tap height via padding expansion

### Collapsing Strategy
- Nav collapses to hamburger at < 744px; drawer slides from left over a 75%-opacity `{colors.scrim}` overlay
- Collection filters become a no-wrap horizontal scroll strip on mobile; no "More Filters" accordion
- Watch spec table does not collapse — scrolls horizontally within a bounded container
- Footer transitions from four-column grid to single-column stacked accordion on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- No pure `#ffffff` found in extracted palette; `surface-card` assigned `#ffffff` as implied standard background but unconfirmed
- Font weights for Barlow Condensed not confirmed from computed CSS; 600/700 assigned by typical display usage convention
- Exact button padding, height, and spacing values estimated at 44px standard touch target — not extracted from computed styles
- Whether `{colors.accent-red}` (`#d02e2e`) is used for UI error states, sale price labels, or as a dial-color badge only is ambiguous from extraction
- `meta theme-color` absent — no confirmed mobile browser chrome color
- Hover/focus transition durations and easing curves not extractable from static snapshot
- Dark mode presence or absence unconfirmed; palette appears single-mode (light canvas primary, dark navy for hero/footer)
- Barlow Condensed weight availability (full variable axis vs. static instances) not confirmed from font-loading inspection
