---
version: alpha
name: "Liquid Death"
source_url: "https://liquiddeath.com"
captured_at: "2026-09-29T04:09:22.573122+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Liquid Death presents itself as a Shopify-hosted storefront for canned mountain water, sparkling
  water, energy drinks and iced tea, wrapped in a heavy-metal, mock-horror brand voice ("Murder Your
  Thirst"). The observed palette is dominated by true black (#000000) and near-black (#151515) paired
  with white (#ffffff), consistent with the brand's signature monochrome skull-and-can aesthetic. A
  muted antique-gold (#8a6d35) appears explicitly as the active/hover navigation color, so it is treated
  here as the primary interactive accent rather than a decorative extra. Bright yellow (#fff100) and red
  (#e4002b) are present in the supplied palette and are inferred as flavor/energy-line accent colors,
  since the copy references distinct product lines (Energy, Iced Tea, Sparkling Water, Mountain Water)
  that a Shopify catalog typically color-codes. Utility blue (#1990c6) is an observed Shopify payment-
  button color and is kept only for that system role, not as a brand color. Typography evidence is mixed:
  a generic Shopify/system UI stack (Inter, Acumin Pro, Segoe UI, Helvetica Neue) governs interface text,
  while brand-flavored display faces (Splash, SuperClarendon, Cedarville Cursive) appear in the font
  list and are inferred as headline/display and playful-script accents; none of their sizes were directly
  measured, so all type scale values below are proposed.

colors:
  primary: "#000000"
  ink: "#151515"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6b7280"
  hairline: "#e0e0e0"
  surface-soft: "#f5f5f5"
  surface-card: "#f0f0f0"
  on-primary: "#ffffff"
  accent-gold: "#8a6d35"
  accent-yellow: "#fff100"
  accent-red: "#e4002b"
  utility-blue: "#1990c6"
typography:
  display-xl: {fontFamily: "Splash, Acumin Pro, sans-serif", fontSize: 56px, fontWeight: 800, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "SuperClarendon, Acumin Pro, serif", fontSize: 36px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Acumin Pro, Inter, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, Acumin Pro, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Inter, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "Acumin Pro, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.3px}
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
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    activeTextColor: "{colors.accent-gold}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.muted}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
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
  flavor-carousel:
    backgroundColor: "{colors.canvas}"
    accentColor: "{colors.accent-red}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"

## Components

**button-primary** models the black, white-text CTA pattern implied by repeated "SHOP NOW" and "LEARN HOW" calls to action; the flat black fill and squared corners follow the observed `#151515`/`#000000` border and text-color rules on hover states. States beyond default/hover are proposed.

**button-secondary** is an outline variant for lower-emphasis actions (e.g. "WATCH VIDEO"), using the same ink border/text so it can sit on white or black sections without a second brand color; hover/active fills are proposed, not observed.

**text-input** covers newsletter and account-style fields ("STAY UPDATED" email capture). Border and radius are proposed defaults since no dedicated input CSS was supplied; text color follows the body role.

**nav-bar** reflects the confirmed `.main-header.active .nav-link-active` rule, which sets active/hover link color to the gold `#8a6d35` against a presumed black header background — the one directly observed interaction color in the evidence.

**product-card** represents the flavor tiles seen in the page text (e.g. "MANGO CHAINSAW," "10 Calories"), using the light card surface and ink text; the Rebuy widget's `.rebuy-product-title`/`.rebuy-money` rule (color `#151515`, 16px) directly informs the title/price color and size.

**hero** is the full-bleed black banner pattern implied by repeated large campaign statements ("WE MADE A BETTER-FOR-YOU ENERGY DRINK"); typography and spacing are proposed since no hero-specific CSS was captured.

**footer** groups the "INFORMATION" and "COMPANY" link columns and social counts (7.5M/7.2M) visible in the page text, kept on the black background with muted gray links for secondary items and white for primary links; exact link states are proposed.

**badge** is a small pill for calorie/flavor-type labels ("Energy," "Iced Tea," "0 Calories") using the bright yellow accent for shelf-style scannability; this role is inferred from the repeated numeric-calorie pattern in the text, not from a captured badge component.

**search** is a proposed utility for the site's product/flavor lookup, styled with the soft surface and hairline border consistent with the rest of the neutral palette; no dedicated search CSS was supplied.

**flavor-carousel** is the category-appropriate component for horizontally scrolling flavor/product tiles, grounded in the observed Flickity carousel rule (`.flickity-button` positioning/arrow image) used in the Rebuy product widget; the red accent marks the active/selected flavor indicator and is proposed.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width       | Layout guidance                                  |
|-----------|-------------|---------------------------------------------------|
| sm        | 0–599px     | Single-column hero/product stack, nav collapses to hamburger |
| md        | 600–959px   | 2-column product grid, carousel shows 2 cards      |
| lg        | 960–1279px  | 3–4 column product grid, full inline nav           |
| xl        | 1280px+     | 4+ column grid, hero uses larger display type      |

Touch targets should be at least 44px in height for buttons and nav links (per the observed accelerated-checkout button clamp of 25–55px). Navigation should collapse below `md`; carousel arrows (per the observed `.flickity-button` rule) should remain tappable at the same 44px minimum. No mobile layout or breakpoint values were directly observed; this table is a proposal only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is limited to static CSS/text extraction; no live rendering, computed layout, or DOM structure was observed, so grid columns, header height, and hero composition above are inferred conventions, not measurements.
- Font-role assignments (Splash, SuperClarendon, Cedarville Cursive to display/script roles) are inferred from font-family list order and brand tone; actual usage per element was not confirmed, and licensing/availability of these families is not verified.
- Only one brand-specific color-role rule was directly observed (`#8a6d35` nav active/hover); all other role assignments (primary, ink, muted, badges) are inferred by matching palette values to plausible UI roles.
- Type sizes in the scale above are proposed except the 16px value taken from the `.rebuy-product-grid` title/price rule.
- Interaction states (focus, disabled, error, mobile menu open/closed) and true mobile/responsive layout were not observed in the supplied evidence.
- Several supplied CSS rules originate from third-party Shopify extensions (accelerated checkout, geolocation modal), not the core theme, and their colors (e.g. utility blue) are kept scoped to those components only.
