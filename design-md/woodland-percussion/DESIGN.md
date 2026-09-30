---
version: alpha
name: "Woodland Percussion"
source_url: "https://www.woodlandpercussion.com"
captured_at: "2026-09-28T09:52:02.411925+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Woodland Percussion's public CSS evidence surfaces a neutral, high-contrast
  foundation (near-black ink tones #111111/#272727/#000000 against white
  #ffffff and off-white #f6f6f6 surfaces) typical of an unstyled Squarespace
  base, plus one warm accent, #f0523d, observed on interactive hover states
  (cookie-banner reject button). This document promotes that accent to the
  brand's primary action color, an inferred choice consistent with a
  handcrafted-wood, workshop-adjacent identity, since no other saturated
  brand color appears outside third-party social-share icon swatches (e.g.
  #3b5998, #ea4c89, #4183c4), which are excluded here as platform icon
  colors rather than brand colors.
  Typography includes Cinzel, a serif face suited to a heritage/craft
  display voice, alongside Poppins for body text and Helvetica
  Neue/Helvetica for small UI chrome (both confirmed in cookie-banner and
  tooltip rules). Font-role assignment (Cinzel for display, Poppins for
  body) is inferred from stylistic fit, not confirmed heading usage.
  Borders, cards, and spacing scales are proposed conventions layered onto
  the observed neutral palette to support a product catalog of custom
  snares and drum kits.

colors:
  primary: "#f0523d"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#272727"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  ink-soft: "#3e3e3e"
  border-strong: "#333333"
typography:
  display-xl: {fontFamily: "Cinzel, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Cinzel, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Poppins, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Poppins, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  caption: {fontFamily: "'Helvetica Neue', Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.05em}
  button-md: {fontFamily: "'Helvetica Neue', Helvetica, sans-serif", fontSize: 11px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink-soft}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
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
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    hairline: "{colors.border-strong}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  custom-build-spec:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.body-sm}"
    valueTypography: "{typography.title-md}"

## Components

**button-primary** uses the single confirmed accent, #f0523d, as a call-to-action color for "Shop Now" and "Add to Cart" actions; hover/active states are proposed, not observed.

**button-secondary** offers a low-emphasis neutral alternative (e.g. "View Gallery") using the off-white surface tone with a hairline border, styled to sit quietly beside the primary accent.

**text-input** covers search, contact-form, and checkout fields with a plain white background and hairline border consistent with the unstyled-Squarespace-base evidence; focus-ring styling is proposed, not confirmed.

**nav-bar** reflects the site's flat top-level structure (Home, Store, About Us, Gallery, Custom Snares, Percussion, Black Out, Birch Series, Policies, Contact, Woodland Woodworx); sticky behavior and mobile menu icon treatment are proposed, since only a text-based "Open Menu/Close Menu" toggle was present in evidence.

**product-card** supports catalog listings for snares, kits, and percussion accessories, pairing a title in the inferred serif display style with a lighter body-sm price/description line; stock badges and hover elevation are proposed.

**hero** proposes a dark, ink-toned banner (using the confirmed #111111/#000000 range) carrying the large Cinzel display headline referenced in the page title ("Giving The Forest Its Voice"), evoking the handcrafted-wood narrative; no hero layout was directly observed.

**footer** mirrors the hero's dark neutral tone to bookend the page, holding secondary navigation and social links; the third-party share-icon colors observed (e.g. #3b5998, #ea4c89) are proposed for icon-hover states only, not for footer background or text.

**badge** is proposed for labeling product attributes such as "Stave Shell," "Ply Snare," or "Custom," using the primary accent for visibility against neutral card backgrounds.

**custom-build-spec** is a category-appropriate component addressing the site's emphasis on individually crafted, configurable drums (stave vs. ply construction, wood species, finish); it presents label/value pairs describing build options and is entirely proposed, as no configurator markup was present in the supplied evidence.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width      | Notes                                      |
|-----------|------------|---------------------------------------------|
| mobile    | 0–599px    | Single-column stack, nav collapses to toggle |
| tablet    | 600–959px  | Two-column product grid                    |
| desktop   | 960–1279px | Three-column product grid, full nav visible |
| wide      | 1280px+    | Max-width container, four-column grid      |

Touch targets should be a minimum 44x44px for buttons and nav toggles. The observed "Open Menu/Close Menu" text pairing suggests a collapsible mobile nav pattern, but its visual treatment (drawer, overlay, icon) was not present in the supplied CSS and is therefore proposed only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is derived solely from static CSS variables, a limited rule sample, and page text; no rendered layout, computed styles, or DOM structure were observed. Font-role assignments (Cinzel for display, Poppins for body) are inferred from stylistic fit and Squarespace convention, not confirmed heading markup. Numeric type scale values beyond the 11px/12px sizes found in cookie-banner and tooltip rules are proposed estimates. Component states (hover, focus, active, disabled) are proposed except where explicitly present in evidence (e.g. button-md sizing, reject-button hover color). The third-party social-icon color set in the palette (Facebook blue, Dribbble pink, GitHub blue, etc.) was excluded from brand role assignment as likely share-icon styling rather than brand identity. Mobile/touch interaction patterns, breakpoint pixel values, and grid column counts are not observed and are marked as recommendations. Custom font licensing and self-hosting status for Cinzel and Poppins were not verified.
