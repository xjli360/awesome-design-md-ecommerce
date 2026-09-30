---
version: alpha
name: "Lola + The Boys"
source_url: "https://lolaandtheboys.com/"
captured_at: "2026-09-29T04:15:45.147718+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Lola + The Boys is a Chicago-born kids' (and mommy-and-me) fashion boutique whose storefront leans playful and saturated. The supplied palette is broad, consistent with a large, actively-merchandised Shopify theme layered with third-party apps (returns, back-in-stock, subscribe forms), so this spec narrows to the subset most plausibly tied to primary brand chrome: near-black text (#000000, #111111, #333333) on white canvas, a vivid magenta/pink family (#ff5bc0, #f06f9a, #f790d1) and a saturated purple family (#b90ef2, #950dc2, #3b204d) that read as celebratory accent colors fitting the "unicorns and rainbows" brand voice, plus a teal (#20b2aa) and sky blue (#2491c4) as secondary accents. Grays (#eaeaea, #f4f4f4, #cccccc, #737373) are treated as structural neutrals for hairlines and soft surfaces. Typography is directly observed: headings are set in "Tstar Pro Headline" and body copy in Inter, both with generic sans-serif fallback. Sizes, weights beyond the one confirmed 700/36px heading rule, and all spacing/radius scales are proposed design-system values, not measured from live layout, intended to support a bright, rounded, high-energy children's-apparel storefront.

colors:
  primary: "#ff5bc0"
  secondary: "#950dc2"
  accent-teal: "#20b2aa"
  accent-blue: "#2491c4"
  sale: "#dc143c"
  ink: "#000000"
  ink-soft: "#333333"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#737373"
  hairline: "#eaeaea"
  border-strong: "#cccccc"
  surface-soft: "#f7f7f7"
  surface-alt: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "'Tstar Pro Headline', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Tstar Pro Headline', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "'Tstar Pro Headline', sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Inter, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
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
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  category-tile:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components
**button-primary** carries the brand's magenta accent as a filled call-to-action (e.g. "SHOP NOW"), using bold uppercase-leaning button typography; hover/pressed states are proposed, not observed. **button-secondary** is an outline variant on ink for lower-emphasis actions like "LEARN MORE," sized to match primary. **text-input** covers newsletter and account fields, styled with a light border and soft radius consistent with generic form conventions; focus-ring treatment is proposed. **nav-bar** models the top navigation housing category links (BABY, GIRLS, TWEENS, BOYS, SHOES, ACCESSORIES) plus login/cart icons on a white bar with a thin hairline divider; mobile collapse behavior is not observed. **product-card** represents best-seller grid items (title + price stack), using card surface and a light border rather than shadow, since no shadow values were confirmed in evidence. **hero** models the top promotional band (e.g. "THE DRESS SALE") on a soft neutral background with a large display headline, matching the one confirmed 700-weight uppercase heading rule. **footer** uses an inverted ink background with white text for the newsletter/company-links region, a common pattern though the live footer background color was not directly measured. **badge** models the sale/percentage-off marker in a saturated red pulled from the palette, pill-shaped per proposed rounding scale. **search** is a proposed lightweight search affordance styled like text-input. **category-tile** is a kids-apparel-appropriate component for the shop-by-age/category tiles (BABY/GIRLS/BOYS/TWEENS, "Birthday Looks," "Sets") seen in the page text, using a soft surface block with title typography; imagery and overlay treatment are not observed.

## Responsive Behavior
Recommended, not measured: mobile <768px single-column stacking with hamburger nav collapsing the category list; tablet 768–1024px two-column product grids; desktop ≥1024px three-to-four-column grids with persistent horizontal nav. Touch targets should be at least 44px tall for nav, cart, and CTA buttons. Category tiles and hero promo bands are assumed to stack vertically below the tablet breakpoint. All breakpoints are proposed defaults, not extracted from live responsive CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This spec is derived from static CSS/text extraction only; no rendered layout, hover/focus states, or real breakpoints were observed. Color roles (primary/secondary/accent) are inferred from a large undifferentiated palette that mixes brand styling with third-party app widgets (Loop returns, Globo back-in-stock/subscribe forms), so some listed hexes may belong to those embedded tools rather than core brand chrome. Font families beyond the confirmed Inter (body) and "Tstar Pro Headline" (headings) — Alata, Karla, Montserrat, Oswald, Poppins, Sofia Pro, "untitled sans," etc. — appear in the broader CSS but were not tied to a specific brand-owned selector, and are treated here as likely third-party/plugin fonts, not brand typography. All spacing, radius, and most typography sizes/weights are proposed conventions rather than measured values. Custom font licensing and hosting were not verified. Mobile navigation, cart drawer, and product-card interaction states are not observed and are marked proposed throughout.
