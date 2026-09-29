---
version: alpha
name: "Brilliant"
source_url: "https://brilliant.tech"
captured_at: "2026-09-28T04:52:03.942117+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Brilliant's public storefront pairs a white canvas (#ffffff) with a near-black
  ink (#1a1919) for body copy, matching the `body { background-color:#fff }`
  and dark hamburger/nav-text patterns seen in layout.theme.css. Headlines use
  "Gotham A", "Gotham B", "Open Sans", sans-serif at weight 700 (observed on
  `.index-hero__slide-cover-caption-header` and `.index-brilliant-products__item-title`),
  while running copy and nav sublinks fall back to Open Sans at lighter weights.
  The single clearly observed accent is a warm orange (#dc721a, hover state
  #ec872e) used on pill-shaped CTA links and product-link borders, so it is
  assigned the primary role. A muted slate-blue (#788188) drives inactive tab
  labels and is proposed here as the general muted/secondary-text role. Several
  additional hues in the palette (#00bbff cyan, #5f25bd violet, #56ad6a green,
  #da4452 red) were not tied to specific selectors in the evidence; they are
  carried forward as inferred status/accent colors appropriate to a smart-home
  and security product line (e.g., online/armed indicators) but their actual
  site usage is unverified. Rounded pill buttons (32–40px radius) and soft
  neutral panel backgrounds (#f6f6f6, #f7f7f9) round out an interpretation
  aimed at a clean, tech-forward, trustworthy control-panel aesthetic.

colors:
  primary: "#dc721a"
  primary-hover: "#ec872e"
  ink: "#1a1919"
  canvas: "#ffffff"
  body: "#363e45"
  muted: "#788188"
  hairline: "#eaeaea"
  surface-soft: "#f6f6f6"
  surface-card: "#f7f7f9"
  on-primary: "#ffffff"
  accent: "#00bbff"
  accent-secondary: "#5f25bd"
  success: "#56ad6a"
  alert: "#da4452"
typography:
  display-xl: {fontFamily: "'Gotham A','Gotham B','Open Sans',sans-serif", fontSize: 42px, fontWeight: 700, lineHeight: 1.24, letterSpacing: 0px}
  display-md: {fontFamily: "'Gotham A','Gotham B','Open Sans',sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "'Gotham A','Gotham B','Open Sans',sans-serif", fontSize: 28px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans',sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans',sans-serif", fontSize: 13px, fontWeight: 700, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans',sans-serif", fontSize: 12px, fontWeight: 800, lineHeight: 1.3, letterSpacing: 3px}
  button-md: {fontFamily: "'Open Sans',sans-serif", fontSize: 11px, fontWeight: 800, lineHeight: 1.2, letterSpacing: 3px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "transparent"
    titleTypography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  system-status-indicator:
    onlineColor: "{colors.success}"
    alertColor: "{colors.alert}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"

## Components

**button-primary** models the observed hover state of `.index-brilliant-products__item-link:hover`, where an outlined pill flips to a solid `#dc721a` fill with white text. The default (non-hover) outlined state is represented by **button-secondary**, matching the 1px border + `color: var(--color-primary)` pattern before hover. Both use a full pill radius consistent with the 32px/40px radii seen on product links and tab buttons.

**text-input** is a proposed pattern for account, search, or "find a distributor" forms; no explicit input styling was present in the evidence, so its border, radius, and padding are inferred defaults consistent with the site's light, low-contrast surfaces.

**nav-bar** reflects `.theme-header-navigation`'s white background and drop shadow, with sublink typography derived from `.header-navigation-sublink` (Gotham A/Open Sans, 16px, weight 300 — approximated here at body-sm weight for token consistency).

**product-card** is inferred for the Home Controls / Smart Lighting / Plugs grid described in the nav text; it borrows the neutral `surface-soft` background and the 28px bold title style from `.index-brilliant-products__item-title`.

**hero** generalizes the full-bleed slide pattern implied by `.index-hero__slide-cover-caption-header`; the dark background is inferred (the header text is white-on-dark per `color:#fff`), though the exact hero background color was not directly captured in the evidence.

**footer** is a proposed structural pattern; no footer-specific selectors were supplied, so its dark ink background and muted link color are inferred from the site's overall dark/light contrast pairing.

**badge** and **system-status-indicator** are category-appropriate proposals for a smart-home/security brand — e.g., "NEW" flags on Brilliant Max, or armed/online device states — using the unclaimed accent, success, and alert colors from the palette since no badge selector was present in the evidence.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width      | Notes |
|---|---|---|
| mobile | 0–599px | Single-column stacks; hero headline drops to `display-md` (32px, matching `.index-hero__caption-mobile-slide-header`). |
| tablet | 600–1023px | Two-column product grids; nav collapses to hamburger (pattern implied by `.hamburger-button__target-bun`). |
| desktop | 1024px+ | Full nav bar with sublinks visible; multi-column hero/product layout. |

Touch targets should be a minimum 40px height (matching the observed `.smart-apartment__tab-button` height of 40px); the hamburger/nav collapse point is proposed at 1024px since no explicit media query values were included in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, real interaction states (hover/focus/active beyond the two documented), or JavaScript-driven behavior (tabs, cart drawer, quiz) were observed directly. CSS custom properties such as `--color-primary`, `--color-body-text-primary`, and `--color-background-primary` were referenced but not resolved to literal values in the evidence, so mappings to `primary`, `body`, and `ink` are best-effort inferences from adjacent hover/text rules. Several palette colors (cyan, violet, green, red) had no associated selectors and are speculative role assignments suited to a security/smart-home context. Font availability, licensing, and whether "Gotham A"/"Gotham B" are self-hosted or third-party licensed webfonts were not verified — generic sans-serif fallbacks are assumed available. All numeric spacing, radius, and unlabeled typography sizes beyond the directly observed 42px/32px/28px/16px/12px/11px values are proposed defaults, not measured site values. Mobile/responsive collapse behavior is a recommendation only.
