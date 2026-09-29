---
version: alpha
name: "Tractive"
source_url: "https://tractive.com"
captured_at: "2026-09-28T09:54:17.823087+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is grounded in the Tractive marketing site's extracted CSS: a Poppins sans-serif
  typeface set at a medium (500) body weight, a deep navy-black ink (#121623) for text, a clean white
  canvas, and a saturated blue (#1a73e8) that drives the primary call-to-action button and link states.
  The supplied palette is unusually broad — including pink/red (#b42f4f, #d93856), green (#00b67a,
  #00652d), purple (#4a14a2), tan/orange (#6b3e1e, #fef2e6), and a lime accent (#d6ff70) — consistent
  with a product line that uses color-coded imagery per species/product (dogs, cats) and rating badges
  (e.g., a Trustpilot-style green). Because static extraction cannot confirm which colors are decorative
  photography artifacts versus true UI tokens, only the blue primary, white/near-white surfaces, the
  navy ink, and the neutral grey/border ramp are treated as confirmed UI roles; the red, green, purple,
  tan, and lime hues are mapped as secondary/accent tokens for badges, alerts, and category tagging,
  explicitly inferred rather than confirmed as buttons or nav elements. Rounded pill buttons (25rem
  radius) are observed directly; other corner radii are proposed conventions. Spacing follows the site's
  responsive gutter/margin-section custom properties, converted to a conventional 4px-based scale.

colors:
  primary: "#1a73e8"
  ink: "#121623"
  canvas: "#ffffff"
  body: "#464b5a"
  muted: "#5c606e"
  hairline: "#e3e4ea"
  surface-soft: "#f5f5fa"
  surface-card: "#e8f1fc"
  on-primary: "#ffffff"
  border-strong: "#c0c2ca"
  accent-danger: "#b42f4f"
  accent-danger-soft: "#fbe4e9"
  accent-success: "#00b67a"
  accent-purple: "#4a14a2"
  accent-purple-soft: "#f3ecff"
  accent-tan-soft: "#fef2e6"
  accent-lime: "#d6ff70"
  link-hover: "#155cba"
  focus-ring: "#76abf1"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.17, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.17, letterSpacing: -0.25px}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.33, letterSpacing: 0px}
  body-md: {fontFamily: "Poppins, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Poppins, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Poppins, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.33, letterSpacing: 0.1px}
  button-md: {fontFamily: "Poppins, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.5, letterSpacing: 0px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  tracker-configurator:
    backgroundColor: "{colors.canvas}"
    accentColor: "{colors.primary}"
    optionBorderColor: "{colors.hairline}"
    optionSelectedBorderColor: "{colors.primary}"
    priceTypography: "{typography.title-md}"
    labelTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** is the solid blue pill CTA (`#1a73e8`, `border-radius: 25rem` confirmed in CSS) used for "Shop Now" and "Activate Tracker" actions; a `:disabled` state with grey background/text is observed directly.

**button-secondary** mirrors the white-background, grey-border pill (`border:1px solid #5c606e`) with an observed hover state that shifts to a light-blue fill (`#d1e3fa`) and blue border — likely used for tab toggles like "Dog / Cat" selectors.

**text-input** is proposed for search/account/email fields; no direct input styling was captured, so border, radius, and padding follow the neutral hairline and spacing scale as a reasonable convention for a Poppins-based form field.

**nav-bar** represents the top navigation bar containing the logo, mega-menu categories (Dogs, Cats, Pricing, Accessories), account/cart icons, and the cart-count badge; layout and collapse behavior are inferred from menu content, not measured.

**product-card** is proposed for tracker listing tiles (e.g., DOG 6, DOG 6 XL, CAT 6 Mini), using a soft blue-tinted card surface to visually separate product tiles from the white page background, with title/body typography drawn from observed heading and body tokens.

**hero** models the dark full-bleed banner pattern implied by white-on-dark hero copy ("Say Hello to the Future of Pet Care") and the `.button--transparent-dark` / `.button--primary-dark` variants, which only make sense over a dark background.

**footer** is proposed as a dark ink-background block for legal/nav links, reusing the same ink token seen on `body`/hero contexts; specific footer markup was not present in the supplied evidence.

**badge** captures the small pill count/label pattern directly observed on the cart icon (`.icon-button--cart span`, pink-red `#b42f4f`), reused generically for "New" or notification badges.

**tracker-configurator** is a category-specific component modeling the product page's device/color/battery selector UI implied by the excerpt (model switch, color swatches, price update); this pattern is proposed from content structure, not from captured component CSS.

## Responsive Behavior
Recommended breakpoints (not measured, inferred from the site's `--breakpoint-*` custom properties): `sm` 640px, `md` 768px, `lg` 1024px, `xl` 1280px. Below `md`, the nav-bar should collapse into a hamburger/menu-drawer pattern and the tracker-configurator should stack selector and price vertically. Touch targets for buttons and icon-buttons should maintain a minimum 44×44px hit area regardless of the visually smaller `1.5rem` icon-button box observed in CSS. Section vertical padding should scale down using the smaller `--margin-section`/`--wide-section-padding` values (1.25rem–2.5rem) captured at narrower breakpoints, expanding to the larger set (3.5rem/5rem) at `lg`+. This section is a recommendation only; no actual responsive/mobile layout was observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties, a limited rule sample, and page text, not a rendered or interactive audit. The split between `ink` (headings) and `body` (paragraph) colors is an inferred semantic distinction; both may resolve to the same `#121623` in production. Which of the many extracted hues (green, purple, tan, lime) map to specific UI roles (ratings, promo banners, category tags) versus incidental photography/background colors is uncertained and treated as accent-only. Rounded corner values other than the confirmed pill (`9999px`) button radius are proposed, not observed. All spacing tokens beyond the captured gutter/margin-section rem values are conventional approximations. No hover, focus, active, error, or mobile-menu states were observed beyond the two documented button/link hover rules. Font availability, licensing, and whether Poppins is self-hosted or a Google Fonts embed were not verified. No component screenshots or DOM structure were available to confirm actual card, nav, or footer markup.
