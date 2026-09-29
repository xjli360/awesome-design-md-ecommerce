---
version: alpha
name: "Spiritless"
source_url: "https://spiritless.com"
captured_at: "2026-09-28T09:28:13.795454+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Spiritless presents as a modern, editorial non-alcoholic spirits brand built on a warm neutral base with a confident red accent. The observed palette centers on near-black ink (#1a1a1a) over white and warm off-white surfaces (#e8e5db, #e8e8e1, #f2f2f2), with #d63636 serving as the dominant call-to-action and sale/announcement color, dimmed by #c92929 on active states. A teal (#009975) appears as a secondary sale-tag color. Theme CSS variables confirm nav and footer both use the warm beige #e8e5db, while borders use the closely related #e8e8e1 hairline tone.

  Typography is explicitly declared in theme CSS: headings (h1–h6, section titles) use "GT Super Display," a serif display face, while body copy, buttons, and labels use "Basis Grotesque Med," a grounded grotesk sans. An italic variant of Basis Grotesque is also present, suggesting emphasis or pull-quote use. No Georgia or system-serif fallback was observed in the live rule set beyond generic serif/sans-serif chains, so those are used as fallbacks only.

  This interpretation proposes a restrained, product-forward system: generous whitespace, sharp-edged buttons (site uses border-radius:0 on review-widget buttons), and warm beige surfaces for cards and footer, reserving red strictly for primary actions, sale badges, and the announcement bar. Layout specifics, spacing scale, and interaction states beyond those in the CSS are proposed, not observed.

colors:
  primary: "#d63636"
  primary-dim: "#c92929"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#1a1a1a"
  muted: "#828282"
  hairline: "#e8e8e1"
  surface-soft: "#f2f2f2"
  surface-card: "#e8e5db"
  on-primary: "#ffffff"
  accent-teal: "#009975"
  border-subtle: "#e5e5eb"
  link-color: "#676986"
  modal-bg: "#1a1a1a"
typography:
  display-xl: {fontFamily: "'GT Super Display', serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0em}
  display-md: {fontFamily: "'GT Super Display', serif", fontSize: 34px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0em}
  title-md: {fontFamily: "'GT Super Display', serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0em}
  body-md: {fontFamily: "'Basis Grotesque Med', sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0em}
  body-sm: {fontFamily: "'Basis Grotesque Med', sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0em}
  caption: {fontFamily: "'Basis Grotesque Med', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.02em}
  button-md: {fontFamily: "'Basis Grotesque Med', sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.02em}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge-sale:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.base}"
  search-field:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  recipe-card:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"

## Components
**button-primary** uses the observed `--colorBtnPrimary` red (#d63636) with white text, matching the theme's confirmed CTA styling; sharp corners are proposed to echo the zero-radius review-widget buttons actually present in the CSS. **button-secondary** is a proposed outline variant for lower-emphasis actions like "View all" or filter toggles, not directly observed but consistent with the single-accent palette. **text-input** and **search-field** are proposed using the light input background (#f2f2f2/#ffffff) and hairline border variables confirmed in `:root`. **nav-bar** uses the observed `--colorNav`/`--colorNavText` pairing (beige on dark ink text). **product-card** is a proposed pattern for bottle/bundle listings, using canvas white with a hairline border and the serif display type for product names. **hero** is proposed for the homepage banner ("GOING DRY REDEFINED") using dark ink background with white hero text, matching `--colorHeroText:#ffffff`. **footer** directly reuses the confirmed `--colorFooter`/`--colorFooterText` beige pairing. **badge-sale** maps to the confirmed `--colorSaleTag:#009975` teal, distinct from the primary red, for sale/promo labeling. **announcement-bar** reuses the confirmed `--colorAnnouncement:#d63636` and its white text variable directly from theme CSS. **recipe-card** is a proposed component for the "But First, We Mix" recipe grid, using soft warm surface tones consistent with the rest of the palette.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured from live site behavior:
| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| mobile | <600px | Single-column stack; nav collapses to hamburger; hero text reduces to display-md scale |
| tablet | 600–1024px | Two-column product grids; nav remains collapsed or condensed |
| desktop | 1024–1440px | Full nav bar, multi-column product/recipe grids |
| wide | >1440px | Max content width constrained, extra margin added |

Touch targets should be a minimum 44px hit area for cart/nav icons; mobile menu collapse and cart drawer behavior are inferred from the presence of "Close menu"/"Close cart" text but not visually verified.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, responsive breakpoints, or interaction states (hover, focus, active, loading) were visually observed beyond the review-widget's explicit hover/active variable declarations. Font availability and licensing for "GT Super Display" and "Basis Grotesque Med" were not verified—these are proprietary-sounding names taken directly from CSS but their loading source, weights, and license status are unconfirmed; generic serif/sans-serif fallbacks are included accordingly. Numeric type scale (font sizes for display-xl, title-md, etc.) beyond the confirmed 34px header/15px body values are proposed, not measured. Spacing and rounded-corner scales are proposed conventions, not extracted from layout measurements. Component definitions for product-card, hero, search-field, and recipe-card are inferred design patterns appropriate to a DTC beverage storefront, not confirmed from rendered DOM or screenshots. Color role assignments (e.g., which beige is footer vs. surface-card) are based on CSS custom-property names and may not reflect final visual hierarchy.
