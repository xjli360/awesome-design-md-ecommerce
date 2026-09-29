---
version: alpha
name: "Alpinestars"
source_url: "https://alpinestars.com"
captured_at: "2026-09-28T10:19:37.158154+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Alpinestars' storefront evidence shows a neutral, high-contrast foundation
  (pure black, white, and a stepped gray scale from #fafafa to #131313) built
  for product photography and racing-suit apparel. A saturated red (#d0112b)
  appears alongside a family of secondary reds (#c81e1e, #b50404, #c72e2f),
  which is interpreted here as the primary brand/action color given the
  page's "Italian racing heritage" copy, though the CSS itself does not label
  any hex as "brand" — this mapping is inferred. A cyan/teal (#29b5c2) and a
  deep blue (#1d3686) recur near Tech-Air® and informational contexts and are
  treated as secondary accents. Warm orange (#d66305, #ee9441) and green
  (#1b9500, #3ed660) tokens are present but not clearly tied to a component in
  the evidence, so they are reserved for status/badge use (sale, in-stock)
  rather than core UI. Typography is exclusively Inter, referenced through
  CSS custom properties (--font-h1--family, --font-paragraph--family) whose
  resolved pixel sizes were not exposed in the supplied rules; all sizes
  below are therefore proposed, not measured. Buttons, drawers, and product
  grids use design-token-driven spacing and radius variables, confirming a
  systemized component architecture even though concrete values are largely
  unmeasured.

colors:
  primary: "#d0112b"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#747474"
  hairline: "#e6e6e6"
  surface-soft: "#f5f5f5"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-teal: "#29b5c2"
  accent-blue: "#1d3686"
  success: "#1b9500"
  warning: "#d66305"
  danger: "#c81e1e"
  border-dark: "#000000"
  overlay: "#00000080"
typography:
  display-xl: {fontFamily: "Inter, sans-serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Inter, sans-serif", fontSize: "32px", fontWeight: 700, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Inter, sans-serif", fontSize: "22px", fontWeight: 600, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.45, letterSpacing: "0px"}
  caption: {fontFamily: "Inter, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.35, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0.3px"}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    priceColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    gap: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.overlay}"
    displayTypography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    hairlineColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  variant-picker:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    gap: "{spacing.xs}"

## Components

**button-primary**: Maps to the `.button`/`.button-primary` rules observed, which resolve color, background, radius, and font family entirely through CSS custom properties. Fill color is inferred as the brand red (`{colors.primary}`) since no literal hex was attached to the button selector in the evidence; state (hover/active/disabled) styling was not captured and is proposed.

**button-secondary**: Outline variant inferred from `.button-secondary` sharing the same structural rule as `.button`. Border/text use ink rather than fill, following typical secondary-button convention; this pairing is proposed, not observed in a screenshot.

**text-input**: No literal input-field CSS was supplied. Structure is proposed using the same hairline/radius tokens seen on button and drawer components, for consistency with the observed border-radius and border-width custom properties.

**nav-bar**: The excerpt's extensive mega-menu text (Motorcycle, MX, Auto, MTB, Sportswear, Outlet) confirms a multi-level navigation exists; exact colors/spacing for the bar itself were not in the CSS rules supplied, so background/hairline are inferred from the global `--color-background`/`--color-border` pattern.

**product-card**: Grounded in `.product-grid__card` and `[product-grid-view=default]` rules, which set gap, vertical padding (24px), and flex-column layout — these values are directly observed. Card background and price-accent color are inferred extensions.

**hero**: No hero-specific selector was present in the evidence; sizing and dark-background treatment are proposed based on the racing/heritage tone of the page copy and the availability of dark ink and overlay tokens.

**footer**: Not directly present in the supplied CSS; proposed as a dark-ink footer consistent with the overall black/white racing aesthetic implied by the page text and observed neutral palette.

**badge**: Inferred from sale-price patterns in the page text (e.g., "-25%", "-25%") and the presence of red tokens (`#c81e1e`, `#d0112b`); actual badge markup/CSS was not in the supplied rules.

**search**: No search-bar selector was supplied; proposed using the soft-surface and hairline tokens observed elsewhere (`.drawer-header` border-block-end pattern) for visual consistency.

**variant-picker**: Directly grounded in the observed `--variant-grid-columns`, `--variant-grid-gap`, and `--variant-picker-button-border-width` custom properties — a category-appropriate component for selecting apparel/boot sizes, common to a motorcycle-gear storefront. Selected-state border color is inferred as brand red.

## Responsive Behavior

| Breakpoint | Approx. width | Notes (proposed) |
|---|---|---|
| Mobile | <768px | Single-column product grid; nav collapses to a drawer/hamburger; variant-picker grid reduces to fewer columns than the 5-column desktop default observed in `--variant-grid-columns: 5`. |
| Tablet | 768–1023px | 2–3 column product grid; mega-menu likely condensed. |
| Desktop | ≥1024px | Full mega-navigation with category flyouts (Motorcycle/MX/Auto/MTB/Sportswear), multi-column product grid per `[product-grid-view=default]`. |

Touch targets are recommended at a minimum 44×44px for buttons and variant-picker cells, consistent with typical Shopify theme conventions (this theme's asset path indicates a Shopify base), though this was not verified against rendered markup. Breakpoint pixel values and collapse behavior are a recommendation only, not measured from the live site.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS rule fragments, a page-text excerpt, and an observed color/font list — no rendered screenshots, computed styles, or DOM inspection were available. Specific gaps:

- Font sizes, weights, and letter-spacing in the `typography` block are proposed; the source CSS references only custom properties (`--font-h1--size`, `--font-paragraph--size`, etc.) without resolved pixel values.
- The mapping of `primary` to `#d0112b` (versus the other reds `#c81e1e`, `#b50404`, `#c72e2f`) is an inferred semantic choice based on frequency and racing-brand context, not a labeled CSS variable.
- Hero, footer, nav-bar, search, and text-input components have no direct selectors in the supplied evidence; their structure and token usage are proposed extensions for design consistency.
- Border-radius values for buttons (`--style-border-radius-buttons-primary`) and border widths were referenced by variable name only; actual computed pixel values were not exposed.
- No hover/active/disabled/focus states, animations, or mobile drawer interactions were observed in rendered form; the transition variables (`--hover-lift-amount`, `--animation-speed`) confirm motion exists but not its visual effect.
- Custom font licensing/availability for Inter was not verified beyond its appearance as a `font-family` value; assume standard Google Fonts Inter with system fallback unless confirmed otherwise.
