---
version: alpha
name: "Nanobebe"
source_url: "https://nanobebe.com"
captured_at: "2026-09-28T04:54:03.861400+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is built from Shopify theme CSS variables, checkout-widget styling, and payment/badge tokens captured on nanobebe.com, not from direct visual inspection. The only distinctly brand-like hue in the palette is a muted sage green (#a2b790), which echoes the "Sage" color option used across bottles, pacifiers, and breastmilk bottles; it is treated here as the primary accent. Ink and surface tones come from dark near-black grays (#1c1c1c, #232323) paired with white canvas and light gray surfaces (#dedede, #cccccc) used for sold-out badges and skeleton loaders. A secondary blue (#1990c6, hover #136f99) appears only inside the Shopify accelerated-checkout button and is mapped here as a functional secondary action color, not a core brand hue. Grayscale-only success/warning/error CSS variables suggest the live theme favors monochrome status messaging, but concrete hex equivalents (#28a745, #ff9800, #dc3545) from the supplied palette are used as clearer stand-ins, labeled inferred. Typography pairs a distinctive display face (Josefin Sans) with a rounder workhorse sans (Nunito) for body and UI text, a common pairing convention rather than a confirmed observation. Layout tokens (container gutters, section spacing) are drawn directly from `:root` custom properties.

colors:
  primary: "#a2b790"
  ink: "#1c1c1c"
  canvas: "#ffffff"
  body: "#232323"
  muted: "#cccccc"
  hairline: "#00000033"
  surface-soft: "#dedede"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  secondary-action: "#1990c6"
  secondary-action-hover: "#136f99"
  overlay: "#00000066"
  success: "#28a745"
  warning: "#ff9800"
  error: "#dc3545"
typography:
  display-xl: {fontFamily: "Josefin Sans, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Josefin Sans, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Instrument Sans, sans-serif", fontSize: "1.375rem", fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito, sans-serif", fontSize: "1.0rem", fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito, sans-serif", fontSize: "0.9375rem", fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Nunito, sans-serif", fontSize: "0.875rem", fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.1px}
  button-md: {fontFamily: "Nunito, sans-serif", fontSize: "0.9375rem", fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.secondary-action}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
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
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  color-swatch-selector:
    backgroundColor: "{colors.surface-soft}"
    activeBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    size: "{spacing.lg}"
    gap: "{spacing.xs}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** uses the sage accent as a warm, low-saturation call-to-action fill consistent with a baby-care brand's soft visual language; hover/active states are proposed since no `:hover` rule for this class was supplied.

**button-secondary** is grounded directly in the observed `.shopify-payment-button__button--unbranded` rule (`#1990c6`, hover `#136f99`), the one concrete interactive-state pair in the evidence, reused here for a general secondary action.

**text-input** infers a light bordered field using the observed low-opacity black hairline (`0 0 0 / 0.15`–`0.33`) seen in header separators; focus and error states are proposed, not observed.

**nav-bar** reflects the documented `--header-grid` layout (logo centered, primary/secondary nav flanking) and `--header-padding-block` values (1rem–1.6rem), collapsed here into a single padding token; exact breakpoint switch to the stacked grid variant is inferred from the presence of two competing grid-template definitions.

**product-card** is proposed for the "our best sellers" grid (bottles, pacifiers, breast pump, monitor) implied by the page text; no card-specific CSS was supplied, so radius and padding are estimates.

**color-swatch-selector** is a category-appropriate addition for Feeding products, since bottle/pacifier variants (Sage, White, Grey, Teal, Pink) are explicitly listed in the evidence; swatch shape/size/active state are proposed.

**hero** models the homepage banner ("Nanobébé wearable breast pump… SHOP NOW") using the soft surface tone and section-vertical-spacing custom property (3.5rem) as a spacing anchor.

**footer** is inferred as a dark-ink block containing the extensive link list observed (Shop, About, Support, policies, payment icons); background choice is a proposed dark treatment, not confirmed.

**badge** covers sale/sold-out/custom badges; the CSS exposes distinct `--sold-out-badge-background` (light gray) and `--custom-badge-background` (`28 28 28`) variables, so real implementations may split this into two badge variants rather than one.

**search** is proposed generically from the visible "Search" nav entry; no dedicated search-input CSS was in the evidence.

## Responsive Behavior

This is a recommendation, not measured site behavior.

| Breakpoint | Width      | Nav behavior                          | Grid columns |
|-----------|------------|----------------------------------------|--------------|
| Mobile     | <640px     | Collapsed hamburger, stacked header grid (matches the second `--header-grid` rule) | 1 |
| Tablet     | 640–1024px | Condensed inline nav                   | 2 |
| Desktop    | >1024px    | Full three-column header grid (`primary-nav logo secondary-nav`) | 3–4 |

Touch targets should be at least 44px per the checkout button's clamped `block-size` (25–55px range observed); interactive swatches and nav items should follow the same minimum. Mobile menu collapse is assumed from the presence of two header-grid definitions but was not visually confirmed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- All values are extracted from static CSS/text; no rendered screenshots, computed styles, or DOM interaction were observed.
- Color-to-role mapping is inferred: only `#a2b790` shows brand-specific intent (via the "Sage" product option); most other hexes are payment-network logos (Visa, Mastercard, PayPal, Amex) or generic UI grays and are excluded from primary brand roles.
- Success/warning/error hexes are approximations; the live theme's own variables (`--success-background`, etc.) are grayscale RGB triplets, not the bright hexes used here.
- Font-role assignment (Josefin Sans for display, Nunito/Instrument Sans for body) is an inferred pairing convention; actual per-element font usage was not verified.
- Font licensing/self-hosting status for Josefin Sans, Nunito, and Instrument Sans was not verified.
- Border-radius scale is a proposed convention; the one concrete radius data point (`0px` default on the accelerated-checkout button) suggests the live theme may favor sharp corners more broadly than this scale implies.
- Spacing scale approximates but does not exactly match observed `--section-vertical-spacing` (3.5rem/56px) and `--section-stack-gap` (2.5rem/40px) values.
- No hover/focus/active/error interaction states were present in the evidence beyond the single checkout-button hover rule; all other interactive states are proposed.
- Mobile/tablet layout behavior is inferred from competing `--header-grid` declarations, not from a captured mobile viewport.
