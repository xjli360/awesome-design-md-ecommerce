---
version: alpha
name: "Micro Kickboard"
source_url: "https://microkickboard.com"
captured_at: "2026-09-28T10:16:19.928097+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Micro Kickboard's storefront evidence points to a clean, high-contrast commerce layout built on a Shopify theme with a third-party review widget (Oke) supplying explicit design tokens. The dominant brand color is a saturated indigo-blue (#3235c0), confirmed as the review widget's active button and background color and reused in on-page heading accents (`color:#3235c0` rules tied to hero heading blocks). A warm coral-red (#de5757) appears as a custom badge/highlight color, likely for sale tags or promotional callouts. Neutral text and surface colors range from near-black (#000000, #090a0a) through mid grays (#676986, #333333) to soft off-whites (#f6f4f2, #fafafa, #f7f7f7), suggesting a light canvas with layered card surfaces rather than a single flat background — this layering is inferred, not directly measured.

  Font evidence includes DM Sans, Work Sans, and IBM Plex Sans as sans-serif system candidates, plus a distinctive custom pairing (SpektraTekst / DOTSpektraTekst-Bold) that likely drives playful, kid-brand headline treatment, and Pacifico as a possible script accent. Border-radius is grounded at 4px from the review widget's `--oke-button-borderRadius` token. This interpretation proposes a friendly, rounded, scooter-brand system: bold indigo CTAs, soft neutral surfaces, and a dotted/rounded display face for age-group and product headings, with all sizing and spacing values marked as proposed unless a literal CSS value was observed.

colors:
  primary: "#3235c0"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#676986"
  hairline: "#e5e5eb"
  surface-soft: "#f6f4f2"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent: "#de5757"
  sale: "#d02e2e"
  success: "#56ad6a"
  info: "#7cc7fd"
  warn: "#ecbd5e"
  border-strong: "#dbdde4"
typography:
  display-xl: {fontFamily: "SpektraTekst, DOTSpektraTekst-Bold, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "SpektraTekst, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "DM Sans, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Work Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Work Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "IBM Plex Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "DM Sans, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.2px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    height: "76px"
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
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
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
  age-range-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    activeBorderColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the confirmed review-widget indigo (#3235c0) with white text and a 4px radius — the one border-radius value directly present in the supplied CSS (`--oke-button-borderRadius:4px`). Hover/active states in the evidence swap to `#3e41c4` (hover) and keep `#3235c0` (active); these are proposed for the storefront's own buttons by analogy, not confirmed outside the review widget.

**button-secondary** is a proposed outline variant using primary-on-transparent, intended for lower-emphasis actions like "Learn More" or "Compare Models" — no direct CSS evidence for this variant exists; it is a conventional pairing.

**text-input** and **search** share a light hairline border (#e5e5eb) and soft canvas background, inferred from the neutral gray palette and the site's visible search-bar affordance ("Open search bar / Search for products"). Focus-ring styling is not observed and is proposed as a primary-color outline.

**nav-bar** is anchored to the one measured layout value in evidence: `--header-height: 76px` and `--header-sticky-height: 60px`. Background and text colors are inferred as white-on-black-text given the neutral palette; actual sticky-state styling was not captured.

**product-card** proposes a soft off-white/near-white card (#fafafa) with hairline borders to separate scooter listings (e.g., "Micro Mini Foldable LED Scooter", color-variant swatches) seen in the page text. Title and price typography map to title-md and body-md; swatch layout and hover states are not observed.

**hero** uses the soft canvas tone (#f6f4f2) as an inferred background for banner sections like "There's a Micro For Everyone," paired with the large display face. The `--adjust-heading` and `padding-top` percentage rules in evidence confirm a responsive/aspect-ratio-driven hero image treatment, though exact crop ratios are not fully resolved from the snippets provided.

**footer** is proposed as a dark, ink-colored band for contrast against the light body, consistent with common ecommerce footer patterns; no footer-specific CSS was present in the evidence.

**badge** maps directly to the observed `--custom-badge-bg-color: #de5757` / `--custom-badge-text-color: #fff` tokens, appropriate for "New," "Sale," or age-range tags (e.g., "Ages 1-2," "Ages 5-12") visible in the shop-by-age navigation.

**age-range-selector** is a category-appropriate component proposed for the "Shop By Age" navigation pattern (Babies & Toddlers, Little Kids, Big Kids, Teens & Adults) repeatedly referenced in the page text. It uses a card treatment with a primary-colored active border to indicate the selected age tier; no visual specification for this pattern was present in the supplied CSS, so styling is fully proposed.

## Responsive Behavior

This is a recommendation based on common ecommerce patterns, not measured site behavior:

| Breakpoint | Range | Nav | Product Grid |
|---|---|---|---|
| mobile | 0–639px | Collapsed hamburger, header height ~60px (sticky value observed) | 1–2 columns |
| tablet | 640–1023px | Condensed horizontal nav | 2–3 columns |
| desktop | 1024px+ | Full nav with "Shop By Age" mega-menu | 3–4 columns |

Touch targets for buttons and age-filter cards should target a minimum of 44×44px. The header's `--header-sticky-height:60px` token suggests a shrink-on-scroll behavior, but the actual collapse/scroll interaction was not observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS custom-property snippets, a page-text excerpt, and a supplied color/font list — no live rendering, computed layout, or interaction testing was performed. The `--oke-*` tokens originate from the third-party Oke reviews widget and were extended by analogy to storefront-wide buttons and badges; this mapping is inferred, not confirmed for native theme components. Most spacing, breakpoint, and card-radius values are proposed defaults rather than measured pixels, with the exception of `--header-height:76px`, `--header-sticky-height:60px`, and the 4px button radius, which are directly sourced. Font role assignments (display vs. body vs. caption) are inferred from typical usage patterns of the named families; actual font-weight availability, custom font licensing (particularly SpektraTekst/DOTSpektraTekst-Bold and Pacifico), and web-font loading were not verified. Mobile menu behavior, hover/focus states beyond the Oke button tokens, and product-card swatch interactions were not observed and are marked proposed throughout.
