---
version: alpha
name: "Hatch"
source_url: "https://hatch.co"
captured_at: "2026-09-28T09:39:44.984671+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Hatch's public site pairs a warm, paper-like canvas (#faf8f4, #f1ebe1) with a deep navy anchor color drawn from CSS custom properties such as --hdc-navy-1000, used for primary buttons, the nav submit action, and product name text. Observed hex values in the surrounding palette (#13294b, #0a1a34, #274d7b, #040f1f) form a plausible navy family; #13294b is proposed as the resolved primary since it sits mid-scale and pairs cleanly with white text. Neutral UI grays (#111827, #374151, #6b7280, #e5e7eb) handle body copy, muted labels, and hairlines, consistent with a Tailwind-influenced utility system layered under a custom design language. A terracotta accent (#b5541a) and soft tan (#e3d5c5) appear in the palette and are inferred as a secondary/warm accent for badges or highlights, not confirmed as primary brand color. Typography relies on three custom font families declared in :root — ttCommonsPro (default UI text), enfantine, and exposure (both likely display/editorial faces) — each with explicit fallback tokens, generic sans/serif fallbacks are assumed since none were declared. Rounded values span pill-shaped shop buttons (100px), 16px back-buttons, and 8px submit buttons, all directly observed in CSS.

colors:
  primary: "#13294b"
  ink: "#111827"
  canvas: "#ffffff"
  body: "#374151"
  muted: "#6b7280"
  hairline: "#e5e7eb"
  surface-soft: "#faf8f4"
  surface-card: "#f1ebe1"
  on-primary: "#ffffff"
  accent: "#b5541a"
  accent-soft: "#e3d5c5"
  disabled: "#9ca3af"
  navy-deep: "#0a1a34"
typography:
  display-xl: {fontFamily: "exposure, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "exposure, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "ttCommonsPro, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "ttCommonsPro, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  body-sm: {fontFamily: "ttCommonsPro, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  caption: {fontFamily: "ttCommonsPro, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  button-md: {fontFamily: "ttCommonsPro, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 1.25px}
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
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    height: 64px
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    titleColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    metaColor: "{colors.muted}"
    metaTypography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.accent}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  audio-feature-card:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** models the observed `.style-module__2dB7tG__submitButton` pattern: navy background, white text, 8px radius, full-width capable. Used for cart/email-signup submit actions.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Learn More" links); not directly observed but inferred from the pill-shaped `shopButtonInner` (100px radius) which suggests a rounded secondary CTA family alongside the squarer primary button.

**text-input** is proposed for the newsletter/email capture field referenced in page text ("Sign up to get sleep tips"); border and radius values are estimated from the surrounding hairline and sm-radius tokens since no explicit input CSS was supplied.

**nav-bar** reflects `.header-module__5y7adq__navBar`, a 64px-tall grid header with white background and grid-gap 8px, holding logo, product nav, and cart icon.

**product-card** draws from `.style-module__9aXxYa__productName/productTagline/productPrice` and `.style-module__IpXK2a__productLabel/productName/productPrice` selectors: navy product title, muted 12–14px meta text, used in nav dropdown product previews and likely reused on shop listing pages (layout not confirmed).

**hero** is a proposed pattern for the homepage "Meet Hatch Sleep Clock" banner described in page text; warm canvas background and large display type are inferred from brand tone, not measured hero CSS.

**footer** is proposed using the darkest navy as background per the copyright/legal link list observed in page text (Privacy Policy, Careers, Support, etc.); actual footer styling was not present in supplied CSS.

**badge** is a proposed small pill using the terracotta accent pairing, suitable for "New," "Refurbished," or "Sale" labels seen in shop navigation (e.g., "Hatch Refurbished").

**search** is a proposed rounded search affordance; no search CSS was supplied, so radius and color are inferred from other pill-shaped controls on the site.

**audio-feature-card** is a category-appropriate component for the "Original Audio" sleep-sound library section (sound baths, meditations, podcasts) mentioned in page text; dark navy card with white text is proposed to visually separate audio content from product cards.

## Responsive Behavior

Recommended (not measured) breakpoints: mobile ≤480px, tablet 481–768px, desktop 769–1200px, wide ≥1201px. The 64px nav height should collapse into a hamburger/back-button pattern below tablet width, consistent with the observed `.style-module__IpXK2a__backButton` mobile-nav-return control. Touch targets should be ≥44px; button-primary's 52px height (seen in `.submitButton`) already satisfies this. Product-card grids are recommended to reflow from multi-column to single-column stacking under 768px. This section is a proposed recommendation only; no live responsive behavior was observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is derived solely from static CSS module fragments, a color list, and page text — no rendered layout, computed styles, or DOM structure were observed. Semantic role assignments (primary, ink, muted, hairline, accent) are inferred from selector names and usage context, not confirmed via visual inspection. Exact hex values for `--hdc-navy-1000`, `--hdc-neutral-400`, and `--hdc-gray-40` were not explicitly resolved in the evidence; best-fit palette matches are used and labeled inferred. Font availability, weights, and licensing for ttCommonsPro, enfantine, and exposure were not verified — generic fallbacks are appended defensively. All typography sizes beyond the explicitly observed 12/14/16/20px values are proposed estimates for scale consistency. Hover, focus, error, and loading states, along with actual mobile navigation behavior, were not present in the supplied CSS and are marked proposed throughout.
