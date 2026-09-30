---
version: alpha
name: "Petros Guitars"
source_url: "https://www.petrosguitars.com"
captured_at: "2026-09-29T04:00:30.189750+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Petros Guitars is a Squarespace-built site for a small-batch, family-run
  acoustic-guitar and ukulele workshop founded in 1972. The observed palette
  is dominated by neutral grayscale (#ffffff, #fafafa, #f6f6f6, #e7e7e7,
  #272727, #111111, #000000) typical of a Squarespace default theme, with a
  small set of warm accent hexes (#8f1100, #f0523d, #dc5d54) that stand out
  against the neutrals and are proposed here as the brand accent family,
  evoking the rosewood/mahogany tones associated with the instruments. Two
  font stacks are present in the CSS: a serif display face (big-caslon-fb)
  suited to the brand's "tradition of distinction" narrative, and a
  sans-serif workhorse (proxima-nova) used for UI and body copy, both with
  generic fallbacks. This interpretation treats the serif as a heritage
  display voice for hero/section headings and the sans-serif for navigation,
  body text, and buttons — a common editorial pairing but not confirmed as
  the live rendered choice on every element. Layout patterns (hero, product
  cards, footer) are inferred as reasonable Squarespace-typical structures
  for a maker/portfolio site, not measured from a rendered page.

colors:
  primary: "#8f1100"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#272727"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#f0523d"
  accent-warm-muted: "#dc5d54"
  border-subtle: "#e7e7e7"
  text-secondary: "#3e3e3e"
  overlay-dark: "#22222266"
typography:
  display-xl: {fontFamily: "big-caslon-fb, serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "big-caslon-fb, serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "proxima-nova, Helvetica Neue, Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "proxima-nova, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "proxima-nova, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "proxima-nova, Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "proxima-nova, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-subtle}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlayColor: "{colors.overlay-dark}"
    headingTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  waitlist-form:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    buttonBackground: "{colors.primary}"
    buttonText: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"

## Components

**button-primary** is the dark warm-red call-to-action style, proposed for actions like "Learn More" and "Contact Us to be Added to the List." Hover/focus states are not observed; a subtle opacity or darken shift is a reasonable proposed treatment.

**button-secondary** is an outlined variant for lower-priority actions (e.g., "See More Instruments"), using the same accent as border and text with a transparent fill, consistent with the outline-button CSS rules present in the extracted stylesheet.

**text-input** covers contact-form fields such as name/email collection for the guitar-order waitlist described in the copy. Border and fill colors are drawn from the neutral palette; focus-ring styling is not observed and is proposed as a thin primary-colored outline.

**nav-bar** represents the top-level site navigation (Ordering, Gallery, Luthier Supplies, Contact) implied by the page text. A simple white bar with dark text and a hairline bottom border is proposed; no scroll or sticky behavior was observed.

**product-card** is proposed for gallery/instrument listings, pairing a serif title with sans-serif descriptive copy on a white card with a subtle border, suited to showcasing individual handmade guitars or the "#500" milestone instrument.

**hero** models the homepage introduction ("Handmade acoustic guitars built just for you") as a dark, full-bleed section with large serif display type and an optional dark overlay, reflecting the workshop-photography style implied by a luthier brand, though no image or exact composition was observed.

**footer** is a light, low-contrast band holding contact details (petros@petrosguitars.com) and secondary links, using muted body text on a soft off-white background drawn from the palette.

**badge** is proposed for small status labels such as "#500" or "Not Accepting New Orders," using the warm accent as a pill-shaped highlight — a pattern not directly observed but consistent with the milestone-announcement content.

**waitlist-form** is a category-specific component addressing the site's stated current state: order slots are closed and visitors are invited to join an email notification list. It combines a soft background, a short explanatory heading, and a primary-styled submit action, reflecting the documented "Contact Us to be Added to the List" flow.

## Responsive Behavior

Proposed breakpoints (not measured): mobile ≤600px (single-column, stacked nav collapsing to a menu icon), tablet 601–1024px (two-column galleries, condensed nav), desktop ≥1025px (full multi-column layout, expanded nav). Touch targets for buttons and nav items should be at least 44×44px. Navigation is expected to collapse into a hamburger/off-canvas menu below tablet width, consistent with common Squarespace patterns, but this collapse behavior was not directly observed on the source page.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is derived from static CSS/text extraction only; no rendered page, computed styles, or DOM screenshots were available. Color-role assignments (primary, accent, surfaces) are inferred from a large undifferentiated palette shared across Squarespace UI/form utility classes and third-party social-icon colors, so some accent hexes may not represent actual brand usage. Typography sizes, weights, and letter-spacing are proposed defaults, not measured values, though the two font families (big-caslon-fb, proxima-nova) are directly present in the supplied CSS. Interaction states (hover, focus, active), mobile navigation behavior, and actual layout/grid structure were not observed and are marked proposed throughout. Licensing and hosting availability of the Adobe Typekit-served fonts (big-caslon-fb, proxima-nova) were not verified.
