---
version: alpha
name: "BlackVue"
source_url: "https://blackvue.com"
captured_at: "2026-09-29T03:59:15.201562+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  BlackVue's storefront (Shopify-based) uses a clinical, tech-forward palette:
  a near-black text ink (#141414) on white canvas, with a single mid-blue
  accent (#2691D0) reserved for primary buttons, links, and interactive
  chrome — explicitly declared as `--color-button` in the CSS custom
  properties. Secondary surfaces lean on light neutrals (#F5F5F5, #F8F8FA,
  #F0F0F0) for section backgrounds and cards, with #E0E0E0/#DEDEDE as
  hairline dividers. A small set of saturated hues (#EB001B, #F79E1B,
  #FF5F00, #142FBD, #007AFF) appear in the evidence but read as third-party
  payment/social iconography rather than brand colors; they are excluded
  from primary roles and only referenced where a badge/utility accent is
  useful. Typography is Open Sans throughout (body and menu), set at a
  16px/1.5 base — no display or heading webfont was distinguished in the
  evidence, so heading sizes below are proposed, not measured. Radius and
  spacing values are not directly evidenced beyond the 8px button radius
  and 60px header height, so the broader scale is inferred from that single
  data point to keep the system internally consistent for a security/tech
  product line (dash cams, fleet hardware) that benefits from crisp,
  low-ornamentation surfaces.

colors:
  primary: "#2691d0"
  ink: "#141414"
  canvas: "#ffffff"
  body: "#1f1f1f"
  muted: "#c8c8c8"
  hairline: "#e0e0e0"
  surface-soft: "#f5f5f5"
  surface-card: "#f8f8fa"
  on-primary: "#ffffff"
  surface-inverse: "#121212"
  border-strong: "#bfbfbf"
  danger: "#eb5757"
  focus: "#007aff"
  overlay-light: "#ffffff80"
  shadow-soft: "#0000000d"
typography:
  display-xl: {fontFamily: "Open Sans, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Open Sans, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Open Sans, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: "60px"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    priceTypography: "{typography.title-md}"
    labelTypography: "{typography.caption}"
  hero:
    backgroundColor: "{colors.surface-inverse}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-inverse}"
    textColor: "{colors.overlay-light}"
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
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  fleet-tracking-panel:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"

## Components

**button-primary** — The site's single declared interactive accent (`--color-button: 38,145,208`), used for "Buy Now" and header CTAs. White text on the blue fill was confirmed via `--color-button-text`. Hover state color exists in CSS but its hex falls outside the supplied palette, so hover is proposed as a token-shift rather than a new literal.

**button-secondary** — Inferred from `--color-button-secondary` (246,246,246 background / dark text), used for tertiary actions like "View More" links. Border/hairline is proposed to give definition on white backgrounds.

**text-input** — Not directly observed in the supplied CSS; proposed using the same hairline and radius language as buttons for consistency across account/login and search forms referenced in the nav ("Log in", "Create Account").

**nav-bar** — Reflects the observed `--header-height: 60px` and the header's conditional theming (`slide-dark-header`, `.fixed` states) that swap text/icon color between white and black depending on scroll and template. Background transitions from transparent-over-hero to solid white on scroll, per the `.fixed .header-wrapper` rule.

**product-card** — Proposed pattern for the repeated ELITE/SAFY product listings (name, price, "Buy Now"). Card surface uses the lighter `#f8f8fa` tone seen in the palette; price and title weight are inferred from typical Shopify catalog structure, not measured directly.

**hero** — Modeled on the homepage's full-bleed promotional banners ("The New ELITE 10 Cabin", "FLEETA CAM"). Dark inverse surface is proposed since header text switches to white over hero imagery (`.body-template-index ... color: #ffffff`), implying a dark or photographic hero background.

**footer** — Proposed dark surface consistent with the inverse header state and typical automotive-electronics footers; overlay-light text token accounts for reduced-contrast secondary footer links.

**badge** — Proposed for "Sale" / discount callouts (e.g., "5% OFF") using the palette's red (#EB5757) as a warning/promo accent, distinct from the payment-icon reds excluded from brand roles.

**search** — Proposed lightweight input styling matching text-input, for the header search affordance implied by standard Shopify header markup (not explicitly present in the supplied excerpt).

**fleet-tracking-panel** — Category-specific component for the "Real-Time Fleet Tracking" / FLEET dashboard promotion, styled as a card with the primary blue as a live-status accent (e.g., map pins, live indicators). Entirely proposed; no dashboard UI was present in the supplied evidence.

## Responsive Behavior

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | <640px | Single-column product grid; nav collapses to hamburger; header height may compress below the observed 60px. |
| Tablet | 640–1024px | 2-column product/category grids; sticky header remains 60px. |
| Desktop | 1024–1440px | Full mega-menu (Dashcams/Accessories/FLEET) as inline lists per observed `.list-menu--inline` structure. |
| Wide | >1440px | Max-width content container; hero imagery scales without additional breakpoints observed. |

Touch targets should be a minimum 44px height for buttons and nav items on mobile, though this is a UX-standard recommendation, not a measured site value. Header collapse behavior (transparent → solid white on scroll) is confirmed in CSS via `.fixed` class toggling but its scroll-trigger threshold and mobile menu animation were not present in the supplied evidence. This table is a design recommendation, not measured site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This DESIGN.md is derived from a static CSS/text snapshot and cannot confirm real rendered layout, breakpoints, or interaction states (hover/focus/active) beyond what appears literally in the declarations. The `--color-foreground-secondary` (115,115,115 / #737373) and button-hover (52,168,236 / #34A8EC) values were referenced in CSS but fall outside the supplied hex palette, so no "muted" or "hover" role could be built from them directly — `#c8c8c8` was substituted as an inferred muted approximation. Several palette entries (#EB001B, #F79E1B, #FF5F00, #142FBD, #1532CB, #1990C6, #136F99, #007AFF) closely resemble third-party payment/card-network and social-icon colors rather than brand-authored tokens; they are treated as non-primary and mostly excluded. Heading sizes, card layout, grid columns, and footer structure are proposed patterns based on typical e-commerce conventions, not measured DOM/visual output. The observed `--spaced-section: 16rem` (256px) section spacing was not adopted verbatim into the fixed spacing scale to preserve a conventional 8-point rhythm; this discrepancy should be reconciled against live rendering if precision matters. Font availability, licensing, and whether "Open Sans" is self-hosted or a Google Fonts import were not verified. Mobile menu behavior, cart drawer, and modal styling were not present in the supplied evidence.
