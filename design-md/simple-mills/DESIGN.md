---
version: alpha
name: "Simple Mills"
source_url: "https://simplemills.com"
captured_at: "2026-09-28T10:07:08.995783+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The observed CSS surfaces a warm, food-forward palette anchored by a deep
  maroon-brown (#663333, written as the CSS shorthand #633) used for headline
  accents and primary buttons, paired with saturated yellow-golds (#f6ce3c,
  #f7ce3f, #ffd141, #f2d058) that read as the brand's "sunny, wholesome"
  accent family across hero type and likely badge/callout surfaces. Neutrals
  are limited to pure white, near-black (#333333), and true black
  (#000000), with a near-transparent yellow (#ffd14100) that appears to be a
  hover/transition state rather than a static fill. Typography mixes a
  decorative display face (Braisetto-Bold) for hero headlines, a rounded
  serif-adjacent medium (CooperMdBTWXX-Medium) for section headers, and
  Gotham A/B for buttons and small caps labels; TT Norms Pro appears in the
  broader font stack and is inferred here as the body-copy workhorse since no
  paragraph selector was captured. This interpretation treats maroon as the
  primary brand color and yellow as a secondary/accent family for badges,
  certifications (e.g. Non-UPF Verified), and recipe highlights, reflecting
  the brand's emphasis on clean-ingredient, better-for-you baked goods.
  Layout, spacing, and most component states below are proposed conventions,
  not measured observations.

colors:
  primary: "#663333"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#86412a"
  hairline: "#86412b"
  surface-soft: "#f2d058"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#f6ce3c"
  accent-alt: "#f7ce3f"
  accent-dark: "#83412c"
  highlight: "#ffd141"
  ink-strong: "#000000"
  overlay-transparent: "#ffd14100"
typography:
  display-xl: {fontFamily: "Braisetto-Bold, serif", fontSize: 75pt, fontWeight: 400, lineHeight: 77px, letterSpacing: 0px}
  display-md: {fontFamily: "Braisetto-Bold, serif", fontSize: 36px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "CooperMdBTWXX-Medium, serif", fontSize: 28px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "TTNormsPro-Regular, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "TTNormsPro-Regular, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Gotham A, Gotham B, sans-serif", fontSize: 15px, fontWeight: 500, lineHeight: 23px, letterSpacing: 0.5px}
  button-md: {fontFamily: "Gotham A, Gotham B, sans-serif", fontSize: 13pt, fontWeight: 500, lineHeight: 34px, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    borderBottom: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  hero:
    backgroundColor: "{colors.canvas}"
    headlineColor: "{colors.accent}"
    headlineAccentColor: "{colors.primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  recipe-card:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  badge:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.ink-strong}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.base}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"

## Components

**button-primary** reflects the observed `.btn.callactoin` rule directly: a solid maroon (#663333) fill, white uppercase Gotham label, and a near-flat 1px radius (approximated here to the `xs` token). A darker maroon hover (#83412c) was observed in CSS and is treated as the confirmed hover state.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g. "Learn More" links seen in copy), reusing the primary color as border/text on a white field so it pairs visually with the primary button without a second brand color.

**text-input** is a proposed pattern for the site search and any newsletter/email fields; no input styling was captured in evidence, so border, radius, and padding are inferred conventions using the muted hairline tone.

**nav-bar** proposes a white, top-anchored bar using Gotham for link labels (matching button-md sizing) since the page text lists a persistent primary nav (Products, Store Locator, Who We Are, etc.); exact spacing and scroll behavior are not observed.

**hero** models the homepage slider treatment literally described in CSS: an oversized Braisetto-Bold headline where a `span` portion shifts to the maroon primary color against the general yellow accent, producing the two-tone hero title style implied by `.Slider_section h1` and its nested `span`.

**product-card** is a proposed grid-tile pattern for listing crackers, cookies, and mixes, using a white card surface, medium radius, and the CooperMdBTWXX title face for product names with a smaller body face for ingredient callouts.

**recipe-card** is a category-appropriate component for the "Recipes" content observed in page text (e.g. "White Chili with Almond Flour Crackers," "Nice Cream"), using the soft yellow surface tone to visually separate editorial/recipe content from commerce content.

**badge** is proposed for the "Non-UPF Verified" and similar certification marks referenced prominently in page copy, using the brighter highlight yellow as a pill background with dark text for legibility, since no literal badge markup was supplied.

**search** and **footer** round out the set: search is a minimal, low-chrome input for product lookup; footer reuses the primary maroon as a dark band (a common pattern for brand sites with this palette) to host the long link list (Products, Who We Are, Recipes, Contact, Careers, Resources, Press, FAQ, legal links) enumerated in the page text, though the actual footer background color was not directly captured in the supplied CSS rules.

## Responsive Behavior

This is a recommended breakpoint approach, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <480px | Single-column stacks; hero headline typography scales down substantially from `display-xl`; nav collapses to a hamburger/off-canvas menu. |
| Tablet | 480–1024px | Two-column product/recipe grids; nav-bar may remain inline or collapse depending on link count. |
| Desktop | >1024px | Multi-column grids (3–4 up) for product-card and recipe-card; full inline nav-bar. |

Touch targets should be at least 44px in height for `button-primary`/`button-secondary` on mobile, exceeding the 34px line-height observed in desktop button CSS. Nav collapse and any sticky-header behavior are proposed, not confirmed by evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no rendered layout, JavaScript-driven interactions, or actual mobile breakpoints were observed.
- `muted`, `hairline`, `surface-soft`, and `surface-card` are inferred role assignments reusing supplied hex values that were not explicitly tied to those semantic purposes in the source CSS.
- `#ffd14100` (transparent yellow) is assumed to be a hover/transition overlay based on its alpha channel; its actual use case is unconfirmed.
- Body/paragraph typography (TT Norms Pro) is inferred from the global font-family list; no selector coupling a body text element to this font was supplied.
- All font sizes not explicitly present in the supplied CSS (body-md, body-sm, display-md, and all component paddings) are proposed defaults, not measurements.
- Border-radius on `.btn.callactoin` was observed as 1px; the `rounded` scale's `xs` (2px) is an approximation, not an exact match.
- Custom font availability, licensing, and web-font delivery (Braisetto-Bold, CooperMdBTWXX-Medium, Gotham A/B, TT Norms Pro) were not verified and may require licensing confirmation before production use.
- Footer, nav, and search components are structurally proposed based on link text present in page copy, not on any captured layout or styling for those regions.
