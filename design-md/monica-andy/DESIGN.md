---
version: alpha
name: "Monica + Andy"
source_url: "https://monicaandandy.com"
captured_at: "2026-09-28T09:20:51.849974+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  The evidence shows a warm, muted neutral system anchored by ash (#414042) and near-black
  ink (#292425), set against snow-white and soft slate/oat backgrounds. A wide accent set of
  pastel "nursery" tones (beige, sun, carrot, sky, ocean, pine, grape, rose) appears in the
  CSS custom-property block, consistent with a baby/kids apparel catalog using color-coded
  collections rather than a single brand accent. Two red tones (#be5343, #e24b52) likely serve
  sale/alert roles, inferred from typical retail patterns, not confirmed by markup context.
  Typography is dual-track: Akkurat LL Web/Sub are explicitly assigned to body-display and
  body-ui classes and are treated here as the verified interface and body font. Additional
  family names (new-spirit, ivybodoni, cofo-raffine, rafaella, schoolbook) appear in the font
  list without confirmed selector bindings; they are used here only for proposed editorial
  display headings, labeled inferred. Buttons are flat, uppercase-capable, with a 42px height,
  2px borders on secondary/outline variants, and a 0.3s ease transition observed directly in
  CSS. Corner radii are not evidenced in the supplied rules, so a conservative, mostly-square
  system with small radii is proposed for cards and inputs.

colors:
  primary: "#414042"
  ink: "#292425"
  canvas: "#ffffff"
  body: "#414042"
  muted: "#6b665f"
  hairline: "#c6c7c8"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-beige: "#ffe6cb"
  accent-sun: "#ffe293"
  accent-carrot: "#f9a980"
  accent-sky: "#94bde5"
  accent-ocean: "#6dacde"
  accent-pine: "#67c18c"
  accent-grape: "#a7a0cb"
  accent-rose: "#f69679"
  sale: "#be5343"
  alert: "#e24b52"
  slate: "#e6e7e8"
  oat: "#d8c6b8"
typography:
  display-xl: {fontFamily: "new-spirit, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "new-spirit, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Akkurat LL Web, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Akkurat LL Web, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Akkurat LL Sub, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Akkurat LL Sub, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Akkurat LL Web, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.32px}
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
    padding: "{spacing.none} {spacing.base}"
    height: "42px"
    note: "Observed as .button-atc/.button-primary: ash background, white text, 42px height, 0.2s ease transition."
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.none} {spacing.base}"
    height: "42px"
    note: "Observed as .button-secondary with matching height/typography to primary, inverse fill."
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    focusRing: "1px solid {colors.canvas}, 4px solid {colors.ink}"
    note: "Focus ring derived from observed :focus-visible box-shadow stack (white inner, dark outer)."
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    height: "120px"
    typography: "{typography.body-sm}"
    note: "120px height taken directly from --header-height. Multi-tier mega-menu structure inferred from extensive category text, not from measured DOM."
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    saleColor: "{colors.sale}"
    note: "Proposed structure: image, title, price, optional sale badge; layout not confirmed by evidence."
  hero:
    backgroundColor: "{colors.accent-beige}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section}"
    note: "Promotional banners ('40% Off Sitewide', 'Fall Styles') suggest a rotating hero; color and layout are proposed."
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    note: "Footer content (contact, help links) inferred from nav text; visual treatment proposed."
  badge:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
    note: "Sale/New badges proposed using observed red tones; no direct badge selector in evidence."
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-md}"
    note: "Custom clear-button hiding rule (::-webkit-search-cancel-button) confirms a styled search input exists; full layout proposed."
  personalization-tag:
    backgroundColor: "{colors.accent-sky}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
    typography: "{typography.caption}"
    note: "Represents the 'Personalize It' embroidery feature repeated across nav; visual treatment proposed, category-specific to this brand's monogram offering."

## Components
**button-primary** and **button-secondary** are drawn directly from `.button-atc`/`.button-primary` and `.button-secondary` rules: 42px height, flat fill or 2px outline in ash, uppercase-capable label, 0.2–0.3s ease transitions. These anchor primary actions like "Add to Cart" and secondary actions like "View Details."

**text-input** infers a standard bordered field using the hairline gray (#c6c7c8) seen on `.button-registry`, paired with the confirmed focus-visible ring (white inset, dark outer) applied globally to interactive elements.

**nav-bar** uses the one hard measurement in the evidence, `--header-height:120px`, and reflects the deeply nested category taxonomy (Baby, Toddler + Kids, Mom + Family, Gear/Nursery/Toys) visible in the page text, implying a mega-menu; exact visual arrangement is not observed.

**product-card** is a proposed pattern typical of apparel grids, using the confirmed hairline border and surface-card white, with a sale-price treatment in the observed red (#be5343) for markdown states.

**hero** proposes a warm beige backdrop (#ffe6cb) to host rotating sitewide promotions ("40% Off Sitewide", "Fall Styles, Thoughtfully Made") referenced in the page text, paired with a serif display headline as an inferred editorial treatment.

**footer** is proposed as a light, low-contrast block carrying contact/help content (phone, email, live chat) mentioned in the text excerpt; no footer-specific CSS was supplied.

**badge** and **personalization-tag** are the two category-specific components: badge covers sale/new flags using the observed alert red, while personalization-tag reflects the recurring "Personalize It" embroidery feature, a distinguishing service of this brand, styled with a soft pastel pill as a proposed convention.

**search** confirms only that a custom search input exists (native cancel-button suppressed via `::-webkit-search-cancel-button`); its container styling is otherwise proposed to match the neutral surface system.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Nav | Grid |
|---|---|---|---|
| mobile | <640px | collapsed hamburger, header height reduced from 120px | 1–2 col product grid |
| tablet | 640–1024px | condensed mega-menu | 2–3 col grid |
| desktop | >1024px | full 120px mega-menu | 3–4 col grid |

Touch targets should meet a 44px minimum; the observed 42px button height is close but should be padded on touch devices. Mega-menu collapse into an accordion/drawer pattern below 1024px is proposed given the taxonomy depth in the evidence, not confirmed by any responsive CSS supplied.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from static CSS custom properties, isolated selector rules, and page text only; no rendered layout, computed styles, or interaction states (hover/open menu/cart drawer) were observed. Corner radius values are not evidenced anywhere in the supplied CSS and are therefore fully proposed defaults. Display typography (new-spirit, ivybodoni, cofo-raffine, rafaella) is listed in the font-family evidence but its selector bindings, weights, and actual usage context are unknown — role assignment to headings is inferred, not confirmed. Letter-spacing on caption/button tokens is estimated from a single `.02em` rule applied at 16px and may not generalize. Mobile menu structure, breakpoint values, and grid column counts are proposed conventions, not measured. Font licensing/availability for Akkurat LL Web/Sub and any display serif is not verified; fallback to system sans-serif/serif is assumed. Color-to-role mapping (e.g., which pastel maps to which product category) is inferred from typical nursery-retail conventions, not from confirmed component-level CSS.
