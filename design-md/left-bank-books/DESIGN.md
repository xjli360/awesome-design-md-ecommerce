---
version: alpha
name: "Left Bank Books"
source_url: "https://www.leftbankbooks.com"
captured_at: "2026-09-28T09:34:27.067819+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Left Bank Books' stylesheet exposes a compact, high-contrast palette built
  from black, white, and a family of dark reds (#3f0000, #880000, #aa0200)
  alongside a small cluster of saturated accent tones (#cc33cc, #ffff00,
  #9999ee, #cc99cc) and two greys (#c0c0c0, #cccccc). The only confirmed
  typeface is "Avenir Next" with a sans-serif fallback, applied to body text
  in white; a monospace fallback is also declared but its usage context is
  not shown. Confirmed component styling is limited to store/browse buttons
  and mobile category buttons: black-on-white or white-on-black fills, bold
  uppercase labels, generous letter-spacing, and a consistently rounded
  1rem (16px) radius.
  This interpretation treats black as the working canvas and white as the
  primary reading color, both directly observed. The reds are assigned to
  primary/surface roles as an inferred extension consistent with the
  store's radical, small-press identity, since no explicit background usage
  for them was captured. Greys are inferred as hairlines/muted text. All
  additional accent colors are preserved as available palette entries
  rather than assigned load-bearing roles, since their real usage was not
  observed in the supplied CSS.

colors:
  primary: "#aa0200"
  ink: "#000000"
  canvas: "#000000"
  body: "#ffffff"
  muted: "#cccccc"
  hairline: "#c0c0c0"
  surface-soft: "#3f0000"
  surface-card: "#880000"
  on-primary: "#ffffff"
  accent-purple: "#cc33cc"
  accent-yellow: "#ffff00"
  accent-lavender: "#9999ee"
  accent-mauve: "#cc99cc"
typography:
  display-xl: {fontFamily: "Avenir Next, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Avenir Next, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Avenir Next, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Avenir Next, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Avenir Next, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Avenir Next, sans-serif", fontSize: 12px, fontWeight: 700, lineHeight: 1.4, letterSpacing: 2px}
  button-md: {fontFamily: "Avenir Next, sans-serif", fontSize: 13px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 2px}
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
    rounded: "{rounded.lg}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  category-list-button:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.lg}"
    padding: "{spacing.sm}"

## Components

**button-primary** reflects the confirmed store/browse submit-button pattern: a solid fill with bold, uppercase, letter-spaced text and the site's signature 1rem/16px radius. The fill color here is proposed as the deep red primary rather than the observed black, extending the pattern toward a more brand-forward accent; the hover inversion (white fill, black text) is confirmed in CSS and should be treated as the default interactive state.

**button-secondary** is a proposed inverse of the primary pattern, useful for lower-emphasis actions (e.g., "View Cart") using the confirmed white-fill/black-text combination already present in the CSS as a resting state, paired with a light hairline border for definition on dark backgrounds.

**text-input** is proposed; no input styling beyond `color: inherit; font: inherit` was observed in normalize.css, so field chrome, border, and radius are inferred to match the button radius language at a smaller scale.

**nav-bar** is proposed to hold the site's stated navigation items (Home, Store, Popular Titles, About Us, Events, etc.) against the dark canvas, using confirmed body typography; no fixed/sticky behavior or breakpoint collapse was observed.

**product-card** is proposed for listing individual books/titles, using a dark surface-card red to differentiate from pure black canvas while remaining within the observed palette; no actual card markup was present in the supplied CSS.

**hero** is proposed for the homepage welcome/intro copy, set against the darker maroon surface tone to create depth without introducing new colors; heading size is a proposed display scale, not measured.

**footer** is proposed using muted grey text on the dark canvas for secondary links (Volunteer, Links, Books to Prisoners), consistent with the site's minimal, text-forward tone.

**badge** and **search** are proposed utility components (e.g., cart-count indicator, site search) built from the confirmed rounded/uppercase/bold button vocabulary rather than any directly observed badge or search markup.

**category-list-button** directly reflects the observed `.categoriesMobile button` rule (uppercase, letter-spaced, bold, white fill, black text, 1rem radius) and is retained as its own component since it is a distinct, evidence-backed pattern likely used for mobile category browsing.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior, since no media queries were included in the supplied evidence:

| Breakpoint | Width      | Notes (proposed) |
|-----------|-----------|-------------------|
| mobile    | 0–599px   | Single column; `.categoriesMobile` pattern suggests a stacked, full-width button list for category browsing. |
| tablet    | 600–959px | Two-column product/category grid; nav may collapse into a toggled menu. |
| desktop   | 960px+    | Multi-column layout; persistent horizontal navigation. |

Touch targets should be at least 44×44px; the observed `.5rem` button padding and `1rem` radius should be preserved across breakpoints. Any menu collapse, hamburger behavior, or actual mobile layout is not observed and should be validated against the live site before implementation.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS extraction cannot confirm actual page background color; canvas is inferred from `body { color: #fff }` implying a dark surface, not directly observed.
- Semantic roles for the red family (#3f0000, #880000, #aa0200) and the accent cluster (#cc33cc, #ffff00, #9999ee, #cc99cc) are inferred placements, not confirmed usage locations.
- Font weight/size values beyond the button and `.categoriesMobile` rules (e.g., headings, body copy sizing) are proposed, not measured.
- No hover/focus/active states were observed except the single button hover inversion; all other interaction states are proposed.
- Mobile/responsive layout, breakpoints, and menu collapse behavior were not present in the supplied CSS and are not observed.
- "Avenir Next" availability/licensing on end-user devices is not verified; fallback to system sans-serif should be assumed in production.
