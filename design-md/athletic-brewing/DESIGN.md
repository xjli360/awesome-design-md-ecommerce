---
version: alpha
name: "Athletic Brewing"
source_url: "https://athleticbrewing.com"
captured_at: "2026-09-28T04:33:30.885246+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Athletic Brewing's storefront CSS centers on a deep navy (#003a5d) as the core
  foreground, link, and badge color, paired with warm neutrals (#ffffff canvas,
  #414042 body copy) and a bright yellow (#ebd923/#ffc629) used for primary
  call-to-action buttons and badge accents. A rotating set of saturated product-card
  backgrounds (coral #fe696d, amber #d09910, orange #ff9432, green #abce5b) signals
  flavor variety across the catalog, while cream (#f6e6d9) and red (#dc584e) appear
  in secondary button and hover treatments on marketing blocks. Typography draws on
  Barlow Condensed for compact, athletic display headlines, Barlow for body and UI
  text, and Caveat as an inferred handwritten accent for callouts or signature-style
  marketing copy — none of these usages are directly measured, only inferred from
  the declared font stack. Root body copy uses a wide letter-spacing (.06rem),
  suggesting an athletic, all-caps-friendly voice for labels and buttons. This
  interpretation proposes a clean, high-contrast e-commerce system: navy-and-white
  base chrome, yellow as the primary action color, and the secondary palette reserved
  for badges, flavor tags, and hover states — all sizes and semantic role names beyond
  the literal CSS variables are proposed, not observed.

colors:
  primary: "#003a5d"
  ink: "#414042"
  canvas: "#ffffff"
  body: "#414042"
  muted: "#d9d9d9"
  hairline: "#dedede"
  surface-soft: "#f7fbfc"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#ebd923"
  accent-gold: "#ffc629"
  accent-teal: "#41c3d6"
  accent-coral: "#fe696d"
  accent-orange: "#ff9432"
  accent-green: "#abce5b"
  accent-cream: "#f6e6d9"
  accent-cream-hover: "#eccbb0"
  danger: "#dc584e"
  danger-dark: "#ce3429"
  olive: "#3c422e"
  navy-hover: "#001a2a"
typography:
  display-xl: {fontFamily: "Barlow Condensed, sans-serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "Barlow Condensed, sans-serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Barlow, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Barlow, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.6px}
  body-sm: {fontFamily: "Barlow, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.4px}
  caption: {fontFamily: "Barlow, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "Barlow Condensed, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 1px}
  script-accent: {fontFamily: "Caveat, cursive", fontSize: 24px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
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
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    hover:
      backgroundColor: "{colors.accent-gold}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    hover:
      backgroundColor: "{colors.navy-hover}"
      textColor: "{colors.on-primary}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
    focus:
      borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    accentBackground: "{colors.accent-coral}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    shadowColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    primaryAction: "button-primary"
    secondaryAction: "button-secondary"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderColor: "{colors.navy-hover}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.primary}"
  age-verification-modal:
    backgroundColor: "{colors.canvas}"
    overlayColor: "{colors.ink}"
    textColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    confirmAction: "button-primary"
    declineAction: "button-secondary"

## Components

**button-primary** uses the yellow (#ebd923) fill with navy text observed directly in the hero banner CSS variables, intended for the storefront's main conversion actions (Shop, Add to Cart). Hover darkens to #c9b812 per the observed hover rule.

**button-secondary** is proposed as a navy-outline, white-fill inverse of the primary button, matching the `--button-secondary-color:#003a5d` pattern seen in banner sections; hover state (navy-hover) is inferred from the observed #001a2a hover token.

**text-input** is a proposed form field using the light surface-soft tint for a soft, non-white field background with a hairline border, focusing to full navy — this pattern is not directly observed but is consistent with the brand's navy-primary system.

**nav-bar** is proposed as a white header bar with navy wordmark/links, matching the root `--color-link` and `--color-foreground` values; exact height, sticky behavior, and mobile collapse are not observed.

**product-card** reflects the observed per-product background-color overrides (coral, amber, orange, green) applied to `.card__inner` elements, suggesting each product/flavor gets a distinct accent tile; card shadow, radius, and title styling are proposed defaults.

**hero** is proposed as a full-width navy section with white text and the display-xl headline style, using the button-primary/secondary pair exactly as configured in the observed banner template, though full hero layout is not confirmed.

**footer** is proposed as a navy band with white text/links, reusing the primary/on-primary pair for brand consistency; content structure (columns, newsletter form) is not observed.

**badge** reflects the observed `--color-badge-*` variables (white background, navy foreground and border), likely used for "Athletic Club" or product certification badges referenced in the page title.

**search** is a proposed lightweight input pattern styled consistently with text-input, using navy iconography; no search-specific selectors were present in the evidence.

**age-verification-modal** is a category-appropriate proposed component for a beverage DTC site, using the canvas/navy pairing and button components already defined; no age-gate markup was present in the supplied evidence, so this is entirely proposed for category fit.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <600px | Single-column product grid, collapsed nav into hamburger (proposed) |
| Tablet | 600–959px | 2-column product grid, condensed nav links |
| Desktop | 960–1279px | 3–4 column product grid, full nav bar |
| Wide | ≥1280px | Max-width container, generous section padding ({spacing.section}) |

Touch targets should be at least 44×44px for buttons and nav items (proposed, standard accessibility guidance). Navigation is expected to collapse into a drawer or hamburger menu below tablet width; this collapse behavior was not observed in the supplied CSS and is a UX recommendation only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS extraction only; no live page render, interaction states (hover/focus/active beyond the few explicitly declared), or JavaScript-driven behavior (cart drawer, age gate, mobile nav) were observed. Font sizes for most typography tokens are proposed conventions, not measured values — only the body element's `font-size: 1.5rem` and `letter-spacing: .06rem` were directly observed, and the effective pixel scale depends on an unconfirmed root font-size. The semantic mapping of colors (e.g., "primary," "muted," "hairline") is an inferred simplification of numerous raw CSS custom properties and per-product override colors; several palette entries (e.g., teal #41c3d6, purple #9877d0, magenta #f27ea1) appear in the supplied palette but have no confirmed selector role and were omitted from the token set. Caveat's actual usage on the site was not observed in any provided selector and is included only because it appears in the font stack. Custom font licensing and self-hosting/CDN availability for Barlow, Barlow Condensed, and Caveat were not verified. Component definitions beyond button-primary, button-secondary (banner-scoped), and product-card background overrides are proposed patterns for a DTC beverage storefront and should be validated against the live site before implementation.
