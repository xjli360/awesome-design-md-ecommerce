---
version: alpha
name: "Espacio Handmade"
source_url: "https://espaciohandmade.com"
captured_at: "2026-09-29T03:56:47.900039+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Espacio Handmade is a Shopify-powered storefront for a woman-owned Austin,
  Texas leather and wood goods studio. The observed palette centers on a
  neutral, workshop-like foundation — white and near-white canvases, soft
  grays for cards and dividers, and near-black ink for text — punctuated by
  a single teal accent (#108474) used in the review-widget CSS variables
  (--jdgm-primary-color, star color, write-review button). That teal is the
  only color with clear observed functional evidence, so it is treated here
  as the primary brand accent; all other palette entries (leather brown,
  forest green, mustard gold) appear only in the broader extracted swatch
  list without confirmed component usage and are included as inferred
  secondary/accent options suited to a leather-and-wood product line.
  Font evidence includes Montserrat, Nunito Sans, Questrial, and Baskerville
  alongside system fallbacks; no CSS rule ties a specific family to a
  specific heading or body role, so the typography scale below assigns
  Baskerville to display moments (evoking handcrafted, heritage leatherwork)
  and Nunito Sans/Questrial to body and UI text as an inferred, brand-
  appropriate pairing. Buttons show real evidence of uppercase-capable
  transform variables, 15px/22px padding, 1px borders, and letter-spacing of
  .05em, which directly inform the button component below. Layout, spacing,
  and radius values beyond those in .btn are proposed conventions, not
  measured observations.

colors:
  primary: "#108474"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f2f2f2"
  surface-card: "#fafafa"
  surface-alt: "#eeeeee"
  on-primary: "#ffffff"
  leather: "#954818"
  forest: "#223c22"
  accent-gold: "#f1a802"
  error: "#d02e2e"
typography:
  display-xl: {fontFamily: "Baskerville, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Baskerville, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Questrial, sans-serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Nunito Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.05em}
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
    border: "1px solid {colors.primary}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.ink}"
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
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    overlayColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  personalization-panel:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    accentColor: "{colors.leather}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the one clearly observed interactive pattern: a 1px border matching the fill color, 15px/22px padding, and letter-spacing of .05em on uppercase-capable text, drawn directly from the `.btn` rule. It is mapped to the teal accent as the primary call-to-action color (proposed mapping; hover/disabled states in CSS reference alpha variants not resolvable to hex here).

**button-secondary** mirrors the same padding and typography but swaps to an outlined, ink-on-white treatment for lower-emphasis actions like "View details," consistent with the `.btn--secondary` border/text-swap pattern seen in the CSS, though exact secondary colors are inferred.

**text-input** is a proposed pattern for account, newsletter, and search fields, using a light hairline border and generous horizontal padding to suit a boutique, handcrafted brand feel; no explicit input CSS was supplied.

**nav-bar** is inferred as a clean white bar given the extensive category list in page text (Wallets, Handbags, Keychains, etc.); a bottom hairline separates it from content. Mobile collapse behavior ("Open navigation menu") is referenced in text but its visual treatment is not observed.

**product-card** proposes a soft off-white card background to differentiate product tiles from the white page canvas, with title and price typography scaled for dense grid browsing typical of a multi-category leather goods catalog.

**hero** reflects the homepage's large "handsome handcrafted goods / Austin, Texas" banner language, using the display-xl serif typography against a soft neutral background; slide/carousel behavior ("Previous slide / Next slide") is referenced in the text but its transition and imagery are not verified here.

**footer** groups newsletter signup, shop policies, and social links on a slightly darker neutral surface, consistent with typical Shopify footer conventions; specific column layout is proposed, not measured.

**badge** is proposed for "Under $40," "Free Shipping" progress, and gift-related callouts referenced in the page text, using the gold accent for warmth against the otherwise neutral palette.

**personalization-panel** is a category-appropriate proposed component for the site's live monogramming and "Build Your Own Wallet" configurator flows, using the leather-brown accent to visually tie the customization UI to the physical material being personalized.

## Responsive Behavior

This is a recommended, non-measured breakpoint scheme:

| Breakpoint | Width | Layout guidance |
|---|---|---|
| Mobile | <600px | Single-column product grid; nav collapses to hamburger menu; hero text stacks. |
| Tablet | 600–1024px | Two-column product grid; nav may remain collapsed or show condensed top-level links. |
| Desktop | >1024px | Three to four-column product grid; full horizontal nav with category dropdowns. |

Touch targets for buttons and nav links should maintain a minimum 44px tap height, consistent with the `.btn` padding scale. Menu collapse thresholds and actual mobile stacking were not observed and should be validated against the live responsive implementation.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, real viewport screenshots, or interaction states (hover, focus, active, form validation) were observed. The mapping of Montserrat/Nunito Sans/Questrial/Baskerville to specific display/body/button roles is inferred, since the supplied CSS references font-family only through unresolved custom properties (`--font-stack-body`, `--font-stack-button`). Most palette entries beyond `#108474` lack confirmed component-level usage and are treated as inferred secondary/accent options rather than verified brand colors. All spacing, radius, and breakpoint values not explicitly present in the `.btn` CSS are proposed conventions. Custom/licensed font availability and webfont loading were not verified. Mobile navigation, carousel, and configurator interaction behavior were referenced only in page text, not confirmed visually.
