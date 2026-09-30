---
version: alpha
name: "Sandqvist"
source_url: "https://sandqvist.com"
captured_at: "2026-09-29T04:01:02.071703+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Sandqvist's storefront CSS shows a restrained, monochrome-led system built on a defined greyscale token scale (--color-scale-0 through --color-scale-90) running from pure white to near-black (#0c0c0e), with body copy set in #212121 and secondary/muted text implied by #959595 and #444444. Hairlines and soft surfaces are drawn from the lighter scale steps (#e3e3e3, #f8f8f8). Two additional colors, a pale mint (#f3fef2) and a light green (#bdefba), appear outside the greyscale token set; their exact usage was not confirmed in the supplied CSS, so they are treated here as inferred accent colors, most plausibly for sustainability/eco badges or availability indicators given Sandqvist's stated sustainability focus. Typography uses a single observed family, dinPro (with a "dinPro Fallback" web-safe substitute), at a 16px/24px body baseline; all other sizes are proposed extrapolations for a product-and-editorial catalog layout, not measured. Buttons follow an outline/underline pattern with dark/light theme variants tied to a transparent, transitioning header (solid on scroll). This interpretation extends those primitives into a full component set for a backpacks/daily-carry storefront while keeping every color and font strictly within the observed evidence.

colors:
  primary: "#0c0c0e"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#212121"
  muted: "#959595"
  hairline: "#e3e3e3"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border-strong: "#444444"
  border-subtle: "#c2c2c2"
  accent-mint-soft: "#f3fef2"
  accent-mint: "#bdefba"
typography:
  display-xl: {fontFamily: "dinPro, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "dinPro, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "dinPro, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "dinPro, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "dinPro, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "dinPro, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "dinPro, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-subtle}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "transparent"
    backgroundColorScrolled: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    textColorScrolled: "{colors.primary}"
    height: "50px"
    padding: "{spacing.md} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.md}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    ctaComponent: "button-secondary"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    linkTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.base}"
  badge:
    backgroundColor: "{colors.accent-mint-soft}"
    textColor: "{colors.primary}"
    borderColor: "{colors.accent-mint}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border-subtle}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  spec-panel:
    backgroundColor: "{colors.canvas}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base}"

## Components
**button-primary** is the solid, near-black call-to-action used for primary conversion actions like "Add to Bag"; it is proposed from the observed `--color-primary` token and the CSS outline-button padding pattern, though no add-to-cart markup was present in the evidence.

**button-secondary** mirrors the observed `.Button-module...outline` selector, using a transparent fill with a border matching the text color and a hover-state inversion (dark↔light) confirmed by the `:hover` rules in the CSS, making it suitable for secondary actions such as "View Details."

**text-input** is a proposed field style for newsletter signup and checkout forms, referencing the newsletter "Enter your email" prompt in the page text; exact border radius and padding are inferred, not measured.

**nav-bar** reflects the observed `Header-module` behavior directly: an absolutely positioned, transparent header at 50px height that transitions to a solid canvas background and inverts text color on scroll, per the `.solid`, `.light`, and `.dark` modifier classes.

**product-card** is proposed for the grid of backpack listings (e.g., "GRID Rolltop Backpack 14\" $199") seen in the page text; card chrome, spacing, and hover states are inferred since no card-specific selectors were supplied.

**hero** represents the full-bleed "GRID – RESTOCKED" campaign banner referenced in the text excerpt; background and CTA styling are proposed extensions of the dark primary token and secondary button.

**footer** consolidates the observed link list (Product Care, Journal, Our Story, Sustainability, etc.) onto the lightest neutral surface token with a hairline top border; exact footer layout is not confirmed.

**badge** is a proposed sustainability/status tag using the two non-greyscale palette colors (#f3fef2, #bdefba), inferred as an eco or "in stock" indicator given the brand's stated sustainability emphasis; this pairing was not explicitly tied to a role in the supplied CSS.

**search** and **spec-panel** are both proposed: search supports the category/browse navigation implied by "Shop by category," while spec-panel proposes a materials/dimensions display appropriate for a daily/laptop backpack detail page, using muted labels against body-colored values.

## Responsive Behavior
Recommendation only, not measured from live site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <480px | single-column product grid, nav collapses to hamburger + logo |
| tablet | 480–960px | 2-column product grid, header remains absolute/transparent-to-solid |
| desktop | 960–1440px | 3–4 column grid, full inline nav |
| wide | >1440px | max-content width constrained, additional gutter via `{spacing.xxl}` |

Touch targets should meet a minimum 44px height (aligned to the `--spacing-11: 44px` token), buttons and nav items should collapse into a drawer or accordion below tablet width, and the transparent-header-to-solid transition observed in `.Header-module` should be preserved across breakpoints for visual continuity.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS and text extraction only; no rendered layout, real breakpoints, or interaction states (hover, focus, active, loading, error) were observed. The roles assigned to `#f3fef2` and `#bdefba` are inferred guesses based on their non-greyscale nature and the brand's sustainability messaging — their actual usage in the live product is unverified. All typography sizes beyond the confirmed 16px/24px body baseline are proposed, not measured. Component existence (product-card, hero, spec-panel, search) is inferred from page text content, not from corresponding CSS selectors. The `dinPro` font's licensing, weights, and availability as a web font were not verified; generic `sans-serif` is used as a safe fallback. Spacing and rounded-corner scales beyond the `--spacing-*` custom properties are proposed conventions, not extracted values.
