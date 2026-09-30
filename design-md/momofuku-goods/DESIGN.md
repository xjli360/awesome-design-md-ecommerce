---
version: alpha
name: "Momofuku Goods"
source_url: "https://shop.momofuku.com/"
captured_at: "2026-09-29T04:11:19.395863+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Momofuku Goods is David Chang's direct-to-consumer pantry line (chili crunch,
  seasoned salts, noodles, and new sauces), presented on the shop.momofuku.com
  storefront. The observed palette is dominated by warm, food-photography-friendly
  neutrals: a cream canvas ("#faf7ee"), a deeper egg-yolk cream card surface
  ("#faebc8"), near-black text and borders ("#000000"), and a muted gray for
  secondary copy ("#737373"). A small set of saturated accents appear in
  promotional and review-widget CSS: a chili-red ("#8e0606"), a turmeric gold
  ("#f6a71b"), a burnt-orange ("#f76c20"), and a herb green ("#387e3b") used as
  an "active" state on category filter pills. Two font families are named in
  loaded-font selectors: "Graphik" (body/UI) and the more distinctive
  "MomoSharpie" (likely a hand-drawn display face for hero/marketing headlines).
  Card and button treatments observed in component CSS favor bold 2px black
  borders, uppercase bold labels, and small pill/rounded-corner radii rather
  than soft rounding, giving a stamped, market-label feel appropriate to a
  condiments brand. Sizes, spacing scale, and most semantic color-role
  assignments below are inferred/proposed from this evidence, not measured
  from rendered layout.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#232323"
  muted: "#737373"
  hairline: "#dddddd"
  surface-soft: "#faf7ee"
  surface-card: "#faebc8"
  on-primary: "#ffffff"
  accent-chili: "#8e0606"
  accent-gold: "#f6a71b"
  accent-orange: "#f76c20"
  accent-green: "#387e3b"
  border-strong: "#000000"
typography:
  display-xl: {fontFamily: "MomoSharpie, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Graphik, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Graphik, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px, textTransform: uppercase}
  body-md: {fontFamily: "Graphik, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5}
  body-sm: {fontFamily: "Graphik, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5}
  caption: {fontFamily: "Graphik, sans-serif", fontSize: 12px, fontWeight: 600, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Graphik, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.0, letterSpacing: 0px, textTransform: uppercase}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    border: "2px solid {colors.border-strong}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: button-primary
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    linkColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  flavor-filter-pill:
    backgroundColor: "{colors.surface-card}"
    activeBackgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    border: "1px solid {colors.border-strong}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"

## Components
**button-primary** is the black, uppercase, bold-weight call-to-action seen in promotional-module CSS (e.g. "SHOP NOW", "LEARN MORE"), using solid black fill and white text with a small corner radius rather than a pill, matching the stamped-label aesthetic.

**button-secondary** proposes a cream-on-black-border variant for lower-emphasis actions (e.g. "shop all" links inside carousels), reusing the observed cream card color so it reads as part of the same panel rather than a competing surface.

**text-input** is a proposed field style (newsletter email capture, account/search forms) using a light hairline border on white, since no distinct input styling was present in the supplied CSS.

**nav-bar** is inferred from the text navigation list (Bundles, Chili Crunch, Noodles, New! Sauces, Shop All) — a white bar with black uppercase-adjacent links and a thin bottom hairline; exact spacing/height is proposed.

**product-card** reflects the one concretely observed card pattern: a cream ("#faf7ee") background bordered top/bottom/right in 2px black, implying a thick-black-outline grid module used for the featured-product carousel; left border is proposed as symmetric.

**hero** models the top banner/carousel ("Your new go-to squeeze," "Get our first batch") as a full-width cream-card-colored panel with a large display headline and a primary CTA; actual hero height/imagery layout is not observed, only its color and copy pattern.

**footer** is inferred from the plain-text link list (Store Locator, Wholesale, FAQ, Contact, Gifting, Careers, Terms, Privacy) — a light background with muted gray text and black links, spacing proposed.

**badge** is a proposed small pill (e.g. "NEW") using the gold accent, since gold/orange tones appear in the palette but no explicit badge selector was supplied.

**search** is proposed for a product search affordance, styled consistently with text-input; no search-specific selector was present in the evidence.

**flavor-filter-pill** directly reflects the observed `ProductCarousel-category-button` styles: cream fill with a black 1px border in its default state, switching to solid green fill with white text when `.is-active`, used to filter the carousel by category (e.g. Chili Crunch vs. Noodles vs. Sauces).

## Responsive Behavior
Recommended, not measured, breakpoints:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <480px | Single-column hero/product-card stacks; nav collapses to a hamburger/off-canvas menu (proposed). |
| Tablet | 480–1024px | 2-column product grid; carousel shows partial next-card peek. |
| Desktop | >1024px | Full nav bar links visible; multi-card carousel; hero at full bleed width. |

Touch targets for buttons and filter pills should maintain a minimum ~44px hit area even where visual padding is smaller (some observed CSS uses fixed 1.25rem icon buttons, which is below this minimum and should be expanded via invisible padding on touch). Category filter pills and carousel arrows should remain horizontally scrollable/swipeable on narrow viewports. This section is a design recommendation only; no live responsive behavior was captured.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from static CSS/text extraction only — no rendered screenshots, computed layout, or DOM interaction were observed, so exact spacing, grid columns, and breakpoints are proposed, not measured. Color-role assignments (e.g., which palette hex is "primary" vs. an incidental widget color from the Junip reviews integration) are inferred from selector context and may not match the brand's actual internal design tokens. "MomoSharpie" is named only via a `.fonts-loaded` selector; its glyph design, weight range, and licensing/availability for reuse are unverified. Interaction states (hover, focus, disabled) beyond the one `.is-active` filter example were not present in the supplied evidence and are marked proposed. Mobile/tablet layout, navigation collapse behavior, and cart/checkout UI were not observed at all and are extrapolated from general e-commerce conventions.
