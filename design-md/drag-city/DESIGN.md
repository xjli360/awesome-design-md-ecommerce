---
version: alpha
name: "Drag City"
source_url: "https://www.dragcity.com"
captured_at: "2026-09-28T05:08:56.706490+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Drag City's stylesheet reflects a long-running independent label site built on
  restrained, editorial conventions rather than a modern branded system. Body copy
  is set in Georgia/"Times New Roman" serif at 14px with an 18px line-height and a
  muted #666 body color, giving the huge artist roster and liner-note-style copy a
  literary, print-catalog feel. Sidebar modules (reviews, press assets, press clips)
  switch to Arial/Helvetica sans-serif, an inferred convention separating narrative
  copy from utility/metadata blocks. Headings use black (#000) or dark charcoal
  (#333, #474747) text with no observed weight declaration on the largest heading,
  so display weight is treated as proposed. The single clear interactive accent is
  #0098ff, used consistently as a link/hover color across product lists, reviews,
  and press panels, and is adopted here as the primary action color. A pale sky-blue
  (#9cc4dc) tiles the page background, with white (#ffffff) used for content
  surfaces like the new-releases module. Additional palette entries (#cc1804,
  #e6001b, #00721e, #eeee00, #00aef0, #ff2a00) appear without confirmed usage
  context in the supplied evidence; they are carried forward as inferred accent/
  status colors (e.g., badges, alerts, in-stock indicators) rather than confirmed
  brand meanings. Rounded corners and spacing scale are proposed conventions, not
  measured from source, since no border-radius or margin/padding rhythm was
  supplied beyond isolated pixel values.

colors:
  primary: "#0098ff"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#666666"
  muted: "#999999"
  hairline: "#cccccc"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  text-strong: "#333333"
  text-mid: "#444444"
  heading-gray: "#474747"
  muted-light: "#aaaaaa"
  muted-mid: "#c2c2c2"
  border-soft: "#e3e4e4"
  border-softer: "#e6e6e6"
  page-band: "#9cc4dc"
  pale-blue: "#e1f2fd"
  pale-blue-alt: "#e7f3fa"
  cool-blue-gray: "#a5b8c4"
  secondary-blue: "#00aef0"
  accent-red: "#cc1804"
  accent-bright-red: "#e6001b"
  accent-orange-red: "#ff2a00"
  accent-green: "#00721e"
  accent-yellow: "#eeee00"
typography:
  display-xl: {fontFamily: "Georgia, 'Times New Roman', serif", fontSize: 36px, fontWeight: 400, lineHeight: 1.1, letterSpacing: 0px}
  display-md: {fontFamily: "Georgia, 'Times New Roman', serif", fontSize: 28px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Georgia, 'Times New Roman', serif", fontSize: 18px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Georgia, 'Times New Roman', serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.29, letterSpacing: 0px}
  body-sm: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 13px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.3px}
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.text-strong}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.page-band}"
    textColor: "{colors.text-strong}"
    typography: "{typography.body-sm}"
    hoverColor: "{colors.primary}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    titleColor: "{colors.text-strong}"
    titleHoverColor: "{colors.primary}"
    typography: "{typography.title-md}"
    border: "1px solid {colors.border-softer}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    headingColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.page-band}"
    textColor: "{colors.text-mid}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.md}"
  audio-player:
    backgroundColor: "{colors.surface-soft}"
    controlSize: "26px"
    border: "none"
    rounded: "{rounded.none}"
    padding: "{spacing.xs}"

## Components

**button-primary** uses the observed hover-link blue (`#0098ff`) as a solid fill, since no dedicated button-background color was present in the evidence; this is a proposed mapping from an interactive accent to a call-to-action surface.

**button-secondary** is a lighter, bordered variant for lower-emphasis actions (e.g., "add to cart" alternates, filters), built from the soft gray surface and hairline border observed on content panels. State changes (hover/active) are not confirmed and remain proposed.

**text-input** assumes a plain white field with a light gray hairline border, consistent with the site's understated, non-illustrated form aesthetic. No focus-state styling was present in the supplied CSS, so focus treatment is proposed only.

**nav-bar** is grounded in `.site-navigation .primary` rules showing sprite-based buttons and a search control; the pale blue page-band color is reused here as a plausible nav background, though the actual nav background color was not explicitly confirmed in the excerpt.

**product-card** reflects `.product-list h2/h3` styling directly: dark gray title text (`#333`) that shifts to the primary blue on hover, appropriate for the record/artist grid layout implied by "Record Shop" and "New Releases" sections.

**hero** is a proposed pattern for a top-of-page artist or release feature, using the `.content-heading h1 span.untitled` values (36px, black, 68px line-height context) as the closest observed analog for a large heading treatment.

**footer** is inferred entirely; no footer-specific selectors were supplied, so it borrows the page-band background and mid-gray body text color used elsewhere for secondary content.

**badge** is speculative, using one of the unconfirmed accent colors (`#eeee00`) as a small label treatment — plausible for "new," "sale," or "limited" tags on a record-shop site, but not verified against any supplied badge selector.

**search** reflects the `.site-navigation .primary li.search button` sprite-button pattern, reinterpreted here as a text-input-style search affordance since the actual rendered search field markup was not included in evidence.

**audio-player** is the one category-specific, strongly grounded component: `.mp3-player .control button` confirms 26×26px sprite-based transport controls with no border and a transparent background, matching a record label's embedded track-preview player.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior (no media queries were present in the supplied CSS excerpt):

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <600px | Single-column artist/product lists, nav collapses to a toggle, audio-player controls stack full-width. |
| tablet | 600–1024px | Two-column product grid, sidebar (reviews/press) moves below main content. |
| desktop | >1024px | Multi-column layout matching the fixed-width `.content-heading` (~1007px) implied by observed pixel widths. |

Touch targets should be at least 40×40px; the observed 26px mp3-player buttons would need visual padding to meet this on touch devices — a proposed adjustment, not an existing pattern.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is static CSS extraction plus one text excerpt; no live rendering, computed layout, or DOM structure was observed.
- Several palette colors (`#cc1804`, `#e6001b`, `#00721e`, `#eeee00`, `#00aef0`, `#ff2a00`) have no confirmed selector usage in the supplied rules; their assigned roles (accent/badge/status) are inferred and speculative.
- No border-radius values were present anywhere in the supplied CSS; the entire `rounded` scale is proposed.
- No explicit spacing/margin system was observed beyond isolated pixel values (e.g., `12px`, `15px`, `20px`); the `spacing` scale is a proposed convention, not extracted.
- Heading font-weight for `display-xl` was not specified in the source rule and is treated as proposed (400) pending confirmation.
- Hover/focus/active interaction states beyond link-color hover (`#0098ff`) were not observed; all other state styling is proposed.
- Mobile/responsive layout, breakpoints, and nav-collapse behavior were not present in the evidence and are entirely proposed.
- Font rendering relies on system fallbacks (Georgia/Times New Roman, Arial/Helvetica); no custom/licensed webfont was found, and licensing status of any future custom font is unverified.
