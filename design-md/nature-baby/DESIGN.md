---
version: alpha
name: "Nature Baby"
source_url: "https://naturebaby.com"
captured_at: "2026-09-29T04:21:13.373955+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Nature Baby's public CSS evidence points to a soft, organic palette built from
  layered off-whites and creams (#ffffff, #fbf7ef, #f5f2ec, #f8f1e3, #f3eee2)
  paired with a family of muted sage and forest greens (#8ca89a, #7d9d8d,
  #588f74, #425c58, #2e5a57) and warm tan/gold tones (#ab8c52, #9a7e4a,
  #e8d4ae, #806430). Text and structural elements rely on near-black and
  charcoal grays (#111111, #1c1c1c, #272727, #333333) with light gray
  hairlines (#d1d1d1, #cccccc, #e8e8e8). A single saturated red (#ea0202)
  appears only once in the evidence and is treated here as an inferred
  sale/alert accent, not a brand color.

  Font evidence lists Gotham, Raleway, Roboto Slab, Helvetica/Arial, American
  Typewriter and "Little Days" alongside generic sans-serif. "Little Days"
  reads as a softer display face suited to a baby/kids storefront and is
  mapped here to hero and section headings; Roboto Slab is mapped to
  sub-headings for warmth; Gotham/Raleway/Helvetica cover body and UI text.
  All font-role assignments, the sage-green primary, gold secondary accent,
  and cream surface tiers are inferred pairings for a natural, unbleached,
  nursery-appropriate storefront — not measured brand declarations. Layout,
  spacing rhythm, and component states beyond the observed 107px/99px/73px
  header heights are proposed, not observed.

colors:
  primary: "#588f74"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#272727"
  muted: "#999999"
  hairline: "#d1d1d1"
  surface-soft: "#f5f2ec"
  surface-card: "#fbf7ef"
  on-primary: "#ffffff"
  accent-gold: "#ab8c52"
  accent-forest: "#425c58"
  surface-mint: "#e6f7f4"
  alert: "#ea0202"
  border-strong: "#cccccc"
typography:
  display-xl: {fontFamily: "Little Days, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Little Days, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Roboto Slab, serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Gotham, Raleway, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Raleway, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Gotham, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    height: "107px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.accent-forest}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
  size-fabric-filter-chip:
    backgroundColor: "{colors.surface-mint}"
    textColor: "{colors.accent-forest}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
    borderColor: "{colors.hairline}"

## Components
**button-primary**: Sage green fill with white text, used for primary calls to action such as "Add to Bag" and newsletter submission; proposed hover/active/disabled states are not present in the supplied CSS.

**button-secondary**: Outlined variant on transparent background for secondary actions (e.g., "View Product," filter toggles); border and text share the primary sage tone, inferred from the surrounding palette rather than an observed button rule.

**text-input**: Cream/white field with a light hairline border for search and account/login forms; the observed evidence shows a `.header__logo__link` and search markup but no explicit input styling, so padding and radius are proposed.

**nav-bar**: Fixed-height header derived from the observed `--HEADER-HEIGHT` custom properties (107px desktop, 99px medium, 73px mobile); houses the mega-menu structure evident in the extensive navigation text (wear, sleep, bedding, care, gifts, shop-by-fabric, shop-by-size).

**product-card**: Cream card surface (`surface-card`) intended for the product grid implied by the "shop all" / category listing text; title and price typography are proposed pairings since no product-grid selectors were captured.

**hero**: Full-width introductory band using the soft cream surface and largest display type, matching the page's lead copy about "precious first weeks and months together"; imagery and CTA placement are proposed, not observed.

**footer**: Deep forest-green band with white text, echoing the darker greens present in the palette (#425c58, #2e5a57); intended to host sustainability/circularity links ("worn again," "sustainability") called out in the nav text.

**badge**: Small pill using the single observed red (#ea0202) for sale or low-stock indicators; this is an inferred use of an otherwise unexplained accent color and should be verified against live markup.

**size-fabric-filter-chip**: Category-appropriate component for the "shop by fabric" (organic cotton, pure merino wool, pointelle) and "shop by size" (baby/toddler/kids) filters visible in the navigation copy; styled as a soft mint pill with forest-green text to reinforce the natural-fiber positioning.

## Responsive Behavior
Recommended breakpoint table (proposed, not measured beyond the observed header-height variables):

| Breakpoint | Width | Header height | Notes |
|---|---|---|---|
| Mobile | <768px | 73px (observed `--HEADER-HEIGHT-MOBILE`) | Collapse mega-menu into a slide-out panel; single-column product grid. |
| Tablet | 768–1023px | 99px (observed `--HEADER-HEIGHT-MEDIUM`) | Two-column product grid; condensed nav labels. |
| Desktop | ≥1024px | 107px (observed `--HEADER-HEIGHT`) | Full mega-menu with multi-column category flyouts. |

Touch targets should be at least 44px in the mobile nav and filter chips. All breakpoint values beyond the three header-height variables are recommendations, not measured site behavior; actual grid columns, menu animation, and collapse thresholds were not observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is derived solely from static CSS/text extraction and carries several limitations: no rendered layout, spacing rhythm, or component states (hover/focus/disabled/error) were directly observed beyond the generic `:focus` outline rule referencing `var(--accent)`, whose color value was not resolved in the evidence. Font-to-role mapping (e.g., "Little Days" as display, Roboto Slab as sub-heading) is inferred from typical usage patterns for a kids/organic brand, not confirmed by selector-level font-family evidence tied to headings. Font licensing and availability (particularly "Little Days" and "Gotham," both commercial faces) were not verified. The `rounded` and `spacing` scales are proposed conventions consistent with the observed `--RADIUS` and grid-gap custom properties but no explicit pixel values for radius were captured. The red (#ea0202) and gold (#ab8c52/#9a7e4a) accents' functional roles are inferred, not confirmed. Mobile menu interaction, cart drawer behavior, and product-grid column counts were not present in the supplied evidence and are therefore excluded from firm claims.
