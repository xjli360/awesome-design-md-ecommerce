---
version: alpha
name: "Varjo"
source_url: "https://varjo.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A high-stakes simulation environment where #0205be — a dense, almost ultraviolet blue — serves as the primary voltage, signaling that this is not consumer VR but military-grade hardware for training pilots and surgeons. The palette reads as industrial precision: #16160e (near-black ink), #5b5b5b and #9d9d9d for muted body text, #e6e6e6 and #f5f5f5 for soft surfaces, and #fbfbfb for canvas. The single accent that breaks the monochrome authority is #da1e28 — a warning red used sparingly for critical CTAs and error states, while #219653 (a cool green) appears for success indicators in simulation telemetry. Type runs Akkurat and Lateral, both Swiss-derived grotesques with sharp terminals and even color — no optical compensation for warmth. Display sizes sit at 24–32px with tight letter-spacing (-0.5px), and body copy at 14–16px with generous line-height (1.6) to maintain legibility across VR heads-up overlays and desktop dashboards. Corners are almost entirely square: {rounded.xs} (4px) appears on input fields and badges, but primary buttons use {rounded.sm} (8px) — the only concession to softness in an otherwise rectilinear system. The nav bar is a fixed 72px strip of {colors.canvas} with {colors.ink} text, and product cards for headsets like the XR-4 and Varjo Aero use a 2-column grid with spec sheets that read like avionics manuals. The overall feel is that of a cockpit instrument panel translated into a web interface — every pixel has a job, and nothing is decorative.

colors:
  primary: "#0205be"
  primary-active: "#0004a0"
  primary-disabled: "#8a8cd6"
  ink: "#16160e"
  body: "#5b5b5b"
  muted: "#9d9d9d"
  muted-soft: "#aaaaaa"
  hairline: "#e6e6e6"
  hairline-soft: "#f5f5f5"
  canvas: "#fbfbfb"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  error: "#da1e28"
  error-hover: "#b81a22"
  success: "#219653"
  success-hover: "#1b7a44"
  dark-bg: "#141414"
  dark-surface: "#2e2d2d"
  dark-muted: "#26323d"
  spec-label: "#5b5b5b"
  spec-value: "#16160e"

typography:
  display-xl:
    fontFamily: "'Akkurat', 'Lateral', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Akkurat', 'Lateral', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.4px
  display-md:
    fontFamily: "'Akkurat', 'Lateral', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Akkurat', 'Lateral', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Akkurat', 'Lateral', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Akkurat', 'Lateral', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Akkurat', 'Lateral', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Akkurat', 'Lateral', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Akkurat', 'Lateral', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Akkurat', 'Lateral', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Space Mono', monospace"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Akkurat', 'Lateral', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Akkurat', 'Lateral', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.3px
  link:
    fontFamily: "'Akkurat', 'Lateral', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Akkurat', 'Lateral', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.2px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Akkurat', 'Lateral', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-value:
    fontFamily: "'Akkurat', 'Lateral', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  mono:
    fontFamily: "'Space Mono', 'Courier New', monospace"
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-tertiary-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  button-error:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-error-hover:
    backgroundColor: "{colors.error-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-success-hover:
    backgroundColor: "{colors.success-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 3px rgba(2, 5, 190, 0.15)"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    boxShadow: "0 1px 3px rgba(0, 0, 0, 0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 24px
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    boxShadow: "0 4px 12px rgba(0, 0, 0, 0.08)"
    border: "1px solid {colors.muted-soft}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "16/9"
  product-card-spec:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.spec-label}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "80px 0"
  hero-section-dark:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-primary}"
    padding: "80px 0"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-headline-dark:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subheadline:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  hero-subheadline-dark:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-error:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 3px rgba(2, 5, 190, 0.15)"
  footer:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "48px 0"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline-soft}"
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.spec-label}"
    padding: "12px 16px"
  spec-table-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.spec-value}"
    padding: "12px 16px"
  toggle-switch:
    backgroundColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
    height: 24px
  toggle-switch-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
  toggle-switch-knob:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  modal-overlay:
    backgroundColor: "rgba(22, 22, 14, 0.6)"
  modal-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "32px"
    boxShadow: "0 8px 24px rgba(0, 0, 0, 0.12)"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, using the brand's distinctive #0205be blue. Hover state shifts to `{colors.primary-active}` (#0004a0) for a subtle darkening. Disabled state uses `{colors.primary-disabled}` (#8a8cd6) with reduced opacity. All primary buttons use `{rounded.sm}` (8px) — the only rounded corners in the system, intentionally slight to maintain the industrial precision feel.

**`button-secondary`** — A bordered variant on white canvas with `{colors.ink}` text and a 1px `{colors.hairline}` border. On hover, the background shifts to `{colors.surface-soft}` and the border strengthens to `{colors.muted}`. Used for "Learn More" and secondary actions alongside primary buttons.

**`button-tertiary-text`** — A text-only button with no background or border, using `{colors.primary}` for the text. Hover darkens to `{colors.primary-active}`. Used for inline actions like "View all specs" or "Cancel" in forms.

**`button-error`** — A red variant using `{colors.error}` (#da1e28) for destructive actions like "Delete simulation" or "Reset configuration". Hover darkens to `{colors.error-hover}` (#b81a22).

**`button-success`** — A green variant using `{colors.success}` (#219653) for confirmations like "Save configuration" or "Deploy". Hover darkens to `{colors.success-hover}` (#1b7a44).

### Text Inputs & Forms
**`text-input`** — A clean input field with `{colors.canvas}` background, `{colors.ink}` text, and a 1px `{colors.hairline}` border. Focus state adds a 3px blue ring (`rgba(2, 5, 190, 0.15)`) and `{colors.primary}` border. Error state swaps the border to `{colors.error}`. All inputs use `{rounded.xs}` (4px) — the tightest corner radius in the system.

**`select-input`** — Matches `text-input` styling with a custom dropdown arrow. Used for filtering simulation parameters and product variants.

**`textarea`** — Same styling as `text-input` but with 12px padding and no fixed height. Used for configuration notes and support requests.

### Navigation
**`nav-bar`** — A fixed 72px header with `{colors.canvas}` background and `{colors.ink}` text. Navigation links use `{typography.nav-link}` (14px, uppercase, 600 weight) for a technical, spec-sheet feel. Active links render in `{colors.primary}`. On scroll, a subtle `boxShadow` appears to separate the nav from content.

**`nav-link-active`** — Active navigation item in `{colors.primary}` with no background. The uppercase weight-600 treatment gives the nav a precision-instrument quality.

**`nav-link-inactive`** — Inactive navigation item in `{colors.muted}` (#9d9d9d), maintaining readability without competing with the active state.

### Cards
**`product-card`** — A border-only card with `{colors.surface-card}` background and `{colors.ink}` text. No corner rounding — the card is a strict rectangle. Hover state adds a subtle `boxShadow` and darkens the border to `{colors.muted-soft}`. Used for headset product listings like XR-4 and Varjo Aero.

**`product-card-spec`** — A small label within product cards showing specification labels (e.g., "RESOLUTION", "FOV"). Uses `{colors.surface-soft}` background, `{colors.spec-label}` text, and `{typography.spec-label}` (12px uppercase with 0.5px letter-spacing). The `{rounded.xs}` (4px) keeps it crisp.

### Badges
**`badge`** — A neutral badge with `{colors.surface-soft}` background and `{colors.muted}` text. Uses `{typography.badge}` — Space Mono at 11px, uppercase, 700 weight — for a technical, telemetry-readout feel. `{rounded.xs}` (4px) keeps it sharp.

**`badge-primary`** — A blue badge using `{colors.primary}` background and `{colors.on-primary}` text. Used for "NEW" or "FEATURED" indicators on products.

**`badge-error`** — A red badge using `{colors.error}` background. Used for "CRITICAL" or "WARNING" status indicators.

**`badge-success`** — A green badge using `{colors.success}` background. Used for "READY" or "CERTIFIED" status indicators.

### Hero Sections
**`hero-section`** — A full-width section with `{colors.canvas}` background and 80px vertical padding. Used for product launches and feature highlights.

**`hero-section-dark`** — A dark variant using `{colors.dark-bg}` (#141414) background with white text. Used for immersive simulation demos and video backgrounds.

**`hero-headline`** — The primary headline in `{typography.display-xl}` (32px, 700 weight, -0.5px letter-spacing). The tight spacing gives it a technical, precision feel.

**`hero-subheadline`** — Supporting text in `{typography.body-md}` (16px, 400 weight, 1.6 line-height). The generous line-height ensures readability against the dense blue or dark backgrounds.

### Footer
**`footer`** — A dark footer using `{colors.dark-bg}` (#141414) background with `{colors.muted-soft}` (#aaaaaa) text. Links use `{typography.link}` (14px, 500 weight) and hover to white. Section headings use `{typography.title-sm}` (16px, 600 weight) in white.

### Spec Tables
**`spec-table`** — A border-only table with no corner rounding. Rows alternate between `{colors.canvas}` and `{colors.surface-card}` backgrounds with a `{colors.hairline-soft}` bottom border. Labels use `{typography.spec-label}` (12px uppercase, 500 weight, 0.5px letter-spacing) in `{colors.spec-label}` (#5b5b5b). Values use `{typography.spec-value}` (14px, 400 weight) in `{colors.spec-value}` (#16160e). This is the core component for technical specification sheets.

### Interactive Elements
**`toggle-switch`** — A pill-shaped toggle with `{colors.muted-soft}` background in off state and `{colors.primary}` in on state. The knob is white and circular. Used for simulation toggles and settings.

**`progress-bar`** — A thin 4px bar with `{colors.hairline}` background and `{colors.primary}` fill. Used for loading states and simulation progress.

**`tooltip`** — A dark tooltip with `{colors.ink}` background and `{colors.canvas}` text. Uses `{typography.caption-sm}` (12px, 400 weight) with 4px padding. `{rounded.xs}` (4px) keeps it sharp.

**`modal-overlay`** — A semi-transparent overlay using `rgba(22, 22, 14, 0.6)` — the `{colors.ink}` value at 60% opacity.

**`modal-content`** — A white modal with no corner rounding, 32px padding, and a 12px shadow. Used for configuration dialogs and simulation settings.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, nav collapses to hamburger, product cards stack vertically, spec tables become scrollable horizontally, hero padding reduces to 48px, display-xl drops to 24px |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but reduced font-size to 13px, hero sections use 64px padding, spec tables show full width |
| Desktop | 1128–1440px | Full three-column product grid, nav at 72px height with uppercase links, hero sections at 80px padding, spec tables with fixed column widths |
| Wide | > 1440px | Max-width container at 1440px, nav links gain additional spacing, hero sections use 96px padding, product cards can show additional spec details |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch targets
- Nav links on mobile use 48px touch targets
- Toggle switches are 28px tall with 20px knobs for easy manipulation
- Search bar maintains 44px height across all breakpoints
- Product card CTAs are 48px on mobile for easier tapping

### Collapsing Strategy
- Navigation collapses to hamburger menu below 744px, with full-height overlay menu
- Product spec tables become horizontally scrollable below 744px, with sticky first column
- Hero sections collapse to single-column layout below 744px, with image stacking below text
- Footer columns collapse to 2-column grid below 744px, single column below 480px
- Product card grids collapse from 3 columns to 2 at tablet, to 1 at mobile
- Multi-step forms collapse to single-step with accordion sections below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list appears to be a generic web palette dominated by blues, grays, and a single red accent (#da1e28) and green (#219653). The brand's TRUE primary (#0205be) is the most distinctive blue in the list, but it's possible the brand uses additional accent colors (e.g., a specific orange or teal for simulation overlays) that weren't captured in the extraction.
- Hover states for all components are inferred from the primary-active color and standard interaction patterns — actual hover transitions (duration, easing) were not extracted.
- Error and success states for forms (error messages, success banners) are inferred from the extracted red and green — actual error text colors and background tints were not captured.
- Dark mode colors (#141414, #2e2d2d, #26323d) are inferred from extracted dark tones — the brand may use a specific dark theme palette that wasn't fully captured.
- Font weights for Akkurat and Lateral are assumed based on standard grotesque weights (400, 500, 600, 700) — the actual weight distribution on the live site may differ.
- Space Mono is used for badges and monospace elements, but its exact usage context (telemetry readouts, code blocks, spec labels) is inferred from the font's technical character.
- Animation and transition specifications (duration, easing curves, stagger delays) were not extracted.
- The brand may use a specific grid system or layout constraints that weren't captured in the extraction.
- Sub-brand or product-specific color variations (e.g., Varjo Aero vs. XR-4 specific colors) were not identified.
- The meta theme-color was not set, suggesting the brand may not use a browser chrome color — or it may be set dynamically via JavaScript.
