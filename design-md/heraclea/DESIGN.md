---
version: alpha
name: "Heraclea"
source_url: "https://heraclea.co"
captured_at: "2026-09-28T10:04:13.128972+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Heraclea's evidence points to an earthy, editorial Mediterranean palette built around deep teal-greens (#236776, #1c5561, #326f83), olive/sage tones (#b0b994, #a0a887, #d6debd), and terracotta browns (#763426, #602b20, #c3a683, #cda787) set against warm off-white canvases (#fcfbf5, #ebe9de) and true ink (#000000, #111827). These earth and sea hues read as brand-forward accents against neutral grays used for structure (#374151, #4b5563, #9ca3af, #e5e7eb). Two font families are confirmed in the CSS: "Assistant" (a humanist sans, used for UI/body-weight text) and "Suisse Works" (a serif-leaning display face used for editorial headings), with "Times" as a system fallback and sans-serif as the generic fallback. This interpretation assigns Suisse Works to display/heading roles and Assistant to body/UI roles as an inferred split, since the CSS custom properties (--font-body-family, --font-heading-family) were not resolved to explicit values in the supplied evidence.

  Layout patterns (product cards, hero banners, review widgets) are proposed based on Shopify-theme conventions and the oke-reviews component tokens observed (4px button radius, 1px hairlines, #236776 button background). Rounded corners stay modest (0–8px) to match the button radius token actually observed. No live page geometry, spacing rhythm, or responsive breakpoints were measured; all sizing values below are proposed defaults for a specialty food/pantry storefront unless otherwise noted.

colors:
  primary: "#236776"
  primary-deep: "#1c5561"
  accent-olive: "#b0b994"
  accent-terracotta: "#763426"
  accent-terracotta-deep: "#602b20"
  accent-sand: "#c3a683"
  ink: "#111827"
  body: "#374151"
  muted: "#6b7280"
  hairline: "#dbdde4"
  canvas: "#fcfbf5"
  surface-soft: "#ebe9de"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border-strong: "#b6b6b6"
typography:
  display-xl: {fontFamily: "'Suisse Works', Times, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Suisse Works', Times, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Assistant, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Assistant, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.06rem}
  body-sm: {fontFamily: "Assistant, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0.04rem}
  caption: {fontFamily: "Assistant, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.08rem}
  button-md: {fontFamily: "Assistant, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.04rem}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
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
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-olive}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  origin-strip:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.base}"

## Components
**button-primary** uses the observed `#236776` value from the oke-reviews button token (`--oke-button-backgroundColor`) as the storefront's primary action color, paired with white text and the observed 4px radius. This is the most concrete component-level evidence in the supplied CSS.

**button-secondary** is a proposed outline treatment for lower-emphasis actions ("Learn More", "View my cart"), using the hairline gray border seen in the reviews token set (`#dbdde4`) rather than a filled background, so it recedes next to the primary teal button.

**text-input** is proposed for newsletter and search fields; it borrows the same hairline border and canvas background, keeping form fields visually quiet against the warm off-white page background.

**nav-bar** is inferred from the presence of "Menu," "Shop," "Our Story," and cart-count text in the page copy; no header CSS was supplied, so background/border values are proposed defaults using canvas and hairline tokens.

**product-card** supports the bundle/collection tiles referenced in the copy (Bestsellers Collection, Tin Collection, Aegean Flavors Collection), each showing a star rating, title, and sale/regular price pair. Card structure, radius, and padding are proposed; only the surface-card white and hairline border are grounded in the observed palette.

**hero** models the homepage banner ("A table without olive oil is a table unfinished") against the sage-toned surface-soft background (`#ebe9de`), which appears in the grove/mill section CSS as a content background. Headline typography uses the inferred display font.

**footer** is proposed using the darker teal (`#1c5561`) as a grounding footer background with white text, echoing the primary teal family without duplicating the button color exactly; this pairing is not confirmed by supplied footer-specific CSS.

**badge** covers the "Fair Trade," "SAVE 5%," and rating-count labels seen throughout the copy, using the olive accent as a pill background — a proposed styling choice since no badge CSS was supplied.

**origin-strip** is a category-appropriate proposed component for a thin banner calling out PDO certification, single-estate sourcing, or the free-shipping/first-order promo line seen at the top of the page, using the terracotta accent for warmth and contrast against the teal primary.

## Responsive Behavior
Recommended, not measured:

| Breakpoint | Range | Layout notes (proposed) |
|---|---|---|
| mobile | <600px | Single-column stack; nav collapses to hamburger menu; hero headline drops to ~32px |
| tablet | 600–959px | 2-column product/collection grid; sticky top promo bar retained |
| desktop | 960–1279px | 3-column product grid; full horizontal nav |
| wide | ≥1280px | Max content width with generous side gutters; 3–4 column grids |

Touch targets should be at least 44×44px for cart, menu, and add-to-bag controls. Mobile nav is expected to collapse into a slide-out or overlay menu given the "Menu"/"Skip to content" text present in the excerpt, but the actual collapse mechanism was not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Static CSS/HTML extraction only; no rendered layout, computed styles, or JavaScript-driven states were observed.
- Font-family role assignment (display vs. body) is inferred; the theme's `--font-body-family` and any heading-family custom properties were not resolved to explicit values in the supplied evidence, so the Suisse Works/Assistant split is a reasonable but unconfirmed mapping.
- Font licensing and availability for "Suisse Works," "Suisse Int'l," and "Assistant" were not verified; fallbacks (Times, sans-serif) are included per observed CSS.
- All spacing scale, radius scale beyond the observed 4px button token, and breakpoint values are proposed defaults, not measured from the live site.
- Hover, focus, active, loading, and error states are proposed/standard patterns except where explicitly defined in the oke-reviews button tokens (hover/active background and border colors).
- Mobile navigation behavior, cart drawer interaction, and slider/carousel mechanics referenced in the page text (Previous/Next slide, Pause) were not directly observed in CSS and are described only structurally.
- Color role assignments beyond the oke-reviews and groves-section tokens are inferred from palette frequency and contrast reasoning, not confirmed semantic labels in the source CSS.
