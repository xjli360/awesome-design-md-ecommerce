---
version: alpha
name: "Peet's"
source_url: "https://peets.com"
captured_at: "2026-09-28T05:00:14.719301+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Peet's public site evidence shows a warm, roast-driven palette built on a
  single dominant gold-brown (#937031, with a near-identical #927036
  variant appearing across buttons and hover states) layered over deep
  coffee browns (#704f2e, #4d331a, #31251b) and warm off-white surfaces
  (#f7f6f1, #f6f5f1, #fdfbf8). Body copy runs in near-black (#000000,
  #222222) on white (#ffffff), with #767676 and #dcdcdc doing quiet work
  as muted text and hairlines. A blue (#3366cc) and a red (#b51b1b) appear
  in the palette and are treated here as inferred link and alert colors,
  since no rule confirmed their role. Two font families are observed:
  DIN Condensed (a tall, condensed grotesk) for display and heading
  moments, and Proxima Nova for body copy, navigation, and buttons —
  matching the CTA button rule's 13px/600 weight. This interpretation
  leans into the brand's "craft coffee since 1966" positioning: condensed
  display type for confident headlines, warm neutral surfaces for
  product/editorial cards, and the gold-brown as the single consistent
  action color across primary buttons, hover underlines, and badges.
  Card and footer surface roles are inferred from the neutral/dark browns
  present in the palette, not from confirmed layout screenshots.

colors:
  primary: "#937031"
  secondary: "#704f2e"
  accent: "#b9975b"
  ink: "#000000"
  body: "#222222"
  muted: "#767676"
  hairline: "#dcdcdc"
  canvas: "#ffffff"
  surface-soft: "#f7f6f1"
  surface-card: "#fdfbf8"
  surface-deep: "#31251b"
  on-primary: "#ffffff"
  link: "#3366cc"
  alert: "#b51b1b"
  scrim: "#00000080"
typography:
  display-xl: {fontFamily: "'DIN Condensed', sans-serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "'DIN Condensed', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Proxima Nova', sans-serif", fontSize: 21px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'Proxima Nova', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Proxima Nova', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "'Proxima Nova', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Proxima Nova', sans-serif", fontSize: 13px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hoverColor: "{colors.primary}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.surface-deep}"
    overlayColor: "{colors.scrim}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
  footer:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.surface-deep}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  subscription-toggle:
    backgroundColor: "{colors.surface-soft}"
    activeColor: "{colors.primary}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
---

## Components

**button-primary** reflects the observed nav-tout and promo CTA rule (white text, gold-brown #937031 background, 13px/600 weight), used for primary shop/subscribe actions.

**button-secondary** mirrors the hero CTA rule that inverts to a white background with brown (#927036) text; proposed for secondary hero and promo-slot actions where the primary button already carries the fill.

**text-input** is a proposed pattern for account/newsletter fields — white background, hairline border, body-md type — since no dedicated input CSS was supplied.

**nav-bar** is grounded in `#header .header__link-wrap .header__link`: white canvas, black 16px/400 text, with the gold-brown hover and underline (`::before` background) confirmed by the evidence.

**product-card** is inferred for the coffee/bundle grid (Major Dickason's, Big Bang®, etc.): off-white card surface, condensed title, body-md price line, generous internal padding — layout not directly observed, proposed for grid consistency.

**hero** proposes a dark, image-backed banner (surface-deep background, scrim overlay, white display-xl headline) matching the homepage's large promotional hero copy pattern in the text excerpt, though exact hero markup/CSS was not supplied.

**footer** is proposed using the darkest brown in the palette as background with white text and accent-colored links, consistent with the brand's coffee-dark visual language; no footer selectors were in evidence.

**badge** is a proposed small pill (e.g., "Limited Release," roast-level tags) using the mid-tone accent gold with dark text, sized at caption scale.

**search** is proposed from the "Header Search" UI referenced in the text excerpt: canvas background, hairline border, body-md input text; exact search-field CSS was not supplied.

**subscription-toggle** is a category-appropriate proposed component for "Subscribe & Save" frequency/quantity selection, using the soft surface as an inactive track and primary gold as the active state — not confirmed by supplied CSS.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Nav | Grid |
|---|---|---|---|
| Mobile | <768px | Collapsed hamburger menu (21px/700 links per observed mobile nav rule) | 1 column |
| Tablet | 768–1023px | Condensed horizontal nav | 2 columns |
| Desktop | ≥1024px | Full mega-menu | 3–4 columns |

Touch targets should be at least 44px tall; the mobile nav's 21px/700 link size suggests generous tap padding is already intended. Search and cart icons should collapse to icon-only affordances below tablet width. All values are proposed, not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, hover/focus states, or animation timing was observed. Semantic color roles (canvas vs. surface-soft vs. surface-card, ink vs. body) are inferred from neutral-tone proximity in the palette, not from confirmed usage. The blue (#3366cc) and red (#b51b1b) are assumed link/alert colors but have no confirming selector. Typography sizes beyond the 16px nav link, 13px/600 button, and 21px/700 mobile nav link are proposed for scale consistency, not measured. Component states (focus, disabled, active toggle) are proposed and unverified. Font availability, licensing, and exact weights for DIN Condensed and Proxima Nova were not verified and should be confirmed against Peet's licensed font files before implementation.
