---
version: alpha
name: "Furbo"
source_url: "https://furbo.com"
captured_at: "2026-09-28T04:18:19.982676+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Furbo's stylesheet confirms a single verified typeface, DM Sans, applied to body copy, buttons, and every text-body utility class observed in the extracted CSS (text-body-1 through text-body-5, at confirmed sizes such as 20px/30px and 24px/36px). A second family, Poppins, is declared as a CSS variable (--font-poppins) but its application to specific elements was not present in the supplied rules; it is treated here as an inferred display typeface, consistent with a two-family system pairing a geometric sans for headlines with DM Sans for reading text.

  The palette is dominated by warm neutrals (#faf8f5, #fefaf6, #ececec) and a soft brand yellow (#f7cd3d) that recurs across near-duplicate hex values (#f7cb3b, #ffdd63, #fcebb1), suggesting a marketing accent rather than a strict single-value token. A cooler blue family (#1e7bac and its neighbors) and a coral (#f0836a) appear with enough frequency to imply secondary and highlight roles. Body text consistently resolves to a dark warm grey (#434343), and true black/white are reserved for contrast extremes. Component defaults reset border-radius to 0, so all rounding values below are proposed conventions layered on top, not measured site behavior.

colors:
  primary: "#f7cd3d"
  secondary: "#1e7bac"
  accent: "#f0836a"
  ink: "#434343"
  canvas: "#ffffff"
  body: "#434343"
  muted: "#7d7d7d"
  hairline: "#e0e0e0"
  border: "#ececec"
  surface-soft: "#faf8f5"
  surface-card: "#fefaf6"
  highlight: "#fcebb1"
  overlay: "#00000080"
  on-primary: "#000000"
  on-secondary: "#ffffff"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "DM Sans, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 36px, letterSpacing: 0px}
  body-md: {fontFamily: "DM Sans, sans-serif", fontSize: 20px, fontWeight: 400, lineHeight: 30px, letterSpacing: 0px}
  body-sm: {fontFamily: "DM Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 24px, letterSpacing: 0px}
  caption: {fontFamily: "DM Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 16px, letterSpacing: 0.1px}
  button-md: {fontFamily: "DM Sans, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 24px, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.secondary}"
    border: "1px solid {colors.secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    typography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  device-status-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.border}"
    accentColor: "{colors.secondary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"

## Components

**button-primary** is the yellow-filled call-to-action (e.g. "Shop Now" / "Buy") pairing the brand accent with dark text for contrast; hover/active states are proposed, not observed.

**button-secondary** is an outlined variant using the blue accent for secondary actions like "Learn more," intended to sit beside a primary button without competing for attention.

**text-input** models newsletter/search fields on a soft warm background with a light hairline border, matching the neutral surface tones seen throughout the palette; focus and error states are proposed.

**nav-bar** is a white top bar with dark ink text, assumed sticky given the `scroll-behavior:smooth` rule on body; exact height, logo placement, and mobile menu behavior are not observed.

**product-card** groups a camera/device image, title, and price on the warm off-white card surface (#fefaf6) with a subtle border, matching the site's product-grid intent for pages like /us.

**hero** is a full-width introductory band on the soft surface tone, using the large display type (Poppins, inferred) for headline copy over supporting DM Sans body text; actual hero imagery and copy were not part of the supplied evidence.

**footer** inverts to the dark ink tone for a grounded closing section, following common pattern for e-commerce sites; column structure and link groupings are proposed.

**badge** is a small pill using the warm highlight yellow, suited to labels like "Best Seller" or "#1 pet camera," echoing the title's "#1 Best-selling" claim.

**device-status-card** is a category-specific component for showing camera/device state (online, treat count, alert), using the blue secondary as an accent dot or icon color against the card surface; this pattern is proposed to fit a pet-camera product context and is not drawn from observed markup.

## Responsive Behavior

Recommended (not measured) breakpoints: mobile ≤480px (single-column, stacked nav collapses to a hamburger), tablet 481–1024px (2-column product grids), desktop ≥1025px (multi-column grids, persistent nav). Touch targets should be at least 44px tall, particularly for button-primary and search. Nav and footer link columns are expected to collapse into accordions or stacked lists below tablet width. These figures are UI-design conventions applied to the brand tokens above, not values extracted from Furbo's live responsive CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS declarations and a color/font inventory only; no rendered page, computed layout, or DOM screenshot was inspected. Poppins' actual usage on headings is inferred from the presence of the `--font-poppins` variable, not from a selector applying it. Rounded corner values are entirely proposed, since the only radius evidence observed (`border-radius:0` on form-control resets) indicates a reset baseline rather than a design scale. Spacing values are conventional proposals, not measured pixel gaps. Interaction states (hover, focus, active, disabled) and mobile/tablet layout behavior were not present in the supplied evidence and are marked proposed throughout. Custom font licensing and self-hosting/CDN availability for DM Sans and Poppins were not verified in this extraction.
