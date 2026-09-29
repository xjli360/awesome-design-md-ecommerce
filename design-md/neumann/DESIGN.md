---
version: alpha
name: "Neumann"
source_url: "https://www.neumann.com"
captured_at: "2026-09-28T04:43:14.765696+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Neumann's site evidence shows a professional-audio brand built on high-contrast
  neutrals — pure black (#000000), near-black panel tones (#141414, #18191a), and
  white (#ffffff) — accented by a single warm orange (#f18823) that appears
  consistently as the hover/active state on buttons and comparison UI. Supporting
  grays (#f7f7f7, #e5e5e5, #8c8c8c, #333333) structure text, dividers, and disabled
  states drawn directly from the mega-menu component CSS. A wide secondary swatch
  set (bootstrap-style success/warning/info/pink hues) appears in the raw palette
  but is not tied to any captured selector, so it is treated here only as optional
  status-color inference, not confirmed brand color.
  The only text font family present in evidence is "FFUnit", paired with icon
  fonts (icomoon, swiper-icons) used solely for glyphs, not body copy. This
  interpretation treats FFUnit as the sole observed brand typeface with sans-serif
  fallback, and proposes a conservative type scale since only the 18px/400/1.5
  button style is explicitly measured. Component shapes (sharp 0px button radius,
  dark mega-menu panel at #18191a, circular 16px compare badge) are taken directly
  from CSS; all other layout, spacing, and interaction behavior is inferred or
  proposed for a technical, minimal, studio-equipment aesthetic.

colors:
  primary: "#f18823"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#8c8c8c"
  hairline: "#e5e5e5"
  surface-soft: "#f7f7f7"
  surface-card: "#18191a"
  on-primary: "#141414"
  surface-dark: "#141414"
  border-strong: "#c1c1c1"
  danger: "#ae262f"
  success: "#198754"
  warning: "#ff9900"
typography:
  display-xl: {fontFamily: "FFUnit, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "FFUnit, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "FFUnit, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "FFUnit, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "FFUnit, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "FFUnit, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "FFUnit, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
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
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    borderColor: "{colors.surface-soft}"
    hoverTextColor: "{colors.primary}"
    hoverBorderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.base}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.surface-soft}"
    hoverBackgroundColor: "{colors.primary}"
    hoverTextColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.base}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.canvas}"
    dividerColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    linkColor: "{colors.canvas}"
    dividerColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.xs}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.body}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  spec-comparison-panel:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.canvas}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"

## Components

**button-primary** reflects the observed `.button--FjSdZ` rule directly: a dark neutral fill, white text, light-gray border, sharp 0px corners, and 18px/400-weight type at 12px/16px padding. The hover state swapping text/border to the orange accent is an observed CSS custom-property transition, not a live-rendered confirmation.

**button-secondary** is inferred from the `.secondary--OA6Lh` variant, which swaps to a lighter neutral background and shifts to the brand accent on hover/active. The exact `--bs-grey-button` hex was not resolvable from evidence, so `surface-soft` is used as a reasonable proxy.

**text-input** is a proposed pattern; no form-field CSS was captured, so neutral canvas/hairline styling with an orange focus ring is a conventional, unconfirmed default.

**nav-bar** models the mega-menu's dark aside panel, whose background (`#18191a`) is explicitly observed in `.aside-body--wBFYH`. Divider and text treatment beyond that single rule are proposed.

**product-card** is a proposed pattern for microphone/monitor listing tiles; no card selector was present in evidence, so soft surface, hairline border, and modest rounding are conservative defaults for a technical product catalog.

**hero** is proposed for homepage banner messaging (e.g., "KH Family," "MT 48") using the large display type scale; no hero-specific CSS was captured.

**footer** is proposed from the page's extensive legal/navigation link list (Imprint, Privacy, Terms), styled dark with muted secondary links, consistent with the brand's dark-neutral system.

**badge** is grounded in `.comparison-lists-node-button--Ny9U_`: a small circular counter with `border-radius:50%`, dark text on the brand secondary color — mapped here to `primary` on `ink`.

**search / spec-comparison-panel** extend the observed `products-category-filtering` and `toggle-compare-button` classes, representing the filtering/compare tray used when browsing microphone models; border and panel colors are approximated from the closest observed neutrals since exact bootstrap-variable hexes were not resolved.

## Responsive Behavior
Recommended, not measured:

| Breakpoint | Width      | Behavior (proposed)                        |
|-----------|------------|---------------------------------------------|
| sm        | <576px     | Single-column, nav collapses to icon/drawer |
| md        | 576–991px  | 2-column product grids, mega-menu simplifies |
| lg        | 992–1199px | Full mega-menu, 3–4 column grids            |
| xl        | ≥1200px    | Max-width container, full desktop layout    |

Touch targets should be at least 44×44px; the dark mega-menu aside (max-width 348px, per evidence) suggests a slide-in drawer pattern on small screens. No mobile viewport or breakpoint values were directly observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Extraction is static CSS/text only; no rendered layout, real breakpoints, or interaction states (focus, active, transitions in motion) were observed.
- Several palette entries (bootstrap-style success/warning/info/pink tones) have no linked selector and are only optionally used as status-color inference.
- `--bs-grey-button` and `--bs-secondary` CSS variables are referenced but their resolved hex values were not present in evidence; approximations are labeled inferred.
- Typography sizes beyond the single observed button rule (18px/400/1.5) are proposed, not measured.
- FFUnit is treated as a proprietary/custom font; its licensing and actual availability were not verified.
- Mobile navigation, product-card, hero, and footer visuals are proposed patterns with no direct supporting CSS captured.
