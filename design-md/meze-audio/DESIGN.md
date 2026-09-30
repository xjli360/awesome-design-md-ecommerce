---
version: alpha
name: "Meze Audio"
source_url: "https://mezeaudio.com"
captured_at: "2026-09-28T09:59:45.425466+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Meze Audio's storefront CSS points to a restrained, materials-led palette: a
  muted olive-brass (#585336) paired with a warm off-white (#faf7f1) forms the
  review-widget accent pairing and is treated here as the primary brand mark,
  since it is the only color explicitly assigned dual foreground/background
  roles in the evidence (--jdgm-primary-color / --jdgm-write-review-bg-color).
  Supporting neutrals range from near-black (#141b22, #000000) through mid
  grays (#333333, #666666, #97907d) to light card surfaces (#eeeeee, #f2f2f2,
  #dddddd), consistent with a premium-audio catalog that relies on product
  photography rather than bright UI color. A warm beige (#e7d8c9) and a teal
  (#108474) appear in the palette and are mapped as secondary accents for
  tags/badges; their exact usage was not confirmed live. Typography is
  explicitly split in the CSS: headings (h1-h6, h0, blockquote) load
  "Reforma Gris" forced to normal weight, while body copy and buttons load
  "Reforma Blanca," both with sans-serif fallback. Numeric type-scale tokens
  (--text-h0 through --text-xs) are taken directly from :root and vary across
  two breakpoints; the larger set is used as the base scale here. Border
  radius is only confirmed at 0 (review widget); all other radii and the
  spacing scale are inferred conventions layered onto the unresolved
  --spacing-* custom properties present in the source.

colors:
  primary: "#585336"
  ink: "#141b22"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#97907d"
  hairline: "#dddddd"
  surface-soft: "#faf7f1"
  surface-card: "#eeeeee"
  on-primary: "#faf7f1"
  border-strong: "#cccccc"
  accent-beige: "#e7d8c9"
  accent-teal: "#108474"
  ink-secondary: "#666666"
typography:
  display-xl: {fontFamily: "\"Reforma Gris\", sans-serif", fontSize: 64px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "\"Reforma Gris\", sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "\"Reforma Gris\", sans-serif", fontSize: 28px, fontWeight: 400, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "\"Reforma Blanca\", sans-serif", fontSize: 17px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "\"Reforma Blanca\", sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  caption: {fontFamily: "\"Reforma Blanca\", sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "\"Reforma Blanca\", sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1, letterSpacing: 0.3px}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-beige}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"

## Components

**button-primary** uses the observed olive-brass/cream pairing from the
review-widget variables as the closest confirmed brand-color relationship;
CSS confirms a `.button:hover` opacity dim to 0.85 as the only observed
interaction state, so hover/active/disabled beyond that are proposed.

**button-secondary** is an outlined variant proposed for lower-emphasis
actions (e.g., "Add to compare"); no outline-button markup was present in
the evidence, so styling is inferred from the primary button's palette.

**text-input** is proposed for search, newsletter, and account forms; the
hairline border and white canvas follow the general neutral palette, but no
input-specific selectors were captured.

**nav-bar** reflects the confirmed sticky header (`position: sticky; top:0;
z-index:10`) with a semi-transparent background (`--header-background-opacity:
0.92`, 20px blur) and a near-white transparent-state text color
(`247 247 247`); the resting-state colors mapped here are inferred since the
opaque background hex wasn't isolated in the source.

**product-card** is proposed for the headphone grid (ARTA, EMPYREAN II,
STRADA, etc. named in nav) using the light card surface and hairline border;
actual card markup/shadow was not present in the CSS evidence.

**hero** is proposed for the homepage lead banner ("Sound. Comfort. Design.
True High-End.") using the dark ink background with display-xl type; live
hero markup was not confirmed.

**footer** groups Community/Our Story/Dealer links seen in the nav text on a
dark ground; the muted taupe (#97907d), which the evidence shows used for a
small blog byline (`.connect-header`), is repurposed here for secondary
footer text.

**badge** is proposed for product tags such as "New" or series labels
(e.g., "2nd Gen"), using the warm beige accent for a soft, non-brand-color
highlight; no badge component was present in the CSS.

**search** styles the header search affordance referenced in nav text
("Search"); treated as a soft cream field to differentiate from standard
white inputs, though field styling itself was not observed.

**spec-table** is a category-appropriate addition for headphone technical
specifications (driver type, impedance, weight) common on audiophile product
pages; entirely proposed, as no table markup was present in the evidence.

## Responsive Behavior

Recommended breakpoints, not measured from live rendering:

| Breakpoint | Width      | Notes                                         |
|-----------|------------|------------------------------------------------|
| Mobile     | 0–599px    | Single-column product list, collapsed nav      |
| Tablet     | 600–1023px | 2-column product grid (matches observed `--product-list-items-per-row: 2`) |
| Desktop    | 1024–1439px| Full nav-bar (main-nav/logo/secondary-nav grid observed) |
| Wide       | 1440px+    | Larger type scale applies (h0 64px vs 52px confirmed in two `:root` blocks) |

Touch targets should be at least 44px tall for nav and button components.
The header's grid-template (`"main-nav logo secondary-nav"`) and logo-size
shrink on scroll/breakpoint (85×150 → 40×71 in evidence) suggest a
collapsing/hamburger pattern on narrow viewports, but the collapse mechanism
itself was not observed. A horizontally scrolling product carousel is
implied by `--product-list-carousel-item-width: 74vw` on at least one
featured-collection section.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, selector
declarations, and page text only — no rendered layout, computed styles, or
interaction states were observed. The primary/on-primary color pairing is
inferred from the third-party review-widget variables (`--jdgm-*`), not from
a confirmed site-wide brand-color declaration. Heading/body font roles are
confirmed by explicit selector rules, but actual glyph rendering, weights
beyond the forced "normal" override, and license/availability of "Reforma
Gris"/"Reforma Blanca" were not verified. The spacing scale is a proposed
convention layered onto unresolved `--spacing-6/10/12/14/16` variables whose
pixel values were not present in the evidence. Border-radius values beyond
the confirmed `0` (review widget) are proposed defaults. Mobile navigation
collapse, hover/focus states beyond the single observed 0.85-opacity button
hover, product-card and hero markup, and breakpoint pixel values are all
inferred or proposed, not measured.
