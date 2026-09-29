---
version: alpha
name: "Ring"
source_url: "https://ring.com"
captured_at: "2026-09-28T04:21:18.125792+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from a Ring.com CSS bundle exposing a compact
  button system, a broad status-color palette (orange, blue, red, green,
  yellow), and a RingSans-led type stack falling back to system UI fonts
  (-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif).
  The observed default button is solid near-black (#121212) on white, while
  a distinct orange (#f1670d) governs outlined and ghost button text/borders,
  with darker oranges (#c74e00, #9c4308) for hover/active and a pale orange
  (#fdefe6) for focus surfaces. This suggests a two-tier action system: a
  high-contrast ink button for primary commerce actions, and orange as the
  brand's interactive accent for secondary and tertiary controls. Reds,
  greens, and yellows appear in enough shades to imply status semantics
  (alert/armed, safe/disarmed, warning) fitting a security product, though no
  component markup confirms this usage — it is inferred and used here for a
  security-status badge. Neutral grays (#6e6e6e, #bdbdbd, #dee5ec, #f6f8fa,
  #fafbfc) round out disabled states, hairlines, and soft surfaces. Sizing,
  spacing, and radii below are proposed, not measured.

colors:
  primary: "#f1670d"
  primary-hover: "#c74e00"
  primary-active: "#9c4308"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#424242"
  muted: "#6e6e6e"
  hairline: "#dee5ec"
  surface-soft: "#f6f8fa"
  surface-card: "#fafbfc"
  on-primary: "#ffffff"
  disabled-bg: "#6e6e6e"
  disabled-text: "#bdbdbd"
  disabled-border: "#facaab"
  focus-surface: "#fdefe6"
  danger: "#d4231a"
  danger-soft: "#fcefef"
  success: "#178019"
  success-soft: "#f0f8f0"
  warning: "#fdd835"
  info: "#0074c2"
typography:
  display-xl: {fontFamily: "'RingSans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'RingSans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "'RingSans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'RingSans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'RingSans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'RingSans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'RingSans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    disabledBackground: "{colors.disabled-bg}"
    disabledText: "{colors.disabled-text}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    hoverText: "{colors.primary-hover}"
    hoverBorder: "{colors.primary-hover}"
    focusBackground: "{colors.focus-surface}"
    disabledText: "{colors.disabled-border}"
    disabledBorder: "{colors.disabled-border}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    focusBorder: "{colors.primary}"
    focusBackground: "{colors.focus-surface}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    linkColor: "{colors.muted}"
    activeLinkColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: "72px"
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    ctaComponent: "button-secondary"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    primaryCta: "button-primary"
    paddingY: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.disabled-text}"
    typography: "{typography.body-sm}"
    paddingY: "{spacing.xxl}"
  badge:
    backgroundColor: "{colors.success-soft}"
    textColor: "{colors.success}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    iconColor: "{colors.muted}"
    focusBorder: "{colors.info}"
  security-status-badge:
    armedBackground: "{colors.danger-soft}"
    armedText: "{colors.danger}"
    disarmedBackground: "{colors.success-soft}"
    disarmedText: "{colors.success}"
    warningBackground: "{colors.focus-surface}"
    warningText: "{colors.primary-active}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"

## Components

**button-primary** reflects the dominant observed pattern (`.btn:not(.btn--white)`), a solid near-black fill with white text; used here as the highest-emphasis commerce and account action.

**button-secondary** mirrors the observed `.btn--outlined` rules exactly: transparent background, orange text/border, darker-orange hover, and a pale-orange focus background — the clearest evidence-backed interactive pattern in the source CSS.

**text-input** is a proposed pattern: no input markup was supplied, so border, padding, and the reuse of the orange focus-surface color are inferred from the button focus treatment for visual consistency.

**nav-bar** infers link and active-link colors from a header rule using unresolved CSS custom properties (`--color-neutral-300/500`); mapped here to muted/ink as a reasonable but unverified approximation.

**product-card** is a proposed layout for device/product listings, combining the soft card surface and hairline border observed elsewhere with a secondary-button CTA.

**hero** proposes a soft-surface banner using the largest display type scale; no hero markup or imagery treatment was present in the supplied evidence.

**footer** proposes an ink-toned band for site-wide navigation and legal links; footer color is not confirmed by the supplied rules and is labeled inferred.

**badge** and **security-status-badge** repurpose the palette's red/green/orange hues into small status pills. Given Ring's security-monitoring context, a dedicated armed/disarmed/warning indicator is proposed as the category-appropriate component, though no live status-indicator markup was observed.

## Responsive Behavior

Recommended, not measured:

| Breakpoint | Width      | Behavior (proposed) |
|-----------|------------|----------------------|
| Mobile    | < 600px    | Single-column stack; nav collapses to a menu icon |
| Tablet    | 600–1024px | 2-column product grids; hero text left-aligned |
| Desktop   | > 1024px   | Full nav row; 3–4 column product grids |

Touch targets should be at least 44px in height for buttons and search inputs. Navigation collapse and off-canvas menu behavior are proposed conventions, not observed in the supplied CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Extraction is static; no rendered DOM, computed layout, or interaction states (hover/focus/active) beyond the button rules quoted above were verifiable.
- Font sizes, line-heights, letter-spacing, and the entire spacing/radius scale are proposed placeholders, not measured from the source.
- Nav-bar colors rely on unresolved CSS custom properties (`--color-neutral-300`, `--color-neutral-500`) and are approximated, not confirmed.
- The security-status-badge, hero, and footer components are inferred design proposals fitted to the security-product category; no corresponding markup was in the evidence.
- RingSans availability, licensing, and exact weights are unverified; system-font fallbacks are assumed to render in most contexts.
- Mobile/responsive behavior, breakpoints, and collapse patterns were not observed and are stated as recommendations only.
