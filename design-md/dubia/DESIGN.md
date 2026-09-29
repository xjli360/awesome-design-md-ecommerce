---
version: alpha
name: "Dubia"
source_url: "https://dubiaroaches.com"
captured_at: "2026-09-28T10:34:06.499874+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Dubia.com's stylesheet centers on a neutral, high-contrast foundation: near-black
  text and surfaces (#121212) against white and light-gray backgrounds (#ffffff,
  #f3f3f3), consistent with the site's dense mega-menu and promo-banner heavy
  storefront for feeder insects and reptile supplies. Montserrat is the confirmed
  body and heading family (weight 300 body, 400 heading), giving a light,
  utilitarian sans-serif voice suited to a catalog-driven retailer. Fraunces
  appears in the supplied font stack and is treated here as an inferred display
  serif for hero/marketing moments, pairing an editorial accent against the
  workhorse sans-serif — its exact selector usage was not captured in evidence.
  Observed hero-card button classes show a strict black/white two-tone button
  system (dark-on-light and light-on-dark), which this spec treats as the primary
  interactive pattern. Additional palette entries — amber/gold, teal-green, and
  red — are inferred as promo/badge accents given the page text's heavy use of
  discount codes, free-shipping callouts, and "live arrival guaranteed" messaging.
  Rounded button radii (40px, from --wk-button-border-radius) suggest a pill-like
  interactive language reused here for badges and search.

colors:
  primary: "#121212"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#5f5f5f"
  hairline: "#e5e5e5"
  surface-soft: "#f3f3f3"
  surface-card: "#f9f8f4"
  on-primary: "#ffffff"
  accent-gold: "#f4c430"
  accent-teal: "#217a49"
  accent-red: "#cc0e39"
  accent-blue: "#177ea7"
  surface-alt: "#f7f7f7"
typography:
  display-xl: {fontFamily: "Fraunces, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Fraunces, serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.02em}
  body-md: {fontFamily: "Montserrat, sans-serif", fontSize: 16px, fontWeight: 300, lineHeight: 1.5, letterSpacing: 0.03em}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 300, lineHeight: 1.5, letterSpacing: 0.02em}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.04em}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.08em}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  promo-banner:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.base}"

## Components

**button-primary** reflects the observed `.dubia-hero-card__button--dark` pattern: solid dark background (#121212) with white text, used for the site's black-on-light CTA style seen on hero slider cards. The full/pill radius is proposed to align with the observed 40px `--wk-button-border-radius` token from the wishlist/button component system.

**button-secondary** mirrors the observed `--outline-dark` hero button variant: transparent background, dark border and text, intended for lower-emphasis actions like "Learn More" or secondary nav CTAs. Hover-state fill is proposed, not observed, based on the `.header__auth-btn--outline:hover` rule which fills to foreground color.

**text-input** is proposed for search and account forms. No explicit input styling was captured beyond `--wk-input-border-radius: 0px` and `--wk-input-min-height: 45px`, so a square-cornered, hairline-bordered field is inferred from that token.

**nav-bar** represents the mega-menu header implied by the extensive "Shop By Pet" / "Live Food" / "Care" category text. Layout (sticky, dropdown mechanics) is proposed; only text content and general foreground/background variables were observed.

**product-card** is a proposed pattern for catalog/collection grids (e.g., Dubia Roaches, Enclosures, Food listings), using the off-white surface-card tone (#f9f8f4) and hairline border for separation, since no explicit card CSS was supplied.

**hero** is grounded in the confirmed `.hero-slider` and `.hero-launch--habitat` selectors, which show dark-background, light-text hero cards with both solid and outline button variants — this is the most directly evidenced component.

**footer** background/text pairing is inferred (dark-on-white sites commonly invert footer to dark); no footer-specific selectors were present in evidence, so this should be treated as a proposal only.

**badge** covers promotional callouts like "25% OFF," "FREE SHIPPING," and "LIVE ARRIVAL GUARANTEED" visible in page text; accent-red is chosen as a plausible urgency color from the observed palette, though the actual badge color was not captured in CSS rules.

**search** and **promo-banner** are category-appropriate additions: the announcement bar rotating discount codes and shipping notices is a defining, repeatedly-mentioned feature of this storefront's text content, so a dedicated promo-banner component is proposed using the observed gold accent (#f4c430) for visibility.

## Responsive Behavior

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| mobile | <768px | Single-column product grid, collapsed hamburger nav, promo-banner truncates to single rotating message |
| tablet | 768–1024px | 2-column product grid, nav collapses secondary categories into "Shop" dropdown |
| desktop | 1024–1440px | Full mega-menu nav, 3–4 column product grid |
| wide | >1440px | Max-width content container, hero slider gains larger padding |

Touch targets should target a minimum 44px height, consistent with the observed `--wk-button-min-height: 45px` and `--wk-input-min-height: 45px` tokens. Mobile nav collapse behavior, sticky header state, and drawer/cart interactions are **not observed** and are recommended defaults only, not measured site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction; no rendered layout, computed breakpoints, or interaction states (hover, focus, active, disabled) were directly observed beyond the few explicit `:hover` rules supplied.
- Color role assignments (e.g., accent-gold as promo/badge, accent-red as urgency) are inferred from page-text context (discount codes, shipping banners), not confirmed CSS class-to-color bindings.
- Font sizes across the typography scale beyond the root `1.5rem` body rule and `0.06rem` letter-spacing are proposed estimates, not measured computed styles.
- Fraunces' actual usage/selector was not present in the supplied CSS rules; its inclusion as a display font is inferred solely from its presence in the font-family list.
- Mobile/responsive layout behavior, nav collapse mechanics, and cart/drawer patterns were not observed and are provided as generic recommendations.
- Licensing and self-hosting/CDN availability of Montserrat, Fraunces, and IBM Plex Mono were not verified from the supplied evidence.
