---
version: alpha
name: "Custom Offsets"
source_url: "https://customwheeloffset.com"
captured_at: "2026-09-29T04:21:07.923770+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Custom Offsets presents itself as an aggressive, performance-truck aftermarket
  retailer, and the supplied CSS confirms a dark-first, high-contrast system
  built around a deep red accent. Root variables define an explicit brand
  palette: `--site-neutral-dark` (#000000) and `--site-neutral-mid` (#262626)
  anchor a black header/nav, `--site-accent-mid` (#A61622) drives primary
  buttons and highlighted finance text, and `--site-accent-dark` (#791C1B)
  supplies a darker hover/border tone with a matching drop-shadow on the
  promotional header banner. `--site-neutral-light` (#C7C7C7) is treated here
  as a light-on-dark secondary text/border tone. A distinct set of status
  colors (`--oe-replacement` #1E40AF, `--best-value` #15803D, `--site-choice`
  #F59E0B, `--most-popular` #F97316, `--featured` #6626dc) is inferred to be
  reserved for merchandising badges rather than core UI chrome. Typography is
  explicitly split: `Saira` for headings/main brand voice (observed at 64px
  uppercase on a user-facing header) and `Inter` for body copy, with `Roboto`
  observed specifically on a "store-wheels-header" pill-shaped UI element,
  suggesting Roboto is reserved for compact uppercase labels/buttons. Rounded
  corners are minimal (2px observed), reinforcing a squared, industrial,
  garage-built aesthetic rather than a soft consumer-retail feel.

colors:
  primary: "#a61622"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#262626"
  muted: "#6b7280"
  hairline: "#e0e0e0"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-dark: "#791c1b"
  accent-light: "#e00000"
  border-light: "#c7c7c7"
  badge-oe: "#1e40af"
  badge-best-value: "#15803d"
  badge-choice: "#f59e0b"
  badge-popular: "#f97316"
  badge-featured: "#6626dc"
typography:
  display-xl: {fontFamily: "Saira, sans-serif", fontSize: 64px, fontWeight: 400, lineHeight: 1.0, letterSpacing: 0px}
  display-md: {fontFamily: "Saira, sans-serif", fontSize: 36px, fontWeight: 500, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Saira, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0.25px}
  caption: {fontFamily: "Inter, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 1px}
  button-md: {fontFamily: "Roboto, Arial, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.border-light}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.badge-popular}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  vehicle-fitment-selector:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.accent-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** is the accent-red call-to-action (e.g. "SHOP NOW," "ADD TO CART") drawn directly from `.btnInstall`/`.wl-shop-btn:hover` rules using `--site-accent-mid`, with white text and a 2px squared corner consistent with the observed `border-top-left-radius:2px` on `.store-wheels-header`.

**button-secondary** is a proposed outlined variant for lower-emphasis actions (e.g. "VIEW ALL"), using the same accent red as text/border on a white background; no outlined-button CSS was directly observed, so this is inferred from the primary button's color role.

**text-input** covers form fields such as the vehicle Year/Make/Model dropdowns and search box; padding, border, and radius are proposed defaults since no explicit input CSS was supplied.

**nav-bar** reflects the observed `header .nav` (black background, white 12px uppercase links with letter-spacing) and the fixed white `#header`/`#mobile-header` bar; the two-tier structure (promo banner + primary nav) is evidenced by separate `.header-banner` and `header .nav` rules.

**product-card** is a proposed grid tile for wheel/tire/part listings (brand, model, price, badge), styled with a light card surface and hairline border; card-specific CSS was not present in evidence, so layout is inferred from general retail-catalog conventions.

**hero** models the black full-bleed banner behind "WHEELS • TIRES • SUSPENSION — BUILT FOR YOUR RIDE," using the 64px Saira display style observed on `#user-system-header` and the site's dark neutral background.

**footer** reflects the multi-column footer content (Shop, Tools, Company, Account, Support, Connect) using the dark neutral background and light-gray text color inferred from `--site-neutral-light`; exact footer CSS rules were not supplied.

**badge** represents the merchandising labels implied by the dedicated status-color variables (OE Replacement, Best Value, Site's Choice, Most Popular, Featured); no badge markup/CSS was directly observed, so shape and padding are proposed.

**search** models the header search/gallery-search affordance using a soft neutral background and hairline border; specific search-input styling was not present in the evidence.

**vehicle-fitment-selector** is the category-defining "Shop By Vehicle" Year/Make/Model/Trim/Drive picker central to this site's fitment-guarantee positioning; it is proposed as a bordered light panel using the accent-dark tone as a distinguishing edge, since no direct CSS for this widget was supplied.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–599px | Single-column stacking; `#mobile-header` (observed as sticky, flex-column, white background) becomes primary chrome; nav collapses behind `.header__burger`. |
| tablet | 600–959px | Two-column product grids; vehicle-fitment-selector fields stack in pairs. |
| desktop | 960–1279px | Full multi-column mega-nav (as implied by extensive `header .nav` category list); 3–4 column product grids. |
| wide | 1280px+ | Hero and category rails use full-bleed backgrounds with centered max-width content. |

Touch targets are recommended at a minimum 44×44px for nav links, buttons, and the mobile burger/search controls referenced in `.mobile-header-search`/`.header__burger`. Mobile navigation is assumed to collapse into a slide-in or accordion panel given the presence of `.mobile-modal-close`, though the actual open/close interaction was not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is generated from static CSS/text extraction only; no live rendering, computed styles, or DOM interaction were observed. Specific gaps:

- Font weights/sizes for `display-md`, `title-md`, `body-md`, and `button-md` are proposed approximations; only `#user-system-header` (64px, weight 400) and a few `.header-banner`/`header .nav` rules provided exact values.
- Component layouts (product-card, hero, footer, search, vehicle-fitment-selector) are inferred from page-text structure and general e-commerce conventions, not from measured selectors/positions.
- Badge colors (`badge-oe`, `badge-best-value`, `badge-choice`, `badge-popular`, `badge-featured`) are confirmed as CSS variables but their exact application/markup was not in evidence.
- Mobile menu, search, and modal interaction behavior (open/close states, transitions) were not observed; only static class names (`.mobile-header-search`, `.header__burger`, `.mobile-modal-close`) were present.
- "Roboto" appears tied to one specific UI element (`.store-wheels-header`); its broader use as a button/label font family is an inferred pattern, not confirmed sitewide.
- Custom/licensed font availability (e.g. "Drop Dead Gorgeous," "Eurostile Bold Extended," "White on Black") was listed in supplied font families but not tied to any specific CSS rule in evidence, so these were excluded from the typography system; licensing and actual usage remain unverified.
- Breakpoint values in the Responsive Behavior table are proposed defaults, not extracted from any `@media` rule in the supplied CSS.
