---
version: alpha
name: "Bobo Choses"
source_url: "https://bobochoses.com"
captured_at: "2026-09-28T09:21:11.058493+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Bobo Choses presents as a Barcelona-rooted kids and family clothing storefront (0–12 years plus a women's line), built on a neutral, high-contrast Shopify foundation rather than a saturated "kids brand" palette. The dominant tones are near-black ink (#181818, #000000) against white and off-white canvases (#ffffff, #f8f8f8), with a single confident accent — a saturated green (#089562, deepening to #00a37e on active states) — reserved for primary commerce actions like add-to-cart. Supporting grays (#404040, #7a7a7a, #e0e0e0, #ebebeb) structure hairlines, muted text, and soft surface fills. A small cluster of warmer, pastel-adjacent hues (#ff673b, #e0342d, #fcebea) appears in the raw palette and is treated here as inferred accent/sale/badge color, since no CSS role was directly observed for them. Typography is exclusively Helvetica Neue with system sans-serif fallback; no display or serif face was found, so heading sizes above the observed 1.4rem/2.2rem body rule are proposed, not measured. Buttons consistently use pill-shaped, large-radius (40px) shapes, which this spec approximates via a full-radius token. The overall interpretation favors a clean, editorial, product-forward retail interface with a single trustworthy green call-to-action color, echoing the site's stated sustainable/organic positioning without over-inventing decoration.

colors:
  primary: "#089562"
  primary-active: "#00a37e"
  ink: "#181818"
  canvas: "#ffffff"
  body: "#404040"
  muted: "#7a7a7a"
  hairline: "#e0e0e0"
  surface-soft: "#f8f8f8"
  surface-card: "#ebebeb"
  on-primary: "#f8f8f8"
  accent-warm: "#ff673b"
  sale: "#e0342d"
  badge-bg: "#fcebea"
  pure-black: "#000000"
typography:
  display-xl: {fontFamily: "Helvetica Neue, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Helvetica Neue, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Helvetica Neue, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Helvetica Neue, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.57, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica Neue, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Helvetica Neue, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "Helvetica Neue, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
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
    padding: "{spacing.sm} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.xl}"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    hoverBackgroundColor: "{colors.primary}"
    activeBackgroundColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    mutedTextColor: "{colors.muted}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.sale}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  age-size-selector:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.primary}"
    selectedBackgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.md}"

## Components
**button-primary** is the dark, pill-shaped default action (observed base `.custom-button` styling: black background, white text, 40px radius), used for general commerce actions like "Shop now."

**button-secondary** mirrors the observed `.custom-button--secondary` outline style: white fill, dark ink border and text, for lower-emphasis actions such as "View collection."

**button-add-to-cart** isolates the directly observed `.custom-button--atc` green treatment, since this is the one component where a distinct accent color (green) was confirmed in the CSS rather than inferred; hover and active states reuse the same or a slightly deeper green per the supplied rules.

**text-input** is proposed for search fields, newsletter signup, and account forms; hairline border and soft placeholder color are inferred from the neutral gray palette, as no explicit input styling was supplied.

**nav-bar** reflects the site's mega-menu structure (Woman/Kid/Baby/Collections navigation implied by page text) on a white background with dark text; exact height, sticky behavior, and transparent-header state (referenced by `.header-menu-bobo-transparent` selectors) are proposed, not measured.

**product-card** is a category-appropriate component for the grid of clothing items; card background uses a light neutral fill, with title and price typography drawn from the type scale. Image aspect ratio and hover interactions were not observed.

**hero** proposes a dark, editorial banner (ink background, light text) consistent with the site's high-contrast palette, appropriate for seasonal drops such as "AW26 All About Monsters."

**footer** uses the soft off-white surface tone with muted body text and hairline dividers, inferred from the general gray/hairline family rather than a directly observed footer block.

**badge** is proposed for sale/new-arrival flags, borrowing the warm coral/red pairing (#fcebea background, #e0342d text) present in the raw palette but not explicitly tied to a badge selector in the supplied CSS.

**search** is inferred as a pill-shaped input consistent with the button radius language, since no dedicated search-field CSS was supplied.

**age-size-selector** is the category-appropriate component for kidswear: an age/size chip selector (e.g., 0–3m, 2–3y, 4–5y) using neutral default states and a green-accented selected state to align with the confirmed primary accent.

## Responsive Behavior
Proposed, not measured — no breakpoint or media-query evidence was supplied.

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | <480px | Single-column product grid, collapsed hamburger nav, full-width buttons |
| Tablet | 480–1024px | 2-column product grid, nav collapses into mega-menu drawer |
| Desktop | >1024px | 3–4 column product grid, full horizontal mega-menu |

Touch targets should be at least 44×44px for buttons and chip selectors. Navigation is expected to collapse into a slide-in or overlay menu below tablet width, consistent with the presence of a `.close-button` overlay pattern in the supplied CSS, though the exact mobile menu behavior was not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived from static CSS and text extraction only; no rendered layout, JavaScript-driven interaction, or real breakpoint behavior was observed. Root font-size (rem base) was not confirmed, so all pixel conversions from `rem` values (e.g., body font-size/line-height) are inferred assuming a common 10px-root convention and should be verified. Only Helvetica Neue was found in font-family declarations; no licensing or brand-proprietary font was verified, and generic sans-serif fallback is assumed. Several palette colors (warm coral, red, blue, pastel accents) appear in the raw color list without a confirmed CSS selector role and have been assigned inferred, conservative roles (badge/sale) rather than primary brand meaning. Component states such as focus rings, disabled buttons, form validation, and mobile menu transitions are proposed patterns only. Product card, hero, and footer layouts are category-appropriate proposals, not confirmed from rendered page structure.
