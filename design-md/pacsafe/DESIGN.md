---
version: alpha
name: "Pacsafe"
source_url: "https://pacsafe.com"
captured_at: "2026-09-28T05:05:00.077947+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Pacsafe's storefront CSS shows a disciplined, security-brand palette built on a
  single deep navy (#1a2651, exposed as --color-pacsafe-blue) against a white
  canvas, with body copy in dark neutrals (#333333/#000000) and a family of light
  grays used for hairlines, muted text, and soft surface fills. Status colors are
  explicit in the stylesheet: a green success state (#059669), a red error/out-of-
  cart state (#dc2626), and a gray disabled state (#6b7280), plus a separate
  brighter red used for sale badging. A muted teal (#4ca7b9) appears in the
  palette and is treated here as an inferred accent for secondary highlights,
  since no selector confirms its usage.

  Typography is dual-track: :root declares Anton as the heading family and
  Roboto as body/body-bold, but the literal h1–h6 rule renders headings in the
  Roboto body-bold family/weight rather than Anton. This spec treats Anton as
  the intended display voice (matching the brand's bold, stenciled travel-gear
  identity) for hero/display roles, and documents the Roboto-driven heading
  fallback as a labeled uncertainty. Buttons use a filled navy pill with a
  4px radius, inverting to white-on-navy on hover, consistent with the observed
  .btn rules.

colors:
  primary: "#1a2651"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#e0e0e0"
  surface-soft: "#f4f4f4"
  surface-card: "#fcfcfd"
  on-primary: "#ffffff"
  accent: "#4ca7b9"
  success: "#059669"
  error: "#dc2626"
  sale: "#ec4048"
  disabled: "#6b7280"
typography:
  display-xl: {fontFamily: "Anton, sans-serif", fontSize: 72px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Anton, sans-serif", fontSize: 52px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Roboto, sans-serif", fontSize: 28px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, sans-serif", fontSize: 16px, fontWeight: 300, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Roboto, sans-serif", fontSize: 14px, fontWeight: 300, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Roboto, sans-serif", fontSize: 12px, fontWeight: 300, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "Roboto, sans-serif", fontSize: 16px, fontWeight: 900, lineHeight: 1, letterSpacing: 0.5px}
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
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.xl}"
    hover: "backgroundColor: {colors.canvas}; textColor: {colors.primary}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.xl}"
    hover: "backgroundColor: {colors.canvas}; textColor: {colors.primary} (proposed, mirrors .btn-outline:hover)"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    focus: "borderColor: {colors.primary} (proposed, not observed)"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xxl}"
  badge:
    sale:
      backgroundColor: "{colors.sale}"
      textColor: "{colors.on-primary}"
      typography: "{typography.caption}"
      rounded: "{rounded.xs}"
    new:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.caption}"
      rounded: "{rounded.xs}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  feature-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    iconColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** reflects the observed `.btn` rule: solid navy fill, white text, 1px navy border, 4px radius, inverting to a white/navy outline on hover — this hover swap is explicitly present in the CSS.

**button-secondary** models the `.btn-outline` variant (transparent fill, white border/text) used against dark hero/footer backgrounds; its hover state is inferred by symmetry with the primary button's hover rule.

**text-input** is proposed from the global `--style-border-radius-inputs: 4px` token; border color, padding, and focus ring are not directly observed and are treated as conventional defaults for a Shopify-style form field.

**nav-bar** is inferred from the presence of header/language-switcher selectors and typical Shopify header structure (logo, mega-menu categories, cart, search); exact height, sticky behavior, and mega-menu layout are not confirmed in the evidence.

**product-card** is proposed from product-grid context (columns-desktop: 4 seen in a section's custom properties) combined with the "Quick Add," review-count, and price text patterns in the page excerpt; visual card chrome (shadow, border) is not directly evidenced beyond the generic hairline gray.

**hero** is proposed from the homepage banner copy ("EXPLORE THE CITY WITH CONFIDENCE," "Shop Now") and uses the navy/white pairing consistent with the button and badge rules; exact hero height and image treatment are not observed.

**footer** is inferred from the sitemap-style link list (About Us, Help Center, legal links) in the excerpt; the navy-on-white vs. white-on-navy treatment is a proposed brand-consistent choice, not a captured footer background rule.

**badge** directly reflects two observed rules: `.product-badges__badge--sale` and `--new`, using the pacsafe-sale and pacsafe-blue background variables respectively.

**search** and **feature-tag** are proposed: search styling follows generic Shopify overlay patterns referenced by the "Search" nav item; feature-tag is a category-appropriate component representing the site's repeated anti-theft callouts (lockable zippers, cut-resistant material, RFID blocking) seen in the announcement bar copy, useful for passport-holder/RFID PDP iconography.

## Responsive Behavior

This is a recommendation based on the `--page-margin*` tokens (80px desktop / 40px tablet / 20px mobile) and a 1920px max page width — not measured breakpoint behavior.

| Breakpoint | Width       | Page margin | Nav pattern (proposed) |
|------------|-------------|-------------|-------------------------|
| Mobile     | < 768px     | 20px        | Hamburger + slide-in menu |
| Tablet     | 768–1199px  | 40px        | Condensed horizontal nav, mega-menu collapses to accordions |
| Desktop    | 1200–1919px | 80px        | Full mega-menu, 4-column product grid |
| Wide       | ≥ 1920px    | 80px (capped content width) | Centered container at max-width |

Touch targets should be at least 44×44px for cart, search, and nav icons; the mobile menu should collapse categories (Shop, Women's, Collections, Explore) into expandable accordions given the depth of the observed navigation tree.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This spec is derived from static CSS/text extraction only; no rendered page, computed styles, or interaction states were observed. The heading font is ambiguous: `:root` declares Anton for `--font-heading--family`, but the literal `h1–h6` selector applies the Roboto body-bold family/weight instead — which family governs actual heading elements site-wide is unverified. Several palette entries (`#83cc1c`, `#43a1fa`, `#43a1fa`-adjacent tones, `#535565`, `#9a9db1`) are present in the evidence but have no attached selector and were excluded from role assignment. Body, caption, and input font sizes are proposed (not present in the evidence) apart from the h1–h4 rem values, which are directly observed. Hover/focus states beyond the documented `.btn` and `.help-center-box` rules are inferred by pattern-matching, not confirmed. Mobile menu structure, sticky header behavior, and product-grid card chrome are not observed and are proposed for usability only. Font licensing/availability for Anton and Roboto as served by Pacsafe was not verified.
