---
version: alpha
name: "TeraFlex"
source_url: "https://teraflex.com"
captured_at: "2026-09-28T09:26:10.363430+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from static CSS and markup evidence for teraflex.com, an off-road/4x4 parts retailer for Jeep, Bronco, and truck platforms. The observed palette centers on a strong red (#da2128, also seen as #ed1c24/#db2027 variants) used for headings, form submit buttons, and active-state icons, set against a black-and-white utility base (#000000 header bars, #ffffff canvas, #1e1e1e body text). Grays (#f7f7f7, #f4f4f4, #cccccc, #616161, #777777) appear repeatedly as panel fills, borders, and secondary nav backgrounds. A blue (#0370c4) appears in the supplied palette and is assigned here, as an inferred role, to informational/link accents since no direct link-color declaration was captured. Typography is confirmed as "Barlow" for body copy and "Barlow Condensed" for headings, with "Anton" layered on h1/h2 for a bold, condensed display treatment consistent with an industrial off-road brand. The proposed system leans into a rugged, high-contrast, red/black/white identity with generous use of uppercase, bold weights, and squared-off (low-radius) buttons, reflecting the trail-hardware tone of the source content. Font sizes beyond the observed 14px base are proposed, not measured.

colors:
  primary: "#da2128"
  ink: "#1e1e1e"
  canvas: "#ffffff"
  body: "#1e1e1e"
  muted: "#777777"
  hairline: "#cccccc"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  surface-dark: "#000000"
  panel-dark: "#616161"
  border-alt: "#dddddd"
  accent-blue: "#0370c4"
typography:
  display-xl: {fontFamily: "Anton, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Anton, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Barlow Condensed', sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Barlow, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Barlow, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Barlow, sans-serif", fontSize: 11px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.25px}
  button-md: {fontFamily: "Barlow, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    activeIndicatorColor: "{colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    hairline: "{colors.panel-dark}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  vehicle-fitment-selector:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    ctaComponent: "button-primary"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"

## Components

**button-primary** — Modeled on the observed red submit buttons (`.webforms .form button.submit`, `.email--popup button`), all using `#da2128` with white text, uppercase, bold, and zero corner radius. Used here as the canonical CTA (e.g., "Shop Now," "Find my parts").

**button-secondary** — Not directly observed; proposed as an outlined red-on-white variant for lower-emphasis actions (e.g., "Learn More" links seen paired with primary CTAs in the content).

**text-input** — Proposed pattern using the light hairline border (`#cccccc`) and white canvas consistent with form field conventions implied by `.webforms .form` classes; exact input styling not captured in evidence.

**nav-bar** — Grounded in `.header--mobile`, which is confirmed black (`#000000`) with white icon color (`.header--mobile .fa { color:#fff }`) and a red active state (`.nav-toggle.active .fa { color:#da2128 }`). Desktop nav structure is inferred from the category link list in page text, not directly observed in layout CSS.

**product-card** — Proposed component for the "Best Sellers" and "Shop By Category" grid content described in page text; card chrome (border, radius, padding) is inferred from generic surface/hairline tokens since no card-specific selector was supplied.

**hero** — Proposed for the "Find the parts that fit your vehicle" banner section; dark background and bold Anton display type are inferred from brand tone and the confirmed dark header treatment, not a captured hero selector.

**footer** — Grounded in the dark `.header--mobile` background and `.mobile--nav__header` panel color (`#616161`), extended here as a footer treatment given the extensive link list (Customer Service, Company Information) in page text; exact footer CSS was not supplied.

**badge** — Proposed small red pill for labels like "New Products" or "What's New," using the confirmed primary red; no badge selector was present in evidence.

**search** — Proposed light-gray search field consistent with `.header--mobile .mobile--menu` background (`#F4F4F4`); exact search-input CSS was not supplied.

**vehicle-fitment-selector** — Category-specific component modeled on the "My Vehicle" / "Find my parts" fitment tool referenced in page text, a hallmark pattern for 4x4/off-road parts sites. Styling is proposed using the surface-soft and hairline tokens; no dedicated selector was captured.

## Responsive Behavior
Recommended, not measured:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <768px | Single-column stack; `.header--mobile` confirms a dedicated mobile header/nav pattern exists |
| tablet | 768–1023px | Two-column product grids; collapsed filters |
| desktop | ≥1024px | Multi-column category grid, persistent top nav |

Touch targets should be ≥44px for nav toggles and CTA buttons. Mobile menu is confirmed to exist as a full-height overlay (`min-height:100vh`) triggered by a toggle icon; exact open/close animation and breakpoint thresholds are not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Color palette is restricted to the supplied observed hex list; any role not directly tied to a captured selector (e.g., accent-blue, surface-dark as footer) is labeled inferred.
- Several palette entries (e.g., `#3b5998`, `#dd4b39`, `#1087dd`, `#cc006a`) appear to be third-party social-icon brand colors and were excluded from the design token set as non-brand.
- Typography sizes beyond the confirmed 14px body base and observed heading families are proposed, not measured; no rendered heading font-size was captured.
- Layout structures (hero, product-card, footer, search) are inferred from page text and category conventions, not from captured layout/grid CSS.
- No hover/focus/active interaction states beyond the two captured button/icon rules were observed; all other states are proposed.
- Mobile menu open/close behavior, breakpoint pixel values, and grid column counts are not confirmed by supplied evidence.
- Font licensing/availability for Anton, Barlow, and Barlow Condensed was not verified; assume generic sans-serif fallback is required for production use.
