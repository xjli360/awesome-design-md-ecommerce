---
version: alpha
name: "Saddleback Leather"
source_url: "https://saddlebackleather.com"
captured_at: "2026-09-28T10:22:46.831734+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Saddleback Leather's storefront runs on a BigCommerce Stencil theme with a
  restrained, craft-goods palette. The observed CSS sets body copy and all
  heading levels in Poppins (falling back to Arial, Helvetica, sans-serif),
  with headings at weight 700 and body copy at weight 400 — a single-family
  system rather than a display/body font pairing. Ink (#2f2f2b) on a white
  canvas forms the base reading pair. The saddle-tan #be7b42 is the confirmed
  primary action color, used on `.button--primary` and default `.button`
  borders, with #f19446 as its confirmed hover/active state. #a2a2a2 is used
  for muted captions and inactive pagination. #f4f0ed appears as a soft panel
  background (`.panel-header`), and #fcfbf9 is treated here as an inferred
  lighter card surface drawn from the same warm-neutral family, since no
  distinct card background rule was supplied. Hairlines and disabled states
  are inferred from the neutral grays present in the palette (#e5e5e5,
  #cccccc) rather than from a rule explicitly labeled "border" or "disabled."
  No product-card, hero, or duffel-specific layout was present in the
  supplied evidence, so those components below are proposed, brand-plausible
  patterns consistent with the leather-goods, warranty-forward tone of the
  copy, not observed markup.

colors:
  primary: "#be7b42"
  primary-hover: "#f19446"
  ink: "#2f2f2b"
  canvas: "#ffffff"
  body: "#2f2f2b"
  muted: "#a2a2a2"
  hairline: "#e5e5e5"
  border-form: "#999999"
  surface-soft: "#f4f0ed"
  surface-card: "#fcfbf9"
  on-primary: "#ffffff"
  disabled: "#cccccc"
  disabled-border: "#0000000d"
typography:
  display-xl: {fontFamily: "Poppins, Arial, Helvetica, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.25px}
  display-md: {fontFamily: "Poppins, Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.25px}
  title-md: {fontFamily: "Poppins, Arial, Helvetica, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0.25px}
  body-md: {fontFamily: "Poppins, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Poppins, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Poppins, Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "Poppins, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.0, letterSpacing: 0px}
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
    hover:
      backgroundColor: "{colors.primary-hover}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    hover:
      borderColor: "{colors.primary-hover}"
  button-disabled:
    backgroundColor: "{colors.disabled}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.disabled-border}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-form}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.body}"
    padding: "{spacing.xxl} {spacing.lg}"
    ctaComponent: "button-primary"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-form}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  warranty-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.primary}"
    padding: "{spacing.xs} {spacing.sm}"

## Components
**button-primary** — Maps directly to the observed `.button--primary` rule (tan fill, white text, hover shifts to the lighter orange-tan). Used for primary conversion actions such as "Add to Cart" and "Shop Now."

**button-secondary** — Inferred outline variant, modeled on the base `.button` rule which is border-only with transparent fill; proposed for secondary actions like "View Details."

**button-disabled** — Directly reflects the `.button[disabled]` rule's gray fill; state and trigger conditions (form validation, sold-out items) are proposed, not observed.

**text-input** — Inferred from `.form-body`'s border/background values; exact input-level border-radius and padding are proposed defaults, not confirmed by a distinct input selector.

**nav-bar** — Proposed composition using the confirmed white canvas and ink text color; the mega-menu structure (Mens/Womens/Footwear/etc.) is evident in the page text but no nav CSS rules were supplied, so visual treatment is inferred.

**product-card** — Proposed for duffel/travel-bag listings; card caption color (`#a2a2a2`) is directly drawn from `.card-figcaption-body .card-text`, but the card container's background, radius, and border are inferred since no `.card` container rule was supplied.

**hero** — Proposed pattern for the "Deep Pocket Leather Duffle Bag" featured-item banners referenced in the page text; background uses the confirmed `#f4f0ed` panel tone, but no hero-specific CSS was in evidence.

**footer** — Proposed structure; reuses the soft surface and muted text tokens already confirmed elsewhere on the page, since no footer selector was supplied.

**badge** — Proposed pill component for merchandising labels ("Sold out," "New Arrivals") seen in the page copy; styling is inferred from the primary color token, not from a badge-specific rule.

**warranty-badge** — Proposed category-appropriate component reflecting the site's repeated "100 YEAR WARRANTY" and "NO BREAKABLE PARTS" messaging; an outlined tag using the primary tan against the soft surface, entirely inferred from copy emphasis rather than CSS.

## Responsive Behavior
Breakpoint math is visible in the supplied media-query fragments (approximate boundaries near 551px, 801px, 1261px, and 1681px), but exact component behavior at each was not observed. Recommended (proposed) breakpoints:

| Range | Layout guidance |
|---|---|
| < 551px | Single-column stack, nav collapses to a toggle menu (site text confirms a "Toggle menu" control), touch targets ≥ 44px |
| 551–801px | Two-column product grids, condensed nav labels |
| 801–1261px | Three-column product grids, full horizontal nav |
| 1261–1681px | Four-column grids, expanded hero imagery |
| ≥ 1681px | Max-width content container with increased whitespace |

This table is a recommendation derived from the presence of matching media-query breakpoints in the CSS bundle, not a measurement of actual rendered layout or interaction behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Static CSS/text extraction only; no rendered DOM, computed styles, or JavaScript-driven states (mega-menu open state, cart drawer, search overlay) were observed.
- Semantic role assignment (e.g., `surface-card`, `hairline`, `disabled-border`) is inferred by matching supplied hex values to plausible UI roles; several colors (e.g., `#fcfbf9`, `#e5e5e5`) had no explicit selector confirming their intended use.
- Typography scale sizes (display-xl, title-md, body-sm, caption, etc.) are proposed; only font-family, and the weight/color/letter-spacing on `h1–h6` and `.button`, were directly confirmed in CSS.
- Spacing and rounded-corner scales are proposed design-system defaults, not extracted from a full ruleset; only `.button` border-radius (4px) and `.panel-header` padding were directly observed.
- Mobile/touch interaction patterns, breakpoint-specific component collapse, and hover/focus states beyond `.button` and pagination were not observed and are marked proposed.
- Custom font availability, licensing, and web-font loading strategy for Poppins were not verified from the supplied evidence.
