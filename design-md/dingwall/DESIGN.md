---
version: alpha
name: "Dingwall"
source_url: "https://www.dingwallguitars.com"
captured_at: "2026-09-28T10:09:59.120044+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Dingwall Guitars' supplied CSS surfaces a stripped-down, workshop-grade
  palette: near-black text (#191919, #333333) on white and light-grey
  surfaces (#f7f7f7, #ececec, #eeeeee), consistent with an instrument-maker
  site rather than a decorative retail theme. A muted gold (#d1a547) is
  present in the observed palette and is adopted here as the primary
  accent; its brand role is inferred from its distinctiveness against an
  otherwise neutral, WordPress/Webflow-default system, not from any
  labeled brand token in the CSS. Headings use eurostile-extended, an
  extended geometric sans typical of guitar/amp branding, set bold
  (font-weight:900) per the observed h1 rule; body copy uses
  century-gothic with an observed 1.6 line-height and 0.1px tracking.
  Arial/Helvetica appears in accordion and FAQ copy, and Lato appears
  once on a form button, so both are treated as supporting utility faces.
  Dark slate (#32373c) recurs as a default WordPress button background
  and is proposed here as a secondary dark surface. Corner radii span
  sharp utility buttons (3px, observed on .faq-button) to fully pill
  WordPress block buttons (9999px); both are retained. Page layout,
  grid structure, and product-imagery treatment are not present in the
  supplied CSS and are proposed only as conventional guidance.

colors:
  primary: "#d1a547"
  ink: "#191919"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#999999"
  hairline: "#dddddd"
  surface-soft: "#f7f7f7"
  surface-card: "#ececec"
  surface-muted: "#eeeeee"
  on-primary: "#ffffff"
  ink-alt: "#32373c"
typography:
  display-xl: {fontFamily: "eurostile-extended, sans-serif", fontSize: 48px, fontWeight: 900, lineHeight: 1.2, letterSpacing: -0.5px}
  display-md: {fontFamily: "eurostile-extended, sans-serif", fontSize: 38px, fontWeight: 900, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "eurostile-extended, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "century-gothic, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.1px}
  body-sm: {fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif", fontSize: 14px, fontWeight: 300, lineHeight: 1.86, letterSpacing: 0px}
  caption: {fontFamily: "Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Lato, sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.3px}
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
    backgroundColor: "{colors.ink-alt}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    border: "none"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineBottom: "{colors.hairline}"
    height: "72px"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    headerBackgroundColor: "{colors.ink-alt}"
    headerTextColor: "{colors.on-primary}"
    bodyTypography: "{typography.body-sm}"
    rowHairline: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** — Proposed gold fill on white, used for primary calls to action (e.g. "Learn more," "Shop"). The gold value is directly observed in the palette; its role as a CTA color is inferred, not confirmed by any labeled button rule.

**button-secondary** — Uses the recurring dark-slate (#32373c) WordPress default button background at a full pill radius, matching the observed `.wp-block-button__link` radius of 9999px. Proposed for secondary/tertiary actions like "Watch full video."

**text-input** — A plain white field with a light hairline border and small radius, inferred from the neutral, utilitarian styling seen across the theme's form and button rules (e.g. warranty-registration form button styling).

**nav-bar** — A white top bar with dark ink text and a light hairline bottom edge, proposed to hold the observed menu items (Artists, Ready to Play, Custom Shop, Dealers, Limited Editions, Contact, Podcast). Height and collapse behavior are not observed.

**hero** — A large, dark, full-bleed section using display-xl type over ink background, proposed to host the "Founded in 1987…" brand statement and instrument photography referenced in the page copy. No hero layout was directly measured.

**product-card** — A light-grey card (#ececec) with a hairline border, housing model name (title-md) and a smaller price/spec line (body-sm); proposed for bass-model listing grids implied by "Ready to Play" and "Limited Editions" navigation items.

**spec-table** — Category-appropriate component for presenting instrument specifications (scale length, pickups, electronics) common to guitar-manufacturer sites; header uses the dark-slate surface with white text, body rows separated by hairlines. Entirely proposed, not observed in the supplied CSS.

**footer** — Dark ink background matching the hero, carrying copyright text ("©2026 Dingwall Guitars") and secondary links (F.A.Q., Privacy Policy, Contact) at body-sm size, per the page-text excerpt.

**badge** — A small gold pill label proposed for tags such as "New," "Limited Edition," or "Custom Shop," reusing the primary accent at caption size.

**search** — A rounded, hairline-bordered field proposed for a site search affordance; no search UI was directly observed in the supplied evidence.

## Responsive Behavior

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | < 480px | Single-column stack, nav collapses to `.w-nav-button` pattern observed in webflow.css |
| Tablet | 480–767px | Two-column product grids, condensed nav |
| Desktop | 768–991px | Full nav bar visible, multi-column layout |
| Large desktop | ≥ 992px | Max-width content container, generous section spacing |

Touch targets are recommended at a minimum of 44×44px for buttons and nav items. The theme includes a `.w-nav-button` class with `display: none` at base and presumably toggled at narrower widths (Webflow convention), but the exact collapse breakpoint was not present in the supplied CSS and should be treated as a recommendation only, not measured site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS/text evidence and carries several limitations: no live rendering, computed layout, or DOM screenshots were available, so grid structure, hero composition, and product-card arrangement are proposed rather than observed. Color-to-role mapping (e.g. gold as "primary") is inferred from palette distinctiveness, not from explicit brand tokens or logo assets. Font stacks (century-gothic, eurostile-extended) are used as observed, but their licensing, hosting method, and cross-browser availability were not verified. Several typography sizes (display-xl, title-md, caption, button line-height) are proposed extrapolations from the one directly observed h1 rule (38px/900/1.2) and the one observed body rule (16px/1.6/0.1px); they are not independently measured. Interaction states (hover, focus, active, disabled) beyond the single observed `:hover/:focus` rule on a Gravity Forms submit button are proposed conventions. Mobile/responsive behavior, breakpoint values, and nav-collapse triggers were not present in the supplied CSS and are marked as recommendations only.
