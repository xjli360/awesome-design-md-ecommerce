---
version: alpha
name: "Top Knobs"
source_url: "https://topknobs.com"
captured_at: "2026-09-28T10:14:44.177925+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Top Knobs presents itself as a premium decorative hardware manufacturer, and the
  extracted evidence reflects a Magento-based storefront built on a large neutral
  grayscale system (from "#ffffff" through "#231f20") with a small set of deeper
  red accent values ("#ab232b", "#b6272d", "#e02b27", "#8b0000") that most plausibly
  carry brand/CTA weight, alongside a Magento-default link blue ("#1979c3"). These
  role assignments are inferred from typical e-commerce conventions, not confirmed
  by any labeled brand token in the supplied CSS. Observed font families include
  Open Sans, Lato, Mulish, Helvetica Neue and Arial for interface text, plus the
  serif display face "Perpetua Titling MT," which is treated here as the likely
  editorial/display typeface for collection names and hero titling given the
  brand's traditional hardware positioning; this pairing is proposed, not verified
  live. One concrete data point—the flipbook widget button (2px radius, #333
  background, 13px/600-weight label)—anchors the button and radius scale below.
  The interpretation favors a restrained, catalog-driven layout: dense grayscale
  content areas, a single confident accent color for calls to action, and generous
  whitespace suited to product photography of knobs, pulls, and finishes.

colors:
  primary: "#b6272d"
  ink: "#231f20"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6d6e71"
  hairline: "#cecece"
  surface-soft: "#f2f2f2"
  surface-card: "#f9f9f9"
  on-primary: "#ffffff"
  link: "#1979c3"
  accent: "#ff5216"
  success: "#006400"
  border-light: "#e4e4e4"
  disabled: "#adadad"
typography:
  display-xl: {fontFamily: "'Perpetua Titling MT', serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Perpetua Titling MT', serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Lato, Arial, sans-serif", fontSize: 13px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
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
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-light}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    iconColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  finish-swatch:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    size: "{spacing.xl}"
    labelTypography: "{typography.caption}"

## Components
**button-primary** carries the brand red ("#b6272d") as an inferred CTA color, sized with the 13px/600-weight label observed in the flipbook widget button and a 2px radius directly matched from that same CSS rule. **button-secondary** is a proposed outline variant for lower-emphasis actions like "Add to Wishlist," using the hairline gray border rather than a filled background. **text-input** assumes a standard Magento-style bordered field in light gray with dark ink text; no focus or error states were observed, so these remain proposed. **nav-bar** reflects the large mega-menu structure implied by the extensive collections/products list in the page text, styled on a white canvas with small body-sm labels; sticky/scroll behavior is not observed. **product-card** is inferred from the "Popular Products" grid (Kinney Knob, Ascendra Pull, etc.), using a slightly off-white card surface and title-md for product names. **hero** models the large banner sections implied by the repeated `min-height: 600px; padding: 40px` data-pb-style rules, using display-xl for collection titling like "THE PEMBERTON COLLECTION." **footer** is proposed as a dark ink-background block given the long list of informational links (Warranty, FAQ, Catalog, Privacy Policy) but its actual color was not confirmed in evidence. **badge** is a proposed small pill for labels such as "New" using the accent orange-red, unconfirmed live. **search** models the header search field referenced in "Toggle Nav ... Search Search Advanced Search," styled consistently with text-input. **finish-swatch** is a category-specific proposed component for representing metal finishes (e.g., Oil Rubbed Bronze, Stainless Steel) as small round selectable swatches, since finish selection is core to a hardware catalog even though no swatch markup was present in the supplied CSS.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Nav | Grid |
|---|---|---|---|
| mobile | <600px | collapsed hamburger menu | 1-column product grid |
| tablet | 600–1024px | condensed horizontal nav | 2–3 column grid |
| desktop | >1024px | full mega-menu | 4+ column grid |

Touch targets should be at least 44px in the collapsed mobile nav and on finish-swatch elements. The mega-menu (implied by the long collections/products taxonomy) should collapse into an accordion on mobile. No actual responsive CSS or JS behavior was captured in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, computed styles, or interaction states were observed. Color role assignments (primary, accent, link, success) are inferred from convention and hue plausibility, not from labeled brand tokens. Typography sizes beyond the 13px button value are proposed, not measured, including all display and body sizing. The presence of "Perpetua Titling MT" in the font list does not confirm it is used for any specific visible heading—its display role here is inferred from brand tone. Border-radius values beyond the 2px flipbook button are proposed defaults, not confirmed. Hover, focus, active, error, and disabled states were not observed and are labeled proposed throughout. Mobile/responsive layout, breakpoints, and touch behavior were not observed and are recommendations only. Font licensing and web-availability of "Perpetua Titling MT" were not verified and may require a fallback or licensed alternative in production.
