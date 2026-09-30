---
version: alpha
name: "Spot & Tango"
source_url: "https://spotandtango.com"
captured_at: "2026-09-28T10:11:26.731744+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Spot & Tango's visual system, as extracted from the storefront's CSS, centers on a
  clean white canvas (#ffffff) paired with near-black ink (#171717) for body copy,
  reflecting a straightforward, trustworthy DTC pet-food aesthetic. A saturated web
  blue (#007bff) recurs alongside pale blue backgrounds (#e7f3ff, #d9ebff, #e8f3ff)
  and a lighter accent blue (#9fcdff), and is treated here as the primary
  interactive/brand color for links, buttons, and highlighted stats. Soft neutral
  surfaces (#f7f7f7, #f3f6f9, #ececec) and a light border tone (#d2d2d7) suggest
  card and section backgrounds distinguishing the marketing page's many proof-point
  blocks (reviews, nutrition claims, testimonials). A small set of high-chroma
  accents — yellow (#fff951), green (#169a3d), coral-red (#ff4e43), and blush pink
  (#ffe2e7) — appear tied to badges, ratings, or callouts and are mapped here as
  supporting/status colors rather than primary brand color, since their exact usage
  is not directly observable in the supplied rules.

  Typography draws on two font stacks declared via CSS variables: --font-primary
  (rendered through Monument Grotesk weights) governs default body text, while
  --font-secondary (Inter) powers the site's text-body-* utility classes.
  BradfordLLWeb and Lora font files are present in the evidence but their applied
  selectors were not captured, so they are treated as an inferred serif display
  pairing for large marketing headlines, distinct from the grotesk/Inter UI system.

colors:
  primary: "#007bff"
  ink: "#171717"
  canvas: "#ffffff"
  body: "#171717"
  muted: "#575757"
  hairline: "#ececec"
  surface-soft: "#f7f7f7"
  surface-card: "#f3f6f9"
  on-primary: "#ffffff"
  accent-yellow: "#fff951"
  accent-green: "#169a3d"
  accent-red: "#ff4e43"
  accent-blue-pale: "#e7f3ff"
  accent-blue-light: "#9fcdff"
  accent-pink: "#ffe2e7"
  border: "#d2d2d7"
  dark: "#0e0e0e"
typography:
  display-xl: {fontFamily: "BradfordLLWeb-Bold, Lora, serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.11, letterSpacing: -0.5px}
  display-md: {fontFamily: "BradfordLLWeb-Regular, Lora, serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Monument Grotesk Medium, Inter, sans-serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, Inter Fallback, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, Inter Fallback, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Inter, Inter Fallback, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.1px}
  button-md: {fontFamily: "Monument Grotesk Medium, Inter, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.2px}
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.border}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  hero:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  recipe-card:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    badgeColor: "{colors.accent-yellow}"
  badge:
    backgroundColor: "{colors.accent-blue-pale}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** — Proposed solid blue call-to-action (e.g., "Start Quiz," "Get Started") using the primary blue against white text, matching the repeated blue CTA pattern implied by `#007bff` and its pale-blue tints appearing throughout the evidence.

**button-secondary** — Proposed outlined variant for lower-emphasis actions (e.g., "See Plans & Pricing") on white canvas, reusing the primary blue for text/border to keep a single accent hue across CTA hierarchy.

**text-input** — Proposed quiz/email-capture field styled with square corners, consistent with the observed `border-radius:0` reset on `button,input,...` in the base stylesheet; border uses the light grey `#d2d2d7`.

**nav-bar** — Proposed sticky header with white background, hairline bottom border (`#ececec`), and small Inter-based body text for links (Recipes, Reviews, FAQ, UnKibble, Login), inferred from the repeated nav-label text in the page excerpt.

**hero** — Proposed top-of-page banner using the pale blue/grey card surface (`#f3f6f9`) as backdrop for the large serif display headline ("Upgrade Your Pup's Bowl With Fresh Dog Food"), with a CTA button and trust badges beneath.

**product-card** — Proposed card for individual recipes (Beef + Barley, Turkey + Sweet Potato, Cod + Salmon) with a white background, thin hairline border, rounded corners, and a small yellow tag for labels like "Best Seller" or "Picky Eater Favorite."

**recipe-card** — Category-specific component built for the "Explore Our Recipes" grid; slightly larger radius and soft surface background to visually group flavor, description, and dietary badge (Grain-Free, Hypoallergenic) per the excerpt's recipe listing.

**badge** — Proposed small pill label (e.g., "Vet Developed," "AAFCO Compliant," "USDA Meats") using pale blue background and primary blue text, echoing the multiple light-blue tint values in the palette.

**footer** — Proposed dark closing section using the near-black `#0e0e0e` tone as background with white text, for company/legal links and secondary navigation; not directly observed but consistent with the dark/light contrast pairs present in the palette.

**search** — Proposed lightweight quiz/plan-finder input using the light grey surface tone, intended for a "find your recipe" or plan-lookup interaction referenced in the page copy ("Find Your Recipe").

## Responsive Behavior

Recommended (not measured) breakpoint table:

| Breakpoint | Width       | Layout notes (proposed) |
|-----------|-------------|--------------------------|
| Mobile    | < 640px     | Single-column stack; nav collapses to hamburger/menu icon; CTA buttons full-width |
| Tablet    | 640–1024px  | Two-column recipe/testimonial grids; nav links may remain inline or collapse near lower end |
| Desktop   | > 1024px    | Multi-column hero, three-up recipe cards, full inline nav |

Touch targets should be minimum 44×44px for CTA buttons and nav items. Collapse patterns (hamburger menu, accordion FAQ) are standard proposals for this content type, not confirmed from the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is derived solely from static CSS declarations and page text; no rendered layout, computed styles, or interaction states (hover, focus, active, disabled) were observed. Font-role mapping (BradfordLLWeb/Lora as display serif vs. Monument Grotesk/Inter as UI sans) is inferred from variable naming and file presence, not confirmed selector usage. Color-to-role assignments (e.g., which blue is "primary" vs. decorative, or exact usage of yellow/green/red accents) are inferred from frequency and typical DTC patterns, not verified against live screenshots. Component sizing, spacing, and radius values are proposed conventions consistent with the observed reset (`border-radius:0` on form elements) rather than measured from rendered pages. Mobile/responsive behavior, breakpoints, and nav-collapse behavior are not observed and are offered only as standard recommendations. Licensing and availability of the custom fonts (BradfordLLWeb, Monument Grotesk) were not verified and should be confirmed before implementation.
