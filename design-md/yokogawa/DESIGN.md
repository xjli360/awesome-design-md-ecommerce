---
version: alpha
name: "Yokogawa"
source_url: "https://www.yokogawa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The two-tiered navigation — a #004f9b navy band 32 pixels tall carrying region, language, and support-portal selectors above the main white header — announces before the page renders that this is infrastructure software, not consumer electronics. Where most industrial sites compress secondary hues entirely into system-state roles, Yokogawa deploys a deep purple (#3b0083) at campaign and solution-entry points alongside the primary navy, giving the brand a second chromatic axis with real authority rather than a rescued accent. The status palette itself is borrowed wholesale from measurement instrument conventions: green #43ac6a, amber #f08a24, and red #f04124 each travel with a darker active companion (#368a55, #cf6e0e, #cf2a0e), appearing in product comparison dashboards, alarm-state indicators, and downloadable-document chips with the same semantic grammar found on physical panel meters. Type runs Noto Sans for Latin and CJK body copy — a practical signal that technical documentation ships in Japanese as readily as English — while Consolas and Liberation Mono surface for specification tables and readout-style numerical displays, where monospace column alignment is functionally mandatory. Corner radii hold at {rounded.xs} (2px) across buttons and inputs, stepping to {rounded.sm} (4px) for cards and chips only; there are no pill shapes in the primary UI and no rounded token above 16px. Cards carry {colors.hairline} borders rather than drop shadows, and hover promotes the border to {colors.primary} rather than lifting the surface — a flat, precise interaction vocabulary. The canvas is a clean white with light-gray zones ({colors.surface-soft} at #f5f5f5) delineating content regions. Hero banners run full-bleed photographic backgrounds with dark overlay scrims and reversed type, letting industrial photography carry the visual weight that the reserved type scale and tight radii deliberately withhold.

colors:
  primary: "#004f9b"
  primary-dark: "#003f7c"
  primary-active: "#003f7c"
  primary-disabled: "#a0d3e8"
  accent-purple: "#3b0083"
  ink: "#222222"
  body: "#363a3d"
  muted: "#646464"
  muted-soft: "#94989a"
  charcoal: "#565656"
  hairline: "#dbdddd"
  hairline-soft: "#e7e7e7"
  border-strong: "#b8babc"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#f6f6f7"
  surface-subtle: "#edeeee"
  on-primary: "#ffffff"
  status-success: "#43ac6a"
  status-success-dark: "#368a55"
  status-warning: "#f08a24"
  status-warning-dark: "#cf6e0e"
  status-error: "#f04124"
  status-error-dark: "#cf2a0e"
  readout-blue: "#61b6d9"
  readout-blue-soft: "#a0d3e8"

typography:
  display-xl:
    fontFamily: "'Noto Sans', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Noto Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Noto Sans', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Noto Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Noto Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Noto Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Noto Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Noto Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Noto Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-label:
    fontFamily: "'Noto Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.36
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Noto Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Noto Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Noto Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  nav-top:
    fontFamily: "'Noto Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  readout-mono:
    fontFamily: "'Consolas', 'Liberation Mono', 'Courier', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.3px
  readout-mono-lg:
    fontFamily: "'Consolas', 'Liberation Mono', 'Courier', monospace"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  spec-value:
    fontFamily: "'Consolas', 'Liberation Mono', 'Courier', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0.2px
  japanese-body:
    fontFamily: "'Noto Sans Japanese', 'Noto Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.8
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 16px
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
    padding: 10px 24px
    height: 40px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: 1px solid
    padding: 9px 23px
    height: 40px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.primary-active}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  button-accent-purple:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: 1px solid
    padding: 8px 12px
    height: 38px
    focus-borderColor: "{colors.primary}"
    focus-outline: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: 1px solid {colors.hairline}
    topBand:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.nav-top}"
      height: 32px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
    padding: "{spacing.base}"
    imageAspect: 4/3
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    hover-borderColor: "{colors.primary}"
    hover-boxShadow: 0 2px 8px rgba(0,0,0,0.08)
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    minHeight: 400px
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: 80px 0
    overlay: rgba(0,0,0,0.40)
  section-header:
    backgroundColor: "{colors.surface-soft}"
    borderLeft: 4px solid {colors.primary}
    titleTypography: "{typography.title-lg}"
    textColor: "{colors.ink}"
    padding: 16px 24px
  status-badge:
    successBackgroundColor: "{colors.status-success}"
    warningBackgroundColor: "{colors.status-warning}"
    errorBackgroundColor: "{colors.status-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.caption-label}"
    rowAltBackgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    cellTypography: "{typography.body-sm}"
    valueTypography: "{typography.spec-value}"
    rounded: "{rounded.none}"
  readout-display:
    backgroundColor: "{colors.ink}"
    valueColor: "{colors.readout-blue}"
    unitColor: "{colors.readout-blue-soft}"
    valueTypography: "{typography.readout-mono-lg}"
    unitTypography: "{typography.readout-mono}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.hairline}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    border: 1px solid
    submitButtonBackgroundColor: "{colors.primary}"
    submitButtonTextColor: "{colors.on-primary}"
    submitButtonRounded: "{rounded.none}"
    submitButtonWidth: 48px
  category-nav-chip:
    backgroundColor: "{colors.surface-subtle}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 14px
    active-backgroundColor: "{colors.primary}"
    active-textColor: "{colors.on-primary}"
  download-cta:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent-purple}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
    padding: 20px 24px
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
  solution-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    accentBarColor: "{colors.accent-purple}"
    accentBarHeight: 3px
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
    padding: "{spacing.xl}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    hover-borderColor: "{colors.accent-purple}"
  footer:
    backgroundColor: "{colors.body}"
    textColor: "{colors.hairline}"
    linkColor: "{colors.readout-blue-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.caption-label}"
    borderTop: 3px solid {colors.primary}
    padding: 48px 0

## Components

### Buttons

**`button-primary`** — Filled #004f9b navy at 40px height with 2px corner radius, 15px semi-bold Noto Sans, 10px/24px padding. Hover deepens to `#003f7c`; disabled washes out to the light blue `#a0d3e8`. The flat, nearly square corner at `{rounded.xs}` reads as mechanical precision rather than friendliness — consistent with instrument hardware aesthetic.

**`button-secondary`** — White fill with a 1px `{colors.primary}` navy border, matching text, same height. On hover the background lifts to `{colors.surface-soft}` and the border deepens to `{colors.primary-active}`. Pairs with `button-primary` in two-action rows (e.g. "Buy Now" / "Request Quote").

**`button-ghost`** — Transparent background, primary-blue text only, no border, `{button-sm}` type at 13px. Used inside cards and table rows where adding a full button border would visually overload dense information layouts.

**`button-accent-purple`** — `{colors.accent-purple}` (#3b0083) fill, identical sizing to `button-primary`. Reserved for solution-campaign CTAs and major download entry points where the purple axis needs a paired action element.

### Text Input

**`text-input`** — 1px `{colors.hairline}` border, 38px height, 2px radius, 8px/12px padding. Focus ring replaces border color with `{colors.primary}` with no outer box-shadow. Placeholder in `{colors.muted-soft}`. Consistent with the form-heavy product configurators and request-for-quote workflows that dominate industrial B2B conversion flows.

### Navigation

**`nav-bar`** — Two-tier structure: a 32px `{colors.primary}` top band holding utility links (region, language, support portal) in 13px regular-weight Noto Sans reversed to `{colors.on-primary}`, sitting above a 56px white main header containing logo, primary nav links at `{typography.nav-link}`, and search. A thin `{colors.hairline}` border separates the white nav from page content. Mega-menu dropdowns use `{colors.canvas}` fill with `{colors.hairline}` column dividers.

### Product Card

**`product-card`** — 4:3 image aspect ratio, 1px `{colors.hairline}` border, 4px radius, 16px internal padding. Title uses `{typography.title-sm}` in `{colors.ink}`, supporting copy in `{typography.body-sm}` in `{colors.body}`. On hover, border color promotes to `{colors.primary}` with a light shadow (0 2px 8px rgba(0,0,0,0.08)) — surface does not lift. Category chips beneath the title use `{category-nav-chip}` styling.

### Spec Table

**`spec-table`** — Column headers carry a solid `{colors.primary}` fill with reversed `{typography.caption-label}` in all-caps 11px. Alternating rows use `{colors.surface-soft}` for data-density legibility. Numerical values in the body render in `{typography.spec-value}` (Consolas monospace) for column alignment; prose cells use `{typography.body-sm}`. No rounded corners — 0px radii throughout.

### Readout Display

**`readout-display`** — Dark `{colors.ink}` (#222222) panel background evoking a physical instrument screen. Primary numeric values render in `{typography.readout-mono-lg}` (20px bold Consolas) in `{colors.readout-blue}` (#61b6d9); unit labels use `{typography.readout-mono}` in the softer `{colors.readout-blue-soft}` (#a0d3e8). Used on product-detail pages and interactive demo widgets to simulate oscilloscope and power-meter panel aesthetics.

### Status Badge

**`status-badge`** — Compact 11px all-caps Noto Sans on filled backgrounds: green (#43ac6a) for active/healthy, amber (#f08a24) for caution/degraded, red (#f04124) for fault/error. 2px radius, 3px/8px padding. Directly mirrors the three-color LED indicator system found on Yokogawa hardware panels, making the semantic mapping intuitive to instrument engineers reading product comparison tables.

### Hero Banner

**`hero-banner`** — Full-bleed photographic background with a 40% black overlay scrim. Title in `{typography.display-xl}` (36px bold) reversed to `{colors.on-primary}`, body in `{typography.body-md}` reversed. Minimum 400px height. Primary CTA uses `button-primary`; secondary uses `button-secondary` with white border and white text variant on the dark field. No rounded shapes break the full-bleed framing.

### Solution Card

**`solution-card`** — White card with a 3px `{colors.accent-purple}` top-edge accent bar, 4px radius, 1px `{colors.hairline}` border. Title in `{typography.title-md}`, body in `{typography.body-sm}`. Hover transitions the full border to `{colors.accent-purple}` to maintain chromatic coherence with the accent bar. Groups industry-vertical solution entries (Oil & Gas, Power, Pharma) in 3-column grids.

### Download CTA

**`download-cta`** — `{colors.surface-soft}` fill, 1px `{colors.hairline}` border, 4px radius, 20px/24px padding. Left or top edge may carry a `{colors.accent-purple}` accent. Title in `{typography.title-sm}`, description in `{typography.body-sm}`. Download button uses `button-accent-purple` to tie the purple axis visually to content acquisition moments.

### Footer

**`footer`** — Dark `{colors.body}` (#363a3d) background with a 3px `{colors.primary}` top border. Link columns use `{typography.caption-label}` (all-caps 11px) for section headings and `{typography.body-sm}` for links in `{colors.readout-blue-soft}`. Copyright and legal text in `{colors.muted-soft}`. Social and legal icons via FontAwesome.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 640px | Top nav band hidden; single-column product grid; hamburger menu replaces horizontal nav links; hero drops to 280px min-height; spec tables scroll horizontally |
| Tablet | 640–1024px | Two-column product grid; nav condenses to icon+label pairs; hero at 340px; solution cards stack to 2-column |
| Desktop | 1024–1440px | Three-column product grid; full two-tier nav visible; four-column footer; spec tables fully inline |
| Wide | > 1440px | Content max-width ~1280px centered; hero imagery scales to fill; five-column footer layout; side-by-side spec + readout panels |

### Touch Targets

- All buttons minimum 40px height; icon-only actions padded to 44px touch area
- Nav-link tap targets extend to full nav-bar height (56px including padding)
- Category chips minimum 36px height on mobile
- Table row tap targets expand to 44px on mobile via increased row padding

### Collapsing Strategy

- Top utility band (region/language/support links) collapses entirely on mobile; moved behind hamburger menu
- Horizontal mega-nav collapses to full-screen drawer with accordion category groups
- Product filter sidebars collapse to a bottom-sheet filter modal on mobile
- Spec tables maintain column structure but scroll horizontally within a scroll-shadow container
- Footer four-column grid stacks to single column; section headings become accordion toggles on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected — font stacks are Noto Sans, Arial, Helvetica (system/generic); if Yokogawa uses a licensed display face for print or campaigns it was not loaded at extraction time
- Exact nav heights (top band 32px, main header 56px) are estimates derived from visual proportion; not extracted as explicit CSS values
- Button padding and height tokens are approximated from common enterprise UI conventions — not pixel-measured from live DOM
- `{colors.accent-purple}` (#3b0083) role (primary campaign accent vs. legacy sub-brand) requires live verification; it may be scoped to specific solution verticals
- Dark-mode or high-contrast alternate palette not observed in extraction; unknown whether one exists
- Icon system (FontAwesome version 5.5.3 detected) specifics — which icon set and custom additions — not catalogued
- Print and PDF stylesheet tokens not captured
- Animation and transition timing values (hover duration, mega-menu open easing) not extracted
