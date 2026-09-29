---
version: alpha
name: "Liqui Moly"
source_url: "https://liqui-moly.com"
captured_at: "2026-09-28T09:43:05.983865+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  LIQUI MOLY's public storefront exposes a Bootstrap-based design system layered with
  brand-specific overrides. The CSS custom properties define a blue primary (#00519e)
  and a red accent (#e2001a) alongside a neutral gray scale (#303030, #6c757d, #b7b7b7,
  #f6f6f6) used for body text, borders, and light surfaces. Buttons, form selects, and
  dropdown carets share a consistent 5px corner radius and 1px hairline borders in
  light gray, suggesting a restrained, technical-catalog aesthetic appropriate to an
  automotive parts and fluids retailer.
  Font stacks reference "DIN Pro" alongside Helvetica Neue, Helvetica, and Arial
  fallbacks; DIN Pro's exact weights and metrics are not confirmed by the supplied
  CSS, so its use here is inferred as the primary display/body family with system
  sans-serif fallback.
  This interpretation extends the observed tokens into a component system: a strong
  blue for primary actions and selected states (as seen on `.btn-outline-light-gray.selected`),
  red reserved for warnings/danger actions (`.btn-danger`), and light green/red tint
  backgrounds for success/error inline messaging. Layout rhythm (spacing, breakpoints)
  is proposed, not measured, since no responsive grid values were present in the
  supplied evidence.

colors:
  primary: "#00519e"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#303030"
  muted: "#6c757d"
  hairline: "#b7b7b7"
  surface-soft: "#f6f6f6"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  danger: "#e2001a"
  success: "#009f10"
  warning: "#ffc107"
  info: "#0dcaf0"
  secondary: "#d4d4d4"
  light-green: "#e5f5e7"
  light-red: "#ffe5e5"
typography:
  display-xl: {fontFamily: "'DIN Pro', 'Helvetica Neue', Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'DIN Pro', 'Helvetica Neue', Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "'DIN Pro', 'Helvetica Neue', Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'DIN Pro', Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'DIN Pro', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'DIN Pro', Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'DIN Pro', Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
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
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    height: "125px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl}"
  badge:
    backgroundColor: "{colors.light-green}"
    textColor: "{colors.success}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.md}"
  spec-approval-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** — Maps to the observed `.btn-danger`/`.btn` pattern generalized with the brand blue primary token instead of red, since red is reserved for danger/alert actions per `.btn-danger{background-color:#e2001a}`. Rounded corners at 4px echo the `.313rem` value seen on `.btn` and `.form-select`. Hover/active states are proposed, not observed.

**button-secondary** — Derived from `.btn-outline-light-gray`, which sets a transparent-to-white background with a `#b7b7b7` border and dark gray text. Used for secondary actions such as "Show details" or "Learn More" links seen throughout the page text. Selected/focus treatment (2px blue border, per `.selected`) is proposed as an extension for toggle-style controls (e.g., size/variant pickers for oil containers).

**text-input** — Based on `.form-select` styling: white background, `#b7b7b7` border, 5px radius, dark gray (`#303030`) text, with a custom SVG chevron. Applied here generically to text fields and dropdowns (e.g., country/region selector, vehicle search). Focus ring color is inferred as primary blue but not confirmed in the supplied CSS.

**nav-bar** — Inferred from the `--header-height:125px` custom property on `body`, indicating a tall fixed or sticky header, likely accommodating a logo, country selector, search, and account/cart icons implied by the keyboard-shortcut text ("Cart shift+ALT+C", "Search ALT+S"). Exact layout and sticky behavior are not observed.

**product-card** — Proposed pattern for the 4000+ product catalog implied by the page copy. Uses a soft off-white card surface (`#f8f8f8`) distinct from the white canvas, with a hairline border and 4px radius consistent with other bordered elements. SKU, container type, and specifications fields (mentioned in page text) would appear as caption-level metadata beneath the title.

**hero** — Proposed full-width banner using the light gray surface token as a background wash, with display-xl typography for headline messaging (e.g., "Motor oil, additives and car care"). No hero-specific CSS was present in the evidence; sizing and imagery placement are inferred from typical automotive-catalog conventions.

**footer** — Proposed dark-toned footer using the darkest observed neutral (`#212529`) as background with white text, reflecting the extensive footer navigation implied by the page text (Company, Career, Sponsoring, Press, Contact, regional language links). Multi-column link groups are inferred, not measured.

**badge** — Uses the observed light-green/success pairing (`#e5f5e7` background, `#009f10` text) seen in the Bootstrap "success" alert tokens (`--bs-light-green`, `--bs-success`), repurposed as a small status pill for tags like "New" or "In Stock." A parallel light-red/danger variant is available via the same token set for "Out of Stock" or warning states.

**search** — Styled identically to text-input per shared `.form-select`-class conventions, intended for the site's global search (referenced via "Search ALT+S" shortcut) and the "Oil guide" vehicle-lookup tool mentioned in the page copy.

**spec-approval-badge** — A category-specific component addressing the product-approval callouts explicit in the page text ("LIQUI MOLY recommends this product for vehicles... specifications or original spare part numbers are required"). Rendered as a muted-gray, small-caption chip with a hairline border to visually separate OEM approval codes from marketing copy, distinguishing it from the success/danger badges used for stock status.

## Responsive Behavior

The following breakpoint table is a **recommendation** based on common Bootstrap 5 conventions implied by class names (`.container`, `--bs-gutter-x`) in the evidence; no explicit media queries were supplied.

| Breakpoint | Width      | Notes (proposed) |
|------------|------------|-------------------|
| xs         | <576px     | Single-column stacking; nav collapses to hamburger/off-canvas menu |
| sm         | ≥576px     | Two-column product grids begin |
| md         | ≥768px     | Header height may reduce from the fixed 125px desktop value |
| lg         | ≥992px     | Full nav bar with visible primary links |
| xl         | ≥1200px    | Container gutter reaches the `clamp()`-defined max of 1.5rem |

Touch targets should meet a minimum 44×44px hit area for buttons and form controls, particularly the `.form-select` chevron control and `.btn-close` icon (currently sized at `1.25em` padding, likely under 44px and worth expanding for mobile). Off-canvas or accordion collapse for the deep multi-level navigation (Company/Products/Service/etc., visible in the page text) is proposed but not confirmed by any observed JavaScript or interaction evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- All font-size, spacing, and breakpoint values beyond the literal `1rem`/`.313rem` figures found in `.btn`/`.form-select` are proposed estimates, not measurements.
- "DIN Pro" is referenced in the font-family evidence but its licensing, weights, and actual rendering could not be verified from static CSS alone; fallback to Helvetica Neue/Arial is assumed.
- No hero, footer, or product-card markup/CSS was directly supplied; those components are structurally inferred from page-text content and generic e-commerce conventions, not from captured selectors.
- Interaction states (hover, focus, active, disabled) beyond the single `.selected` class example are not observed and are labeled proposed throughout.
- Mobile/responsive layout, navigation collapse behavior, and touch-target sizing are not observed in the supplied evidence; the responsive table above is a design recommendation only.
- Color-role assignments (e.g., which gray serves as "ink" vs. "body") are inferred from usage context in the supplied selectors, not from explicit design documentation.
