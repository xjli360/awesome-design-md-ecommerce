---
version: alpha
name: "NI (National Instruments)"
source_url: "https://www.ni.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  FinancierDisplay — a typeface born in financial editorial — anchors the hero of a test-and-measurement instruments company, and that incongruity is the first thing to understand about NI's visual identity. The serif carries institutional authority without aggression, pairing with FoundersGrotesk's clean geometric weight to give instrument data and marketing prose a shared voice that reads as rigorous rather than corporate. The primary brand anchor is #044123, a forest green so saturated it reads nearly black in isolation and only reveals its chroma when the electric mint #03b585 or the high-voltage #32eb96 ignites alongside it in interactive states, data overlays, and success indicators. Blue (#0d6efd, #0a58ca, #084298) arrives as a secondary palette inherited from Bootstrap's utility layer — status badges, info callouts, link text — rather than as brand ambition, which keeps the verdant greens legible as identity rather than system chrome.

  Surface treatments use the meta theme-color #f4f4f4 as a near-white page canvas, pulling sage-tinged panels (#cddcc8) into section dividers and alternating table rows. Cards sit on white with a #e7e7e7 hairline rather than elevation shadow, preserving the flat, diagram-adjacent aesthetic that engineers scanning datasheets expect. FinancierDisplay runs at 56px in hero positions at restrained tracking that feels editorial; FoundersGrotesk handles all UI chrome — nav labels, form inputs, data table columns — at 14–16px. The monospace stack (Consolas, Courier New, Liberation Mono) surfaces in code samples and parameter readouts, treating technical precision as a first-class design material rather than an afterthought restyled with font-family: inherit.

  The color system signals meaning exactly: #d73a0f for destructive alerts, #ffc60b for warnings and promotional pricing callouts, #32eb96 as a live-data success pulse in data-readout panels against the #141619 dark background. Badge shapes use {rounded.xs} rather than pill rounding — a deliberate angularity that suits instrumentation vocabulary. Navigation runs horizontal at desktop with mega-dropdown panels for product families (DAQ, RF, oscilloscopes, software). Now under Emerson's portfolio (confirmed by page title), NI's design system is an editorial bet: spend type budget on a serif display face to earn credibility with the lab directors and systems engineers who read white papers before they approve a purchase order.

colors:
  primary: "#044123"
  primary-active: "#003018"
  primary-disabled: "#cddcc8"
  primary-accent: "#03b585"
  primary-accent-bright: "#32eb96"
  green-mid: "#008053"
  green-success: "#198754"
  green-deep: "#0f5132"
  green-soft: "#35b77d"
  info-blue: "#0dcaf0"
  link-blue: "#0d6efd"
  link-blue-active: "#0a58ca"
  link-blue-dark: "#084298"
  warning: "#ffc60b"
  warning-text: "#664d03"
  danger: "#d73a0f"
  danger-text: "#842029"
  teal-dark: "#055160"
  sage-soft: "#cddcc8"
  ink: "#141619"
  body: "#444444"
  muted: "#777777"
  muted-light: "#888888"
  hairline: "#e7e7e7"
  hairline-mid: "#b2b2b2"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#f9fafb"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'FinancierDisplay', Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'FinancierDisplay', Georgia, serif"
    fontSize: 44px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'FinancierDisplay', Georgia, serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'FinancierDisplay', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'FoundersGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'FoundersGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'FoundersGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'FoundersGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'FoundersGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'FoundersGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  label-sm:
    fontFamily: "'FoundersGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'FoundersGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'FoundersGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'FoundersGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  code:
    fontFamily: "Consolas, 'Courier New', 'Liberation Mono', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  data-readout:
    fontFamily: "Consolas, 'Courier New', 'Liberation Mono', monospace"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  badge:
    fontFamily: "'FoundersGrotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px

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
    padding: 12px 24px
    height: 44px
    states:
      hover: { backgroundColor: "{colors.primary-active}" }
      disabled: { backgroundColor: "{colors.primary-disabled}", textColor: "{colors.muted}" }

  button-primary-accent:
    backgroundColor: "{colors.primary-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    states:
      hover: { backgroundColor: "{colors.green-mid}", textColor: "{colors.on-primary}" }

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.primary}"
    padding: 11px 23px
    height: 44px
    states:
      hover: { backgroundColor: "{colors.sage-soft}" }

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.link-blue}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    states:
      hover: { backgroundColor: "{colors.surface-soft}" }

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-mid}"
    padding: 10px 14px
    height: 44px
    states:
      focus: { border: "1.5px solid {colors.primary-accent}", outline: "3px solid {colors.primary-disabled}" }
      error: { border: "1.5px solid {colors.danger}" }

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"

  mega-menu-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    shadow: "0 8px 24px rgba(0,0,0,0.08)"
    rounded: "{rounded.xs}"
    padding: "{spacing.xl}"

  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.hairline-mid}"
    padding: "10px 44px 10px 14px"
    height: 44px
    iconColor: "{colors.muted}"
    states:
      focus: { border: "1.5px solid {colors.primary-accent}" }

  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    states:
      hover: { border: "1px solid {colors.primary-accent}", shadow: "0 4px 12px rgba(3,181,133,0.15)" }

  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
    accentLine: "4px solid {colors.primary-accent}"

  section-divider-sage:
    backgroundColor: "{colors.sage-soft}"
    padding: "{spacing.section} 0"
    rounded: "{rounded.none}"

  resource-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    tagTypography: "{typography.caption}"
    tagColor: "{colors.primary-accent}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"

  tab-nav:
    activeColor: "{colors.primary}"
    activeIndicator: "2px solid {colors.primary-accent}"
    inactiveColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"

  spec-table:
    headerBackgroundColor: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.title-sm}"
    rowBackgroundColor: "{colors.canvas}"
    rowAltBackgroundColor: "{colors.surface-soft}"
    rowTextColor: "{colors.body}"
    rowTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"

  data-readout-panel:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.primary-accent-bright}"
    typography: "{typography.data-readout}"
    labelTypography: "{typography.label-sm}"
    labelColor: "{colors.muted-light}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"

  code-block:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.primary-accent}"
    typography: "{typography.code}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"

  badge-status:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  badge-accent:
    backgroundColor: "{colors.primary-accent-bright}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  badge-info:
    backgroundColor: "{colors.info-blue}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  badge-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.warning-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  badge-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  alert-info:
    backgroundColor: "#cfe2ff"
    textColor: "{colors.link-blue-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.info-blue}"
    padding: "{spacing.md} {spacing.base}"

  alert-success:
    backgroundColor: "#d1e7dd"
    textColor: "{colors.green-deep}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.green-success}"
    padding: "{spacing.md} {spacing.base}"

  alert-warning:
    backgroundColor: "#fff3cd"
    textColor: "{colors.warning-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.warning}"
    padding: "{spacing.md} {spacing.base}"

  alert-danger:
    backgroundColor: "#f8d7da"
    textColor: "{colors.danger-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.danger}"
    padding: "{spacing.md} {spacing.base}"

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-light}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.primary-accent}"
    headingTypography: "{typography.label-sm}"
    headingColor: "{colors.on-dark}"
    padding: "{spacing.section} 0"

---

## Components

### Buttons

**`button-primary`** — Forest-green (#044123) fill with white text at {rounded.xs} corners, 44px tall. The square-ish radius signals instrument-world precision rather than consumer friendliness. Hover darkens to #003018; disabled state drops to the sage fill ({colors.primary-disabled}) with muted text, visually analogous to an inactive instrument channel.

**`button-primary-accent`** — Uses the electric mint #03b585 as fill with dark ink text, delivering the brand's most visible CTA variant in contexts where the deep green feels too heavy (white hero sections, light-surface cards). Hover transitions to {colors.green-mid} and flips text to white, maintaining contrast without a jarring jump.

**`button-secondary`** — White fill with a 1.5px {colors.primary} border and matching text. The outline-on-white pairing gives a clean engineering-drawing quality. Hover introduces the sage (#cddcc8) background tint as a soft confirmation of state.

**`button-ghost`** — Transparent with {colors.link-blue} text; no border. Used for tertiary actions like "Learn more" inside content blocks. Hover adds a {colors.surface-soft} background wash.

### Inputs

**`text-input`** — 44px height, 1px mid-gray border, {rounded.xs} corners. Focus state replaces the border with a 1.5px {colors.primary-accent} stroke and adds a 3px sage outline drawn from {colors.primary-disabled} — the mint-on-sage halo is unmistakably NI. Error state uses {colors.danger} border with no outline.

**`search-bar`** — Matches text-input geometry but carries a 44px search icon inset on the right. Focus border fires {colors.primary-accent}. Used in the global nav and the product/documentation filter panels.

### Navigation

**`nav-bar`** — White canvas, 64px height, 1px {colors.hairline} bottom border. Logo renders in {colors.primary}. Nav links use {typography.nav-link} at 15px/500 weight — lower weight than consumer nav conventions, which reads as deliberate restraint for an audience that trusts information density over brand performance.

**`mega-menu-panel`** — Floating white panel with 1px {colors.hairline} border and an 8px shadow at 8% black. Opens below top-nav product-family triggers. Interior columns use {typography.body-sm} for links and {typography.title-sm} for column headers. Corners at {rounded.xs} — the panel is a floating rectangle, not a balloon.

**`tab-nav`** — Horizontal tabs with no border, no background, no radius. Active tab shows a 2px {colors.primary-accent} underline indicator and text in {colors.primary}; inactive tabs use {colors.muted}. Padding of {spacing.sm} × {spacing.base} keeps the row compact against spec-heavy page layouts.

### Cards

**`product-card`** — White card, 1px {colors.hairline} border, {rounded.xs} corners, {spacing.lg} padding. Title in {typography.title-sm}, body in {typography.body-sm}. Hover swaps the border to {colors.primary-accent} and adds a 4px shadow tinted with the mint at 15% opacity — the glow reads as an instrument acquisition confirming signal lock.

**`resource-card`** — Structurally identical to product-card but carries a tag line in {typography.caption} colored {colors.primary-accent} to classify content type (white paper, webinar, application note). Used in resource libraries and the "Related content" rail.

### Hero & Sections

**`hero-banner`** — Full-width {colors.primary} deep-green field, minimum 480px tall. Heading in {typography.display-xl} (FinancierDisplay serif at 56px), body in {typography.body-md} white. A 4px {colors.primary-accent} rule runs as a left-edge accent on the text column or below the headline, grounding the editorial serif in brand color without a separate graphic device.

**`section-divider-sage`** — Alternating page sections use the pale sage #cddcc8 as background rather than a hairline, creating block-level rhythm without border artifacts. Padding at {spacing.section} top and bottom.

### Data & Technical

**`data-readout-panel`** — Dark (#141619) panel with {colors.primary-accent-bright} monospace values in {typography.data-readout} (24px bold Consolas). Unit labels and channel identifiers sit above in {typography.label-sm} at {colors.muted-light}. This component is the system's most brand-specific element — the electric mint on near-black mimics oscilloscope trace color conventions while staying recognizably NI.

**`code-block`** — Same dark (#141619) background as the readout panel, but text runs in {colors.primary-accent} (#03b585) rather than the bright mint, keeping code legible at smaller {typography.code} sizes. {rounded.sm} corners, {spacing.lg} padding.

**`spec-table`** — Header row in {colors.primary} with white text ({typography.title-sm}). Body rows alternate between {colors.canvas} and {colors.surface-soft}. All borders 1px {colors.hairline}. No rounded corners — the table is a grid, and grids have hard corners.

### Badges & Alerts

**Badges** (`badge-status`, `badge-accent`, `badge-info`, `badge-warning`, `badge-danger`) — All 11px/700-weight {typography.badge} labels at {rounded.xs} with 3px × 8px padding. The consistent square corner across all badge variants creates a taxonomy that reads as a legend on a circuit diagram. Accent (#32eb96 on dark ink) and status (white on #044123) are the most common on product pages; warning (#ffc60b on #664d03 text) surfaces on pricing and availability callouts.

**Alerts** (`alert-info`, `alert-success`, `alert-warning`, `alert-danger`) — Bootstrap-system tinted fills (light blue, sage, amber, pink) with matching text and 1px border colors drawn from the semantic color palette. {rounded.xs} corners, {typography.body-sm} text. Used in documentation, download pages, and form validation feedback.

### Footer

**`footer`** — Near-black (#141619) background, column headings in {typography.label-sm} uppercase white, link text in {typography.body-sm} at {colors.muted-light}. Active links use {colors.primary-accent} — the mint on black is the highest-contrast brand combination, reserved here for the footer's persistent link-heavy layout.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; mega-menu collapses to an accordion drawer with a hamburger trigger; hero min-height drops to 320px; FinancierDisplay display-xl scales to 36px (display-md); product cards stack full-width; spec-table scrolls horizontally inside a scroll container |
| Tablet | 744–1128px | Two-column card grids; mega-menu may remain as overlay or shift to accordion; nav compresses to icon + wordmark + hamburger; hero uses display-lg at 44px |
| Desktop | 1128–1440px | Full horizontal nav-bar with mega-menu dropdowns; three- or four-column product card grids; sidebar + content layouts for documentation and spec pages; full hero at display-xl |
| Wide | > 1440px | Max content width caps at 1440px with auto side margins; hero text column constrained to ~600px to prevent line-length overrun on FinancierDisplay serif |

### Touch Targets

- All buttons and inputs target 44px minimum height
- Nav links in mobile drawer: 48px minimum tap height with {spacing.base} side padding
- Badge-only tap targets (e.g., filter tags) expand to 36px height via padding rather than font scaling
- Data-readout panels are display-only; no touch affordances needed

### Collapsing Strategy

- Mega-menu product families collapse into a flat accordion on mobile, preserving hierarchy without nested flyouts
- Spec-table columns prioritize left-most (parameter name + value) on narrow viewports; secondary columns (conditions, units, notes) scroll off-screen right inside a touch-scrollable container
- Tab-nav scrolls horizontally with no wrapping below 744px; active tab is scrolled into view on mount
- Footer columns reflow to two-column at tablet, single-column at mobile; column order follows information priority (product, support, company, legal)

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No icon system or glyph set confirmed; the font stack includes `Glyphicons Glyphicon` suggesting Bootstrap 3 icon font usage in legacy sections, but current icon treatment (SVG vs icon font vs image sprite) could not be verified from extraction
- Exact FinancierDisplay and FoundersGrotesk weight axes and available cuts unknown; weights above are inferred from the editorial/UI role split rather than measured from rendered glyphs
- Button and input exact padding/height values are estimated from Bootstrap 5 defaults; NI may override these in a custom stylesheet not reachable via static extraction
- Hover and focus animations (duration, easing) not captured; Bootstrap defaults (0.15s ease-in-out) are assumed
- Dark-mode treatment unknown; no `prefers-color-scheme` tokens observed; the dark data-readout panel is a component-level inversion, not a system-level theme
- Specific FinancierDisplay and FoundersGrotesk licensing status and self-hosting vs. CDN delivery not confirmed; Georgia and Helvetica Neue are listed as fallbacks
- Page was served in Japanese (EmersonのNIテストおよび計測ソリューション) suggesting localization layers; CJK typographic overrides (line-height, font-size scaling) may exist but were not extractable
- Exact shadow values, transition durations, and z-index layering for mega-menu panels estimated from visual inspection conventions, not extracted CSS values
