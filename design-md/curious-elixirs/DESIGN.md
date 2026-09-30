---
version: alpha
name: "Curious Elixirs"
source_url: "https://curiouselixirs.com"
captured_at: "2026-09-29T03:55:44.503631+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Curious Elixirs presents booze-free craft cocktails with a warm, apothecary-meets-cocktail-bar aesthetic. The observed palette centers on a warm terracotta (#d5835b) paired with golden ambers (#ebb66c, #f2b56e) and cream surfaces (#fef1de, #fbefdc), evoking infused spirits and citrus garnish. A deep navy-black (#060626), confirmed as the heading and referral-widget text color, anchors typography against white canvases. A saturated red (#d02e2e) appears in the palette and is inferred here as a sale/promo accent given cart-banner language ("$10 off," "37% off"), while muted slate (#676986) and light hairlines (#dbdde4, #e5e5eb) come from the Okendo review-widget CSS variables and are reused for secondary text and dividers.
  Font evidence includes IvyPresto Display/Headline (serif, likely editorial headlines), Dallas-Regular/Light (a distinct weighted family, inferred as UI/product-title font), and Work Sans (a standard grotesk, inferred as body/button copy). Rasa, Vollkorn, Montserrat, and Lexend also appear but their in-page roles are unconfirmed, so they are treated as secondary/unused-in-spec candidates.
  This spec proposes a cream-and-terracotta storefront with navy ink, gold accents for badges/ingredients callouts, and red reserved for promotional urgency — all roles inferred from usage context, not verified visual layout.

colors:
  primary: "#d5835b"
  ink: "#060626"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#676986"
  hairline: "#dbdde4"
  surface-soft: "#fef1de"
  surface-card: "#fbefdc"
  on-primary: "#ffffff"
  accent-gold: "#ebb66c"
  accent-warm: "#f2b56e"
  accent-tan: "#d4c3a9"
  sale: "#d02e2e"
  success: "#56ad6a"
  link: "#2563eb"
  surface-dark: "#171d3b"
  surface-darker: "#0d0d52"
  border-light: "#e5e5eb"
typography:
  display-xl: {fontFamily: "IvyPresto Display, serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "IvyPresto Headline, serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Dallas-Regular, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Work Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Work Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Work Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Work Sans, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.2px}
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    borderBottom: "1px solid {colors.border-light}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    shadow: "0 1px 3px {colors.border-light}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  ingredient-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md} {spacing.lg}"
    iconColor: "{colors.accent-warm}"

## Components

**button-primary** uses the terracotta brand color for primary calls-to-action like "Shop Now" or "Explore Elixirs," with white text for contrast. Hover/active states are proposed, not observed.

**button-secondary** is an outlined variant for lower-emphasis actions (e.g., "Log in"), using the ink color on a transparent field with a light hairline border, mirroring the border tokens found in the Okendo review-widget CSS.

**text-input** covers search and account fields; the hairline border and white background are inferred from typical e-commerce conventions since no direct input styling was captured in the extracted CSS.

**nav-bar** represents the top navigation containing "Booze-Free Cocktails," "Flavor Quiz," "Bundle & Save," etc. A white background with a light bottom border is proposed; actual sticky/scroll behavior was not observed.

**product-card** models the flavor tiles (Curious No. 1–9, bundles) using a warm cream card surface, rounded corners, and a serif-adjacent title style, distinguishing product names from body copy.

**hero** reflects the homepage banner text ("Award-Winning Non-Alcoholic Drinks," "Feel better tomorrow without giving up tonight") on a soft cream background with large display typography.

**footer** is inferred as a darker navy surface for contrast/closure, using cream text — this color pairing is plausible given the dark navy tokens present but placement in-page was not directly observed.

**badge** covers small labels like "No Added Sugar," "Gluten-Free," or promotional banners ("$10 off"), using the gold accent for a warm, food-safe callout style; the sale-red token is reserved separately for urgent discount badges.

**search** models the "Open search bar" interaction referenced in the page text, styled consistently with the text-input pattern.

**ingredient-callout** is a category-specific component for listing adaptogens/superfoods (e.g., "Rhodiola, Gentian, Bitter Orange") beneath product names, using the cream surface and warm icon accent to reinforce the wellness positioning.

## Responsive Behavior

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | up to 599px | Single-column stack, nav collapses to hamburger menu, touch targets ≥44px |
| Tablet | 600–1023px | Two-column product grids, nav may remain collapsed |
| Desktop | 1024px+ | Multi-column product grids, full horizontal nav |

This table is a recommendation based on common e-commerce patterns, not measured site behavior. Buttons and nav items should maintain a minimum 44×44px touch target on mobile. Actual collapse thresholds, menu animation, and mobile layout were not observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS/text extraction only; no rendered layout, breakpoints, or interaction states (hover, focus, active, loading) were directly observed beyond the Okendo widget's own CSS variables. Color-role assignments (e.g., sale-red, gold-as-badge, navy-as-footer) are inferred from contextual page copy and typical e-commerce conventions, not confirmed via computed styles on brand-specific elements. Font usage for IvyPresto and Dallas families is inferred as headline/title roles based on naming convention and presence in the font list; their actual application, weight availability, and licensing were not verified. Spacing and border-radius values beyond the Okendo button (--oke-button-borderRadius:4px) are proposed defaults, not measured from the storefront's own components. Mobile navigation, cart drawer, and product-page layouts were not captured in the provided evidence.
