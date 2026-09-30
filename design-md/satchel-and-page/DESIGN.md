---
version: alpha
name: "Satchel & Page"
source_url: "https://satchel-page.com"
captured_at: "2026-09-28T09:48:44.060183+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Satchel & Page's public CSS evidence points to a utilitarian, no-nonsense
  Shopify storefront built around heritage leather goods. The observed
  palette is dominated by near-black inks (#231f20, #030712, #121212) against
  white and off-white surfaces (#ffffff, #f9fafb), with a cyan-blue
  (#1990c6, hover #136f99) surfacing on the accelerated-checkout button and a
  cooler blue (#3256e5) on a returns-modal header link. Two named CSS
  variables, --color-swatch-brown (#613e2e) and --color-swatch-green
  (#2d4f2d), are explicitly tied to product color options and are the
  strongest brand-relevant colors in the evidence, so this interpretation
  treats leather-brown as the heritage accent while keeping the checkout blue
  as the primary interactive/CTA color, since it is the only color actually
  applied to a call-to-action button in the source. Button and modal
  components in the evidence use border-radius:0, so square, sharp-cornered
  buttons are treated as an observed pattern rather than an assumption.
  Typography evidence lists Krona One (a geometric all-caps display face),
  Lora (serif), Roboto/Noto Sans/system-ui stacks, and theme-custom families
  brandon-grotesque and "untitled sans," which this spec assigns to display,
  secondary, and body roles respectively; exact weights, tracking, and
  in-page usage are inferred, not confirmed from rendered layout.

colors:
  primary: "#1990c6"
  primary-hover: "#136f99"
  ink: "#231f20"
  ink-deep: "#030712"
  canvas: "#ffffff"
  body: "#374151"
  muted: "#d1d5db"
  hairline: "#eaeaea"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-brown: "#613e2e"
  accent-green: "#2d4f2d"
  accent-link: "#3256e5"
  placeholder: "#dedede"
  overlay: "#00000000"
  graphite: "#1f2937"
  near-black: "#121212"
typography:
  display-xl: {fontFamily: "Krona One, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: 0.5px}
  display-md: {fontFamily: "Krona One, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0.25px}
  title-md: {fontFamily: "Lora, serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "untitled sans, Roboto, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "untitled sans, Roboto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "brandon-grotesque, Noto Sans, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "brandon-grotesque, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.5px}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
    border: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.muted}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    priceColor: "{colors.body}"
    badgeAccent: "{colors.accent-brown}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-link}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.placeholder}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  material-swatch:
    optionBrown: "{colors.accent-brown}"
    optionGreen: "{colors.accent-green}"
    borderColor: "{colors.hairline}"
    selectedRing: "{colors.primary}"
    rounded: "{rounded.full}"
    size: "{spacing.lg}"

## Components

**button-primary** is the checkout/add-to-cart action, using the observed accelerated-checkout blue (#1990c6, hover #136f99) with a zero-radius corner, matching the `border-radius:0` value found on the Shopify payment-button CSS. **button-secondary** is a proposed outlined variant for tertiary actions (e.g. "Shop Daily Carry") using ink-colored text on a white ground; its exact border weight is inferred. **text-input** covers newsletter/search fields with a light muted border and minimal radius, proposed to keep the same restrained, squared-off character as the buttons. **nav-bar** reflects the evidenced mega-menu categories (Bags, Luggage, Jackets, Belts, Leather Goods, Sale) on a white background with a hairline rule beneath it; exact height and sticky behavior are not confirmed. **product-card** represents listing tiles such as "Diplomat," "Carry On Pro," and "Weekender," pairing a title in the serif title style with a brown "Low Stock" badge accent drawn from the swatch-brown variable; card imagery treatment is proposed. **hero** models the "Built to work / Made to Last" banner as a dark, ink-toned full-bleed section with large Krona One display type and light text, since no rendered hero screenshot was supplied. **footer** uses the darkest observed neutral (#030712) as background with the evidenced link-blue (#3256e5) for the About/Help/Information columns; multi-column layout is proposed, not measured. **badge** is a soft pill used for review counts ("1,444 Reviews") or stock flags, built from the light gray badge tokens found in the Loop Returns CSS block. **search** is a proposed lightweight overlay input styled consistently with text-input. **material-swatch** is a category-appropriate component directly grounded in the `--color-swatch-brown` / `--color-swatch-green` CSS variables, representing leather color/finish pickers on product pages as round selectable dots.

## Responsive Behavior

Recommended, not measured, breakpoints: mobile ≤480px (single-column stack, hamburger nav confirmed by "Toggle mobile menu" text, full-width buttons, swatches enlarged to ≥44px touch target), tablet 481–1024px (2-column product grid, condensed nav), desktop ≥1025px (mega-menu nav bar, 3–4 column product grid, hero at full display-xl scale). All interactive targets (buttons, swatches, nav toggle) should maintain a minimum 44×44px hit area per common accessibility guidance; this is a proposal, since no live responsive layout, media query, or touch-interaction evidence was captured.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived entirely from static CSS/text extraction and contains no rendered screenshots, computed layout, or interaction traces. Semantic color roles (primary vs. accent vs. link) are inferred from selector context (e.g., checkout button, Loop Returns modal) rather than a documented brand style guide, and the true brand accent may differ from the checkout blue used here. Font availability, licensing, and whether "brandon-grotesque" or "untitled sans" are self-hosted/licensed correctly were not verified. All typography sizes, letter-spacing, spacing scale, and rounded scale (aside from the observed `border-radius:0` on buttons) are proposed conventions, not measured values. Hover, focus, error, and mobile-menu states are proposed patterns only, since no such states were present in the supplied evidence.
