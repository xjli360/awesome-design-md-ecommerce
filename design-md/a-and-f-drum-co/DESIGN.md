---
version: alpha
name: "A&F Drum Co"
source_url: "https://www.anfdrumco.com"
captured_at: "2026-09-28T05:07:47.305346+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A&F Drum Co is a handmade luxury drum manufacturer based in Austin, Texas, selling snares,
  kits, cymbals, and hardware through a Shopify storefront. The observed CSS shows a dark,
  near-black header (#161010) paired with a warm brass/bronze accent (#a68247) used for primary
  buttons, evoking the metal finishes (raw brass, copper, nickel) central to the product line.
  Body copy renders in a neutral mid-gray (#4a4a4a) on white and warm off-white surfaces
  (#f4f1ec, #faf9f6), suggesting a workshop-clean, editorial aesthetic rather than a saturated
  retail look. A muted red (#952123) appears only on the cart-notification bubble, so it is
  treated here as a small status/accent color rather than a brand color. Buttons are square
  (border-radius: 0), uppercase, bold, and letter-spaced, reinforcing an industrial, engraved-
  metal character consistent with the brand's hand-engraving and metalwork imagery.
  Typography is system/web-safe (Avenir with Helvetica Neue/Helvetica/Arial fallbacks); no
  custom webfont file was confirmed in evidence. Heading sizes, the full spacing scale, and
  rounded-corner scale beyond the observed zero-radius buttons are proposed conventions for a
  premium e-commerce interpretation, not measured values. Semantic color roles (ink, muted,
  hairline) are inferred from usage context in the supplied CSS, not confirmed design tokens.

colors:
  primary: "#a68247"
  ink: "#161010"
  canvas: "#ffffff"
  body: "#4a4a4a"
  muted: "#777777"
  hairline: "#dddddd"
  surface-soft: "#f4f1ec"
  surface-card: "#faf9f6"
  on-primary: "#ffffff"
  accent-danger: "#952123"
  accent-alert: "#eb4f47"
  line-dark: "#333333"
  warm-tint: "#ebe5dc"
typography:
  display-xl: {fontFamily: "'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Avenir', 'HelveticaNeue', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.625, letterSpacing: 0px}
  body-sm: {fontFamily: "'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 2.2, letterSpacing: 1.5px}
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
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.body}"
    minHeight: "60px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    overlay: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-danger}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    size: "10px"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
  finish-swatch-selector:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    activeBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs}"

## Components

**button-primary** — Solid brass-gold fill with white uppercase, letter-spaced label and a square
corner, matching the observed `.btn` rule (`background-color: #a68247; border-radius: 0;
text-transform: uppercase; letter-spacing: 1.5px`). Used for primary calls to action like "Add to
Cart" or "View Collection."

**button-secondary** — A transparent, hairline-bordered variant (proposed) for secondary actions
such as "View" links seen throughout the collection menu (e.g., "Copper Snares — View"). Text
color matches observed body gray.

**text-input** — Proposed form field treatment for account, checkout, and newsletter signup
fields, using the observed hairline gray for borders and body-md typography for entered text.

**nav-bar** — The dark, near-black wrapper (`#161010`) observed on `.site-header__wrapper`,
60px minimum height, white logo/text in transparent-header state. Holds the deep drum-category
mega menu (Snares, Metal Kits, Wood Kits, Percussion, Cymbals & Accessories, etc.).

**product-card** — Proposed card pattern for collection grids (snares, kits, cymbals), using the
warm off-white surface-card background and hairline border to separate product photography from
the page background without heavy shadows, consistent with the site's understated palette.

**hero** — Proposed full-bleed banner using the ink background and white display type, mirroring
the transparent-header/dark-hero pairing implied by `.site-header--transparent` overriding to a
transparent wrapper over dark imagery (e.g., the homepage slider and video section).

**footer** — Dark ink-background footer (inferred consistent with header) housing social links,
contact, and legal pages ("Terms and Conditions," "FAQ/Refund Policy") noted in page text.

**badge** — Small circular indicator using the observed `.site-header__cart-bubble` red
(`#952123`), a 10px dot signaling cart item count; proposed default hidden/opacity-0 state per
CSS transition rule.

**search** — Simple bordered input matching the site's search icon/flow ("🔎 Search … Search
again"), styled consistently with text-input but reserved for the header search overlay.

**finish-swatch-selector** — A category-appropriate, proposed component for selecting drum
finishes (Raw Brass, Copper, Nickel over Brass, Raw Steel, Wood, etc.), rendered as small round
swatches with a brass-gold active-state ring, reflecting the extensive finish taxonomy in the
navigation.

## Responsive Behavior

This is a recommended breakpoint structure, not measured site behavior:

| Breakpoint | Width       | Notes (proposed)                                  |
|------------|-------------|----------------------------------------------------|
| mobile     | < 480px     | Single-column product grid; nav collapses to burger |
| tablet     | 480–1024px  | 2-column product grid; mega-menu becomes accordion  |
| desktop    | 1024–1440px | 3–4 column grid; full mega navigation visible        |
| wide       | > 1440px    | Max-width content container, generous side margins   |

Touch targets on buttons and nav items should be at least 44px tall, consistent with the
observed `.shopify-payment-button__button` clamp (25–55px) as a reference range. The mega
navigation (Drums, Snares, Metal Kits, Wood Kits, Percussion, Cymbals & Accessories, Gadgets,
Heads and Wires, Merch) should collapse into a single scrollable drawer on mobile; specific
collapse/animation behavior was not observed and is proposed only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS and page-text evidence only; no rendered layout,
responsive breakpoints, hover/focus states, or JavaScript-driven interactions (mega-menu
behavior, cart drawer animation, video autoplay) were directly observed. Several palette colors
(e.g., `#0078a8`, `#1990c6`, `#3388ff`, `#54ca80`) appear in the source but have unclear or
utility/plugin-level roles (map/leaflet UI, third-party embeds) and were excluded from the core
brand palette rather than guessed into semantic roles. Heading sizes, spacing scale, and rounded
scale beyond the confirmed zero-radius buttons/checkout controls are proposed design
conventions, not measured values. Font rendering relies on system fallbacks (Avenir, Helvetica
Neue, Helvetica, Arial); no custom webfont file or license was confirmed in the supplied
evidence. Color-role assignments (ink, muted, hairline, surface-soft/card) are inferred from
selector context, not confirmed brand guidelines.
