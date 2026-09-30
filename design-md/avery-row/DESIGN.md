---
version: alpha
name: "Avery Row"
source_url: "https://avery-row.com"
captured_at: "2026-09-29T03:58:51.437287+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Avery Row's storefront CSS evidence shows a warm, neutral palette dominated by soft creams
  (#fcf7f1, #faf7f1, #f4eee1, #f1ebdd) paired with near-black ink tones (#212121, #262626,
  #19191e) and mid-grey body copy (#4d4d4d, #575756, #878787). This reads as a calm, editorial
  nursery-goods aesthetic rather than a saturated retail one. Two custom font stacks are
  declared at the root: --font-01 ('ar-larkin', serif) for headings and --font-02
  ('ar-helvetica', sans-serif) for body, nav, and buttons; additional families (Bodoni, Cardo,
  Roundhand, cursive) appear in the raw font list but their usage context is not confirmed by
  the supplied rules, so any script/serif accent role below is marked inferred. A small set of
  saturated colors (#29845a green, #ed6e41 terracotta, #af7b88 dusty rose) appear only once or
  twice in the evidence and are treated as inferred accent/badge colors rather than confirmed
  brand primaries, consistent with the site's "sustainable," "organic cotton" messaging. Button
  styling borrowed from the reviews widget (uppercase, 700 weight, 0.1em letter-spacing, 0
  border-radius) is reused here as the general button pattern since no separate site-button CSS
  was supplied. Layout, spacing, and breakpoints are proposed, not measured.

colors:
  primary: "#29845a"
  ink: "#212121"
  canvas: "#fcf7f1"
  body: "#4d4d4d"
  muted: "#878787"
  hairline: "#d9d9d9"
  surface-soft: "#f4eee1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-terracotta: "#ed6e41"
  accent-rose: "#af7b88"
  focus: "#005bd3"
  success-bg: "#cdfee1"
  warning-bg: "#fff8db"
  error: "#721c24"
  error-bg: "#f8d7da"
typography:
  display-xl: {fontFamily: "'ar-larkin', serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'ar-larkin', serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'ar-larkin', serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "'ar-helvetica', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'ar-helvetica', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'ar-helvetica', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.1px}
  button-md: {fontFamily: "'ar-helvetica', sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.1em}
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.focus}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    mutedTextColor: "{colors.muted}"
    priceTypography: "{typography.body-md}"
    titleTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    gap: "{spacing.xs}"
  swatch-selector:
    size: 24px
    rounded: "{rounded.full}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.ink}"
    gap: "{spacing.xs}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    linkColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components
**button-primary** proposes the site's main call-to-action style, adapted from the reviews-widget button pattern (`#333` background, white text, uppercase, 700 weight, 0.1em tracking) but recolored to the inferred green `primary` token to align with the "sustainable/organic" positioning; hover and active states are not observed and should be treated as proposed only.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g. "Quick Add" alternates, filter toggles) using ink-on-transparent styling consistent with the neutral, editorial tone of the palette; no outline button was directly observed in the supplied CSS.

**text-input** covers newsletter signup and search fields; border and focus-ring colors are inferred (hairline grey and the one observed blue, reused as a focus token) since no explicit input CSS was supplied.

**nav-bar** represents the top navigation/mega-menu structure implied by the extensive category text (Shop, Christmas, Out & About, Nursery, Gifting, etc.); background uses the warm canvas cream and hairline dividers, but exact nav CSS (padding, sticky behavior) was not in the evidence and is proposed.

**product-card** models the repeating "Quick Add" product tiles seen in the page text (price, colour-count, badges like "best seller"/"new in"/"bundle offer"); card background is white against the cream page background to create gentle contrast, which is inferred from the palette's surface tones rather than measured card CSS.

**swatch-selector** is a category-appropriate component for nursery/baby goods, where nearly every product lists multiple colourways or print collections ("3 colours," "6 colours," "Little Farm," "Riverbank"); a small circular swatch pattern is proposed since no swatch markup/CSS was supplied.

**hero** proposes the homepage banner treatment for messages like "Christmas Magic Has Landed" and "10% Off Your First Order," using the display heading font on a soft cream surface; exact hero imagery, height, and overlay treatment are not observed.

**footer** groups newsletter, trust badges ("Organic Cotton," "Free Shipping," "53k IG Followers") and link columns implied by the page text; styling is proposed from the same soft-surface/ink-text pairing used elsewhere.

**badge** covers merchandising labels ("best seller," "new in," "bundle offer," "Personalise Me") visible in the page text; the terracotta accent color is used here as an inferred badge color since it appears sparingly in the raw palette and no other more frequent accent was evidenced.

**search** is a proposed pattern for the header search field/overlay referenced in the page text ("Search Search Clear Popular searches"); field chrome is inferred from the general neutral palette, not from dedicated search CSS.

## Responsive Behavior
Recommendation only — no responsive/mobile behavior was captured in the supplied evidence.

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | up to 599px | Single-column product grid; nav collapses to hamburger + slide-out menu; sticky announcement bar may need to shrink or dismiss. |
| Tablet | 600–1023px | 2-column product grid; mega-menu may collapse into accordions. |
| Desktop | 1024–1439px | Full mega-menu nav; 3–4 column product grid. |
| Wide | 1440px+ | Max-width content container with increased side padding. |

Touch targets should be a minimum 44×44px for nav items, swatches, and Quick Add buttons. Mega-menu categories (Shop, Christmas, Out & About, Baby Changing Bags, Feeding & Weaning, Nursery, Baby Toys & Activity, Gifting, Bundles, Print Collections) should collapse into expandable accordion groups on mobile given their depth, but this collapse behavior is proposed, not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no live rendering, computed layout, or interaction states (hover, focus, active, disabled, error) were observed beyond the third-party reviews-widget rules supplied. The semantic role of several single-occurrence colors (`#29845a`, `#ed6e41`, `#af7b88`, `#2332d5`, `#005bd3`) is inferred and could belong to unrelated third-party widgets rather than core brand styling. Font usage for Bodoni, Cardo, and Roundhand/cursive was listed in the raw font-family evidence but no selector confirmed where they apply, so they are excluded from the typography scale. All pixel sizes in the typography, rounded, and spacing scales beyond the explicitly observed `border-radius:0` and letter-spacing `0.1em` values are proposed, not measured. Mobile/responsive layout, breakpoints, and component collapse behavior were not observed and are recommendations only. Licensing and availability of the custom 'ar-larkin' and 'ar-helvetica' font files were not verified.
