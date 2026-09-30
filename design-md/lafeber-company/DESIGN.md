---
version: alpha
name: "Lafeber Company"
source_url: "https://lafeber.com"
captured_at: "2026-09-29T04:10:10.084558+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Lafeber Company's site evidence points to a WordPress/Elementor-driven storefront built on CSS custom-property theming rather than a bespoke design system. Confirmed rules tie brand blue (#0078c2) to button backgrounds, warm brown (#45220e) to block text and heading color, and white (#ffffff) to button labels and card surfaces — these three form the backbone of the interpretation below. The broader supplied palette includes deep red (#aa001b), forest green (#0f834d), and dark navy tones (#171d2d, #151d2d) that plausibly serve accent, success/eco-badge, and footer-dark roles respectively; these mappings are inferred, not confirmed by a direct CSS rule.
  Typography draws on the observed font stack: Fraunces (a serif with editorial, heritage character) is proposed for display and heading roles to echo the brand's "two generations of veterinarians" farm-heritage story, while Lato serves body copy, matching the theme's 16px base font-size token. Button radii of 25–30px observed in CSS suggest a pill-leaning, friendly interaction style, approximated here against a fixed rounded-token scale. Spacing follows WordPress's 24px block-gap convention as the "lg" step. All layout, hover, and responsive behaviors below are proposed patterns for a small-animal/bird/reptile nutrition retailer, not measured observations.

colors:
  primary: "#0078c2"
  ink: "#45220e"
  canvas: "#ffffff"
  body: "#212121"
  muted: "#5a5a59"
  hairline: "#dddddd"
  surface-soft: "#eeeeee"
  surface-card: "#f9f9f9"
  on-primary: "#ffffff"
  accent: "#aa001b"
  success: "#0f834d"
  footer-dark: "#171d2d"
  link-hover: "#45220e"
typography:
  display-xl: {fontFamily: "Fraunces, Georgia, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Fraunces, Georgia, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Fraunces, Georgia, serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Lato, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Lato, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Lato, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Lato, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.footer-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  species-filter-tab:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"

## Components

**button-primary** renders the site's blue call-to-action ("Shop Now", "Sign Up"), directly reflecting the confirmed `--wr-button-background-color:#0078c2` / white-text rule, with a pill-like radius approximating the observed 25–30px corner values.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Learn more about us") sharing the primary blue as text/border color on a transparent field; no such outline button was directly observed, so this is inferred from typical companion-button patterns.

**text-input** covers newsletter and search-adjacent fields; background and border are proposed from the neutral hairline/canvas tones since no distinct input style was captured in the evidence.

**nav-bar** models the top utility/category navigation (Pet Birds, Small Animals, Backyard Chickens, Shop) on a white canvas with brown ink text, consistent with the heading-color rule; exact height, sticky behavior, and hover states are not observed.

**product-card** represents catalog tiles (Nutri-Berries, Avi-Cakes, Pellet-Berries) with a soft off-white card surface and mid rounding; the WordPress block default `--wr-block-background-color:#ffffff` and `border-radius:30px` support the general softened-corner tone, mapped here to the nearest token.

**hero** covers the rotating homepage banner (seasonal product promos, loyalty program, webinars) using a light soft surface and the largest display type for campaign headlines; actual hero copy sizing/cropping is not measured.

**footer** is proposed as a dark navy band (from the palette's #171d2d/#151d2d family) carrying store-locator and social links in white text; the site evidence lists footer content but not its literal background color, so this is inferred.

**badge** supports promotional or trust markers (e.g., "Trusted by 1025 Verified 5-Star Reviewers", Non-GMO/Hand-inspected chips) using the palette's red as an attention accent; badge color choice is inferred, not directly tied to a supplied rule.

**species-filter-tab** is a category-appropriate proposed component for toggling between Pet Birds / Small Animals / Backyard Chickens content sections, using the pill radius and primary-blue active state consistent with the confirmed button styling.

## Responsive Behavior

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | ≤599px | Single-column stacks; nav collapses to a hamburger/off-canvas menu; hero text shrinks toward display-md. |
| Tablet | 600–899px | Two-column product grids; nav-bar may condense category labels. |
| Desktop | 900–1199px | Three to four-column product grids; full nav-bar visible. |
| Wide | ≥1200px | Content constrained near the theme's 1200px wide-size / 800px content-size tokens observed in `:root`. |

Touch targets for buttons and filter tabs should maintain a minimum ~44px hit area given the pill padding; the mobile nav is expected to collapse behind a toggle, though no such interaction was directly observed. This table is a recommendation for implementation, not a measurement of the live site.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is built from static CSS/text extraction only; no rendered layout, hover state, animation, or actual breakpoint behavior was observed. The theme's `--wp--preset--color--beige`, `--wp--preset--color--gray`, `--wp--preset--color--blue`, `--wp--preset--color--brown`, and `--wp--preset--color--white` variables are referenced in rules (body background, link/heading color) but their resolved hex values were not supplied, so mappings to `#0078c2`, `#45220e`, and `#ffffff` are reasonable but not fully confirmed. Font-family variables (`--wp--preset--font-family--body/--heading`) are likewise unresolved; Fraunces and Lato were selected from the observed font list as plausible heading/body pairings, not confirmed assignments. Rounded-token values (2/4/8/16/9999px) do not exactly match the observed 25px/30px radii, so mappings to `full`/`md` are approximations. Component states (focus, disabled, active nav item), mobile menu behavior, and exact grid column counts are proposed rather than observed. Custom font licensing/self-hosting for Fraunces and Lato was not verified from the supplied evidence.
