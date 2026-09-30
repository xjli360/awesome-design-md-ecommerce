---
version: alpha
name: "Zesty Paws"
source_url: "https://zestypaws.com"
captured_at: "2026-09-28T04:19:22.782364+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Zesty Paws presents as a warm, approachable supplement brand built on a white
  canvas (#ffffff) with dark charcoal text (#383838, matching the observed
  sticky header's text/background tokens). The dominant accent across the
  supplied palette is a confident orange (#ec7700, with #fe8000 and #ffb600 as
  tonal siblings), which is inferred here as the primary action color given its
  repetition and contrast against white. A deep navy (#29387e) appears as a
  secondary/trust color, while muted warm tints (#fdefe0, #fbefe2, #f3f3f3)
  suggest soft section backgrounds and card surfaces. Small saturated hues
  (#217b37 green, #de2a2a red, #40918d teal, #bd5e96 pink) are treated as
  semantic or category-tag colors rather than core brand colors, since their
  usage context was not confirmed.
  Typography pairs a serif/typewriter display face ("American Typewriter" with
  monospace fallbacks) for headings against a humanist sans ("motiva-sans",
  Arial, sans-serif) for body and UI text — an observed pairing from the theme
  CSS. Heading sizes (48–60px H1, 36–48px H2) and 52px control heights (buttons,
  inputs) are taken directly from the CSS custom properties. Rounded corners,
  spacing scale, and component states below are proposed interpretations, not
  measured visual observations.

colors:
  primary: "#ec7700"
  primary-strong: "#ce4a22"
  secondary: "#29387e"
  ink: "#383838"
  canvas: "#ffffff"
  body: "#383838"
  muted: "#757575"
  hairline: "#dedede"
  surface-soft: "#fdefe0"
  surface-card: "#f3f3f3"
  surface-alt: "#f6f6f6"
  on-primary: "#ffffff"
  success: "#217b37"
  warning: "#f7be00"
  error: "#de2a2a"
  accent-teal: "#40918d"
  accent-pink: "#bd5e96"
typography:
  display-xl: {fontFamily: "'American Typewriter', Menlo, Consolas, Monaco, monospace", fontSize: 60px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'American Typewriter', Menlo, Consolas, Monaco, monospace", fontSize: 36px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "'American Typewriter', Menlo, Consolas, Monaco, monospace", fontSize: 22px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "'motiva-sans', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'motiva-sans', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'motiva-sans', Arial, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "'motiva-sans', Arial, sans-serif", fontSize: 13px, fontWeight: 700, lineHeight: 52px, letterSpacing: 1.5px, textTransform: uppercase}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: "52px"
    padding: "0 {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    position: "sticky-top"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-alt}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: "52px"
  supplement-fact-callout:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.caption}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** — The core call-to-action treatment, using the observed orange accent (#ec7700) against white text, uppercase lettering, and the 52px control height defined in the theme's `--button-height` variable. Hover/active darkening is proposed, not observed.

**button-secondary** — An outline variant for lower-emphasis actions (e.g., "Learn More"), sharing the same 52px height and radius as primary but with a hairline border and ink-colored text. State transitions are proposed.

**text-input** — Modeled directly on the theme's `.input__field` rule: 52px height, subtle hairline border, and a focus state (proposed here as a solid ink-colored ring) matching the CSS's documented `box-shadow: 0 0 0 1px` focus pattern.

**nav-bar** — A sticky white header (confirmed via `--enable-sticky-header: 1` and header background/text/border variables) housing logo, navigation links, and cart/search icons. Mobile collapse into a hamburger menu is proposed, not observed.

**product-card** — Represents individual supplement SKUs in listing grids; uses a soft neutral card surface (#f3f3f3), rounded corners, and a title/price hierarchy pulling from the heading and body type scales. Hover elevation and quick-add controls are proposed.

**hero** — A full-width introductory banner using the warm cream surface tint (#fdefe0) as an inferred section background, paired with the large display heading size (48–60px per breakpoint) and a primary button. Imagery treatment is not observed.

**footer** — Proposed as a navy-toned closing section (#29387e) with white text for contrast, housing newsletter signup, links, and legal text at smaller body sizes. This color role is inferred from the palette, not confirmed via extracted footer-specific CSS.

**badge** — A small pill label (proposed) for tags like "Best Seller" or "Vet Recommended," using the warm yellow (#f7be00) fill common in supplement/CPG merchandising patterns; exact usage on-site was not confirmed.

**search** — A lightweight input variant sharing the input field's height and radius tokens but sitting on a soft neutral background (#f6f6f6) for header/overlay contexts. Proposed only.

**supplement-fact-callout** — A category-specific component for surfacing key ingredient or dosage information on product pages, using a bordered card with an orange accent rule and compact caption/body typography. This pattern is proposed to fit a pet-supplement product page's informational needs; no direct CSS evidence for this exact component was supplied.

## Responsive Behavior

Proposed breakpoints (not measured from live site rendering):

| Breakpoint | Width | Grid/Layout Notes |
|---|---|---|
| Mobile | < 600px | Single-column stacking; nav collapses to hamburger; hero padding reduces to `{spacing.xl}` |
| Tablet | 600–1024px | 2–3 column product grids; `--vertical-breather` steps toward 64–80px per observed root tokens |
| Desktop | 1024–1440px | Full 20-column grid (per `--grid-column-count: 20`); `--vertical-breather` up to 90px |
| Wide | > 1440px | Container gutter fixed at `--container-gutter: 40px`; content max-width capped, extra space as margin |

Touch targets should meet a 44px minimum; the observed 52px button/input height already satisfies this. Navigation and filter panels on mobile are recommended to collapse into drawers/accordions — this is a UX recommendation, not an observed mobile interaction.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted from static CSS/HTML sources only; no rendered layout, hover states, animations, or JavaScript-driven interactions were observed.
- Semantic color roles (primary vs. secondary vs. category-tag colors) are inferred from frequency and contrast, not from confirmed component usage in context.
- Rounded-corner and spacing scales follow a proposed standard system rather than values directly measured from the site's border-radius or margin CSS.
- Mobile menu behavior, cart drawer, and product-page interactions were not observed and are proposed based on common e-commerce patterns.
- "American Typewriter" and "motiva-sans" are used as declared in CSS `font-family` stacks; their licensing, actual availability, and fallback rendering on end-user devices were not verified.
- Exact hex-to-role mapping for footer and badge backgrounds is a design proposal reusing supplied palette colors, not a confirmed extraction from footer/badge-specific selectors.
