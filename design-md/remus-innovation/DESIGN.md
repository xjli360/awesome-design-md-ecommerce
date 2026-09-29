---
version: alpha
name: "Remus Innovation"
source_url: "https://remus.eu"
captured_at: "2026-09-28T10:00:39.277007+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  The extracted evidence shows a high-contrast, editorial system built on a
  near-black ink (#000000/#161516/#212121) against a white canvas (#ffffff),
  with a warm off-white surface (#f5f3f3) and a light gray hairline (#c6c1c2)
  for card and section separation. A single saturated red (#e52421) appears
  as the standout accent among the CSS custom properties and is proposed
  here as the primary brand/action color, consistent with a performance
  exhaust brand; its role as "the" brand red is inferred from prominence in
  the palette list, not from a confirmed CTA screenshot. A muted plum-gray
  (#454048) and a softer coral (#e1615f) are treated as secondary/supporting
  tones. Typography is built entirely on the single observed custom font
  family, "gtAmerica" (declared via the --font-gt-america CSS variable),
  used across all body, headline, button and caption utility classes found
  in the stylesheet; no other proprietary family was observed. Font weights
  400/500/700 are confirmed via CSS custom properties. Sizing for body-sm
  (14px/22px) and body-md (16px/24px) is directly observed; larger display
  sizes are proposed extrapolations in the absence of captured heading
  rules. Rounded and spacing scales are proposed conventions, not measured.

colors:
  primary: "#e52421"
  ink: "#161516"
  canvas: "#ffffff"
  body: "#212121"
  muted: "#454048"
  hairline: "#c6c1c2"
  surface-soft: "#f5f3f3"
  surface-card: "#f8f7f7"
  on-primary: "#ffffff"
  accent-coral: "#e1615f"
  danger: "#b71d1a"
  overlay-dark: "#00000099"
  overlay-light: "#ffffff99"
typography:
  display-xl: {fontFamily: "gtAmerica, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "gtAmerica, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "gtAmerica, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-lg: {fontFamily: "gtAmerica, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.625rem, letterSpacing: 0px}
  body-md: {fontFamily: "gtAmerica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5rem, letterSpacing: 0px}
  body-sm: {fontFamily: "gtAmerica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.375rem, letterSpacing: 0px}
  caption: {fontFamily: "gtAmerica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "gtAmerica, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.2px}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlayColor: "{colors.overlay-dark}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-lg}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    hairlineColor: "{colors.muted}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  vehicle-fitment-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components
**button-primary** uses the observed red (#e52421) as a solid fill with white text, intended for primary calls to action such as "Find a Dealer" or "Discover" links; hover/active states are proposed, not observed. **button-secondary** is an outlined variant for lower-emphasis actions, sharing the same red for border/text on a white background. **text-input** proposes a hairline-bordered field matching the light gray (#c6c1c2) divider tone seen in the palette, for use in dealer-locator or B2B portal forms. **nav-bar** is inferred from the presence of `--spacing-navbar-padding` custom properties differentiating B2B/B2C store types; it assumes a white bar with dark text and a hairline bottom border. **product-card** models the exhaust product tiles referenced by the `.group-hover/product-summary:scale-105` utility class (a proposed hover zoom on product imagery), set on a soft off-white card surface. **hero** reflects the large "Break Silence" landing banner described in the text excerpt, using a dark ink background with white type for high-contrast automotive photography overlays; exact overlay opacity is proposed. **footer** mirrors the dark ink treatment for global site chrome consistency, given the deep near-black colors present in the palette. **badge** proposes a pill-shaped red label for tags like "Now available!" or "New," a pattern common to product-news callouts referenced in the excerpt but not confirmed via captured markup. **search** is a proposed lightweight input for header or menu search, styled with the off-white surface tone. **vehicle-fitment-selector** is a category-appropriate proposed component for selecting car/motorcycle make-model-exhaust compatibility, a standard pattern for performance-exhaust e-commerce, styled with the neutral card surface and hairline border; its structure is not present in the supplied CSS and is entirely inferred from category norms.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width      | Layout notes (proposed) |
|-----------|------------|--------------------------|
| xs        | <480px     | Single-column stack; nav collapses to hamburger menu |
| sm        | 480–767px  | Product cards 1-up; hero text stacks over media |
| md        | 768–1023px | Product cards 2-up; nav shows primary items, overflow in menu |
| lg        | 1024–1439px| Product cards 3-up; full horizontal nav |
| xl        | ≥1440px    | Product cards 3–4 up; max-width content container |

Touch targets should be at least 44×44px for nav items, buttons, and the vehicle-fitment-selector controls. Navigation is assumed to collapse into a slide-out or dropdown menu below the `md` breakpoint, consistent with the "Menu Menu" duplication seen in the extracted text (suggesting a toggled mobile menu state), though this interaction was not directly observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived from static CSS and text extraction only; no rendered page, computed layout, or interaction states were observed. Semantic color roles (primary red, muted plum, surface tones) are inferred from palette position and typical brand usage, not from confirmed element screenshots. All font sizes beyond the two directly observed utility classes (body-sm, body-md) are proposed conventions scaled from those values. Rounded and spacing scales are conventional proposals, not extracted from the CSS. Hover, focus, active, and disabled states for all components are proposed and unverified. Mobile menu behavior, breakpoint values, and touch-target sizing are recommendations only. The custom font "gtAmerica" is referenced via CSS variable but its license, weights availability, and self-hosting terms were not verified from the supplied evidence.
