---
version: alpha
name: "American Standard"
source_url: "https://americanstandard-us.com"
captured_at: "2026-09-29T04:11:42.265340+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  American Standard's storefront pairs a clean, utilitarian Montserrat typeface with a compact,
  high-contrast red-and-charcoal palette. Body copy renders in near-black (#1c1c1e) on white,
  while the primary call-to-action color is a saturated red (#e70025) that darkens through
  hover-adjacent (#d70025, inferred nearest observed swatch) and active (#720216, exact match to
  the computed active state) states. Montserrat is declared with system-ui and -apple-system
  fallbacks, giving the brand a corporate, slightly condensed feel appropriate to a manufacturer
  catalog with dense navigation and product-spec content. Neutral grays (#f8f8f8, #e5e7eb,
  #6b6b72) do the work of surfaces, hairlines and disabled/secondary text; these are inferred
  semantic roles rather than confirmed design-token names. A handful of secondary hues —
  navy (#0f2b4b), blue (#2563eb), green (#22973f), orange (#ff9500) — appear in the palette and
  are treated here as informational/status accents (e.g., success, promotional, or link states)
  since no selectors confirming their exact use were supplied. Layout patterns (grid structure,
  card composition, breakpoints) are not observed in the evidence and are proposed conventions
  suited to a fixtures/faucets e-commerce catalog with heavy product imagery, finish swatches,
  and comparison tooling.

colors:
  primary: "#e70025"
  primary-hover: "#d70025"
  primary-active: "#720216"
  ink: "#1c1c1e"
  canvas: "#ffffff"
  body: "#4f4f4f"
  muted: "#6b6b72"
  hairline: "#e5e7eb"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  disabled-surface: "#dedede"
  navy: "#0f2b4b"
  accent-blue: "#2563eb"
  accent-green: "#22973f"
  accent-orange: "#ff9500"
  border-strong: "#1c1c1e"
typography:
  display-xl: {fontFamily: "Montserrat, system-ui, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, system-ui, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "Montserrat, system-ui, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: -0.2px}
  body-md: {fontFamily: "Montserrat, system-ui, -apple-system, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: -0.16px}
  body-sm: {fontFamily: "Montserrat, system-ui, -apple-system, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: -0.14px}
  caption: {fontFamily: "Montserrat, system-ui, -apple-system, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  button-md: {fontFamily: "Montserrat, system-ui, -apple-system, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 0px}
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
    padding: "{spacing.base} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  finish-swatch:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    size: "{spacing.xl}"

## Components

**button-primary** is the site's principal call-to-action pattern, observed directly in the `.btn` rule set: a solid red (#e70025) fill with white text, 600-weight Montserrat at 16px, generous horizontal padding (16px/32px), and a darkening sequence on hover (proposed nearest observed red) and active (#720216, an exact computed match). It is used for actions like "Get Started," "Submit," and "Shop Now."

**button-secondary** is proposed as the transparent/outlined counterpart, matching the `.btn-secondary` rule's transparent background and ink-colored text/border, used for lower-emphasis actions such as "Stay on site" in the partner-redirect modal.

**text-input** is a proposed pattern for form fields (zip code entry, contact forms) using the hairline gray border and card-white background; no explicit input styling was present in the supplied CSS, so padding and radius are inferred conventions consistent with the button radius family.

**nav-bar** represents the multi-level mega-menu structure implied by the extensive category text (Bathroom, Kitchen, Commercial, Inspiration, Support). Visual styling (background, spacing) is proposed since no header selector CSS was supplied.

**product-card** models the featured-product grid (e.g., Belmeade, Becklow, Saybrook faucets) seen in the text excerpt, pairing a title, model number, price, and finish options. Card chrome (border, radius, padding) is proposed; only typography and color tokens are grounded in observed declarations.

**hero** is proposed for the homepage banner ("Inspired by life, Designed for you since 1875") using the navy (#0f2b4b) as a dark background option and white text, though no hero-specific CSS was supplied — this mapping is inferred from the brand's presence in the palette.

**footer** is proposed as a dark, ink-colored band housing utility links (FAQs, Warranty, Returns) implied by the Support navigation text; no footer selector was present in evidence.

**badge** is proposed for status labels such as "Out of Stock" or promotional markers, using the observed green (#22973f) as a placeholder success/availability color; actual badge styling was not present in the supplied CSS.

**search** models the header search affordance ("Search" appears in nav text) using soft-surface background and hairline border consistent with the neutral palette; exact search-bar CSS was not supplied.

**finish-swatch** is a category-appropriate component for plumbing fixtures, representing the repeated "Polished Chrome / Brushed Nickel / Matte Black" finish selectors seen across product listings. Circular swatches with a primary-red selected-state ring are proposed; no swatch CSS was included in evidence.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <640px | Single-column product grid, collapsed mega-menu into an off-canvas drawer |
| Tablet | 640–1024px | Two-column product grid, condensed nav with dropdowns |
| Desktop | 1024–1440px | Full mega-menu, 3–4 column product grid |
| Wide | >1440px | Max-width content container, unchanged grid density |

Touch targets should be at least 44×44px for buttons and swatches given the observed 16px/32px button padding. Mega-menu items should collapse into accordions below tablet width. None of this is confirmed by the supplied CSS/HTML; it is a standard e-commerce recommendation.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no rendered layout, grid structure, or interaction states (hover/focus/active transitions beyond the `.btn` rules) were observed.
- Several palette entries (e.g., #2563eb, #22973f, #ff9500, #0f2b4b) have no selector context confirming their functional role; roles assigned (link, success, warning, hero background) are inferred guesses, not confirmed.
- The computed hover color rgb(190,3,36) does not exactly match any hex in the supplied palette; #d70025 was substituted as the nearest observed red and labeled inferred.
- Disabled-button background rgb(209,209,209) does not exactly match a supplied hex; #dedede was used as the nearest approximation.
- Font sizes beyond the observed 16px button/body value (display-xl, display-md, title-md, body-sm, caption) are proposed scale extrapolations, not measured from rendered pages.
- Spacing and rounded-corner scales beyond the observed 4px focus-outline radius and 16px/32px button padding are proposed conventions.
- No mobile navigation, cart drawer, or product-detail page markup was supplied, so nav-bar, footer, search, and product-card structural details are inferred from category/text context only.
- Montserrat's licensing/hosting (self-hosted vs. Google Fonts) was not verified from the supplied evidence.
