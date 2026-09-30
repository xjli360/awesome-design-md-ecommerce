---
version: alpha
name: "Amrapali"
source_url: "https://www.amrapalijewels.com"
captured_at: "2026-09-28T04:15:20.098490+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Amrapali's observed CSS shows a stark black-and-white foundation (#000000, #ffffff) overlaid with a single saturated red accent (#e11931) used consistently as a hover/interaction color on buttons and links. Supporting neutrals (#868686, #bbbbbb, #f5f5f5, #f8f8f8, #dcdcdc, #e7e7e7) appear in hairlines, topbar borders, and light surface fills, suggesting a minimal, editorial UI scaffold typical of a Shopify theme (wpbingo page-builder classes are visible throughout).
  Two verified font families anchor the type system: Cormorant Garamond, a high-contrast serif well suited to the brand's heritage/ethnic jewelry positioning, and Lato, a neutral grotesque used for UI chrome (buttons show font-size:11px, font-weight:500, letter-spacing:2px). Feather, icomoon, and wpbingofont are icon fonts, not text faces, and are excluded from typographic roles.
  This interpretation assigns Cormorant Garamond to display/heading roles to evoke craft and tradition, and Lato to body/UI text for legibility. Gold (#d49a06) and rose (#b76e79) tones present in the palette are inferred as decorative accent options for jewelry-metal cues (gold/rose-gold) though no CSS rule confirms their applied role. All layout, spacing, and component states beyond the literal button/topbar rules are proposed, not observed.

colors:
  primary: "#e11931"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#868686"
  hairline: "#bbbbbb"
  surface-soft: "#f5f5f5"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  border-light: "#e7e7e7"
  divider: "#dcdcdc"
  accent-gold: "#d49a06"
  accent-rose: "#b76e79"
typography:
  display-xl: {fontFamily: "Cormorant Garamond, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Cormorant Garamond, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Cormorant Garamond, serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Lato, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Lato, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Lato, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Lato, sans-serif", fontSize: 11px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 2px}
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
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-light}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    iconColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  heritage-collection-tile:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.accent-gold}"
    titleTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"

## Components

**button-primary** is the filled call-to-action seen in hover states of homepage banner buttons (`background:#e11931`), used for primary conversion actions like "Shop Now." Its resting state in the CSS is transparent-with-outline; the filled red only appears on `:hover`, so the always-filled variant here is a proposed normalization for consistent CTA affordance.

**button-secondary** reflects the observed default (unhovered) outline button style: transparent background, dark border and text, sharp corners (`border-radius:0`). This is a directly observed pattern from the homepage button blocks, generalized as a reusable secondary action.

**text-input** is proposed for search and account forms; no input-specific CSS was captured, so border color, radius, and padding follow the neutral hairline/surface tokens as a plausible, unobserved default.

**nav-bar** reflects the transparent-over-black header seen on the homepage template (`body.template-index .header-desktop`), where nav links, search, account, and cart icons all render in white against the dark hero. Sticky/scrolled header states were not captured and are proposed as inheriting the same tokens with a solid `{colors.ink}` background.

**product-card** is a proposed pattern for jewelry listings, pairing a clean white surface with the serif title face to emphasize craftsmanship; no card markup was present in the supplied evidence.

**hero** models the homepage banner region implied by the topbar/header rules — full-bleed dark background with white overlay text and generous top padding (`60px 0 20px` observed on `.header-desktop`). Exact hero copy layout is not confirmed.

**footer** is proposed using the same dark/light contrast established by the header, assuming continuity of the black-canvas, white-text brand chrome; no footer selectors were supplied.

**badge** is a proposed small label (e.g., "New," "Handcrafted") using the gold accent for a metallic cue appropriate to jewelry merchandising; gold's applied role is inferred from palette presence only.

**search** proposes a light, unobtrusive search affordance using surface-soft, matching the neutral utility grays seen in topbar hairline/border treatments.

**heritage-collection-tile** is a category-appropriate proposed component for curated collection or artisan-story tiles, using a gold hairline border to visually nod to traditional metalwork; entirely a design proposal, not present in the supplied CSS.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <600px | Single-column stacking, nav collapses to hamburger, touch targets ≥44px |
| tablet | 600–1024px | 2-column product grids, header may condense padding |
| desktop | >1024px | Full nav row as observed in `.header-desktop`, multi-column layouts |

Interactive elements (buttons, nav icons, search toggle) should maintain a minimum 44×44px touch target on mobile. Sticky header behavior is implied by the `.bwp-header.sticky` class name but its resulting styles were not supplied, so exact collapse/transition behavior is unverified.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS extraction only; no runtime/browser rendering was observed, so hover, focus, active, and error states beyond the two captured button `:hover` rules are proposed.
- Color-to-role mapping is inferred: only `#ffffff`, `#000000`, `#e11931`, and `#bbbbbb` have direct selector evidence; all other palette entries (including gold, rose, and several UI grays) are assigned roles by plausibility, not confirmed CSS usage.
- Several palette values (`#005bd3`, `#05aa3d`, `#ffc0cb`, `#f61f1f`, `#ffe500`) resemble generic CMS/page-builder swatch defaults and were intentionally excluded from role assignment as likely non-brand utility colors.
- Typography sizes beyond the observed button rule (11px/500/2px) are proposed estimates for a jewelry e-commerce hierarchy, not measured from live pages.
- Feather, icomoon, and wpbingofont are icon fonts; their glyph sets, licensing, and availability were not verified and are excluded from the typographic system.
- No mobile-specific markup, collapsed-nav CSS, or footer selectors were present in the supplied evidence; responsive and footer guidance above is fully proposed.
- Custom font (Cormorant Garamond, Lato) hosting, licensing, and loading strategy were not verified from the supplied evidence.
