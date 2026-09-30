---
version: alpha
name: "Joie"
source_url: "https://joiebaby.com"
captured_at: "2026-09-29T04:21:28.886281+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from CSS and evidence captured on joiebaby.com/us, the parent-site
  presentation of Joie's car seats, strollers, and travel-system catalog. Observed CSS confirms a
  display heading face of Mikado (bold, 40–50px, tight letter-spacing) used for category and video
  titles, alongside a font stack that also references Colfax, Lexend, Hind, and system fallbacks for
  body and UI text; body-copy weight and size are not directly observed and are treated as proposed.
  The supplied palette centers on a family of blues (#3777c4, #295891, #407ec9, #5492dd) that appear
  in button-icon and interactive contexts, paired with warm neutrals (#f7f4f0, #3a3533, #434446) likely
  used for canvas and body text. Accent hues — a red (#ec0927), a warm yellow (#ffcd58), and mint-greens
  (#37cd8f, #058a5e) — are present in the palette and are inferred here as promotional, alert, and
  success-state accents respectively, since no selector evidence ties them to specific roles. Rounded
  corners, spacing scale, and component states below are proposed conventions appropriate to a baby-gear
  retail site and are not claimed as measured from the live layout.

colors:
  primary: "#3777c4"
  primary-dark: "#295891"
  primary-light: "#407ec9"
  ink: "#3a3533"
  canvas: "#ffffff"
  body: "#434446"
  muted: "#737578"
  hairline: "#ebebeb"
  surface-soft: "#f7f4f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#ec0927"
  accent-yellow: "#ffcd58"
  accent-mint: "#37cd8f"
  accent-mint-dark: "#058a5e"
  border-strong: "#cccccc"
typography:
  display-xl: {fontFamily: "Mikado, sans-serif", fontSize: 50px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
  display-md: {fontFamily: "Mikado, sans-serif", fontSize: 40px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
  title-md: {fontFamily: "Mikado, sans-serif", fontSize: 28px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Colfax, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Colfax, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Colfax, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Colfax, Arial, sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.3px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  car-seat-safety-callout:
    backgroundColor: "{colors.canvas}"
    accentColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"

## Components
**button-primary** is proposed as the main call-to-action treatment (e.g. "Discover More," "Submit") using the observed primary blue with white text; hover/active states are not observed and would need confirmation.

**button-secondary** mirrors the outlined style implied by the `.joie-button-secondary` class in the evidence, using blue text/border on a transparent background; the icon color `#3771b7` observed in that selector supports the blue-on-transparent pattern.

**text-input** is a proposed field style (e.g. newsletter email capture) using neutral hairline borders and canvas background, since no input-specific CSS was supplied.

**nav-bar** is inferred from the site's stated navigation labels (Car Seats, Travel Systems, Strollers, Home & Gear, Accessories); visual styling (sticky behavior, active-state underline) is not observed and is proposed.

**product-card** is a category-appropriate proposed pattern for listing car seats/strollers, using surface-card background and hairline borders; no card markup was present in the supplied CSS.

**hero** reflects the "small to fold, ready to fly" promotional module referenced in the page text, using the large Mikado display type observed in `.home__video-title h1` / `.home__category-title h1` rules.

**footer** is proposed dark-ink footer treatment for the observed link groups (Legal, Support, Follow Us, Newsletter); actual footer background/text colors were not directly evidenced.

**badge** is a proposed small label component (e.g. "New," "Best Seller") using the warm yellow accent from the palette; no badge selector was present in evidence.

**search** is a proposed input pattern for site search, styled consistently with text-input using soft surface and hairline border.

**car-seat-safety-callout** is a category-specific proposed component for highlighting safety/certification messaging (e.g. FMVSS standards, 1-year warranty) referenced in the page text, using the mint accent to suggest trust/assurance without claiming it was observed in that role.

## Responsive Behavior
This is a recommended breakpoint structure, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <600px | Single-column stacking; nav collapses to a toggle (evidence references "Toggle Nav"). |
| tablet | 600–1024px | 2-column product grids; hero title steps down toward the 40px Mikado size observed in secondary rule. |
| desktop | ≥1024px | Multi-column grids; hero title uses the 50px Mikado size observed in the primary rule. |

Touch targets should be at least 44px in height for nav and buttons; the mobile nav toggle should expand/collapse a full-height overlay menu (proposed, not observed).

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is static CSS/text extraction; no rendered layout, computed styles, or interaction states (hover, focus, active, disabled) were observed.
- Semantic color roles (canvas, surface-soft, ink vs. body) are inferred from likely usage patterns, not confirmed by selector-to-role mapping in the supplied CSS.
- Font weights/sizes for body-md, body-sm, caption, and button-md are proposed conventions; only the Mikado heading rules (40–50px, 700 weight) were directly observed.
- Custom font availability and licensing (Mikado, Colfax) were not verified; fallback sans-serif stacks are assumed safe defaults.
- Mobile navigation, cart, and checkout flows were not present in the supplied evidence and are not described here.
- Accent color roles (red, yellow, mint) are inferred for promotional/alert/success use based on typical retail conventions, not confirmed by site markup.
