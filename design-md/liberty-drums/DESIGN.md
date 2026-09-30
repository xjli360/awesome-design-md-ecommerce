---
version: alpha
name: "Liberty Drums"
source_url: "https://www.libertydrums.com"
captured_at: "2026-09-29T03:54:19.531599+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Liberty Drums presents as a dark-on-white, craft-forward storefront for a UK
  boutique drum manufacturer. The confirmed CSS shows a near-black ink
  (#1a1a1a) used for headings, primary buttons and link color, with a pure
  black (#000000) hover state on buttons, sitting on a white canvas
  (#ffffff). Body copy runs in Open Sans/Helvetica-family sans-serif at 15px,
  color #666666, line-height 1.6 — a legible, unfussy pairing appropriate to
  a workshop-and-catalog site. Headings use Ubuntu (with Helvetica Neue
  fallback) at font-weight 400 with a wide 0.05em letter-spacing, giving
  titles a slightly spaced, engraved-plate feel that suits a handcrafted
  instrument brand.
  Accent colors are inferred from a currency-switcher control: a warm red
  (#de4c39) for selected/sale states and a muted green (#89b171) with a pale
  green background (#ddf6cf) for hover/success states — both are reused here
  for sale badges and interactive-selection affordances (e.g. a kit-builder
  wood/finish selector), since no dedicated e-commerce component CSS was
  supplied. Neutral grays (#f9f9f9, #f5f5f5, #dadada, #9a9a9a) are used for
  soft surfaces, card backgrounds, hairlines and muted text. Rounded corners
  are conservative (2px on buttons), consistent with a restrained, craft
  aesthetic rather than a rounded, playful one. All semantic role
  assignments beyond the two directly-styled components (.btn,
  currency-switcher) are inferred and flagged accordingly.

colors:
  primary: "#1a1a1a"
  ink: "#1a1a1a"
  ink-deep: "#000000"
  canvas: "#ffffff"
  body: "#666666"
  muted: "#9a9a9a"
  hairline: "#dadada"
  surface-soft: "#f9f9f9"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  accent: "#de4c39"
  accent-positive: "#89b171"
  accent-positive-bg: "#ddf6cf"
typography:
  display-xl: {fontFamily: "Ubuntu, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.05em}
  display-md: {fontFamily: "Ubuntu, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.05em}
  title-md: {fontFamily: "Ubuntu, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.05em}
  body-md: {fontFamily: "Open Sans, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0em}
  body-sm: {fontFamily: "Open Sans, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0em}
  caption: {fontFamily: "Open Sans, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.02em}
  button-md: {fontFamily: "Ubuntu, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1, letterSpacing: 0.05em}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    typography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  kit-builder-selector:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** maps directly to the observed `.btn` rule: near-black (#1a1a1a) fill, white text, 2px radius, Ubuntu button typography with 0.05em tracking, and a darker-black (#000000) hover/focus state confirmed in CSS. This is the highest-confidence component in the set.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g. "View all Snares"), reusing the hairline border color and canvas background seen in the currency-switcher's unselected state; its hover treatment is proposed, not confirmed for this specific variant.

**text-input** is inferred for the newsletter/search fields visible in page text ("Email address," "Search"). Border, radius and padding are proposed from the general hairline/xs-radius pattern established by the button and currency-switcher rules.

**nav-bar** is inferred from the multi-level menu structure in the text excerpt (Drum Kits, Snares, Kit Builder, Accessories, etc.) but no nav-specific CSS was supplied; background, ink text and hairline divider are proposed defaults consistent with the light theme.

**product-card** is proposed for kit/snare listing tiles (e.g. "5-Piece Artist Birch Kit," price + sale strike-through). Surface-card gray and hairline border are proposed to differentiate cards from the white page background; no card CSS was directly observed.

**hero** is inferred for the homepage intro ("UK'S LARGEST BOUTIQUE DRUM MANUFACTURER"), using the display-xl heading style with generous section spacing; exact hero layout and imagery were not present in the supplied evidence.

**footer** reflects the link list of policy/social pages in the text (Privacy Policy, Terms, social icons). Surface-soft background and muted text are proposed for visual separation from the main content; no footer-specific selector was supplied.

**badge** directly reuses the confirmed `.currency-switcher-btn.selected` red (#de4c39) as the basis for a "Sale" price-tag component, matching the "Regular price … now … Sale" pattern seen in product listings.

**search** is a proposed pill-shaped input reflecting the rounded, pill-style currency buttons already observed (border-radius 25px in source, generalized here to the `full` token); actual search-bar markup was not in evidence.

**kit-builder-selector** is a category-specific component proposed for the site's "Kit Builder" custom-wood/finish tool. It reuses the accent-positive hover pair (#ddf6cf background / #89b171 border) confirmed on the currency switcher, applied here to a wood/finish swatch-selection state — this mapping is inferred by analogy, not directly observed on the builder itself.

## Responsive Behavior

Recommended breakpoints (not measured from live site):

| Range | Target |
|---|---|
| < 480px | Mobile: single-column, collapsed nav |
| 481–768px | Tablet: 2-column product grids |
| 769–1024px | Small desktop: 3-column grids, inline nav |
| 1025px+ | Desktop: full multi-column layout |

Touch targets should be at least 44×44px for buttons and nav items. The page text includes "Close menu" and "Back to site navigation," suggesting a collapsible/drawer mobile menu pattern exists, but its exact behavior, animation and breakpoint were not observed and are inferred solely from copy content. This section is a recommendation only, not a measured description of site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction; no rendered layout, computed styles, or DOM structure was observed.
- Only two selectors (`.btn` and `.layered-currency-switcher`) had substantive styling; all other component definitions (nav, card, hero, footer, search, input) are inferred/proposed and not directly verified.
- Several palette entries (#3cb0fd, #3498db, #cb2027, #1990c6, #dd4b39, #00aced, #3b5998) resemble common framework/social-icon defaults and were excluded from role assignment as their brand relevance is unclear.
- Typography sizes beyond the observed 15px body and 16px button text are proposed, not measured.
- Mobile/responsive behavior, hover/active/focus states beyond `.btn`, and interaction patterns were not observed and are labeled proposed.
- Font licensing/availability for Ubuntu and Open Sans as used in production was not verified; generic sans-serif fallbacks are assumed safe.
