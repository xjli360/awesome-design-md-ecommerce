---
version: alpha
name: "Kickee Pants"
source_url: "https://kickeepants.com"
captured_at: "2026-09-29T04:12:33.786094+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  KicKee Pants presents itself through a Shopify-based storefront selling baby,
  kids, youth, women's, men's and home sleepwear/apparel. The supplied CSS
  exposes a Bootstrap-derived variable system (--bs-font-family-base,
  --bs-font-family-heading, --bs-color-black) rather than hardcoded brand
  hexes, so most role assignments here are inferred from the small set of
  literal colors present: neutral grays (#333333, #686868, #e5e5e5, #f3f3f3)
  for text and surfaces, a mid blue pair (#005eac/#1990c6) that reads as the
  interactive/link/CTA color, a soft sky blue (#74cee2) and a yellow-green
  (#d5e041) as playful secondary accents fitting a baby-brand tone, and
  standard Bootstrap alert triads (success green, danger red) for system
  feedback. Two observed font-family tokens, "Nunito Sans" and "Open Sans",
  are mapped here as heading and body respectively — this pairing is inferred
  from common heading/base variable separation, not confirmed per-element.
  Buttons are uppercase with a 6px border-radius per .btn/input rules,
  approximated to the nearest token in this scale. Icon fonts ("kickee",
  "icon-fluid", swiper-icons) are noted as UI iconography, not text
  typography. Layout structure (grid, breakpoints, card composition) is not
  present in the evidence and is proposed only, suited to a friendly,
  soft-goods children's apparel retailer.

colors:
  primary: "#005eac"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#686868"
  hairline: "#e5e5e5"
  surface-soft: "#f3f3f3"
  surface-card: "#ebebeb"
  on-primary: "#ffffff"
  accent-sky: "#74cee2"
  accent-lime: "#d5e041"
  info: "#1990c6"
  info-dark: "#136f99"
  success: "#198754"
  danger: "#dc3545"
  border-input: "#cccccc"
  disabled: "#bcbcbc"
typography:
  display-xl: {fontFamily: "'Nunito Sans', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Nunito Sans', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "'Nunito Sans', sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Nunito Sans', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.border-input}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-input}"
    selectedBorderColor: "{colors.primary}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"

## Components

**button-primary** — Maps to the `.btn` rule set observed (uppercase text-transform, dedicated button font/size/weight/letter-spacing variables, 6px radius approximated here to `{rounded.sm}`). Assigned `{colors.primary}` as the fill since no literal brand accent hex was present; hover/active/disabled states are proposed, not observed.

**button-secondary** — An outline variant inferred from `.btn-link`'s underline-based secondary treatment, reworked as a bordered button for a category page needing add-to-cart plus secondary actions (e.g., "Add to Wishlist"). Fully proposed styling.

**text-input** — Derived from the generic `button,input{margin:0;font-family:inherit}` reset and the shared `--bs-border-radius-input:6px` token. Focus, error, and success ring states are proposed and not present in the supplied CSS.

**nav-bar** — Built from the extensive mega-menu text content (Babies/Kids/Youth/Women/Men/Home & Gifts) implying a multi-level dropdown navigation; visual treatment (background, hairline) is inferred from the neutral palette since no header-specific selector was supplied.

**product-card** — Proposed pattern for grid display of SKUs across the many listed subcategories (sleepwear, underwear, outfit sets). Card surface uses `{colors.surface-card}` to sit slightly off-white against a white canvas; no card CSS was directly observed.

**hero** — Proposed landing/banner treatment for "NEW ARRIVALS" and seasonal collection promotion (Halloween, Christmas, etc.), using `{typography.display-xl}` for a large title on a soft background tint.

**footer** — Proposed structural footer for the deep catalog/utility links (Gift Certificates, Sign In, My Orders); typography and color inferred from body-text neutrals, not confirmed by supplied footer-specific CSS.

**badge** — Uses the lime-green accent `{colors.accent-lime}` for promotional or "New" labels, a plausible playful accent for a baby-apparel brand; the exact application (sale tag vs. new-arrival flag) is proposed.

**search** — Proposed search-input styling matching the general input pattern; no dedicated search-bar CSS was present in the evidence.

**size-selector** — A category-appropriate component for baby/kids apparel sizing (e.g., 2T–8, 8–16 Years groupings referenced in the deals navigation). Selected-state border uses `{colors.primary}`; all interaction states are proposed.

## Responsive Behavior

This is a recommendation only; no responsive/media-query behavior or breakpoint values were present in the supplied evidence.

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| xs | <576px | Single-column nav collapses to hamburger/drawer; mega-menu becomes accordion |
| sm | 576–767px | 2-column product grid |
| md | 768–991px | 3-column product grid; nav shows top-level categories |
| lg | 992–1199px | Full mega-menu on hover/click; 4-column grid |
| xl | ≥1200px | Max-width content container; hero at full display-xl scale |

Touch targets should be at least 44px per side for buttons and nav items (consistent with the `--swiper-navigation-size:44px` value observed for carousel controls). Mobile nav collapse behavior is proposed, not measured.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS/HTML extraction only; no rendered layout, JavaScript-driven interactions, or actual breakpoints were observed.
- Core brand colors (primary blue, accent lime/sky) were inferred by process of elimination from a shared Bootstrap-style palette rather than confirmed brand tokens; actual usage context (logo, CTA, link) is unverified.
- `--bs-body-color`, `--bs-color-black`, and other CSS custom properties referenced in rules had no literal hex resolution supplied, so `ink` and `body` role assignments are inferred defaults.
- Font-family role split (Nunito Sans = heading, Open Sans = body) is inferred from variable naming convention, not confirmed per-selector.
- Button/input border-radius (6px, from `--bs-border-radius-button`/`-input`) was approximated to the nearest defined token (`{rounded.sm}` = 4px); exact value not preserved.
- All component states (hover, focus, active, disabled, loading) beyond the single observed `.shopify-payment-button` hover rule are proposed, not observed.
- Custom/icon font availability ("kickee", "icon-fluid") and any licensing terms were not verified.
- Mobile menu, cart drawer, and search interaction patterns are proposed only; no corresponding interactive CSS or markup was supplied.
