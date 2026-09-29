---
version: alpha
name: "Akrapovic"
source_url: "https://akrapovic.com"
captured_at: "2026-09-28T09:42:07.906674+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Akrapovič's public site presents itself as a technical, racing-derived performance brand rather than a lifestyle retailer. The observed palette is dominated by near-white canvases (#ffffff, #f9f9f9, #f5f5f5) and a family of dark neutrals (#000000, #1a1b24, #2d2d2d, #333333) used for body copy and structural chrome, consistent with a photography-led, product-focused layout. A racing red (#c60c30) with a deeper secondary red (#9b0a26) appears in the extracted palette and is interpreted here as the primary accent, reflecting the brand's motorsport positioning ("racing is in Akrapovič DNA"); this role is inferred rather than confirmed against a live rendered button. Typography is observed as Open Sans for body text via the site's CSS; Saira is present in the extracted font stack and is proposed here for display/heading use given its common association with automotive and motorsport type systems, though its applied role on this site is unverified. Hairlines and card surfaces are drawn from the light gray set (#e5e7eb, #f9fafb, #e0e0e0). The resulting interpretation favors a dark-on-light, high-contrast editorial grid with a restrained red accent reserved for calls to action and key racing/product highlights, avoiding decorative color use.

colors:
  primary: "#c60c30"
  primary-dark: "#9b0a26"
  ink: "#1a1b24"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#e5e7eb"
  surface-soft: "#f5f5f5"
  surface-card: "#f9fafb"
  on-primary: "#ffffff"
  border-strong: "#9ca3af"
  overlay: "#000000b3"
  ink-soft: "#58595b"
typography:
  display-xl: {fontFamily: "Saira, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Saira, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Saira, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    height: "80px"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
  hero:
    backgroundColor: "{colors.ink}"
    overlay: "{colors.overlay}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  vehicle-finder:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    stepTypography: "{typography.body-md}"
    accent: "{colors.primary}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.ink-soft}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

**button-primary** is proposed as the racing-red call-to-action used for "Find the System" and similar conversion prompts; the red/white pairing is drawn directly from the observed palette but its exact application on live buttons was not confirmed in the extracted CSS.

**button-secondary** covers outline-style actions (e.g. "More" links) against light backgrounds, using a neutral border rather than color to keep emphasis on the primary red action — a proposed pattern, not an observed style rule.

**text-input** supports search and contact forms with a light canvas, thin hairline border, and body typography; states such as focus or error are not observed and are proposed defaults.

**nav-bar** reflects the one confirmed layout fact in the evidence — a white, 80px-tall header (`.header{background-color:#fff;height:80px}`) — extended here with inferred text color and spacing for logo, mega-menu triggers (Motorcycles/Cars/Racing), and search icon.

**hero** models the homepage's large video/image banner with overlay text ("World Championship-Winning Exhaust System Technology"); the dark overlay and large display type are proposed to ensure legibility over photographic or racing footage backgrounds.

**product-card** is a proposed pattern for exhaust-system listings (per motorcycle/car model), using a soft card surface, hairline border, and title/body type pairing; no live card markup was present in the supplied evidence.

**vehicle-finder** is a category-appropriate component reflecting the site's "Select Motorcycle Brand" / "Find Your Exhaust" flow described in the page text, styled as a light panel guiding users through brand → model → part selection.

**search** models the global search overlay ("Search / Close / Popular search terms") referenced in the text content, using a simple bordered field consistent with the neutral, technical tone of the rest of the interface.

**badge** is proposed for labeling OEM/partner or "Racing" tags on product and story cards, using the primary red in a pill shape for short, scannable labels.

**footer** consolidates the extensive link taxonomy seen in the page text (Our story, Careers, For Partners, Legal Notice, etc.) into a dark, high-density footer, contrasting with the light body to visually close out long content pages.

## Responsive Behavior

Recommended, not measured, breakpoint table:

| Range | Target | Notes |
|---|---|---|
| ≤480px | Mobile | Single-column, nav collapses to a hamburger/menu drawer; vehicle-finder steps stack vertically |
| 481–768px | Large mobile / small tablet | Two-column product grids; search expands to full-width overlay |
| 769–1024px | Tablet | Nav-bar shows primary categories inline; hero text scales to display-md |
| ≥1025px | Desktop | Full mega-menu navigation; hero uses display-xl; multi-column footer |

Touch targets should be at least 44×44px for menu triggers and buttons. Mega-menus and the vehicle-finder are recommended to collapse into accordion patterns below tablet width. This behavior is a design recommendation only; no responsive CSS or mobile rendering was captured in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, computed styles, or interaction states (hover, focus, active, error) were observed. Color-to-role mapping (e.g., primary red, ink, surface tiers) is inferred from palette frequency and brand context, not from confirmed component usage. Font sizes, weights, spacing scale, and rounded-corner values are proposed defaults calibrated to the observed Open Sans/Saira stack, not measured from live typographic output. The presence of "Saira" in the extracted font list does not confirm it is actively applied to headings on the current site. Mobile navigation, menu collapse behavior, and the vehicle-finder/search overlay interactions described in the page text were not visually observed. Licensing and hosting of any custom or web fonts referenced were not verified.
