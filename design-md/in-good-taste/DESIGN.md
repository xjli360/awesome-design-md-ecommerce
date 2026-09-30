---
version: alpha
name: "In Good Taste"
source_url: "https://ingoodtaste.com"
captured_at: "2026-09-28T10:22:12.334112+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  In Good Taste is a Sonoma-based DTC wine brand built around advent-calendar tasting flights of 187ml bottles. The observed CSS confirms a warm, editorial palette: a coral-red accent (#f94938) drives buttons, review widgets, and section titles against a soft blush canvas (#faf3f1) and near-black ink (#1e1e1e/#020617) body copy on white. A secondary set of theme color variables (--color_1 through --color_6, teal, plum, terracotta, violet) appears defined in the stylesheet but its on-page role is unconfirmed, so those are treated as inferred accent options rather than primary brand colors. The confirmed body font is Visby, falling back to Arial and system sans-serif; no serif or display webfont was observed in the CSS, so all typography tokens below use the Visby/Arial/sans-serif stack, with weight and size differences proposed to create hierarchy for hero, product-card, and calendar-door content. Rounded corners and spacing follow a conventional soft-retail scale (generous radii, moderate section spacing) appropriate to a gift-forward, unboxing-driven commerce experience, though exact pixel values are proposed defaults, not measured from layout.

colors:
  primary: "#f94938"
  ink: "#1e1e1e"
  canvas: "#ffffff"
  body: "#1e1e1e"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#faf3f1"
  surface-card: "#fdf1ef"
  on-primary: "#ffffff"
  accent-teal: "#1b4c62"
  accent-terracotta: "#cc4e32"
  accent-plum: "#5f1f5b"
  accent-gold: "#e8a44b"
  border-black: "#020617"
typography:
  display-xl: {fontFamily: "Visby, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Visby, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Visby, Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Visby, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Visby, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Visby, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Visby, Arial, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.3px}
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
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl} {spacing.xl}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  advent-calendar-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent-gold}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm}"
    numberTypography: "{typography.title-md}"

## Components

**button-primary** is the coral CTA used repeatedly for "Add to cart" and "Shop Now" actions, matching the `#f94938` background/white-text pairing confirmed in the featured-products CSS.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Learn More", "Choose options" contexts) using the same coral as border/text on a transparent field; hover/active states are proposed, not observed.

**text-input** covers search and email-capture fields; background, border, and padding are proposed conventions since no explicit input styling was supplied in evidence.

**nav-bar** represents the top utility/menu bar implied by the multiple repeated navigation labels ("Shop All", "Advent Wine Club", "Log in/Sign up") in the page text; exact height, sticky behavior, and mobile collapse are not observed.

**product-card** models the repeated calendar/gift-set listings (title, feature bullets, strikethrough price, CTA) seen in the text excerpt; the soft blush card surface is inferred from `#faf3f1`/`#fdf1ef` backgrounds used elsewhere in the CSS.

**hero** represents the top banner promoting the 2026 Advent Calendar preorder; the blush background and dark ink text reuse the confirmed `#faf3f1`/`#1e1e1e` pairing from the template block.

**footer** is a proposed dark-ink footer for legal/newsletter content, inverting ink and canvas roles; no footer-specific CSS was supplied.

**badge** is a proposed small pill (e.g., "Sold out," "Save $18," rating stars) using the coral primary, consistent with the Judge.me widget's coral/rounded review styling (`--jdgm-primary-color`, `--jdgm-border-radius`).

**search** is a proposed pill-shaped input for site search, styled consistently with other rounded UI elements; not directly observed in evidence.

**advent-calendar-tile** is a category-specific component representing a single "door" of the wine advent calendar grid, using the gold accent (`#e8a44b`) as a proposed highlight color for numbering/interaction, since the product is structurally built around 24 daily reveals.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| small | ≤480px | Single-column product/calendar grid, stacked nav, full-width buttons |
| mobile | ≤768px | 2-column calendar/product grid, collapsed hamburger nav |
| tablet | ≤976px | 3-column grid, inline nav with condensed labels |
| desktop | ≥1300px | 4–6 column grid, full nav bar, persistent hero media |

Touch targets should be at minimum 44×44px for cart/CTA buttons; nav collapses to a drawer or hamburger below tablet width. These values derive from the `--small-resolution`, `--mobile-resolution`, `--tablet-resolution`, and `--desktop-resolution` CSS variables present in evidence, but actual grid/column behavior at each breakpoint was not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.




- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS/text extraction only; no live rendering, JavaScript-driven interaction, or mobile viewport testing was performed. The secondary theme color variables (`--color_1` through `--color_6`) are present in the stylesheet but their applied UI role is unconfirmed, so they are treated as optional/inferred accents rather than primary brand colors. All typography sizes, weights, and letter-spacing values beyond the confirmed body `font-size:1.6rem; line-height:1.5; font-family:Visby,Arial,sans-serif` are proposed for hierarchy and not measured from rendered headings. Rounded-corner and spacing scales follow a generic proposed system, aside from the `--jdgm-border-radius: 10` variable tied specifically to the review widget. Font availability, licensing, and fallback behavior for "Visby" were not verified. Component states (hover, focus, disabled, error) are proposed conventions, not observed interactions.
