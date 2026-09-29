---
version: alpha
name: "Ritual Zero Proof"
source_url: "https://ritualzeroproof.com"
captured_at: "2026-09-28T05:01:53.468749+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Ritual Zero Proof's evidence is dominated by a near-black ink (#161a14) used
  as the primary text and border color across the review/loyalty widget CSS,
  paired with white canvas and a teal accent (#17af9c) that appears as the
  loyalty-widget trigger, lead color, and "EARN POINTS" headline color —
  treated here as the brand's primary accent since it is the only saturated
  hue tied to functional UI. Slate gray (#676986) appears for secondary
  review-helper text and is mapped to a muted role. Light neutrals
  (#dddddd, #f8f8f8, #f4f4f6) are inferred for hairlines and soft/card
  surfaces, as no explicit background-surface rule was observed. Typography
  draws on "Avenir Next" and "Avenir Next Condensed" (confirmed in loyalty
  and button rules at 13–48px, weights 400–700) for UI text and buttons, and
  Georgia (confirmed 28px/400) for a serif accent moment. "Figtree",
  "Mission Accomplished", and "Otoiwo Grotesk Ultra Wide" appear only as
  font-family names in evidence with no measured usage, so they are proposed
  cautiously for hero display type, marked inferred pending live confirmation.
  Rounded corners follow the observed 5px button radius; layout spacing is a
  proposed generic scale, not measured.

colors:
  primary: "#17af9c"
  ink: "#161a14"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#676986"
  hairline: "#dddddd"
  surface-soft: "#f8f8f8"
  surface-card: "#f4f4f6"
  on-primary: "#ffffff"
  accent-teal-light: "#d1efeb"
  accent-teal-bright: "#00caaa"
  accent-gold: "#fcd300"
  accent-navy: "#272d45"
  accent-berry: "#96262c"
typography:
  display-xl: {fontFamily: "'Otoiwo Grotesk Ultra Wide', sans-serif", fontSize: 64px, fontWeight: 700, lineHeight: 1.05, letterSpacing: -1px}
  display-md: {fontFamily: "'Avenir Next Condensed', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1, letterSpacing: 0px}
  title-md: {fontFamily: "Georgia, serif", fontSize: 28px, fontWeight: 400, lineHeight: 1, letterSpacing: 0px}
  body-md: {fontFamily: "'Avenir Next', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  body-sm: {fontFamily: "'Avenir Next', sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  caption: {fontFamily: "'Avenir Next', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Avenir Next', sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 22px, letterSpacing: 0.5px}
rounded:
  none: 0px
  xs: 2px
  sm: 5px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  zero-proof-badge:
    backgroundColor: "{colors.accent-teal-light}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.md}"

## Components
**button-primary** uses the confirmed teal accent as a solid fill with white text, sized from the observed 20px/700 button typography and 5px radius seen in the loyalty widget's `--oke-button` variables; proposed as the default add-to-cart and CTA treatment.

**button-secondary** mirrors the outline pattern explicitly observed in `#oke-loyalty-profile .c-button--outline` (ink border, transparent fill, ink text), proposed for lower-emphasis actions like "Learn More" or account links.

**text-input** is proposed using canvas background and a light hairline border; no explicit form-input CSS was captured, so field padding and radius are inferred from general form conventions.

**nav-bar** is proposed as a white bar with ink text and a bottom hairline, reflecting the site's dark-on-light header pattern implied by ink-dominant text colors; the megamenu/cart-drawer structure referenced in page text (Shop, Subscriptions, Recipes, Cart) is not visually confirmed.

**product-card** proposes a slightly-off-white card surface with generous internal padding for bottle imagery, price, and "ADD TO CART" action, consistent with the flavor-line SKUs (Gin/Rum/Whiskey/Agave/Aperitif Alternatives) named in the page content; card elevation/shadow was not observed.

**hero** is proposed as a full-bleed dark (ink) section with large display type, matching the "ENJOY THE RITUAL WITHOUT THE ALCOHOL" campaign copy; the oversized grotesk font is a proposed treatment since its rendered size/weight were not captured.

**footer** uses the ink background with small body-sm text for the multi-column link structure (About, Details, Inquiries, Wholesale) visible in page text; layout columns are proposed, not measured.

**badge** proposes a small pill using the gold accent for merchandising labels (e.g. "NEW", sale price flags like "$32.95 → $29.95"); color choice is inferred, not tied to an explicit badge rule.

**search** is a proposed pill-shaped field using the soft surface tone, since no dedicated search-bar CSS was present in evidence.

**zero-proof-badge** is a category-specific component proposing a light-teal pill to flag "0% ABV / Non-Alcoholic" claims near product titles, reusing the primary teal at reduced saturation (`accent-teal-light`) for a calmer, informational badge distinct from promotional badges.

## Responsive Behavior
Recommended, not measured, breakpoints: mobile ≤480px (single-column product grid, stacked nav collapsing into a hamburger/megamenu), tablet 481–1024px (2-column product grid, condensed nav), desktop ≥1025px (multi-column grid, full horizontal nav with mega-menu). Touch targets should be at least 44×44px for cart/add-to-cart controls, matching the 60px-tall buttons seen in the loyalty widget. Sticky "Add $40 for Free Shipping" and cart-drawer patterns implied by page text should collapse to a bottom sheet on mobile. All breakpoint values and collapse behavior are proposed conventions, not observed layout data.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered page, computed layout, or interaction states (hover, focus, active, mobile menu behavior) were observed. Semantic role mapping (e.g., which gray is "body" vs "muted") is inferred from limited widget-scoped CSS (Okendo reviews, loyalty modal) rather than main site templates. Spacing scale and most typography sizes beyond the explicitly captured 13/14/20/22/28/48px values are proposed, not measured. "Mission Accomplished," "Otoiwo Grotesk Ultra Wide," and "Figtree" appear only as font-family names in evidence with no confirming font-size/weight rule; their actual usage, availability, and licensing are unverified. Component existence (nav-bar, hero, footer, search, product-card) is inferred from page text and generic e-commerce convention, not from captured layout CSS.
