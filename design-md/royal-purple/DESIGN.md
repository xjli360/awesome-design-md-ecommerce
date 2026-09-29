---
version: alpha
name: "Royal Purple"
source_url: "https://royalpurple.com"
captured_at: "2026-09-28T10:01:53.371858+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Royal Purple's public site pairs a deep proprietary-looking purple (#330072, echoed in the
  homepage's diagonal gradient token) against a mostly neutral, high-contrast system of
  near-black text, mid-grays, and white surfaces — a palette suited to a technical, industrial
  lubricants brand rather than a lifestyle one. Buttons are observed with a dark slate fill
  (#32373c), white text, and a fully-rounded 9999px pill shape, which this spec treats as the
  primary interactive pattern site-wide. A navy (#141b38) and slate (#2c324c) appear in the
  supplied CSS and are inferred here as secondary dark-surface options (footers, overlays,
  hover-heading text shadows) rather than confirmed section backgrounds. Typography draws on
  the observed font stack: Russo One is assigned to display/heading roles as the only distinct
  display-style face present, while Figtree and Open Sans (with Arial/Helvetica fallbacks)
  cover body and UI text. Sizes largely follow WordPress preset tokens actually present in the
  CSS (16px base, 42px "huge"); all other sizes, weights, and line-heights are proposed
  extrapolations, not measured. Red (#dc3545) is reserved as an inferred error/alert accent
  only, sourced from an admin-bar icon rule, not a confirmed brand or CTA color.

colors:
  primary: "#330072"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  button-dark: "#32373c"
  navy: "#141b38"
  slate: "#2c324c"
  danger: "#dc3545"
typography:
  display-xl: {fontFamily: "'Russo One', sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Russo One', sans-serif", fontSize: 42px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Figtree, Arial, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.1, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Figtree, Arial, sans-serif", fontSize: 18px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.3px}
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
    backgroundColor: "{colors.button-dark}"
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
    typography: "{typography.body-md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    overlay: "{colors.primary}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.slate}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  product-selector-tool:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the observed dark-slate fill (#32373c) with white text and a full 9999px
pill radius, matching the `.wp-block-button__link` rule found in the CSS. This is treated as the
site's primary call-to-action style (e.g., "Learn More," "Find a Retailer").

**button-secondary** is a proposed outline variant using the brand purple, inferred from the
`is-style-outline` button rule (transparent background, currentColor text) but recolored to the
purple token for visual hierarchy; not directly confirmed against a live screenshot.

**text-input** is a proposed pattern for search and locator forms (service-center finder, product
selector), using neutral surfaces and hairline borders consistent with the site's restrained
palette; no live form styling was captured in evidence.

**nav-bar** reflects the multi-level menu structure evident in the page text (Solutions, Personal,
Racing, Commercial, About Us, etc.) as a white, ink-text bar with a bottom hairline; exact height,
sticky behavior, and dropdown styling are proposed, not measured.

**product-card** is proposed for listing motor oils, additives, and specialty lubricants (referenced
in nav copy like "Motor Oils," "Performance Additives," "Racing"), using a card surface with a
subtle border and medium radius; card imagery, badges, and spec tags were not directly observed.

**hero** is inferred from the homepage's gradient token (`--gs-gradientone`, purple-to-white
diagonal) and large "huge" 42px type preset; this spec substitutes a solid navy background with a
purple overlay treatment as a conservative interpretation, since exact gradient rendering context
wasn't confirmed.

**footer** uses the slate/navy family as a dark closing band, consistent with typical WordPress
theme footer patterns and the dark-surface tokens present in CSS; content structure (columns,
legal links) is proposed.

**badge** is proposed for spec/viscosity labels (e.g., "0W-16," "ILSAC GF-7," "Dexos D") mentioned
throughout the product news copy, using a soft neutral chip; no badge markup was present in the
supplied CSS.

**search** and **product-selector-tool** are category-appropriate additions: the site explicitly
promotes a "Product Selector" and "Retail & Service Finder" in its navigation, so these components
model a pill-shaped search affordance and a card-based selector tool using brand-purple accents;
both are proposed compositions from available tokens, not observed component markup.

## Responsive Behavior

Proposed, non-measured breakpoint table:

| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| xs        | <480px      | Single-column nav collapses to hamburger/toggle menu ("Toggle Menu" text was observed in page copy, confirming a mobile menu exists, though its styling was not). |
| sm        | 480–768px   | Stacked hero and product cards; touch targets ≥44px. |
| md        | 768–1024px  | Two-column product grids; nav dropdowns may become accordions. |
| lg        | 1024–1440px | Full multi-level nav bar with hover/click submenus. |
| xl        | >1440px     | Max content width constrained via WordPress `--wp--style--global--content-size` token. |

Touch targets should maintain a minimum 44×44px hit area for buttons and nav toggles. All
breakpoint values, collapse behavior, and touch-target sizing are recommendations based on common
WordPress/responsive conventions, not measurements of the live site.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS custom properties, a page-text excerpt, and a
supplied color/font list — no live rendering, computed styles, or DOM screenshots were available.
Semantic role assignments (e.g., which grays serve as body vs. muted text, which dark color is the
true footer background) are inferred from common usage patterns, not confirmed against rendered
pages. The `#330072` primary is inferred from brand-name association and gradient usage, not an
explicit "brand color" variable. Russo One's assignment to display headings is inferred from its
distinctiveness in the font list; no heading element was directly observed using it. All font
weights, letter-spacing values, and most font-sizes beyond the two confirmed WordPress presets
(16px, 42px) are proposed, not extracted. Interaction states (hover, focus, active, disabled),
mobile menu behavior, and actual grid/card layouts were not observed. Font licensing and
self-hosting/CDN availability for Figtree, Open Sans, and Russo One were not verified.
