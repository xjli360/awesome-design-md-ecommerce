---
version: alpha
name: "Mini Rodini"
source_url: "https://minirodini.com"
captured_at: "2026-09-28T04:23:19.724210+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Mini Rodini's extracted CSS shows a neutral operating palette — near-black
  (#161316, #000000), white (#ffffff), and a small set of warm-to-cool grays
  (#222222, #666666, #6b7280, #9ca3af, #e5e7eb, #f6f6f6) — layered under a
  wide spread of saturated hues (#007a41, #253b84, #368dcc, #5da64c,
  #af5238, #dab4d8, #de3d16, #f5572e, #f7a840, #fc728e). No CSS rule ties a
  specific hex to a button, link, or badge role, so semantic assignment
  here is inferred: the neutrals are treated as brand ink/canvas/surface,
  and the saturated set is treated as a rotating accent/swatch palette
  suited to a kids'-apparel catalog (print colorways, size/color chips,
  category tags) rather than a single fixed brand color.

  Typography is dominated by "Circular" as the declared primary family,
  backed by system-ui and sans-serif fallbacks; a separate monospace stack
  (Consolas, Menlo, Monaco, etc.) appears only for form/utility contexts
  such as phone-input widgets, not for editorial type. The interpretation
  below proposes a clean, high-contrast retail layout — generous white
  space, black-on-white typography, and color used sparingly as accent —
  appropriate for a product-led, image-forward children's clothing site.
  All sizes, weights, and component states beyond the raw hex/font
  evidence are proposed, not observed.

colors:
  primary: "#161316"
  ink: "#161316"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#6b7280"
  hairline: "#e5e7eb"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border-strong: "#9ca3af"
  scrim: "#00000099"
  accent-green: "#007a41"
  accent-navy: "#253b84"
  accent-blue: "#368dcc"
  accent-sage: "#5da64c"
  accent-brown: "#af5238"
  accent-lilac: "#dab4d8"
  accent-red: "#de3d16"
  accent-orange: "#f5572e"
  accent-amber: "#f7a840"
  accent-pink: "#fc728e"
typography:
  display-xl: {fontFamily: "Circular, system-ui, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Circular, system-ui, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Circular, system-ui, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "Circular, system-ui, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Circular, system-ui, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Circular, system-ui, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Circular, system-ui, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.2px}
  mono-input: {fontFamily: "Consolas, Menlo, Monaco, 'Liberation Mono', 'Courier New', monospace", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "0px"}
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
    border: "1px solid {colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    overlay: "{colors.scrim}"
    titleTypography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch:
    size: "{spacing.lg}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.ink}"
    fills: ["{colors.accent-green}", "{colors.accent-navy}", "{colors.accent-blue}", "{colors.accent-sage}", "{colors.accent-brown}", "{colors.accent-lilac}", "{colors.accent-red}", "{colors.accent-orange}", "{colors.accent-amber}", "{colors.accent-pink}"]

## Components

**button-primary** is the near-black, full-fill call-to-action (add to bag, checkout) proposed to sit on white product surfaces; hover/pressed states are not observed and would need a darkened or opacity-shifted variant.

**button-secondary** is an outlined variant for lower-priority actions (wishlist, filters-clear) using the same neutral ink on a bordered white field, keeping the palette restrained outside of product imagery.

**text-input** covers standard form fields (newsletter signup, checkout, search-adjacent inputs); the hairline border and soft radius are proposed defaults consistent with the tailwind-reset evidence showing inherited font and transparent backgrounds on native form controls.

**nav-bar** is a white, hairline-bottomed header holding logo, category links, and account/cart icons; sticky/scroll-collapse behavior is proposed, not confirmed by any observed rule.

**product-card** presents a product image, title, and price on a bordered white card; the rounded-md corner and compact padding are inferred conventions for a catalog grid rather than measured values.

**hero** is a full-width banner section pairing large display type over a soft neutral or image background, with an optional dark scrim for text legibility — a common e-commerce landing pattern, not a captured layout.

**footer** inverts to a near-black background with white text, grouping newsletter, help, and legal links; this contrast pairing is proposed for visual anchoring at the page end.

**badge** is a small pill label (e.g. "New," "Sale") using one of the saturated accent hues, defaulting to accent-red here as a plausible sale-tag color; actual badge-to-color mapping is unverified.

**search** is a pill-shaped input on a soft-gray fill, matching the muted surface tokens observed in the neutral palette; icon placement and expand/collapse behavior are proposed.

**color-swatch** is category-appropriate for kids' apparel: a row of small circular swatches drawn from the ten saturated accents, used to represent print/colorway options on product cards and PDPs; selection state (ink-bordered ring) is proposed.

## Responsive Behavior

This is a recommended breakpoint strategy, not measured site behavior:

| Breakpoint | Width       | Layout guidance                                  |
|-----------|-------------|---------------------------------------------------|
| mobile    | <640px      | Single-column product grid, collapsed nav to menu icon |
| tablet    | 640–1024px  | 2–3 column grid, condensed nav links               |
| desktop   | 1024–1440px | 4-column grid, full nav bar                        |
| wide      | >1440px     | Max-width container (~1440px), extra gutter        |

Touch targets should be at least 44×44px for buttons, swatches, and nav icons on mobile. Navigation is expected to collapse into a slide-out or overlay menu below the tablet breakpoint; this is a proposed pattern, not an observed interaction.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is limited to static CSS extraction (Tailwind reset, a phone-input plugin, and a handful of utility rules); no page-specific component CSS (actual header, hero, product grid, or footer selectors) was supplied.
- Semantic color roles (primary/ink/accent) are inferred from a flat hex list; no rule explicitly binds any hex to a button, link, or badge.
- All typography sizes, weights, and spacing/rounded scales beyond the observed font-family stacks are proposed defaults, not measured from rendered pages.
- Interaction states (hover, focus, active, disabled) beyond the two documented focus/border utility rules are not observed and are marked proposed throughout.
- Mobile/responsive layout, navigation collapse, and breakpoint values are recommendations only; no responsive CSS or viewport behavior was captured.
- "Circular" is used as the declared font-family per CSS evidence; its licensing, availability, and exact weight set are not verified and should be confirmed before implementation.
