---
version: alpha
name: "Bob's Red Mill"
source_url: "https://bobsredmill.com"
captured_at: "2026-09-28T09:48:09.613842+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Evidence centers on a warm, earthy palette anchored by mill-red ("#e03c31") as
  the primary action color, paired with a deep umber ink ("#3e2b2e") and a soft
  cream surface ("#faf2e3") that the CSS variable --color-autumn-wheat assigns
  as button text-on-red, and which this spec also treats as a warm background
  surface (inferred). White ("#ffffff") is used as the canvas/card surface.
  Neutral grays ("#7e8594", "#e7e9ee") drawn from the supplied palette were
  assigned to muted-text and hairline roles by inference, since no dedicated
  role classes were supplied for them in the evidence. Typography draws on two
  proprietary display families — "Red Mill Sans" (bold, condensed/stretched
  headlines and uppercase category labels) and "Red Mill Serif" (an editorial
  accent face) — plus "Cabin" for product-card labels and, by inference, general
  body copy, as it is the only humanist sans observed for smaller UI text.
  Button styling (5px radius, uppercase 18px Red Mill Sans, 0.72px tracking) is
  taken directly from the observed .btn rules. This interpretation proposes a
  rustic, ingredient-forward system: cream surfaces, a confident red
  call-to-action, and a serif/sans pairing echoing the brand's since-1978
  milling heritage, balanced with clean product and recipe cards suited to a
  baking-mix catalog. No live layout, breakpoints, or interaction states beyond
  the supplied hover rules were observed.

colors:
  primary: "#e03c31"
  primary-alt: "#fb4143"
  ink: "#3e2b2e"
  canvas: "#ffffff"
  body: "#3e2b2e"
  muted: "#7e8594"
  hairline: "#e7e9ee"
  surface-soft: "#faf2e3"
  surface-card: "#ffffff"
  on-primary: "#faf2e3"
  accent-green: "#5cb767"
typography:
  display-xl: {fontFamily: '"Red Mill Sans", sans-serif', fontSize: 50px, fontWeight: 700, lineHeight: 0.95, letterSpacing: 0px}
  display-md: {fontFamily: '"Red Mill Serif", serif', fontSize: 46px, fontWeight: 700, lineHeight: 0.95, letterSpacing: 0px}
  title-md: {fontFamily: '"Red Mill Sans", sans-serif', fontSize: 22px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: '"Cabin", sans-serif', fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: '"Cabin", sans-serif', fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: '"Cabin", sans-serif', fontSize: 12px, fontWeight: 600, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: '"Red Mill Sans", sans-serif', fontSize: 18px, fontWeight: 700, lineHeight: 1.28, letterSpacing: 0.72px}
rounded:
  none: 0px
  xs: 2px
  sm: 5px
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    hoverTextColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  recipe-card:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"

## Components

**button-primary** reflects the observed `.btn.btn-red` rule: mill-red fill, cream (`autumn-wheat`) label, uppercase Red Mill Sans with 0.72px tracking, and a 5px radius directly measured from `border-radius:5px`. Hover-to-outline (fill drops, text becomes red) is observed in `.btn.btn-red:hover` and is retained conceptually here, though exact transition timing is not restated.

**button-secondary** mirrors the observed `.btn.btn-red-subtle` pattern: red outline on transparent background, inverting to filled red with cream text on hover. Proposed as the standard secondary action (e.g., "Learn More" links seen throughout the copy).

**text-input** is a proposed pattern; no form-field CSS was supplied. Border, radius, and padding are inferred from general site spacing and the neutral hairline gray in the palette.

**nav-bar** is inferred from the extensive mega-menu text content (Products, Recipes, Articles, Where to Buy, Our Story) but no nav CSS rules were supplied, so background, spacing, and behavior are proposed on a light canvas with ink-colored labels.

**product-card** is grounded in `.product-card-link` and `.small-product-title`: Cabin at 18px/600 for the clickable title, with a mill-red hover state directly observed. Card container styling (border, radius, padding) is proposed.

**hero** is proposed but informed by the `--hero-spacing:-177px` custom property, which suggests an overlapping/pulled-up hero composition (e.g., a hero image bleeding into content below). Background uses the cream surface tone; exact hero markup was not observed.

**footer** is proposed, using the dark ink tone as background and cream text for contrast, echoing the on-primary treatment used on red buttons. Footer link list (About Us, Community Impact, Press & Media, etc.) is confirmed from page text; visual styling is not.

**badge** is a proposed small-label component for callouts like "Non-GMO Project Verified" and "Gluten Free," which appear repeatedly in navigation text. The green accent is drawn from the supplied palette but its brand role (approval/certification) is inferred, not confirmed by any CSS class.

**search** is proposed based on the dense "Popular Searches" content blocks in the evidence, implying a prominent search feature; no search-input CSS was supplied.

**recipe-card** is a category-specific proposal for the Baking Mixes / Bread Mixes vertical, styled on the warm cream surface with a red accent, intended for recipe tiles like "Easy Everything Bagels" or "Berrylicious Strawberry Rhubarb Hand Pies" referenced in the page text.

## Responsive Behavior
Recommended, not measured from the live site:

| Breakpoint | Width      | Behavior (proposed)                              |
|------------|-----------|---------------------------------------------------|
| sm         | 0–599px   | Single-column stack; nav collapses to hamburger    |
| md         | 600–959px | 2-column product grid; condensed mega-menu         |
| lg         | 960–1279px| 3-column product grid; full nav bar visible        |
| xl         | 1280px+   | 4-column product grid; hero at full display-xl size|

Touch targets should be a minimum 44×44px, matching or exceeding the observed 56px `.btn` height. Primary nav is assumed to collapse into a hamburger/drawer pattern below `md`, consistent with the deep, multi-level menu text (Featured Flours, By Need, Mealtime & More, etc.) implied by the evidence, though no mobile nav markup was supplied.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS and page-text evidence only; no rendered layout, computed styles, or JavaScript-driven interactions were observed. Role assignments for muted text, hairlines, and surface-soft/accent-green colors are inferred from the general palette, not from role-specific CSS classes. Typography sizes for `title-md`, `body-md`, `body-sm`, and `caption` are proposed estimates, not measured from supplied CSS (only `display-xl`, `display-md`, and `button-md` map to directly observed rules). Breakpoints, grid columns, and mobile navigation behavior are proposed recommendations, not measured site behavior. Availability, licensing, and full character support of the proprietary "Red Mill Sans" and "Red Mill Serif" fonts were not verified. Hover/focus states beyond the two explicitly supplied `.btn` and `.product-card-link` hover rules are unconfirmed.
