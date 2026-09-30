---
version: alpha
name: "Sassy Baby"
source_url: "https://sassybaby.com"
captured_at: "2026-09-28T09:07:33.721798+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Sassy Baby's storefront CSS centers on a bright teal (#00a2af) used for body text color, links, and interactive states, paired with a pure white canvas. Titles render in Nunito at 800 weight, while body and UI text use Nunito at regular weight — no secondary typeface is present in the evidence, so sans-serif is retained as the sole fallback. The palette includes soft teal tints (#f0f9fa, #ebf5fa, #f4f6f8) that are inferred as card and section backgrounds, alongside a deep purple (#230051) and coral (#f26d79) that appear only as raw values without confirmed usage — these are treated here as secondary/accent roles for badges or highlights, consistent with a playful, sensory-toy brand. Grays (#333333, #888888, #dddddd) are mapped to body copy, muted text, and hairlines respectively, though their exact application was not directly observed in a labeled rule. The interpretation favors rounded, soft-edged components (pill buttons, rounded cards) to reflect the checkout button's 25px radius and the slick-dots' fully rounded indicators, extended here as a general design language for a friendly infant/toddler toy brand. All semantic role assignments beyond directly quoted CSS are explicitly inferred.

colors:
  primary: "#00a2af"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#888888"
  hairline: "#dddddd"
  surface-soft: "#f0f9fa"
  surface-card: "#f4f6f8"
  on-primary: "#ffffff"
  accent-purple: "#230051"
  accent-coral: "#f26d79"
  accent-yellow: "#ffe607"
  border-soft: "#ccecef"
  teal-deep: "#001416"
  overlay-scrim: "#0000004d"
typography:
  display-xl: {fontFamily: "Nunito, sans-serif", fontSize: 48px, fontWeight: 800, lineHeight: 1.2em, letterSpacing: 0em}
  display-md: {fontFamily: "Nunito, sans-serif", fontSize: 32px, fontWeight: 800, lineHeight: 1.2em, letterSpacing: 0em}
  title-md: {fontFamily: "Nunito, sans-serif", fontSize: 22px, fontWeight: 800, lineHeight: 1.2em, letterSpacing: 0em}
  body-md: {fontFamily: "Nunito, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6em, letterSpacing: 0em}
  body-sm: {fontFamily: "Nunito, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.6em, letterSpacing: 0em}
  caption: {fontFamily: "Nunito, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5em, letterSpacing: 0em}
  button-md: {fontFamily: "Nunito, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.15em, letterSpacing: 0em}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.primary}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.primary}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.border-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  development-stage-tag:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components
**button-primary** is proposed as the primary teal call-to-action (e.g. "shop now," "sign up"), using the observed pill-shaped checkout button radius (25px, mapped to `rounded.full`) and the site's dominant teal color as background with white text.

**button-secondary** is a proposed outline variant for lower-emphasis actions such as "learn more," reusing the same teal on a white background to maintain a light, approachable feel consistent with the brand's soft palette.

**text-input** covers search and newsletter signup fields ("Email address / Sign up"), styled with a light hairline border and soft rounding; exact input styling was not directly observed and is inferred from general form conventions.

**nav-bar** represents the header navigation containing "Discover, Shop, Search, Log in" links seen in the page text; a white background with teal text/links is inferred from the global `body { color:#00a2af }` rule, though header-specific CSS was not isolated in evidence.

**product-card** is proposed for best-seller listings (e.g. "Stacks Of Circles Ring Stacker $15.00"), using a soft tinted background to visually group product image, title, and teal-colored price against the white page canvas.

**hero** models the homepage banner area introducing sensory/STEM messaging, using a soft teal-tinted background (`surface-soft`) with large bold Nunito display type and a primary CTA button; exact hero markup was not present in the supplied CSS and is proposed.

**footer** reflects the observed footer content structure (Company, Information, Crown Crafts Family of Brands, social links), styled plainly on white with muted body text and teal links, consistent with `.plain-link { color:inherit }` behavior.

**badge** is a proposed small pill label (e.g. "New," "Best Seller") using the observed yellow accent (#ffe607) for visual pop against the mostly teal/white palette; no badge component was directly observed in the CSS.

**search** models the "Search our store" overlay referenced in the page text, using a soft background and full rounding to match the pill aesthetic seen elsewhere (slick dot and checkout button radii).

**development-stage-tag** is a category-specific proposed component for labeling toys by developmental stage (e.g. "Tummy Time," "STEM," age range), using the deep purple accent color to differentiate from primary teal CTAs; this pattern is inferred from the site's stage-based navigation taxonomy, not from observed component CSS.

## Responsive Behavior
The following breakpoint table is a recommendation based on common ecommerce patterns and is not derived from measured site behavior:

| Breakpoint | Width | Nav | Product Grid |
|---|---|---|---|
| Mobile | <640px | Collapsed hamburger menu | 1–2 columns |
| Tablet | 640–1024px | Condensed horizontal nav | 2–3 columns |
| Desktop | >1024px | Full horizontal nav with dropdowns | 4+ columns |

Touch targets should maintain a minimum 44×44px hit area, matching the observed `--shopify-accelerated-checkout-button-block-size: 44px` variable. Navigation collapse behavior, carousel touch interactions (slick), and modal transitions were not observed in static CSS and should be treated as proposed only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is derived from static CSS extraction and a page-text excerpt; no rendered layout, computed styles, or responsive breakpoints were directly observed. Several palette colors (e.g. #230051, #f26d79, #ffe607, #3e5c9a) appear as raw hex values without an associated selector, so their semantic roles (accent, badge, error, success) are inferred rather than confirmed. Component structures — hero, product-card, nav-bar, footer — are proposed based on common ecommerce conventions and the page-text content, not extracted from labeled markup. Typography sizes beyond the observed 100%/1.15em (form elements) and 1.2em/1.6em (titles/body) line-heights are proposed estimates, as no explicit `font-size` values were present in the supplied CSS rules. Interaction states (hover, focus, active, disabled) beyond `.plain-link:hover { opacity:.8 }` were not observed. Mobile/tablet layout behavior was not present in evidence. Nunito's availability, hosting source, and licensing terms were not verified from the supplied CSS.
