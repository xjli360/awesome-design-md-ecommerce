---
version: alpha
name: "Little Kideauxs"
source_url: "https://littlekideauxs.com"
captured_at: "2026-09-29T04:15:38.243291+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Little Kideauxs is a Shopify-powered storefront selling needlepoint-embroidered
  baseball, rope, and snapback hats for children ages 1–10, designed in
  Louisiana with a southern, preppy sensibility. The extracted evidence gives a
  neutral, high-contrast base palette (white canvas, near-black text at #121212
  and #232323, light gray skeleton/border tones at #dedede and #f3f3f3) rather
  than a saturated brand color system. The only functionally observed
  chromatic value is #1990c6, used as the background of the Shopify
  accelerated-checkout button (with #136f99 as its hover state), so this
  interpretation promotes that blue as the working primary/interactive color;
  this is a semantic inference from a payment-widget default, not a confirmed
  brand color, and is labeled as such. Several other palette entries
  (#eb001b, #f79e1b, #ff5f00, #334fb4, #0071ce, #142fbd, #1532cb) are standard
  card-network icon colors (Mastercard, Visa, PayPal, etc.) and are excluded
  from brand role assignment. Typography pairs the serif "Arapey" for
  headline/display roles with "Assistant" for body and UI text, inferred from
  the two observed non-utility font families and the theme's heading/body
  variable convention; exact heading sizes are proposed, while the 24px/0.06rem
  body letter-spacing is directly observed on the root body rule. The overall
  interpretation favors a light, airy, southern-preppy children's-goods feel:
  generous whitespace, soft neutral surfaces, and a single confident accent
  used sparingly for calls to action.

colors:
  primary: "#1990c6"
  accent-dark: "#136f99"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#232323"
  muted: "#dedede"
  hairline: "#dedede"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  overlay-transparent: "#00000000"
typography:
  display-xl: {fontFamily: "Arapey, serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Arapey, serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Assistant, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0.02em}
  body-md: {fontFamily: "Assistant, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.8, letterSpacing: 0.06rem}
  body-sm: {fontFamily: "Assistant, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.03em}
  caption: {fontFamily: "Assistant, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.04em}
  button-md: {fontFamily: "Assistant, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.04em}
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
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
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
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    hairline: "{colors.muted}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  age-size-chip:
    backgroundColor: "{colors.surface-soft}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.base}"

## Components

**button-primary** is the main commerce action (Add to Cart, Shop links) using the observed accelerated-checkout blue (#1990c6) with white text; a proposed hover state would shift to #136f99, matching the CSS-defined hover rule for the unbranded payment button.

**button-secondary** is an outline-style action for tertiary flows (e.g., "View all," "Continue shopping") — inferred from the theme's `.button--secondary`/`.button--tertiary` CSS variables that swap button and background colors rather than introducing a new hue.

**text-input** covers the email subscribe field and search box; background and border values are inferred from the neutral palette since no explicit input styling was supplied.

**nav-bar** represents the header row (Home, Catalog, New Arrivals, hat-type links, Contact, cart, search) on a white canvas with dark text, per the light body background and near-black `--color-base-text` inference.

**product-card** models the hat listing tiles (name, vendor "Little Kideauxs," regular/sale price, "Sold out" badge) using serif-free title text and a light card surface; hover elevation is proposed, not observed.

**hero** is the homepage banner ("Fun and classic hat designs for your Little Kideauxs. Shop New Arrivals") using the serif display font on a soft neutral background; exact imagery/overlay treatment is not observed.

**footer** mirrors the dark, high-contrast footer content (Quick links, Our Story, payment icons, social links) using ink-on-light or inverted treatment — the inverted footer background is a proposed pattern, not a measured value.

**badge** supports status labels like "Sold out" and payment-method chips, styled as a bordered pill on white per `--color-badge-*` variables.

**age-size-chip** is a category-appropriate control for the brand's ages-1–10 sizing model, proposed as a pill selector that fills with the primary blue when active — no such component was directly observed in the supplied CSS, so it is fully proposed to fit the product domain.

## Responsive Behavior

Recommended, not measured, breakpoints:

| Breakpoint | Width       | Notes |
|---|---|---|
| Mobile | <600px | Single-column product grid, collapsed hamburger nav, stacked hero |
| Tablet | 600–959px | 2-column product grid, inline search icon |
| Desktop | ≥960px | Full nav bar, 3–4 column product grid, sticky header optional |

Touch targets should be at least 44px for buttons and chips (aligned with the observed `--shopify-accelerated-checkout-button-block-size` clamp of 25–55px). Nav collapses to a drawer/hamburger below tablet width; this is a standard Dawn-theme pattern assumption, not a confirmed observation.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is built from static CSS/text extraction only; no rendered layout, hover/focus states, animations, or actual mobile breakpoints were observed. The primary accent color (#1990c6) is inferred from a Shopify payment-button default rather than a confirmed brand swatch — the true brand accent (if any) is unverified. Font-family role assignment (Arapey = display, Assistant = body) is inferred from naming convention, not confirmed heading usage. All font sizes except the root 24px/0.06rem body rule are proposed. Border-radius values are a proposed scale; only 0px (button fallback) was directly observed. Card-network palette entries were deliberately excluded from brand roles. Custom font licensing/availability for Arapey and Assistant was not verified. Component states (hover, active, disabled, error) beyond the two documented payment-button rules are proposed only.
