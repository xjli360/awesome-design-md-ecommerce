---
version: alpha
name: "Marshall"
source_url: "https://marshallheadphones.com"
captured_at: "2026-09-28T04:55:25.959453+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Marshall Headphones' evidenced CSS shows a black-canvas storefront (`body{background:#000000}`)
  set against a NeueHelvetica sans-serif body face with generic system-ui/sans-serif fallback,
  reflecting the brand's rock-heritage, amp-black aesthetic rather than a light e-commerce look.
  Body copy resolves to a mid-grey (#595959) with white as inverse/on-dark text, and the
  supplied palette includes a distinct red cluster (#e42a2a, #f63131, #ca1d1d) that is treated
  here as the brand accent for CTAs, sale badges and the "Iconic Duo Deal" style callouts,
  since no CSS variable explicitly labels a "--brand-primary" token. A second, unlabeled
  cluster (#1d7732/#2a9e43 green, #8371f2 purple, #e8f4f9 pale blue) is inferred as semantic
  UI status color (stock/availability, membership tiers) rather than core brand identity. The
  large yellow/orange/red numeric scales and Chakra gray ramp are Chakra UI framework defaults
  (light/dark theme tokens) and are mapped here only to structural roles (borders, subtle
  surfaces) rather than brand meaning. A "SexPistols" font family appears in the evidence but
  is not confirmed as licensed for production use, so it is excluded from typography tokens.

colors:
  primary: "#e42a2a"
  ink: "#000000"
  canvas: "#000000"
  body: "#595959"
  muted: "#8c8c8c"
  hairline: "#333333"
  surface-soft: "#1a1a1a"
  surface-card: "#262626"
  on-primary: "#ffffff"
  surface-light: "#f2f2f2"
  border-light: "#e6e6e6"
  gray-mid: "#a6a6a6"
  success: "#2a9e43"
  success-soft: "#aaddaa"
  danger: "#ca1d1d"
  info-soft: "#e8f4f9"
  accent-alt: "#8371f2"
typography:
  display-xl: {fontFamily: "NeueHelvetica, system-ui, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "NeueHelvetica, system-ui, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "NeueHelvetica, system-ui, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "NeueHelvetica, system-ui, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "NeueHelvetica, system-ui, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "NeueHelvetica, system-ui, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "NeueHelvetica, system-ui, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
  mono-caption: {fontFamily: "SFMono-Regular, Consolas, Menlo, Monaco, monospace", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
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
    textColor: "{colors.on-primary}"
    borderColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-highlight:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.accent-alt}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** renders the site's red accent (`{colors.primary}`) as a solid fill for main calls to action such as "Shop now"; white text on red is proposed for AA contrast, and hover/pressed states are not observed and remain proposed (e.g., slight darken toward `{colors.danger}`).

**button-secondary** is an outline variant for secondary actions ("Find out more") on the black canvas, using white borders/text on transparent background; useful where a solid red button would compete visually with a nearby primary CTA.

**text-input** uses a dark surface (`{colors.surface-soft}`) with a subtle hairline border, matching the site's dark-first shell; focus-ring styling is not confirmed in the evidence and is proposed.

**nav-bar** sits on the black canvas with white type and a hairline divider beneath it; the evidence shows nested category links (Amps, Speakers, Headphones, Drums, Clothing) implying a multi-level flyout, whose exact open/hover behavior is not observed.

**product-card** groups imagery, title, and price on a slightly lighter card surface than the page background, giving product tiles separation from the black canvas in grid contexts like "Emberton III" or "Milton A.N.C." listings.

**hero** is a full-bleed black section pattern inferred from repeated homepage promo blocks (Milton A.N.C., Stanmore IV, Heston 120); large display type plus a single primary CTA is proposed as the template.

**footer** carries the muted grey body color over black, with support/company/shop link columns matching the page-text structure (Support, Company, Shop); link hover states are proposed.

**badge** is a small pill using the red accent, suited to labels like "Award-winning" or sale/deal callouts ("ICONIC DUO DEAL"); color choice for non-promotional badges (e.g., stock status) should draw from `{colors.success}`/`{colors.danger}` instead, proposed.

**search** is a dark, low-contrast field intended for the header/nav search entry point; no icon or autocomplete styling was observed and is proposed.

**spec-highlight** is a category-appropriate component for headphone/earbud detail pages, surfacing a single spec (battery life, ANC, colour) in a card with an accent value color; this pattern is proposed to support the site's repeated battery-life and feature callouts (e.g., "Battery life that plays the Hendrix discography on a single charge").

## Responsive Behavior
Recommended, not measured, breakpoints:

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| sm | ≤480px | Single-column stack, nav collapses to menu icon, hero text/CTA full width |
| md | 481–768px | 2-column product grids, sticky header retained |
| lg | 769–1024px | 3-column product grids, inline nav categories |
| xl | ≥1025px | 4+ column grids, full mega-menu nav |

Touch targets should be at minimum 44×44px for nav and CTA buttons. Nav should collapse into a hamburger/menu icon below `md`. None of the above breakpoint values or collapse behaviors were directly observed in the supplied CSS; they are conventional defaults for a storefront of this category.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from a static CSS/text snapshot, not a rendered or interactive audit. The palette mixes what appear to be Chakra UI framework default color ramps (gray/red/orange/yellow scales, e.g. `#edf2f7`…`#171923`, `#fff5f5`…`#63171b`) with a smaller set of colors more plausibly tied to brand/semantic use (`#e42a2a`, `#ca1d1d`, `#2a9e43`, `#8371f2`); the primary/accent, success, danger, and info-soft role assignments are inferred, not confirmed via a labeled brand token. Exact rendered `font-size`/`line-height` in pixels depends on the page's root font-size, which was not supplied, so `body-md` sizing is a best-effort conversion from the observed `1.6rem`/`2.4rem` ratio. The "SexPistols" font family is observed only as a family name in the CSS bundle; its use, availability, and licensing are unverified, so it is excluded from the typography tokens above. No hover, focus, active, error, or mobile-menu states were observed; all interaction states and the entire Responsive Behavior table are proposed conventions for this product category, not measured site behavior. Component paddings, radii, and spacing values are proposed defaults consistent with the supplied spacing/rounded scale, not extracted layout measurements.
