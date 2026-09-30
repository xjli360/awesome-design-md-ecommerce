---
version: alpha
name: "Delta Children"
source_url: "https://deltachildren.com"
captured_at: "2026-09-28T04:52:38.540511+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Delta Children's storefront runs on a Shopify theme with a compact, utilitarian
  visual system built around Poppins as the primary typeface (falling back to
  Helvetica, Arial, sans-serif) for headings, body copy, and buttons. The
  observed palette centers on a mid-saturation blue (#3575ca) used consistently
  as the primary action and review-widget accent color, with a darker blue
  (#2d63ac / #2a5ea2) reserved for hover and border states. Body copy uses a
  muted charcoal-gray (#666666), while neutral grays (#999999, #c6c6c6,
  #fafafa) construct hairlines, disabled states, and soft surface fills such
  as accordion panels. White (#ffffff) is the canvas and on-primary text
  color. This interpretation infers a card-and-accordion-driven product UI
  typical of nursery/juvenile e-commerce, assigns semantic roles (ink, muted,
  hairline, surface-soft/card) to the closest matching observed hex values,
  and proposes a light-blue tint (#dfe9f6) as an informational/accent
  surface. Corner radii of 4px and 8px are directly observed on accordions
  and buttons; the rounded scale extends this pattern. All type sizes beyond
  the two directly observed (14px body, 15px button, 16px accordion header)
  are proposed extrapolations for a coherent scale, not measured site values.

colors:
  primary: "#3575ca"
  primary-hover: "#2d63ac"
  primary-border-hover: "#2a5ea2"
  ink: "#1e1e1e"
  canvas: "#ffffff"
  body: "#666666"
  muted: "#999999"
  hairline: "#c6c6c6"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-tint: "#dfe9f6"
  accent-line: "#8eb2e1"
  success: "#409606"
  error: "#c3201e"
typography:
  display-xl: {fontFamily: "Poppins, Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Poppins, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-md: {fontFamily: "Poppins, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.15px}
  body-sm: {fontFamily: "Poppins, Helvetica, Arial, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Poppins, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.15px}
  button-md: {fontFamily: "Poppins, Helvetica, Arial, sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1, letterSpacing: 0px}
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
  button-primary: {backgroundColor: "{colors.primary}", textColor: "{colors.on-primary}", typography: "{typography.button-md}", rounded: "{rounded.md}", padding: "{spacing.md} {spacing.lg}"}
  button-secondary: {backgroundColor: "transparent", textColor: "{colors.primary}", borderColor: "{colors.primary}", typography: "{typography.button-md}", rounded: "{rounded.md}", padding: "{spacing.md} {spacing.lg}"}
  text-input: {backgroundColor: "{colors.canvas}", borderColor: "{colors.hairline}", textColor: "{colors.ink}", typography: "{typography.body-md}", rounded: "{rounded.sm}", padding: "{spacing.sm} {spacing.base}"}
  nav-bar: {backgroundColor: "{colors.canvas}", textColor: "{colors.body}", typography: "{typography.body-md}", borderColor: "{colors.hairline}", padding: "{spacing.base} {spacing.lg}"}
  product-card: {backgroundColor: "{colors.surface-card}", borderColor: "{colors.hairline}", rounded: "{rounded.sm}", padding: "{spacing.base}", titleTypography: "{typography.title-md}", priceTypography: "{typography.body-md}"}
  hero: {backgroundColor: "{colors.accent-tint}", textColor: "{colors.ink}", typography: "{typography.display-md}", padding: "{spacing.section} {spacing.xl}"}
  footer: {backgroundColor: "{colors.surface-soft}", textColor: "{colors.body}", typography: "{typography.body-sm}", borderColor: "{colors.hairline}", padding: "{spacing.xxl} {spacing.lg}"}
  badge: {backgroundColor: "{colors.success}", textColor: "{colors.on-primary}", typography: "{typography.caption}", rounded: "{rounded.full}", padding: "{spacing.xxs} {spacing.sm}"}
  search: {backgroundColor: "{colors.canvas}", borderColor: "{colors.hairline}", textColor: "{colors.ink}", typography: "{typography.body-md}", rounded: "{rounded.sm}", padding: "{spacing.sm} {spacing.base}"}
  cart-drawer: {backgroundColor: "{colors.canvas}", textColor: "{colors.ink}", borderColor: "{colors.hairline}", subtotalTypography: "{typography.title-md}", itemTypography: "{typography.body-sm}", padding: "{spacing.lg}"}

## Components

**button-primary** uses the directly observed `#3575ca` fill with white text and a 700-weight 15px label, matching the `.button--primary` rule; hover darkening to `#2d63ac` is observed and proposed for all primary CTAs (Add to Cart, checkout).

**button-secondary** is a proposed outline variant using the same primary blue for border and text on a transparent background, for lower-emphasis actions like "View Details."

**text-input** is a proposed pattern using the observed hairline gray for borders and body-md typography, since no explicit input CSS was supplied.

**nav-bar** infers a white header with gray body-weight link text, given the extensive mega-menu text content (Nursery, Kids' Bedroom, Play & Outdoor, Strollers, Baby Gear) but no direct header CSS.

**product-card** is a proposed container for grid listings (e.g., "Nest 4-in-1 Convertible Crib," "$499.99") using surface-card white and the 4px radius family observed on accordions/buttons.

**hero** is a proposed promotional band using the soft accent-tint blue background inferred from `--jdgm-secondary-color`/`#dfe9f6`, suited to sale banners like "FALL SALE | 15% OFF SITEWIDE."

**footer** groups the extensive "Here To Help," "Safety," and "About Us" link clusters observed in navigation text, using surface-soft gray and small body typography.

**badge** is a proposed small pill for trust/safety callouts (e.g., "GREENGUARD GOLD Certified") using the observed green `#409606`; not confirmed as an actual badge color in supplied CSS.

**search** mirrors text-input styling for the site search field referenced in navigation ("Search Products").

**cart-drawer** reflects the "Cart Preview" / "Subtotal" content observed in the page text, using white background and hairline dividers between line items.

## Responsive Behavior

Proposed breakpoints (not measured): mobile ≤599px, tablet 600–1023px, desktop ≥1024px. Below tablet, the multi-level mega-menu (Nursery, Kids' Bedroom, Play & Outdoor, Baby Gear, Mattresses, Bedding, Accessories) is expected to collapse into the "Mobile Nav" accordion pattern referenced in the page text ("Mobile Nav Close Search"). Touch targets for nav items and buttons should be at least 44px tall, consistent with the 40px `.numbered-dots` control already observed. Product grids likely reflow from multi-column desktop to single/double-column mobile; this is a recommendation only, not confirmed layout behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, breakpoints, or interactive states (hover/focus/active, mobile menu open/close, cart drawer animation) were directly observed. Semantic role assignments (ink, muted, surface-card vs. surface-soft, accent-tint) are inferred from the closest matching hex in the supplied palette and may not reflect actual design intent. Typography sizes beyond the three explicitly observed (14px body, 15px button, 16px accordion header) are proposed for scale coherence, not measured. Font availability, licensing, and web-font loading for Poppins are not verified from the supplied evidence. Additional fonts listed in evidence (Gotham, RIFFIC, Sweety Tea, Avenir Black, JudgemeStar) were not tied to any supplied CSS rule and are therefore excluded from the typography scale.
