---
version: alpha
name: "Dog Threads"
source_url: "https://goodthomas.com/"
captured_at: "2026-09-29T04:15:24.179590+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation documents the current Good Thomas™ storefront presentation
  of the Dog Threads matching dog-and-owner apparel line, as Dog Threads is now
  sold and fulfilled through goodthomas.com rather than as an independent site.
  The observed palette centers on a dark ink (#1f1e1c) and near-black body text
  against a white canvas, with a navy accent (#003e68) driving the Judge.me
  review widget (stars, reviewer names, write-a-review button) — inferred here
  as the brand's primary trust/accent color. A secondary blue pair (#1990c6,
  hover #136f99) appears on the Shopify accelerated-checkout button, inferred
  as a secondary action color distinct from primary. Soft neutrals (#f2f4f5,
  #eaeaea, #e3e3e3) suggest card and hairline surfaces typical of a Shopify
  Dawn-derived theme. A violet family (#5433eb, #eeeaff, #ebe6fc) and warm
  reds/oranges (#d92a0f, #ff4500, #f05d38) are present and inferred as
  sale-badge and limited-accent colors given the "$10 OR LESS," "SALE," and
  "Last Few Left" copy in the page text. Typography uses GTStandard-M for
  heading roles and Inter for paragraph roles, per the base theme's CSS custom
  property scaffolding (--font-h1--family, --font-paragraph--family); exact
  weights/sizes are not resolved in the supplied CSS and are proposed. Observed
  border-radius:0 on the payment button suggests a squared, no-radius button
  aesthetic, which this spec treats as the primary interaction shape.

colors:
  primary: "#003e68"
  ink: "#1f1e1c"
  canvas: "#ffffff"
  body: "#404040"
  muted: "#9ca3af"
  hairline: "#eaeaea"
  surface-soft: "#f2f4f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  action-blue: "#1990c6"
  action-blue-hover: "#136f99"
  sale: "#d92a0f"
  highlight: "#ff4500"
  accent-violet: "#5433eb"
  accent-violet-soft: "#eeeaff"
  rescue-green: "#214c3a"
  skeleton: "#dedede"
typography:
  display-xl: {fontFamily: "GTStandard-M, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "GTStandard-M, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "GTStandard-M, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Inter, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.action-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    hoverBackgroundColor: "{colors.action-blue-hover}"
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
    typography: "{typography.body-sm}"
    borderBottomColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  size-variant-selector:
    backgroundColor: "{colors.surface-soft}"
    selectedBackgroundColor: "{colors.accent-violet-soft}"
    selectedBorderColor: "{colors.accent-violet}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.md}"

## Components

**button-primary** — Uses the navy `{colors.primary}` sourced from the Judge.me review-widget theming variables (`--jdgm-write-review-bg-color: #003E68`), which is the strongest observed brand-accent signal in the CSS. Proposed for primary CTAs like "Add to Cart" and "Shop Now." Squared corners (`{rounded.none}`) are inferred from the observed `border-radius:0` on the Shopify accelerated-checkout button.

**button-secondary** — Maps to the observed `.shopify-payment-button__button--unbranded` styling (`background-color:#1990c6`, hover `#136f99`), used here as a secondary action color (e.g., "Choose Options," wishlist). Hover state is directly observed in CSS, not proposed.

**text-input** — No input styling was present in supplied CSS; colors and radius are proposed, borrowing the hairline gray and squared-to-slightly-rounded convention consistent with the theme's minimal radius elsewhere.

**nav-bar** — Inferred from page-text structure (mega-menu categories: "All Matching," "Dog People," "Super Sale," "Shop by Style," "Gift Shop"). Background/text colors are proposed from the base ink-on-white body styling; no header-specific selector was supplied.

**product-card** — Reflects the repeated product-grid pattern in the text excerpt (title, price, "CHOOSE"/"ADD" action, occasional "SALE" tag). Card surface and hairline border are proposed defaults consistent with the neutral palette; no card CSS block was supplied.

**hero** — Proposed layout for a top banner combining the "$10 OR LESS | Last Few Left!" announcement bar and a lifestyle hero image implied by "Look For Me In The Rainbows Suncatcher™" video block. Colors and type scale are proposed; no hero selector was in evidence.

**footer** — Uses the dark ink color as an inverted footer background (proposed), housing the "our story," "dog parent blog," "customer care," and rescue-donation copy ("$63,800 to help homeless pups"). Structure inferred from page-text ordering, not from footer CSS.

**badge** — Represents "SALE," "$10 or Less," and "Last Few Left" markers seen throughout the text excerpt. Color choice (`{colors.sale}`) is inferred from the warm red family in the palette (`#d92a0f`, `#ff4500`, `#f05d38`); no badge selector was directly supplied.

**search** — No search-bar CSS was supplied; this is a proposed pattern using muted text and hairline border consistent with the observed neutral-gray tokens, intended for the header's implied search affordance.

**size-variant-selector** — A category-appropriate proposed component for Dog Threads' matching-outfit model, where a shopper must pick both a human size and a dog size on one product. The violet accent (`#5433eb` / `#eeeaff`) is inferred as a selection-state color since it appears only as soft-tint and saturated pairs in the palette with no other clear assigned role.

## Responsive Behavior

Recommended, not measured — no responsive breakpoints or mobile layout were present in the supplied CSS.

| Breakpoint | Width | Nav | Product grid |
|---|---|---|---|
| Mobile | <640px | Collapsed hamburger, full-screen mega-menu | 1–2 columns |
| Tablet | 640–1024px | Horizontal nav, dropdown mega-menu | 2–3 columns |
| Desktop | >1024px | Full horizontal nav with mega-menu flyouts | 4 columns |

Touch targets should be at least 44×44px for cart/add buttons and size selectors. Mega-menu categories (e.g., "Sweaters," "Pajamas," "Poop Bags") should collapse into an accordion on mobile. None of this is confirmed live-site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This is a static-CSS extraction; no rendered DOM, JavaScript-driven states, or interaction behavior (hover, focus, open menu, cart drawer) were observed.
- Color role assignments (primary, sale, accent-violet, rescue-green, etc.) are inferred from where each hex appeared in isolated CSS rules (e.g., Judge.me theming, Shopify payment button) and from page-text cues, not from confirmed brand-guideline documentation.
- Typography sizes, weights, and letter-spacing are proposed; the supplied CSS only exposes CSS custom-property names (`--font-h1--family`, `--font-paragraph--size`, etc.) without resolved values.
- Font families GTStandard-M and Inter are observed in the `font_families` list but licensing, exact weight availability, and whether GTStandard-M is a licensed proprietary asset were not verified.
- No mobile menu, footer, or product-card selectors were present in the supplied CSS; those components are structurally inferred from the page-text ordering only.
- This document describes Dog Threads as presented within the current Good Thomas™ parent storefront per the confirmed brand-successor relationship; it does not reconstruct any former independent Dog Threads site design.
