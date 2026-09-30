---
version: alpha
name: "Radiance Films"
source_url: "https://www.radiancefilms.co.uk"
captured_at: "2026-09-28T09:52:32.798388+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Radiance Films is a Shopify-powered specialty retailer of collector's-edition
  Blu-ray and UHD releases (classic, cult, and arthouse cinema). The extracted
  CSS is dominated by Shopify's Dawn-theme base variables and third-party
  payment-icon assets (Mastercard, PayPal, Diners, etc.), so most literal hex
  values in the supplied palette describe checkout chrome rather than brand
  identity. The one clearly product-specific accent is the accelerated-checkout
  button pairing, #1990c6 with a #136f99 hover state, which this spec treats as
  the inferred primary interactive color. Text and background tones are drawn
  from the near-black #01090e / #121212 range against near-white #ffffff,
  #fcfcfc, and #fefefe canvases, with #212b36 proposed as the running body-text
  color (a common Dawn `--color-base-text` value) and #666666/#888888 as muted
  secondary text. Hairlines and card surfaces use the light gray family
  (#dddddd, #e4e4e4, #f5f5f5). Typography is limited to two observed families:
  Josefin Sans, a narrow geometric sans well suited to poster-forward,
  editorial headings, and Roboto for workhorse body and UI text; both fall back
  to system sans-serif. The interpretation favors a dark, cinema-poster-led
  layout with restrained chrome, letting cover art carry visual weight while
  UI elements stay quiet and utilitarian.

colors:
  primary: "#1990c6"
  primary-hover: "#136f99"
  ink: "#01090e"
  canvas: "#ffffff"
  body: "#212b36"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#fcfcfc"
  on-primary: "#ffffff"
  border-soft: "#e4e4e4"
  skeleton: "#dedede"
  ink-deep: "#121212"
  muted-strong: "#888888"
typography:
  display-xl: {fontFamily: "'Josefin Sans', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Josefin Sans', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "'Josefin Sans', sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.25, letterSpacing: "0.02rem"}
  body-md: {fontFamily: "'Roboto', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.06rem"}
  body-sm: {fontFamily: "'Roboto', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.04rem"}
  caption: {fontFamily: "'Roboto', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.06rem"}
  button-md: {fontFamily: "'Roboto', sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: "0.06rem"}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.border-soft}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.muted-strong}"
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
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  edition-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** is proposed for primary calls to action ("Add to cart", "Notify Me"), reusing the observed accelerated-checkout accent `#1990c6` since that is the only unambiguous interactive brand color in the extracted CSS; hover/pressed states are proposed, not observed.

**button-secondary** covers outline-style actions (filters, "Continue shopping"), using canvas background with an ink-colored label and a light hairline border, consistent with Shopify Dawn's `--color-button: var(--color-background)` outline pattern seen in the base CSS.

**text-input** models the email-signup and search fields referenced in the page text ("Join our email list…"), using a plain canvas field with a soft hairline border; focus and validation states are proposed and unobserved.

**nav-bar** represents the top utility/category bar implied by the long list of collection links (Shop, Crime & Noir, Arthouse, Horror, USA, Italy, Japan, France, Radiance, Hosted Labels). A light canvas bar with ink text is proposed; no actual header layout, height, or sticky behavior was measured.

**product-card** is the core catalog unit for titles like "Ossessione" and "Across 110th Street," pairing a light card surface with a soft border, small-caption title type, and slightly larger price type to match the repeated "Regular price / Sale price / Unit price" pattern in the text excerpt.

**hero** proposes a dark, poster-forward banner (ink background, white text, large Josefin Sans display type) appropriate for a cinema/collector's-edition storefront, though no hero markup or imagery was present in the supplied evidence.

**footer** reflects the long link list (About, FAQ, Shipping & Returns, Terms, Privacy Policy, Jobs, Calendar) and payment-icon row; a near-black background with muted gray text is proposed to visually separate it from the lighter body content.

**badge** supports labels such as "Sale," "Sold Out," and "Exclusives" seen in the navigation/collection text; a pill outline in ink-on-canvas is proposed as a neutral default since no confirmed sale-red brand color could be isolated from the payment-icon palette.

**search** models the header search affordance implied by "Search" in the page text, styled as a full-radius canvas field consistent with the `full` rounded token.

**edition-tag** is a category-specific component for physical-media metadata such as "(LE)", "(UHD + BD LE)", and "UHD Bundles," rendered as a small muted chip distinct from primary badges, since these labels recur heavily across product titles in the evidence.

## Responsive Behavior

This is a recommended breakpoint scheme, not a measured observation of the live site's responsive CSS.

| Breakpoint | Width      | Notes (proposed) |
|-----------|------------|-------------------|
| compact   | <480px     | Single-column product grid, collapsed nav into a drawer/menu, touch targets ≥44px |
| medium    | 480–768px  | 2-column product grid, search remains inline |
| large     | 768–1024px | 3-column product grid, full nav bar visible |
| wide      | 1024px+    | 4+ column grid, hero at full display-xl scale |

Buttons and form inputs should maintain a minimum 44px tap target on touch devices. Navigation collapse (hamburger vs. inline links) is a standard e-commerce pattern assumption, not confirmed from the extracted CSS or markup.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS/text extraction only; no rendered layout, grid structure, or breakpoints were observed, so all responsive guidance above is a recommendation.
- The supplied palette is heavily populated by third-party payment-icon brand colors (Mastercard red/orange, PayPal blue, Diners/Discover greens) and generic Bootstrap-style utility colors (`#007bff`, `#dc3545`); these are excluded or treated cautiously rather than assigned brand roles.
- `#1990c6` / `#136f99` are drawn from the accelerated-checkout wallet button CSS, which may reflect a Shopify component default rather than a deliberate brand choice; treated here as the best available primary-accent signal.
- `#212b36` is inferred as the body-text color from Shopify Dawn's base-text CSS variable pattern, not confirmed via a direct rendered computed style.
- The supplied `font_families` list included a non-font value ("object-fit: contain"), indicating noisy extraction; only "Josefin Sans" and "Roboto" were treated as real families.
- No custom font hosting, licensing, or weight-availability was verified; only the two named families are assumed available with sans-serif fallback.
- No hover, focus, active, error, or loading states were visually observed; all such states in components above are proposed conventions.
- Product imagery, grid density, and card sizing for the "Sale"/collector's-edition product listings were not observed and are inferred from typical e-commerce conventions.
