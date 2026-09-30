---
version: alpha
name: "Master & Dynamic"
source_url: "https://masterdynamic.com"
captured_at: "2026-09-28T09:40:37.086832+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Master & Dynamic's storefront CSS shows a restrained, high-contrast neutral system built on true black, white, and a run of near-black and mid-gray steps (#171d21, #3c4144, #4a4a4a, #595959, #626262, #888888, #9e9e9e). Surface tones step from #ffffff through #fbfbfb, #f7f7f7, #f2f2f2, #f1f1f1 to #dedede/#e1e1e1 hairlines, consistent with a premium product-photography-first layout. A small set of saturated colors (#1990c6/#136f99 blue, #0018ff link-blue, #f1c418 yellow, #a45cec purple) appear alongside neutral-dominant tokens and are treated here as inferred utility colors (links, alerts, swatch/status accents) rather than primary brand color, since no CSS evidence ties them to buttons or headers. Semi-transparent black values (#00000066, #00000033, #0000001a, #0000000d, #0000000f) are mapped to overlays and scrims for modals, image hovers, and sticky-header blur states. Typography uses a custom "blender" family (thin/book/medium/bold/heavy weights) for display and heading roles with sans-serif fallback, plus a monospace stack likely reserved for code/SKU contexts, not body copy. Heading sizes (h0–h6) are taken directly from observed CSS custom properties. Corner radii and precise spacing rhythm beyond the exposed section/container variables are proposed, not measured, and are noted accordingly.

colors:
  primary: "#000000"
  ink: "#171d21"
  canvas: "#ffffff"
  body: "#3c4144"
  muted: "#888888"
  hairline: "#e1e1e1"
  surface-soft: "#f7f7f7"
  surface-card: "#fbfbfb"
  on-primary: "#ffffff"
  border-subtle: "#dedede"
  neutral-mid: "#9e9e9e"
  neutral-dark: "#595959"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  link: "#0018ff"
  alert: "#f1c418"
  accent-purple: "#a45cec"
  overlay-scrim: "#00000066"
  overlay-soft: "#0000001a"
typography:
  display-xl: {fontFamily: "blenderbold, sans-serif", fontSize: 64px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "blenderbold, sans-serif", fontSize: 41px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "blendermedium, sans-serif", fontSize: 26px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  caption: {fontFamily: "sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "blendermedium, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 1px}
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
    textColor: "{colors.ink}"
    border: "2px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: "3.125rem"
    padding: "0 {spacing.lg}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    logoWidth: "170px"
    position: "sticky"
    padding: "{spacing.sm} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    gap: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.overlay-scrim}"
    headlineTypography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.neutral-mid}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    inactiveBorder: "{colors.border-subtle}"
    activeBorder: "{colors.ink}"
    size: "32px"
    rounded: "{rounded.full}"
    gap: "{spacing.xs}"

## Components
**button-primary** renders solid-black, white-text calls to action ("Shop Now," "Add to Cart"), matching the button-background/text-color pattern found in the button hover rules; hover state (85% opacity, transparent border) is proposed from the `--button-background-opacity: 0.85` custom property.

**button-secondary** is an outline variant inferred from `.button--outline` selectors, using a 2px ink border on a white background for secondary actions like "Learn More."

**text-input** uses the observed `--input-height: 3.125rem` and `--input-padding-inline: var(--spacing-5)` tokens for form fields such as email capture or account login; border and radius are proposed.

**nav-bar** reflects the sticky header grid (`--header-grid-template`, `position: sticky; top: 0; z-index: 10;`) with a 170–220px logo width depending on breakpoint, and a hairline underline for the product mega-menu (Headphones/Earphones/Accessories).

**product-card** represents the featured-product grid (MW75, MW50+, MH40, MG20) with title/price stacking and a soft card surface; row-gap uses the observed `--product-list-row-gap: var(--spacing-12)`.

**hero** models the rotating homepage banners ("MH40 Wireless," "MW75 Perfect sound, perfect silence") as full-bleed dark sections with a scrim overlay for text legibility over product photography; this compositional pattern is proposed, not directly measured.

**footer** groups support/account/country-selector links seen in the page text (extensive country/currency list) on a dark ink background, consistent with the site's black-and-white contrast strategy.

**badge** covers status labels like "RE-RELEASE" and "Sold out," using the yellow accent as an inferred attention color since no explicit badge CSS was supplied.

**search** models the "Open search" control in the header; background and radius are proposed defaults since no dedicated search-field CSS was included in evidence.

**color-swatch-selector** is a category-specific component for headphone/earphone color options (e.g., "Silver Metal / Brown Leather," "Nocturne / Lake Blue") seen repeatedly in product text; circular swatches with an ink ring on the active state are proposed.

## Responsive Behavior
Recommended breakpoints (not measured from live rendering): mobile ≤640px, tablet 641–1024px, desktop ≥1025px, wide ≥1440px. The header's own custom properties shift `--header-logo-width` from 170px to 220px and switch grid template order between two configurations, implying at least one desktop/tablet breakpoint exists, though the exact pixel threshold is not in the supplied CSS. Container gutter and section spacing variables also scale up at larger viewports (`--container-gutter` moves from 2rem to `var(--spacing-12)`, and section inner spacing increases through several tiers), suggesting three or more responsive tiers. Touch targets should target a minimum 44×44px hit area for nav, cart, and search icons; the product-list carousel (`--product-list-carousel-item-width: 60vw` → `36vw` → fixed 3-column) implies a swipeable card carousel on narrow viewports collapsing to a static grid at desktop widths. Mobile navigation should collapse into a slide-out or drawer menu given the header's compact single-row grid; this is a proposed pattern, not an observed interaction.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties and page text only; no rendered screenshots, computed styles, or interactive states (hover, focus, active, disabled) were observed. Color-to-role mapping (e.g., which blues/yellows/purples serve as links vs. alerts vs. swatch accents) is inferred from typical e-commerce conventions, not confirmed by selector-level evidence tying them to specific UI elements. Font weights and exact letter-spacing for the "blender" family are proposed defaults since only family names, not weight/size pairings, were supplied for body text. Border radius values throughout are proposed defaults; no `border-radius` declarations appeared in the supplied CSS. Breakpoint pixel values are recommended, not extracted from actual `@media` rules. Mobile menu behavior, search overlay behavior, and cart-drawer interactions are not observed and are described only as plausible patterns. Licensing and web-font delivery method for the custom "blender" family were not verified.
