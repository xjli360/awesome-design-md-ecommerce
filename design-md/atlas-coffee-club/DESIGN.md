---
version: alpha
name: "Atlas Coffee Club"
source_url: "https://atlascoffeeclub.com"
captured_at: "2026-09-28T09:26:55.538409+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Atlas Coffee Club's storefront CSS centers on a saturated egg-yolk yellow ("#f9e124") paired with a near-black charcoal ink ("#252323"), evidenced directly in the Tailwind-style button--primary rules (yellow background, dark text, pale-yellow hover state). Body copy is explicitly set in Open Sans with Helvetica/Arial fallbacks across the text-body utility classes, so that mapping is observed rather than assumed. Headline and display fonts (Jost, Barlow, Arsenal, Dancing Script) appear only in the loaded font-family list without a confirmed selector mapping; their assignment to display and title roles below is inferred from typical marketing-site hierarchy and should be treated as proposed, not confirmed.
  The palette also carries a muted, warm-neutral surface family (cream/off-whites like "#fbf7ef" and "#fcfdfc") suited to card and hero backgrounds against the primary yellow, plus semantic greens and corals (success/error states) already wired into button--primary.success and .error variants. A terracotta and a muted teal round out an "explore the world" accent set, appropriate to a globally-sourced coffee brand, though their specific UI usage was not observed and is treated as available accent inventory. Rounded corners and spacing follow a conventional 4/8-based scale inferred from the one confirmed 4px button radius.

colors:
  primary: "#f9e124"
  ink: "#252323"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#7d7d7d"
  hairline: "#dddddd"
  surface-soft: "#fbf7ef"
  surface-card: "#fcfdfc"
  on-primary: "#252323"
  success: "#49865a"
  error: "#e88974"
  accent-terracotta: "#c2410c"
  accent-teal: "#467c99"
typography:
  display-xl: {fontFamily: "Jost, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Jost, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Barlow, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.02em}
  button-md: {fontFamily: "Open Sans, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.1em}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.muted}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  subscription-plan-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.display-md}"
    ctaComponent: "button-primary"

## Components

**button-primary** reflects the observed `.button.button--primary` rule directly: yellow ("#f9e124") background with dark ink text, a 1px border in the same yellow, and a lighter yellow hover state. It is the primary conversion action (Get Started, subscribe CTAs).

**button-secondary** is drawn from the observed `.button--secondary` rule (dark ink background, white text, transitioning to an outlined ink-on-transparent state on hover). Proposed for secondary actions like "Give a Gift" alongside a primary CTA.

**text-input** is a proposed pattern for email capture and account fields; no explicit input styling was present in the supplied CSS, so border color, radius, and padding follow the general 4px/8-based scale inferred from button radii elsewhere on the site.

**nav-bar** is proposed based on standard Shopify header conventions; the supplied evidence shows no nav-specific selectors, so background/text colors are drawn from the safe ink-on-canvas pairing observed in body/button rules.

**product-card** supports coffee-of-the-month and subscription tiles. Background and radius are proposed (no card selector was in the evidence); title/body typography reuse the confirmed Open Sans body stack and inferred display stack.

**hero** models the homepage's "Try coffee from around the world" banner region using the soft cream surface tone and the larger inferred display type scale; exact hero layout and imagery were not present in the CSS evidence.

**footer** uses the dark ink background with canvas text and muted link color, consistent with the newsletter and support-contact content block seen in the page text (email/support/hours/policy links).

**badge** is proposed for the many promotional labels seen in the text excerpt (National Coffee Day, Black Friday, 50% Off, etc.), using the terracotta accent for visual contrast against yellow CTAs; exact badge styling was not in the supplied CSS.

**search** is a proposed pattern; no search UI selectors were supplied, so styling follows the soft-surface, pill-shaped convention common to Shopify storefronts.

**subscription-plan-card** is a category-specific component for "Build Your Plan" (Drip, Pods, French Press, Espresso, Decaf) tier selection, using a yellow-bordered card to echo the brand's primary CTA color and a `button-primary` embedded call to action.

## Responsive Behavior
Recommended breakpoints (not measured from live site): mobile ≤ 480px, tablet 481–1024px, desktop ≥ 1025px. Nav should collapse to a hamburger/off-canvas menu below 1024px; hero and product-card grids should stack to single-column below 768px. Touch targets for buttons and badges should maintain a minimum 44px height. This section is a proposed recommendation only; no interaction or breakpoint behavior was observed in the supplied static CSS/text evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS rules, a color/font inventory, and page text only — no rendered layout, DOM structure, or responsive behavior was observed. Heading/display font assignments (Jost, Barlow, Arsenal, Dancing Script) are inferred from the loaded font list, not from confirmed selector mappings, and their licensing/self-hosting status was not verified. Several component definitions (nav-bar, text-input, product-card, hero, search, badge) are proposed patterns with no matching selectors in the supplied evidence. All spacing and rounded-corner scale values beyond the single confirmed 4px button radius are proposed conventions, not measured. Color-to-role assignments (e.g., surface-soft vs. surface-card, hairline) are best-fit inferences from a flat hex list without confirmed usage context.
