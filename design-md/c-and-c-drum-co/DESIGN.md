---
version: alpha
name: "C&C Drum Co"
source_url: "https://www.candccustomdrums.com"
captured_at: "2026-09-28T04:42:45.887764+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from a WordPress/Beaver Builder-based content site
  (CCDrums) operating under the C&C Drum Company name as an Amazon affiliate
  publisher covering drum kits, electronic and acoustic drums, components, pads,
  and gear. The only explicit brand-level CSS variable is --primary-color: #008848,
  a mid-tone green, paired with a defined secondary rust (#C05530), a success green
  (#627D47), and an alert red (#B20000) in the theme's design-token block — these
  four are treated as the core brand palette. A distinct blue (#0C4DA2) appears
  only in third-party GDPR/cookie-consent UI and is retained here as a utility
  accent rather than a primary brand color. Neutrals span near-white surfaces
  (#ffffff, #f7f7f7, #ececec) to near-black text (#0a0a0a, #202020, #333333),
  consistent with a content-first, editorial layout. Font stacks reference Manrope
  and Nunito alongside generic sans-serif/serif fallbacks; no proprietary or
  licensed webfont was confirmed, so Manrope is inferred for display/heading use
  and Nunito for body copy based on their presence in the font-family list. Layout
  structure (grid, spacing, breakpoints) is not observable from static CSS and is
  proposed for consistency, not measured.

colors:
  primary: "#008848"
  secondary: "#c05530"
  success: "#627d47"
  alert: "#b20000"
  accent-blue: "#0c4da2"
  ink: "#0a0a0a"
  body: "#333333"
  canvas: "#ffffff"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-dark: "#32373c"
  on-primary: "#ffffff"
  border-strong: "#cccccc"
typography:
  display-xl: {fontFamily: "Manrope, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Manrope, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Manrope, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Nunito, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Manrope, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineBottom: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  drum-spec-list:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-sm}"
    padding: "{spacing.base}"

## Components

**button-primary** uses the theme's declared --primary-color (#008848) as its fill, a green tied directly to the site's CSS custom properties, with white text for contrast; proposed hover/active/disabled states are not observed.

**button-secondary** is an outlined variant reusing the primary green for border and label, intended for lower-emphasis actions like "Read More" links on guide articles; state is proposed, not confirmed in markup.

**text-input** is a proposed form field style (e.g., contact or search) using neutral canvas and hairline border, since no dedicated input CSS was present in the supplied evidence.

**nav-bar** reflects the observed `.header-bottom` (#ffffff background) and `.header-bg-color` (90%-opacity white), suggesting a light, semi-transparent top navigation; sticky/scroll behavior is inferred, not measured.

**product-card** is a category-appropriate proposed pattern for listing drum kits, electronic/acoustic drums, and components, using a white surface and hairline border consistent with the site's light neutral tones; no actual card markup was supplied.

**hero** proposes a light soft-surface (#f7f7f7) banner area for landing/category intros, pairing the largest display type scale with body copy; exact hero markup was not present in evidence.

**footer** is modeled on the dark neutral #32373c seen in the default WordPress button background, repurposed here as a footer surface since the site's real footer color was not directly captured; navigation links (Home, About, Privacy Policy, Contact) are confirmed from page text.

**badge** reuses the success green (#627D47) from the CSS variable block, proposed for labels such as "Best Value" or "Editor's Pick" on drumstick/gear guide content; not an observed component.

**search** is a proposed light-surface search field for the content-heavy blog structure (44+ paginated posts), styled consistently with text-input.

**drum-spec-list** is a category-specific proposed component for presenting drum/drumstick specifications (e.g., diameter, material, weight) in guide articles, using neutral card styling and the caption/body-sm type pairing for label/value rows.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width      | Notes                                  |
|-----------|------------|-----------------------------------------|
| sm        | ≤ 480px    | Single-column, stacked nav, full-width cards |
| md        | 481–768px  | Collapsed hamburger nav, 2-col card grid |
| lg        | 769–1024px | Expanded nav, 2–3 col card grid         |
| xl        | ≥ 1025px   | Full nav bar, 3–4 col card grid, max content width ~1200px |

Touch targets should be at least 44×44px for nav and button elements. Navigation is assumed to collapse into a hamburger/menu pattern below `md`; this is a UX recommendation, not an observed interaction.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted from static CSS/HTML text only; no rendered layout, spacing, grid, or breakpoint values were directly observed.
- The site functions as an Amazon-affiliate content publisher rather than a transactional drum storefront; product-card, search, and drum-spec-list components are therefore proposed patterns, not confirmed UI.
- Many supplied hex values (e.g., #ff6900, #fcb900, #8ed1fc, #7bdcb5, #cf2aba) match default WordPress block-editor palettes rather than brand-specific choices and were excluded from the core token set.
- Manrope and Nunito are inferred as the primary display/body fonts based on their presence in the font-family list; actual font-weight availability, self-hosting, and licensing were not verified.
- The blue accent (#0C4DA2) originates from third-party GDPR consent-banner styling, not confirmed brand usage, and is retained only as a utility/accent color.
- All component states (hover, focus, active, disabled) and responsive collapse behavior are proposed for design consistency and have not been observed in a live rendered session.
