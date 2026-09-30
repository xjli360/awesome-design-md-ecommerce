---
version: alpha
name: "Carr Amps"
source_url: "https://www.carramps.com"
captured_at: "2026-09-28T05:07:37.141489+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Carr Amps sells hand-built tube guitar amplifiers and cabinets, and the
  supplied evidence is dominated by two signal groups: a small set of neutral
  UI colors (#222222, #ffffff, #000000, and their 40%-opacity variants) and a
  long tail of saturated hex values that match common third-party social-icon
  brand colors (Facebook blue, Instagram pink/red, YouTube red, Twitter blue,
  etc.). Those social-brand colors are treated here strictly as icon-badge
  references, not as site palette, since their presence does not prove a
  page-design role. The one non-neutral, non-social hex worth promoting is
  #382110, a dark leather/wood brown that plausibly echoes amp tolex and
  cabinet materials; it is used here as the inferred primary/brand color.
  #00b4b3, a teal not matching any recognizable third-party brand, is kept as
  a secondary accent for interactive highlights, also inferred. Typography
  observed is Oswald (condensed, bold-leaning) paired with Ubuntu (humanist
  sans), a fitting combination for a vintage-tinged, craft-amplifier brand:
  Oswald for confident display type, Ubuntu for readable body copy. All
  spacing, radii, and component states below are proposed conventions, not
  measured site behavior.

colors:
  primary: "#382110"
  ink: "#222222"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#22222266"
  hairline: "#00000066"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#00b4b3"
  accent-teal-soft: "#00b4b366"
  overlay-black: "#00000066"
  overlay-transparent: "#00000000"
typography:
  display-xl: {fontFamily: "Oswald, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Oswald, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Oswald, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Ubuntu, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Ubuntu, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Ubuntu, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Oswald, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 1px}
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    overlay: "{colors.overlay-black}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  swatch-selector:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    itemRounded: "{rounded.full}"
    padding: "{spacing.base}"
    labelTypography: "{typography.caption}"

## Components

**button-primary** — A brown-filled call-to-action (e.g., "LEARN MORE" on the Trail Rider hero) using the inferred `primary` leather/tolex tone with white text in condensed Oswald caps. Hover/focus states are proposed, not observed.

**button-secondary** — An outlined variant for lower-emphasis actions (e.g., "Find a Dealer") sharing the same type treatment but with a transparent fill, so it recedes against the brown primary button.

**text-input** — A light, hairline-bordered field for forms such as "Register Your Amp" or dealer/warranty submissions. Padding and radius are proposed conventions since no form CSS was supplied.

**nav-bar** — A white top bar carrying ABOUT / PRODUCTS / KNOWLEDGE BASE / CONTACT links plus a mobile Open/Close Menu toggle referenced in the page text. Desktop vs. mobile menu behavior is inferred from the "Skip to Content" and menu-toggle text, not from measured layout.

**product-card** — A card for each amp model (Trail Rider, Skylark, Special, Bel-Ray, Super Bee, etc.) pairing a condensed Oswald model-name title with Ubuntu body copy for specs, on a white card with a hairline border. Grid arrangement is proposed.

**hero** — A dark, full-bleed slide (the site references a multi-slide carousel: "Slide 1"–"Slide 6") using ink as background with white display type, suited to product photography and the Trail Rider announcement copy. Slide transition/interaction behavior is not observed.

**footer** — A dark closing band holding contact details (phone, email), legal links (Terms, Privacy), and social follow links (Instagram/YouTube/Facebook). Social icon colors from the supplied palette are treated as fixed third-party brand marks rather than site-theme colors.

**badge** — A small teal pill for short labels (e.g., "New," a swatch tag, or a knowledge-base flag), using the one non-neutral accent not attributable to a recognized outside brand.

**swatch-selector** — Category-appropriate component for the site's "Color Swatches" knowledge-base page: a bordered panel of round tolex/cabinet-color chips with a caption label beneath each, letting a visitor preview finish options. Selection/active states are proposed.

## Responsive Behavior

Recommended breakpoints (not measured):

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–599px | Single-column stack; nav collapses to Open/Close Menu toggle as referenced in page text |
| tablet | 600–1023px | Two-column product grid; nav may remain collapsed |
| desktop | 1024px+ | Full horizontal nav; multi-column product grid; hero at full width |

Touch targets should be at least 44×44px for nav toggle, buttons, and swatch chips. The folder-style submenu structure implied by "Folder: PRODUCTS / Back" text suggests an accordion or drill-down pattern on mobile; this is inferred from copy only, not from observed interaction or CSS media queries.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- No CSS rules were supplied (`css_rules` was empty), so all spacing, radii, breakpoints, and component states are proposed conventions, not extracted values.
- The large supplied color list is mostly recognizable third-party social-icon brand colors (Facebook, Instagram, YouTube, Twitter, etc.); these were excluded from the brand palette and are not guaranteed to appear anywhere in the site's own UI chrome.
- `#382110` (primary) and `#00b4b3` (accent-teal) are inferred as brand-relevant because they don't match known third-party marks, but their actual UI role (button, link, background) is unconfirmed.
- Font weights, exact sizes, and letter-spacing for Oswald/Ubuntu are proposed; only the family names were observed.
- No mobile menu, carousel, or hover/focus interaction was directly observed — behavior above is inferred from page text (e.g., "Open Menu Close Menu," "Slide 1... (current slide)").
- Licensing/self-hosting status of Oswald and Ubuntu (both are open-source Google Fonts in common usage) was not verified against this site's actual font-loading method.
- Component layout (grid columns, card sizing, hero dimensions) is proposed based on typical amp-brand e-commerce patterns, not measured page geometry.
