---
version: alpha
name: "DeWit"
source_url: "https://www.dewit.eu/"
captured_at: "2026-09-29T03:59:00.184743+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from DeWit's public stylesheet, which sets a
  root type color of #161f24 on a white canvas, with Montserrat as the sole
  confirmed text typeface (body and headings both declare
  font-family: montserrat, sans-serif). A muted gold, #b7a361, appears as an
  interactive/hover accent on link borders and an SVG close-icon fill,
  suggesting its role as the brand's primary accent rather than a workhorse
  UI color. Several Bootstrap utility hues are present (#0d6efd, #28a745,
  #db001b, #dee2e6, #6c757d, #f3f3f3) and are mapped here to conventional
  system roles (link/info, success, danger, hairline, muted text, soft
  surface) since no brand-specific usage was evidenced beyond framework
  defaults. #007aff is the Swiper carousel theme variable and is kept as a
  distinct interactive accent rather than merged with the primary gold.
  Grays (#aaaaaa, #b8b9ba, #333333, #000000) and a pale pink (#fcbcc6) are
  retained as supporting neutrals/accents with inferred, non-critical roles.
  Layout metrics (breakpoints, spacing scale, radii) are proposed
  conventions for a tools/hardware storefront, not measured from rendered
  pages, and are labeled accordingly throughout.

colors:
  primary: "#b7a361"
  ink: "#161f24"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-info: "#0d6efd"
  accent-interactive: "#007aff"
  success: "#28a745"
  danger: "#db001b"
  gray-mid: "#aaaaaa"
  gray-light: "#b8b9ba"
  blush: "#fcbcc6"
  black: "#000000"
typography:
  display-xl: {fontFamily: "montserrat, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.5px}
  display-md: {fontFamily: "montserrat, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "montserrat, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "montserrat, sans-serif", fontSize: 18px, fontWeight: 500, lineHeight: 2, letterSpacing: 0px}
  body-sm: {fontFamily: "montserrat, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "montserrat, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "montserrat, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.gray-light}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  tool-spec-panel:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-sm}"

## Components
- **button-primary**: A solid gold call-to-action button (e.g. "Offerte aanvragen") using the observed #b7a361 accent as background with white text; proposed as the main conversion element, hover/active states not observed.
- **button-secondary**: A white/outline button variant for lower-emphasis actions, bordered in the Bootstrap hairline gray; proposed pairing with button-primary in forms and toolbars.
- **text-input**: A bordered form field using the hairline border color and body text color, sized for filters/search/contact forms; focus-ring color not observed and left as proposed.
- **nav-bar**: A white top navigation bar with dark ink text and gold hover underlines, matching the `.list--sites li a` hover-to-gold pattern found in the CSS; mobile collapse behavior not observed.
- **product-card**: A white card with a thin hairline border for tool listings (spades, rakes, trowels), pairing a title-md heading with body-sm descriptive copy; spacing and imagery ratio are proposed, not measured.
- **hero**: A dark, full-width introductory band using the ink color as background and large display-xl Montserrat type for the brand statement ("DeWit, een begrip in gereedschap"); actual hero imagery/overlay not observed.
- **footer**: A dark footer band echoing the ink background, with muted gray link text turning gold on hover, consistent with `.list--sites` hover styling; column layout is proposed.
- **badge**: A small pill using the soft surface gray, suited to tags like "sinds 1898" or material/category labels; not directly observed in supplied markup.
- **search**: A minimal search field consistent with `.header__search` padding rules, styled as a borderless-to-bordered input on focus; icon and expand animation are proposed.
- **tool-spec-panel**: A category-appropriate component for gardening-tool detail specs (material, length, handle type) using the soft surface background and caption/body-sm pairing; entirely proposed for this product category, not observed in the supplied evidence.

## Responsive Behavior
Recommended breakpoints (not measured from the live site): `xs <576px`, `sm ≥576px`, `md ≥768px`, `lg ≥992px`, `xl ≥1200px`, `xxl ≥1400px`, mirroring the Bootstrap variables found in `:root`. Nav collapses to a hamburger/off-canvas pattern below `md`; product-card grids proposed as 1-column (xs), 2-column (sm/md), 3–4 column (lg+). Touch targets should be at least 44×44px for buttons and nav links. This is a design recommendation only; no actual responsive/mobile layout was observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS and text extraction only; no rendered layout, interaction states (hover/focus/active), or mobile behavior were observed. Semantic color roles (muted, hairline, surface-soft/card, danger/success/info) are inferred from conventional Bootstrap variable naming, not confirmed brand usage. Typography sizes beyond the observed h1 rule (2.6667rem/3.2222rem at an 18px root) are proposed estimates. The `montserrat-alternates` family appeared in the font list but was not tied to any selector in the supplied CSS, so it was excluded from typography tokens in favor of the confirmed `montserrat` family. Font licensing/self-hosting details were not verified. Spacing scale and border-radius values are conventional proposals, not measured from the site.
