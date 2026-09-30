---
version: alpha
name: "Pet Honesty"
source_url: "https://pethonesty.com"
captured_at: "2026-09-28T04:48:09.609562+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The evidence shows a neutral-first system: near-black text (#1e1e1e, #333333) on white/off-white
  canvases (#ffffff, #f6f6f6, #fafafa), with a warm cream section tone (#f5f4f0) and a soft beige
  hairline/border tone (#dad2c6). A dark teal (#1e534d) appears in the source palette distinctly from
  the grays and is inferred here as the primary brand color, consistent with a "clean, trustworthy
  pet-health" positioning implied by the copy ("clean, transparent ingredients," "The Honest
  Difference"). Orange (#faa624) is explicitly tied to review-star tokens and is proposed as a
  secondary accent for ratings and CTAs. Magenta (#c2208e) and teal-cyan (#26b8c3) are present in the
  palette and are inferred as promotional/category accent colors (e.g., "For Cats" or sale badges),
  since no selector evidence ties them to a specific UI role. Status colors (success/warning/error/info)
  are explicitly defined as CSS custom properties and are mapped directly.
  Typography is anchored on 'Museo Sans' for body copy (16px/1.5, observed) and 'Museo Sans Display'
  for headings (36px/900 and 25px/900, both observed via richtext h1 rules). A distinctive script
  family, 'rychard walker', is observed at 32px on product-detail headings and is treated as a
  decorative accent face rather than a body font. All sizes not directly observed are labeled proposed.

colors:
  primary: "#1e534d"
  ink: "#1e1e1e"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#707070"
  hairline: "#dedede"
  surface-soft: "#f6f6f6"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-orange: "#faa624"
  accent-pink: "#c2208e"
  accent-teal: "#26b8c3"
  cream: "#f5f4f0"
  beige: "#dad2c6"
  success: "#22c55e"
  success-text: "#0b4320"
  warning: "#f59e0b"
  warning-text: "#634004"
  error: "#fc0000"
  error-text: "#630000"
  info: "#38bdf8"
  info-text: "#056792"

typography:
  display-xl: {fontFamily: "'Museo Sans Display', sans-serif", fontSize: 44px, fontWeight: 900, lineHeight: 1.2, letterSpacing: -0.4px}
  display-md: {fontFamily: "'Museo Sans Display', sans-serif", fontSize: 36px, fontWeight: 900, lineHeight: 1.3, letterSpacing: -0.36px}
  title-md: {fontFamily: "'Museo Sans Display', sans-serif", fontSize: 25px, fontWeight: 900, lineHeight: 1.3, letterSpacing: -0.36px}
  accent-script: {fontFamily: "'rychard walker', cursive", fontSize: 32px, fontWeight: 400, lineHeight: 1.26, letterSpacing: -0.32px}
  body-md: {fontFamily: "'Museo Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Museo Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Museo Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Museo Sans Display', sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.2px}

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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  hero:
    backgroundColor: "{colors.cream}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  subscription-callout:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base} {spacing.lg}"

## Components

**button-primary** — Solid teal fill intended for the main "Shop now" / add-to-cart actions implied by the copy. Rounded corners are proposed (sm) since no border-radius was captured in the supplied CSS rules.

**button-secondary** — An outlined variant for lower-priority actions ("Learn," "Take Our Quiz"), sharing the primary color as text/border on a transparent background. State transitions (hover/active) are proposed, not observed.

**text-input** — A bordered field for the newsletter "Email / Submit" capture seen in the footer copy. Border uses the observed light hairline gray; focus/error states are proposed and would logically map to `{colors.error}`/`{colors.info}`.

**nav-bar** — Modeled on the `--header-height` custom properties, which combine an announcement bar, progress bar, and navigation bar into one stacked header. Sticky behavior is inferred from the variable structure, not confirmed via computed styles.

**hero** — A large banner area using the observed 36px/900-weight display heading on a warm cream background, matching the page's promotional messaging ("Real Results, Powered By Real Ingredients"). Background tone is inferred, not tied to a specific selector.

**product-card** — Represents best-seller/category tiles (Multivitamins, Allergy, Digestive, Skin+Coat). Card surface, radius, and padding are proposed conventions since no card-specific selector was supplied.

**footer** — Dark, ink-colored footer housing the multi-column "Information / About / Connect / Stay in Touch" link groups and payment-method icons referenced in the page text. Link and text colors are inferred for contrast against the dark background.

**badge** — A small pill for "NEW," "Sale," and free-gift/threshold messaging ("Choose a free gift on orders over $60!"). Orange was chosen because it is the only accent explicitly tied to a named token (`--color-review-stars`) in the supplied CSS.

**search** — A pill-shaped input, proposed for product discovery; no search-specific markup was present in the evidence, so this is a category-standard convention rather than an observed pattern.

**subscription-callout** — A category-appropriate component reflecting the recurring-purchase model central to pet supplement e-commerce ("Subscribe & save on every order!", "Earn points on every purchase"). Uses the teal accent to visually differentiate loyalty/subscription messaging from standard product content; entirely proposed styling.

## Responsive Behavior

This is a recommendation, not measured site behavior — no media queries or breakpoint-specific rules were present in the supplied evidence beyond the `--layout-page-width-*` tokens (640 / 1280 / 1440 / 1640px), which are used here only as directional signals.

| Breakpoint | Width       | Layout guidance (proposed)                          |
|------------|-------------|------------------------------------------------------|
| xs         | ≤640px      | Single-column stack; nav collapses to hamburger menu |
| sm         | 641–1280px  | 2-column product grids; sticky header condenses       |
| md         | 1281–1440px | 3-column product grids; full nav visible               |
| lg         | 1441–1640px | Max-width content container centered, wide gutters     |

Touch targets should be at least 44×44px for buttons and nav items (proposed, not measured). Below `sm`, the announcement/progress/nav header stack (implied by `--header-height`) should collapse vertically to conserve space, and search/cart icons should remain persistently visible per typical e-commerce convention — this is an inferred pattern, not confirmed from the source.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted statically; no computed layout, hover/focus states, or JavaScript-driven interactions (e.g., quiz flow, cart drawer, subscription modal) were observed.
- Many palette values (e.g., #e8ff00, #00ff07, #f1ec08, #cbf37a, #eaf37a) appear to originate from category iconography or illustrations rather than core UI chrome; they were excluded from the design token set as their semantic role is unclear.
- The mapping of #1e534d to "primary" and #c2208e/#26b8c3 to accent roles is inferred from palette prominence and thematic fit, not from selector-level confirmation.
- Font sizes for body-sm, caption, button-md, display-xl, and all spacing/rounded values are proposed conventions, not values captured in the supplied CSS rules.
- The custom fonts 'Museo Sans', 'Museo Sans Display', and 'rychard walker' are used as observed family names only; licensing, weight availability, and web-font delivery were not verified.
- Component states (hover, active, disabled, error) and exact card/button border-radius values were not present in the evidence and are marked proposed throughout.
