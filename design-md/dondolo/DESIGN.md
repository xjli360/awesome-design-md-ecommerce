---
version: alpha
name: "Dondolo"
source_url: "https://dondolo.com"
captured_at: "2026-09-29T04:21:43.666631+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Dondolo presents handcrafted, hand-smocked childrenswear and womenswear through a
  gentle, heritage-inflected palette. The dominant accent is a dusty rose (#db918a),
  used consistently as link-button background and hover states across multiple
  content blocks, paired with a muted blue-gray (#65738c) as an alternate button
  treatment — together these read as the brand's two primary accent colors, both
  observed directly in component CSS. A warm taupe (#938c70) is used specifically
  for serif section headings (crosssell-title, sec-ttl) set in the "monarcha" serif
  typeface, giving collection titles an artisanal, storybook quality distinct from
  the plain Arial used for body copy and form controls. Body and price text default
  to a soft charcoal (#444444) rather than pure black, softening the overall
  contrast. Neutral grays (#eeeeee, #f5f5f5, #dddddd, #e7e7e7) are inferred as
  surface and hairline roles for cards, dividers, and section backgrounds, since no
  explicit surface/border declarations were supplied. A cluster of red tones
  (#d20000, #f04343, #e34848) is present in the palette and is inferred here as a
  sale/badge accent, consistent with the "Sale" and "LAST CALL" navigation labels,
  though no badge component CSS was observed. Typography roles beyond monarcha,
  Lato, and Arial (e.g. Baskerville, Branch, Poppins, Montserrat) appear only in the
  raw font list without confirmed selector usage and are treated as unverified.

colors:
  primary: "#db918a"
  secondary: "#65738c"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#444444"
  muted: "#938c70"
  hairline: "#e7e7e7"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border-light: "#dddddd"
  accent-soft: "#f7cac6"
  accent-deep: "#9d5955"
  sale: "#d20000"
typography:
  display-xl: {fontFamily: "monarcha, serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "monarcha, serif", fontSize: 30px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "monarcha, serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Lato, Arial, Tahoma, Verdana, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Lato, Arial, Tahoma, Verdana, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.3px}
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
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.secondary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.border-light}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    priceColor: "{colors.body}"
  collection-tile:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.muted}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"

## Components

**button-primary** uses the dusty-rose `{colors.primary}` background observed directly on `.image-block-text-wrap-image_RqphR6/XnJXcd` link-buttons, with white text as a proposed contrast pairing (on-primary color is inferred, not stated in the supplied hover/link CSS).

**button-secondary** reuses the blue-gray `{colors.secondary}` seen on the `_FdLndx`/`_TJXCbq`/`_mFDG3g` button blocks, which share the same rose hover state as the primary buttons — this secondary/primary hover convergence is observed and preserved here.

**text-input** is a proposed pattern for login/newsletter/search fields; no input-specific CSS was supplied, so border, radius, and padding are inferred defaults consistent with the site's soft, low-contrast neutrals.

**nav-bar** reflects the large mega-menu structure evident in the page text (Girls/Boys/Women/Accessories/Collections), styled with body-sm Arial text on a white canvas; exact height, sticky behavior, and active-state styling are not observed.

**product-card** models the "Goldie Girl Dress," "Louise Girl Bubble," etc. listings, pairing a body-md product title with a body-sm price in `{colors.body}` (#444444), matching the observed `.xs-price` color declaration.

**collection-tile** is category-appropriate for seasonal drops (Fall Heritage, Apples to Apples, Secret Garden) and reuses the observed monarcha display-md heading style and muted taupe title color from `.crosssell-title`/`.sec-ttl h3`.

**hero** is a proposed full-width banner for launch messaging ("Just Launched: Fall Heritage Collection"), using display-xl monarcha type at a larger, unobserved size extrapolated from the confirmed 30px section-title pattern.

**footer** is a proposed dark-ink footer for legal/donation/currency links (the page lists an extensive currency selector and "Colombia Donations" link), styled with inverse text; no footer CSS was supplied.

**badge** covers "Sale," "Last Call," and "Final Favorites" labels visible in navigation text; the red hue is inferred from the palette's red cluster since no badge selector was captured.

**search** is a proposed pill-shaped input for site search/wishlist lookup; fully inferred, no search-bar CSS observed.

## Responsive Behavior
Recommended (not measured) breakpoints:

| Breakpoint | Width | Nav behavior | Grid |
|---|---|---|---|
| mobile | <600px | Hamburger + slide-out mega-menu | 1–2 col product grid |
| tablet | 600–1024px | Condensed top nav, dropdowns | 2–3 col |
| desktop | >1024px | Full mega-menu with category flyouts | 3–4 col |

Touch targets should be at least 44px for nav, cart, and wishlist icons. Mega-menu categories (Girls/Boys/Women/Accessories) should collapse into accordions below tablet width. None of this is observed site behavior — it is a proposed responsive strategy based on the mega-menu content structure implied by the page text.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, breakpoints, hover/focus states beyond the explicit link-button rules, or JavaScript-driven interactions (flickity carousel, wishlist, cross-sell quickview) were observed in motion. Semantic color roles (ink, canvas, surface-soft/card, hairline, badge/sale) are inferred from a flat palette list and reused where plausible; several neutrals (#eeeeee, #f5f5f5, #f9f9f9, #dddddd, #e7e7e7) are visually similar and their exact component assignment is uncertain. Typography sizes outside the two confirmed values (24px, 30px) are proposed. Fonts such as Baskerville, Branch, Petit Formal Script, Poppins, Montserrat, and canada-type-gibson appear in the raw font list but have no confirmed selector binding in the supplied CSS and are excluded from typography tokens. Custom/licensed font availability (monarcha, eldwin-script, adorn-icons) is not verified for production use. Mobile menu, cart drawer, and checkout flows were not observed.
