---
version: alpha
name: "Sakura Bloom"
source_url: "https://sakurabloom.com"
captured_at: "2026-09-28T09:40:04.588314+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Sakura Bloom's storefront CSS defines a restrained two-typeface system: Tenor Sans, a serif-adjacent display face, for headers at a fixed 28px/400-weight, and Outfit, a light-weight sans, for body copy at 15px/300-weight with slight letter-spacing (0.025em). No brand accent color is declared as a CSS custom property; the only functional color decisions observed are two muted blue-grey button backgrounds (#7396a2, #5487a0) used on a passcode gate and a third-party "smt-button" utility, plus a warm orange (#c86800) and status reds/greens that appear to be system or app-injected rather than brand-authored. Given the product context (natural-fiber, handcrafted baby carriers made in California) and the observed blue-grey buttons, this interpretation treats #7396a2 as the working primary accent, reserving #5487a0 as a secondary/hover variant — both are inferred brand roles, not confirmed CTA colors sitewide. Neutrals (near-black inks, mid greys, off-white surfaces) dominate the palette and are mapped to ink/body/muted/surface roles to support a quiet, editorial, textile-forward aesthetic. Buttons are flat (--buttonRadius: 0), reinforcing a minimal, handcraft-focused visual language. Layout, spacing rhythm, and responsive breakpoints are not present in the supplied evidence and are proposed conventions only.

colors:
  primary: "#7396a2"
  primary-alt: "#5487a0"
  ink: "#202020"
  canvas: "#ffffff"
  body: "#303030"
  muted: "#6a6a6a"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-warm: "#c86800"
  error: "#aa0000"
  success: "#29845a"
  border-subtle: "#e0e0e0"
typography:
  display-xl: {fontFamily: "'Tenor Sans', sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: 0em}
  display-md: {fontFamily: "'Tenor Sans', sans-serif", fontSize: 28px, fontWeight: 400, lineHeight: 1, letterSpacing: 0em}
  title-md: {fontFamily: "'Tenor Sans', sans-serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0em}
  body-md: {fontFamily: "Outfit, sans-serif", fontSize: 15px, fontWeight: 300, lineHeight: 1.4, letterSpacing: 0.025em}
  body-sm: {fontFamily: "Outfit, sans-serif", fontSize: 13px, fontWeight: 300, lineHeight: 1.4, letterSpacing: 0.025em}
  caption: {fontFamily: "Outfit, sans-serif", fontSize: 12px, fontWeight: 300, lineHeight: 1.3, letterSpacing: 0.03em}
  button-md: {fontFamily: "Outfit, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1, letterSpacing: 0.05em}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    priceColor: "{colors.muted}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    iconColor: "{colors.muted}"
    padding: "{spacing.sm} {spacing.md}"
  fabric-swatch-selector:
    backgroundColor: "{colors.canvas}"
    defaultTextColor: "{colors.muted}"
    selectedTextColor: "{colors.ink}"
    priceColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.ink}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** carries the site's primary call-to-action (e.g. "Shop Scouts," checkout). Its flat corner treatment (`rounded.none`) is directly observed via the `--buttonRadius: 0` custom property; the blue-grey fill is an inferred brand-accent mapping from the two observed button backgrounds.

**button-secondary** is a proposed outline variant for lower-emphasis actions ("View all," "Log in") using the same accent as text/border on a white field. No secondary-button CSS was present in evidence; this is a conventional pairing.

**text-input** covers search and cart note fields. Border, radius, and padding are proposed defaults consistent with the site's minimal, flat aesthetic; no input-specific CSS was supplied.

**nav-bar** represents the top navigation ("SHOP / LEARN / ABOUT" structure implied by the menu text). White background and hairline underline are inferred from the neutral, high-key palette; exact nav styling was not present in the CSS evidence.

**product-card** models listing tiles such as "Venice Scout, starting at $480.00." Title uses the Tenor Sans title-md style; price uses muted grey body-sm, mirroring the observed swatch price color (#7A7A7A → mapped to `colors.muted`).

**hero** models the homepage slideshow ("Fall has arrived, shop now"). Headline typography uses the proposed larger display-xl size; the observed 28px header token is reserved for `display-md` (section headings), since no hero-specific font size was in evidence.

**footer** models the Help Center / Community / Currency block. Muted text on a soft neutral background is proposed, matching the dense, utilitarian footer content described in the page text.

**badge** is a proposed small-label component (e.g. sale/new tags) using the observed warm orange (#c86800), which appears in the palette but not confirmed in the sampled CSS rules as a badge; role is inferred.

**search** models the header search affordance ("icon-search Search"), styled as a bordered flat field consistent with the button radius convention.

**fabric-swatch-selector** is a category-specific component modeling the textile/color swatch picker referenced by the `variant-swatch-king` CSS (used to choose carrier fabric or leather option). Selected vs. default text colors (#292929 vs. #6A6A6A) and the fixed 13px size are directly observed; hover and selection borders are proposed extensions of that pattern.

## Responsive Behavior

Recommended (not measured) breakpoint table:

| Breakpoint | Width      | Layout notes (proposed) |
|-----------|-----------|--------------------------|
| mobile    | < 600px   | Single-column product grid, collapsed hamburger nav (`icon-hamburger` observed in menu text) |
| tablet    | 600–1024px| 2-column product grid, nav may remain collapsed |
| desktop   | > 1024px  | 3–4 column product grid, full horizontal nav |

Touch targets should be at least 44×44px for cart, search, and swatch-selector controls. The hamburger menu and slide-out cart (`icon-X Close cart` / `icon-X Close menu` in page text) suggest an off-canvas mobile pattern, but exact collapse behavior, animation, and breakpoint values were not observed and are recommendations only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no rendered layout, grid structure, or actual breakpoints were observed.
- The mapping of `#7396a2`/`#5487a0` to a primary brand accent is inferred from two isolated button rules (a passcode gate and a third-party app button), not confirmed as the sitewide CTA color.
- Several palette colors (e.g. `#005bd3`, `#2332d5`, `#8051ff`, `#ea5455`, `#7367f0`) appear tied to third-party app widgets (checkout, reviews) rather than brand design and were excluded from role mapping.
- Font availability, licensing, and self-hosting status for Tenor Sans and Outfit were not verified.
- Component states (hover, focus, disabled, error) beyond the swatch-selector are proposed, not observed.
- Spacing and rounded-corner scales beyond the confirmed `buttonRadius: 0` and `smt-button` 5px radius are proposed conventions, not measured site values.
- Mobile menu/cart interaction sequencing is inferred from menu label text only, not from observed DOM/JS behavior.
