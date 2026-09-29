---
version: alpha
name: "Ucon Acrobatics"
source_url: "https://ucon-acrobatics.com"
captured_at: "2026-09-29T04:05:25.286832+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Ucon Acrobatics presents itself as a Berlin-founded, B Corp-certified backpack
  and bag label built from recycled textiles, with a restrained, industrial-minimal
  visual language. The observed palette is dominated by warm, desaturated
  near-neutrals (#363439, #3f3b31, #373945, #908076) paired with a clean white
  canvas and light structural grays (#f6f6f8, #dedede, #ededf0). Muted material
  tones (#c1b2a4, #d8cec1, #dcc9b3) and a small set of accent hues (#ab515d,
  #c54641, #284073, #5e6967) appear in product/series imagery and are treated
  here as secondary brand accents rather than primary UI color, since their
  functional role in the live UI is not confirmed. Buttons use uppercase,
  letter-spaced labels with 1px black borders, suggesting a sharp-edged,
  low-radius aesthetic; this design system therefore defaults interactive
  elements toward `rounded.none`/`rounded.xs`. Two distinct type families are
  evidenced — a condensed grotesque for headings and a rounder geometric sans
  for body copy — mapped here as inferred `heading-font`/`body-font` roles.
  Phosphor is an icon font and is excluded from text typography. The resulting
  interpretation favors flat surfaces, thin hairlines, high-contrast ink-on-white
  text, and small warm-accent moments for badges and series tags, echoing the
  brand's "no empty claims" sustainability positioning.

colors:
  primary: "#111111"
  ink: "#363439"
  canvas: "#ffffff"
  body: "#3c4548"
  muted: "#908076"
  hairline: "#dedede"
  surface-soft: "#f6f6f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border-strong: "#2a2a2a"
  accent-clay: "#ab515d"
  accent-terracotta: "#c54641"
  accent-navy: "#284073"
  accent-sage: "#5e6967"
  tone-sand: "#c1b2a4"
  tone-oat: "#dcc9b3"
  tone-stone: "#a38977"
  overlay-scrim: "#00000000"
typography:
  display-xl: {fontFamily: "Roboto Condensed, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Roboto Condensed, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Roboto Condensed, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Rubik, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Rubik, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Rubik, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.02em}
  button-md: {fontFamily: "Rubik, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.08em}
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
    padding: "{spacing.xs} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    height: "64px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.tone-sand}"
    textColor: "{colors.ink}"
    overlay: "{colors.overlay-scrim}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-clay}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  variant-selector:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.md}"

## Components

**button-primary** renders the site's uppercase, letter-spaced call-to-action ("Shop Now") as a solid dark fill with white text and a hard-edged (0px radius) rectangle, matching the observed `.btn-fill` border/typography rules; hover-state color inversion is proposed, not confirmed from static CSS.

**button-secondary** mirrors `.btn-ghost` — transparent background, 1px black border, dark text — used for lower-emphasis actions like filter toggles; hover fill-swap is inferred from the `:hover` color rules present in the CSS but not visually verified.

**text-input** is a proposed pattern for newsletter/account forms; only a generic 1px hairline border and body typography are evidenced via form-adjacent theme rules, so padding and radius are estimated defaults.

**nav-bar** reflects the persistent header row containing logo, country/language selector, search, account, and cart-count badge (`.header-cart__count`); the 44px minimum tap target from `.header-cart__count`'s parent icon button is directly observed and preserved here.

**product-card** models the bestseller grid (e.g. "Tristan Packable Backpack," "Hajo Roll-Top Backpack") showing title, series name, price, and star rating; card chrome (hairline border, no radius) is inferred from the theme's flat, sharp-edge language rather than a captured card selector.

**hero** represents the top "Berlin by Design" banner with heavy display type over an image; background color is a placeholder token from the sand/tan palette since the true hero background is an image, not a flat fill — this is explicitly inferred.

**footer** is proposed as an inverted (dark-on-light-text) block for mission/values links, consistent with the brand's dark ink tones; no footer-specific CSS was supplied, so structure is a category-standard assumption.

**badge** covers small pills such as sustainability/series callouts ("B Corp," "New"); color choice (accent-clay) is a proposed accent selection from the observed palette, not a confirmed badge color.

**variant-selector** is a category-appropriate addition for backpack size/variant chips ("Medium," "One size," "+17" swatch counts) seen in the bestseller listing text; selected-state border uses the primary ink token, proposed rather than observed.

## Responsive Behavior

This is a recommended breakpoint structure, not measured site behavior:

| Breakpoint | Width      | Layout notes (proposed) |
|------------|-----------|--------------------------|
| xs         | <480px    | Single-column product grid, collapsed nav to hamburger + icon row |
| sm         | 480–767px | 2-column product grid, sticky search icon |
| md         | 768–1023px| 2–3 column grid, inline country/language dropdown |
| lg         | 1024–1279px| 3–4 column grid, full horizontal nav |
| xl         | ≥1280px   | 4-column grid, max-width content container |

Touch targets should maintain the observed 44×44px minimum (per `.header-cart__count` parent button rule). Mobile nav collapse into a drawer/hamburger is a standard proposal, not confirmed from the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Extraction is static and text/CSS-based; no rendered screenshots, so real layout, grid columns, and hover/focus states are not observed and are labeled proposed throughout.
- CSS custom properties like `--black`, `--white`, `--body-font`, `--heading-font` were referenced but not resolved to explicit hex/font values in the supplied evidence; mappings to `Roboto Condensed`/`Rubik`/specific hex codes are inferred, best-effort assignments.
- Several observed palette entries (`#0071ce`, `#eb001b`, `#f79e1b`, `#ff5f00`, `#142fbd`, `#1532cb`, `#1990c6`, `#136f99`) closely match third-party payment-method brand colors (e.g. PayPal, Mastercard, Visa) and were deliberately excluded from brand-facing tokens above.
- Border-radius values are mostly inferred as `0px` from a single accelerated-checkout button rule; broader site-wide corner treatment is not confirmed.
- Spacing scale values (`--space-*`) were referenced in `:root` but their pixel equivalents were not resolved from supplied CSS; the spacing tokens here follow a conventional proposed scale.
- Font licensing/availability for "Roboto Condensed" and "Rubik" (e.g. self-hosted vs. Google Fonts) was not verified from the supplied evidence.
- Mobile navigation, cart drawer, and filter/sort interaction patterns are proposed conventions for the category, not confirmed from captured markup or scripts.
