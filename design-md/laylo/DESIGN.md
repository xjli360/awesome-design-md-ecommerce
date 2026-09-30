---
version: alpha
name: "Laylo"
source_url: "https://www.laylopets.com/"
captured_at: "2026-09-29T03:58:47.956565+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  LAY LO Pets sells design-forward dog beds, blankets, and pet furniture through a Shopify storefront that reads as editorial and gallery-like rather than utilitarian. The observed palette is dominated by true black (#000000) and white (#ffffff), with charcoal and slate grays (#333333, #202223, #757575) carrying body copy, and a warm amber/gold (#f1b74e) appearing as the review-star and "write a review" accent — inferred here as the brand's single warm highlight color against an otherwise neutral system. A muted navy (#1f294f) appears in root-level CSS and is treated as a secondary structural color for footers or dark sections, though its exact live usage is not confirmed from static extraction. Typography evidence shows a serif family (Big Caslon, Fraunces) alongside sans families (DM Sans, DIN Neuzeit Grotesk, p22-underground), suggesting an editorial pairing: serif for large display moments (collection names, hero copy) and sans for navigation, body text, and buttons, consistent with the letter-spaced, uppercase-leaning button styles observed in calendar and add-to-cart controls. Layout, spacing, and rounding values below are proposed conventions for a premium pet-lifestyle catalog and are not measured from live rendering.

colors:
  primary: "#000000"
  ink: "#202223"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#757575"
  hairline: "#dcdcdc"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#f1b74e"
  accent-navy: "#1f294f"
  sale-highlight: "#d02e2e"
  link: "#4a90e2"
typography:
  display-xl: {fontFamily: "'Big Caslon', 'Fraunces', serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Big Caslon', 'Fraunces', serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'DM Sans', 'p22-underground', sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'DM Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'DM Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'DM Sans', sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.05em}
  button-md: {fontFamily: "'DIN Neuzeit Grotesk', 'p22-underground', sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.1em}
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    saleTextColor: "{colors.sale-highlight}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale-highlight}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  expert-consult-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    nameTypography: "{typography.title-md}"
    credentialTypography: "{typography.caption}"
    accentColor: "{colors.accent-gold}"

## Components

**button-primary** renders as a solid black pill/rectangle with white uppercase, letter-spaced text, matching the observed `.eab-atc-button` and accelerated-checkout button patterns (black background, white text, rounded corners near 4–5px). Used for "Shop Now," "Book a Session," and add-to-cart actions.

**button-secondary** is an outlined variant on white, reserving solid black for primary calls-to-action — proposed for "Shop All" or "View Collection" links where a lighter visual weight is wanted alongside a primary button.

**text-input** is a minimal bordered field using the hairline gray border color, intended for newsletter subscribe and account/search forms; no live focus-state styling was observed, so focus treatment is proposed only.

**nav-bar** is a white, black-text horizontal bar (Beds / Accessories / Gift Guide / Our Services / About) with a hairline bottom border; sticky/collapsing behavior referenced by the `--header-height` custom property is inferred but not visually confirmed.

**product-card** presents a product image, title in the serif/sans title style, price, and an optional strikethrough-plus-sale-price pattern (seen in "Save 44%" copy), with the sale badge in the red highlight color pulled from the `--highlight` custom property.

**hero** is a full-width, soft-neutral background section pairing a large serif headline ("Beauty meets comfort") with a single primary button — proposed spacing and centering, not measured.

**footer** uses the darker navy tone as an inferred background for contact info, company links, and newsletter signup, with white text for contrast; this mapping treats `#1f294f` as a section color rather than a confirmed brand-navy identity.

**badge** is a small solid-red label for sale/discount callouts, matching the `--highlight: #d02e2e` root variable found in the CSS evidence.

**search** is a rounded, pill-shaped input intended for the "Open search bar" trigger noted in the page text; exact shape and placement are proposed conventions for this pattern, not observed.

**expert-consult-card** is a category-specific component for the "Meet some of our experts" section — a card listing an expert's name, role, and certifications, with the gold star/accent color used sparingly to echo the review-star color already present in the CSS variables.

## Responsive Behavior

This is a recommended, non-measured breakpoint scheme for a catalog + editorial content site of this type:

| Breakpoint | Width       | Nav                          | Product Grid |
|-----------|-------------|-------------------------------|--------------|
| mobile    | <600px      | collapses to hamburger/drawer | 1 column     |
| tablet    | 600–1024px  | condensed inline nav          | 2 columns    |
| desktop   | 1024–1440px | full inline nav               | 3 columns    |
| wide      | >1440px     | full inline nav, wider gutters| 4 columns    |

Touch targets for buttons and nav items should maintain a minimum 44px height, consistent with the `min-height: 45px` value observed on the calendar popup button. Filter/search UI and the primary nav are expected to collapse into a drawer or sheet below the tablet breakpoint. All of the above is a proposed responsive strategy, not behavior observed from live rendering.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is generated from static CSS/text extraction only; no live browser rendering, computed layout, hover/focus states, or JavaScript-driven interactions (cart drawer, quick-buy modal, search overlay) were observed. Color-to-role mapping (e.g., navy as footer background, gold as accent) is inferred from variable names and isolated selector context, not confirmed against rendered screenshots. Typography sizes, weights, and line-heights are proposed based on category conventions since no explicit `font-size`/`line-height` values for headline or body text were present in the supplied CSS rules. Spacing and rounding scales are conventional proposals, not extracted measurements. Availability and licensing of "Big Caslon," "Fraunces," "DIN Neuzeit Grotesk," and "p22-underground" for reuse have not been verified; fallback generic families are included for safety. Mobile navigation and drawer behavior, breakpoint values, and grid column counts are recommendations only and were not observed in the supplied evidence.
