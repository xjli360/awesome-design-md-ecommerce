---
version: alpha
name: "Freud"
source_url: "https://freudtools.com"
captured_at: "2026-09-29T03:59:49.386942+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Freud's public site evidence shows a utilitarian industrial-tools palette built on
  near-black and white neutrals (#000000, #333333, #282828, #ffffff) with mid-gray
  utility tones (#555555, #767676, #999999, #a3a3a3, #dddddd, #eeeeee, #f8f8f8) used
  for borders, disabled states, and secondary buttons. CSS declarations repeatedly
  reference a literal red keyword for primary call-to-action surfaces (search button,
  featured-product headings, home-feature buttons, modal headers), confirming red as
  the brand's dominant accent role even though its exact hex was not captured in the
  extracted swatch list; it is therefore described in prose only, not assigned a
  token. In its place this interpretation proposes the observed slate-blue
  #4f5d75 as a secondary structural accent and treats the near-black neutrals as the
  primary interactive color for buttons/text, an inferred substitution pending
  confirmation of the true red hex. Typography draws on the observed family list —
  a custom "nexa" face for display headlines, Montserrat for headings/buttons, and
  Nunito for body copy, all falling back to sans-serif per the site's base
  body,html rule. Uppercase, tight-tracking button labels and boxed heading banners
  (per .featured-copy .heading) suggest a squared-off, low-radius component language
  suited to an industrial tool catalog, applied here as inferred defaults rather than
  measured values.

colors:
  primary: "#4f5d75"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#767676"
  hairline: "#dddddd"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  surface-dark: "#282828"
  accent-info: "#2196f3"
  neutral-mid: "#a3a3a3"
  neutral-btn: "#555555"
  border-light: "#eeeeee"
typography:
  display-xl: {fontFamily: "nexa, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 1px}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    overlay: "rgba(80,80,80,.8)"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.neutral-btn}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.neutral-btn}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    accentButton: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  product-spec-table:
    backgroundColor: "{colors.surface-soft}"
    hairline: "{colors.hairline}"
    headerTextColor: "{colors.ink}"
    valueTextColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** is proposed as the site's dominant call-to-action surface, standing in for the CSS-observed "red" background used across `.x-search-nav-drop .s-button`, `.home-feature-button.button-red`, and modal headers. Since the exact red hex was not enumerated in the extracted swatch list, this token substitutes the observed slate `#4f5d75` and flags the mapping as inferred pending confirmation.

**button-secondary** models the lighter gray/white buttons seen in `.button.inverse` and `.home-feature-button.button-gray`, using hairline borders and neutral text for lower-emphasis actions such as "Learn More" links.

**text-input** is a proposed pattern for search and form fields; no explicit input styling was present in the supplied CSS, so border, radius, and padding are inferred defaults consistent with the site's boxy, low-radius button language.

**nav-bar** represents the top navigation containing PRODUCTS, INFORMATION CENTER, WHERE TO BUY, and SIGN IN links visible in the page text; visual styling (spacing, hover states) is not confirmed by the supplied CSS and is treated as proposed.

**product-card** is a category-appropriate proposed component for listing saw blades, router bits, and drilling/boring products, using the card surface and hairline tokens; no explicit product-grid CSS was supplied, so structure is inferred from typical catalog patterns.

**hero** models the observed `.headline-slider .headline-body`, which uses a semi-transparent dark overlay (`rgba(80,80,80,.8)`) over imagery with white text — mapped here to the surface-dark token as the closest available opaque equivalent.

**footer** reflects the multi-column link structure (PRODUCTS, INFORMATION CENTER, WHY FREUD, WHERE TO BUY, WHERE TO SHARPEN, CAREERS, social icons, newsletter form) visible in page text; exact footer background/color pairing is inferred, using dark-surface and neutral-button tokens for contrast.

**badge** generalizes the small uppercase "learnmore" and heading-banner treatments (`.featured-copy .heading`, `.learnmore`) that use compact padding, uppercase text, and solid fills — useful for labeling promotional callouts like "Quadra-Cut™."

**search** is inferred from the `.x-search-nav-drop .s-button` selector, which confirms a search trigger button exists in the header; the surrounding input field styling is proposed, not observed.

**product-spec-table** is a category-appropriate proposed component (not present in supplied CSS) for displaying tool specifications — tooth count, kerf, arbor size, bit diameter — using hairline-divided rows consistent with the site's neutral, utilitarian palette.

## Responsive Behavior

This is a recommended breakpoint structure, not a measured observation of the live site:

| Breakpoint | Width       | Notes                                      |
|-----------|-------------|---------------------------------------------|
| mobile    | <600px      | Nav collapses to a hamburger/off-canvas menu |
| tablet    | 600–959px   | Two-column product grids, stacked hero copy  |
| desktop   | 960–1279px  | Full nav bar, three/four-column product grids |
| wide      | ≥1280px     | Max-width container, generous section padding |

Touch targets should be a minimum of 44×44px for buttons and nav items. The primary nav is expected to collapse below tablet width given the number of top-level items (PRODUCTS, INFORMATION CENTER, WHY FREUD, WHERE TO BUY, WHERE TO SHARPEN, CAREERS, CONTACT, SIGN IN). None of this collapse behavior was directly observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS extraction provides declarations tied to scoped component hashes (e.g., `data-v-7056c376`) but no confirmation of full page layout, grid structure, or responsive breakpoints actually in use.
- The brand's primary accent color is referenced repeatedly as the literal CSS keyword `red` rather than a hex value; the exact red hex was not present in the supplied swatch list, so `colors.primary` substitutes an inferred neutral (`#4f5d75`) pending verification against the live site.
- Font role assignments (nexa for display, Montserrat for headings/buttons, Nunito for body) are inferred from the font-family list; no selector-to-family mapping was supplied, so actual usage may differ.
- All typography sizes, spacing scale, radius scale, and component states (hover, focus, active, disabled) are proposed defaults, not measured values.
- Licensing and web-delivery availability of "nexa," Montserrat, and Nunito were not verified from the supplied evidence.
- Mobile/touch interaction behavior, nav collapse pattern, and product-grid column counts were not observed and are recommendations only.
