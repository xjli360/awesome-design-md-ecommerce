---
version: alpha
name: "Book Passage"
source_url: "https://www.bookpassage.com"
captured_at: "2026-09-29T04:10:45.257135+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation draws from the observed Book Passage site CSS, which
  exposes a small set of interface colors and a plain system font stack
  (Arial, Helvetica, sans-serif) used across widget and utility elements.
  A CSS custom property references a "--font-raleway" variable name, but no
  Raleway font file, @font-face rule, or actual family declaration was present
  in the supplied evidence, so this design uses only the confirmed Arial/
  Helvetica/sans-serif stack for all typography.
  Color roles are inferred: --color-primary (#2e4550, a muted slate-blue) and
  --color-secondary (#07534e, a deep teal-green) are treated as the brand's
  primary and accent colors, evoking a calm, literary, independent-bookstore
  feel appropriate to author events and community programming. Neutral grays
  (#333333, #454545, #666666, #eeeeee, #f6f6f6) support body text and card
  surfaces, while jQuery UI state colors (#007fff active, #fffa90 highlight,
  #fddfdf error) are repurposed as functional accents for interactive and
  status states. Rounded corners and spacing are proposed conventions, not
  measured. Layout, hover states, and mobile behavior are not observed and are
  marked as proposed throughout.

colors:
  primary: "#2e4550"
  secondary: "#07534e"
  ink: "#000000"
  body: "#333333"
  canvas: "#ffffff"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f6f6f6"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent-active: "#007fff"
  accent-highlight: "#fffa90"
  accent-highlight-text: "#777620"
  accent-error-bg: "#fddfdf"
  accent-error-text: "#5f3f3f"
  border-strong: "#c5c5c5"
typography:
  display-xl: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.2px}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  none: 0px
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-highlight}"
    textColor: "{colors.accent-highlight-text}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  event-listing:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    dateTypography: "{typography.caption}"
    titleTypography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.md}"
    rounded: "{rounded.xs}"

## Components
button-primary is proposed for primary calls to action such as "Add to Cart" or "Register," using the inferred primary slate-blue with white text; no live hover/active/disabled states were observed, so those remain proposed. button-secondary offers an outlined alternative for lower-emphasis actions like "Wishlist," reusing the same primary color as border and text. text-input models basic form fields (search box, login, sign-up) with a light border and neutral text, sized from generic body typography since no explicit input CSS was supplied. nav-bar represents the observed multi-level navigation (Author Events, Classes, Conferences, Books/Gifts/Clubs) as a light bar with small body-sm labels; submenu and active-link states are not observed and are proposed. product-card is designed for book/product tiles, using the light gray surface-card background from the observed `#eeeeee`/`#ededed` values with a hairline border. hero is a proposed banner treatment using the deep primary color as background, intended for top-of-page promotional or author-event imagery; no hero markup was directly observed. footer reuses the deep teal secondary color as a grounding band, a common independent-retailer pattern, though the actual footer markup was not supplied. badge repurposes the jQuery UI "highlight" yellow state for promotional flags (e.g., "New," "Signed Copy"), an inferred reuse of an interaction color for merchandising. search maps to the site's visible search UI (Books/Audiobooks/Services search type selector), using the light gray surface tone seen in widget-header styles. event-listing is a category-specific component built for Book Passage's dense author-event calendar (date/time plus title), styled with caption-weight dates and title-md event names to reflect the text-heavy event lists visible in the page excerpt.

## Responsive Behavior
Recommended, not measured: mobile (<640px) single-column stacking with the nav-bar collapsing into a toggled menu drawer; tablet (640–1024px) two-column event/product grids; desktop (>1024px) three- to four-column grids for events and books. Touch targets should be at least 44px in height for buttons and menu items. This breakpoint scheme is a general proposal for a content/commerce hybrid site and was not derived from any observed media query in the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from a partial, static CSS/text extraction and does not reflect live rendering, computed layout, or interaction states. The `--font-family: var(--font-raleway)` custom property suggests a Raleway typeface was intended by the theme, but no @font-face, font file, or family name was present in the supplied evidence, so all typography here uses only the confirmed Arial/Helvetica/sans-serif stack — actual rendered fonts may differ and should be re-verified against live font loads. Color role assignments (primary, secondary, muted, surface tones) are inferred from CSS variable names and jQuery UI widget theming, not from confirmed brand-guideline documentation. All font sizes, spacing, and rounded-corner values are proposed conventions rather than measured pixel values. Hover, focus, active, and disabled states for buttons, inputs, and nav items were not observed. Mobile menu behavior, grid column counts, and image/hero treatments were not present in the supplied evidence. Custom font licensing and availability (if Raleway is in fact used) were not verified.
