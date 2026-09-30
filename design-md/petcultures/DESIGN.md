---
version: alpha
name: "PetCultures"
source_url: "https://petcultures.com"
captured_at: "2026-09-28T09:36:44.987240+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  PetCultures presents a clinical-yet-warm wellness identity built on a deep teal-green
  (#087e67) paired with a dark navy (#002b3e), evoking the "gut health / cultures" science
  narrative without leaning on typical pastel pet-brand cues. Montserrat is the only
  brand-authored sans-serif observed in the CSS font stack and is used here for both
  headline and body roles, since no separate body typeface was distinguished in the
  supplied evidence. A neutral gray scale (#f6f7f8 through #6b7280) supports surfaces,
  hairlines, and secondary text. A light teal (#8ad2d8) is treated as an inferred
  secondary/accent tone that echoes the primary without competing with it. Several
  palette entries (#eb001b, #f79e1b, #ff5f00, #0071ce, #007aff, #142fbd, #1532cb,
  #1990c6, #136f99) match common third-party payment-badge colors (e.g., card-network
  marks) rather than brand-authored tokens; they are excluded from role assignment
  below and should not be treated as PetCultures brand colors. Button typography,
  border-radius, and letter-spacing (0.025em) are grounded directly in the `.btn`
  ruleset; most component sizing, elevation, and card treatments are proposed
  extrapolations consistent with a Shopify-templated supplement DTC storefront, not
  measured page renders.

colors:
  primary: "#087e67"
  primary-accent: "#8ad2d8"
  ink: "#002b3e"
  canvas: "#ffffff"
  body: "#232323"
  muted: "#6b7280"
  hairline: "#e5e7eb"
  surface-soft: "#f6f7f8"
  surface-card: "#ffffff"
  surface-alt: "#f1f1f1"
  border-strong: "#a0abb5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
typography:
  display-xl: {fontFamily: "Montserrat, sans-serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: "36px", fontWeight: 700, lineHeight: "40px", letterSpacing: "0em"}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.4, letterSpacing: "0em"}
  body-md: {fontFamily: "Montserrat, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: "24px", letterSpacing: "0em"}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0em"}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.02em"}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1.5, letterSpacing: "0.025em"}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    accent: "{colors.primary}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.primary-accent}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  subscription-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.primary}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.base}"

## Components

**button-primary** is the core commerce action (Add to cart, Checkout, Find Their Formula) using the observed `.btn` background/border/color variable pattern with the measured 0.025em letter-spacing; the teal primary is proposed for these variables since actual hex values were not resolvable from custom properties.

**button-secondary** mirrors `.btn--secondary`'s structural pattern (distinct background/border/foreground variables) as an outlined, lower-emphasis variant for actions like "Explore the Science."

**text-input** is a proposed field style for account, subscription-management, and checkout forms; hairline border and soft radius are consistent with the neutral gray palette but not directly observed as an input rule.

**nav-bar** represents the persistent header with Home / Shop / Formula Technology / Manage Subscription / About us links and the USD|EN locale switcher noted in the page text; a light canvas background with hairline underline is proposed, not confirmed via header-specific CSS.

**product-card** models the repeated formula tiles (Skin & Coat, Hip & Joint, Daily Probiotic, Calming) shown with price and star-rating count; card chrome (radius, hairline border, padding) is proposed from the general neutral palette.

**hero** covers the rotating homepage panels ("Proactive Wellness Starts in the Gut," "The Veterinarian-Formulated Difference," etc.), each pairing a display headline with a CTA pair; only the h1 typography values are directly observed, spacing and background are inferred.

**footer** groups policy and account links (Contact us, Affiliate, Privacy/Refund/Shipping/Subscription Policy, Terms of Service); a dark-navy treatment is proposed as an inferred brand-anchoring choice, not confirmed as the actual rendered footer background.

**badge** supports the review-count and rating chips ("4.8 (121)") and trust markers ("Vet-Approved," "Made in USA," "90-day money-back guarantee") seen in the philosophy section; pill shape and soft background are proposed.

**subscription-selector** is a category-specific proposed component for the "Manage Subscription" flow and the "buy 2+ for free shipping" incentive referenced in the cart copy, using an active/inactive toggle pattern typical of supplement subscription commerce; no subscription-widget markup was present in the supplied CSS.

## Responsive Behavior

Recommended (not measured) breakpoints: mobile ≤640px, tablet 641–1024px, desktop ≥1025px. Nav collapses to a hamburger/drawer below tablet; product-card grids move from 1-column (mobile) to 2-column (tablet) to 3–4-column (desktop). Touch targets on button-primary/secondary and subscription-selector should maintain a minimum 44px height. Hero panels stack copy above imagery on mobile. This section is a proposed responsive strategy only; no actual mobile rendering or breakpoint CSS was present in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

Color and typography variables in the source CSS (`--color__background-primary`, `--type__font-body-family`, etc.) are indirected through custom properties whose resolved values were not present in the supplied evidence; role assignments (primary, ink, canvas, etc.) are inferred from the raw observed hex palette, not confirmed variable output. Several palette entries strongly resemble third-party payment-icon colors and were deliberately excluded from brand role mapping. Only `h1` font-size/line-height and `.btn` letter-spacing/line-height are directly observed typography values; all other type sizes are proposed. No interaction states (hover, focus, disabled), mobile layout, or actual component screenshots were observed — all component visuals are proposed patterns consistent with a Shopify-based supplement storefront. Montserrat's licensing/self-hosting status was not verified from the supplied evidence; it is treated as an observed font-family declaration only.
