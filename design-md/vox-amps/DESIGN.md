---
version: alpha
name: "Vox Amps"
source_url: "https://www.voxamps.com"
captured_at: "2026-09-29T04:08:06.081130+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from voxamps.com, the current parent-hosted
  storefront for the VOX amplifier and cabinet line (AC30, AC15, AC10 Custom,
  Pathfinder, AC Mini, effects, and accessories). Confirmed CSS shows a dark
  charcoal button fill (#32373c, background-color observed on
  .wp-block-button__link and :root buttons) with white text and a fully
  rounded pill radius (border-radius:9999px). A cookie-consent panel exposes
  additional real values: link/accent blue #1863dc, ink #212121 for accordion
  headers, and a success-state green #008000. The remaining palette is the
  WordPress/WooCommerce editor preset set (grays from #eeeeee through
  #111111, plus scattered saturated swatches such as #a39164, #e0ae14, and
  #958e09) which is inferred rather than confirmed as intentional brand
  color; the brass/olive-gold tones are proposed as accent colors because
  they read consistently with VOX's traditional brass-and-black amp
  hardware, not because they were measured as UI accents. Typography relies
  on Avenir LT Roman for body copy and Helvetica Neue Condensed Bold for
  headings, both observed in font-family evidence, with Open Sans/Roboto as
  present fallbacks. Layout, hover, and mobile behavior are not observed and
  are proposed conventions only.

colors:
  primary: "#32373c"
  ink: "#212121"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#767676"
  hairline: "#cccccc"
  surface-soft: "#f4f4f4"
  surface-card: "#f6f6f6"
  on-primary: "#ffffff"
  accent-brass: "#a39164"
  accent-gold: "#e0ae14"
  link: "#1863dc"
  success: "#008000"
  border-strong: "#111111"
typography:
  display-xl: {fontFamily: "'Helvetica Neue LT W05_77 Bd Cn', 'Roboto Condensed', sans-serif", fontSize: 42px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Helvetica Neue LT W05_77 Bd Cn', 'Roboto Condensed', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Avenir LT W01_55 Roman1475520', 'Open Sans', sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Avenir LT W01_55 Roman1475520', 'Open Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Avenir LT W01_55 Roman1475520', 'Open Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Avenir LT W01_55 Roman1475520', 'Open Sans', sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-brass}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xs} {spacing.base}"
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** reflects the confirmed `.wp-block-button__link` rule: charcoal fill (`{colors.primary}`), white text, and a fully pill-shaped radius (`9999px`), matching the observed `border-radius` value. Used for "Shop", "Find a Dealer", and CTA buttons.

**button-secondary** is a proposed outline variant sharing the same pill geometry, for lower-emphasis actions like "View Details" on amp listing pages; hover/focus fill is not observed and is left undefined.

**text-input** is a proposed field style (rounded corners, hairline border) for the newsletter "Email" and "Country" form fields seen in the footer subscription block; no focus-ring color was captured in evidence.

**nav-bar** models the top utility row (search, social icons, SHOP/History/Artists/Support links) as a light bar with dark ink text; sticky behavior and mobile menu treatment are not observed.

**product-card** is inferred from the repeating amp-tile pattern in the excerpt (model name, wattage, speaker spec, e.g. "AC10 CUSTOM / 10W RMS / 1×10-INCH CELESTION VX10"); card surface uses `{colors.surface-card}` with a hairline border, sized for a responsive grid.

**hero** proposes a dark full-bleed band ("NOTHIN' LIKE A VOX! ★ Since 1957 ★") using the ink background and display typography; the slider/carousel mechanics ("Previous/Next") are referenced in the text but not measured.

**footer** groups AMPS/OTHER PRODUCTS/COMPANY/FOLLOW US columns plus the subscribe form on the dark ink background, consistent with typical multi-column site footers; exact column widths are proposed.

**badge** and **spec-badge** are category-appropriate additions for amp specs: badge uses the brass accent for promotional/"New" flags, while spec-badge is a neutral pill for wattage and speaker-size callouts (e.g. "10 WATTS RMS", "1×12\" CELESTION") drawn directly from the excerpt's product data pattern.

**search** models the "search / open search box" control referenced in the header text as a rounded, muted-background field; no expand/collapse animation was observed.

## Responsive Behavior
| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | <600px | Single-column product grid; nav collapses to hamburger/off-canvas menu (not observed) |
| Tablet | 600–1024px | 2-column product grid; footer columns stack to 2-across |
| Desktop | >1024px | 3–4 column product grid; full horizontal nav and multi-column footer |

Touch targets should be at least 44×44px for buttons and nav items. This table and all collapse/stacking behavior are recommendations only; no live responsive layout, hover state, or breakpoint was captured from the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is static CSS/text extraction; no rendered layout, hover, focus, or animation states were observed.
- Most of the supplied palette originates from WordPress/WooCommerce editor presets rather than confirmed brand UI usage; brass/gold accent roles are inferred from thematic fit, not measured application.
- Only `#32373c` (button fill), `#1863dc` (cookie-banner link), `#212121` (accordion text), and `#008000` (status green) are directly tied to a rendering rule in the supplied CSS; all other role assignments are inferred.
- Font sizes beyond the confirmed `16px`/`42px` presets are proposed, not measured.
- Custom font family availability, licensing, and actual `@font-face` sources (Avenir LT, Helvetica Neue Condensed) were not verified.
- Mobile navigation, carousel mechanics, and product-grid responsiveness are not observed and are proposed conventions only.
