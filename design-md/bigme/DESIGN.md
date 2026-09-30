---
version: alpha
name: "Bigme"
source_url: "https://bigmestore.com"
captured_at: "2026-09-28T09:24:26.861559+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Bigme's storefront runs on Shopify's Dawn-derived theme, and the evidence
  exposes a strict two-value neutral system rather than a colorful brand
  palette: canvas white (255,255,255) paired with a near-black foreground
  (18,18,18, rendered here as #121212). Buttons, links, and badges all
  reference these same two CSS custom properties, so the interpretation
  below treats #121212 as the primary/ink color and pure white as canvas
  and on-primary text. A muted charcoal (#232323) and light dividers
  (#dedede, #0000000d) are inferred from skeleton-loader and hairline
  usage to give secondary text and card borders somewhere to sit. A
  cyan-blue pair (#1990c6 / #136f99) appears only inside Shopify's
  accelerated-checkout button styles; it is carried forward here as an
  optional accent/interactive color for wallet or secondary CTAs, since
  no other brand accent was observed. Hex values such as #eb001b,
  #f79e1b, #ff5f00, and #0071ce are third-party card-network marks and
  are explicitly excluded from semantic roles. Typography uses the only
  observed family, "Assistant," for both body and heading, with heading
  weight/style driven by theme variables rather than literal values.
  Radii and spacing are proposed conventions, not measured.

colors:
  primary: "#121212"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#232323"
  muted: "#1c1c1c"
  hairline: "#dedede"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#1990c6"
  accent-hover: "#136f99"
  divider-subtle: "#0000000d"
  overlay-scrim: "#00000080"
  surface-dark: "#242833"
typography:
  display-xl: {fontFamily: "Assistant, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Assistant, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Assistant, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.3, letterSpacing: "0.06rem"}
  body-md: {fontFamily: "Assistant, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.06rem"}
  body-sm: {fontFamily: "Assistant, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.04rem"}
  caption: {fontFamily: "Assistant, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.04rem"}
  button-md: {fontFamily: "Assistant, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1, letterSpacing: "0.06rem"}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    hoverBackgroundColor: "{colors.accent-hover}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
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
    borderColor: "{colors.divider-subtle}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  device-spec-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"

## Components

**button-primary** maps directly to the theme's `--color-button: 18,18,18` / `--color-button-text: 255,255,255` pair, giving a solid near-black CTA used for "Add to cart" and checkout actions; hover/active states darken via opacity and are proposed, not measured.

**button-secondary** mirrors the theme's `--color-secondary-button` values (white fill, dark text and border) and is proposed for lower-emphasis actions like "Compare" or "Wishlist" on device listing pages.

**button-accent** is built from the Shopify accelerated-checkout unbranded button, the only non-neutral interactive color pair in the evidence (`#1990c6` default, `#136f99` hover). It is proposed for wallet-style or express-checkout CTAs distinct from the primary black button.

**text-input** uses the light hairline (`#dedede`) as a border against white, consistent with the skeleton-loader background token; focus and error states are proposed and unverified.

**nav-bar** assumes a white header with dark ink text and a hairline bottom border, appropriate for a Shopify header with Home/Devices/Deals/Stylus/Accessories links; sticky behavior and mobile menu treatment are not observed.

**product-card** draws on `.product-card-wrapper .card` variables (radius, border, shadow, image padding all theme-driven), rendered here with a soft border, white surface, and rounded corners sized to the proposed `md` token since actual radius values were not resolved.

**hero** is proposed for a device-launch banner and uses the darker `#242833` tone (present in the palette but of undetermined original usage) as a full-bleed background with white headline text, appropriate for showcasing e-reader/tablet photography.

**device-spec-card** is a category-specific component proposed for e-reader/tablet spec sheets (screen size, resolution, battery), using caption-weight labels over body-weight values inside a bordered white card, matching the site's plain, information-dense product presentation style implied by the long variant/region text content.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Layout guidance |
|---|---|---|
| Mobile | <750px | Single-column product grid; nav collapses to a hamburger/drawer; touch targets ≥44px |
| Tablet | 750–989px | Two-column product grid; nav remains condensed |
| Desktop | ≥990px | Multi-column grid (3–4 up); full horizontal nav |

Buttons and inputs should maintain a minimum 44×44px touch target on mobile. Country/currency selector (extensive list observed in page text) should collapse into a scrollable dropdown or modal on small screens.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Static CSS extraction only; no rendered layout, breakpoints, hover/focus states, or JS-driven interactions (e.g., menu drawers, region selector behavior) were observed.
- Border-radius values reference theme CSS custom properties (`--product-card-corner-radius`, `--buttons-radius-outset`, etc.) whose resolved pixel values were not present in evidence; the `rounded` scale here is a generic proposal.
- `body`, `muted`, and `surface-dark` are inferred semantic assignments over palette colors whose original component usage in Bigme's live theme is unconfirmed.
- Colors `#eb001b`, `#f79e1b`, `#ff5f00`, `#0071ce`, `#142fbd`, `#1532cb`, and `#334fb4` are excluded from the semantic palette; they read as third-party payment-network brand marks, not Bigme brand colors.
- Only one font family ("Assistant") was observed; heading/body weight and style rely on theme variables (`--font-heading-weight`, etc.) whose literal values were not captured, so weights above are proposed.
- Font licensing/hosting (self-hosted vs. Google Fonts) was not verified from the supplied evidence.
- Typography sizes beyond the literal `1.5rem` body-font-size and `0.06rem` letter-spacing are proposed conventions for a device-catalog storefront, not extracted values.
