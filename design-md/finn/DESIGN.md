---
version: alpha
name: "Finn"
source_url: "https://petfinn.com/"
captured_at: "2026-09-29T04:15:20.251180+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Finn's public storefront (petfinn.com) presents a vet-formulated dog supplement line through a playful, trust-forward visual system. The dominant brand color is a deep indigo-navy (#161345), used consistently across large display headlines, review-widget theming (Junip primary/button color), and button text — establishing it as the core identity color. A warm orange (#ff7f00) appears specifically as the star-rating accent, suggesting a secondary highlight role rather than a primary CTA color. Large-scale headline type uses "Athletics-Medium," a distinctive rounded display face rendered at very large sizes (133px observed) for section titles like "The Finn Formula" and "Loved by Pets, Endorsed by Vets" — this is treated as the brand's signature display font. Buttons and UI labels use "Larsseit-Regular"/"Larsseit-Medium," a clean geometric sans. Body copy font is not directly confirmed in the CSS evidence; Montserrat and Helvetica Neue are present in the font stack and are used here as the inferred body typeface, with generic sans-serif fallback. Neutral surfaces (#f9f9f9, #f7f7f7, #ffffff) and soft hairlines (#e2e8f0, #dedede) support a light, airy product-card layout, consistent with the observed 20px-radius product image containers.

colors:
  primary: "#161345"
  ink: "#1a202c"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#637381"
  hairline: "#e2e8f0"
  surface-soft: "#f9f9f9"
  surface-card: "#f7f7f7"
  on-primary: "#ffffff"
  accent: "#ff7f00"
  success: "#56ad6a"
  danger: "#d02e2e"
  danger-surface: "#fff6f6"
  info: "#1773b0"
  border: "#dedede"
typography:
  display-xl: {fontFamily: "'Athletics-Medium', sans-serif", fontSize: "133px", fontWeight: 400, lineHeight: 1, letterSpacing: "0px"}
  display-md: {fontFamily: "'Athletics-Medium', sans-serif", fontSize: "64px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "0px"}
  title-md: {fontFamily: "'Larsseit-Medium', sans-serif", fontSize: "28px", fontWeight: 500, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "'Montserrat', 'Helvetica Neue', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Montserrat', 'Helvetica Neue', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'Montserrat', 'Helvetica Neue', sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "'Larsseit-Regular', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.42, letterSpacing: "0px"}
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
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    descriptionTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
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
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  quiz-cta-panel:
    backgroundColor: "{colors.surface-card}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"

## Components

**button-primary** renders the indigo brand color as a solid fill with white text, matching the observed `--junipButtonColor` and `.solid-button` text-color pairing; used for primary actions like "Shop Now" and "Take Quiz."

**button-secondary** is a transparent/outline treatment using the same indigo as text and border, mirroring the `.transparent-button` class (color `#161345`, no fill) seen on hero and section CTAs.

**text-input** is a proposed pattern for email capture ("Join the pack") and account/login fields; border and padding are inferred defaults since no dedicated input CSS was supplied.

**nav-bar** is inferred from the page's listed navigation items (Shop, Take Quiz, Log In, Cart); a light canvas background with hairline underline is proposed, as no header CSS block was captured.

**product-card** reflects the observed `.product-card-image` styling directly: light gray background (`#f9f9f9`), generous padding, and a pronounced border radius, used for the six-supplement grid (Allergy & Itch, Calming Aid, etc.).

**hero** is a proposed full-width banner pattern using the large `Athletics-Medium` display type observed in `.finn-way-module-header-title` and similar headline classes, paired with a primary CTA button.

**footer** is inferred as a dark, ink-toned band containing sitemap links (Home, Shop, About, Quiz, Blog, FAQs) and the email signup form; color inversion is proposed, not directly observed in supplied CSS.

**badge** uses the accent orange (`#ff7f00`), matching the observed `--junipStarColor`, proposed here as a small pill for labels like "NASC Certified" or bundle savings callouts.

**search** is a proposed rounded input pattern for a product search affordance; no search-specific CSS was present in the evidence, so styling follows the general card/surface tokens.

**quiz-cta-panel** is a category-specific component representing the "Fetch the Right Solution" quiz module — a card-style panel prompting personalized supplement recommendations, styled with the soft surface and primary CTA button.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <600px | Single-column product grid; hero display type steps down from `display-xl` to `display-md` scale; nav collapses to a hamburger menu (proposed). |
| tablet | 600–1024px | Two-column product/bundle grid; quiz CTA panel remains full-width. |
| desktop | >1024px | Multi-column grid (3–4 cards); large `display-xl` headlines as observed at 133px, capped by a max content width (1440px, per `.get-started-content-header-title`). |

Touch targets for buttons should maintain a minimum 44px height; the observed button padding (`13px` block, `20px` inline) approximates but does not guarantee this on all devices. Mobile nav collapse and drawer behavior are proposed, not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS and text extraction only; no rendered layout, interaction states (hover/focus/active), or JavaScript-driven behavior (e.g., quiz flow, cart drawer) were observed. Color role assignments (ink, muted, hairline, surface-card) are inferred from usage context in the supplied CSS/JS variables and may not reflect final designer intent. Body copy typography (Montserrat/Helvetica Neue) is inferred from the font-family list; no CSS rule directly ties a body font to paragraph text. Font availability, licensing, and self-hosting terms for "Athletics-Medium," "Larsseit," and "Monosten" were not verified. Spacing and rounded-corner scales beyond the directly observed `20px` product-image radius are proposed conventions, not extracted values. Mobile/tablet layout, breakpoint pixel values, and navigation collapse patterns are recommendations only.
