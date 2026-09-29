---
version: alpha
name: "Earthen Shop"
source_url: "https://earthen-shop.com"
captured_at: "2026-09-28T04:38:23.451145+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Earthen Shop's captured CSS reveals a layered stylesheet: a Bootstrap-derived
  utility/alert palette (blues, greens, reds, ambers used for status states)
  sits beneath a smaller set of storefront-specific rules governing a product
  options customizer (po-option, po-font_picker) and a hero slider. The
  customizer rules are the most concrete brand signal observed — near-black
  selection and button states (#000000, #18181b), a warm neutral border
  (#e3e1e1), and a mid-grey hover fill (#555555) against white (#ffffff)
  surfaces — suggesting a restrained, high-contrast neutral aesthetic suited
  to handmade ceramics, where product photography and clay tones should carry
  visual weight rather than saturated UI color. Font evidence is dominated by
  product-personalization font-picker options (Lydian, CircularStd,
  BeirutDisplay, PlanscribeNF-Bold) rather than a confirmed site typographic
  voice; the interface font is inferred to fall back to a system-UI stack
  (-apple-system, Segoe UI, Roboto, Helvetica Neue, Arial), with "Assistant"
  treated as a plausible heading candidate. This interpretation proposes a
  warm, gallery-like neutral canvas with near-black ink and clay-toned accents
  drawn from the observed palette, reserving Bootstrap's semantic colors for
  inferred form/alert states rather than brand identity.

colors:
  primary: "#000000"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#3a3a3a"
  muted: "#949494"
  hairline: "#e3e1e1"
  surface-soft: "#f8f9fa"
  surface-card: "#eaeaea"
  on-primary: "#ffffff"
  accent-clay: "#bfad7b"
  accent-sand: "#ead8a4"
  hover-strong: "#555555"
  focus-active: "#18181b"
  success: "#28a745"
  danger: "#dc3545"
  warning: "#ffc107"
  info: "#17a2b8"
typography:
  display-xl: {fontFamily: "'Assistant', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Assistant', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Assistant', sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.primary}"
    titleTypography: "{typography.display-xl}"
    ctaBackground: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  option-swatch:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    hoverBackground: "{colors.hover-strong}"
    hoverText: "{colors.on-primary}"
    selectedBackground: "{colors.hover-strong}"
    selectedBorder: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
    typography: "{typography.body-sm}"

## Components

**button-primary** models the observed `.btn` and `po-edit-options-in-cart` rules, which set a black background with white text and a small border radius — used here for primary CTAs like "Add to Cart" and hero actions.

**button-secondary** is a proposed lower-emphasis action style using the observed hairline border (#e3e1e1) on a white surface, for actions like "View Details" or "Continue Shopping"; its hover/focus states are not observed and are proposed only.

**text-input** infers a minimal bordered field using the same hairline border and white canvas seen across product-option controls, appropriate for search boxes, quantity fields, and checkout forms; focus-ring styling is not observed.

**nav-bar** is a proposed top-level navigation pattern on a white canvas with dark-ink text and a hairline bottom border, consistent with the neutral surfaces seen elsewhere in the stylesheet; sticky/scroll behavior is not observed.

**product-card** proposes a light card surface (#eaeaea) with a hairline border and small radius to house ceramic product photography, title, and price, mirroring the subdued card-like treatment seen in the option/button media blocks.

**hero** is inferred from the `.slider-block` caption rules, which show white text and a solid black button over a dark background, with a focus/inverse state (white background, black text) — used here as the homepage banner pattern.

**footer** is a proposed low-contrast block using the soft surface tone (#f8f9fa) and muted text (#949494), for site links, contact information, and legal text; no footer-specific CSS was present in evidence.

**badge** proposes a small labeled chip using the light card surface and muted text, suited to status labels like "Handmade" or "Limited Stock"; not directly observed, styled to match nearby helptext-option coloring.

**search** is a proposed pill-shaped input using the observed hairline border, intended for the product catalog; no search-specific selectors were present in evidence.

**option-swatch** directly reflects the richest observed component: `.po-option__button-media` and `.po-font_picker-option--button`. Default state is a white surface with a light border; hover and selected states both switch to a solid grey-black fill (#555555) with white text, and the checked radio/checkbox indicator uses near-black (#18181b). This pattern is proposed for ceramics customization choices such as glaze color, size, or engraving font.

## Responsive Behavior
This is a recommended layout strategy, not measured site behavior.

| Breakpoint | Width       | Layout guidance                                  |
|-----------|-------------|---------------------------------------------------|
| mobile    | < 480px     | Single-column stack, full-width buttons/cards      |
| tablet    | 480–1024px  | 2-column product grid, nav collapses to a menu icon|
| desktop   | 1024–1440px | 3–4 column product grid, full nav bar visible      |
| wide      | > 1440px    | Max content width with increased side padding      |

Touch targets should be at least 44px tall, particularly for `option-swatch` and `button-primary`. Navigation and filter panels are assumed to collapse into a drawer or accordion below the tablet breakpoint; this collapse behavior has not been observed and is a proposed pattern only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- This document is derived from static CSS extraction only; no rendered page, real layout, or interaction states were observed.
- Most palette entries (e.g. #007bff, #28a745, #dc3545, #ffc107, #17a2b8 and their tint/shade variants) match default Bootstrap/theme utility colors and may not reflect intentional brand decisions; they are treated here as inferred system/alert states, not brand identity.
- Font evidence is dominated by product-personalization font-picker choices (Lydian, CircularStd, BeirutDisplay, PlanscribeNF-Bold); the actual heading/body typeface for the storefront itself is unconfirmed, and "Assistant" is used here as an inferred placeholder.
- All typography sizes, letter-spacing values, and the rounded/spacing scales beyond the single observed 3px radius are proposed conventions, not measured values.
- Hover, focus, active, and disabled states for components outside the product-options customizer (nav, search, footer) are not observed and are proposed for consistency only.
- Mobile and tablet layout behavior was not captured in the supplied evidence; all responsive guidance is a recommendation.
- Licensing and hosting availability of any named font (including Assistant and the font-picker options) has not been verified.
