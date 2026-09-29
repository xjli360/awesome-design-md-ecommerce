---
version: alpha
name: "Coverking"
source_url: "https://coverking.com"
captured_at: "2026-09-29T04:12:55.122898+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Coverking's storefront pairs a near-black header and hero (#00101a, #0a1a24) with a light,
  neutral working canvas (#f4f6f9) and white card surfaces (#ffffff), giving the site an
  automotive, workshop-adjacent tone rather than a soft retail one. A single confident blue
  (#0078c9, deepening to #00558f on hover states per --ck-blue-hover) anchors primary actions
  and emphasis text (e.g. ".hero h1 em"), while a gold accent (#f2a900/#d99700) is reserved for
  secondary CTAs and underline accents on the fitment widget. Red (#e0301e) and green (#1d8a4c)
  exist in the palette as likely status/alert accents; their exact usage is not confirmed by the
  supplied rules and is treated as inferred. Typography is observed as a custom stack —
  Coverking-Bold / Coverking-Medium / Coverking-Light — layered over Barlow as the workhorse
  body font; generic sans-serif fallbacks are added since the custom faces' availability and
  licensing cannot be verified from CSS alone. Structural values (border colors, muted text,
  8px/6px radii) come directly from the site's own CSS variables. Layout rhythm, spacing scale,
  and rounded-corner sizes beyond --r-sm/--r-md are proposed conventions sized to match the
  observed 1320px max-width and 80–112px header heights, not measured page geometry.

colors:
  primary: "#0078c9"
  primary-deep: "#00558f"
  ink: "#0a1a24"
  ink-deep: "#00101a"
  canvas: "#f4f6f9"
  body: "#0a1a24"
  muted: "#5c6675"
  hairline: "#dce1e8"
  border-strong: "#c4ccd6"
  surface-soft: "#eef1f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#f2a900"
  accent-gold-hover: "#d99700"
  on-gold: "#1a1300"
  accent-red: "#e0301e"
  accent-green: "#1d8a4c"
  text-faint: "#8a93a1"
typography:
  display-xl: {fontFamily: "Coverking-Bold, Barlow, sans-serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.0, letterSpacing: -1.5px}
  display-md: {fontFamily: "Coverking-Bold, Barlow, sans-serif", fontSize: 34px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.5px}
  title-md: {fontFamily: "Coverking-Medium, Barlow, sans-serif", fontSize: 21px, fontWeight: 600, lineHeight: 1.15, letterSpacing: 0px}
  body-md: {fontFamily: "Barlow, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Barlow, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Barlow, sans-serif", fontSize: 12px, fontWeight: 900, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "Barlow, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.3px}
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
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    hoverBackgroundColor: "{colors.accent-gold-hover}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    border: "1.5px solid rgba(255,255,255,.55)"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-primary}"
    height: "80px"
    typography: "{typography.body-sm}"
    underlineAccent: "{colors.accent-gold}"
  vehicle-fitment-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    fieldGap: "{spacing.sm}"
    accentUnderline: "{colors.accent-gold}"
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-primary}"
    emphasisColor: "{colors.primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-gold}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.md}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-strong}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"
    iconColor: "{colors.muted}"

## Components

**button-primary** uses the observed `--ck-blue` fill with white text, intended for primary conversion actions like "Browse all products" or "Explore." Hover/active darkening to `--ck-blue-hover` (#00558f) is defined in CSS as a variable but its exact trigger state is proposed.

**button-secondary** maps to the observed `.btn--gold` rule (gold fill, near-black `#1a1300` text) — likely used for secondary or promotional CTAs (e.g. seasonal accessory callouts). The hover swap to `--ck-gold-hover` is asserted by variable name, not confirmed by a captured `:hover` rule.

**button-ghost** reflects `.btn--ghost` (transparent, translucent white border) — plausible for header-level secondary links over the dark nav. Its exact placement on the page is inferred from selector naming.

**text-input** is a proposed pattern for search and fitment form fields, styled from the shared border/surface tokens since no explicit input CSS was supplied.

**nav-bar** reproduces the confirmed `.site-header` (black background, white text) at the two observed header heights (80px default, 112px when `.header-fit` fitment strip is shown). The gold underline on `.header-fit__label` is directly observed.

**vehicle-fitment-selector** is a category-specific component modeling the Year/Make/Model/Submodel picker referenced in page text; card styling, spacing, and gold underline accent are proposed extrapolations from `.header-fit` and `.advisor-tags` rules.

**product-card** represents listing tiles for Seat Covers, Car Covers, Dash Covers, etc., using the confirmed `.company-card__body h3`/`p` typography pairing (21px title, 14px muted body) on a white card — border and radius are proposed.

**hero** reflects the confirmed `.hero-copy-panel h1` clamp sizing and `.hero h1 em` blue emphasis over a dark panel; exact hero padding/section height is a proposed value.

**footer, badge, and search** are proposed components built from shared tokens (surface, hairline, gold accent) to keep secondary UI consistent; none were directly evidenced in the supplied CSS.

## Responsive Behavior

Recommended, not measured, breakpoints:

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <640px | single-column stacking; fitment selector fields stack vertically |
| tablet | 641–1024px | 2-column product grids; nav may collapse to a toggle |
| desktop | 1025–1320px | full nav, multi-column grids, matches observed `--maxw: 1320px` |
| wide | >1320px | content centered at max-width, background canvas extends |

Touch targets should be ≥44px, matching typical accessory-store checkout flows. The header's two observed heights (80px / 112px) suggest the fitment strip toggles visibility responsively; whether it collapses into the mobile nav or a modal is not observed. All breakpoint values above are proposed conventions, not extracted from media queries in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no rendered screenshots, hover states, or JS-driven interactions (e.g. the vehicle fitment dropdown behavior) were observed.
- Custom font family `--font` variable was referenced but not resolved to a literal value; Barlow and the Coverking-* faces are inferred as the intended stack from the separate `font_families` list. Licensing/availability of Coverking-Bold/Medium/Light is not verified.
- `--r-lg` value was truncated in the supplied `:root` block; the `rounded.lg` token (16px) is a proposed default, not the site's actual value.
- Hero and hero-copy-panel `clamp()` sizing was collapsed to a single representative pixel value (56px) for the typography scale; true responsive scaling is not captured.
- Role assignments for muted text, hairline borders, and surface tiers are inferred from CSS variable naming conventions, not from confirmed rendered usage on specific components.
- Red and green palette entries (`--ck-red`, `--ck-green`) have no confirmed component usage in the supplied rules; treat any status/alert use as speculative.
- Mobile navigation collapse pattern, search UI, and footer structure are proposed conventions with no direct supporting selectors in the evidence.
