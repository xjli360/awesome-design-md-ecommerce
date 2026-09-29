---
version: alpha
name: "Native Pet"
source_url: "https://nativepet.com"
captured_at: "2026-09-28T09:04:59.712748+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Native Pet's storefront evidence centers on a Shopify theme with CSS custom
  properties defining a bright, clinical-but-playful palette: a saturated
  brand blue (#155dd7) used as `--color-foreground` for text, links and
  shadow, paired with a lime-green (#deff5b) used as `--color-button`
  background and white (#ffffff) as the base canvas. The review-widget
  variables (oke-*) confirm a secondary navy (#24364b) for primary body copy
  and a muted slate (#676986) for secondary/meta text, plus a light border
  gray (#e5e5eb). The wider observed swatch array (pale blues, corals,
  yellows, greens) is treated as inferred supporting/badge colors since no
  selector ties them to specific roles; they likely back concern-category
  tags, star ratings, and sale badges seen in the product grid. Typography
  draws on three observed families — Adieu (buttons, likely headline/display
  use), F37 Ginger Soft (a rounded, friendly candidate for body/title text),
  and Suisse Intl Mono (a technical mono, inferred for labels/captions like
  review counts or SKU-style text) — each with system sans-serif/monospace
  fallbacks. The interpretation favors a rounded, high-contrast CTA system
  (pill buttons, 100px radius confirmed by oke-button-borderRadius) suited to
  a friendly, trustworthy pet-health brand.

colors:
  primary: "#deff5b"
  on-primary: "#155dd7"
  ink: "#155dd7"
  body: "#24364b"
  muted: "#676986"
  canvas: "#ffffff"
  hairline: "#e5e5eb"
  surface-soft: "#e2f5fa"
  surface-card: "#fafafa"
  danger: "#ef3340"
  success: "#04b26e"
  accent-highlight: "#ffcf2a"
typography:
  display-xl: {fontFamily: "Adieu, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Adieu, sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "F37 Ginger Soft, sans-serif", fontSize: "20px", fontWeight: 500, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "F37 Ginger Soft, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "F37 Ginger Soft, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Suisse Intl Mono, monospace", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.5px"}
  button-md: {fontFamily: "Adieu, sans-serif", fontSize: "14px", fontWeight: 300, lineHeight: 1, letterSpacing: "0px"}
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
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-highlight}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  quiz-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components
**button-primary** uses the confirmed `--color-button`/`--color-button-text` pair (lime on blue-text) with a fully rounded pill shape, matching the 100px radius seen on the review-widget button tokens; hover/active states are proposed, not observed. **button-secondary** inverts to a white background with blue border/text, inferred from `--color-secondary-button` variables for lower-emphasis actions like "Add to Cart" alternates. **text-input** is a proposed neutral field using the observed hairline border color for forms such as the newsletter/Klaviyo signup. **nav-bar** reflects the sticky header behavior implied by `.header-section` transitioning from transparent to white background on scroll (`data-state='sticky'`), with brand-blue text once solid. **product-card** is inferred from the product-grid content (title, star rating, price range) using a soft off-white card surface for visual separation. **hero** proposes a light-blue tinted section (from the pale palette swatches) to host the rotating hero carousel (`data-carousel='hero-carousel'`) confirmed in CSS. **footer** is a proposed dark-ink block for contrast and closure, not directly observed in supplied rules. **badge** covers "best seller"/"new!" labels seen in the product excerpt, using a yellow accent pill — color role inferred from the broader swatch set. **search** is a pill-shaped proposed pattern consistent with the button radius language. **quiz-banner** is a category-appropriate component for the "Take the Quiz + $5 off" funnel prominent in the page content, styled as a high-contrast CTA block using the primary lime/blue pairing.

## Responsive Behavior
Recommended breakpoints (not measured): mobile ≤599px, tablet 600–959px, desktop ≥960px, wide ≥1440px. Nav collapses to a hamburger/off-canvas menu below tablet, consistent with the `html[data-menu='open']` state hook found in CSS. Touch targets should be a minimum 44×44px for buttons and badges. Product grids likely reflow from a multi-column desktop layout to 1–2 columns on mobile; the reviews carousel (`--slide-size` variables) suggests horizontal scroll/snap on narrow viewports. This section is a recommendation only, not observed site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/token extraction and a text excerpt, not a rendered browser session — no live layout, animation, hover state, or actual mobile breakpoint was observed. Color-to-role mapping beyond the explicit `:root` and `oke-*` variables (e.g., which of the ~40 additional palette swatches map to specific badges, category tags, or icons) is inferred from plausibility, not confirmed selectors. Spacing and rounded scales beyond the confirmed `100px`/pill radius are proposed conventions, not measured values. Font availability, weights, and licensing for Adieu, F37 Ginger Soft, and Suisse Intl Mono were not verified; fallbacks are generic. Component states (hover, focus, disabled, error) are proposed patterns only.
