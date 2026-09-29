---
version: alpha
name: "Inspired Leather"
source_url: "https://inspiredleatherco.com"
captured_at: "2026-09-28T10:23:53.020801+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Inspired Leather's storefront evidence shows a deliberately high-contrast,
  black-and-white foundation: body and sidebar text render in pure black
  (#000000) on white (#ffffff) backgrounds, footer inverts to black on white
  text, and both observed hero button variants pair a light background
  (#ffffff or #fafafa) with black (#000) label text and a border-radius of 0.
  This flat, sharp-edged button treatment is carried forward literally rather
  than softened. Supporting neutrals (#f2f2f2, #f9f9f9, #e0e0e0, #dedede,
  #262626, #1c1c1c, #232323) supply card surfaces, hairlines, and muted body
  copy. Two teal-blue tones (#1990c6, #136f99) appear in the palette and are
  used here, as an inferred role, for a restrained interactive accent (links,
  focus rings) since no confirmed brand accent hex was present outside
  payment-badge colors, which are excluded from brand use. Typography draws
  on the two observed families: Baskerville (serif) for display/headline
  moments, evoking the handcrafted, heritage character of leather goods, and
  Montserrat (sans-serif) for body copy, UI labels, and buttons, with Arial as
  a plain-text fallback. Layout spacing and radii below are a proposed system
  consistent with the flat, minimal-radius button evidence; they are not
  measured page metrics.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#262626"
  muted: "#33333340"
  hairline: "#e0e0e0"
  surface-soft: "#fafafa"
  surface-card: "#f9f9f9"
  on-primary: "#ffffff"
  ink-soft: "#1c1c1c"
  overlay: "#000000cc"
  accent: "#1990c6"
  accent-deep: "#136f99"
typography:
  display-xl: {fontFamily: "Baskerville, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Baskerville, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Montserrat, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.2px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.overlay}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkAccent: "{colors.accent}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  personalization-panel:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.caption}"
    optionTypography: "{typography.body-sm}"
    accent: "{colors.accent}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** is the solid black call-to-action used for cart, checkout, and "Shop Now" actions, mirroring the observed white-background/black-text button pattern inverted for primary emphasis; hover/focus states are proposed, not observed.

**button-secondary** offers an outlined black-on-white variant for lower-priority actions (e.g., "Continue Browsing"), consistent with the observed `.button--outline` rule using `rgba(var(--color-body-txt),1)` for border and text.

**text-input** is a proposed form field style (search box, newsletter email, account login) using the observed light hairline gray for its border since no explicit input styling was present in evidence.

**nav-bar** represents the top navigation/menu bar implied by the page's listed links (Home, Hats, Bags, Small Leather Goods, etc.); background and text colors are drawn from the root `--color-body-bg`/`--color-body-txt` variables, layout is inferred.

**product-card** covers the repeated "Add to cart" product tiles seen in the featured collection (bag/dopp-kit listings with price and title); card surface and hairline border are proposed for visual separation, not directly observed.

**hero** models the homepage slider ("Custom Leather Hats," "Leather Bags") which used `.button--solid` with light backgrounds over presumably dark or image-backed slides; the dark ink background and overlay here are a proposed treatment for text legibility, not confirmed slide styling.

**footer** reflects the observed `--color-footer-bg: 0,0,0` / `--color-footer-txt: 255,255,255` variables directly, housing policy links, payment icons, and social links as listed in page text.

**badge** is a proposed pill element for tags like "#madeinUSA" or "Sold Out" labels referenced in the product excerpt; exact styling was not present in evidence.

**search** is a proposed input treatment for the "Search" menu item, styled consistently with text-input.

**personalization-panel** is a category-appropriate proposed component for the brand's core "Free personalization" and custom-sizing/custom-color selection flow mentioned in the copy (hats, bags customization); no such UI was present in the supplied CSS, so this is fully proposed.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| Mobile | <600px | Single-column product grid, stacked nav collapsed behind a menu icon, hero text reduces to `display-md` |
| Tablet | 600–999px | 2-column product grid, condensed horizontal padding per theme's scaling variables (`--horizontal-padding` reductions observed in CSS) |
| Desktop | 1000–1439px | 3–4 column product grid, full nav bar visible |
| Wide | ≥1440px | Max-width content container, generous `{spacing.section}` vertical rhythm |

Touch targets should be at least 44px tall; `button-md`'s observed 55px height comfortably satisfies this. Navigation and filter panels are assumed to collapse into a drawer/menu below tablet width; this collapse behavior was not observed and is a standard e-commerce convention.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted statically from CSS/text; no rendered layout, hover states, animations, or actual mobile breakpoint behavior were observed.
- The `--color-body-accent`/`--color-sidebar-accent` RGB(239,16,16) implies a red accent in theme variables, but since no corresponding hex appeared in the supplied color list, it was excluded per sourcing rules; `#1990c6`/`#136f99` are used instead as an inferred accent, with uncertain actual on-site usage.
- Several palette entries (e.g., #0071ce, #eb001b, #f79e1b, #ff5f00, #142fbd, #1532cb) are consistent with third-party payment-method badges (Visa/Mastercard/PayPal) and were deliberately excluded from brand role assignment.
- Bootstrap-style alert colors (#721c24/#f8d7da, #155724/#d4edda, #856404/#fff3cd) appear in the palette but their actual usage context (form validation states) is unconfirmed and not mapped to components here.
- Font-family declarations reference CSS custom properties (`var(--font-stack-body)`) whose resolved values were not directly shown; Baskerville, Montserrat, and Arial are used based on the separately supplied `font_families` evidence, but exact weight/style pairings per family are inferred.
- All spacing and rounded-corner scales beyond the observed `border-radius:0` on buttons are proposed conventions, not extracted measurements.
- Font licensing/availability (e.g., whether Baskerville is web-licensed or a system font substitution) was not verified.
