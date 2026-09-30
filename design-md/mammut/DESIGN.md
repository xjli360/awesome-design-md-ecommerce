---
version: alpha
name: "Mammut"
source_url: "https://mammut.com"
captured_at: "2026-09-29T04:21:19.300015+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from Mammut's Next.js-served stylesheet fragments and Yotpo review-widget overrides, which together expose the brand's typographic and chromatic system rather than a full page layout. Two observed font families anchor the type system: __AGNext (a proportional sans used for headings, review titles, and body text) and __BaselGroteskMonoBook (a monospaced, uppercase-tracked face used for buttons, labels, and "read more" links). The palette is dominated by true black (#000000) and white (#ffffff), with the CSS custom property --accentColor explicitly set to #ed001b, a saturated red used sparingly as the brand accent. Supporting neutrals (#676767, #cdcdcd, #e1e1e1, #f0f0f0, #dadada, #999999) form a grayscale hairline-and-surface system, while additional hues (#4b9524, #fe5219, #dfff54, #1cc286, #db3a00, #23293c) appear in the palette but their functional roles are not evidenced in the supplied rules, so they are treated as inferred accent/status candidates rather than assigned primary meaning. Borders and buttons favor a tight 2px corner radius. The overall interpretation proposes a restrained, high-contrast, performance-oriented alpine aesthetic: black/white foundation, red accent for calls to action, and monospaced uppercase micro-copy for a technical, athletic tone.

colors:
  primary: "#ed001b"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#454545"
  muted: "#676767"
  hairline: "#cdcdcd"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border-subtle: "#e1e1e1"
  border-strong: "#dadada"
  neutral-mid: "#999999"
  overlay-scrim: "#00000080"
  accent-orange: "#fe5219"
  accent-green: "#4b9524"
  accent-teal: "#1cc286"
  deep-navy: "#23293c"
typography:
  display-xl: {fontFamily: "__AGNext, __AGNext_Fallback, sans-serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.02em}
  display-md: {fontFamily: "__AGNext, __AGNext_Fallback, sans-serif", fontSize: 23px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.02em}
  title-md: {fontFamily: "__AGNext, __AGNext_Fallback, sans-serif", fontSize: 17px, fontWeight: 500, lineHeight: 1.2, letterSpacing: -0.01em}
  body-md: {fontFamily: "__AGNext, __AGNext_Fallback, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0em}
  body-sm: {fontFamily: "__AGNext, __AGNext_Fallback, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0em}
  caption: {fontFamily: "__BaselGroteskMonoBook, __BaselGroteskMonoBook_Fallback, monospace", fontSize: 12px, fontWeight: 400, lineHeight: 1.0, letterSpacing: 0.04em}
  button-md: {fontFamily: "__BaselGroteskMonoBook, __BaselGroteskMonoBook_Fallback, monospace", fontSize: 13px, fontWeight: 400, lineHeight: 1.0, letterSpacing: 0.04em}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-subtle}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.border-subtle}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.deep-navy}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.overlay-scrim}"
    titleTypography: "{typography.display-xl}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-subtle}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  pack-spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"

## Components
**button-primary** renders as a black-filled, white-text control with a tight 2px radius, matching the observed Yotpo "write a review" button styling (`background-color:#000!important;border-radius:2px!important`). Hover state (proposed by analogy to the observed inverse hover) swaps to white background with a light gray border.

**button-secondary** is an outlined inverse of the primary, white background with a hairline border, intended for lower-emphasis actions like "Learn more" links seen throughout the hero and collection copy blocks.

**text-input** is a minimal bordered field using the light border-subtle tone (#e1e1e1) observed on card and container edges; padding and focus states are proposed, not measured.

**nav-bar** is inferred from the multi-tier "Main navigation" text content (genders, Clothing, Footwear, Equipment, Outlet, Shop by Activity, Collections) but no header CSS was supplied, so its background, border, and spacing are proposed defaults consistent with the neutral palette.

**product-card** is proposed for the repeated jacket/product tiles ("Rime Light IN Hybrid Hooded Jacket", price displays) implied by the page text; card chrome (border, radius, padding) is inferred from the general hairline/surface tokens since no card-specific CSS rule was in evidence.

**hero** models the large promotional banners referenced in copy ("The art of alpine comfort", "Stay dry, whatever the weather"); the deep-navy background and overlay scrim are proposed choices from the supplied palette to suggest an alpine, image-backed hero, not a measured style.

**footer** is inferred from the long sitemap-style link list (Shop, About, Support) in the page text; a black background with white text is proposed to mirror the button-primary treatment, but no footer CSS was supplied.

**badge** proposes a small pill using the accent red, suitable for "New Style" / "New Colors Added" labels seen in the product copy; shape and color are inferred, not directly styled in the evidence.

**search** is a proposed lightweight input treatment for the Help Center / site search implied by navigation copy; no dedicated search CSS was present in the supplied rules.

**pack-spec-table** is a category-appropriate proposed component for Backpacks & Bags product detail pages (capacity, weight, material specs), styled with the neutral surface and hairline tokens observed elsewhere, since no literal spec-table CSS was supplied.

## Responsive Behavior
Recommended, not measured: mobile (<480px) collapses navigation into a hamburger/drawer pattern with 44px minimum touch targets; tablet (480–1024px) shows a condensed top nav with category flyouts; desktop (>1024px) shows the full mega-menu implied by the "all genders \\ Clothing / Footwear / Equipment" text structure. Buttons and inputs should maintain a minimum 44×44px hit area on touch devices. This table is a proposed convention based on typical e-commerce patterns, not an observed breakpoint from the supplied CSS.

| Breakpoint | Width | Nav behavior |
|---|---|---|
| Mobile | < 480px | Hamburger drawer, single-column product grid |
| Tablet | 480–1024px | Condensed nav, 2-column product grid |
| Desktop | > 1024px | Full mega-menu, 3–4 column product grid |

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from a partial CSS extraction (primarily a single bundled chunk plus Yotpo review-widget overrides) and the visible page text; no full page layout, header/footer markup, or product-listing CSS was supplied, so nav-bar, product-card, hero, footer, search, and pack-spec-table are proposed/inferred components, not observed styles. The two font families (__AGNext, __BaselGroteskMonoBook) are Next.js-obfuscated local-font identifiers; their visual rendering, weights beyond those shown (400/500), and licensing/availability are not verified. Many palette entries (#4b9524, #fe5219, #dfff54, #1cc286, #db3a00, #23293c, and various alpha-channel blacks/whites) appear in the supplied color list without an associated selector, so their semantic roles (status colors, chart colors, overlays) are inferred guesses rather than confirmed mappings. All spacing, radius scale (beyond the confirmed 2px button radius), breakpoints, and hover/focus interaction states are proposed conventions for a performance-outdoor storefront and have not been visually confirmed against the live site.
