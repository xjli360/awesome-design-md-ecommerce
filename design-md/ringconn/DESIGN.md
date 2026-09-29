---
version: alpha
name: "RingConn"
source_url: "https://ringconn.com"
captured_at: "2026-09-28T09:41:20.256856+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  RingConn's storefront evidence shows a clean, clinical wearables aesthetic built on a white canvas
  (#ffffff) with near-black body text (#111111) and a mid-saturation blue (#2970d3) used explicitly
  as the header navigation hover/underline accent. A closely related blue (#2a6fd3, #3181df) appears
  elsewhere in the palette, suggesting a small family of interactive-blue tones rather than one fixed
  brand blue; this design treats #2970d3 as the canonical primary and reserves the others as inferred
  hover/active variants. Neutral grays (#f6f6f6, #f3f3f3, #e5e5e5, #666666, #999999) support card
  surfaces, hairlines, and secondary text in a typical health-tech, low-chroma system. Two warm outlier
  tokens (#fff1e3, #412d00) likely back a seasonal or gift-card promotional module and are kept
  separate from the core UI palette. Typography is led by HelveticaNowDisplay, a licensed display
  sans confirmed in the font stack, backed by system-ui/Helvetica Neue/Arial fallbacks; Montserrat and
  Roboto also appear in the stack and are treated as inferred secondary/utility faces. A CJK/monospace
  tail (NotoSansJP, FZLTZHK, Consolas, Menlo) supports localization and technical spec display only.
  Heading and body sizes are taken directly from the site's own CSS custom-property type scale.

colors:
  primary: "#2970d3"
  primary-hover: "#2a6fd3"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e5e5e5"
  surface-soft: "#f6f6f6"
  surface-card: "#f3f3f3"
  on-primary: "#ffffff"
  accent-warm-bg: "#fff1e3"
  accent-warm-ink: "#412d00"
  success: "#28a745"
typography:
  display-xl: {fontFamily: "HelveticaNowDisplay, system-ui, sans-serif", fontSize: 56px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "HelveticaNowDisplay, system-ui, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "HelveticaNowDisplay, system-ui, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "HelveticaNowDisplay, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "HelveticaNowDisplay, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "HelveticaNowDisplay, Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "HelveticaNowDisplay, system-ui, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hoverAccent: "{colors.primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderRadius: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.canvas}"
    headingTypography: "{typography.display-xl}"
    subheadingTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    spacing: "{spacing.section}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-warm-bg}"
    textColor: "{colors.accent-warm-ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  ring-size-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm}"

## Components
**button-primary** carries the solid-blue call-to-action pattern (e.g. "Shop Now," "Learn More") inferred from the explicit `#2970d3` hover/underline token seen on nav links; the resting fill is treated as the same blue with white text, a common pattern for this class of storefront, and is proposed rather than directly observed on button elements.

**button-secondary** is an outline variant using the same primary blue for border and text on a transparent background, matching the `.button--outline` hover-swap logic present in the site's own CSS (`box-shadow: inset 0 0 0 2px currentColor`), which confirms an outline-to-fill hover behavior exists even though exact resting styles were not captured.

**text-input** is a proposed field style using the near-white canvas, a light hairline border, and body-md type; no explicit input CSS was supplied, so padding and radius are conventional defaults.

**nav-bar** reflects the confirmed sticky header: `position: sticky; top: 0; background-color: #ffffff` with a subtle drop shadow and a `#2970d3` underline that fades in on hover of dropdown/mega-menu triggers, per the supplied selector.

**product-card** is inferred for the Gen 3 / Gen 2 / Gen 2 Air / Charging Case grid implied by the shop navigation; it uses the light gray surface tone and title-md typography, but exact card padding/shadow were not present in evidence.

**hero** models the homepage's large promotional banners ("Make Health the Perfect Gift," "A health intelligence system, built into a ring") using the largest measured heading token (`--text-h0`) and generous section spacing drawn from `--section-outer-spacing-block`.

**footer** is proposed using the muted surface-soft background and smaller body-sm type, consistent with the multi-region language/country selector list seen in the page text, though no footer-specific CSS was supplied.

**badge** covers small status labels such as "HSA/FSA eligible," using the warm outlier tokens (`#fff1e3`/`#412d00`) that appear disconnected from the core neutral/blue system and are likely reserved for promotional or eligibility callouts.

**search** is a proposed overlay input for the confirmed "Open search" control referenced in navigation markup; visual styling is inferred from the general surface/hairline system since no dedicated search CSS was supplied.

**ring-size-selector** is a category-specific proposed component for smart-ring size/fit selection (referenced via "sizing kit," "Find Your Perfect Ring"), using pill-shaped selectable swatches with the primary blue marking the active state.

## Responsive Behavior
This is a recommended breakpoint strategy, not measured site behavior; the supplied CSS confirms only that heading sizes and section spacing scale up at wider viewports via redefined `:root` custom properties (e.g. `--text-h0` moving from 3.5rem to 4.5rem, `--section-outer-spacing-block` increasing stepwise).

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <768px | Single-column stacking, nav collapses to a menu drawer, smaller `--text-h*` tier applies |
| Tablet | 768–1199px | Two-column product grids, header padding reduces from the 40px desktop value |
| Desktop | ≥1200px | Full header grid (`logo / main-nav / secondary-nav`), largest heading tier, `--header-section-padding: 0px 40px` |

Touch targets should be at least 44×44px for nav and cart controls; the mega-menu/dropdown disclosure pattern implied by `details[is="mega-menu-disclosure"]` should collapse to an accordion on mobile. Exact collapse thresholds and drawer behavior were not observed and are proposed defaults.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Static CSS extraction does not confirm actual rendered button, card, or input styles beyond the header/nav rules supplied; several components above are proposed patterns, not verified observations.
- The primary blue is inferred from one confirmed usage (nav hover underline, `#2970d3`); resting-state button and link colors were not directly evidenced.
- Semantic roles for near-duplicate blues (`#2a6fd3`, `#3181df`, `#005fcc`, `#007bff`, `#0056b3`) and grays (`#f9f9f9` vs `#f6f6f6` vs `#f5f5f5`) are approximated; the true design-token mapping is unknown.
- HelveticaNowDisplay is a licensed commercial font; its availability and licensing terms were not verified beyond its presence in the font-family stack.
- No interaction states (focus, disabled, loading), mobile menu behavior, or checkout/cart UI were observed; all such details in this document are proposed, not measured.
- Type scale pixel values are converted from the site's own `rem`-based custom properties assuming a 16px root, which was not independently confirmed.
