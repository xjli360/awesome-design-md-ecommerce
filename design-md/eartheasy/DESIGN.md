---
version: alpha
name: "EarthEasy"
source_url: "https://eartheasy.com"
captured_at: "2026-09-28T04:41:16.047565+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  EarthEasy's evidence shows a utilitarian ecommerce palette built around a terracotta-red primary (#c4301c) reused across CTAs, sale badges, and the "sale/error" color-scheme background, paired with a warm gold accent (#e1a308) used for primary buttons in the default scheme. Neutral ink-on-white (#000000/#ffffff) carries body copy and headings, with a mid-gray (#666666) reserved for subtext/metadata and a light hairline (#e5e5e5) for borders and dividers. A deep forest green (#284529) appears as an inverse/dark-mode surface, echoing the brand's sustainable-living positioning, while a soft cream (#f8f7f1) and light gray (#dedede) stand in for secondary backgrounds and card surfaces. Multiple numbered "color-scheme" blocks (info, sale, inverse, farmstead) suggest the CMS supports section-level theming rather than a single fixed page background.
  Typography combines two observed proprietary families: "P22 Mackinac Pro" (a serif-leaning display face, likely used for hero/section headlines) and "GT America" (a grotesque sans for UI chrome, nav, and buttons), with "Instrument Sans" appearing as a secondary body/reading typeface. All sizes below are proposed for a content-rich garden/greenhouse storefront; no live layout, spacing, or breakpoint behavior was measured. Semantic color-to-role assignments (surface-soft, surface-card) are inferred approximations from the nearest supplied hex values, not exact CMS variable matches.

colors:
  primary: "#c4301c"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#666666"
  hairline: "#e5e5e5"
  surface-soft: "#dedede"
  surface-card: "#f8f7f1"
  on-primary: "#ffffff"
  accent-gold: "#e1a308"
  accent-gold-hover: "#f0b428"
  forest-dark: "#284529"
  forest-deep: "#2e442c"
  sale-red: "#cf5747"
typography:
  display-xl: {fontFamily: "'P22 Mackinac Pro', serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'P22 Mackinac Pro', serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'GT America', sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'GT America', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Instrument Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'GT America', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'GT America', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    backgroundColor: "{colors.accent-gold}"
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.forest-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.forest-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  guide-callout:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the gold accent seen in the default `:root` scheme (`--color-button: 225,163,8`) with white text, matching the site's default add-to-cart/CTA treatment. **button-secondary** is a proposed outlined variant for lower-emphasis actions like "Learn more" links inside content blocks, using the neutral hairline border rather than a claimed live style. **text-input** assumes the light-gray field background (`--color-field: 237,237,237`) approximated here with the nearest supplied hex, `#dedede`, since the exact field value isn't in the observed palette array. **nav-bar** is inferred from the presence of a persistent shop/learn menu structure in the page text; no header height, sticky behavior, or breakpoint collapse was measured. **product-card** proposes a soft cream surface (`#f8f7f1`) drawn from the "scheme-6" farmstead background, suited to raised-bed and greenhouse product tiles with a serif-leaning title and sans price line. **hero** uses the dark forest inverse scheme (`--color-background: 40,69,41`) with white heading type, plausible for seasonal or category hero banners given the site's sustainability framing, though no hero markup was directly observed. **footer** reuses the deeper forest green as a full-bleed dark band, a common ecommerce pattern; exact footer content/columns were not present in the supplied evidence. **badge** maps to the "sale/clearance" merchandising language in the nav (Fall Harvest Sale, Clearance) using the muted red-orange tone distinct from the brighter primary. **search** is a proposed pill-shaped field consistent with typical header search patterns; **guide-callout** is a category-specific proposed component for the site's "Guides" and "Articles" content (Live/Grow/Eat/Play/Wear/Move/Give), using the info-scheme neutral background to visually separate editorial sustainability content from product listings.

## Responsive Behavior

Recommended, not measured:

| Breakpoint | Width      | Notes |
|---|---|---|
| mobile | <640px | Single-column product grid; nav collapses to a hamburger/drawer pattern; touch targets ≥44px. |
| tablet | 640–1024px | 2-column product grid; secondary nav items may move into a "More" overflow. |
| desktop | 1024–1440px | Full mega-menu (Yard & Garden, Backyard Living, etc.) as suggested by the flat category list in page text. |
| wide | >1440px | Max-width content container with increased side padding (`{spacing.xxl}`). |

Touch targets should meet a 44×44px minimum on primary buttons and nav items. Mega-menu categories (Raised Garden Beds, Greenhouses, Sheds & Structures) likely require an accordion or flyout on mobile; this interaction was not observed and is a UX recommendation only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS custom-property dumps, a page-text excerpt, and a supplied color/font list — no rendered layout, DOM structure, responsive breakpoints, or interaction states (hover, focus, active, disabled) were observed. Several CMS color-scheme variables (e.g., `--color-field: 237,237,237`) do not exactly match any hex in the supplied observed palette array, so `surface-soft` and `surface-card` are approximated to the nearest available swatches and should be treated as inferred, not verified. Typography sizes, weights, and line-heights are proposed defaults for an ecommerce/content hybrid site and are not confirmed via rendered CSS font-size rules. "P22 Mackinac Pro," "P22 Mackinac-Book," "GT America," and "Instrument Sans" are asserted only as font-family declarations present in the source; their licensing, actual glyph availability, and whether they load successfully in production were not verified. Component states beyond default/idle (hover, error, loading, empty-state) are proposed patterns for a garden/greenhouse category storefront and should be validated against the live site before implementation.
