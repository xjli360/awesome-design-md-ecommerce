---
version: alpha
name: "Pehr"
source_url: "https://pehr.com"
captured_at: "2026-09-28T10:17:22.311015+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Pehr's storefront CSS shows a restrained, black-and-white foundation layered
  with a single recurring sage-teal tone. Solid buttons and outline-button
  labels are driven by `--wk-color-accent-1`/`--wk-color-outline-button-label`,
  both set to pure black (rgb 0,0,0) against a white background, with
  `--wk-button-border-radius: 0px` and `--wk-input-border-radius: 0px`,
  indicating squared-off, unrounded UI controls. A secondary sage tone
  (`#5a7c7d`, with close variants `#5c7a7e`, `#597c7c`, `#4a6a6a`) recurs
  across the Judge.me review-widget variables (primary color, star color,
  write-review button, reviewer-name color) strongly enough to treat it as
  an intentional brand accent rather than incidental widget styling; this
  role is **inferred**, not confirmed as the primary brand hue. Typography
  pairs a thin serif display face, `Quincy Thin`, for headings with a
  humanist sans, `Brown Regular` (plus `Brown Bold` and `Brown Light`
  weights), for body and UI text — a soft/organic-meets-editorial pairing
  fitting for organic baby goods. Neutral grays (`#333333`, `#68696d`,
  `#dddddd`, `#f5f5f5`) round out surfaces and hairlines. A warm gold
  (`#ab8c52`) and a red (`#c8102e`) appear in the palette and are proposed
  here for accent/sale badge use, as their functional role could not be
  confirmed from static CSS alone. Observed `--hover-lift-amount: 4px` and
  `--hover-scale-amount: 1.03` tokens inform proposed card hover treatments.

colors:
  primary: "#000000"
  accent: "#5a7c7d"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#68696d"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  gold: "#ab8c52"
  sale: "#c8102e"
  alert-yellow: "#fbcd0a"
typography:
  display-xl: {fontFamily: "'Quincy Thin', serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Quincy Thin', serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Brown Bold', sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Brown Regular', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Brown Regular', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Brown Light', sans-serif", fontSize: 12px, fontWeight: 300, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "'Brown Bold', sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    submenuBackground: "{colors.canvas}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    resultTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  variant-swatch:
    backgroundColor: "{colors.surface-soft}"
    activeBorderColor: "{colors.ink}"
    inactiveBorderColor: "{colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** reflects the observed `--wk-color-accent-1: 0,0,0` and `--wk-button-border-radius: 0px` variables directly: a solid black, square-cornered call-to-action with white label text, sized against the observed `--wk-button-min-height: 45px`. This would drive "Add to Cart," "Shop Now," and checkout actions.

**button-secondary** is a proposed outline variant mirroring `--wk-color-outline-button-label: 0,0,0` — black text and border on a transparent field, for lower-emphasis actions like "View Details" or filter toggles. Hover/pressed states are not observed and are proposed only.

**text-input** uses the observed `--wk-input-min-height: 45px`, `--wk-input-border-width: 1px`, and `--wk-input-border-radius: 0px` to define a flush-bordered field for email capture, search, and account forms. Focus-state color is not observed and is proposed as a subtle border darkening.

**nav-bar** is inferred from the extensive mega-menu category text (New, Baby, Toddler, Footwear, On The Go, Nursery, Gifts & Sets, Sale) and the `--color-submenu: rgb(255 255 255 / 1.0)` variable, implying a white dropdown submenu layered over a white or transparent header bar. Sticky behavior is proposed, not confirmed.

**product-card** proposes a white card with a hairline border and serif-adjacent title styling, since no explicit card CSS was supplied; the observed `--hover-lift-amount: 4px` / `--hover-scale-amount: 1.03` tokens (with `.25s ease-out` transition) are applied here as a proposed hover lift/zoom, though their live application to product tiles was not confirmed in the evidence.

**hero** is a proposed full-width banner pattern using the `Quincy Thin` display face for an editorial, softly-serif headline over a light neutral background, paired with a single primary CTA — consistent with a lifestyle-led nursery/apparel brand, but not a directly observed layout.

**footer** is proposed as a dark (black) full-width band with white text and multi-column navigation echoing the header's category depth, appropriate for a large SKU catalog; this inverts the otherwise light palette and is not confirmed from supplied evidence.

**badge** covers sale/markdown flagging, using the observed red (`#c8102e`) for a "Sale" or "New" tag; alternate use of the observed yellow (`#fbcd0a`) for a promotional banner (e.g., the "Free Shipping on Orders Over $90 USD" strip text) is plausible but unconfirmed.

**search** proposes a predictive-search overlay with white background, hairline divider rows, and small-caption result typography, matching the site's flush, unrounded input aesthetic.

**variant-swatch** is the category-appropriate component: given Pehr's apparel sizing (Newborn through 8Y) and print/collection naming (Corduroy, Gingham, Wildflower, High Seas), a pill-style swatch selector is proposed for both size chips and fabric/print selection on product pages, using the ink border for the active state.

## Responsive Behavior

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | < 480px | Single-column nav collapses to hamburger; mega-menu becomes accordion |
| Small tablet | 480–767px | 2-column product grid |
| Tablet | 768–1023px | 3-column product grid; nav shows top-level categories only |
| Desktop | 1024–1439px | Full mega-menu with submenu columns; 4-column product grid |
| Wide | ≥ 1440px | Increased gutter/margin, max content width applied |

Touch targets should meet a minimum 44×44px hit area, consistent with the observed `--wk-button-min-height: 45px`. Header mega-menu collapse to an off-canvas or accordion pattern on mobile is a recommendation based on the size of the supplied navigation taxonomy, not a measured behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is derived solely from static CSS variables, color values, font-family declarations, and page text supplied as evidence; no live rendering, computed layout, or DOM screenshots were available. The "primary vs. accent" color split (black button system vs. sage-teal review-widget tone) is an inferred semantic separation, not a confirmed brand hierarchy. All typography sizes, line-heights, and letter-spacing values beyond the two confirmed font-family/weight/style variables are proposed, not measured. Component states (hover, focus, active, disabled) are proposed conventions except where an explicit CSS custom property (`--hover-lift-amount`, `--hover-scale-amount`, transition durations) was present, and even those were not confirmed as applied to any specific rendered component. Mobile menu behavior, breakpoint pixel values, and grid column counts are recommendations only. Availability, licensing, and web-font delivery of `Quincy Thin`, `Brown Regular/Bold/Light` are unverified proprietary font names found in CSS and should be confirmed with Pehr/foundry licensing before implementation; generic serif/sans-serif fallbacks are specified accordingly.
