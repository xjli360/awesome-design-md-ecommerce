---
version: alpha
name: "Siete Foods"
source_url: "https://sietefoods.com"
captured_at: "2026-09-28T10:19:56.675357+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Siete Foods is a Mexican-American heritage food brand whose site evidence shows a warm,
  earth-toned neutral base (cream #f8f3ec canvas, off-white #ffffff cards) paired with a
  deep navy-violet ink (#1e1a34, CSS var --color-brand-medianoche) used for body copy and
  as text-on-gold. The dominant action color is a warm amber-gold (#f2a900, CSS var
  --color-brand-garzagold) used for primary buttons, with a deep violet (#463770,
  --color-violeta-700) serving as a secondary/alt-section color per observed button and
  section-background selector logic. Five full 9-step tonal ramps were supplied (pink/
  magenta, violet, teal, green, gold/orange), which this spec treats as a systematic brand
  ramp system for accents, badges, and seasonal section backgrounds; exact ramp-to-token
  names are inferred from CSS variable naming patterns (garzagold, violeta, fuego, blanco),
  not confirmed pixel-for-pixel. Custom font families "BD Rendall," "Queulat," and "Latino
  Gothic" appear in the stylesheet font stack and are assumed to be licensed heritage/display
  faces; role assignment (display vs. body) is inferred, not verified. Gray utility tokens
  (#9ca3af, #e5e7eb) are used for muted text and hairlines per Tailwind-style CSS defaults.
  All spacing, radius, and most typographic sizes are proposed design-system defaults, not
  measured from rendered layout.

colors:
  primary: "#f2a900"
  ink: "#1e1a34"
  canvas: "#f8f3ec"
  body: "#1e1a34"
  muted: "#9ca3af"
  hairline: "#e5e7eb"
  surface-soft: "#f8f0e2"
  surface-card: "#ffffff"
  on-primary: "#1e1a34"
  secondary: "#463770"
  accent-magenta: "#cc0066"
  teal-accent: "#23b0ba"
  verde-accent: "#6eb222"
  gold-deep: "#f4ad07"
  warm-orange: "#db6013"
  fuego-mid: "#d84db9"
  disabled-bg: "#d1c5ae80"
  disabled-text: "#ffffffbf"
typography:
  display-xl: {fontFamily: "BD Rendall, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "BD Rendall, sans-serif", fontSize: 34px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Queulat, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Latino Gothic, system-ui, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Latino Gothic, system-ui, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Latino Gothic, system-ui, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Latino Gothic, system-ui, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    border: "3px solid {colors.primary}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "2px solid {colors.secondary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.verde-accent}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  flavor-swatch:
    backgroundColor: "{colors.gold-deep}"
    border: "2px solid {colors.surface-card}"
    rounded: "{rounded.full}"
    size: "{spacing.lg}"

## Components

**button-primary** — The gold call-to-action button ("Shop Now!", "Celebrate With Us") reflects the observed CSS pattern where `.action-button .button-element` sets a garzagold background with medianoche (dark ink) text and a matching 3px border, giving a bold, high-contrast pill-like control.

**button-secondary** — Derived from `.action-button.secondary .button-element`, which swaps to a background-colored fill with violeta-700 text and border. Used for lower-emphasis actions such as "Learn More" links inside colored sections.

**text-input** — Proposed form field styling for newsletter/search/account forms; no direct input-field CSS was observed beyond generic reset rules, so border, radius, and padding are inferred defaults consistent with the brand's soft, rounded aesthetic.

**nav-bar** — Proposed top navigation bar (Home / Shop / Recipes / About / Community) using the canvas cream background and ink text seen in body-level tokens; sticky/scroll behavior is not observed.

**product-card** — Proposed card for tortilla chip and product tiles (e.g., "Maíz Three Cheese Nacho Corn Tortilla Chips"); white surface with a hairline border and generous internal padding, sized for grid layouts referenced in the product listing copy.

**hero** — Proposed large banner treatment for the homepage video hero ("Honoring the past. Together, we spark the future."), using the soft cream surface and large display type; the site is known to include a `<video>` element behind hero content, but exact visual composition was not measured.

**footer** — Proposed dark ink footer containing the multi-column link groups (Ways to Shop, Help, About, Community) and social icons visible in the page text, using light text for contrast against ink.

**badge** — Proposed dietary/label chip (e.g., "gluten free," "dairy free") using the green ramp accent, matching the small inline tags seen adjacent to recipe titles in the page text.

**search** — Proposed pill-shaped search input for the "Search the Site" control referenced in header copy; rounded-full shape and hairline border are stylistic proposals, not measured.

**flavor-swatch** — Category-specific proposed component: a small rounded color dot used to represent chip/salsa flavor or heat-level variants (e.g., Mild/Spicy Taco Seasoning, Three Cheese, Jalapeño), drawing on the gold/orange ramp for warmth-coded variant selection.

## Responsive Behavior

Recommended, not measured, breakpoints:

| Breakpoint | Width       | Layout notes (proposed) |
|-----------|-------------|--------------------------|
| sm        | ≤ 640px     | Single-column stack; nav collapses to hamburger/menu icon |
| md        | 641–1024px  | 2-column product grid; nav remains condensed |
| lg        | 1025–1440px | 3–4 column product grid; full nav visible |
| xl        | ≥ 1441px    | Max-width content container, generous section padding |

Touch targets for buttons and nav items should be at least 44×44px. Search and nav collapse behavior (drawer vs. dropdown) was not observed and is a UX recommendation only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS/text extraction only; no rendered page, computed styles, or interaction states (hover, focus, active, disabled beyond the two `.disabled` rules shown) were observed. Hex-to-brand-token mapping (e.g., which ramp step equals "garzagold," "violeta-700," "fuego-light," "blanco-200") is inferred from CSS variable naming conventions and typical 9-step ramp ordering, not confirmed against rendered swatches. All typographic sizes, line-heights, and letter-spacing values are proposed defaults; only font-family names and generic inheritance rules were present in the supplied CSS. Availability and licensing of "BD Rendall," "Queulat," and "Latino Gothic" were not verified and should be confirmed before production use. Mobile navigation, cart drawer, and search interaction patterns are proposed UX conventions, not observed site behavior. Spacing and radius scales follow a generic system-default progression rather than measured site values.
