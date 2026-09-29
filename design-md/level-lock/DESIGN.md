---
version: alpha
name: "Level Lock"
source_url: "https://level.co"
captured_at: "2026-09-28T04:26:32.128513+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Level Lock's public site evidence points to a minimal, hardware-forward aesthetic built on a warm neutral canvas (cotton-toned #f0efed and #e9e5dd) paired with near-black ink (#151515) for typography and primary actions, echoing the brand's "invisible" lock hardware finishes. CSS custom properties named --color-cotton, --color-charcoal, and --color-slate strongly imply a warm-neutral / near-black / blue-gray triad; "slate" is mapped here to the observed blue-gray #6596ab, used for hover and active navigation states. A thin hairline (#e0e7ec) separates list items and account-menu rows in the observed CSS. Two warm hardware-adjacent tones in the palette — a muted gold (#d6b587) and a terracotta (#c94633) — are proposed as secondary accents for badges or finish-swatches, evocative of physical lock materials such as brass or bronze. Typography draws on the Suisse type family: SuisseWorks is proposed for display/serif headlines and SuisseIntl for UI/body text, both retained with generic fallbacks since custom font licensing and availability are unverified. Header-height and submenu-height CSS variables confirm a floating/sticky top navigation with a secondary page-menu bar, though exact pixel layout beyond these tokens is not measured. All component definitions, type scale sizes, and interaction states below are proposed conventions consistent with the supplied evidence, not confirmed live observations.

colors:
  primary: "#151515"
  ink: "#151515"
  canvas: "#f0efed"
  body: "#3a3a3c"
  muted: "#9ca3af"
  hairline: "#e0e7ec"
  surface-soft: "#e9e5dd"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-slate: "#6596ab"
  accent-gold: "#d6b587"
  accent-terracotta: "#c94633"
  border-subtle: "#d9d9d9"
  overlay-scrim: "#000000cc"
  danger: "#ff0000"
typography:
  display-xl: {fontFamily: "suisseWorks, serif", fontSize: 64px, fontWeight: 500, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "suisseWorks, serif", fontSize: 40px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.25px}
  title-md: {fontFamily: "suisseIntl, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "suisseIntl, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "suisseIntl, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "suisseIntl, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "suisseIntl, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-subtle}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.accent-slate}"
    typography: "{typography.body-sm}"
    height: "60px"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.button-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-subtle}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  lock-status-indicator:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.accent-slate}"
    dangerColor: "{colors.danger}"
    typography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** is a solid near-black CTA (`{colors.primary}`) with white text, used for primary conversions such as "Shop Now" or "Add to Cart." Proposed hover/active states would deepen slightly toward `#000000`; disabled state is not observed.

**button-secondary** is a transparent, hairline-bordered button for tertiary actions (e.g., "Learn more"), sharing the same type scale as the primary button for visual rhythm without competing for attention. Focus/hover treatment is proposed, not confirmed.

**text-input** reflects a plain, low-chrome form field consistent with the site's minimal aesthetic — white surface, subtle border, muted placeholder text. Error and focus-ring states are proposed conventions, not observed in the supplied CSS.

**nav-bar** is derived directly from observed CSS: a `.level-global-header-top-nav` with a `--color-cotton` background and a 60px base height (100px on some breakpoint per the second `body` rule), with active/hover link color shifting to the mapped slate blue-gray. Submenu height is computed from viewport minus nav height, implying a full-height dropdown/overlay pattern.

**product-card** is a proposed pattern for lock/hardware product tiles: white surface, soft hairline border, rounded corners, with a clear title/body/price hierarchy suited to showcasing device finishes and pricing.

**hero** proposes a large, warm-neutral banner section using the display type scale for headline copy, appropriate for showcasing lock hardware photography against the cotton-toned canvas.

**footer** inverts to the near-black ink color with white text and muted-gray links, providing contrast against the light body sections and reinforcing the "invisible hardware, confident brand" visual language.

**badge** and **search** are supporting UI proposals: badge uses the gold accent for labels like "New" or finish callouts; search uses a pill-shaped, bordered field consistent with e-commerce navigation patterns.

**lock-status-indicator** is a category-specific proposed component representing real-time device state (locked/unlocked/battery), using the slate accent for nominal states and the red (`{colors.danger}`) for alerts — no live app/device UI was observed, so this is a design proposal only.

## Responsive Behavior

This is a recommendation, not measured site behavior; no responsive breakpoints or mobile layouts were directly observed in the supplied evidence.

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | < 640px | Single-column stacking; nav collapses to hamburger/drawer |
| Tablet | 640–1024px | Two-column product grids; nav-bar retains horizontal links |
| Desktop | > 1024px | Full multi-column layout; hover-revealed submenus |

Touch targets should be at minimum 44x44px for buttons and nav links. Navigation submenus (implied by the `--global-header-submenu-height` calc) likely collapse into an accordion or full-screen overlay on narrower viewports; this pattern is proposed, not confirmed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS extraction only surfaces class/selector names and custom-property declarations; no rendered screenshots or computed layout were available, so spacing, grid structure, and imagery treatment are inferred.
- Semantic color mapping (e.g., `--color-cotton`, `--color-charcoal`, `--color-slate` → specific hex values) is inferred from naming conventions and palette proximity, not confirmed via computed styles.
- Typography sizes, weights, and line-heights beyond the base scale are proposed design values; only the font-family tokens (`suisseIntl`, `suisseWorks`, and monospace fallbacks) are directly observed.
- Interaction states (hover, focus, active, disabled) and all mobile/responsive layouts are proposed conventions, not observed in the supplied CSS.
- Availability and licensing of the SuisseIntl/SuisseWorks font families are not verified; generic fallbacks are specified for safety.
