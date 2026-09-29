---
version: alpha
name: "Wild Earth"
source_url: "https://wildearth.com"
captured_at: "2026-09-28T05:09:01.520521+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Wild Earth positions itself as a science-backed, vegan pet food brand with a clean,
  high-contrast interface built around a signature lime-green accent (#e6f85f) paired
  with near-black ink and white canvas. Observed CSS shows this lime tone used for
  announcement-bar borders, highlighted text, and CTA button borders, while a softer
  chartreuse (#e3ecaa) appears as a filled button background with black text and a
  black border, suggesting a bold, outlined-button aesthetic rather than soft shadows.
  A secondary olive-green (#97b10d) and a hot pink (#e95485) surface in accent contexts
  (borders, badges) and are treated here as inferred secondary/tertiary accents for
  promotions and alerts. Typography evidence shows 'Labil Grotesk' (Bold/Regular) used
  explicitly for buttons and CTAs, with 'Hanken Grotesk' present as a lighter body/UI
  family and 'Tiempos Text' as a serif available for editorial or quote treatments;
  system sans-serif stacks serve as fallbacks throughout. Neutrals span a wide gray
  range (#111827 to #f9f9f9), which this spec consolidates into a restrained ink/body/
  muted/hairline/surface scale. Rounded corners are modest (6–10px observed on buttons),
  reused here as sm/md tokens; larger radii and spacing scales are proposed for
  consistency, not directly measured.

colors:
  primary: "#e6f85f"
  secondary: "#97b10d"
  accent-pink: "#e95485"
  accent-yellow: "#ffd042"
  accent-soft: "#e3ecaa"
  ink: "#111827"
  canvas: "#ffffff"
  body: "#374151"
  muted: "#6b7280"
  hairline: "#e5e7eb"
  surface-soft: "#fafafa"
  surface-card: "#f9f9f9"
  on-primary: "#000000"
typography:
  display-xl: {fontFamily: "'Labil Grotesk Bold', 'Hanken Grotesk', sans-serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Labil Grotesk Bold', 'Hanken Grotesk', sans-serif", fontSize: "32px", fontWeight: 700, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "'Labil Grotesk Regular', 'Hanken Grotesk', sans-serif", fontSize: "22px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "'Hanken Grotesk', 'Inter', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Hanken Grotesk', 'Inter', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'Hanken Grotesk Light', sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "'Labil Grotesk Bold', sans-serif", fontSize: "16px", fontWeight: 700, lineHeight: 1, letterSpacing: "0px"}
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
  button-primary: {backgroundColor: "{colors.primary}", textColor: "{colors.on-primary}", typography: "{typography.button-md}", rounded: "{rounded.md}", padding: "{spacing.md} {spacing.lg}", border: "2px solid {colors.ink}"}
  button-secondary: {backgroundColor: "transparent", textColor: "{colors.canvas}", typography: "{typography.button-md}", rounded: "{rounded.md}", padding: "{spacing.sm} {spacing.base}", border: "1px solid {colors.accent-pink}"}
  text-input: {backgroundColor: "{colors.canvas}", textColor: "{colors.ink}", typography: "{typography.body-md}", rounded: "{rounded.sm}", padding: "{spacing.sm} {spacing.md}", border: "1px solid {colors.hairline}"}
  nav-bar: {backgroundColor: "{colors.canvas}", textColor: "{colors.ink}", typography: "{typography.body-sm}", rounded: "{rounded.none}", padding: "{spacing.sm} {spacing.lg}", border: "1px solid {colors.hairline}"}
  product-card: {backgroundColor: "{colors.surface-card}", textColor: "{colors.ink}", typography: "{typography.title-md}", rounded: "{rounded.md}", padding: "{spacing.base}", border: "1px solid {colors.hairline}"}
  hero: {backgroundColor: "{colors.surface-soft}", textColor: "{colors.ink}", typography: "{typography.display-xl}", rounded: "{rounded.none}", padding: "{spacing.xxl} {spacing.lg}"}
  footer: {backgroundColor: "{colors.ink}", textColor: "{colors.canvas}", typography: "{typography.body-sm}", rounded: "{rounded.none}", padding: "{spacing.xl} {spacing.lg}"}
  badge: {backgroundColor: "{colors.accent-soft}", textColor: "{colors.on-primary}", typography: "{typography.caption}", rounded: "{rounded.full}", padding: "{spacing.xxs} {spacing.sm}"}
  search: {backgroundColor: "{colors.surface-soft}", textColor: "{colors.ink}", typography: "{typography.body-sm}", rounded: "{rounded.full}", padding: "{spacing.sm} {spacing.base}", border: "1px solid {colors.hairline}"}
  meal-plan-card: {backgroundColor: "{colors.canvas}", textColor: "{colors.ink}", typography: "{typography.body-md}", rounded: "{rounded.lg}", padding: "{spacing.lg}", border: "2px solid {colors.primary}"}

## Components

**button-primary** is the lime-accented CTA (e.g. "Grab Deal", "Check Plans"), matching the observed `.check-plans-button` pattern of a light-green fill, black text, and a solid black border; hover/active states are proposed and not confirmed in the evidence.

**button-secondary** models the pink-bordered, transparent-background announcement link (`a.btn-h`), used for lower-emphasis promotional actions inside dark or colored header bars; text color is proposed as white to sit on darker announcement backgrounds.

**text-input** is a proposed pattern for search, email, and account fields; no explicit input styling was present in the supplied CSS, so border, radius, and padding are inferred from the general button/border conventions observed.

**nav-bar** represents the primary site header containing Dog Food, Cat Food, Treats, and account/cart controls; background and hairline are proposed neutrals since header-specific background color was not directly isolated in the evidence.

**product-card** covers listing tiles such as "Performance Formula Dog Food" or "Unicorn Pate Cat Food," including price, variant selector, and "Choose Your Plan" CTA; card surface and border are proposed from the neutral palette.

**hero** models the homepage banner promoting subscription offers (e.g. "20% off first order," "Free mystery treat"); large display typography and generous padding reflect the promotional, benefit-led messaging in the page text, though exact hero background was not isolated.

**footer** is proposed as a dark, ink-toned band for legal, newsletter, and secondary navigation links, inverting the light canvas used elsewhere; this inversion is inferred from common category conventions, not confirmed by evidence.

**badge** covers small labels like "Sale," "43% reduced itching," or subscription callouts, using the soft chartreuse (#e3ecaa) fill seen on the check-plans button as a badge background with dark text for contrast.

**search** is a pill-shaped input proposed for the header search affordance referenced in the page text ("Search"); rounding and soft background are inferred conventions, not directly observed styling.

**meal-plan-card** is a category-specific component for the "Find Your Meal Plan" / subscription flow central to Wild Earth's funnel, using a lime-bordered card to visually separate plan-selection steps from standard product cards.

## Responsive Behavior

This is a proposed breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Layout notes |
|---|---|---|
| Mobile | <640px | Single-column product grid, collapsed hamburger nav, sticky bottom CTA proposed |
| Tablet | 640–1024px | 2-column product grid, condensed nav with visible cart/search icons |
| Desktop | >1024px | 3–4 column product grid, full horizontal nav with mega-menu dropdowns |

Touch targets should be a minimum of 44×44px for cart, plan-selector, and nav controls. Navigation is expected to collapse into a slide-out or accordion menu below tablet width; none of this was directly observed and should be validated against live rendering.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no live rendering, computed styles, or DOM interaction were observed. Component states (hover, focus, disabled, error) are proposed conventions, not verified. Exact header, footer, and hero background colors were not isolated from the supplied rules, so surface roles are inferred from the general neutral palette. The semantic distinction between "primary" (#e6f85f) and "secondary" (#97b10d) green tones is an inferred hierarchy based on frequency of use in buttons/borders, not an explicit brand declaration. Font availability, licensing, and web-font loading for 'Labil Grotesk', 'Hanken Grotesk', and 'Tiempos Text' were not verified and should be confirmed before implementation. Responsive breakpoints and touch-target sizing are standard recommendations, not measured from the live site. All spacing and radius scales beyond the directly observed button padding/border-radius values are proposed for internal consistency.
